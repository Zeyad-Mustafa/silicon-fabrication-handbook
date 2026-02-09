"""
3D Oxide Growth Model (Deal-Grove Kinetics)
Silicon Fabrication Handbook

This module provides comprehensive analysis and visualization tools for thermal
oxidation of silicon, based on the Deal-Grove model. Includes:

- Linear and parabolic growth regimes
- Temperature-dependent rate constants
- Wet vs. dry oxidation kinetics
- Orientation dependence (<100>, <110>, <111>)
- 3D visualization of oxide layer growth over time
- Stress and defect formation analysis
- Process optimization and prediction tools

The Deal-Grove model describes oxide thickness growth as:
    x²_ox + A·x_ox = B(t + τ)

where:
- x_ox is oxide thickness
- A is the linear rate constant
- B is the parabolic rate constant
- t is oxidation time
- τ is an initial time offset

Usage
-----
Run stand-alone for demonstration:
    python oxide_growth_model_3D.py

Or import for custom analysis:
    from oxide_growth_model_3D import OxidationParameters, OxideGrowthAnalyzer

Author: Silicon Fabrication Handbook Project
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import cm
from matplotlib.colors import Normalize
import scipy.optimize as opt
from scipy.integrate import odeint
from dataclasses import dataclass
from typing import Tuple, List, Optional, Dict
import warnings
import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Image output directory setup
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent.resolve()
IMAGE_DIR = SCRIPT_DIR / "images" / "oxide"
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

def get_image_path(filename: str) -> str:
    """Get full path for saving an image in the organized directory structure."""
    return str(IMAGE_DIR / filename)

# ---------------------------------------------------------------------------
# Physical constants
# ---------------------------------------------------------------------------
K_B = 1.380649e-23      # Boltzmann constant (J/K)
Q = 1.602176634e-19     # Elementary charge (C)
R_GAS = 8.314           # Universal gas constant (J/mol·K)

# Silicon and SiO2 properties
RHO_SI = 2.33           # Silicon density (g/cm³)
RHO_SIO2 = 2.27         # SiO2 density (g/cm³)
MW_SI = 28.086          # Silicon molecular weight (g/mol)
MW_SIO2 = 60.084        # SiO2 molecular weight (g/mol)

# Volume expansion ratio
ALPHA = 2.27 / 2.33     # ≈ 0.44 of silicon consumed

# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class OxidationParameters:
    """
    Parameters for thermal oxidation process.
    
    Attributes
    ----------
    temperature      : float   Oxidation temperature               (K)
    ambient          : str     'dry' or 'wet' or 'steam'
    pressure         : float   Oxidation pressure                  (atm)
    orientation      : str     '<100>', '<110>', or '<111>'
    initial_oxide    : float   Initial oxide thickness (if any)    (nm)
    """
    temperature:  float
    ambient:      str = 'dry'
    pressure:     float = 1.0
    orientation:  str = '<100>'
    initial_oxide: float = 0.0
    
    def __post_init__(self):
        if self.temperature < 800 or self.temperature > 1400:
            warnings.warn("Temperature outside typical range (800-1400 K)")
        if self.ambient not in ['dry', 'wet', 'steam']:
            raise ValueError("ambient must be 'dry', 'wet', or 'steam'")
        if self.orientation not in ['<100>', '<110>', '<111>']:
            raise ValueError("orientation must be '<100>', '<110>', or '<111>'")


@dataclass
class DealGroveCoefficients:
    """
    Deal-Grove model coefficients A and B.
    
    Attributes
    ----------
    A : float   Linear rate coefficient       (nm)
    B : float   Parabolic rate coefficient    (nm²/min)
    tau : float Initial time offset           (min)
    """
    A: float
    B: float
    tau: float = 0.0


# ---------------------------------------------------------------------------
# Core oxide growth analyzer
# ---------------------------------------------------------------------------

class OxideGrowthAnalyzer:
    """
    Comprehensive thermal oxidation analyzer based on Deal-Grove model.
    
    Parameters
    ----------
    parameters : OxidationParameters
    """
    
    def __init__(self, parameters: OxidationParameters):
        self.params = parameters
        self.coeffs = self._calculate_deal_grove_coefficients()
    
    # ==================================================================
    # 1. DEAL-GROVE COEFFICIENT CALCULATION
    # ==================================================================
    
    def _calculate_deal_grove_coefficients(self) -> DealGroveCoefficients:
        """
        Calculate Deal-Grove A and B coefficients based on temperature and ambient.
        
        These are empirical fits to experimental data.
        
        Returns
        -------
        DealGroveCoefficients
        """
        T = self.params.temperature
        
        # Activation energies (eV)
        if self.params.ambient == 'dry':
            # Dry O2
            E_A_B = 1.23  # eV (parabolic)
            E_A_A = 2.0   # eV (linear)
            B_0 = 7.72e7  # nm²/min
            A_0 = 6.23e6  # nm
        elif self.params.ambient == 'wet':
            # H2O (wet oxidation)
            E_A_B = 0.78  # eV
            E_A_A = 2.05  # eV
            B_0 = 3.86e8  # nm²/min
            A_0 = 3.71e6  # nm
        else:  # steam
            E_A_B = 0.78
            E_A_A = 2.0
            B_0 = 5e8
            A_0 = 4e6
        
        # Temperature dependence: Arrhenius form
        B = B_0 * np.exp(-E_A_B * Q / (K_B * T))
        A = A_0 * np.exp(-E_A_A * Q / (K_B * T))
        
        # Pressure dependence (simplified)
        B *= self.params.pressure
        A *= self.params.pressure
        
        # Orientation factor (relative to <100>)
        if self.params.orientation == '<110>':
            orientation_factor = 1.68
        elif self.params.orientation == '<111>':
            orientation_factor = 1.20
        else:  # <100>
            orientation_factor = 1.0
        
        B *= orientation_factor
        
        # Initial time offset (if initial oxide present)
        if self.params.initial_oxide > 0:
            x_i = self.params.initial_oxide
            tau = (x_i**2 + A * x_i) / B
        else:
            tau = 0.0
        
        return DealGroveCoefficients(A=A, B=B, tau=tau)
    
    # ==================================================================
    # 2. OXIDE THICKNESS CALCULATION
    # ==================================================================
    
    def oxide_thickness(self, time: float) -> float:
        """
        Calculate oxide thickness using Deal-Grove equation.
        
        Solves: x² + A·x = B(t + τ)
        
        Parameters
        ----------
        time : float   Oxidation time (min)
        
        Returns
        -------
        thickness : float   Oxide thickness (nm)
        """
        A = self.coeffs.A
        B = self.coeffs.B
        tau = self.coeffs.tau
        
        # Quadratic formula solution
        discriminant = A**2 + 4 * B * (time + tau)
        if discriminant < 0:
            return 0.0
        
        thickness = (-A + np.sqrt(discriminant)) / 2.0
        return max(0.0, thickness)
    
    def growth_rate(self, time: float) -> float:
        """
        Calculate instantaneous growth rate dx/dt.
        
        From Deal-Grove: dx/dt = B / (2x + A)
        
        Parameters
        ----------
        time : float   Oxidation time (min)
        
        Returns
        -------
        rate : float   Growth rate (nm/min)
        """
        x = self.oxide_thickness(time)
        if x < 1e-10:
            return self.coeffs.B / self.coeffs.A  # Linear regime limit
        
        return self.coeffs.B / (2 * x + self.coeffs.A)
    
    def time_for_thickness(self, target_thickness: float) -> float:
        """
        Calculate time required to grow oxide to target thickness.
        
        Parameters
        ----------
        target_thickness : float   Desired oxide thickness (nm)
        
        Returns
        -------
        time : float   Required oxidation time (min)
        """
        A = self.coeffs.A
        B = self.coeffs.B
        tau = self.coeffs.tau
        
        x = target_thickness
        time = (x**2 + A * x) / B - tau
        return max(0.0, time)
    
    # ==================================================================
    # 3. REGIME ANALYSIS
    # ==================================================================
    
    def identify_regime(self, time: float) -> str:
        """
        Identify oxidation regime (linear vs parabolic).
        
        Linear regime: thin oxides, t << A²/(4B)
        Parabolic regime: thick oxides, t >> A²/(4B)
        
        Parameters
        ----------
        time : float   Oxidation time (min)
        
        Returns
        -------
        regime : str   'linear', 'transition', or 'parabolic'
        """
        t_transition = self.coeffs.A**2 / (4 * self.coeffs.B)
        
        if time < 0.1 * t_transition:
            return 'linear'
        elif time > 10 * t_transition:
            return 'parabolic'
        else:
            return 'transition'
    
    def linear_rate_constant(self) -> float:
        """
        Calculate linear rate constant B/A (nm/min).
        
        Valid in thin oxide regime.
        """
        return self.coeffs.B / self.coeffs.A
    
    def parabolic_rate_constant(self) -> float:
        """
        Calculate parabolic rate constant B (nm²/min).
        
        Valid in thick oxide regime.
        """
        return self.coeffs.B
    
    # ==================================================================
    # 4. STRESS AND CONSUMED SILICON
    # ==================================================================
    
    def silicon_consumed(self, oxide_thickness: float) -> float:
        """
        Calculate thickness of silicon consumed during oxidation.
        
        Parameters
        ----------
        oxide_thickness : float   Oxide thickness (nm)
        
        Returns
        -------
        si_consumed : float   Silicon consumed (nm)
        """
        # From volume ratio: 0.44 of oxide thickness comes from Si
        return oxide_thickness * ALPHA
    
    def volumetric_stress(self, oxide_thickness: float) -> float:
        """
        Estimate volumetric compressive stress in oxide (simplified).
        
        Stress arises from volume expansion during oxidation.
        
        Parameters
        ----------
        oxide_thickness : float   Oxide thickness (nm)
        
        Returns
        -------
        stress : float   Approximate stress (MPa)
        """
        # Empirical model (very simplified)
        # Real stress depends on many factors including temperature history
        
        # Thermal expansion mismatch coefficient
        delta_alpha = 0.5e-6  # 1/K (SiO2 - Si difference)
        delta_T = self.params.temperature - 300  # Cool-down from oxidation temp
        
        # Young's modulus of SiO2
        E_oxide = 70e3  # MPa
        nu = 0.17  # Poisson's ratio
        
        # Thermal stress (simplified)
        thermal_stress = E_oxide / (1 - nu) * delta_alpha * delta_T
        
        # Growth stress (volume expansion)
        growth_stress = 300  # MPa (typical compressive)
        
        total_stress = thermal_stress + growth_stress
        return total_stress
    
    # ==================================================================
    # 5. PLOTTING FUNCTIONS
    # ==================================================================
    
    def plot_thickness_vs_time(self,
                               time_range: Optional[Tuple[float, float]] = None,
                               log_scale: bool = False,
                               save_path: Optional[str] = None,
                               auto_save: bool = True):
        """
        Plot oxide thickness vs. oxidation time.
        
        Parameters
        ----------
        time_range : tuple   (t_min, t_max) in minutes
        log_scale  : bool    Use log-log scale
        save_path  : str     Custom save path
        auto_save  : bool    Auto-save to images/oxide/
        """
        if time_range is None:
            # Auto-determine reasonable time range
            if self.params.ambient == 'dry':
                time_range = (0.1, 1000)  # minutes
            else:
                time_range = (0.1, 500)
        
        if log_scale:
            time_array = np.logspace(np.log10(time_range[0]), 
                                    np.log10(time_range[1]), 300)
        else:
            time_array = np.linspace(time_range[0], time_range[1], 300)
        
        thickness_array = np.array([self.oxide_thickness(t) for t in time_array])
        
        plt.figure(figsize=(10, 7))
        plt.plot(time_array, thickness_array, 'b-', linewidth=2.5)
        
        # Mark regime transitions
        t_trans = self.coeffs.A**2 / (4 * self.coeffs.B)
        if time_range[0] < t_trans < time_range[1]:
            x_trans = self.oxide_thickness(t_trans)
            plt.axvline(t_trans, color='orange', linestyle='--', linewidth=1.5,
                       label=f'Transition time: {t_trans:.1f} min')
            plt.plot(t_trans, x_trans, 'ro', markersize=8)
        
        plt.xlabel('Oxidation Time (min)', fontsize=12)
        plt.ylabel('Oxide Thickness (nm)', fontsize=12)
        plt.title(f'Deal-Grove Oxide Growth\n'
                 f'{self.params.ambient.capitalize()} O₂, T = {self.params.temperature:.0f} K, '
                 f'{self.params.orientation}',
                 fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        
        if log_scale:
            plt.xscale('log')
            plt.yscale('log')
        
        plt.legend(fontsize=10)
        
        # Determine save path
        if save_path:
            final_path = save_path
        elif auto_save:
            suffix = '_log' if log_scale else ''
            final_path = get_image_path(f'thickness_vs_time{suffix}.png')
        else:
            final_path = None
        
        if final_path:
            plt.savefig(final_path, dpi=300, bbox_inches='tight')
            print(f"  → Saved: {final_path}")
        
        plt.show()
    
    def plot_growth_rate(self,
                        time_range: Optional[Tuple[float, float]] = None,
                        save_path: Optional[str] = None,
                        auto_save: bool = True):
        """
        Plot instantaneous growth rate vs. time.
        
        Shows transition from linear to parabolic regime.
        """
        if time_range is None:
            if self.params.ambient == 'dry':
                time_range = (0.1, 1000)
            else:
                time_range = (0.1, 500)
        
        time_array = np.logspace(np.log10(time_range[0]), 
                                np.log10(time_range[1]), 300)
        rate_array = np.array([self.growth_rate(t) for t in time_array])
        
        plt.figure(figsize=(10, 7))
        plt.plot(time_array, rate_array, 'r-', linewidth=2.5)
        
        plt.xlabel('Oxidation Time (min)', fontsize=12)
        plt.ylabel('Growth Rate (nm/min)', fontsize=12)
        plt.title(f'Oxide Growth Rate vs. Time\n'
                 f'{self.params.ambient.capitalize()} O₂, T = {self.params.temperature:.0f} K',
                 fontsize=14, fontweight='bold')
        plt.xscale('log')
        plt.yscale('log')
        plt.grid(True, alpha=0.3, which='both')
        
        # Determine save path
        if save_path:
            final_path = save_path
        elif auto_save:
            final_path = get_image_path('growth_rate.png')
        else:
            final_path = None
        
        if final_path:
            plt.savefig(final_path, dpi=300, bbox_inches='tight')
            print(f"  → Saved: {final_path}")
        
        plt.show()
    
    def plot_temperature_dependence(self,
                                   temp_range: Tuple[float, float] = (900, 1300),
                                   fixed_time: float = 60.0,
                                   save_path: Optional[str] = None,
                                   auto_save: bool = True):
        """
        Plot oxide thickness vs. temperature at fixed time.
        
        Shows Arrhenius temperature dependence.
        """
        temps = np.linspace(temp_range[0], temp_range[1], 100)
        thicknesses = []
        
        original_temp = self.params.temperature
        
        for T in temps:
            self.params.temperature = T
            self.coeffs = self._calculate_deal_grove_coefficients()
            thickness = self.oxide_thickness(fixed_time)
            thicknesses.append(thickness)
        
        # Restore original temperature
        self.params.temperature = original_temp
        self.coeffs = self._calculate_deal_grove_coefficients()
        
        plt.figure(figsize=(10, 7))
        plt.plot(temps, thicknesses, 'g-', linewidth=2.5)
        plt.xlabel('Temperature (K)', fontsize=12)
        plt.ylabel(f'Oxide Thickness at t = {fixed_time} min (nm)', fontsize=12)
        plt.title(f'Temperature Dependence of Oxide Growth\n'
                 f'{self.params.ambient.capitalize()} O₂',
                 fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        
        # Add Celsius scale on top
        ax2 = plt.gca().twiny()
        ax2.set_xlim(temp_range[0] - 273, temp_range[1] - 273)
        ax2.set_xlabel('Temperature (°C)', fontsize=12)
        
        # Determine save path
        if save_path:
            final_path = save_path
        elif auto_save:
            final_path = get_image_path('temperature_dependence.png')
        else:
            final_path = None
        
        if final_path:
            plt.savefig(final_path, dpi=300, bbox_inches='tight')
            print(f"  → Saved: {final_path}")
        
        plt.show()
    
    def plot_wet_vs_dry(self,
                       time_range: Tuple[float, float] = (1, 500),
                       save_path: Optional[str] = None,
                       auto_save: bool = True):
        """
        Compare wet and dry oxidation at same temperature.
        """
        time_array = np.logspace(np.log10(time_range[0]), 
                                np.log10(time_range[1]), 300)
        
        # Store original ambient
        original_ambient = self.params.ambient
        
        # Dry oxidation
        self.params.ambient = 'dry'
        self.coeffs = self._calculate_deal_grove_coefficients()
        thickness_dry = np.array([self.oxide_thickness(t) for t in time_array])
        
        # Wet oxidation
        self.params.ambient = 'wet'
        self.coeffs = self._calculate_deal_grove_coefficients()
        thickness_wet = np.array([self.oxide_thickness(t) for t in time_array])
        
        # Restore original
        self.params.ambient = original_ambient
        self.coeffs = self._calculate_deal_grove_coefficients()
        
        plt.figure(figsize=(10, 7))
        plt.plot(time_array, thickness_dry, 'b-', linewidth=2.5, label='Dry O₂')
        plt.plot(time_array, thickness_wet, 'r-', linewidth=2.5, label='Wet O₂ (H₂O)')
        
        plt.xlabel('Oxidation Time (min)', fontsize=12)
        plt.ylabel('Oxide Thickness (nm)', fontsize=12)
        plt.title(f'Wet vs. Dry Oxidation Comparison\n'
                 f'T = {self.params.temperature:.0f} K, {self.params.orientation}',
                 fontsize=14, fontweight='bold')
        plt.xscale('log')
        plt.yscale('log')
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3, which='both')
        
        # Determine save path
        if save_path:
            final_path = save_path
        elif auto_save:
            final_path = get_image_path('wet_vs_dry.png')
        else:
            final_path = None
        
        if final_path:
            plt.savefig(final_path, dpi=300, bbox_inches='tight')
            print(f"  → Saved: {final_path}")
        
        plt.show()
    
    def plot_3d_growth_animation(self,
                                time_points: List[float] = None,
                                save_path: Optional[str] = None,
                                auto_save: bool = True):
        """
        3D visualization of oxide layer growth over time.
        
        Shows silicon substrate with growing oxide layer.
        """
        if time_points is None:
            # Select representative time points
            if self.params.ambient == 'dry':
                time_points = [1, 10, 60, 180, 360]
            else:
                time_points = [1, 5, 30, 90, 180]
        
        fig = plt.figure(figsize=(14, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Base substrate dimensions (arbitrary units for visualization)
        substrate_L = 200  # nm (lateral)
        substrate_W = 200  # nm
        substrate_H = 100  # nm (depth)
        
        # Draw substrate (gray)
        self._draw_box(ax, 0, substrate_L, 0, substrate_W, -substrate_H, 0,
                      color='lightgray', alpha=0.5, label='Si Substrate')
        
        # Color map for time evolution
        cmap = cm.viridis
        norm = Normalize(vmin=0, vmax=len(time_points)-1)
        
        for i, t in enumerate(time_points):
            oxide_thickness = self.oxide_thickness(t)
            si_consumed = self.silicon_consumed(oxide_thickness)
            
            color = cmap(norm(i))
            
            # Draw oxide layer
            z_bottom = -si_consumed
            z_top = oxide_thickness - si_consumed
            
            # Offset in Y to show multiple layers side-by-side
            y_offset = i * (substrate_W / len(time_points))
            y_width = substrate_W / (len(time_points) + 1)
            
            self._draw_box(ax, 0, substrate_L, y_offset, y_width, 
                          z_bottom, z_top,
                          color=color, alpha=0.7,
                          label=f't = {t:.0f} min, x_ox = {oxide_thickness:.1f} nm')
        
        ax.set_xlabel('Length (nm)', fontsize=11)
        ax.set_ylabel('Width (nm)', fontsize=11)
        ax.set_zlabel('Height (nm)', fontsize=11)
        ax.set_title(f'3D Oxide Growth Evolution\n'
                    f'{self.params.ambient.capitalize()} O₂, T = {self.params.temperature:.0f} K',
                    fontsize=14, fontweight='bold')
        
        ax.legend(fontsize=9, loc='upper left')
        ax.view_init(elev=25, azim=45)
        
        # Determine save path
        if save_path:
            final_path = save_path
        elif auto_save:
            final_path = get_image_path('3d_growth_evolution.png')
        else:
            final_path = None
        
        if final_path:
            plt.savefig(final_path, dpi=300, bbox_inches='tight')
            print(f"  → Saved: {final_path}")
        
        plt.show()
    
    def plot_3d_cross_section(self,
                             time: float = 60.0,
                             save_path: Optional[str] = None,
                             auto_save: bool = True):
        """
        Detailed 3D cross-section showing oxide layer and consumed silicon.
        """
        oxide_thickness = self.oxide_thickness(time)
        si_consumed = self.silicon_consumed(oxide_thickness)
        
        fig = plt.figure(figsize=(12, 9))
        ax = fig.add_subplot(111, projection='3d')
        
        # Dimensions
        L = 300  # nm (lateral extent)
        W = 200  # nm
        
        # Silicon substrate
        substrate_depth = 200  # nm
        self._draw_box(ax, 0, L, 0, W, -substrate_depth, -si_consumed,
                      color='dimgray', alpha=0.6, label='Si Substrate')
        
        # Consumed silicon (interface region)
        self._draw_box(ax, 0, L, 0, W, -si_consumed, 0,
                      color='salmon', alpha=0.4, label=f'Consumed Si ({si_consumed:.1f} nm)')
        
        # Oxide layer
        self._draw_box(ax, 0, L, 0, W, 0, oxide_thickness,
                      color='lightblue', alpha=0.8, label=f'SiO₂ ({oxide_thickness:.1f} nm)')
        
        # Original silicon surface reference
        self._draw_wireframe_plane(ax, 0, L, 0, W, 0, color='red', 
                                   linewidth=1.5, label='Original Si surface')
        
        ax.set_xlabel('Length (nm)', fontsize=11)
        ax.set_ylabel('Width (nm)', fontsize=11)
        ax.set_zlabel('Height (nm)', fontsize=11)
        ax.set_title(f'Oxide Cross-Section after t = {time:.0f} min\n'
                    f'{self.params.ambient.capitalize()} O₂, T = {self.params.temperature:.0f} K, '
                    f'{self.params.orientation}',
                    fontsize=13, fontweight='bold')
        
        ax.legend(fontsize=10)
        ax.view_init(elev=20, azim=135)
        
        # Determine save path
        if save_path:
            final_path = save_path
        elif auto_save:
            final_path = get_image_path('3d_cross_section.png')
        else:
            final_path = None
        
        if final_path:
            plt.savefig(final_path, dpi=300, bbox_inches='tight')
            print(f"  → Saved: {final_path}")
        
        plt.show()
    
    @staticmethod
    def _draw_box(ax, x0, x1, y0, y1, z0, z1, color='gray', alpha=0.7, label=''):
        """Draw a 3D box."""
        vertices = np.array([
            [x0, y0, z0], [x1, y0, z0], [x1, y1, z0], [x0, y1, z0],
            [x0, y0, z1], [x1, y0, z1], [x1, y1, z1], [x0, y1, z1]
        ])
        
        faces = [
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[2], vertices[3], vertices[7], vertices[6]],
            [vertices[0], vertices[3], vertices[7], vertices[4]],
            [vertices[1], vertices[2], vertices[6], vertices[5]],
            [vertices[0], vertices[1], vertices[2], vertices[3]],
            [vertices[4], vertices[5], vertices[6], vertices[7]]
        ]
        
        poly = Poly3DCollection(faces, alpha=alpha, facecolor=color,
                               edgecolor='black', linewidth=0.4)
        if label:
            poly.set_label(label)
        ax.add_collection3d(poly)
    
    @staticmethod
    def _draw_wireframe_plane(ax, x0, x1, y0, y1, z, color='red', linewidth=1, label=''):
        """Draw a wireframe plane at constant z."""
        # Draw rectangle outline
        x_corners = [x0, x1, x1, x0, x0]
        y_corners = [y0, y0, y1, y1, y0]
        z_corners = [z, z, z, z, z]
        ax.plot(x_corners, y_corners, z_corners, color=color, 
               linewidth=linewidth, linestyle='--', label=label)
    
    # ==================================================================
    # 6. REPORT
    # ==================================================================
    
    def generate_report(self, time: float = 60.0) -> str:
        """
        Generate comprehensive oxidation analysis report.
        
        Parameters
        ----------
        time : float   Oxidation time for analysis (min)
        
        Returns
        -------
        str : Formatted report
        """
        thickness = self.oxide_thickness(time)
        rate = self.growth_rate(time)
        regime = self.identify_regime(time)
        si_consumed = self.silicon_consumed(thickness)
        stress = self.volumetric_stress(thickness)
        
        t_100nm = self.time_for_thickness(100.0)
        t_500nm = self.time_for_thickness(500.0)
        t_1000nm = self.time_for_thickness(1000.0)
        
        report = f"""
