#!/usr/bin/env python3
"""
MEMS Spring-Mass-Damper System Simulation
==========================================

Simulates the dynamics of a MEMS accelerometer modeled as a
spring-mass-damper system with capacitive sensing.

Features:
    - Time-domain response to acceleration
    - Frequency response (Bode plot)
    - Noise analysis
    - Design space exploration
    - Capacitive readout simulation

Author: Silicon Fabrication Handbook
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from pathlib import Path

# Create output directory for plots
OUTPUT_DIR = Path("images")
OUTPUT_DIR.mkdir(exist_ok=True)

# Plot style
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 10


class MEMSAccelerometer:
    """
    MEMS accelerometer spring-mass-damper model.
    
    Parameters:
        m (float): Proof mass [kg]
        k (float): Spring constant [N/m]
        b (float): Damping coefficient [N·s/m]
        C0 (float): Nominal capacitance [F]
        d0 (float): Nominal gap [m]
        A (float): Electrode area [m²]
    """
    
    def __init__(self, m=1e-9, k=10, b=1e-6, C0=1e-12, d0=2e-6, A=1e-8):
        self.m = m  # Mass (typical: 1 ng)
        self.k = k  # Spring constant (typical: 10 N/m)
        self.b = b  # Damping (typical: 1 µN·s/m)
        self.C0 = C0  # Capacitance (1 pF)
        self.d0 = d0  # Gap (2 µm)
        self.A = A  # Area (100 µm²)
        
        # Derived parameters
        self.omega_n = np.sqrt(k / m)  # Natural frequency [rad/s]
        self.f_n = self.omega_n / (2 * np.pi)  # Natural frequency [Hz]
        self.zeta = b / (2 * np.sqrt(m * k))  # Damping ratio
        self.Q = 1 / (2 * self.zeta)  # Quality factor
        
        # Sensitivity
        self.sensitivity = 1 / (k / m)  # Displacement per g [m/g]
        
        print(f"MEMS Accelerometer Parameters:")
        print(f"  Mass (m): {m*1e9:.2f} ng")
        print(f"  Spring constant (k): {k:.2f} N/m")
        print(f"  Damping (b): {b*1e6:.3f} µN·s/m")
        print(f"  Natural frequency: {self.f_n/1e3:.2f} kHz")
        print(f"  Damping ratio (ζ): {self.zeta:.3f}")
        print(f"  Quality factor (Q): {self.Q:.1f}")
        print(f"  Sensitivity: {self.sensitivity*1e9:.2f} nm/g")
        print()
    
    def transfer_function(self):
        """Return transfer function H(s) = X(s)/A(s)"""
        # H(s) = 1 / (s² + 2ζω_n·s + ω_n²)
        num = [1]
        den = [1, 2*self.zeta*self.omega_n, self.omega_n**2]
        return signal.TransferFunction(num, den)
    
    def step_response(self, acceleration=9.81, t_max=0.01, n_points=1000):
        """
        Simulate step response to constant acceleration.
        
        Args:
            acceleration: Applied acceleration [m/s²]
            t_max: Simulation time [s]
            n_points: Number of time points
        
        Returns:
            t, x: Time array and displacement array
        """
        sys = self.transfer_function()
        t = np.linspace(0, t_max, n_points)
        
        # Step response
        t_step, x = signal.step(sys, T=t)
        
        # Scale by acceleration
        x = x * acceleration
        
        return t_step, x
    
    def frequency_response(self, f_min=1, f_max=1e6, n_points=1000):
        """
        Calculate frequency response (Bode plot).
        
        Args:
            f_min: Minimum frequency [Hz]
            f_max: Maximum frequency [Hz]
            n_points: Number of frequency points
        
        Returns:
            f, H: Frequency array and transfer function magnitude
        """
        sys = self.transfer_function()
        w = 2 * np.pi * np.logspace(np.log10(f_min), np.log10(f_max), n_points)
        w, H = signal.freqs(sys.num, sys.den, worN=w)
        f = w / (2 * np.pi)
        
        return f, np.abs(H)
    
    def displacement_to_capacitance(self, x):
        """
        Convert displacement to capacitance change.
        
        C = ε₀·A / (d₀ - x)
        ΔC ≈ C₀·x/d₀ (for small x)
        
        Args:
            x: Displacement [m]
        
        Returns:
            C: Capacitance [F]
        """
        epsilon_0 = 8.854e-12  # Permittivity of free space
        C = epsilon_0 * self.A / (self.d0 - x)
        return C
    
    def capacitance_to_voltage(self, C, V_bias=1.0):
        """
        Convert capacitance to voltage using charge amplifier.
        
        V_out = -V_bias · ΔC/C_f
        
        Args:
            C: Capacitance [F]
            V_bias: Bias voltage [V]
        
        Returns:
            V_out: Output voltage [V]
        """
        C_f = 1e-12  # Feedback capacitance (1 pF)
        delta_C = C - self.C0
        V_out = -V_bias * delta_C / C_f
        return V_out


def simulate_step_response(accelerometer, save_plot=True):
    """Simulate and plot step response."""
    print("Simulating step response to 1g acceleration...")
    
    # Simulate
    t, x = accelerometer.step_response(acceleration=9.81, t_max=0.01)
    
    # Convert to nm
    x_nm = x * 1e9
    
    # Settling time (2% criterion)
    steady_state = x_nm[-1]
    settling_idx = np.where(np.abs(x_nm - steady_state) < 0.02 * steady_state)[0][0]
    settling_time = t[settling_idx]
    
    # Plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Displacement
    ax1.plot(t * 1e3, x_nm, 'b-', linewidth=2, label='Displacement')
    ax1.axhline(steady_state, color='r', linestyle='--', label=f'Steady state: {steady_state:.2f} nm')
    ax1.axvline(settling_time * 1e3, color='g', linestyle='--', label=f'Settling time: {settling_time*1e3:.2f} ms')
    ax1.set_xlabel('Time [ms]')
    ax1.set_ylabel('Displacement [nm]')
    ax1.set_title('Step Response to 1g Acceleration')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Capacitance change
    C = accelerometer.displacement_to_capacitance(x)
    delta_C_fF = (C - accelerometer.C0) * 1e15
    ax2.plot(t * 1e3, delta_C_fF, 'r-', linewidth=2)
    ax2.set_xlabel('Time [ms]')
    ax2.set_ylabel('Capacitance Change [fF]')
    ax2.set_title('Capacitive Sensor Response')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_plot:
        output_file = OUTPUT_DIR / "step_response.png"
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"✓ Saved: {output_file}")
    
    plt.show()
    
    print(f"  Steady-state displacement: {steady_state:.2f} nm")
    print(f"  Settling time (2%): {settling_time*1e3:.2f} ms")
    print()


def simulate_frequency_response(accelerometer, save_plot=True):
    """Simulate and plot frequency response (Bode plot)."""
    print("Calculating frequency response...")
    
    # Calculate
    f, H = accelerometer.frequency_response(f_min=10, f_max=1e6, n_points=1000)
    
    # Magnitude and phase
    mag_dB = 20 * np.log10(H)
    phase = np.angle(H * 2 * np.pi * f, deg=True)
    
    # -3dB bandwidth
    mag_max = np.max(mag_dB)
    bw_idx = np.where(mag_dB >= mag_max - 3)[0]
    bandwidth = f[bw_idx[-1]]
    
    # Plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Magnitude
    ax1.semilogx(f, mag_dB, 'b-', linewidth=2)
    ax1.axhline(mag_max - 3, color='r', linestyle='--', label='-3dB line')
    ax1.axvline(bandwidth, color='g', linestyle='--', label=f'BW: {bandwidth/1e3:.1f} kHz')
    ax1.axvline(accelerometer.f_n, color='orange', linestyle=':', label=f'f_n: {accelerometer.f_n/1e3:.1f} kHz')
    ax1.set_ylabel('Magnitude [dB]')
    ax1.set_title('Frequency Response (Bode Plot)')
    ax1.legend()
    ax1.grid(True, alpha=0.3, which='both')
    
    # Phase
    ax2.semilogx(f, phase, 'r-', linewidth=2)
    ax2.set_xlabel('Frequency [Hz]')
    ax2.set_ylabel('Phase [degrees]')
    ax2.grid(True, alpha=0.3, which='both')
    
    plt.tight_layout()
    
    if save_plot:
        output_file = OUTPUT_DIR / "frequency_response.png"
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"✓ Saved: {output_file}")
    
    plt.show()
    
    print(f"  -3dB Bandwidth: {bandwidth/1e3:.1f} kHz")
    print(f"  Resonant peak: {mag_max:.1f} dB")
    print()


def simulate_noise_analysis(accelerometer, save_plot=True):
    """Analyze noise sources and total noise."""
    print("Performing noise analysis...")
    
    # Frequency range
    f = np.logspace(0, 6, 1000)  # 1 Hz to 1 MHz
    
    # Thermal (Brownian) noise
    k_B = 1.38e-23  # Boltzmann constant
    T = 300  # Temperature [K]
    
    # Displacement noise spectral density [m/√Hz]
    S_x_thermal = np.sqrt(4 * k_B * T * accelerometer.b / accelerometer.k**2)
    x_thermal = S_x_thermal * np.ones_like(f)
    
    # Convert to acceleration noise [g/√Hz]
    a_thermal = x_thermal * accelerometer.k / accelerometer.m / 9.81
    
    # Electronic noise (charge amplifier)
    # Johnson noise from feedback resistor
    R_f = 1e9  # Feedback resistor [Ω]
    C_f = 1e-12  # Feedback capacitor [F]
    v_n_amplifier = np.sqrt(4 * k_B * T * R_f)  # V/√Hz
    
    # Convert to equivalent acceleration
    V_bias = 1.0
    sens_V_per_g = V_bias * accelerometer.C0 / C_f / accelerometer.d0 * accelerometer.sensitivity
    a_electronic = v_n_amplifier / sens_V_per_g / 9.81
    a_electronic = a_electronic * np.ones_like(f)
    
    # Total noise
    a_total = np.sqrt(a_thermal**2 + a_electronic**2)
    
    # Integrate over bandwidth to get RMS noise
    bandwidth = 100  # Hz
    f_bw = f[f <= bandwidth]
    a_total_bw = a_total[f <= bandwidth]
    noise_rms = np.sqrt(np.trapz(a_total_bw**2, f_bw))
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.loglog(f, a_thermal * 1e6, 'b-', linewidth=2, label='Thermal (Brownian) noise')
    ax.loglog(f, a_electronic * 1e6, 'r-', linewidth=2, label='Electronic noise')
    ax.loglog(f, a_total * 1e6, 'k-', linewidth=2, label='Total noise')
    ax.axvline(bandwidth, color='g', linestyle='--', label=f'Bandwidth: {bandwidth} Hz')
    
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Noise Spectral Density [µg/√Hz]')
    ax.set_title('Noise Analysis')
    ax.legend()
    ax.grid(True, alpha=0.3, which='both')
    
    plt.tight_layout()
    
    if save_plot:
        output_file = OUTPUT_DIR / "noise_analysis.png"
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"✓ Saved: {output_file}")
    
    plt.show()
    
    print(f"  Thermal noise: {a_thermal[0]*1e6:.2f} µg/√Hz")
    print(f"  Electronic noise: {a_electronic[0]*1e6:.2f} µg/√Hz")
    print(f"  Total noise: {a_total[0]*1e6:.2f} µg/√Hz")
    print(f"  RMS noise (0-{bandwidth} Hz): {noise_rms*1e6:.2f} µg")
    print()


def design_space_exploration(save_plot=True):
    """Explore design trade-offs."""
    print("Exploring design space...")
    
    # Vary mass and spring constant
    masses = np.logspace(-10, -8, 50)  # 0.1 ng to 10 ng
    spring_constants = np.logspace(0, 2, 50)  # 1 to 100 N/m
    
    M, K = np.meshgrid(masses, spring_constants)
    
    # Calculate metrics
    f_n = np.sqrt(K / M) / (2 * np.pi)  # Natural frequency
    sensitivity = M / K * 9.81 * 1e9  # Sensitivity [nm/g]
    
    # Thermal noise (simplified)
    k_B = 1.38e-23
    T = 300
    b = 1e-6  # Fixed damping
    noise = np.sqrt(4 * k_B * T * b / K**2) * K / M / 9.81 * 1e6  # µg/√Hz
    
    # Plot
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    # Natural frequency
    c1 = axes[0].contourf(M * 1e9, K, f_n / 1e3, levels=20, cmap='viridis')
    axes[0].set_xlabel('Mass [ng]')
    axes[0].set_ylabel('Spring Constant [N/m]')
    axes[0].set_title('Natural Frequency [kHz]')
    axes[0].set_xscale('log')
    axes[0].set_yscale('log')
    plt.colorbar(c1, ax=axes[0])
    
    # Sensitivity
    c2 = axes[1].contourf(M * 1e9, K, sensitivity, levels=20, cmap='plasma')
    axes[1].set_xlabel('Mass [ng]')
    axes[1].set_ylabel('Spring Constant [N/m]')
    axes[1].set_title('Sensitivity [nm/g]')
    axes[1].set_xscale('log')
    axes[1].set_yscale('log')
    plt.colorbar(c2, ax=axes[1])
    
    # Noise
    c3 = axes[2].contourf(M * 1e9, K, noise, levels=20, cmap='coolwarm')
    axes[2].set_xlabel('Mass [ng]')
    axes[2].set_ylabel('Spring Constant [N/m]')
    axes[2].set_title('Thermal Noise [µg/√Hz]')
    axes[2].set_xscale('log')
    axes[2].set_yscale('log')
    plt.colorbar(c3, ax=axes[2])
    
    plt.tight_layout()
    
    if save_plot:
        output_file = OUTPUT_DIR / "design_space.png"
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"✓ Saved: {output_file}")
    
    plt.show()
    print()


def simulate_transient_acceleration(accelerometer, save_plot=True):
    """Simulate response to time-varying acceleration."""
    print("Simulating transient acceleration (sine wave)...")
    
    # Time vector
    t = np.linspace(0, 0.02, 2000)  # 20 ms
    
    # Input: 1g sine wave at 500 Hz
    f_input = 500  # Hz
    a_input = 9.81 * np.sin(2 * np.pi * f_input * t)
    
    # Simulate using lsim
    sys = accelerometer.transfer_function()
    t, x, _ = signal.lsim(sys, a_input, t)
    
    # Convert to capacitance and voltage
    C = accelerometer.displacement_to_capacitance(x)
    V_out = accelerometer.capacitance_to_voltage(C)
    
    # Plot
    fig, axes = plt.subplots(3, 1, figsize=(10, 10))
    
    # Input acceleration
    axes[0].plot(t * 1e3, a_input / 9.81, 'b-', linewidth=2)
    axes[0].set_ylabel('Acceleration [g]')
    axes[0].set_title('Input: 1g Sine Wave at 500 Hz')
    axes[0].grid(True, alpha=0.3)
    
    # Displacement
    axes[1].plot(t * 1e3, x * 1e9, 'r-', linewidth=2)
    axes[1].set_ylabel('Displacement [nm]')
    axes[1].set_title('Proof Mass Displacement')
    axes[1].grid(True, alpha=0.3)
    
    # Output voltage
    axes[2].plot(t * 1e3, V_out * 1e3, 'g-', linewidth=2)
    axes[2].set_xlabel('Time [ms]')
    axes[2].set_ylabel('Output Voltage [mV]')
    axes[2].set_title('Capacitive Readout Signal')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_plot:
        output_file = OUTPUT_DIR / "transient_response.png"
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"✓ Saved: {output_file}")
    
    plt.show()
    
    print(f"  Peak displacement: {np.max(np.abs(x))*1e9:.2f} nm")
    print(f"  Peak output voltage: {np.max(np.abs(V_out))*1e3:.2f} mV")
    print()


def main():
    """Run all simulations."""
    print("=" * 60)
    print("MEMS Spring-Mass-Damper System Simulation")
    print("=" * 60)
    print()
    
    # Create accelerometer instance
    # Typical MEMS accelerometer parameters
    accel = MEMSAccelerometer(
        m=1e-9,      # 1 ng proof mass
        k=10,        # 10 N/m spring constant
        b=1e-6,      # 1 µN·s/m damping
        C0=1e-12,    # 1 pF nominal capacitance
        d0=2e-6,     # 2 µm gap
        A=1e-8       # 100 µm² electrode area
    )
    
    # Run simulations
    simulate_step_response(accel)
    simulate_frequency_response(accel)
    simulate_noise_analysis(accel)
    simulate_transient_acceleration(accel)
    design_space_exploration()
    
    print("=" * 60)
    print("All simulations complete!")
    print(f"Plots saved to: {OUTPUT_DIR}/")
    print("=" * 60)


if __name__ == "__main__":
    main()