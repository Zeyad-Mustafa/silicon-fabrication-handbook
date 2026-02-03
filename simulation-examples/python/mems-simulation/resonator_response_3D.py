"""
3D Comb Drive Analysis for MEMS Devices
Silicon Fabrication Handbook

This module provides comprehensive analysis tools for electrostatic comb drive actuators
commonly used in MEMS devices. It includes:
- Electrostatic force and capacitance calculations
- Displacement and voltage relationship analysis
- 3D visualization of comb drive structures
- Performance optimization tools

Author: Silicon Fabrication Handbook Project
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.patches import Rectangle
from matplotlib import cm
import scipy.optimize as opt
from dataclasses import dataclass
from typing import Tuple, List, Optional
import warnings

# Physical constants
EPSILON_0 = 8.854e-12  # Permittivity of free space (F/m)
EPSILON_R_SILICON = 11.7  # Relative permittivity of silicon
EPSILON_R_AIR = 1.0  # Relative permittivity of air


@dataclass
class CombDriveGeometry:
    """
    Geometry parameters for a comb drive actuator.
    
    Attributes:
        n_fingers: Number of movable fingers
        finger_length: Length of each finger (m)
        finger_width: Width of each finger (m)
        finger_thickness: Thickness of each finger (m)
        gap: Initial gap between fingers (m)
        overlap: Initial overlap between fingers (m)
        finger_separation: Separation between adjacent fingers on same comb (m)
    """
    n_fingers: int
    finger_length: float
    finger_width: float
    finger_thickness: float
    gap: float
    overlap: float
    finger_separation: float
    
    def __post_init__(self):
        """Validate geometry parameters."""
        if self.n_fingers < 1:
            raise ValueError("Number of fingers must be at least 1")
        if any(param <= 0 for param in [self.finger_length, self.finger_width, 
                                         self.finger_thickness, self.gap, self.overlap]):
            raise ValueError("All geometric dimensions must be positive")


@dataclass
class CombDriveMaterial:
    """
    Material properties for comb drive structure.
    
    Attributes:
        youngs_modulus: Young's modulus (Pa)
        density: Material density (kg/m³)
        poissons_ratio: Poisson's ratio
        residual_stress: Residual stress in film (Pa)
    """
    youngs_modulus: float = 169e9  # Silicon
    density: float = 2329  # Silicon (kg/m³)
    poissons_ratio: float = 0.22  # Silicon
    residual_stress: float = 0.0  # Default: no residual stress


class CombDriveAnalyzer:
    """
    Comprehensive analysis tool for electrostatic comb drive actuators.
    """
    
    def __init__(self, geometry: CombDriveGeometry, material: Optional[CombDriveMaterial] = None):
        """
        Initialize the comb drive analyzer.
        
        Args:
            geometry: CombDriveGeometry object with device dimensions
            material: CombDriveMaterial object (optional, defaults to silicon)
        """
        self.geom = geometry
        self.material = material if material else CombDriveMaterial()
        
    def calculate_capacitance(self, displacement: float = 0.0) -> float:
        """
        Calculate total capacitance of the comb drive.
        
        For parallel plate approximation with fringing fields correction.
        
        Args:
            displacement: Displacement in direction of actuation (m)
            
        Returns:
            Total capacitance (F)
        """
        # Effective overlap accounting for displacement
        effective_overlap = self.geom.overlap + displacement
        
        if effective_overlap <= 0:
            warnings.warn("Negative overlap detected, returning zero capacitance")
            return 0.0
        
        # Parallel plate capacitance per finger pair
        C_parallel = (EPSILON_0 * EPSILON_R_AIR * self.geom.finger_thickness * 
                     effective_overlap / self.geom.gap)
        
        # Fringing field correction (simplified)
        fringing_factor = 1 + (self.geom.gap / (np.pi * self.geom.finger_thickness))
        
        # Total capacitance (2 gaps per finger, n fingers)
        C_total = 2 * self.geom.n_fingers * C_parallel * fringing_factor
        
        return C_total
    
    def calculate_force(self, voltage: float, displacement: float = 0.0) -> float:
        """
        Calculate electrostatic force on the comb drive.
        
        Force is derived from F = 0.5 * V² * dC/dx
        
        Args:
            voltage: Applied voltage (V)
            displacement: Current displacement (m)
            
        Returns:
            Electrostatic force (N)
        """
        # Capacitance gradient with respect to displacement
        # For comb drive: dC/dx is approximately constant
        dC_dx = (2 * self.geom.n_fingers * EPSILON_0 * EPSILON_R_AIR * 
                 self.geom.finger_thickness / self.geom.gap)
        
        # Fringing field correction
        fringing_factor = 1 + (self.geom.gap / (np.pi * self.geom.finger_thickness))
        dC_dx *= fringing_factor
        
        # Electrostatic force
        force = 0.5 * voltage**2 * dC_dx
        
        return force
    
    def calculate_spring_constant(self, beam_length: float, beam_width: float, 
                                  n_beams: int = 4) -> float:
        """
        Calculate effective spring constant of suspension beams.
        
        Assumes fixed-guided beam configuration.
        
        Args:
            beam_length: Length of suspension beam (m)
            beam_width: Width of suspension beam (m)
            n_beams: Number of suspension beams
            
        Returns:
            Spring constant (N/m)
        """
        # Moment of inertia for rectangular cross-section
        I = (beam_width * self.geom.finger_thickness**3) / 12
        
        # Spring constant for fixed-guided beam
        k_single = (24 * self.material.youngs_modulus * I) / beam_length**3
        
        # Total spring constant (parallel springs)
        k_total = n_beams * k_single
        
        return k_total
    
    def calculate_displacement(self, voltage: float, spring_constant: float) -> float:
        """
        Calculate steady-state displacement for a given voltage.
        
        Solves: k*x = F(V, x)
        
        Args:
            voltage: Applied voltage (V)
            spring_constant: Mechanical spring constant (N/m)
            
        Returns:
            Displacement (m)
        """
        # For linear regime: x = F/k where F = 0.5*V²*dC/dx
        force = self.calculate_force(voltage, 0)
        displacement = force / spring_constant
        
        return displacement
    
    def calculate_pull_in_voltage(self, spring_constant: float) -> float:
        """
        Calculate pull-in voltage (theoretical).
        
        For parallel plate: V_pi = sqrt(8*k*g³/(27*ε*A))
        For comb drive, pull-in is typically not applicable in the linear direction,
        but can occur in transverse direction.
        
        Args:
            spring_constant: Mechanical spring constant (N/m)
            
        Returns:
            Approximate transverse pull-in voltage (V)
        """
        # Transverse instability analysis (simplified)
        # Lateral spring constant (much stiffer)
        lateral_k = spring_constant * 100  # Approximation
        
        # Critical gap for pull-in
        critical_gap = self.geom.gap / 3
        
        # Pull-in voltage estimate
        area = self.geom.finger_thickness * self.geom.overlap
        V_pi = np.sqrt((8 * lateral_k * self.geom.gap**3) / 
                      (27 * EPSILON_0 * EPSILON_R_AIR * area))
        
        return V_pi
    
    def frequency_response(self, spring_constant: float, 
                          damping_ratio: float = 0.1) -> Tuple[float, float]:
        """
        Calculate resonant frequency and quality factor.
        
        Args:
            spring_constant: Mechanical spring constant (N/m)
            damping_ratio: Damping ratio (dimensionless)
            
        Returns:
            Tuple of (resonant frequency in Hz, quality factor)
        """
        # Estimate mass (fingers + portion of suspension)
        finger_volume = (self.geom.n_fingers * self.geom.finger_length * 
                        self.geom.finger_width * self.geom.finger_thickness)
        mass = self.material.density * finger_volume * 1.5  # 1.5 factor for suspension
        
        # Natural frequency
        omega_n = np.sqrt(spring_constant / mass)
        f_n = omega_n / (2 * np.pi)
        
        # Quality factor
        Q = 1 / (2 * damping_ratio)
        
        return f_n, Q
    
    def plot_force_displacement(self, voltage_range: np.ndarray, 
                               spring_constant: float,
                               save_path: Optional[str] = None):
        """
        Plot force and displacement vs. voltage characteristics.
        
        Args:
            voltage_range: Array of voltages to analyze (V)
            spring_constant: Mechanical spring constant (N/m)
            save_path: Optional path to save figure
        """
        forces = []
        displacements = []
        
        for V in voltage_range:
            F = self.calculate_force(V, 0)
            x = self.calculate_displacement(V, spring_constant)
            forces.append(F * 1e6)  # Convert to μN
            displacements.append(x * 1e6)  # Convert to μm
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # Force vs. Voltage
        ax1.plot(voltage_range, forces, 'b-', linewidth=2)
        ax1.set_xlabel('Voltage (V)', fontsize=12)
        ax1.set_ylabel('Electrostatic Force (μN)', fontsize=12)
        ax1.set_title('Comb Drive Force Characteristics', fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        
        # Displacement vs. Voltage
        ax2.plot(voltage_range, displacements, 'r-', linewidth=2)
        ax2.set_xlabel('Voltage (V)', fontsize=12)
        ax2.set_ylabel('Displacement (μm)', fontsize=12)
        ax2.set_title('Comb Drive Displacement Characteristics', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
    
    def plot_capacitance_vs_displacement(self, displacement_range: np.ndarray,
                                        save_path: Optional[str] = None):
        """
        Plot capacitance vs. displacement.
        
        Args:
            displacement_range: Array of displacements (m)
            save_path: Optional path to save figure
        """
        capacitances = [self.calculate_capacitance(x) * 1e15  # Convert to fF
                       for x in displacement_range]
        
        plt.figure(figsize=(10, 6))
        plt.plot(displacement_range * 1e6, capacitances, 'g-', linewidth=2)
        plt.xlabel('Displacement (μm)', fontsize=12)
        plt.ylabel('Capacitance (fF)', fontsize=12)
        plt.title('Comb Drive Capacitance vs. Displacement', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
    
    def visualize_3d_structure(self, displacement: float = 0.0, 
                              show_fields: bool = False,
                              save_path: Optional[str] = None):
        """
        Create 3D visualization of the comb drive structure.
        
        Args:
            displacement: Current displacement to visualize (m)
            show_fields: Whether to show electric field lines
            save_path: Optional path to save figure
        """
        fig = plt.figure(figsize=(14, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Create fixed comb (blue)
        for i in range(self.geom.n_fingers):
            y_pos = i * self.geom.finger_separation
            self._draw_finger(ax, 0, y_pos, 0, 'blue', alpha=0.6, label='Fixed' if i == 0 else '')
        
        # Create movable comb (red) - displaced
        x_offset = displacement * 1e6  # Convert to μm for visualization
        for i in range(self.geom.n_fingers):
            y_pos = i * self.geom.finger_separation + self.geom.finger_separation/2
            self._draw_finger(ax, x_offset, y_pos, 0, 'red', alpha=0.6, 
                            label='Movable' if i == 0 else '')
        
        # Add electric field visualization if requested
        if show_fields:
            self._draw_field_lines(ax, displacement)
        
        # Formatting
        ax.set_xlabel('X (μm)', fontsize=12)
        ax.set_ylabel('Y (μm)', fontsize=12)
        ax.set_zlabel('Z (μm)', fontsize=12)
        ax.set_title(f'3D Comb Drive Structure (Displacement: {displacement*1e6:.2f} μm)', 
                    fontsize=14, fontweight='bold')
        ax.legend(fontsize=10)
        
        # Set equal aspect ratio
        max_range = max(self.geom.finger_length, 
                       self.geom.n_fingers * self.geom.finger_separation) * 1e6
        ax.set_xlim([-max_range/4, max_range/2])
        ax.set_ylim([0, max_range])
        ax.set_zlim([0, self.geom.finger_thickness * 1e6 * 2])
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
    
    def _draw_finger(self, ax, x_offset, y_base, z_base, color, alpha=0.7, label=''):
        """Helper function to draw a single finger in 3D."""
        # Convert to μm for visualization
        length = self.geom.finger_length * 1e6
        width = self.geom.finger_width * 1e6
        thickness = self.geom.finger_thickness * 1e6
        
        # Define vertices of the rectangular finger
        vertices = [
            [x_offset, y_base, z_base],
            [x_offset + length, y_base, z_base],
            [x_offset + length, y_base + width, z_base],
            [x_offset, y_base + width, z_base],
            [x_offset, y_base, z_base + thickness],
            [x_offset + length, y_base, z_base + thickness],
            [x_offset + length, y_base + width, z_base + thickness],
            [x_offset, y_base + width, z_base + thickness]
        ]
        
        # Define the 6 faces
        faces = [
            [vertices[0], vertices[1], vertices[5], vertices[4]],  # Front
            [vertices[2], vertices[3], vertices[7], vertices[6]],  # Back
            [vertices[0], vertices[3], vertices[7], vertices[4]],  # Left
            [vertices[1], vertices[2], vertices[6], vertices[5]],  # Right
            [vertices[0], vertices[1], vertices[2], vertices[3]],  # Bottom
            [vertices[4], vertices[5], vertices[6], vertices[7]]   # Top
        ]
        
        # Create and add the 3D polygon collection
        poly = Poly3DCollection(faces, alpha=alpha, facecolor=color, 
                               edgecolor='black', linewidth=0.5, label=label)
        ax.add_collection3d(poly)
    
    def _draw_field_lines(self, ax, displacement):
        """Helper function to draw electric field lines between fingers."""
        gap_um = self.geom.gap * 1e6
        
        for i in range(self.geom.n_fingers):
            y_fixed = i * self.geom.finger_separation * 1e6
            y_movable = (i * self.geom.finger_separation + 
                        self.geom.finger_separation/2) * 1e6
            
            # Draw field lines (simplified)
            x_start = self.geom.finger_length * 1e6 / 2
            x_end = displacement * 1e6 + self.geom.finger_length * 1e6 / 2
            
            for j in range(3):
                z_pos = j * self.geom.finger_thickness * 1e6 / 3
                ax.plot([x_start, x_end], 
                       [y_fixed + self.geom.finger_width * 1e6, y_movable],
                       [z_pos, z_pos], 
                       'g--', alpha=0.3, linewidth=0.5)
    
    def generate_report(self, voltage: float, spring_constant: float, 
                       beam_length: float, beam_width: float) -> str:
        """
        Generate a comprehensive analysis report.
        
        Args:
            voltage: Operating voltage (V)
            spring_constant: Mechanical spring constant (N/m)
            beam_length: Suspension beam length (m)
            beam_width: Suspension beam width (m)
            
        Returns:
            Formatted report string
        """
        # Calculate key parameters
        C = self.calculate_capacitance(0)
        F = self.calculate_force(voltage, 0)
        x = self.calculate_displacement(voltage, spring_constant)
        V_pi = self.calculate_pull_in_voltage(spring_constant)
        f_n, Q = self.frequency_response(spring_constant)
        
        report = f"""
