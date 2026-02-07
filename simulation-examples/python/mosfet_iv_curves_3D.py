"""
3D MOSFET I-V Characteristics Analysis
Silicon Fabrication Handbook

This module provides comprehensive analysis and visualization tools for MOSFET
transistors, including I-V curves, threshold voltage extraction, subthreshold 
behavior, and 3D device structure rendering. Covers both NMOS and PMOS devices
with physical models for:

- Drain current (I_D) vs. V_GS and V_DS in linear, saturation, and subthreshold regions
- Threshold voltage (V_th) extraction using multiple methods
- Channel length modulation (lambda) and DIBL effects
- Output conductance (g_ds) and transconductance (g_m)
- Temperature dependence and short-channel effects
- 3D MOSFET structure visualization with depletion regions

Usage
-----
Run stand-alone for demonstration:
    python mosfet_iv_curves_3D.py

Or import for custom analysis:
    from mosfet_iv_curves_3D import MOSFETGeometry, MOSFETAnalyzer

Author: Silicon Fabrication Handbook Project
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import cm
from matplotlib.colors import Normalize, LinearSegmentedColormap
import scipy.optimize as opt
from dataclasses import dataclass
from typing import Tuple, List, Optional, Dict
import warnings
import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Image output directory setup
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent.resolve()
IMAGE_DIR = SCRIPT_DIR / "images" / "mosfet"
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

def get_image_path(filename: str) -> str:
    """Get full path for saving an image in the organized directory structure."""
    return str(IMAGE_DIR / filename)

# ---------------------------------------------------------------------------
# Physical constants
# ---------------------------------------------------------------------------
Q         = 1.602176634e-19   # Elementary charge (C)
K_B       = 1.380649e-23      # Boltzmann constant (J/K)
EPSILON_0 = 8.854187817e-12   # Permittivity of free space (F/m)
EPSILON_SI = 11.7             # Relative permittivity of silicon
EPSILON_OX = 3.9              # Relative permittivity of SiO2
T_REF     = 300.0             # Reference temperature (K)

# Silicon intrinsic carrier concentration at 300K
N_I_300K  = 1.0e10            # cm^-3


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class MOSFETGeometry:
    """
    Physical geometry of a MOSFET device.
    
    Attributes
    ----------
    channel_length : float   Gate length (L)                   (m)
    channel_width  : float   Gate width (W)                    (m)
    oxide_thickness: float   Gate oxide thickness (t_ox)       (m)
    junction_depth : float   Source/drain junction depth (x_j) (m)
    substrate_doping: float  Substrate doping (N_A for NMOS, N_D for PMOS) (cm^-3)
    """
    channel_length:  float
    channel_width:   float
    oxide_thickness: float
    junction_depth:  float = 200e-9
    substrate_doping: float = 1e16
    
    def __post_init__(self):
        if self.channel_length <= 0 or self.channel_width <= 0:
            raise ValueError("Channel length and width must be positive")
        if self.oxide_thickness <= 0:
            raise ValueError("Oxide thickness must be positive")
        if self.substrate_doping <= 0:
            raise ValueError("Substrate doping must be positive")

@dataclass
class MOSFETParameters:
    """
    Electrical and process parameters for MOSFET model.
    
    Attributes
    ----------
    device_type     : str    'nmos' or 'pmos'
    threshold_voltage: float Threshold voltage V_th             (V)
    mobility        : float  Carrier mobility μ                 (cm²/V·s)
    lambda_param    : float  Channel length modulation λ        (1/V)
    gamma           : float  Body effect coefficient γ          (V^0.5)
    phi_f           : float  Fermi potential φ_F                (V)
    subthreshold_swing: float Subthreshold swing S             (mV/decade)
    temperature     : float  Operating temperature              (K)
    """
    device_type:      str   = 'nmos'
    threshold_voltage: float = 0.5
    mobility:         float = 400.0      # cm²/V·s (NMOS typical)
    lambda_param:     float = 0.05       # 1/V
    gamma:            float = 0.4        # V^0.5
    phi_f:            float = 0.35       # V
    subthreshold_swing: float = 80.0    # mV/decade
    temperature:      float = 300.0      # K
    
    def __post_init__(self):
        if self.device_type not in ['nmos', 'pmos']:
            raise ValueError("device_type must be 'nmos' or 'pmos'")


# ---------------------------------------------------------------------------
# Core MOSFET analyzer
# ---------------------------------------------------------------------------

class MOSFETAnalyzer:
    """
    Comprehensive MOSFET I-V characteristics analyzer with 3D visualization.
    
    Parameters
    ----------
    geometry   : MOSFETGeometry
    parameters : MOSFETParameters
    """
    
    def __init__(self, 
                 geometry: MOSFETGeometry,
                 parameters: Optional[MOSFETParameters] = None):
        self.geom = geometry
        self.params = parameters if parameters else MOSFETParameters()
        
        # Calculate derived parameters
        self.C_ox = (EPSILON_0 * EPSILON_OX) / self.geom.oxide_thickness  # F/m²
        self.V_T = (K_B * self.params.temperature) / Q  # Thermal voltage
        
    # ==================================================================
    # 1. DRAIN CURRENT MODELS
    # ==================================================================
    
    def drain_current(self, V_GS: float, V_DS: float, V_BS: float = 0.0) -> float:
        """
        Calculate drain current using piecewise-continuous model.
        
        Includes linear, saturation, and subthreshold regions.
        
        Parameters
        ----------
        V_GS : float   Gate-source voltage (V)
        V_DS : float   Drain-source voltage (V)
        V_BS : float   Bulk-source voltage (V), default 0
        
        Returns
        -------
        I_D : float    Drain current (A)
        """
        # Body effect on threshold voltage
        V_th = self.threshold_voltage_with_body_effect(V_BS)
        
        # Sign convention for PMOS
        sign = 1.0 if self.params.device_type == 'nmos' else -1.0
        V_GS_eff = sign * V_GS
        V_DS_eff = sign * V_DS
        
        # Overdrive voltage
        V_OD = V_GS_eff - V_th
        
        # Subthreshold region
        if V_OD < -3 * self.V_T:
            return self._subthreshold_current(V_GS_eff, V_DS_eff, V_th)
        
        # Off region
        if V_OD <= 0:
            return 0.0
        
        # Calculate beta (transconductance parameter)
        beta = self.params.mobility * 1e-4 * self.C_ox * (self.geom.channel_width / 
                                                            self.geom.channel_length)
        
        # Linear region
        if V_DS_eff < V_OD:
            I_D = beta * (V_OD * V_DS_eff - 0.5 * V_DS_eff**2)
            I_D *= (1 + self.params.lambda_param * V_DS_eff)  # CLM
        else:
            # Saturation region
            I_D = 0.5 * beta * V_OD**2
            I_D *= (1 + self.params.lambda_param * V_DS_eff)  # CLM
        
        return sign * I_D
    
    def _subthreshold_current(self, V_GS: float, V_DS: float, V_th: float) -> float:
        """Calculate subthreshold current using exponential model."""
        # Subthreshold slope factor (typically 1.3-1.5)
        n = (self.params.subthreshold_swing * 1e-3) / (2.3 * self.V_T)
        
        # Subthreshold current
        I_0 = 1e-12  # Leakage current scale factor (A)
        I_sub = I_0 * np.exp((V_GS - V_th) / (n * self.V_T))
        
        # DIBL effect (simplified)
        I_sub *= (1 + 0.1 * V_DS)
        
        return I_sub
    
    def threshold_voltage_with_body_effect(self, V_BS: float) -> float:
        """
        Calculate threshold voltage including body effect.
        
        V_th = V_th0 + γ(sqrt(|2φ_F - V_BS|) - sqrt(|2φ_F|))
        """
        V_th0 = self.params.threshold_voltage
        gamma = self.params.gamma
        phi_f = self.params.phi_f
        
        body_term = gamma * (np.sqrt(np.abs(2 * phi_f - V_BS)) - 
                            np.sqrt(np.abs(2 * phi_f)))
        
        return V_th0 + body_term
    
    # ==================================================================
    # 2. SMALL-SIGNAL PARAMETERS
    # ==================================================================
    
    def transconductance(self, V_GS: float, V_DS: float, V_BS: float = 0.0) -> float:
        """
        Calculate transconductance g_m = ∂I_D/∂V_GS.
        
        Uses numerical differentiation.
        """
        dV = 1e-6  # Small voltage step
        I_plus = self.drain_current(V_GS + dV, V_DS, V_BS)
        I_minus = self.drain_current(V_GS - dV, V_DS, V_BS)
        return (I_plus - I_minus) / (2 * dV)
    
    def output_conductance(self, V_GS: float, V_DS: float, V_BS: float = 0.0) -> float:
        """
        Calculate output conductance g_ds = ∂I_D/∂V_DS.
        """
        dV = 1e-6
        I_plus = self.drain_current(V_GS, V_DS + dV, V_BS)
        I_minus = self.drain_current(V_GS, V_DS - dV, V_BS)
        return (I_plus - I_minus) / (2 * dV)
    
    def intrinsic_gain(self, V_GS: float, V_DS: float, V_BS: float = 0.0) -> float:
        """
        Calculate intrinsic gain A_v0 = g_m / g_ds.
        """
        g_m = self.transconductance(V_GS, V_DS, V_BS)
        g_ds = self.output_conductance(V_GS, V_DS, V_BS)
        return g_m / g_ds if g_ds > 0 else np.inf
    
    # ==================================================================
    # 3. THRESHOLD VOLTAGE EXTRACTION
    # ==================================================================
    
    def extract_threshold_constant_current(self, I_ref: float = 1e-7) -> float:
        """
        Extract V_th using constant-current method.
        
        V_th is defined as V_GS where I_D = I_ref * (W/L).
        """
        W_L = self.geom.channel_width / self.geom.channel_length
        I_target = I_ref * W_L
        
        # Binary search for V_GS
        V_low, V_high = 0.0, 2.0
        for _ in range(50):
            V_mid = (V_low + V_high) / 2
            I_D = abs(self.drain_current(V_mid, 0.1, 0.0))
            
            if I_D < I_target:
                V_low = V_mid
            else:
                V_high = V_mid
        
        return (V_low + V_high) / 2
    
    def extract_threshold_linear_extrapolation(self, V_DS: float = 0.1) -> Tuple[float, float]:
        """
        Extract V_th using linear extrapolation method.
        
        Returns V_th and maximum g_m point.
        """
        V_GS_array = np.linspace(0, 1.5, 100)
        g_m_array = np.array([self.transconductance(V, V_DS) for V in V_GS_array])
        
        # Find maximum g_m
        idx_max = np.argmax(g_m_array)
        V_GS_max = V_GS_array[idx_max]
        g_m_max = g_m_array[idx_max]
        
        # Linear extrapolation to I_D = 0
        I_D_max = self.drain_current(V_GS_max, V_DS)
        V_th_extrap = V_GS_max - I_D_max / g_m_max
        
        return V_th_extrap, V_GS_max
    
    # ==================================================================
    # 4. PLOTTING FUNCTIONS
    # ==================================================================
    
    def plot_transfer_characteristics(self, 
                                      V_DS_values: List[float] = None,
                                      V_GS_range: Tuple[float, float] = None,
                                      log_scale: bool = False,
                                      save_path: Optional[str] = None,
                                      auto_save: bool = True):
        """
        Plot I_D vs V_GS (transfer characteristics).
        
        Parameters
        ----------
        V_DS_values : list    List of V_DS values to plot
        V_GS_range  : tuple   (V_GS_min, V_GS_max)
        log_scale   : bool    Use logarithmic y-axis
        save_path   : str     Custom save path (overrides auto_save)
        auto_save   : bool    Auto-save to images/mosfet/
        """
        if V_DS_values is None:
            V_DS_values = [0.1, 0.5, 1.0, 1.5]
        
        if V_GS_range is None:
            V_GS_range = (0.0, 2.0)
        
        V_GS_array = np.linspace(V_GS_range[0], V_GS_range[1], 300)
        
        plt.figure(figsize=(10, 7))
        
        for V_DS in V_DS_values:
            I_D_array = np.array([abs(self.drain_current(V_GS, V_DS)) 
                                 for V_GS in V_GS_array])
            
            # Convert to mA
            I_D_mA = I_D_array * 1e3
            
            plt.plot(V_GS_array, I_D_mA, linewidth=2, 
                    label=f'V_DS = {V_DS:.1f} V')
        
        # Mark threshold voltage
        V_th = self.params.threshold_voltage
        plt.axvline(V_th, color='gray', linestyle='--', linewidth=1,
                   label=f'V_th = {V_th:.2f} V')
        
        plt.xlabel('Gate-Source Voltage V_GS (V)', fontsize=12)
        plt.ylabel('Drain Current |I_D| (mA)', fontsize=12)
        plt.title(f'{self.params.device_type.upper()} Transfer Characteristics\n'
                 f'L = {self.geom.channel_length*1e9:.0f} nm, '
                 f'W = {self.geom.channel_width*1e6:.1f} μm',
                 fontsize=14, fontweight='bold')
        plt.legend(fontsize=10)
        plt.grid(True, alpha=0.3)
        
        if log_scale:
            plt.yscale('log')
            plt.ylim([1e-9, None])
        
        # Determine save path
        if save_path:
            final_path = save_path
        elif auto_save:
            suffix = '_log' if log_scale else ''
            final_path = get_image_path(f'transfer_characteristics{suffix}.png')
        else:
            final_path = None
        
        if final_path:
            plt.savefig(final_path, dpi=300, bbox_inches='tight')
            print(f"  → Saved: {final_path}")
        
        plt.show()
    
    def plot_output_characteristics(self,
                                    V_GS_values: List[float] = None,
                                    V_DS_range: Tuple[float, float] = None,
                                    save_path: Optional[str] = None,
                                    auto_save: bool = True):
        """
        Plot I_D vs V_DS (output characteristics).
        
        Parameters
        ----------
        V_GS_values : list   List of V_GS values to plot
        V_DS_range  : tuple  (V_DS_min, V_DS_max)
        save_path   : str    Custom save path
        auto_save   : bool   Auto-save to images/mosfet/
        """
        if V_GS_values is None:
            # Default: steps from V_th to V_th + 1V
            V_th = self.params.threshold_voltage
            V_GS_values = [V_th + i*0.2 for i in range(6)]
        
        if V_DS_range is None:
            V_DS_range = (0.0, 2.0)
        
        V_DS_array = np.linspace(V_DS_range[0], V_DS_range[1], 300)
        
        plt.figure(figsize=(10, 7))
        
        for V_GS in V_GS_values:
            I_D_array = np.array([abs(self.drain_current(V_GS, V_DS)) 
                                 for V_DS in V_DS_array])
            I_D_mA = I_D_array * 1e3
            
            plt.plot(V_DS_array, I_D_mA, linewidth=2,
                    label=f'V_GS = {V_GS:.2f} V')
        
        plt.xlabel('Drain-Source Voltage V_DS (V)', fontsize=12)
        plt.ylabel('Drain Current |I_D| (mA)', fontsize=12)
        plt.title(f'{self.params.device_type.upper()} Output Characteristics\n'
                 f'L = {self.geom.channel_length*1e9:.0f} nm, '
                 f'W = {self.geom.channel_width*1e6:.1f} μm',
                 fontsize=14, fontweight='bold')
        plt.legend(fontsize=10, loc='upper left')
        plt.grid(True, alpha=0.3)
        
        # Determine save path
        if save_path:
            final_path = save_path
        elif auto_save:
            final_path = get_image_path('output_characteristics.png')
        else:
            final_path = None
        
        if final_path:
            plt.savefig(final_path, dpi=300, bbox_inches='tight')
            print(f"  → Saved: {final_path}")
        
        plt.show()
    
    def plot_3d_iv_surface(self,
                          V_GS_range: Tuple[float, float] = None,
                          V_DS_range: Tuple[float, float] = None,
                          save_path: Optional[str] = None,
                          auto_save: bool = True):
        """
        Plot 3D surface of I_D(V_GS, V_DS).
        
        Parameters
        ----------
        V_GS_range : tuple  (V_GS_min, V_GS_max)
        V_DS_range : tuple  (V_DS_min, V_DS_max)
        save_path  : str    Custom save path
        auto_save  : bool   Auto-save to images/mosfet/
        """
        if V_GS_range is None:
            V_GS_range = (0.0, 2.0)
        if V_DS_range is None:
            V_DS_range = (0.0, 2.0)
        
        # Create mesh
        V_GS_array = np.linspace(V_GS_range[0], V_GS_range[1], 80)
        V_DS_array = np.linspace(V_DS_range[0], V_DS_range[1], 80)
        V_GS_mesh, V_DS_mesh = np.meshgrid(V_GS_array, V_DS_array)
        
        # Calculate I_D for each point
        I_D_mesh = np.zeros_like(V_GS_mesh)
        for i in range(V_GS_mesh.shape[0]):
            for j in range(V_GS_mesh.shape[1]):
                I_D_mesh[i, j] = abs(self.drain_current(V_GS_mesh[i, j], 
                                                        V_DS_mesh[i, j]))
        
        # Convert to mA
        I_D_mesh_mA = I_D_mesh * 1e3
        
        # Create 3D plot
        fig = plt.figure(figsize=(12, 9))
        ax = fig.add_subplot(111, projection='3d')
        
        surf = ax.plot_surface(V_GS_mesh, V_DS_mesh, I_D_mesh_mA,
                              cmap='viridis', alpha=0.9,
                              edgecolor='none', antialiased=True)
        
        ax.set_xlabel('V_GS (V)', fontsize=11)
        ax.set_ylabel('V_DS (V)', fontsize=11)
        ax.set_zlabel('|I_D| (mA)', fontsize=11)
        ax.set_title(f'{self.params.device_type.upper()} 3D I-V Surface\n'
                    f'L = {self.geom.channel_length*1e9:.0f} nm, '
                    f'W = {self.geom.channel_width*1e6:.1f} μm',
                    fontsize=14, fontweight='bold')
        
        # Add colorbar
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='|I_D| (mA)')
        
        # Determine save path
        if save_path:
            final_path = save_path
        elif auto_save:
            final_path = get_image_path('3d_iv_surface.png')
        else:
            final_path = None
        
        if final_path:
            plt.savefig(final_path, dpi=300, bbox_inches='tight')
            print(f"  → Saved: {final_path}")
        
        plt.show()
    
    def plot_small_signal_parameters(self,
                                     V_DS: float = 1.0,
                                     save_path: Optional[str] = None,
                                     auto_save: bool = True):
        """
        Plot g_m, g_ds, and A_v0 vs V_GS.
        
        Parameters
        ----------
        V_DS      : float  Fixed V_DS value
        save_path : str    Custom save path
        auto_save : bool   Auto-save to images/mosfet/
        """
        V_GS_array = np.linspace(0, 2.0, 200)
        
        g_m_array = []
        g_ds_array = []
        A_v0_array = []
        
        for V_GS in V_GS_array:
            g_m = self.transconductance(V_GS, V_DS)
            g_ds = self.output_conductance(V_GS, V_DS)
            A_v0 = g_m / g_ds if g_ds > 1e-12 else 0
            
            g_m_array.append(g_m * 1e3)   # mS
            g_ds_array.append(g_ds * 1e6)  # μS
            A_v0_array.append(A_v0)
        
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
        
        # Transconductance
        ax1.plot(V_GS_array, g_m_array, 'b-', linewidth=2)
        ax1.set_ylabel('g_m (mS)', fontsize=11)
        ax1.set_title(f'Small-Signal Parameters vs V_GS (V_DS = {V_DS} V)',
                     fontsize=13, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.axvline(self.params.threshold_voltage, color='gray', 
                   linestyle='--', linewidth=1)
        
        # Output conductance
        ax2.plot(V_GS_array, g_ds_array, 'r-', linewidth=2)
        ax2.set_ylabel('g_ds (μS)', fontsize=11)
        ax2.grid(True, alpha=0.3)
        ax2.axvline(self.params.threshold_voltage, color='gray',
                   linestyle='--', linewidth=1)
        
        # Intrinsic gain
        ax3.plot(V_GS_array, A_v0_array, 'g-', linewidth=2)
        ax3.set_xlabel('Gate-Source Voltage V_GS (V)', fontsize=11)
        ax3.set_ylabel('A_v0 (V/V)', fontsize=11)
        ax3.grid(True, alpha=0.3)
        ax3.axvline(self.params.threshold_voltage, color='gray',
                   linestyle='--', linewidth=1, label=f'V_th = {self.params.threshold_voltage:.2f} V')
        ax3.legend(fontsize=9)
        
        plt.tight_layout()
        
        # Determine save path
        if save_path:
            final_path = save_path
        elif auto_save:
            final_path = get_image_path('small_signal_parameters.png')
        else:
            final_path = None
        
        if final_path:
            plt.savefig(final_path, dpi=300, bbox_inches='tight')
            print(f"  → Saved: {final_path}")
        
        plt.show()
    
    # ==================================================================
    # 5. 3D DEVICE STRUCTURE VISUALIZATION
    # ==================================================================
    
    def visualize_3d_structure(self,
                              V_GS: float = 0.0,
                              V_DS: float = 0.0,
                              show_depletion: bool = True,
                              save_path: Optional[str] = None,
                              auto_save: bool = True):
        """
        Render 3D MOSFET structure with cross-section view.
        
        Shows gate, source, drain, oxide, channel, and depletion regions.
        
        Parameters
        ----------
        V_GS            : float  Gate-source voltage (for depletion visualization)
        V_DS            : float  Drain-source voltage
        show_depletion  : bool   Show depletion region extent
        save_path       : str    Custom save path
        auto_save       : bool   Auto-save to images/mosfet/
        """
        fig = plt.figure(figsize=(14, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Dimensions in nm for visualization
        L = self.geom.channel_length * 1e9
        W = self.geom.channel_width * 1e9
        t_ox = self.geom.oxide_thickness * 1e9
        x_j = self.geom.junction_depth * 1e9
        
        # Scale W for better visualization if too large
        W_vis = min(W, L * 3)
        
        # Substrate
        self._draw_box(ax, -L*0.3, L*1.3, 0, W_vis, -x_j*3, 0,
                      color='lightgray', alpha=0.3, label='Substrate')
        
        # Gate oxide
        self._draw_box(ax, 0, L, 0, W_vis, 0, t_ox,
                      color='lightblue', alpha=0.7, label='Gate Oxide (SiO₂)')
        
        # Gate (poly-silicon or metal)
        gate_height = t_ox * 3
        self._draw_box(ax, 0, L, 0, W_vis, t_ox, gate_height,
                      color='gold', alpha=0.8, label='Gate')
        
        # Source region
        self._draw_box(ax, -L*0.25, 0, 0, W_vis, -x_j, 0,
                      color='red', alpha=0.6, label='Source (N+)' if self.params.device_type == 'nmos' else 'Source (P+)')
        
        # Drain region
        self._draw_box(ax, L, L*1.25, 0, W_vis, -x_j, 0,
                      color='blue', alpha=0.6, label='Drain (N+)' if self.params.device_type == 'nmos' else 'Drain (P+)')
        
        # Channel region (under gate)
        if show_depletion and V_GS > self.params.threshold_voltage:
            # Inversion layer (exaggerated for visibility)
            inv_thickness = t_ox * 0.3
            self._draw_box(ax, 0, L, 0, W_vis, -inv_thickness, 0,
                          color='yellow', alpha=0.5, label='Inversion Layer')
        
        # Depletion region (if bias applied)
        if show_depletion and V_GS > 0:
            depl_depth = x_j * 1.5
            self._draw_box(ax, 0, L, 0, W_vis, -depl_depth, -inv_thickness if V_GS > self.params.threshold_voltage else 0,
                          color='cyan', alpha=0.2, label='Depletion Region')
        
        # Axes and labels
        ax.set_xlabel('Length (nm)', fontsize=11)
        ax.set_ylabel('Width (nm)', fontsize=11)
        ax.set_zlabel('Height (nm)', fontsize=11)
        ax.set_title(f'3D {self.params.device_type.upper()} Structure\n'
                    f'L = {L:.0f} nm, W = {W:.0f} nm, t_ox = {t_ox:.1f} nm\n'
                    f'V_GS = {V_GS:.2f} V, V_DS = {V_DS:.2f} V',
                    fontsize=13, fontweight='bold')
        
        ax.legend(fontsize=9, loc='upper right')
        
        # Set view angle
        ax.view_init(elev=20, azim=45)
        
        # Set limits
        ax.set_xlim([-L*0.4, L*1.4])
        ax.set_ylim([0, W_vis*1.1])
        ax.set_zlim([-x_j*3.5, gate_height*1.2])
        
        # Determine save path
        if save_path:
            final_path = save_path
        elif auto_save:
            final_path = get_image_path('3d_device_structure.png')
        else:
            final_path = None
        
        if final_path:
            plt.savefig(final_path, dpi=300, bbox_inches='tight')
            print(f"  → Saved: {final_path}")
        
        plt.show()
    
    @staticmethod
    def _draw_box(ax, x0, x1, y0, y1, z0, z1, color='gray', alpha=0.7, label=''):
        """Draw a 3D box (cuboid) given corner coordinates."""
        # Define 8 vertices
        vertices = np.array([
            [x0, y0, z0], [x1, y0, z0], [x1, y1, z0], [x0, y1, z0],  # bottom
            [x0, y0, z1], [x1, y0, z1], [x1, y1, z1], [x0, y1, z1]   # top
        ])
        
        # Define 6 faces
        faces = [
            [vertices[0], vertices[1], vertices[5], vertices[4]],  # front
            [vertices[2], vertices[3], vertices[7], vertices[6]],  # back
            [vertices[0], vertices[3], vertices[7], vertices[4]],  # left
            [vertices[1], vertices[2], vertices[6], vertices[5]],  # right
            [vertices[0], vertices[1], vertices[2], vertices[3]],  # bottom
            [vertices[4], vertices[5], vertices[6], vertices[7]]   # top
        ]
        
        poly = Poly3DCollection(faces, alpha=alpha, facecolor=color,
                               edgecolor='black', linewidth=0.5)
        if label:
            poly.set_label(label)
        ax.add_collection3d(poly)
    
    # ==================================================================
    # 6. ANALYSIS REPORT
    # ==================================================================
    
    def generate_report(self, V_GS: float = 1.0, V_DS: float = 1.0) -> str:
        """
        Generate comprehensive MOSFET analysis report.
        
        Parameters
        ----------
        V_GS : float   Operating gate-source voltage
        V_DS : float   Operating drain-source voltage
        
        Returns
        -------
        str : Formatted report
        """
        I_D = self.drain_current(V_GS, V_DS)
        g_m = self.transconductance(V_GS, V_DS)
        g_ds = self.output_conductance(V_GS, V_DS)
        A_v0 = self.intrinsic_gain(V_GS, V_DS)
        
        V_th_cc = self.extract_threshold_constant_current()
        V_th_le, V_GS_max_gm = self.extract_threshold_linear_extrapolation()
        
        report = f"""
