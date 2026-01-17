#!/usr/bin/env python3
"""
MEMS Spring-Mass System Simulator
==================================

This script simulates a MEMS accelerometer using a spring-mass-damper model.
It calculates resonant frequency, quality factor, displacement response,
and visualizes the frequency response.

Author: Silicon Fabrication Handbook Contributors
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import signal
from scipy.integrate import odeint

OUTPUT_DIR = Path(__file__).resolve().parents[2] / "images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Physical constants
RHO_SI = 2329  # Silicon density [kg/m³]
E_SI = 169e9   # Young's modulus for Si <100> [Pa]
NU_SI = 0.064  # Poisson's ratio for Si

class MEMSAccelerometer:
    """
    Model for a MEMS comb-drive accelerometer
    
    Attributes:
        mass: Proof mass [kg]
        k_spring: Spring constant [N/m]
        b_damping: Damping coefficient [N·s/m]
        Q: Quality factor (dimensionless)
        omega_n: Natural frequency [rad/s]
        f_n: Natural frequency [Hz]
    """
    
    def __init__(self, length, width, thickness, n_springs=4, 
                 spring_length=200e-6, spring_width=2e-6, pressure=1e5):
        """
        Initialize MEMS accelerometer with geometric parameters
        
        Args:
            length: Proof mass length [m]
            width: Proof mass width [m]
            thickness: Structural layer thickness [m]
            n_springs: Number of folded springs
            spring_length: Length of one spring beam [m]
            spring_width: Width of spring beam [m]
            pressure: Ambient pressure [Pa] (affects damping)
        """
        # Calculate proof mass
        volume = length * width * thickness
        self.mass = RHO_SI * volume
        
        # Calculate spring constant (folded beam spring)
        # For a cantilever beam: k = (E * w * t³) / (4 * L³)
        k_single = (E_SI * spring_width * thickness**3) / (4 * spring_length**3)
        self.k_spring = n_springs * k_single
        
        # Calculate damping (squeeze-film damping)
        # Simplified model: b = (μ * A²) / (h³) where h is gap
        mu = 1.81e-5  # Air viscosity [Pa·s] at 20°C
        gap = 2e-6    # Typical gap spacing [m]
        area = length * width
        
        # Couette flow damping (parallel plates)
        self.b_damping = (mu * area**2) / (gap**3) * (pressure / 1e5)
        
        # Calculate resonant frequency
        self.omega_n = np.sqrt(self.k_spring / self.mass)
        self.f_n = self.omega_n / (2 * np.pi)
        
        # Calculate quality factor
        self.Q = (self.mass * self.omega_n) / self.b_damping
        
        # Store geometry for reference
        self.geometry = {
            'mass_length': length,
            'mass_width': width,
            'thickness': thickness,
            'spring_length': spring_length,
            'spring_width': spring_width
        }
    
    def frequency_response(self, freq_range):
        """
        Calculate displacement amplitude vs frequency for 1g acceleration
        
        Args:
            freq_range: Array of frequencies [Hz]
            
        Returns:
            displacement: Array of displacement amplitudes [m]
            phase: Array of phase angles [degrees]
        """
        g = 9.81  # Acceleration due to gravity [m/s²]
        F0 = self.mass * g  # Force amplitude for 1g
        
        omega = 2 * np.pi * freq_range
        
        # Transfer function: X(ω) = F0 / sqrt((k - m*ω²)² + (b*ω)²)
        denominator = np.sqrt((self.k_spring - self.mass * omega**2)**2 + 
                             (self.b_damping * omega)**2)
        displacement = F0 / denominator
        
        # Phase: φ = arctan(b*ω / (k - m*ω²))
        phase = np.arctan2(self.b_damping * omega, 
                           self.k_spring - self.mass * omega**2)
        phase_deg = np.degrees(phase)
        
        return displacement, phase_deg
    
    def time_response(self, acceleration_input, time_vec):
        """
        Simulate time-domain response to arbitrary acceleration input
        
        Args:
            acceleration_input: Array of acceleration values [m/s²]
            time_vec: Time vector [s]
            
        Returns:
            displacement: Position response [m]
            velocity: Velocity response [m/s]
        """
        # State-space representation: [x, v]' = [v, (F - b*v - k*x)/m]'
        def dynamics(state, t, accel_func):
            x, v = state
            a_input = accel_func(t)
            F = self.mass * a_input
            dv_dt = (F - self.b_damping * v - self.k_spring * x) / self.mass
            return [v, dv_dt]
        
        # Interpolate acceleration input
        from scipy.interpolate import interp1d
        accel_func = interp1d(time_vec, acceleration_input, 
                             kind='linear', fill_value='extrapolate')
        
        # Solve ODE
        initial_state = [0.0, 0.0]
        solution = odeint(dynamics, initial_state, time_vec, args=(accel_func,))
        
        displacement = solution[:, 0]
        velocity = solution[:, 1]
        
        return displacement, velocity
    
    def sensitivity(self):
        """
        Calculate static sensitivity (displacement per g)
        
        Returns:
            sensitivity: Displacement per 1g [m/g or μm/g]
        """
        g = 9.81
        F = self.mass * g
        x = F / self.k_spring  # Static displacement
        return x, x * 1e6  # Return in [m] and [μm]
    
    def print_specs(self):
        """Print device specifications"""
        sens_m, sens_um = self.sensitivity()
        
        print("=" * 60)
        print("MEMS Accelerometer Specifications")
        print("=" * 60)
        print(f"Proof Mass:          {self.mass * 1e9:.3f} ng")
        print(f"Spring Constant:     {self.k_spring:.3f} N/m")
        print(f"Damping Coefficient: {self.b_damping * 1e6:.3f} μN·s/m")
        print(f"Resonant Frequency:  {self.f_n / 1e3:.3f} kHz")
        print(f"Quality Factor:      {self.Q:.1f}")
        print(f"Sensitivity:         {sens_um:.3f} μm/g")
        print(f"3dB Bandwidth:       {self.f_n / self.Q / 1e3:.3f} kHz")
        print("=" * 60)
        print("\nGeometry:")
        for key, val in self.geometry.items():
            print(f"  {key}: {val * 1e6:.2f} μm")
        print("=" * 60)


def plot_frequency_response(accelerometer):
    """Generate frequency response plots"""
    # Frequency range: 0.1 Hz to 10x resonant frequency
    f_min = 0.1
    f_max = 10 * accelerometer.f_n
    freq = np.logspace(np.log10(f_min), np.log10(f_max), 1000)
    
    displacement, phase = accelerometer.frequency_response(freq)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Magnitude plot
    ax1.loglog(freq, displacement * 1e9, 'b-', linewidth=2)
    ax1.axvline(accelerometer.f_n, color='r', linestyle='--', 
                label=f'$f_n$ = {accelerometer.f_n/1e3:.2f} kHz')
    ax1.grid(True, which='both', alpha=0.3)
    ax1.set_xlabel('Frequency [Hz]', fontsize=12)
    ax1.set_ylabel('Displacement [nm/g]', fontsize=12)
    ax1.set_title('MEMS Accelerometer Frequency Response', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    
    # Phase plot
    ax2.semilogx(freq, phase, 'g-', linewidth=2)
    ax2.axvline(accelerometer.f_n, color='r', linestyle='--')
    ax2.axhline(-90, color='k', linestyle=':', alpha=0.5)
    ax2.grid(True, which='both', alpha=0.3)
    ax2.set_xlabel('Frequency [Hz]', fontsize=12)
    ax2.set_ylabel('Phase [degrees]', fontsize=12)
    ax2.set_ylim([-180, 0])
    
    plt.tight_layout()
    return fig


def plot_step_response(accelerometer):
    """Simulate step response to sudden 1g acceleration"""
    # Time vector: 0 to 10 periods of natural frequency
    t_end = 10 / accelerometer.f_n
    time = np.linspace(0, t_end, 2000)
    
    # Step input: 0g → 1g at t=0
    g = 9.81
    accel_input = g * np.ones_like(time)
    
    displacement, velocity = accelerometer.time_response(accel_input, time)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Displacement
    ax1.plot(time * 1e3, displacement * 1e9, 'b-', linewidth=2)
    ax1.axhline(accelerometer.sensitivity()[1], color='r', linestyle='--',
                label=f'Static Sensitivity = {accelerometer.sensitivity()[1]:.3f} μm/g')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('Time [ms]', fontsize=12)
    ax1.set_ylabel('Displacement [nm]', fontsize=12)
    ax1.set_title('Step Response (1g Acceleration)', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    
    # Velocity
    ax2.plot(time * 1e3, velocity * 1e3, 'g-', linewidth=2)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('Time [ms]', fontsize=12)
    ax2.set_ylabel('Velocity [mm/s]', fontsize=12)
    
    plt.tight_layout()
    return fig


def plot_shock_response(accelerometer):
    """Simulate response to shock pulse"""
    # Time vector
    t_end = 10 / accelerometer.f_n
    time = np.linspace(0, t_end, 2000)
    
    # Half-sine shock pulse: 100g peak, 0.5ms duration
    g = 9.81
    t_shock = 0.5e-3
    shock_accel = np.where(time < t_shock, 
                          100 * g * np.sin(np.pi * time / t_shock),
                          0)
    
    displacement, velocity = accelerometer.time_response(shock_accel, time)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Input acceleration
    ax1.plot(time * 1e3, shock_accel / g, 'r-', linewidth=2)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('Time [ms]', fontsize=12)
    ax1.set_ylabel('Acceleration [g]', fontsize=12)
    ax1.set_title('Shock Input and Response', fontsize=14, fontweight='bold')
    
    # Displacement response
    ax2.plot(time * 1e3, displacement * 1e6, 'b-', linewidth=2)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('Time [ms]', fontsize=12)
    ax2.set_ylabel('Displacement [μm]', fontsize=12)
    
    plt.tight_layout()
    return fig


# Example usage and main script
if __name__ == "__main__":
    print("\n" + "="*60)
    print("MEMS ACCELEROMETER SIMULATION")
    print("="*60 + "\n")
    
    # Define typical MEMS accelerometer geometry
    # These values are representative of a commercial device
    accel = MEMSAccelerometer(
        length=500e-6,        # 500 μm proof mass
        width=500e-6,         # 500 μm proof mass
        thickness=10e-6,      # 10 μm structural polysilicon
        n_springs=4,          # 4 folded springs
        spring_length=200e-6, # 200 μm spring beams
        spring_width=2e-6,    # 2 μm beam width
        pressure=1e5          # Atmospheric pressure (1 bar)
    )
    
    # Print specifications
    accel.print_specs()
    
    # Generate plots
    print("\nGenerating frequency response plot...")
    fig1 = plot_frequency_response(accel)
    
    print("Generating step response plot...")
    fig2 = plot_step_response(accel)
    
    print("Generating shock response plot...")
    fig3 = plot_shock_response(accel)
    
    # Save figures
    output_frequency = OUTPUT_DIR / "frequency_response.png"
    output_step = OUTPUT_DIR / "step_response.png"
    output_shock = OUTPUT_DIR / "shock_response.png"

    fig1.savefig(output_frequency, dpi=300, bbox_inches='tight')
    fig2.savefig(output_step, dpi=300, bbox_inches='tight')
    fig3.savefig(output_shock, dpi=300, bbox_inches='tight')
    
    print("\n✓ Plots saved successfully!")
    print(f"  - {output_frequency}")
    print(f"  - {output_step}")
    print(f"  - {output_shock}")
    
    # Display plots
    plt.show()
    
    print("\n" + "="*60)
    print("Simulation complete!")
    print("="*60 + "\n")


# Additional utility functions
def compare_designs():
    """Compare multiple accelerometer designs"""
    designs = {
        'High Sensitivity': MEMSAccelerometer(600e-6, 600e-6, 10e-6, 4, 300e-6, 1.5e-6),
        'High Frequency': MEMSAccelerometer(200e-6, 200e-6, 10e-6, 4, 100e-6, 4e-6),
        'Balanced': MEMSAccelerometer(400e-6, 400e-6, 10e-6, 4, 200e-6, 2e-6)
    }
    
    plt.figure(figsize=(12, 6))
    
    for name, design in designs.items():
        freq = np.logspace(1, 6, 1000)
        disp, _ = design.frequency_response(freq)
        plt.loglog(freq, disp * 1e9, linewidth=2, label=f'{name} (fn={design.f_n/1e3:.1f}kHz, Q={design.Q:.1f})')
    
    plt.grid(True, which='both', alpha=0.3)
    plt.xlabel('Frequency [Hz]', fontsize=12)
    plt.ylabel('Displacement [nm/g]', fontsize=12)
    plt.title('Comparison of Accelerometer Designs', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.tight_layout()
    output_comparison = OUTPUT_DIR / "design_comparison.png"
    plt.savefig(output_comparison, dpi=300, bbox_inches='tight')
    plt.show()


def noise_analysis(accelerometer):
    """
    Calculate noise floor (Brownian motion)
    """
    k_B = 1.38e-23  # Boltzmann constant [J/K]
    T = 300         # Temperature [K]
    
    # Thermomechanical noise PSD: S_x = (4 * k_B * T * b) / (k² * ω²)
    # At resonance: x_rms = sqrt(k_B * T / k)
    
    x_thermal = np.sqrt(k_B * T / accelerometer.k_spring)
    a_thermal = x_thermal * accelerometer.omega_n**2  # Acceleration noise
    
    # Convert to μg/√Hz
    g = 9.81
    noise_density = a_thermal / g * 1e6 * np.sqrt(accelerometer.f_n / 2)
    
    print(f"\nNoise Analysis:")
    print(f"  Thermal displacement noise: {x_thermal * 1e12:.3f} pm RMS")
    print(f"  Acceleration noise density: {noise_density:.3f} μg/√Hz")
    print(f"  Resolution (1 Hz BW):       {noise_density:.3f} μg")
    
    return noise_density
