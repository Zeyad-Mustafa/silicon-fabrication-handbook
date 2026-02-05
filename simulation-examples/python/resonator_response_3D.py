"""
3D MEMS Resonator Response Analysis
Silicon Fabrication Handbook

This module provides comprehensive analysis tools for MEMS mechanical resonators.
It builds on the material and suspension models from comb_drive_analysis_3D and extends
them into the frequency domain with:
- Transfer-function (H(ω)) computation for 1-DOF and 2-DOF resonators
- Squeeze-film and slide-film damping models
- Nonlinear (Duffing) backbone-curve analysis
- Mode-shape visualization for beam and plate resonators
- 3D structural rendering with displacement-field colour mapping
- Bode & Nyquist plots, Q-factor extraction, and parametric sweeps
- Fabrication-tolerance sensitivity analysis

Usage
-----
Run stand-alone for a full demo:
    python resonator_response_3D.py

Or import the classes directly:
    from resonator_response_3D import ResonatorGeometry, ResonatorAnalyzer

Author: Silicon Fabrication Handbook Project
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import cm
from matplotlib.colors import Normalize
import scipy.signal as sig
import scipy.optimize as opt
from dataclasses import dataclass, field
from typing import Tuple, List, Optional
import warnings
import os
from pathlib import Path

import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Image output directory setup
# ---------------------------------------------------------------------------
# Automatically create images directory structure for saving plots
SCRIPT_DIR = Path(__file__).parent.resolve()
IMAGE_DIR = SCRIPT_DIR / "images" / "resonator"
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

def get_image_path(filename: str) -> str:
    """
    Get full path for saving an image in the organized directory structure.
    
    Args:
        filename: Name of the image file (e.g., 'bode_plot.png')
        
    Returns:
        Full path as string
    """
    return str(IMAGE_DIR / filename)

# ---------------------------------------------------------------------------
# Physical constants  (shared with comb_drive_analysis_3D)
# ---------------------------------------------------------------------------
EPSILON_0       = 8.854e-12   # Permittivity of free space          (F/m)
EPSILON_R_AIR   = 1.0         # Relative permittivity of air
MU_AIR          = 1.81e-5     # Dynamic viscosity of air @ 20 °C   (Pa·s)
P_ATM           = 101325.0    # Atmospheric pressure               (Pa)


# ---------------------------------------------------------------------------
# Dataclasses  ──  geometry  ·  material  ·  damping
# ---------------------------------------------------------------------------

@dataclass
class ResonatorGeometry:
    """
    Geometry of a single-mode beam resonator with optional anchor beams.

    Attributes
    ----------
    beam_length      : float   Resonator beam length                (m)
    beam_width       : float   Beam width (in-plane)                (m)
    beam_thickness   : float   Beam thickness (out-of-plane / etch depth) (m)
    n_beams          : int     Number of parallel suspension beams
    anchor_gap       : float   Gap between beam and substrate       (m)
    mass_length      : float   Length of the attached proof-mass    (m)
    mass_width       : float   Width  of the attached proof-mass    (m)
    mass_thickness   : float   Thickness of the proof-mass          (m)
                                 (set to 0 for a simple cantilever)
    """
    beam_length:     float
    beam_width:      float
    beam_thickness:  float
    n_beams:         int   = 2
    anchor_gap:      float = 2e-6
    mass_length:     float = 0.0
    mass_width:      float = 0.0
    mass_thickness:  float = 0.0

    def __post_init__(self):
        pos_fields = ['beam_length', 'beam_width', 'beam_thickness', 'anchor_gap']
        if any(getattr(self, f) <= 0 for f in pos_fields):
            raise ValueError("beam_length, beam_width, beam_thickness, and anchor_gap must be > 0")
        if self.n_beams < 1:
            raise ValueError("n_beams must be >= 1")

    # ------------------------------------------------------------------
    @property
    def has_proof_mass(self) -> bool:
        return self.mass_length > 0 and self.mass_width > 0 and self.mass_thickness > 0


@dataclass
class ResonatorMaterial:
    """
    Material properties — defaults match <100> silicon.

    Attributes
    ----------
    youngs_modulus   : float   Young's modulus                      (Pa)
    density          : float   Density                              (kg/m³)
    poissons_ratio   : float   Poisson's ratio
    residual_stress  : float   In-film residual stress              (Pa)
    """
    youngs_modulus:  float = 169e9
    density:         float = 2329.0
    poissons_ratio:  float = 0.22
    residual_stress: float = 0.0


@dataclass
class DampingModel:
    """
    Selectable damping model with all required parameters.

    Attributes
    ----------
    model_type       : str    'squeeze' | 'slide' | 'constant_Q' | 'constant_zeta'
    quality_factor   : float  Q  (used when model_type == 'constant_Q')
    damping_ratio    : float  ζ  (used when model_type == 'constant_zeta')
    gap              : float  Squeeze-film or slide-film gap       (m)
    pressure         : float  Ambient pressure                     (Pa)
    """
    model_type:      str   = 'constant_Q'
    quality_factor:  float = 100.0
    damping_ratio:   float = 0.005
    gap:             float = 2e-6
    pressure:        float = P_ATM


# ---------------------------------------------------------------------------
# Core analyzer
# ---------------------------------------------------------------------------

class ResonatorAnalyzer:
    """
    Full-stack resonator analysis: statics → dynamics → 3-D visualisation.

    Parameters
    ----------
    geometry : ResonatorGeometry
    material : ResonatorMaterial   (optional – defaults to silicon)
    damping  : DampingModel        (optional – defaults to constant_Q = 100)
    """

    def __init__(self,
                 geometry: ResonatorGeometry,
                 material: Optional[ResonatorMaterial] = None,
                 damping:  Optional[DampingModel]      = None):
        self.geom     = geometry
        self.material = material or ResonatorMaterial()
        self.damping  = damping  or DampingModel()

    # ==================================================================
    # 1.  LUMPED-PARAMETER EXTRACTION
    # ==================================================================

    def effective_mass(self) -> float:
        """
        Lumped effective mass  (kg).

        For a fixed–guided beam the effective mass contribution is 17/35 of
        the beam mass.  A proof-mass, when present, contributes fully.
        """
        t  = self.geom.beam_thickness
        L  = self.geom.beam_length
        w  = self.geom.beam_width
        rho = self.material.density

        m_beam_eff = self.geom.n_beams * (17.0 / 35.0) * rho * w * t * L

        if self.geom.has_proof_mass:
            m_proof = (rho * self.geom.mass_length *
                       self.geom.mass_width * self.geom.mass_thickness)
        else:
            m_proof = 0.0

        return m_beam_eff + m_proof

    def spring_constant(self) -> float:
        """
        Effective spring constant (N/m) — fixed–guided beams in parallel.

        k_single = 12 E I / L³,   I = w t³ / 12   (out-of-plane bending)
        """
        E = self.material.youngs_modulus
        w = self.geom.beam_width
        t = self.geom.beam_thickness
        L = self.geom.beam_length

        I       = w * t**3 / 12.0
        k_single = 12.0 * E * I / L**3
        return self.geom.n_beams * k_single

    def resonant_frequency(self) -> float:
        """Natural frequency  f₀  (Hz)."""
        k = self.spring_constant()
        m = self.effective_mass()
        return (1.0 / (2.0 * np.pi)) * np.sqrt(k / m)

    def angular_frequency(self) -> float:
        """Natural angular frequency  ω₀  (rad/s)."""
        return 2.0 * np.pi * self.resonant_frequency()

    # ==================================================================
    # 2.  DAMPING  –  squeeze / slide / constant models
    # ==================================================================

    def _squeeze_film_damping(self) -> float:
        """
        Squeeze-film damping coefficient  b  (N·s/m).

        Uses the long-channel (parallel-plate) formula:
            b = 12 μ A² / (gap³)   (per beam face)
        """
        mu  = MU_AIR
        gap = self.damping.gap
        A   = self.geom.beam_length * self.geom.beam_thickness   # face area
        b_single = 12.0 * mu * A**2 / gap**3
        return self.geom.n_beams * b_single * 2  # two faces

    def _slide_film_damping(self) -> float:
        """
        Slide-film (Couette) damping coefficient  b  (N·s/m).

            b = μ A / gap
        """
        mu  = MU_AIR
        gap = self.damping.gap
        A   = self.geom.beam_length * self.geom.beam_width
        return self.geom.n_beams * mu * A / gap * 2  # top + bottom

    def damping_coefficient(self) -> float:
        """Return b (N·s/m) according to the selected model."""
        m  = self.effective_mass()
        w0 = self.angular_frequency()

        if self.damping.model_type == 'squeeze':
            return self._squeeze_film_damping()
        elif self.damping.model_type == 'slide':
            return self._slide_film_damping()
        elif self.damping.model_type == 'constant_Q':
            return m * w0 / self.damping.quality_factor
        elif self.damping.model_type == 'constant_zeta':
            return 2.0 * self.damping.damping_ratio * m * w0
        else:
            raise ValueError(f"Unknown damping model: {self.damping.model_type}")

    def quality_factor(self) -> float:
        """Effective Q = m ω₀ / b."""
        return self.effective_mass() * self.angular_frequency() / self.damping_coefficient()

    # ==================================================================
    # 3.  TRANSFER FUNCTION  –  H(ω)
    # ==================================================================

    def transfer_function(self, freqs: np.ndarray) -> np.ndarray:
        """
        Compute the 1-DOF displacement transfer function  H(f).

            H(f) = 1 / ( k − m ω² + j b ω )

        Parameters
        ----------
        freqs : array   Frequency vector  (Hz)

        Returns
        -------
        H : complex array   same length as freqs
        """
        k  = self.spring_constant()
        m  = self.effective_mass()
        b  = self.damping_coefficient()
        w  = 2.0 * np.pi * freqs

        H = 1.0 / (k - m * w**2 + 1j * b * w)
        return H

    # ==================================================================
    # 4.  DUFFING  (nonlinear) BACKBONE CURVE
    # ==================================================================

    @staticmethod
    def duffing_backbone(amplitude: np.ndarray,
                         omega_0: float,
                         alpha: float) -> np.ndarray:
        """
        Backbone (peak-locus) frequency of a Duffing oscillator.

            ω_peak = ω₀ √(1 + (3α / 4ω₀²) A²)

        Parameters
        ----------
        amplitude : array   Oscillation amplitude A  (m)
        omega_0   : float   Linear natural frequency  (rad/s)
        alpha     : float   Cubic stiffness coefficient  (N/m³)
                            >0 → hardening,  <0 → softening

        Returns
        -------
        omega_peak : array  (rad/s)
        """
        return omega_0 * np.sqrt(1.0 + (3.0 * alpha / (4.0 * omega_0**2)) * amplitude**2)

    def estimate_cubic_stiffness(self) -> float:
        """
        Geometric nonlinearity estimate  α  (N/m³).

        For an axially constrained beam (mid-plane stretching):
            α ≈ (π⁴ E w t) / (8 L³)
        This is a first-order estimate; FEA should be used for final values.
        """
        E = self.material.youngs_modulus
        w = self.geom.beam_width
        t = self.geom.beam_thickness
        L = self.geom.beam_length
        return (np.pi**4 * E * w * t) / (8.0 * L**3)

    # ==================================================================
    # 5.  SENSITIVITY  (fabrication tolerance sweep)
    # ==================================================================

    def sensitivity_sweep(self,
                          param_name: str,
                          nominal: float,
                          tolerance_pct: float = 10.0,
                          n_points: int = 51) -> Tuple[np.ndarray, np.ndarray]:
        """
        Sweep a single geometry parameter ± tolerance and return f₀.

        Parameters
        ----------
        param_name     : str    Field name inside self.geom
        nominal        : float  Nominal value  (m)
        tolerance_pct  : float  ± percentage
        n_points       : int    Number of sweep points

        Returns
        -------
        values : array   Swept parameter values  (m)
        freqs  : array   Corresponding f₀       (Hz)
        """
        values = np.linspace(nominal * (1 - tolerance_pct / 100),
                             nominal * (1 + tolerance_pct / 100),
                             n_points)
        freqs  = np.empty_like(values)

        original = getattr(self.geom, param_name)
        for i, v in enumerate(values):
            setattr(self.geom, param_name, v)
            freqs[i] = self.resonant_frequency()
        setattr(self.geom, param_name, original)   # restore

        return values, freqs

    # ==================================================================
    # 6.  PLOTS
    # ==================================================================

    # --- 6a.  Bode magnitude + phase --------------------------------
    def plot_bode(self,
                  freq_range: Optional[Tuple[float, float]] = None,
                  n_points: int = 2000,
                  save_path: Optional[str] = None,
                  auto_save: bool = True):
        """
        Bode plot (magnitude & phase) around the first resonance.

        Args:
            freq_range : (f_low, f_high) in Hz.  Defaults to 0.5 f₀ … 1.5 f₀.
            n_points   : number of frequency samples
            save_path  : optional path to save figure (overrides auto_save)
            auto_save  : if True and save_path is None, auto-saves to images/resonator/
        """
        f0 = self.resonant_frequency()
        if freq_range is None:
            freq_range = (0.5 * f0, 1.5 * f0)

        freqs = np.linspace(freq_range[0], freq_range[1], n_points)
        H     = self.transfer_function(freqs)

        mag   = 20.0 * np.log10(np.abs(H) / np.abs(H).max())   # normalised dB
        phase = np.degrees(np.unwrap(np.angle(H)))

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

        ax1.plot(freqs / 1e3, mag, 'b-', linewidth=2)
        ax1.set_ylabel('Magnitude (dB, normalised)', fontsize=12)
        ax1.set_title('Resonator Bode Response', fontsize=14, fontweight='bold')
        ax1.axvline(f0 / 1e3, color='gray', linestyle='--', linewidth=1, label=f'f₀ = {f0/1e3:.2f} kHz')
        ax1.legend(fontsize=10)
        ax1.grid(True, alpha=0.3)

        ax2.plot(freqs / 1e3, phase, 'r-', linewidth=2)
        ax2.set_xlabel('Frequency (kHz)', fontsize=12)
        ax2.set_ylabel('Phase (°)', fontsize=12)
        ax2.axvline(f0 / 1e3, color='gray', linestyle='--', linewidth=1)
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        
        # Determine save path
        if save_path:
            final_path = save_path
        elif auto_save:
            final_path = get_image_path('bode_plot.png')
        else:
            final_path = None
            
        if final_path:
            plt.savefig(final_path, dpi=300, bbox_inches='tight')
            print(f"  → Saved: {final_path}")
            
        plt.show()

    # --- 6b.  Nyquist circle -----------------------------------------
    def plot_nyquist(self,
                     freq_range: Optional[Tuple[float, float]] = None,
                     n_points: int = 2000,
                     save_path: Optional[str] = None,
                     auto_save: bool = True):
        """
        Nyquist (real vs imag) plot — useful for Q extraction.

        Args:
            freq_range : (f_low, f_high) in Hz
            n_points   : frequency samples
            save_path  : optional path to save figure (overrides auto_save)
            auto_save  : if True and save_path is None, auto-saves to images/resonator/
        """
        f0 = self.resonant_frequency()
        if freq_range is None:
            freq_range = (0.5 * f0, 1.5 * f0)

        freqs = np.linspace(freq_range[0], freq_range[1], n_points)
        H     = self.transfer_function(freqs)
        H_n   = H / np.abs(H).max()   # normalise

        plt.figure(figsize=(8, 8))
        plt.plot(H_n.real, -H_n.imag, 'b-', linewidth=2)
        plt.plot(H_n.real[0], -H_n.imag[0], 'go', markersize=8, label='Start')
        plt.plot(H_n.real[-1], -H_n.imag[-1], 'rs', markersize=8, label='End')

        # Mark resonance (peak imaginary)
        idx_res = np.argmax(-H_n.imag)
        plt.plot(H_n.real[idx_res], -H_n.imag[idx_res], 'k*', markersize=14, label='Resonance')

        plt.xlabel('Real (normalised)', fontsize=12)
        plt.ylabel('−Imag (normalised)', fontsize=12)
        plt.title('Nyquist Plot – Resonator Response', fontsize=14, fontweight='bold')
        plt.legend(fontsize=10)
        plt.grid(True, alpha=0.3)
        plt.axis('equal')

        # Determine save path
        if save_path:
            final_path = save_path
        elif auto_save:
            final_path = get_image_path('nyquist_plot.png')
        else:
            final_path = None
            
        if final_path:
            plt.savefig(final_path, dpi=300, bbox_inches='tight')
            print(f"  → Saved: {final_path}")
            
        plt.show()

    # --- 6c.  Duffing backbone + linear comparison -----------------
    def plot_duffing_backbone(self,
                              amplitude_range: Optional[np.ndarray] = None,
                              alpha_override: Optional[float]      = None,
                              save_path: Optional[str]             = None,
                              auto_save: bool = True):
        """
        Backbone curve (hardening / softening) vs linear resonance.

        Args:
            amplitude_range : array of amplitudes (m).  Defaults 0…500 nm.
            alpha_override  : cubic stiffness (N/m³).   Defaults to geometric estimate.
            save_path       : optional path to save figure (overrides auto_save)
            auto_save       : if True and save_path is None, auto-saves to images/resonator/
        """
        w0    = self.angular_frequency()
        alpha = alpha_override if alpha_override is not None else self.estimate_cubic_stiffness()

        if amplitude_range is None:
            amplitude_range = np.linspace(0, 500e-9, 200)

        w_back = self.duffing_backbone(amplitude_range, w0, alpha)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(w_back / (2 * np.pi * 1e3), amplitude_range * 1e9,
                'b-', linewidth=2, label='Duffing backbone')
        ax.axvline(w0 / (2 * np.pi * 1e3), color='r', linestyle='--',
                   linewidth=1.5, label=f'Linear f₀ = {w0/(2*np.pi*1e3):.2f} kHz')

        ax.set_xlabel('Frequency (kHz)',       fontsize=12)
        ax.set_ylabel('Oscillation Amplitude (nm)', fontsize=12)
        ax.set_title('Duffing Nonlinear Backbone Curve',
                     fontsize=14, fontweight='bold')

        # Annotation for hardening / softening
        label_text = 'Hardening (α > 0)' if alpha > 0 else 'Softening (α < 0)'
        ax.annotate(label_text,
                    xy=(w_back[-1] / (2 * np.pi * 1e3), amplitude_range[-1] * 1e9),
                    xytext=(w_back[len(w_back)//2] / (2 * np.pi * 1e3),
                            amplitude_range[-1] * 1e9 * 0.75),
                    fontsize=11, color='blue',
                    arrowprops=dict(arrowstyle='->', color='blue'))

        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)

        # Determine save path
        if save_path:
            final_path = save_path
        elif auto_save:
            final_path = get_image_path('duffing_backbone.png')
        else:
            final_path = None
            
        if final_path:
            plt.savefig(final_path, dpi=300, bbox_inches='tight')
            print(f"  → Saved: {final_path}")
            
        plt.show()

    # --- 6d.  Sensitivity bar chart ----------------------------------
    def plot_sensitivity(self, save_path: Optional[str] = None, auto_save: bool = True):
        """
        Relative sensitivity of f₀ to ±10 % variations in every geometry
        parameter.  Displayed as a horizontal bar chart.

        Args:
            save_path : optional path to save figure (overrides auto_save)
            auto_save : if True and save_path is None, auto-saves to images/resonator/
        """
        params = {
            'beam_length':     self.geom.beam_length,
            'beam_width':      self.geom.beam_width,
            'beam_thickness':  self.geom.beam_thickness,
        }
        if self.geom.has_proof_mass:
            params['mass_length']    = self.geom.mass_length
            params['mass_width']     = self.geom.mass_width
            params['mass_thickness'] = self.geom.mass_thickness

        f0_nom = self.resonant_frequency()
        labels, sens_pos, sens_neg = [], [], []

        for name, nom_val in params.items():
            vals, freqs = self.sensitivity_sweep(name, nom_val, tolerance_pct=10, n_points=3)
            # vals[0] = -10 %, vals[2] = +10 %
            sens_neg.append((freqs[0] - f0_nom) / f0_nom * 100)
            sens_pos.append((freqs[2] - f0_nom) / f0_nom * 100)
            labels.append(name.replace('_', ' ').title())

        y_pos = np.arange(len(labels))

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.barh(y_pos, sens_pos, height=0.35, left=0,  color='steelblue',  label='+10 %')
        ax.barh(y_pos, sens_neg, height=0.35, left=0,  color='salmon',     label='−10 %')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels, fontsize=11)
        ax.set_xlabel('Δf₀ / f₀  (%)', fontsize=12)
        ax.set_title('Fabrication Sensitivity – Resonant Frequency',
                     fontsize=14, fontweight='bold')
        ax.axvline(0, color='black', linewidth=0.8)
        ax.legend(fontsize=10)
        ax.grid(True, axis='x', alpha=0.3)

        plt.tight_layout()
        
        # Determine save path
        if save_path:
            final_path = save_path
        elif auto_save:
            final_path = get_image_path('sensitivity_analysis.png')
        else:
            final_path = None
            
        if final_path:
            plt.savefig(final_path, dpi=300, bbox_inches='tight')
            print(f"  → Saved: {final_path}")
            
        plt.show()

    # ==================================================================
    # 7.  3-D VISUALISATION
    # ==================================================================

    def visualize_3d_structure(self,
                               displacement: float  = 0.0,
                               show_mode_shape: bool = True,
                               save_path: Optional[str] = None,
                               auto_save: bool = True):
        """
        Render the resonator structure in 3-D.

        The proof-mass (if present) is shown in dark-grey; each beam is
        colour-mapped by its local deflection according to the first
        fixed–guided mode shape when *show_mode_shape* is True.

        Args:
            displacement    : tip displacement to visualise           (m)
            show_mode_shape : colour-map beams by mode shape
            save_path       : optional path to save figure (overrides auto_save)
            auto_save       : if True and save_path is None, auto-saves to images/resonator/
        """
        fig = plt.figure(figsize=(14, 10))
        ax  = fig.add_subplot(111, projection='3d')

        # ── unit conversions to μm ──────────────────────────────────
        L  = self.geom.beam_length    * 1e6
        w  = self.geom.beam_width     * 1e6
        t  = self.geom.beam_thickness * 1e6
        d  = displacement            * 1e6   # tip displacement  (μm)
        gap = self.geom.anchor_gap   * 1e6

        n  = self.geom.n_beams
        # total width occupied by beams + gaps between them
        total_y = n * w + (n - 1) * gap

        # ── colour map setup ────────────────────────────────────────
        cmap  = cm.coolwarm
        norm  = Normalize(vmin=-abs(d) if d != 0 else -1, vmax=abs(d) if d != 0 else 1)

        # ── draw each beam ──────────────────────────────────────────
        n_segments = 20                         # segments along length
        x_vals     = np.linspace(0, L, n_segments + 1)

        # first fixed–guided mode shape  ≈  x² (3L − x) / (2L³)  normalised
        mode_raw = x_vals**2 * (3 * L - x_vals) / (2.0 * L**3)
        mode_shape = mode_raw / mode_raw.max() * d   # scaled to tip displacement

        for i in range(n):
            y_base = i * (w + gap)

            for s in range(n_segments):
                x0, x1 = x_vals[s], x_vals[s + 1]
                z0, z1 = mode_shape[s], mode_shape[s + 1]

                if show_mode_shape and d != 0:
                    colour = cmap(norm((z0 + z1) / 2.0))
                else:
                    colour = 'steelblue'

                self._draw_beam_segment(ax, x0, x1, y_base, w, t, z0, z1, colour)

        # ── anchor blocks (fixed ends) ──────────────────────────────
        anchor_size = w * 1.5
        for i in range(n):
            y_base = i * (w + gap)
            self._draw_box(ax, -anchor_size, 0, y_base, anchor_size, w, t,
                           color='dimgray', alpha=0.8,
                           label='Anchor' if i == 0 else '')

        # ── proof mass ──────────────────────────────────────────────
        if self.geom.has_proof_mass:
            mL = self.geom.mass_length    * 1e6
            mW = self.geom.mass_width     * 1e6
            mT = self.geom.mass_thickness * 1e6

            # centre the mass on the beam array, attached at x = L
            mass_y = (total_y - mW) / 2.0
            mass_z = d   # displaced with beams

            self._draw_box(ax, L, L + mL, mass_y, mW, mT, 0,
                           z_offset=mass_z,
                           color='darkslategray', alpha=0.7, label='Proof mass')

        # ── colour bar ──────────────────────────────────────────────
        if show_mode_shape and d != 0:
            sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
            sm.set_array([])
            cbar = fig.colorbar(sm, ax=ax, shrink=0.5, pad=0.1)
            cbar.set_label('Lateral Displacement (μm)', fontsize=10)

        # ── axes & title ────────────────────────────────────────────
        ax.set_xlabel('X (μm)', fontsize=12)
        ax.set_ylabel('Y (μm)', fontsize=12)
        ax.set_zlabel('Z (μm)', fontsize=12)
        ax.set_title(f'3D Resonator Structure  (tip displacement: {d:.2f} μm)',
                     fontsize=14, fontweight='bold')
        ax.legend(fontsize=10, loc='upper left')

        # ── set limits ──────────────────────────────────────────────
        x_max = L * 1.6 if not self.geom.has_proof_mass else L + self.geom.mass_length * 1e6 + 10
        ax.set_xlim([-anchor_size - 5, x_max])
        ax.set_ylim([-5, total_y + 5])
        ax.set_zlim([-abs(d) - t, abs(d) + t * 2])

        # Determine save path
        if save_path:
            final_path = save_path
        elif auto_save:
            final_path = get_image_path('3d_structure.png')
        else:
            final_path = None
            
        if final_path:
            plt.savefig(final_path, dpi=300, bbox_inches='tight')
            print(f"  → Saved: {final_path}")
            
        plt.show()

    # ==================================================================
    # 8.  REPORT
    # ==================================================================

    def generate_report(self) -> str:
        """
        Pretty-printed summary of all computed resonator parameters.

        Returns
        -------
        str   Formatted report block.
        """
        k    = self.spring_constant()
        m    = self.effective_mass()
        f0   = self.resonant_frequency()
        Q    = self.quality_factor()
        b    = self.damping_coefficient()
        alpha = self.estimate_cubic_stiffness()

        report = f"""