╔══════════════════════════════════════════════════════════════╗
║              MOSFET I-V ANALYSIS REPORT                      ║
╚══════════════════════════════════════════════════════════════╝

DEVICE TYPE: {self.params.device_type.upper()}
────────────────────────────────────────────────────────────────

GEOMETRY PARAMETERS:
────────────────────────────────────────────────────────────────
  Channel Length (L):       {self.geom.channel_length*1e9:>10.1f} nm
  Channel Width (W):        {self.geom.channel_width*1e6:>10.2f} μm
  W/L Ratio:                {self.geom.channel_width/self.geom.channel_length:>10.1f}
  Oxide Thickness (t_ox):   {self.geom.oxide_thickness*1e9:>10.2f} nm
  Junction Depth (x_j):     {self.geom.junction_depth*1e9:>10.1f} nm
  Substrate Doping:         {self.geom.substrate_doping:>10.2e} cm⁻³

ELECTRICAL PARAMETERS:
────────────────────────────────────────────────────────────────
  Threshold Voltage (V_th): {self.params.threshold_voltage:>10.3f} V
  Mobility (μ):             {self.params.mobility:>10.1f} cm²/V·s
  Lambda (λ):               {self.params.lambda_param:>10.4f} V⁻¹
  Body Effect (γ):          {self.params.gamma:>10.3f} V^0.5
  Subthreshold Swing (S):   {self.params.subthreshold_swing:>10.1f} mV/dec
  Temperature:              {self.params.temperature:>10.1f} K