╔══════════════════════════════════════════════════════════════╗
║         COMB DRIVE ACTUATOR ANALYSIS REPORT                  ║
╚══════════════════════════════════════════════════════════════╝

GEOMETRY PARAMETERS:
────────────────────────────────────────────────────────────────
  Number of Fingers:        {self.geom.n_fingers}
  Finger Length:            {self.geom.finger_length*1e6:.2f} μm
  Finger Width:             {self.geom.finger_width*1e6:.2f} μm
  Finger Thickness:         {self.geom.finger_thickness*1e6:.2f} μm
  Gap:                      {self.geom.gap*1e6:.2f} μm
  Initial Overlap:          {self.geom.overlap*1e6:.2f} μm

SUSPENSION PARAMETERS:
────────────────────────────────────────────────────────────────
  Beam Length:              {beam_length*1e6:.2f} μm
  Beam Width:               {beam_width*1e6:.2f} μm
  Spring Constant:          {spring_constant:.4f} N/m

ELECTRICAL PERFORMANCE @ {voltage}V:
────────────────────────────────────────────────────────────────
  Capacitance:              {C*1e15:.4f} fF
  Electrostatic Force:      {F*1e6:.4f} μN
  Displacement:             {x*1e6:.4f} μm
  Pull-in Voltage (est.):   {V_pi:.2f} V