╔══════════════════════════════════════════════════════════════╗
║           THERMAL OXIDATION ANALYSIS REPORT                  ║
╚══════════════════════════════════════════════════════════════╝

PROCESS PARAMETERS:
────────────────────────────────────────────────────────────────
  Ambient:                  {self.params.ambient.upper()}
  Temperature:              {self.params.temperature:>10.1f} K ({self.params.temperature-273:.1f} °C)
  Pressure:                 {self.params.pressure:>10.2f} atm
  Orientation:              {self.params.orientation}
  Initial Oxide:            {self.params.initial_oxide:>10.2f} nm

DEAL-GROVE COEFFICIENTS:
────────────────────────────────────────────────────────────────
  Linear Constant (B/A):    {self.coeffs.B/self.coeffs.A:>10.4f} nm/min
  Parabolic Constant (B):   {self.coeffs.B:>10.2e} nm²/min
  A Parameter:              {self.coeffs.A:>10.2e} nm
  Initial Time Offset (τ):  {self.coeffs.tau:>10.4f} min

OXIDATION RESULTS @ t = {time:.1f} min:
────────────────────────────────────────────────────────────────
  Oxide Thickness:          {thickness:>10.2f} nm
  Growth Rate:              {rate:>10.4f} nm/min
  Growth Regime:            {regime.upper()}
  Silicon Consumed:         {si_consumed:>10.2f} nm
  Estimated Stress:         {stress:>10.1f} MPa (compressive)