╔══════════════════════════════════════════════════════════════╗
║            MEMS RESONATOR ANALYSIS REPORT                    ║
╚══════════════════════════════════════════════════════════════╝

GEOMETRY PARAMETERS:
────────────────────────────────────────────────────────────────
  Beam Length:              {self.geom.beam_length   *1e6:>10.2f} μm
  Beam Width:               {self.geom.beam_width    *1e6:>10.2f} μm
  Beam Thickness:           {self.geom.beam_thickness*1e6:>10.2f} μm
  Number of Beams:          {self.geom.n_beams:>10d}
  Anchor Gap:               {self.geom.anchor_gap    *1e6:>10.2f} μm"""

        if self.geom.has_proof_mass:
            report += f"""
  Proof-Mass Length:        {self.geom.mass_length   *1e6:>10.2f} μm
  Proof-Mass Width:         {self.geom.mass_width    *1e6:>10.2f} μm
  Proof-Mass Thickness:     {self.geom.mass_thickness*1e6:>10.2f} μm"""

        report += f"""

MATERIAL PROPERTIES:
────────────────────────────────────────────────────────────────
  Young's Modulus:          {self.material.youngs_modulus /1e9:>10.2f} GPa
  Density:                  {self.material.density        :>10.1f} kg/m³
  Poisson's Ratio:          {self.material.poissons_ratio :>10.3f}
  Residual Stress:          {self.material.residual_stress/1e6:>10.2f} MPa

