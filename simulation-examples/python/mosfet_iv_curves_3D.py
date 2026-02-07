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