TIME PREDICTIONS:
────────────────────────────────────────────────────────────────
  For 100 nm oxide:         {t_100nm:>10.2f} min ({t_100nm/60:.2f} hours)
  For 500 nm oxide:         {t_500nm:>10.2f} min ({t_500nm/60:.2f} hours)
  For 1000 nm oxide:        {t_1000nm:>10.2f} min ({t_1000nm/60:.2f} hours)

REGIME ANALYSIS:
────────────────────────────────────────────────────────────────
  Transition Time:          {self.coeffs.A**2/(4*self.coeffs.B):>10.2f} min
  Linear Rate Constant:     {self.linear_rate_constant():>10.4f} nm/min
  Parabolic Rate Constant:  {self.parabolic_rate_constant():>10.2e} nm²/min

"""
        return report


# ---------------------------------------------------------------------------
# Example / demonstration
# ---------------------------------------------------------------------------

def example_analysis():
    """
    Complete demonstration of oxide growth analysis.
    """
    print("=" * 70)
    print("THERMAL OXIDATION (DEAL-GROVE) ANALYSIS – DEMO")
    print("=" * 70)
    
    # Typical dry oxidation at 1000°C
    params_dry = OxidationParameters(
        temperature=1273,      # 1000°C
        ambient='dry',
        pressure=1.0,
        orientation='<100>',
        initial_oxide=0.0
    )
    
    analyzer = OxideGrowthAnalyzer(params_dry)
    
    # Print report
    print(analyzer.generate_report(time=120.0))
    
    # Generate plots
    print("Generating oxide growth analysis plots...\n")
    
    print("[1/7] Thickness vs. time (linear scale)...")
    analyzer.plot_thickness_vs_time(log_scale=False)
    
    print("[2/7] Thickness vs. time (log-log scale)...")
    analyzer.plot_thickness_vs_time(log_scale=True)
    
    print("[3/7] Growth rate vs. time...")
    analyzer.plot_growth_rate()
    
    print("[4/7] Temperature dependence...")
    analyzer.plot_temperature_dependence()
    
    print("[5/7] Wet vs. dry comparison...")
    analyzer.plot_wet_vs_dry()
    
    print("[6/7] 3D growth evolution...")
    analyzer.plot_3d_growth_animation()
    
    print("[7/7] 3D cross-section...")
    analyzer.plot_3d_cross_section(time=120.0)
    
    print("\nAnalysis complete!")
    print(f"\n{'='*70}")
    print(f"All images saved to: {IMAGE_DIR}")
    print(f"{'='*70}\n")


def compare_orientations():
    """
    Compare oxide growth on different crystal orientations.
    """
    print("=" * 70)
    print("CRYSTAL ORIENTATION COMPARISON")
    print("=" * 70)
    
    orientations = ['<100>', '<110>', '<111>']
    colors = ['blue', 'red', 'green']
    
    time_array = np.logspace(0, 3, 200)  # 1 to 1000 min
    
    plt.figure(figsize=(10, 7))
    
    for orient, color in zip(orientations, colors):
        params = OxidationParameters(
            temperature=1373,  # 1100°C
            ambient='dry',
            orientation=orient
        )
        
        analyzer = OxideGrowthAnalyzer(params)
        thickness_array = [analyzer.oxide_thickness(t) for t in time_array]
        
        plt.plot(time_array, thickness_array, color=color, linewidth=2.5,
                label=f'Si {orient}')
    
    plt.xlabel('Oxidation Time (min)', fontsize=12)
    plt.ylabel('Oxide Thickness (nm)', fontsize=12)
    plt.title('Crystal Orientation Effect on Oxide Growth\n'
             'Dry O₂, T = 1100°C',
             fontsize=14, fontweight='bold')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3, which='both')
    
    save_path = get_image_path('orientation_comparison.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"  → Saved: {save_path}")
    
    plt.show()


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    example_analysis()
    
    print("\n" + "="*70)
    print("CRYSTAL ORIENTATION COMPARISON")
    print("="*70 + "\n")
    
    compare_orientations()