LUMPED PARAMETERS:
────────────────────────────────────────────────────────────────
  Effective Mass:           {m  *1e12:>10.4f} pg
  Spring Constant:          {k  :>10.4f} N/m
  Damping Coefficient:      {b  *1e9 :>10.4f} nN·s/m

DYNAMIC CHARACTERISTICS:
────────────────────────────────────────────────────────────────
  Resonant Frequency  f₀:   {f0 /1e3 :>10.4f} kHz
  Quality Factor  Q:        {Q  :>10.1f}
  Bandwidth  Δf (f₀/Q):    {f0/Q/1e3:>10.4f} kHz

NONLINEAR (DUFFING):
────────────────────────────────────────────────────────────────
  Cubic Stiffness  α:       {alpha  :>12.4e} N/m³
  Type:                     {'Hardening' if alpha > 0 else 'Softening'}

DAMPING MODEL:
────────────────────────────────────────────────────────────────
  Model:                    {self.damping.model_type}
  Gap (if applicable):      {self.damping.gap *1e6:>10.2f} μm
  Pressure:                 {self.damping.pressure/1e3:>10.2f} kPa

"""
        return report

    # ==================================================================
    # PRIVATE  –  3-D drawing helpers
    # ==================================================================

    @staticmethod
    def _draw_beam_segment(ax, x0, x1, y_base, w, t, z0, z1, color, alpha=0.75):
        """
        Draw one trapezoidal segment of a deflected beam.

        The segment runs from (x0, y_base, z0) to (x1, y_base, z1) with
        width *w* (Y) and thickness *t* (Z).
        """
        # bottom face z-offsets
        zb0, zb1 = z0, z1
        # top face
        zt0, zt1 = z0 + t, z1 + t

        v = [
            [x0, y_base,     zb0],   # 0  bot-left-front
            [x1, y_base,     zb1],   # 1  bot-left-back
            [x1, y_base + w, zb1],   # 2  bot-right-back
            [x0, y_base + w, zb0],   # 3  bot-right-front
            [x0, y_base,     zt0],   # 4  top-left-front
            [x1, y_base,     zt1],   # 5  top-left-back
            [x1, y_base + w, zt1],   # 6  top-right-back
            [x0, y_base + w, zt0],   # 7  top-right-front
        ]

        faces = [
            [v[0], v[1], v[5], v[4]],   # left
            [v[2], v[3], v[7], v[6]],   # right
            [v[0], v[3], v[7], v[4]],   # front
            [v[1], v[2], v[6], v[5]],   # back
            [v[0], v[1], v[2], v[3]],   # bottom
            [v[4], v[5], v[6], v[7]],   # top
        ]

        poly = Poly3DCollection(faces, alpha=alpha,
                                facecolor=color, edgecolor='black', linewidth=0.3)
        ax.add_collection3d(poly)

    @staticmethod
    def _draw_box(ax, x0, x1, y0, w, h, z0,
                  z_offset=0.0, color='gray', alpha=0.7, label=''):
        """
        Draw an axis-aligned box from (x0, y0, z0+z_offset) with
        dimensions (x1-x0) × w × h.
        """
        dx = x1 - x0
        v = [
            [x0,      y0,     z0 + z_offset],
            [x0 + dx, y0,     z0 + z_offset],
            [x0 + dx, y0 + w, z0 + z_offset],
            [x0,      y0 + w, z0 + z_offset],
            [x0,      y0,     z0 + z_offset + h],
            [x0 + dx, y0,     z0 + z_offset + h],
            [x0 + dx, y0 + w, z0 + z_offset + h],
            [x0,      y0 + w, z0 + z_offset + h],
        ]
        faces = [
            [v[0], v[1], v[5], v[4]],
            [v[2], v[3], v[7], v[6]],
            [v[0], v[3], v[7], v[4]],
            [v[1], v[2], v[6], v[5]],
            [v[0], v[1], v[2], v[3]],
            [v[4], v[5], v[6], v[7]],
        ]
        poly = Poly3DCollection(faces, alpha=alpha,
                                facecolor=color, edgecolor='black', linewidth=0.4)
        if label:
            poly.set_label(label)
        ax.add_collection3d(poly)


# ---------------------------------------------------------------------------
# Example / demo runner
# ---------------------------------------------------------------------------

def example_analysis():
    """
    Full demo: lumped parameters → Bode → Nyquist → Duffing →
    sensitivity → 3-D structure.
    """
    print("=" * 70)
    print("MEMS RESONATOR RESPONSE ANALYSIS – DEMO")
    print("=" * 70)

    # ── geometry: 2-beam fixed–guided resonator with proof mass ──
    geometry = ResonatorGeometry(
        beam_length    = 200e-6,     # 200 μm
        beam_width     =   4e-6,     #   4 μm
        beam_thickness =  10e-6,     #  10 μm
        n_beams        = 2,
        anchor_gap     =   2e-6,     #   2 μm
        mass_length    =  60e-6,     #  60 μm  proof mass
        mass_width     = 100e-6,     # 100 μm
        mass_thickness =  10e-6,     #  10 μm
    )

    # ── damping: squeeze-film ─────────────────────────────────────
    damping = DampingModel(
        model_type     = 'squeeze',
        gap            =   2e-6,
        pressure       = P_ATM,
    )

    analyzer = ResonatorAnalyzer(geometry, damping=damping)

    # ── print report ──────────────────────────────────────────────
    print(analyzer.generate_report())

    # ── 1.  Bode ──────────────────────────────────────────────────
    print("Generating Bode plot …")
    analyzer.plot_bode()

    # ── 2.  Nyquist ───────────────────────────────────────────────
    print("Generating Nyquist plot …")
    analyzer.plot_nyquist()

    # ── 3.  Duffing backbone ──────────────────────────────────────
    print("Generating Duffing backbone …")
    analyzer.plot_duffing_backbone()

    # ── 4.  Sensitivity ───────────────────────────────────────────
    print("Generating sensitivity chart …")
    analyzer.plot_sensitivity()

    # ── 5.  3-D view ──────────────────────────────────────────────
    print("Generating 3D structure …")
    analyzer.visualize_3d_structure(displacement=3e-6, show_mode_shape=True)

    print("\nAnalysis complete!")
    print(f"\n{'='*70}")
    print(f"All images saved to: {IMAGE_DIR}")
    print(f"{'='*70}\n")


def compare_damping_models():
    """
    Side-by-side Bode comparison of squeeze, slide, and constant-Q models
    for the same geometry.
    """
    print("=" * 70)
    print("DAMPING MODEL COMPARISON")
    print("=" * 70)

    geometry = ResonatorGeometry(
        beam_length=200e-6, beam_width=4e-6, beam_thickness=10e-6,
        n_beams=2, anchor_gap=2e-6,
        mass_length=60e-6, mass_width=100e-6, mass_thickness=10e-6,
    )

    models = {
        'Squeeze film':  DampingModel(model_type='squeeze', gap=2e-6),
        'Slide film':    DampingModel(model_type='slide',   gap=2e-6),
        'Constant Q=50': DampingModel(model_type='constant_Q', quality_factor=50),
    }

    # frequency vector centred on resonance
    ref = ResonatorAnalyzer(geometry, damping=DampingModel(model_type='constant_Q', quality_factor=100))
    f0  = ref.resonant_frequency()
    freqs = np.linspace(0.5 * f0, 1.5 * f0, 2000)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    for (label, damp), clr in zip(models.items(), colors):
        a = ResonatorAnalyzer(geometry, damping=damp)
        H = a.transfer_function(freqs)
        mag   = 20.0 * np.log10(np.abs(H) / np.abs(H).max())
        phase = np.degrees(np.unwrap(np.angle(H)))

        ax1.plot(freqs / 1e3, mag,   color=clr, linewidth=2, label=f'{label}  (Q={a.quality_factor():.1f})')
        ax2.plot(freqs / 1e3, phase, color=clr, linewidth=2)

    ax1.set_ylabel('Magnitude (dB, norm.)', fontsize=12)
    ax1.set_title('Damping Model Comparison – Bode', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)

    ax2.set_xlabel('Frequency (kHz)', fontsize=12)
    ax2.set_ylabel('Phase (°)',       fontsize=12)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    
    # Save to images folder
    save_path = get_image_path('damping_comparison.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"  → Saved: {save_path}")
    
    plt.show()


# ---------------------------------------------------------------------------
# __main__
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    example_analysis()

    print("\n" + "=" * 70)
    print("DAMPING MODEL COMPARISON")
    print("=" * 70 + "\n")

    compare_damping_models()