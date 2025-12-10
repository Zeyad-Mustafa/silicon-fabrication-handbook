"""
MEMS Surface Micromachining Process Simulator

This module simulates key aspects of MEMS surface micromachining including:
- Polysilicon deposition and stress
- Sacrificial layer etching and release
- Residual stress effects
- Cantilever beam mechanics
- Stiction analysis
- Design space exploration

Part of the Silicon Fabrication Handbook
https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook

Author: Silicon Fabrication Handbook Team
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import fsolve
from dataclasses import dataclass
from typing import Tuple, Dict, List
import warnings
warnings.filterwarnings('ignore')

# Physical Constants
K_B = 1.381e-23  # Boltzmann constant (J/K)
Q_E = 1.602e-19  # Elementary charge (C)

@dataclass
class MaterialProperties:
    """Material properties for MEMS structures"""
    # Polysilicon properties
    E_poly: float = 160e9  # Young's modulus (Pa)
    nu_poly: float = 0.22  # Poisson's ratio
    rho_poly: float = 2330  # Density (kg/m³)
    sigma_residual: float = -50e6  # Residual stress (Pa, negative = compressive)
    
    # Silicon dioxide (sacrificial layer)
    etch_rate_oxide: float = 100e-9  # HF etch rate (m/s) for SiO₂
    
    # Environmental
    T: float = 300  # Temperature (K)
    P: float = 101325  # Pressure (Pa)
    RH: float = 0.5  # Relative humidity (0-1)
    
    # Surface properties
    gamma_water: float = 0.072  # Surface tension of water (N/m)
    theta_contact: float = 0  # Contact angle (radians)

class CantileverBeam:
    """
    Models a cantilever beam structure - fundamental MEMS element
    """
    def __init__(self, length: float, width: float, thickness: float, 
                 material: MaterialProperties):
        """
        Initialize cantilever beam
        
        Parameters:
        -----------
        length : float - Beam length (m)
        width : float - Beam width (m)
        thickness : float - Beam thickness (m)
        material : MaterialProperties - Material properties
        """
        self.L = length
        self.w = width
        self.t = thickness
        self.mat = material
        
        # Calculate derived properties
        self.I = (self.w * self.t**3) / 12  # Second moment of area (m⁴)
        self.A = self.w * self.t  # Cross-sectional area (m²)
        self.mass = self.mat.rho_poly * self.L * self.A  # Mass (kg)
        
        # Spring constant for tip deflection
        self.k = (3 * self.mat.E_poly * self.I) / (self.L**3)
        
        # Natural frequency
        self.f_n = (1/(2*np.pi)) * np.sqrt(self.k / self.mass)
        
        # Quality factor (typical for vacuum)
        self.Q = 1000
        
    def static_deflection(self, force: float) -> float:
        """
        Calculate static tip deflection under point load
        
        Parameters:
        -----------
        force : float - Applied force at tip (N)
        
        Returns:
        --------
        deflection : float - Tip deflection (m)
        """
        return (force * self.L**3) / (3 * self.mat.E_poly * self.I)
    
    def stress_from_residual(self) -> Tuple[float, float]:
        """
        Calculate beam deflection and curvature from residual stress
        
        Returns:
        --------
        tip_deflection : float - Tip deflection (m)
        radius : float - Radius of curvature (m)
        """
        # Radius of curvature from Stoney's equation
        sigma = self.mat.sigma_residual
        R = (self.mat.E_poly * self.t) / (6 * sigma * (1 - self.mat.nu_poly))
        
        # Tip deflection (small angle approximation)
        delta = self.L**2 / (2 * R)
        
        return delta, R
    
    def pull_in_voltage(self, gap: float) -> float:
        """
        Calculate electrostatic pull-in voltage
        
        Parameters:
        -----------
        gap : float - Initial gap (m)
        
        Returns:
        --------
        V_pi : float - Pull-in voltage (V)
        """
        epsilon_0 = 8.854e-12  # Permittivity of free space (F/m)
        
        # Pull-in occurs at 1/3 of gap
        V_pi = np.sqrt((8 * self.k * gap**3) / (27 * epsilon_0 * self.w * self.L))
        
        return V_pi
    
    def frequency_response(self, freq_range: np.ndarray, 
                          force_amplitude: float) -> np.ndarray:
        """
        Calculate frequency response (displacement vs frequency)
        
        Parameters:
        -----------
        freq_range : ndarray - Frequency range (Hz)
        force_amplitude : float - Driving force amplitude (N)
        
        Returns:
        --------
        displacement : ndarray - Displacement amplitude (m)
        """
        omega = 2 * np.pi * freq_range
        omega_n = 2 * np.pi * self.f_n
        
        # Frequency response function
        H = 1 / np.sqrt((1 - (omega/omega_n)**2)**2 + (omega/(omega_n*self.Q))**2)
        
        # Displacement
        disp = (force_amplitude / self.k) * H
        
        return disp

class StictionAnalyzer:
    """
    Analyzes stiction (adhesion) phenomena in released MEMS structures
    """
    def __init__(self, material: MaterialProperties):
        self.mat = material
        
    def capillary_force(self, length: float, width: float, 
                       gap: float, meniscus_height: float) -> float:
        """
        Calculate capillary adhesion force during drying
        
        Parameters:
        -----------
        length : float - Beam length (m)
        width : float - Beam width (m)
        gap : float - Gap under beam (m)
        meniscus_height : float - Height of water meniscus (m)
        
        Returns:
        --------
        force : float - Capillary force (N)
        """
        # Capillary pressure
        P_cap = (2 * self.mat.gamma_water * np.cos(self.mat.theta_contact)) / gap
        
        # Force over contact area
        contact_area = length * width
        F_cap = P_cap * contact_area
        
        return F_cap
    
    def van_der_waals_force(self, area: float, separation: float) -> float:
        """
        Calculate van der Waals adhesion force
        
        Parameters:
        -----------
        area : float - Contact area (m²)
        separation : float - Surface separation (m)
        
        Returns:
        --------
        force : float - vdW force (N)
        """
        # Hamaker constant for Si-Si in air (J)
        A_H = 2.0e-19
        
        # Non-retarded vdW force
        F_vdw = (A_H * area) / (6 * np.pi * separation**3)
        
        return F_vdw
    
    def stiction_number(self, beam: CantileverBeam, gap: float) -> float:
        """
        Calculate dimensionless stiction number
        
        Parameters:
        -----------
        beam : CantileverBeam - Beam structure
        gap : float - Gap under beam (m)
        
        Returns:
        --------
        S : float - Stiction number (S < 1 indicates no stiction)
        """
        # Capillary force (assuming full wetted length)
        F_cap = self.capillary_force(beam.L, beam.w, gap, gap/2)
        
        # Restoring force from beam stiffness
        F_restore = beam.k * gap
        
        # Stiction number
        S = F_cap / F_restore
        
        return S
    
    def critical_length(self, width: float, thickness: float, 
                       gap: float, E: float) -> float:
        """
        Calculate critical beam length for stiction-free release
        
        Parameters:
        -----------
        width : float - Beam width (m)
        thickness : float - Beam thickness (m)
        gap : float - Gap (m)
        E : float - Young's modulus (Pa)
        
        Returns:
        --------
        L_crit : float - Critical length (m)
        """
        gamma = self.mat.gamma_water
        theta = self.mat.theta_contact
        
        # Critical length from energy balance
        L_crit = np.sqrt((E * thickness**3 * gap**2) / 
                        (12 * gamma * np.cos(theta)))
        
        return L_crit

class SacrificialLayerRelease:
    """
    Simulates the release process for surface micromachined structures
    """
    def __init__(self, material: MaterialProperties):
        self.mat = material
        
    def release_time(self, length: float, width: float, 
                    gap: float, n_holes: int = 0, 
                    hole_diameter: float = 0) -> float:
        """
        Calculate release time for sacrificial layer etching
        
        Parameters:
        -----------
        length : float - Structure length (m)
        width : float - Structure width (m)
        gap : float - Sacrificial layer thickness (m)
        n_holes : int - Number of release holes
        hole_diameter : float - Diameter of release holes (m)
        
        Returns:
        --------
        time : float - Release time (s)
        """
        if n_holes == 0:
            # Lateral etching from edges only
            max_distance = min(length, width) / 2
        else:
            # With release holes - calculate average distance to nearest hole
            area_per_hole = (length * width) / n_holes
            spacing = np.sqrt(area_per_hole)
            max_distance = spacing / 2
        
        # Time = distance / etch rate
        t_release = max_distance / self.mat.etch_rate_oxide
        
        return t_release
    
    def optimize_release_holes(self, length: float, width: float,
                               target_time: float, 
                               hole_diameter: float = 2e-6) -> Dict:
        """
        Optimize number and spacing of release holes for target release time
        
        Parameters:
        -----------
        length : float - Structure length (m)
        width : float - Structure width (m)
        target_time : float - Target release time (s)
        hole_diameter : float - Hole diameter (m)
        
        Returns:
        --------
        results : dict - Optimization results
        """
        # Required etch distance
        distance = target_time * self.mat.etch_rate_oxide
        
        # Required hole spacing
        spacing = 2 * distance
        
        # Number of holes
        n_x = int(np.ceil(length / spacing))
        n_y = int(np.ceil(width / spacing))
        n_holes = n_x * n_y
        
        # Hole area fraction (loss of structural material)
        hole_area = n_holes * np.pi * (hole_diameter/2)**2
        total_area = length * width
        area_fraction = hole_area / total_area
        
        return {
            'n_holes': n_holes,
            'spacing': spacing,
            'n_x': n_x,
            'n_y': n_y,
            'area_fraction': area_fraction,
            'actual_time': self.release_time(length, width, 0, n_holes, hole_diameter)
        }

class ProcessSimulator:
    """
    Complete surface micromachining process flow simulator
    """
    def __init__(self):
        self.mat = MaterialProperties()
        self.layers = []
        
    def deposit_layer(self, material: str, thickness: float, 
                     stress: float = 0) -> None:
        """
        Add a deposited layer to the stack
        
        Parameters:
        -----------
        material : str - Material name ('poly-Si', 'SiO2', 'Si3N4')
        thickness : float - Layer thickness (m)
        stress : float - Residual stress (Pa)
        """
        layer = {
            'material': material,
            'thickness': thickness,
            'stress': stress,
            'step': len(self.layers)
        }
        self.layers.append(layer)
        
    def pattern_layer(self, layer_index: int, fraction_removed: float) -> None:
        """
        Pattern (etch) a layer
        
        Parameters:
        -----------
        layer_index : int - Index of layer to pattern
        fraction_removed : float - Fraction of area removed (0-1)
        """
        if layer_index < len(self.layers):
            self.layers[layer_index]['patterned'] = True
            self.layers[layer_index]['fraction_removed'] = fraction_removed
            
    def release_structure(self) -> Dict:
        """
        Simulate release of sacrificial layers
        
        Returns:
        --------
        results : dict - Release analysis results
        """
        # Find sacrificial layers (typically SiO2)
        sacrificial = [l for l in self.layers if l['material'] == 'SiO2']
        structural = [l for l in self.layers if l['material'] == 'poly-Si']
        
        if not sacrificial or not structural:
            return {'error': 'No sacrificial or structural layers found'}
        
        # Calculate total stress in structural layers
        total_stress = sum(l['stress'] * l['thickness'] for l in structural)
        avg_stress = total_stress / sum(l['thickness'] for l in structural)
        
        return {
            'n_sacrificial': len(sacrificial),
            'n_structural': len(structural),
            'avg_stress': avg_stress,
            'total_thickness': sum(l['thickness'] for l in structural)
        }

def design_space_exploration():
    """
    Explore design space for cantilever beam parameters
    """
    print("=" * 70)
    print("MEMS SURFACE MICROMACHINING - DESIGN SPACE EXPLORATION")
    print("=" * 70)
    
    # Parameter ranges
    lengths = np.linspace(50e-6, 500e-6, 50)  # 50 to 500 μm
    thicknesses = np.array([0.5e-6, 1e-6, 2e-6, 3e-6])  # 0.5 to 3 μm
    
    # Fixed parameters
    width = 20e-6  # 20 μm
    mat = MaterialProperties()
    
    # Calculate properties for each combination
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    for i, t in enumerate(thicknesses):
        freqs = []
        springs = []
        stresses = []
        
        for L in lengths:
            beam = CantileverBeam(L, width, t, mat)
            freqs.append(beam.f_n / 1e3)  # Convert to kHz
            springs.append(beam.k)
            
            # Residual stress deflection
            delta, _ = beam.stress_from_residual()
            stresses.append(abs(delta) * 1e6)  # Convert to μm
        
        # Plot results
        axes[0, 0].plot(lengths*1e6, freqs, label=f't = {t*1e6:.1f} μm')
        axes[0, 1].plot(lengths*1e6, springs, label=f't = {t*1e6:.1f} μm')
        axes[1, 0].plot(lengths*1e6, stresses, label=f't = {t*1e6:.1f} μm')
    
    # Stiction analysis
    analyzer = StictionAnalyzer(mat)
    gap = 2e-6  # 2 μm gap
    
    crit_lengths = []
    for t in thicknesses:
        L_crit = analyzer.critical_length(width, t, gap, mat.E_poly)
        crit_lengths.append(L_crit * 1e6)
    
    axes[1, 1].bar(range(len(thicknesses)), crit_lengths, 
                    tick_label=[f'{t*1e6:.1f}' for t in thicknesses])
    
    # Formatting
    axes[0, 0].set_xlabel('Length (μm)')
    axes[0, 0].set_ylabel('Resonant Frequency (kHz)')
    axes[0, 0].set_title('Natural Frequency vs Length')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    axes[0, 1].set_xlabel('Length (μm)')
    axes[0, 1].set_ylabel('Spring Constant (N/m)')
    axes[0, 1].set_title('Stiffness vs Length')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_yscale('log')
    
    axes[1, 0].set_xlabel('Length (μm)')
    axes[1, 0].set_ylabel('Tip Deflection (μm)')
    axes[1, 0].set_title('Residual Stress Deflection')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    axes[1, 1].set_xlabel('Thickness (μm)')
    axes[1, 1].set_ylabel('Critical Length (μm)')
    axes[1, 1].set_title('Stiction-Free Critical Length')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('mems_design_space.png', dpi=300, bbox_inches='tight')
    print("\n✓ Design space exploration plot saved as 'mems_design_space.png'")
    
    return fig

def analyze_release_process():
    """
    Analyze sacrificial layer release optimization
    """
    print("\n" + "=" * 70)
    print("SACRIFICIAL LAYER RELEASE ANALYSIS")
    print("=" * 70)
    
    mat = MaterialProperties()
    release = SacrificialLayerRelease(mat)
    
    # Structure dimensions
    length = 200e-6  # 200 μm
    width = 100e-6   # 100 μm
    gap = 2e-6       # 2 μm
    
    # Without release holes
    t_no_holes = release.release_time(length, width, gap, 0)
    print(f"\nRelease time without holes: {t_no_holes:.1f} s ({t_no_holes/60:.1f} min)")
    
    # Optimize for 5-minute release
    target_time = 5 * 60  # 5 minutes
    results = release.optimize_release_holes(length, width, target_time)
    
    print(f"\nOptimized release hole design for {target_time/60:.0f} min release:")
    print(f"  Number of holes: {results['n_holes']}")
    print(f"  Grid: {results['n_x']} × {results['n_y']}")
    print(f"  Spacing: {results['spacing']*1e6:.1f} μm")
    print(f"  Area fraction lost: {results['area_fraction']*100:.2f}%")
    print(f"  Actual release time: {results['actual_time']:.1f} s")
    
    # Plot release time vs number of holes
    n_holes_range = np.arange(0, 101, 5)
    times = [release.release_time(length, width, gap, n, 2e-6) 
             for n in n_holes_range]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(n_holes_range, np.array(times)/60, 'b-', linewidth=2)
    ax.axhline(y=target_time/60, color='r', linestyle='--', 
               label=f'Target: {target_time/60:.0f} min')
    ax.axvline(x=results['n_holes'], color='g', linestyle='--', 
               label=f'Optimal: {results["n_holes"]} holes')
    
    ax.set_xlabel('Number of Release Holes')
    ax.set_ylabel('Release Time (minutes)')
    ax.set_title(f'Release Time Optimization\n{length*1e6:.0f}×{width*1e6:.0f} μm structure')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('release_optimization.png', dpi=300, bbox_inches='tight')
    print("\n✓ Release optimization plot saved as 'release_optimization.png'")
    
    return fig

def simulate_cantilever_dynamics():
    """
    Simulate dynamic response of cantilever beam
    """
    print("\n" + "=" * 70)
    print("CANTILEVER BEAM DYNAMICS SIMULATION")
    print("=" * 70)
    
    # Create beam
    mat = MaterialProperties()
    beam = CantileverBeam(length=200e-6, width=20e-6, thickness=2e-6, material=mat)
    
    print(f"\nBeam Properties:")
    print(f"  Dimensions: {beam.L*1e6:.0f} × {beam.w*1e6:.0f} × {beam.t*1e6:.1f} μm")
    print(f"  Mass: {beam.mass*1e9:.2f} ng")
    print(f"  Spring constant: {beam.k:.3f} N/m")
    print(f"  Natural frequency: {beam.f_n/1e3:.2f} kHz")
    print(f"  Quality factor: {beam.Q}")
    
    # Static deflection
    force = 1e-9  # 1 nN
    deflection = beam.static_deflection(force)
    print(f"\nStatic deflection under {force*1e9:.0f} nN: {deflection*1e9:.2f} nm")
    
    # Residual stress effects
    delta_stress, R = beam.stress_from_residual()
    print(f"\nResidual stress effects:")
    print(f"  Stress: {mat.sigma_residual/1e6:.0f} MPa (compressive)")
    print(f"  Tip deflection: {abs(delta_stress)*1e6:.2f} μm")
    print(f"  Radius of curvature: {abs(R)*1e3:.1f} mm")
    
    # Pull-in voltage
    gap = 2e-6
    V_pi = beam.pull_in_voltage(gap)
    print(f"\nPull-in voltage (gap={gap*1e6:.0f} μm): {V_pi:.1f} V")
    
    # Frequency response
    freq_range = np.linspace(0.1*beam.f_n, 2*beam.f_n, 500)
    disp = beam.frequency_response(freq_range, force)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Frequency response
    axes[0].plot(freq_range/1e3, disp*1e9, 'b-', linewidth=2)
    axes[0].axvline(x=beam.f_n/1e3, color='r', linestyle='--', 
                     label=f'f₀ = {beam.f_n/1e3:.2f} kHz')
    axes[0].set_xlabel('Frequency (kHz)')
    axes[0].set_ylabel('Displacement Amplitude (nm)')
    axes[0].set_title('Frequency Response (Q = 1000)')
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()
    
    # Phase response
    omega = 2 * np.pi * freq_range
    omega_n = 2 * np.pi * beam.f_n
    phase = -np.arctan2(omega/(omega_n*beam.Q), 1 - (omega/omega_n)**2)
    
    axes[1].plot(freq_range/1e3, np.degrees(phase), 'g-', linewidth=2)
    axes[1].axvline(x=beam.f_n/1e3, color='r', linestyle='--')
    axes[1].set_xlabel('Frequency (kHz)')
    axes[1].set_ylabel('Phase (degrees)')
    axes[1].set_title('Phase Response')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('cantilever_dynamics.png', dpi=300, bbox_inches='tight')
    print("\n✓ Dynamics plot saved as 'cantilever_dynamics.png'")
    
    return fig

def stiction_analysis():
    """
    Comprehensive stiction analysis
    """
    print("\n" + "=" * 70)
    print("STICTION ANALYSIS")
    print("=" * 70)
    
    mat = MaterialProperties()
    analyzer = StictionAnalyzer(mat)
    
    # Beam parameters
    length = 200e-6
    width = 20e-6
    thickness = 2e-6
    gap = 2e-6
    
    beam = CantileverBeam(length, width, thickness, mat)
    
    # Capillary force
    F_cap = analyzer.capillary_force(length, width, gap, gap/2)
    print(f"\nCapillary adhesion force: {F_cap*1e9:.2f} nN")
    
    # van der Waals force
    area = length * width
    separation = 0.4e-9  # Typical contact separation
    F_vdw = analyzer.van_der_waals_force(area, separation)
    print(f"van der Waals force: {F_vdw*1e9:.2f} nN")
    
    # Stiction number
    S = analyzer.stiction_number(beam, gap)
    print(f"\nStiction number: {S:.2f}")
    if S < 1:
        print("  → Structure will NOT stick (safe)")
    else:
        print("  → Structure WILL stick (redesign needed)")
    
    # Critical length
    L_crit = analyzer.critical_length(width, thickness, gap, mat.E_poly)
    print(f"\nCritical length for stiction-free release: {L_crit*1e6:.0f} μm")
    print(f"Actual length: {length*1e6:.0f} μm")
    if length < L_crit:
        print("  → Safe from stiction")
    else:
        print("  → Risk of stiction")
    
    # Plot stiction number vs length and thickness
    lengths = np.linspace(50e-6, 500e-6, 100)
    thicknesses = np.array([0.5e-6, 1e-6, 2e-6, 3e-6])
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for t in thicknesses:
        S_values = []
        for L in lengths:
            beam_temp = CantileverBeam(L, width, t, mat)
            S_values.append(analyzer.stiction_number(beam_temp, gap))
        
        ax.plot(lengths*1e6, S_values, linewidth=2, 
                label=f't = {t*1e6:.1f} μm')
    
    ax.axhline(y=1, color='r', linestyle='--', linewidth=2, 
               label='Stiction threshold')
    ax.set_xlabel('Length (μm)')
    ax.set_ylabel('Stiction Number S')
    ax.set_title('Stiction Risk Assessment\n(S < 1 = safe, S > 1 = stiction)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 3)
    
    plt.tight_layout()
    plt.savefig('stiction_analysis.png', dpi=300, bbox_inches='tight')
    print("\n✓ Stiction analysis plot saved as 'stiction_analysis.png'")
    
    return fig

def simulate_process_flow():
    """
    Simulate a complete surface micromachining process flow
    """
    print("\n" + "=" * 70)
    print("PROCESS FLOW SIMULATION")
    print("=" * 70)
    
    proc = ProcessSimulator()
    
    print("\nSimulating multi-layer polysilicon process...")
    print("\nStep 1: Deposit first sacrificial oxide (PSG)")
    proc.deposit_layer('SiO2', 2e-6, stress=0)
    
    print("Step 2: Deposit and pattern first poly-Si layer (Poly-0)")
    proc.deposit_layer('poly-Si', 0.5e-6, stress=-50e6)
    proc.pattern_layer(1, 0.3)
    
    print("Step 3: Deposit second sacrificial oxide")
    proc.deposit_layer('SiO2', 2e-6, stress=0)
    
    print("Step 4: Deposit and pattern second poly-Si layer (Poly-1)")
    proc.deposit_layer('poly-Si', 2e-6, stress=-30e6)
    proc.pattern_layer(3, 0.5)
    
    print("Step 5: Deposit third sacrificial oxide")
    proc.deposit_layer('SiO2', 2e-6, stress=0)
    
    print("Step 6: Deposit and pattern third poly-Si layer (Poly-2)")
    proc.deposit_layer('poly-Si', 3e-6, stress=-20e6)
    proc.pattern_layer(5, 0.4)
    
    print("\nStep 7: Release structures (HF etch)")
    results = proc.release_structure()
    
    print(f"\nProcess Summary:")
    print(f"  Sacrificial layers: {results['n_sacrificial']}")
    print(f"  Structural layers: {results['n_structural']}")
    print(f"  Average residual stress: {results['avg_stress']/1e6:.1f} MPa")
    print(f"  Total structural thickness: {results['total_thickness']*1e6:.1f} μm")
    
    # Visualize layer stack
    fig, ax = plt.subplots(figsize=(12, 6))
    
    y_pos = 0
    colors = {'poly-Si': 'steelblue', 'SiO2': 'lightcoral', 'Si3N4': 'lightgreen'}
    
    for i, layer in enumerate(proc.layers):
        height = layer['thickness'] * 1e6
        color = colors.get(layer['material'], 'gray')
        
        ax.barh(0, 100, height, y_pos, color=color, 
                edgecolor='black', linewidth=1)
        
        # Add label
        label = f"{layer['material']}\n{layer['thickness']*1e6:.1f} μm"
        if layer.get('patterned'):
            label += f"\n({layer['fraction_removed']*100:.0f}% etched)"
        
        ax.text(50, y_pos + height/2, label, 
                ha='center', va='center', fontsize=9)
        
        y_pos += height
    
    ax.set_xlim(0, 100)
    ax.set_ylim(0, y_pos)
    ax.set_xlabel('Width (arbitrary units)')
    ax.set_ylabel('Height (μm)')
    ax.set_title('Surface Micromachining Layer Stack')
    ax.set_xticks([])
    
    plt.tight_layout()
    plt.savefig('process_flow_stack.png', dpi=300, bbox_inches='tight')
    print("\n✓ Process stack visualization saved as 'process_flow_stack.png'")
    
    return fig

def main():
    """
    Main execution function - runs all simulations
    """
    print("\n" + "=" * 70)
    print(" " * 15 + "MEMS SURFACE MICROMACHINING SIMULATOR")
    print(" " * 10 + "Silicon Fabrication Handbook - Educational Tool")
    print("=" * 70)
    print("\nThis simulator demonstrates key concepts in MEMS surface")
    print("micromachining including:")
    print("  • Polysilicon mechanical properties")
    print("  • Sacrificial layer release optimization")
    print("  • Stiction analysis and prevention")
    print("  • Cantilever beam dynamics")
    print("  • Complete process flow simulation")
    print("\nGenerating plots and analysis...")
    
    # Run all simulations
    try:
        design_space_exploration()
        analyze_release_process()
        simulate_cantilever_dynamics()
        stiction_analysis()
        simulate_process_flow()
        
        print("\n" + "=" * 70)
        print("SIMULATION COMPLETE!")
        print("=" * 70)
        print("\nGenerated files:")
        print("  1. mems_design_space.png - Design parameter exploration")
        print("  2. release_optimization.png - Sacrificial layer release")
        print("  3. cantilever_dynamics.png - Frequency and phase response")
        print("  4. stiction_analysis.png - Adhesion risk assessment")
        print("  5. process_flow_stack.png - Multi-layer process visualization")
        print("\nAll simulations completed successfully!")
        print("\nFor more information, visit:")
        print("https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook")
        print("=" * 70 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error during simulation: {e}")
        raise

if __name__ == "__main__":
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Configure matplotlib for better plots
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.labelsize'] = 11
    plt.rcParams['axes.titlesize'] = 12
    plt.rcParams['legend.fontsize'] = 9
    plt.rcParams['figure.dpi'] = 100
    
    # Run main simulation
    main()
    
    # Show all plots
    plt.show()

# Example usage for individual components:
"""
# Create a cantilever beam
mat = MaterialProperties()
beam = CantileverBeam(length=200e-6, width=20e-6, thickness=2e-6, material=mat)

# Calculate properties
print(f"Natural frequency: {beam.f_n/1e3:.2f} kHz")
print(f"Spring constant: {beam.k:.3f} N/m")

# Analyze stiction
analyzer = StictionAnalyzer(mat)
S = analyzer.stiction_number(beam, gap=2e-6)
print(f"Stiction number: {S:.2f}")

# Optimize release
release = SacrificialLayerRelease(mat)
results = release.optimize_release_holes(200e-6, 100e-6, target_time=300)
print(f"Optimized holes: {results['n_holes']}")
"""