DERIVED PARAMETERS:
────────────────────────────────────────────────────────────────
  Gate Oxide Capacitance:   {self.C_ox*1e4:>10.4f} fF/μm²
  Thermal Voltage (V_T):    {self.V_T*1e3:>10.2f} mV

DC OPERATING POINT @ V_GS = {V_GS:.2f} V, V_DS = {V_DS:.2f} V:
────────────────────────────────────────────────────────────────
  Drain Current (I_D):      {abs(I_D)*1e3:>10.4f} mA
  Transconductance (g_m):   {g_m*1e3:>10.4f} mS
  Output Conductance (g_ds):{g_ds*1e6:>10.4f} μS
  Intrinsic Gain (A_v0):    {A_v0:>10.1f} V/V

THRESHOLD VOLTAGE EXTRACTION:
────────────────────────────────────────────────────────────────
  Constant Current Method:  {V_th_cc:>10.3f} V
  Linear Extrapolation:     {V_th_le:>10.3f} V
  Max g_m Point:            {V_GS_max_gm:>10.3f} V

"""
        return report


# ---------------------------------------------------------------------------
# Example / demonstration
# ---------------------------------------------------------------------------

def example_analysis():
    """
    Complete demonstration of MOSFET analysis capabilities.
    """
    print("=" * 70)
    print("MOSFET I-V CHARACTERISTICS ANALYSIS – DEMO")
    print("=" * 70)
    
    # Define a 45nm NMOS device
    geometry = MOSFETGeometry(
        channel_length=45e-9,      # 45 nm
        channel_width=1e-6,        # 1 μm
        oxide_thickness=1.2e-9,    # 1.2 nm (high-k equivalent)
        junction_depth=50e-9,      # 50 nm
        substrate_doping=1e17      # 10^17 cm^-3
    )
    
    parameters = MOSFETParameters(
        device_type='nmos',
        threshold_voltage=0.4,
        mobility=350.0,            # cm²/V·s
        lambda_param=0.08,         # 1/V
        gamma=0.35,
        subthreshold_swing=75.0,   # mV/decade
        temperature=300.0
    )
    
    analyzer = MOSFETAnalyzer(geometry, parameters)
    
    # Print report
    print(analyzer.generate_report(V_GS=1.0, V_DS=1.0))
    
    # Generate plots
    print("Generating I-V characteristic plots...\n")
    
    print("[1/6] Transfer characteristics (linear scale)...")
    analyzer.plot_transfer_characteristics(log_scale=False)
    
    print("[2/6] Transfer characteristics (log scale)...")
    analyzer.plot_transfer_characteristics(log_scale=True)
    
    print("[3/6] Output characteristics...")
    analyzer.plot_output_characteristics()
    
    print("[4/6] 3D I-V surface...")
    analyzer.plot_3d_iv_surface()
    
    print("[5/6] Small-signal parameters...")
    analyzer.plot_small_signal_parameters()
    
    print("[6/6] 3D device structure...")
    analyzer.visualize_3d_structure(V_GS=1.2, V_DS=0.8, show_depletion=True)
    
    print("\nAnalysis complete!")
    print(f"\n{'='*70}")
    print(f"All images saved to: {IMAGE_DIR}")
    print(f"{'='*70}\n")


def compare_channel_lengths():
    """
    Compare I-V characteristics for different channel lengths (short-channel effects).
    """
    print("=" * 70)
    print("CHANNEL LENGTH COMPARISON")
    print("=" * 70)
    
    lengths = [22e-9, 45e-9, 90e-9, 180e-9]  # nm nodes
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    for L in lengths:
        geom = MOSFETGeometry(
            channel_length=L,
            channel_width=1e-6,
            oxide_thickness=L/40,  # Scaled oxide
            junction_depth=L*1.2,
            substrate_doping=1e17
        )
        
        params = MOSFETParameters(
            threshold_voltage=0.4,
            mobility=300.0,
            lambda_param=0.05 + 0.5/L*1e-9,  # Shorter → more CLM
        )
        
        analyzer = MOSFETAnalyzer(geom, params)
        
        # Transfer curve
        V_GS_array = np.linspace(0, 1.5, 200)
        I_D_array = [abs(analyzer.drain_current(V, 1.0)) for V in V_GS_array]
        ax1.plot(V_GS_array, np.array(I_D_array)*1e3, linewidth=2,
                label=f'L = {L*1e9:.0f} nm')
        
        # Output curve (at V_GS = 1.0V)
        V_DS_array = np.linspace(0, 1.5, 200)
        I_D_array = [abs(analyzer.drain_current(1.0, V)) for V in V_DS_array]
        ax2.plot(V_DS_array, np.array(I_D_array)*1e3, linewidth=2,
                label=f'L = {L*1e9:.0f} nm')
    
    ax1.set_xlabel('V_GS (V)', fontsize=11)
    ax1.set_ylabel('|I_D| (mA)', fontsize=11)
    ax1.set_title('Transfer Curves (V_DS = 1.0 V)', fontsize=12, fontweight='bold')
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3)
    
    ax2.set_xlabel('V_DS (V)', fontsize=11)
    ax2.set_ylabel('|I_D| (mA)', fontsize=11)
    ax2.set_title('Output Curves (V_GS = 1.0 V)', fontsize=12, fontweight='bold')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    save_path = get_image_path('channel_length_comparison.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"  → Saved: {save_path}")
    
    plt.show()


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    example_analysis()
    
    print("\n" + "="*70)
    print("CHANNEL LENGTH COMPARISON")
    print("="*70 + "\n")
    
    compare_channel_lengths()