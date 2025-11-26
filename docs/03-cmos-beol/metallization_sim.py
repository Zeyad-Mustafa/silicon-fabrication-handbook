"""
CMOS BEOL Metallization Simulator
==================================

Complete simulation suite for copper interconnect analysis including:
- Effective resistivity with size effects
- RC delay calculation
- Electromigration lifetime prediction
- Optimal repeater insertion
- Crosstalk analysis
- Power grid IR drop

Author: Silicon Fabrication Handbook Team
Date: November 2025
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Tuple, List
import warnings

# Physical constants
K_BOLTZMANN = 8.617e-5  # eV/K
ELECTRON_CHARGE = 1.602e-19  # C
EPSILON_0 = 8.854e-12  # F/m

@dataclass
class MetalLayer:
    """Metal layer properties"""
    name: str
    width: float  # nm
    thickness: float  # nm
    pitch: float  # nm (width + space)
    barrier_thickness: float  # nm
    resistivity_bulk: float  # µΩ·cm
    k_dielectric: float
    
    @property
    def spacing(self) -> float:
        """Calculate spacing between lines"""
        return self.pitch - self.width

@dataclass
class ProcessNode:
    """Technology node parameters"""
    node_name: str
    metal_layers: dict  # Dictionary of MetalLayer objects
    em_activation_energy: float  # eV
    em_exponent: float
    max_current_density: float  # MA/cm²

# Define standard process nodes
def get_7nm_node() -> ProcessNode:
    """7nm technology node parameters"""
    layers = {
        'M1': MetalLayer('M1', 40, 80, 80, 4, 1.7, 2.5),
        'M2': MetalLayer('M2', 50, 100, 100, 4, 1.7, 2.5),
        'M3': MetalLayer('M3', 80, 150, 160, 5, 1.7, 2.7),
        'M5': MetalLayer('M5', 200, 400, 450, 5, 1.7, 3.0),
        'M8': MetalLayer('M8', 1000, 1500, 2000, 8, 1.7, 3.5),
    }
    return ProcessNode('7nm', layers, 1.2, 1.5, 15.0)

def get_28nm_node() -> ProcessNode:
    """28nm technology node parameters"""
    layers = {
        'M1': MetalLayer('M1', 80, 160, 160, 5, 1.7, 2.8),
        'M2': MetalLayer('M2', 100, 200, 200, 5, 1.7, 2.8),
        'M3': MetalLayer('M3', 150, 300, 320, 6, 1.7, 3.0),
        'M5': MetalLayer('M5', 400, 800, 900, 8, 1.7, 3.2),
    }
    return ProcessNode('28nm', layers, 1.0, 1.5, 10.0)


class InterconnectSimulator:
    """Main simulator class for BEOL interconnects"""
    
    def __init__(self, node: ProcessNode):
        self.node = node
        
    def effective_resistivity(self, layer: MetalLayer, 
                            temperature: float = 300) -> float:
        """
        Calculate effective resistivity including size effects
        
        Uses Fuchs-Sondheimer model for surface scattering and
        Mayadas-Shatzkes for grain boundary scattering.
        
        Args:
            layer: Metal layer properties
            temperature: Temperature in Kelvin
            
        Returns:
            Effective resistivity in µΩ·cm
        """
        # Bulk resistivity with temperature dependence
        T0 = 300  # Reference temperature
        alpha_cu = 0.0039  # Temperature coefficient for Cu
        rho_bulk = layer.resistivity_bulk * (1 + alpha_cu * (temperature - T0))
        
        # Mean free path in Cu at room temperature
        lambda_mfp = 40  # nm
        
        # Specularity parameter (0 = fully diffuse, 1 = fully specular)
        p = 0.5  # Typical for Cu with barrier
        
        # Surface scattering correction (Fuchs-Sondheimer)
        w_eff = layer.width - 2 * layer.barrier_thickness
        t_eff = layer.thickness - 2 * layer.barrier_thickness
        
        # Simplified F-S correction for rectangular cross-section
        fs_correction = 1.0
        if w_eff > 0 and t_eff > 0:
            w_ratio = lambda_mfp / w_eff
            t_ratio = lambda_mfp / t_eff
            fs_correction = 1 + (3 * lambda_mfp / 8) * (
                (1 - p) / w_eff + (1 - p) / t_eff
            )
        
        # Grain boundary scattering (Mayadas-Shatzkes)
        # Assume grain size ~ line width for damascene Cu
        R = 0.3  # Grain boundary reflection coefficient
        alpha = lambda_mfp / w_eff if w_eff > 0 else 0
        
        gb_correction = 1.0
        if alpha > 0:
            gb_correction = (1 - 3 * alpha / 2 + 3 * alpha**2 - 3 * alpha**3 * 
                           np.log(1 + 1/alpha)) / (1 - alpha) if alpha < 10 else 1 + R * alpha
        
        # Barrier contribution
        barrier_area = 2 * layer.barrier_thickness * (layer.width + layer.thickness)
        cu_area = w_eff * t_eff if w_eff > 0 and t_eff > 0 else 1e-6
        total_area = layer.width * layer.thickness
        
        # Effective resistivity (parallel resistance model)
        rho_barrier = 200  # µΩ·cm for Ta/TaN barrier
        
        if cu_area > 0:
            rho_eff = rho_bulk * fs_correction * gb_correction * total_area / cu_area
        else:
            rho_eff = rho_barrier  # Extremely narrow line
            
        return rho_eff
    
    def line_resistance(self, layer: MetalLayer, length: float,
                       temperature: float = 300) -> float:
        """
        Calculate line resistance
        
        Args:
            layer: Metal layer properties
            length: Line length in µm
            temperature: Temperature in K
            
        Returns:
            Resistance in Ω
        """
        rho_eff = self.effective_resistivity(layer, temperature)
        
        # Convert units: µΩ·cm → Ω·m
        rho_si = rho_eff * 1e-8  # Ω·m
        
        # Cross-sectional area
        w_eff = max(layer.width - 2 * layer.barrier_thickness, 1)  # nm
        t_eff = max(layer.thickness - 2 * layer.barrier_thickness, 1)  # nm
        area = w_eff * t_eff * 1e-18  # m²
        
        length_m = length * 1e-6  # m
        
        return rho_si * length_m / area
    
    def line_capacitance(self, layer: MetalLayer, length: float,
                        include_fringing: bool = True) -> float:
        """
        Calculate line capacitance to ground and adjacent lines
        
        Args:
            layer: Metal layer properties
            length: Line length in µm
            include_fringing: Include fringing field effects
            
        Returns:
            Total capacitance in fF
        """
        # Parallel plate capacitance (to ground plane below)
        h = layer.thickness  # Height above ground (simplified)
        w = layer.width
        s = layer.spacing
        k = layer.k_dielectric
        
        # Ground capacitance per unit length (fF/µm)
        c_ground = EPSILON_0 * k * w / (h * 1e-9) * 1e15 / 1e-6
        
        if include_fringing:
            # Fringing field correction (approximate)
            c_ground *= (1 + (2 * h / (np.pi * w)) * np.log(1 + w / h))
        
        # Coupling capacitance to adjacent lines (Miller capacitance)
        if s > 0:
            # Parallel plate between adjacent lines
            c_coupling = EPSILON_0 * k * layer.thickness / (s * 1e-9) * 1e15 / 1e-6
            
            if include_fringing:
                # Fringing between adjacent lines
                c_coupling *= (1 + s / layer.thickness)
        else:
            c_coupling = 0
        
        # Total capacitance per unit length
        c_total_per_um = c_ground + c_coupling
        
        return c_total_per_um * length
    
    def elmore_delay(self, layer: MetalLayer, length: float,
                    load_cap: float = 0) -> float:
        """
        Calculate Elmore delay for RC line
        
        Args:
            layer: Metal layer properties
            length: Line length in µm
            load_cap: Additional load capacitance in fF
            
        Returns:
            Delay in ps
        """
        R = self.line_resistance(layer, length)
        C = self.line_capacitance(layer, length) + load_cap
        
        # Elmore delay for distributed RC line
        # For lumped approximation: τ = 0.69 * R * C
        # For distributed: τ = 0.38 * R * C (more accurate)
        
        delay_ps = 0.38 * R * C  # Already in ps (Ω * fF = ps)
        
        return delay_ps
    
    def electromigration_lifetime(self, layer: MetalLayer, 
                                  current: float,
                                  temperature: float = 400) -> float:
        """
        Calculate median time to failure due to electromigration
        Uses Black's equation
        
        Args:
            layer: Metal layer properties
            current: DC current in mA
            temperature: Operating temperature in K
            
        Returns:
            MTF in years
        """
        # Current density
        area_cm2 = (layer.width * layer.thickness) * 1e-14  # cm²
        j = (current * 1e-3) / area_cm2  # A/cm²
        j_MA = j / 1e6  # MA/cm²
        
        # Black's equation: MTF = A * j^(-n) * exp(Ea / kT)
        # A is empirical constant, we'll normalize to give reasonable values
        
        Ea = self.node.em_activation_energy  # eV
        n = self.node.em_exponent
        
        # Normalization: at j = max_j, T = 400K, MTF should be ~10 years
        A_norm = 10 * (self.node.max_current_density ** n) / np.exp(Ea / (K_BOLTZMANN * 400))
        
        mtf_years = A_norm * (j_MA ** (-n)) * np.exp(Ea / (K_BOLTZMANN * temperature))
        
        return mtf_years
    
    def max_current_limit(self, layer: MetalLayer, 
                         lifetime_years: float = 10,
                         temperature: float = 400) -> float:
        """
        Calculate maximum allowable current for target lifetime
        
        Args:
            layer: Metal layer properties
            lifetime_years: Target lifetime in years
            temperature: Operating temperature in K
            
        Returns:
            Maximum current in mA
        """
        # Invert Black's equation
        Ea = self.node.em_activation_energy
        n = self.node.em_exponent
        
        A_norm = 10 * (self.node.max_current_density ** n) / np.exp(Ea / (K_BOLTZMANN * 400))
        
        j_MA = (A_norm * np.exp(Ea / (K_BOLTZMANN * temperature)) / lifetime_years) ** (1/n)
        
        area_cm2 = (layer.width * layer.thickness) * 1e-14
        i_max = j_MA * 1e6 * area_cm2 * 1e3  # mA
        
        return i_max
    
    def optimal_repeater_count(self, layer: MetalLayer, length: float,
                              driver_r: float = 1000,
                              driver_c: float = 10,
                              buffer_gain: float = 4) -> Tuple[int, float]:
        """
        Calculate optimal number of repeaters and resulting delay
        
        Args:
            layer: Metal layer properties
            length: Total wire length in µm
            driver_r: Driver resistance in Ω
            driver_c: Driver capacitance in fF
            buffer_gain: Inverter gain (W_p/W_n ratio related)
            
        Returns:
            (optimal_count, optimized_delay_ps)
        """
        # Wire parameters per unit length
        r_wire = self.line_resistance(layer, 1.0) / 1.0  # Ω/µm
        c_wire = self.line_capacitance(layer, 1.0) / 1.0  # fF/µm
        
        # Optimal segment length (Bakoglu's formula)
        l_opt = np.sqrt((driver_r * driver_c) / (r_wire * c_wire))
        
        # Number of repeaters
        n_repeaters = max(0, int(length / l_opt) - 1)
        
        # Segment length with repeaters
        if n_repeaters > 0:
            l_segment = length / (n_repeaters + 1)
        else:
            l_segment = length
        
        # Delay per segment
        r_segment = r_wire * l_segment
        c_segment = c_wire * l_segment
        
        delay_per_segment = 0.69 * (driver_r * (driver_c + c_segment) + 
                                    r_segment * c_segment / 2)
        
        total_delay = delay_per_segment * (n_repeaters + 1)
        
        return n_repeaters, total_delay
    
    def crosstalk_analysis(self, layer: MetalLayer, length: float,
                          switching_pattern: str = 'opposite') -> dict:
        """
        Analyze crosstalk effects on delay
        
        Args:
            layer: Metal layer properties
            length: Wire length in µm
            switching_pattern: 'opposite', 'same', or 'static'
            
        Returns:
            Dictionary with delay components
        """
        # Intrinsic capacitances
        c_ground = EPSILON_0 * layer.k_dielectric * layer.width / \
                  (layer.thickness * 1e-9) * 1e15 / 1e-6 * length
        
        c_coupling = EPSILON_0 * layer.k_dielectric * layer.thickness / \
                    (layer.spacing * 1e-9) * 1e15 / 1e-6 * length if layer.spacing > 0 else 0
        
        R = self.line_resistance(layer, length)
        
        # Miller effect
        if switching_pattern == 'opposite':
            # Aggressor switches opposite: effective capacitance increases
            c_eff = c_ground + 2 * c_coupling
            miller_factor = 2.0
        elif switching_pattern == 'same':
            # Aggressor switches same direction: effective capacitance decreases
            c_eff = c_ground
            miller_factor = 0.0
        else:  # static
            c_eff = c_ground + c_coupling
            miller_factor = 1.0
        
        delay = 0.69 * R * c_eff
        
        return {
            'c_ground': c_ground,
            'c_coupling': c_coupling,
            'miller_factor': miller_factor,
            'c_effective': c_eff,
            'delay_ps': delay,
            'delay_ratio': c_eff / (c_ground + c_coupling) if (c_ground + c_coupling) > 0 else 1
        }
    
    def power_grid_ir_drop(self, layer: MetalLayer, 
                          grid_size: Tuple[int, int],
                          wire_lengths: Tuple[float, float],
                          total_current: float) -> np.ndarray:
        """
        Calculate IR drop in power grid
        
        Args:
            layer: Metal layer for power grid
            grid_size: (rows, cols) of grid
            wire_lengths: (horizontal_length_µm, vertical_length_µm)
            total_current: Total current drawn in mA
            
        Returns:
            2D array of voltage drops in mV
        """
        rows, cols = grid_size
        h_length, v_length = wire_lengths
        
        # Resistance of each segment
        r_horizontal = self.line_resistance(layer, h_length)
        r_vertical = self.line_resistance(layer, v_length)
        
        # Current distribution (simplified: uniform current draw)
        i_per_node = total_current / (rows * cols)  # mA
        
        # Build resistance network (simplified 2D mesh)
        ir_drop = np.zeros((rows, cols))
        
        # Simple model: IR drop increases with distance from supply
        for i in range(rows):
            for j in range(cols):
                # Manhattan distance from corner (supply point)
                path_resistance = i * r_vertical + j * r_horizontal
                # Cumulative current
                cumulative_current = (i * cols + j + 1) * i_per_node
                ir_drop[i, j] = path_resistance * cumulative_current
        
        return ir_drop
    
    def via_resistance(self, diameter: float, height: float,
                      num_vias: int = 1) -> float:
        """
        Calculate via resistance
        
        Args:
            diameter: Via diameter in nm
            height: Via height in nm
            num_vias: Number of vias in parallel
            
        Returns:
            Total via resistance in Ω
        """
        # Cu resistivity in vias (worse than bulk due to grain structure)
        rho_via = 2.5e-8  # Ω·m (1.5× bulk)
        
        area = np.pi * (diameter * 1e-9 / 2) ** 2
        length = height * 1e-9
        
        r_single = rho_via * length / area
        
        # Contact resistance at interfaces
        r_contact = 1e-8  # Ω·m² specific contact resistivity
        r_interface = 2 * r_contact / area  # Top and bottom
        
        r_total_single = r_single + r_interface
        
        # Parallel vias
        return r_total_single / num_vias


def plot_resistivity_scaling(sim: InterconnectSimulator):
    """Plot effective resistivity vs linewidth"""
    node = sim.node
    m1 = node.metal_layers['M1']
    
    # Vary linewidth
    widths = np.linspace(20, 200, 50)
    resistivities = []
    
    for w in widths:
        layer_test = MetalLayer(
            'test', w, m1.thickness, w * 2, 
            m1.barrier_thickness, m1.resistivity_bulk, m1.k_dielectric
        )
        resistivities.append(sim.effective_resistivity(layer_test))
    
    plt.figure(figsize=(10, 6))
    plt.plot(widths, resistivities, 'b-', linewidth=2, label='Effective ρ')
    plt.axhline(y=m1.resistivity_bulk, color='r', linestyle='--', 
                label=f'Bulk Cu ({m1.resistivity_bulk} µΩ·cm)')
    plt.xlabel('Line Width (nm)', fontsize=12)
    plt.ylabel('Resistivity (µΩ·cm)', fontsize=12)
    plt.title(f'Cu Resistivity vs Line Width ({node.node_name} node)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=11)
    plt.tight_layout()
    
    return plt.gcf()


def plot_rc_delay_comparison(sim: InterconnectSimulator):
    """Compare RC delay across different metal layers"""
    lengths = np.logspace(0, 3, 50)  # 1 µm to 1 mm
    
    plt.figure(figsize=(12, 6))
    
    colors = ['b', 'g', 'r', 'c', 'm']
    for idx, (name, layer) in enumerate(sim.node.metal_layers.items()):
        delays = [sim.elmore_delay(layer, L) for L in lengths]
        plt.loglog(lengths, delays, color=colors[idx % len(colors)], 
                  linewidth=2, label=f'{name} ({layer.width}nm)')
    
    plt.xlabel('Wire Length (µm)', fontsize=12)
    plt.ylabel('RC Delay (ps)', fontsize=12)
    plt.title(f'RC Delay vs Wire Length ({sim.node.node_name} node)', fontsize=14)
    plt.grid(True, which='both', alpha=0.3)
    plt.legend(fontsize=10)
    plt.tight_layout()
    
    return plt.gcf()


def plot_em_lifetime(sim: InterconnectSimulator):
    """Plot electromigration lifetime vs current density"""
    m1 = sim.node.metal_layers['M1']
    
    currents = np.linspace(0.1, 10, 50)  # mA
    temps = [350, 375, 400, 425]
    
    plt.figure(figsize=(10, 6))
    
    for T in temps:
        lifetimes = [sim.electromigration_lifetime(m1, I, T) for I in currents]
        plt.semilogy(currents, lifetimes, linewidth=2, label=f'T = {T}K')
    
    plt.axhline(y=10, color='r', linestyle='--', alpha=0.5, label='10-year target')
    plt.xlabel('Current (mA)', fontsize=12)
    plt.ylabel('Median Time to Failure (years)', fontsize=12)
    plt.title(f'Electromigration Lifetime (M1, {m1.width}nm × {m1.thickness}nm)', 
              fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    plt.tight_layout()
    
    return plt.gcf()


def comprehensive_analysis_report(sim: InterconnectSimulator, 
                                 layer_name: str = 'M1',
                                 length: float = 100.0):
    """Generate comprehensive analysis report"""
    layer = sim.node.metal_layers[layer_name]
    
    print("=" * 70)
    print(f"COMPREHENSIVE INTERCONNECT ANALYSIS - {sim.node.node_name} Node")
    print("=" * 70)
    print(f"\nLayer: {layer_name}")
    print(f"  Width: {layer.width} nm")
    print(f"  Thickness: {layer.thickness} nm")
    print(f"  Pitch: {layer.pitch} nm (spacing: {layer.spacing} nm)")
    print(f"  Barrier thickness: {layer.barrier_thickness} nm")
    print(f"  Wire length: {length} µm")
    
    # Resistivity analysis
    print("\n" + "-" * 70)
    print("RESISTIVITY ANALYSIS")
    print("-" * 70)
    rho_eff = sim.effective_resistivity(layer)
    print(f"  Bulk Cu resistivity: {layer.resistivity_bulk:.2f} µΩ·cm")
    print(f"  Effective resistivity: {rho_eff:.2f} µΩ·cm")
    print(f"  Resistivity increase: {(rho_eff/layer.resistivity_bulk - 1)*100:.1f}%")
    
    # Resistance and capacitance
    print("\n" + "-" * 70)
    print("RC PARAMETERS")
    print("-" * 70)
    R = sim.line_resistance(layer, length)
    C = sim.line_capacitance(layer, length)
    print(f"  Resistance: {R:.2f} Ω ({R/length:.3f} Ω/µm)")
    print(f"  Capacitance: {C:.2f} fF ({C/length:.3f} fF/µm)")
    print(f"  RC product: {R*C:.2f} ps")
    
    # Delay analysis
    print("\n" + "-" * 70)
    print("DELAY ANALYSIS")
    print("-" * 70)
    delay = sim.elmore_delay(layer, length)
    print(f"  Elmore delay: {delay:.2f} ps")
    print(f"  Delay per mm: {delay*10:.2f} ps/mm")
    
    # Repeater optimization
    n_rep, delay_opt = sim.optimal_repeater_count(layer, length)
    print(f"\n  Repeater insertion optimization:")
    print(f"    Optimal repeater count: {n_rep}")
    print(f"    Optimized delay: {delay_opt:.2f} ps")
    if n_rep > 0:
        print(f"    Improvement: {(1 - delay_opt/delay)*100:.1f}%")
    
    # Crosstalk
    print("\n" + "-" * 70)
    print("CROSSTALK ANALYSIS")
    print("-" * 70)
    
    for pattern in ['static', 'same', 'opposite']:
        result = sim.crosstalk_analysis(layer, length, pattern)
        print(f"  {pattern.capitalize()} switching:")
        print(f"    Effective capacitance: {result['c_effective']:.2f} fF")
        print(f"    Delay: {result['delay_ps']:.2f} ps " + 
              f"({result['delay_ratio']:.2f}× nominal)")
    
    # Electromigration
    print("\n" + "-" * 70)
    print("ELECTROMIGRATION RELIABILITY")
    print("-" * 70)
    
    test_currents = [0.5, 1.0, 2.0, 5.0]
    print(f"  Activation energy: {sim.node.em_activation_energy:.2f} eV")
    print(f"\n  Lifetime at T=400K:")
    for I in test_currents:
        lifetime = sim.electromigration_lifetime(layer, I, 400)
        j = I * 1e-3 / (layer.width * layer.thickness * 1e-14) / 1e6  # MA/cm²
        print(f"    {I:4.1f} mA ({j:5.2f} MA/cm²): {lifetime:8.2f} years")
    
    i_max_10yr = sim.max_current_limit(layer, 10, 400)
    print(f"\n  Maximum current (10-year lifetime, 400K): {i_max_10yr:.2f} mA")
    
    # Via resistance
    print("\n" + "-" * 70)
    print("VIA RESISTANCE")
    print("-" * 70)
    via_dia = layer.width * 0.8  # Typical via diameter
    via_height = 150  # nm
    
    for n_vias in [1, 2, 4]:
        r_via = sim.via_resistance(via_dia, via_height, n_vias)
        print(f"  {n_vias} via{'s' if n_vias > 1 else ''} " + 
              f"({via_dia:.0f}nm dia, {via_height}nm height): {r_via:.2f} Ω")
    
    print("\n" + "=" * 70)
    print("END OF REPORT")
    print("=" * 70 + "\n")


def main():
    """Main execution function"""
    print("\n" + "=" * 70)
    print("CMOS BEOL METALLIZATION SIMULATOR")
    print("=" * 70 + "\n")
    
    # Initialize simulator with 7nm node
    node_7nm = get_7nm_node()
    sim = InterconnectSimulator(node_7nm)
    
    # Run comprehensive analysis
    comprehensive_analysis_report(sim, 'M1', 100.0)
    
    # Generate plots
    print("\nGenerating analysis plots...")
    
    try:
        fig1 = plot_resistivity_scaling(sim)
        fig1.savefig('resistivity_scaling.png', dpi=300, bbox_inches='tight')
        print("  ✓ Resistivity scaling plot saved")
        
        fig2 = plot_rc_delay_comparison(sim)
        fig2.savefig('rc_delay_comparison.png', dpi=300, bbox_inches='tight')
        print("  ✓ RC delay comparison plot saved")
        
        fig3 = plot_em_lifetime(sim)
        fig3.savefig('em_lifetime.png', dpi=300, bbox_inches='tight')
        print("  ✓ Electromigration lifetime plot saved")
        
        plt.show()
        
    except Exception as e:
        print(f"  ✗ Error generating plots: {e}")
    
    # Additional analyses
    print("\n" + "-" * 70)
    print("TECHNOLOGY NODE COMPARISON")
    print("-" * 70)
    
    node_28nm = get_28nm_node()
    sim_28nm = InterconnectSimulator(node_28nm)
    
    for node_name, sim_node in [('7nm', sim), ('28nm', sim_28nm)]:
        m1 = sim_node.node.metal_layers['M1']
        delay = sim_node.elmore_delay(m1, 100)
        print(f"\n{node_name} node (M1, 100µm wire):")
        print(f"  Width: {m1.width} nm")
        print(f"  RC delay: {delay:.2f} ps")
        print(f"  Max current (10yr): {sim_node.max_current_limit(m1):.2f} mA")
    
    print("\n" + "=" * 70)
    print("Simulation complete!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()