DYNAMIC CHARACTERISTICS:
────────────────────────────────────────────────────────────────
  Resonant Frequency:       {f_n/1e3:.2f} kHz
  Quality Factor:           {Q:.1f}

DESIGN RECOMMENDATIONS:
────────────────────────────────────────────────────────────────
  Maximum Safe Voltage:     {V_pi*0.7:.2f} V (70% of pull-in)
  Recommended Op. Range:    0 - {x*1e6*1.5:.2f} μm
  Bandwidth (-3dB):         {f_n*Q/1e3:.2f} kHz

"""
        return report


def example_analysis():
    """
    Example analysis of a typical MEMS comb drive.
    """
    print("=" * 70)
    print("COMB DRIVE ANALYSIS EXAMPLE")
    print("=" * 70)
    
    # Define geometry (typical MEMS dimensions)
    geometry = CombDriveGeometry(
        n_fingers=50,
        finger_length=100e-6,      # 100 μm
        finger_width=4e-6,          # 4 μm
        finger_thickness=10e-6,     # 10 μm
        gap=2e-6,                   # 2 μm
        overlap=80e-6,              # 80 μm
        finger_separation=10e-6     # 10 μm
    )
    
    # Create analyzer
    analyzer = CombDriveAnalyzer(geometry)
    
    # Suspension parameters
    beam_length = 300e-6   # 300 μm
    beam_width = 4e-6      # 4 μm
    n_beams = 4
    
    k = analyzer.calculate_spring_constant(beam_length, beam_width, n_beams)
    
    # Generate report
    report = analyzer.generate_report(
        voltage=10.0,
        spring_constant=k,
        beam_length=beam_length,
        beam_width=beam_width
    )
    print(report)
    
    # Create plots
    print("\nGenerating analysis plots...")
    
    # Force-displacement characteristics
    voltages = np.linspace(0, 20, 100)
    analyzer.plot_force_displacement(voltages, k)
    
    # Capacitance vs displacement
    displacements = np.linspace(-20e-6, 20e-6, 100)
    analyzer.plot_capacitance_vs_displacement(displacements)
    
    # 3D visualization
    analyzer.visualize_3d_structure(displacement=5e-6, show_fields=True)
    
    print("\nAnalysis complete!")


def optimize_comb_drive(target_force: float, target_voltage: float, 
                       constraints: dict) -> CombDriveGeometry:
    """
    Optimize comb drive geometry for target specifications.
    
    Args:
        target_force: Target electrostatic force (N)
        target_voltage: Operating voltage (V)
        constraints: Dictionary of geometric constraints
        
    Returns:
        Optimized CombDriveGeometry object
    """
    print("Optimizing comb drive design...")
    print(f"Target Force: {target_force*1e6:.2f} μN @ {target_voltage} V")
    
    # Simple optimization: adjust number of fingers and overlap
    def objective(params):
        n_fingers, overlap = params
        n_fingers = int(n_fingers)
        
        geom = CombDriveGeometry(
            n_fingers=n_fingers,
            finger_length=constraints.get('finger_length', 100e-6),
            finger_width=constraints.get('finger_width', 4e-6),
            finger_thickness=constraints.get('finger_thickness', 10e-6),
            gap=constraints.get('gap', 2e-6),
            overlap=overlap,
            finger_separation=constraints.get('finger_separation', 10e-6)
        )
        
        analyzer = CombDriveAnalyzer(geom)
        force = analyzer.calculate_force(target_voltage, 0)
        
        return abs(force - target_force)
    
    # Initial guess
    x0 = [50, 80e-6]
    
    # Bounds
    bounds = [(10, 200), (20e-6, 200e-6)]
    
    # Optimize
    result = opt.minimize(objective, x0, bounds=bounds, method='L-BFGS-B')
    
    n_opt, overlap_opt = result.x
    n_opt = int(n_opt)
    
    optimal_geom = CombDriveGeometry(
        n_fingers=n_opt,
        finger_length=constraints.get('finger_length', 100e-6),
        finger_width=constraints.get('finger_width', 4e-6),
        finger_thickness=constraints.get('finger_thickness', 10e-6),
        gap=constraints.get('gap', 2e-6),
        overlap=overlap_opt,
        finger_separation=constraints.get('finger_separation', 10e-6)
    )
    
    print(f"\nOptimized Design:")
    print(f"  Number of Fingers: {n_opt}")
    print(f"  Overlap: {overlap_opt*1e6:.2f} μm")
    
    return optimal_geom


if __name__ == "__main__":
    # Run example analysis
    example_analysis()
    
    # Optional: Run optimization
    print("\n" + "="*70)
    print("DESIGN OPTIMIZATION EXAMPLE")
    print("="*70 + "\n")
    
    constraints = {
        'finger_length': 100e-6,
        'finger_width': 4e-6,
        'finger_thickness': 10e-6,
        'gap': 2e-6,
        'finger_separation': 10e-6
    }
    
    optimal_geom = optimize_comb_drive(
        target_force=50e-6,  # 50 μN
        target_voltage=15.0,  # 15 V
        constraints=constraints
    )
    
    # Analyze optimal design
    analyzer = CombDriveAnalyzer(optimal_geom)
    k = analyzer.calculate_spring_constant(300e-6, 4e-6, 4)
    
    print("\n" + analyzer.generate_report(15.0, k, 300e-6, 4e-6))