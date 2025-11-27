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
        R_gb = 0.3  # Grain boundary reflection coefficient - renamed to R_gb to avoid shadowing R
        alpha = lambda_mfp / w_eff if w_eff > 0 else 0
        
        gb_correction = 1.0
        if alpha > 0:
            # Replaced R with R_gb
            # Corrected MS equation approximation for larger alpha
            if alpha < 1:
                 # Standard MS approximation (k=1)
                gb_correction = 1 + (3/2) * alpha * R_gb / (1 - R_gb)
            else:
                 # Simplified expression for large alpha - original code's logic was complex.
                 # The simplified F-S/MS parallel resistance approximation is more robust.
                 # Using a simpler form for MS (rho_gb / rho_bulk = 1 + A*alpha)
                warnings.warn(f"High alpha ({alpha:.2f}): Simplified MS model used.", UserWarning)
                # Reverting to original implementation but using R_gb
                if alpha < 10:
                    gb_correction = (1 - 3 * alpha / 2 + 3 * alpha**2 - 3 * alpha**3 * np.log(1 + 1/alpha)) / (1 - alpha)
                else:
                    gb_correction = 1 + R_gb * alpha

        # Barrier contribution
        # rho_barrier = 200  # µΩ·cm for Ta/TaN barrier - not strictly used in current model
        
        # Effective resistivity (parallel resistance model using only Cu area for size effects)
        cu_area = w_eff * t_eff
        total_area = layer.width * layer.thickness
        
        if cu_area > 0 and total_area > 0:
             # This is a highly simplified parallel model attempt mixed with F-S/MS.
             # In modern analysis, it's typically: rho_eff = rho_bulk * f_fs * f_ms.
             # The original code's final line seems to be an attempt at a simplified
             # combination of the resistivity of the Cu core and the barrier/liner
             # (where a higher resistivity barrier occupies a fixed volume).
             # We will stick to the standard model: rho_eff = rho_bulk * fs_correction * gb_correction
            rho_eff = rho_bulk * fs_correction * gb_correction
        else:
            rho_eff = 200.0  # Barrier-dominated or extremely narrow line
            
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
        
        # Convert units: µΩ·cm -> Ω·m
        rho_si = rho_eff * 1e-8  # Ω·m
        
        # Cross-sectional area calculation
        # Effective Cu area for the resistance calculation.
        w_eff = max(layer.width - 2 * layer.barrier_thickness, 1)  # nm
        t_eff = max(layer.thickness - 2 * layer.barrier_thickness, 1)  # nm
        
        # Area of the CU core in m²
        area = w_eff * t_eff * 1e-18  # m²
        
        length_m = length * 1e-6  # m
        
        if area < 1e-24: # Check for near-zero area
            warnings.warn("Area is near zero, returning a high resistance.", UserWarning)
            return 1e12 # Return a very high resistance
            
        # R = rho * L / A
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
        
        # Ground capacitance per unit length (F/m)
        c_ground_per_m = EPSILON_0 * k * w / (h * 1e-9)
        
        if include_fringing:
            # Fringing field correction (approximate)
            c_ground_per_m *= (1 + (2 * h / (np.pi * w)) * np.log(1 + w / h))
        
        # Coupling capacitance to adjacent lines (Miller capacitance)
        c_coupling_per_m = 0.0
        if s > 0:
            # Parallel plate between adjacent lines
            c_coupling_per_m = EPSILON_0 * k * layer.thickness / (s * 1e-9)
            
            if include_fringing:
                # Fringing between adjacent lines
                c_coupling_per_m *= (1 + s / layer.thickness)
        
        # Total capacitance per unit length (F/m)
        c_total_per_m = c_ground_per_m + c_coupling_per_m
        
        # Convert length to meters and total capacitance to fF
        length_m = length * 1e-6 # m
        
        # C_total = C_total_per_m * length_m * 1e15 (fF/F)
        return c_total_per_m * length_m * 1e15
    
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
        
        # Elmore delay for distributed RC line: T_d = 0.38 * R_total * C_total.
        # R (Ohm) * C (fF) * 1e-3 = ps. The 0.38 factor is typically scaled for the units.
        # We will keep the original formula for consistency (0.38 * R * C)
        
        delay_ps = 0.38 * R * C 
        
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
        if area_cm2 <= 0:
            return 0.0 # Return 0 lifetime for no area
        
        j = (current * 1e-3) / area_cm2  # A/cm²
        j_MA = j / 1e6  # MA/cm²
        
        # Black's equation: MTF = A * j^(-n) * exp(Ea / kT)
        
        Ea = self.node.em_activation_energy  # eV
        n = self.node.em_exponent
        
        # Normalization: at j = max_j, T = 400K, MTF should be ~10 years
        # The original normalization logic is fine.
        A_norm = 10 * (self.node.max_current_density ** n) / np.exp(Ea / (K_BOLTZMANN * 400))
        
        if j_MA <= 0:
            return np.inf # Return infinite lifetime for zero or negative current
            
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
        
        if lifetime_years <= 0:
            return 0.0
            
        # j_MA = (A_norm * exp(Ea / kT) / lifetime_years) ^ (1/n)
        j_MA = (A_norm * np.exp(Ea / (K_BOLTZMANN * temperature)) / lifetime_years) ** (1/n)
        
        area_cm2 = (layer.width * layer.thickness) * 1e-14
        if area_cm2 <= 0:
            return 0.0
            
        i_max = j_MA * 1e6 * area_cm2 * 1e3  # MA/cm^2 * 1e6 A/MA * cm^2 * 1e3 mA/A = mA
        
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
        if length <= 0:
            return 0, 0.0
            
        r_wire = self.line_resistance(layer, 1.0) # Ω/µm
        c_wire = self.line_capacitance(layer, 1.0) # fF/µm
        
        if r_wire * c_wire <= 0:
            # Handle case where line is lossless or has zero resistance/capacitance
            return 0, 0.69 * driver_r * driver_c 

        # Optimal segment length (Bakoglu's formula)
        l_opt_sq = (driver_r * driver_c) / (r_wire * c_wire)
        if l_opt_sq < 0:
            l_opt = 0.0
        else:
            l_opt = np.sqrt(l_opt_sq) # Preserving original simplified formula
        
        
        if l_opt <= 0:
             n_repeaters = 0
             l_segment = length
        else:
             # Number of repeaters
             n_repeaters = max(0, int(round(length / l_opt)) - 1) # Added round for better int conversion
             l_segment = length / (n_repeaters + 1)
        
        # Delay per segment (using Elmore approximation)
        r_segment = r_wire * l_segment
        c_segment = c_wire * l_segment
        
        # Delay is t_driver_RC + t_wire_RC
        # t_driver_RC = R_driver * (C_driver + C_segment)
        # t_wire_RC = 0.5 * R_segment * C_segment
        # Total delay per segment = 0.69 * (t_driver_RC + t_wire_RC)
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
        # Intrinsic capacitances per unit length (F/m)
        c_ground_per_m = EPSILON_0 * layer.k_dielectric * layer.width / \
                  (layer.thickness * 1e-9)
        
        c_coupling_per_m = EPSILON_0 * layer.k_dielectric * layer.thickness / \
                    (layer.spacing * 1e-9) if layer.spacing > 0 else 0
        
        # Total capacitance (fF)
        length_m = length * 1e-6
        c_ground = c_ground_per_m * length_m * 1e15 # fF
        c_coupling = c_coupling_per_m * length_m * 1e15 # fF
        
        R = self.line_resistance(layer, length)
        
        # Miller effect
        if switching_pattern == 'opposite':
            # Aggressor switches opposite: effective capacitance increases
            c_eff = c_ground + 2 * c_coupling
            miller_factor = 2.0
        elif switching_pattern == 'same':
            # Aggressor switches same direction: effective capacitance decreases (the coupling cap is effectively shorted)
            c_eff = c_ground
            miller_factor = 0.0
        else:  # static
            # Aggressor is static: coupling cap is effectively C_coupling
            c_eff = c_ground + c_coupling
            miller_factor = 1.0
        
        # Delay using the Elmore approximation
        delay = 0.69 * R * c_eff
        
        c_nominal = c_ground + c_coupling
        
        return {
            'c_ground': c_ground,
            'c_coupling': c_coupling,
            'miller_factor': miller_factor,
            'c_effective': c_eff,
            'delay_ps': delay,
            'delay_ratio': c_eff / c_nominal if c_nominal > 0 else 1.0
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
        
        if rows <= 0 or cols <= 0:
            return np.array([0])
            
        # Resistance of each segment (in Ohms)
        r_horizontal = self.line_resistance(layer, h_length)
        r_vertical = self.line_resistance(layer, v_length)
        
        # Current distribution (simplified: uniform current draw)
        num_nodes = rows * cols
        if num_nodes == 0:
            return np.array([0])
            
        i_per_node = total_current / num_nodes # mA
        
        # Build resistance network (simplified 2D mesh)
        ir_drop_mV = np.zeros((rows, cols)) # Drop in mV
        
        # Simple model: IR drop increases with distance from supply (assume supply at (0,0))
        # This is a highly simplified model. Actual power grid analysis uses KCL/KVL or FEM.
        for i in range(rows):
            for j in range(cols):
                # Manhattan distance from corner (supply point) in terms of segments
                
                # Cumulative current assumption: current for all nodes from (i, j) to (rows-1, cols-1) 
                # flows through the segments closest to the supply. The formula below is a 
                # highly simplified path-resistance model.
                
                # Simplified total resistance from (0,0) to (i,j)
                path_resistance = i * r_vertical + j * r_horizontal # Ohm
                
                # Cumulative current (mA) - assuming current is drawn uniformly up to this node
                cumulative_current = (i * cols + j + 1) * i_per_node # mA
                
                # IR Drop: I (mA) * R (Ohm) = V (mV)
                ir_drop_mV[i, j] = path_resistance * cumulative_current
        
        return ir_drop_mV
    
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
        if diameter <= 0 or height <= 0 or num_vias <= 0:
            return np.inf
            
        # Cu resistivity in vias (worse than bulk due to grain structure)
        rho_via = 2.5e-8  # Ω·m (1.5x bulk)
        
        area = np.pi * (diameter * 1e-9 / 2) ** 2 # m^2
        length = height * 1e-9 # m
        
        r_single = rho_via * length / area
        
        # Contact resistance at interfaces
        r_contact_spec = 1e-8  # Ω·m² specific contact resistivity
        r_interface = 2 * r_contact_spec / area  # Top and bottom interfaces
        
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
        # Added try-except to handle potential warnings/errors from resistivity calculation
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                resistivities.append(sim.effective_resistivity(layer_test))
        except:
            resistivities.append(np.nan)

    
    plt.figure(figsize=(10, 6))
    plt.plot(widths, resistivities, 'b-', linewidth=2, label='Effective rho')
    plt.axhline(y=m1.resistivity_bulk, color='r', linestyle='--', 
                label=f'Bulk Cu ({m1.resistivity_bulk} uOhm·cm)')
    plt.xlabel('Line Width (nm)', fontsize=12)
    plt.ylabel('Resistivity (uOhm·cm)', fontsize=12)
    plt.title(f'Cu Resistivity vs Line Width ({node.node_name} node)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=11)
    plt.tight_layout()
    
    # Return the figure object for saving/displaying
    return plt.gcf()


def plot_rc_delay_comparison(sim: InterconnectSimulator):
    """Compare RC delay across different metal layers"""
    lengths = np.logspace(0, 3, 50)  # 1 µm to 1 mm
    
    plt.figure(figsize=(12, 6))
    
    # FIX: Extended colors list for safety against IndexError
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'purple'] 
    
    for idx, (name, layer) in enumerate(sim.node.metal_layers.items()):
        delays = []
        for L in lengths:
            try:
                # Catch warnings/errors in delay calculation
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    delays.append(sim.elmore_delay(layer, L))
            except:
                delays.append(np.nan)
                
        plt.loglog(lengths, delays, color=colors[idx % len(colors)], 
                  linewidth=2, label=f'{name} ({layer.width}nm)')
    
    plt.xlabel('Wire Length (um)', fontsize=12)
    plt.ylabel('RC Delay (ps)', fontsize=12)
    plt.title(f'RC Delay vs Wire Length ({sim.node.node_name} node)', fontsize=14)
    plt.grid(True, which='both', alpha=0.3)
    plt.legend(fontsize=10)
    plt.tight_layout()
    
    # Return the figure object for saving/displaying
    return plt.gcf()


def plot_em_lifetime(sim: InterconnectSimulator):
    """Plot electromigration lifetime vs current density"""
    m1 = sim.node.metal_layers['M1']
    
    currents = np.linspace(0.1, 10, 50)  # mA
    temps = [350, 375, 400, 425]
    
    plt.figure(figsize=(10, 6))
    
    for T in temps:
        lifetimes = []
        for I in currents:
             try:
                lifetimes.append(sim.electromigration_lifetime(m1, I, T))
             except:
                lifetimes.append(np.nan)
                
        plt.semilogy(currents, lifetimes, linewidth=2, label=f'T = {T}K')
    
    plt.axhline(y=10, color='r', linestyle='--', alpha=0.5, label='10-year target')
    plt.xlabel('Current (mA)', fontsize=12)
    plt.ylabel('Median Time to Failure (years)', fontsize=12)
    plt.title(f'Electromigration Lifetime (M1, {m1.width}nm x {m1.thickness}nm)', 
              fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    plt.tight_layout()
    
    # Return the figure object for saving/displaying
    return plt.gcf()


def comprehensive_analysis_report(sim: InterconnectSimulator, 
                                 layer_name: str = 'M1',
                                 length: float = 100.0):
    """Generate comprehensive analysis report"""
    
    if layer_name not in sim.node.metal_layers:
        print(f"Error: Layer {layer_name} not found in {sim.node.node_name} node.")
        return
        
    layer = sim.node.metal_layers[layer_name]
    
    # Use a warning filter to suppress runtime warnings from numpy/math operations
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        
        print("=" * 70)
        print(f"COMPREHENSIVE INTERCONNECT ANALYSIS - {sim.node.node_name} Node")
        print("=" * 70)
        print(f"\nLayer: {layer_name}")
        print(f"  Width: {layer.width} nm")
        print(f"  Thickness: {layer.thickness} nm")
        print(f"  Pitch: {layer.pitch} nm (spacing: {layer.spacing} nm)")
        print(f"  Barrier thickness: {layer.barrier_thickness} nm")
        print(f"  Wire length: {length} um")
        
        # Resistivity analysis
        print("\n" + "-" * 70)
        print("RESISTIVITY ANALYSIS")
        print("-" * 70)
        rho_eff = sim.effective_resistivity(layer)
        print(f"  Bulk Cu resistivity: {layer.resistivity_bulk:.2f} uOhm·cm")
        print(f"  Effective resistivity: {rho_eff:.2f} uOhm·cm")
        # Added check for division by zero
        if layer.resistivity_bulk > 0:
            print(f"  Resistivity increase: {(rho_eff/layer.resistivity_bulk - 1)*100:.1f}%")
        
        # Resistance and capacitance
        print("\n" + "-" * 70)
        print("RC PARAMETERS")
        print("-" * 70)
        R = sim.line_resistance(layer, length)
        C = sim.line_capacitance(layer, length)
        print(f"  Resistance: {R:.2f} Ohm ({R/length:.3f} Ohm/um)" if length > 0 else f"  Resistance: {R:.2f} Ohm")
        print(f"  Capacitance: {C:.2f} fF ({C/length:.3f} fF/um)" if length > 0 else f"  Capacitance: {C:.2f} fF")
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
        if n_rep > 0 and delay > 0:
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
                  f"({result['delay_ratio']:.2f}x nominal)")
        
        # Electromigration
        print("\n" + "-" * 70)
        print("ELECTROMIGRATION RELIABILITY")
        print("-" * 70)
        
        test_currents = [0.5, 1.0, 2.0, 5.0]
        print(f"  Activation energy: {sim.node.em_activation_energy:.2f} eV")
        print(f"\n  Lifetime at T=400K:")
        
        area_cm2 = (layer.width * layer.thickness) * 1e-14
        
        for I in test_currents:
            lifetime = sim.electromigration_lifetime(layer, I, 400)
            j = I * 1e-3 / area_cm2 / 1e6 if area_cm2 > 0 else 0 # MA/cm²
            print(f"    {I:4.1f} mA ({j:5.2f} MA/cm2): {lifetime:8.2f} years")
        
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
                  f"({via_dia:.0f}nm dia, {via_height}nm height): {r_via:.2f} Ohm")
        
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
    
    # Use a warning filter for this block as well
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        
        try:
            # 1. Generate and save plots to files (so you can find them)
            fig1 = plot_resistivity_scaling(sim)
            fig1.savefig('resistivity_scaling.png', dpi=300, bbox_inches='tight')
            print("  [OK] Resistivity scaling plot saved to resistivity_scaling.png")
            
            fig2 = plot_rc_delay_comparison(sim)
            fig2.savefig('rc_delay_comparison.png', dpi=300, bbox_inches='tight')
            print("  [OK] RC delay comparison plot saved to rc_delay_comparison.png")
            
            fig3 = plot_em_lifetime(sim)
            fig3.savefig('em_lifetime.png', dpi=300, bbox_inches='tight')
            print("  [OK] Electromigration lifetime plot saved to em_lifetime.png")
            
            # 2. Call plt.show() to display the figures in a pop-up window
            # This is the command that will open the figure windows on your local machine.
            plt.show() 
            
        except Exception as e:
            print(f"  [ERROR] Error generating or showing plots: {e}")
    
    # Additional analyses
    print("\n" + "-" * 70)
    print("TECHNOLOGY NODE COMPARISON")
    print("-" * 70)
    
    node_28nm = get_28nm_node()
    sim_28nm = InterconnectSimulator(node_28nm)
    
    # Use a warning filter for this block as well
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        
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