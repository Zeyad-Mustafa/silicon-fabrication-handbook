#!/usr/bin/env python3
"""
Thermal Actuator Analytical Model
==================================

This script provides a simplified analytical model of a V-beam thermal actuator
for users who don't have access to COMSOL Multiphysics. While not as accurate
as FEA, it gives good first-order estimates for preliminary design.

The model includes:
- Electrical resistance calculation
- Thermal analysis (1D approximation)
- Thermal expansion displacement
- Stress estimation
- Parametric design sweeps

Author: Silicon Fabrication Handbook
License: MIT
Date: January 2026
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ============================================================================
# MATERIAL PROPERTIES (Polysilicon)
# ============================================================================

class Material:
    """Doped polysilicon material properties"""
    def __init__(self):
        self.rho_elec = 2e-5        # Electrical resistivity [Ω·m]
        self.k_thermal = 34         # Thermal conductivity [W/m·K]
        self.alpha = 2.6e-6         # Coefficient of thermal expansion [1/K]
        self.E = 169e9              # Young's modulus [Pa]
        self.nu = 0.22              # Poisson's ratio
        self.rho_mass = 2329        # Density [kg/m³]
        self.Cp = 712               # Specific heat [J/kg·K]
        self.sigma_yield = 7e9      # Yield strength [Pa]

# ============================================================================
# THERMAL ACTUATOR CLASS
# ============================================================================

class ThermalActuator:
    """V-beam thermal actuator analytical model"""
    
    def __init__(self, L=200e-6, w=4e-6, t=2e-6, theta=2, V=3.0, 
                 T_amb=293.15, h_conv=10):
        """
        Initialize thermal actuator
        
        Parameters:
        -----------
        L : float
            Beam length [m] (default: 200 μm)
        w : float
            Beam width [m] (default: 4 μm)
        t : float
            Beam thickness [m] (default: 2 μm)
        theta : float
            V-angle in degrees (default: 2°)
        V : float
            Applied voltage [V] (default: 3 V)
        T_amb : float
            Ambient temperature [K] (default: 293.15 K / 20°C)
        h_conv : float
            Convection coefficient [W/m²·K] (default: 10)
        """
        self.L = L
        self.w = w
        self.t = t
        self.theta = np.deg2rad(theta)
        self.V = V
        self.T_amb = T_amb
        self.h_conv = h_conv
        
        self.mat = Material()
        
        # Derived geometric parameters
        self.A = w * t                          # Cross-sectional area
        self.I = w * t**3 / 12                  # Moment of inertia
        self.L_horiz = L * np.cos(self.theta)   # Horizontal projection
        self.L_vert = L * np.sin(self.theta)    # Vertical offset
        self.perimeter = 2 * (w + t)            # Perimeter for convection
        
        # Results storage
        self.results = {}
        
    def electrical_analysis(self):
        """Calculate electrical resistance, current, and power"""
        # Single beam resistance
        R_beam = self.mat.rho_elec * self.L / self.A
        
        # Total resistance (2 beams in series)
        R_total = 2 * R_beam
        
        # Current (Ohm's law)
        I = self.V / R_total
        
        # Power dissipation
        P_total = self.V * I
        P_beam = P_total / 2  # Per beam
        
        # Power density (volumetric)
        q_vol = P_beam / (self.L * self.A)
        
        self.results['R_beam'] = R_beam
        self.results['R_total'] = R_total
        self.results['I'] = I
        self.results['P_total'] = P_total
        self.results['P_beam'] = P_beam
        self.results['q_vol'] = q_vol
        
        return R_total, I, P_total
    
    def thermal_analysis(self):
        """
        Simplified 1D thermal analysis
        
        Assumptions:
        - 1D heat conduction along beam length
        - Uniform convective cooling from perimeter
        - Steady-state
        
        Governing equation:
        k·A·d²T/dx² - h·p·(T - T_amb) + q_vol·A = 0
        
        where p is perimeter
        """
        # Thermal parameters
        k = self.mat.k_thermal
        h = self.h_conv
        p = self.perimeter
        A = self.A
        q = self.results['q_vol']
        
        # Characteristic length for heat transfer
        # m² = k·A / (h·p)
        m_squared = h * p / (k * A)
        m = np.sqrt(m_squared)
        
        # Position along beam
        x = np.linspace(0, self.L, 100)
        
        # Calibrated thermal model based on MEMS literature
        # Typical thermal resistance for microbeams: 1000-5000 K/W
        # Reference: Huang & Lee 1999, Guckel et al. 1992
        
        # Thermal resistance combines conduction and convection
        # For a beam heated in the middle, conducting to anchors at both ends:
        # R_cond ≈ L / (2 × k × A)  (factor of 2 for two paths to ground)
        R_cond = self.L / (2 * k * A)
        
        # Convection resistance (entire beam surface)
        R_conv = 1 / (h * p * self.L)
        
        # Parallel combination
        R_thermal = (R_cond * R_conv) / (R_cond + R_conv)
        
        # Temperature rise (using half the beam power since heat flows both ways)
        Delta_T_avg = self.results['P_beam'] * R_thermal
        
        # Maximum temperature at center (roughly 2x average for distributed heating)
        Delta_T_max = 2.5 * Delta_T_avg
        
        # Absolute temperatures
        T_avg = self.T_amb + Delta_T_avg
        T_max = self.T_amb + Delta_T_max
        
        # Temperature rise
        Delta_T_avg = T_avg - self.T_amb
        Delta_T_max = T_max - self.T_amb
        
        # Store temperature distribution
        T_dist = self.T_amb + (q / (h * p)) * \
                 (np.cosh(m * (x - self.L/2)) / np.cosh(m * self.L/2) - 1)
        
        self.results['T_avg'] = T_avg
        self.results['T_max'] = T_max
        self.results['Delta_T_avg'] = Delta_T_avg
        self.results['Delta_T_max'] = Delta_T_max
        self.results['x_dist'] = x
        self.results['T_dist'] = T_dist
        
        return T_avg, T_max
    
    def mechanical_analysis(self):
        """Calculate thermal expansion displacement and stress"""
        # Average temperature for displacement calculation
        T_avg = self.results['T_avg']
        Delta_T = T_avg - self.T_amb
        
        # Thermal strain
        epsilon_thermal = self.mat.alpha * Delta_T
        
        # Elongation of each beam
        Delta_L = epsilon_thermal * self.L
        
        # Shuttle displacement (geometric amplification)
        # For small angles: δ ≈ 2·ΔL / tan(θ)
        delta_shuttle = 2 * Delta_L / np.tan(self.theta)
        
        # Thermal stress (if constrained)
        # For free expansion, stress is minimal
        # For partial constraint: σ = E·α·ΔT / (1 - ν)
        sigma_thermal = self.mat.E * self.mat.alpha * Delta_T / (1 - self.mat.nu)
        
        # Bending stress (simplified)
        # M = F·L where F is thermal expansion force
        # σ_bending ≈ E·α·ΔT·t / (2·L) (rough estimate)
        sigma_bending = self.mat.E * self.mat.alpha * Delta_T * self.t / (2 * self.L)
        
        # Total stress (combination)
        sigma_max = sigma_thermal + sigma_bending
        
        # Safety factor
        SF = self.mat.sigma_yield / sigma_max if sigma_max > 0 else np.inf
        
        self.results['Delta_L'] = Delta_L
        self.results['delta_shuttle'] = delta_shuttle
        self.results['epsilon_thermal'] = epsilon_thermal
        self.results['sigma_thermal'] = sigma_thermal
        self.results['sigma_bending'] = sigma_bending
        self.results['sigma_max'] = sigma_max
        self.results['SF'] = SF
        
        return delta_shuttle, sigma_max, SF
    
    def time_constant(self):
        """Estimate thermal time constant"""
        # Thermal mass
        C_thermal = self.mat.rho_mass * self.mat.Cp * (self.L * self.A)
        
        # Thermal resistance (conduction + convection)
        R_cond = self.L / (self.mat.k_thermal * self.A)
        R_conv = 1 / (self.h_conv * self.L * self.perimeter)
        R_total = R_cond + R_conv
        
        # Time constant
        tau = C_thermal * R_total
        
        # Bandwidth
        BW = 1 / (2 * np.pi * tau)
        
        self.results['tau'] = tau
        self.results['BW'] = BW
        self.results['C_thermal'] = C_thermal
        self.results['R_thermal'] = R_total
        
        return tau, BW
    
    def analyze(self):
        """Run complete analysis"""
        self.electrical_analysis()
        self.thermal_analysis()
        self.mechanical_analysis()
        self.time_constant()
        return self.results
    
    def print_summary(self):
        """Print analysis summary"""
        r = self.results
        
        print("\n" + "="*60)
        print("THERMAL ACTUATOR ANALYTICAL MODEL - RESULTS")
        print("="*60)
        
        print("\nGEOMETRY:")
        print(f"  Beam length: {self.L*1e6:.1f} μm")
        print(f"  Beam width: {self.w*1e6:.1f} μm")
        print(f"  Beam thickness: {self.t*1e6:.1f} μm")
        print(f"  V-angle: {np.rad2deg(self.theta):.1f}°")
        print(f"  Applied voltage: {self.V:.1f} V")
        
        print("\nELECTRICAL:")
        print(f"  Total resistance: {r['R_total']:.1f} Ω")
        print(f"  Current: {r['I']*1e3:.2f} mA")
        print(f"  Total power: {r['P_total']*1e3:.2f} mW")
        
        print("\nTHERMAL:")
        print(f"  Average temperature: {r['T_avg']:.1f} K ({r['T_avg']-273.15:.1f}°C)")
        print(f"  Maximum temperature: {r['T_max']:.1f} K ({r['T_max']-273.15:.1f}°C)")
        print(f"  Average temp rise: {r['Delta_T_avg']:.1f} K")
        print(f"  Maximum temp rise: {r['Delta_T_max']:.1f} K")
        
        print("\nMECHANICAL:")
        print(f"  Beam elongation: {r['Delta_L']*1e9:.1f} nm")
        print(f"  Shuttle displacement: {r['delta_shuttle']*1e6:.2f} μm")
        print(f"  Thermal strain: {r['epsilon_thermal']*1e6:.1f} με")
        print(f"  Maximum stress: {r['sigma_max']/1e6:.1f} MPa")
        print(f"  Safety factor: {r['SF']:.1f}")
        
        print("\nDYNAMICS:")
        print(f"  Thermal time constant: {r['tau']*1e3:.2f} ms")
        print(f"  Bandwidth: {r['BW']:.1f} Hz")
        
        print("\nPERFORMACE METRICS:")
        print(f"  Displacement/Voltage: {r['delta_shuttle']/self.V*1e6:.2f} μm/V")
        print(f"  Displacement/Power: {r['delta_shuttle']/r['P_total']*1e9:.2f} nm/mW")
        print(f"  Energy/Stroke: {r['P_total']*r['tau']*1e6:.2f} μJ")
        
        print("\n" + "="*60 + "\n")

# ============================================================================
# DESIGN SPACE EXPLORATION
# ============================================================================

def parametric_sweep_voltage():
    """Sweep voltage from 0 to 5 V"""
    print("\n--- Voltage Sweep Analysis ---\n")
    
    V_range = np.linspace(0, 5, 21)
    displacement = np.zeros_like(V_range)
    temperature = np.zeros_like(V_range)
    power = np.zeros_like(V_range)
    stress = np.zeros_like(V_range)
    
    for i, V in enumerate(V_range):
        actuator = ThermalActuator(V=V)
        actuator.analyze()
        displacement[i] = actuator.results['delta_shuttle'] * 1e6  # μm
        temperature[i] = actuator.results['Delta_T_max']  # K
        power[i] = actuator.results['P_total'] * 1e3  # mW
        stress[i] = actuator.results['sigma_max'] / 1e6  # MPa
    
    # Plotting
    fig = plt.figure(figsize=(12, 8))
    gs = GridSpec(2, 2, figure=fig, hspace=0.3, wspace=0.3)
    
    # Displacement vs Voltage
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.plot(V_range, displacement, 'b-o', linewidth=2, markersize=6)
    ax1.set_xlabel('Applied Voltage [V]', fontsize=11)
    ax1.set_ylabel('Displacement [μm]', fontsize=11)
    ax1.set_title('Displacement vs Voltage', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Fit quadratic
    p = np.polyfit(V_range, displacement, 2)
    ax1.plot(V_range, np.polyval(p, V_range), 'r--', linewidth=1.5, 
             label=f'Fit: δ = {p[0]:.2f}V²')
    ax1.legend()
    
    # Temperature vs Voltage
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.plot(V_range, temperature, 'r-o', linewidth=2, markersize=6)
    ax2.set_xlabel('Applied Voltage [V]', fontsize=11)
    ax2.set_ylabel('Temperature Rise [K]', fontsize=11)
    ax2.set_title('Temperature Rise vs Voltage', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    # Power vs Voltage
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.plot(V_range, power, 'g-o', linewidth=2, markersize=6)
    ax3.set_xlabel('Applied Voltage [V]', fontsize=11)
    ax3.set_ylabel('Power [mW]', fontsize=11)
    ax3.set_title('Power Dissipation vs Voltage', fontsize=13, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    
    # Stress vs Voltage
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.plot(V_range, stress, 'purple', linewidth=2, marker='o', markersize=6)
    ax4.axhline(7000, color='r', linestyle='--', linewidth=1.5, label='Yield (7000 MPa)')
    ax4.set_xlabel('Applied Voltage [V]', fontsize=11)
    ax4.set_ylabel('Maximum Stress [MPa]', fontsize=11)
    ax4.set_title('Stress vs Voltage', fontsize=13, fontweight='bold')
    ax4.grid(True, alpha=0.3)
    ax4.legend()
    
    plt.suptitle('Thermal Actuator: Voltage Sweep Analysis', 
                 fontsize=15, fontweight='bold', y=0.995)
    plt.savefig('thermal_actuator_voltage_sweep.png', dpi=150, bbox_inches='tight')
    print("✓ Saved: thermal_actuator_voltage_sweep.png")
    
    return V_range, displacement, temperature, power, stress

def parametric_sweep_geometry():
    """Sweep beam length and width"""
    print("\n--- Geometry Sweep Analysis ---\n")
    
    L_range = np.linspace(100e-6, 400e-6, 20)
    w_range = np.linspace(2e-6, 8e-6, 20)
    
    delta_L = np.zeros(len(L_range))
    delta_w = np.zeros(len(w_range))
    
    # Length sweep (fixed width)
    for i, L in enumerate(L_range):
        actuator = ThermalActuator(L=L)
        actuator.analyze()
        delta_L[i] = actuator.results['delta_shuttle'] * 1e6
    
    # Width sweep (fixed length)
    for i, w in enumerate(w_range):
        actuator = ThermalActuator(w=w)
        actuator.analyze()
        delta_w[i] = actuator.results['delta_shuttle'] * 1e6
    
    # Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    ax1.plot(L_range*1e6, delta_L, 'b-o', linewidth=2, markersize=6)
    ax1.set_xlabel('Beam Length [μm]', fontsize=11)
    ax1.set_ylabel('Displacement [μm]', fontsize=11)
    ax1.set_title('Displacement vs Beam Length', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    ax2.plot(w_range*1e6, delta_w, 'r-o', linewidth=2, markersize=6)
    ax2.set_xlabel('Beam Width [μm]', fontsize=11)
    ax2.set_ylabel('Displacement [μm]', fontsize=11)
    ax2.set_title('Displacement vs Beam Width', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('thermal_actuator_geometry_sweep.png', dpi=150, bbox_inches='tight')
    print("✓ Saved: thermal_actuator_geometry_sweep.png")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("THERMAL ACTUATOR ANALYTICAL MODEL")
    print("Simplified 1D Analysis for Preliminary Design")
    print("="*60)
    
    # Create actuator with default parameters
    actuator = ThermalActuator()
    
    # Run analysis
    results = actuator.analyze()
    
    # Print summary
    actuator.print_summary()
    
    # Parametric sweeps
    parametric_sweep_voltage()
    parametric_sweep_geometry()
    
    print("\n✓ Analysis complete!")
    print("✓ Plots saved: thermal_actuator_voltage_sweep.png")
    print("                thermal_actuator_geometry_sweep.png\n")
    
    plt.show()