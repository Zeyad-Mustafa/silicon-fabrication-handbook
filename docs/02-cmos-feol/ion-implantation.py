#!/usr/bin/env python3
"""
Ion Implantation Profile Simulator
===================================

Simulates ion implantation profiles in silicon including:
- Gaussian concentration profiles
- Range (Rp) and straggle (ΔRp) calculations
- Junction depth determination
- Annealing effects (diffusion and activation)
- Multiple implant scenarios

Based on empirical models and LSS theory for rapid calculations.

Author: Silicon Fabrication Handbook Contributors
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import special, optimize
from dataclasses import dataclass
from typing import Tuple, List

# Physical constants
Q_E = 1.602e-19  # Elementary charge [C]
K_B = 1.381e-23  # Boltzmann constant [J/K]
N_SI = 5.0e22    # Silicon atomic density [atoms/cm³]

OUTPUT_DIR = Path(__file__).resolve().parents[2] / "images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

@dataclass
class IonSpecies:
    """Ion species properties for implantation"""
    name: str
    symbol: str
    mass: float  # Atomic mass [amu]
    
    # Empirical parameters for range calculation in Si
    # Rp = a * E^b / M^c where E in keV
    a: float
    b: float  
    c: float
    
    # Straggle parameter (ΔRp/Rp ratio)
    straggle_ratio: float

# Common dopant species
BORON = IonSpecies("Boron", "B", 11, a=3.0, b=1.0, c=0.5, straggle_ratio=0.35)
BF2 = IonSpecies("Boron Difluoride", "BF₂", 49, a=1.2, b=1.0, c=0.5, straggle_ratio=0.30)
PHOSPHORUS = IonSpecies("Phosphorus", "P", 31, a=2.0, b=1.0, c=0.5, straggle_ratio=0.38)
ARSENIC = IonSpecies("Arsenic", "As", 75, a=1.1, b=1.0, c=0.5, straggle_ratio=0.40)


class ImplantSimulator:
    """
    Simulator for ion implantation profiles
    
    Uses Gaussian approximation and empirical range-energy relationships
    """
    
    def __init__(self, substrate_doping: float = 1e15, 
                 substrate_type: str = 'p'):
        """
        Initialize simulator
        
        Args:
            substrate_doping: Background doping concentration [atoms/cm³]
            substrate_type: 'p' for p-type or 'n' for n-type
        """
        self.substrate_doping = substrate_doping
        self.substrate_type = substrate_type.lower()
        
    def calculate_range(self, energy_kev: float, 
                       ion: IonSpecies) -> Tuple[float, float]:
        """
        Calculate projected range and straggle using empirical formula
        
        Args:
            energy_kev: Ion energy [keV]
            ion: Ion species data
            
        Returns:
            (Rp, delta_Rp) in nanometers
        """
        # Projected range [nm]
        Rp = ion.a * (energy_kev ** ion.b) / (ion.mass ** ion.c)
        
        # Straggle (standard deviation)
        delta_Rp = ion.straggle_ratio * Rp
        
        return Rp, delta_Rp
    
    def implant_profile(self, depth: np.ndarray, 
                       dose: float,
                       energy_kev: float,
                       ion: IonSpecies) -> np.ndarray:
        """
        Calculate Gaussian implant concentration profile
        
        Args:
            depth: Depth array [nm]
            dose: Implant dose [atoms/cm²]
            energy_kev: Ion energy [keV]
            ion: Ion species
            
        Returns:
            Concentration profile [atoms/cm³]
        """
        Rp, delta_Rp = self.calculate_range(energy_kev, ion)
        
        # Convert nm to cm for concentration calculation
        Rp_cm = Rp * 1e-7
        delta_Rp_cm = delta_Rp * 1e-7
        depth_cm = depth * 1e-7
        
        # Gaussian profile
        normalization = 1 / (np.sqrt(2 * np.pi) * delta_Rp_cm)
        exponent = -((depth_cm - Rp_cm) ** 2) / (2 * delta_Rp_cm ** 2)
        
        concentration = dose * normalization * np.exp(exponent)
        
        return concentration
    
    def find_junction_depth(self, depth: np.ndarray, 
                           concentration: np.ndarray,
                           junction_criterion: float = None) -> float:
        """
        Find junction depth where implant equals background doping
        
        Args:
            depth: Depth array [nm]
            concentration: Dopant concentration [atoms/cm³]
            junction_criterion: Override substrate doping level
            
        Returns:
            Junction depth [nm]
        """
        if junction_criterion is None:
            junction_criterion = self.substrate_doping
        
        # Find where concentration crosses substrate doping
        # (assumes monotonic decrease after peak)
        peak_idx = np.argmax(concentration)
        
        # Search after peak
        tail = concentration[peak_idx:]
        depth_tail = depth[peak_idx:]
        
        # Find crossing point
        try:
            cross_idx = np.where(tail < junction_criterion)[0][0]
            
            # Linear interpolation for accuracy
            if cross_idx > 0:
                x1, x2 = depth_tail[cross_idx-1], depth_tail[cross_idx]
                y1, y2 = tail[cross_idx-1], tail[cross_idx]
                
                # Linear interpolation
                x_j = x1 + (junction_criterion - y1) * (x2 - x1) / (y2 - y1)
                return x_j
            else:
                return depth_tail[cross_idx]
                
        except IndexError:
            # Junction deeper than simulation depth
            return depth[-1]
    
    def anneal_diffusion(self, depth: np.ndarray,
                        concentration: np.ndarray,
                        temperature_c: float,
                        time_sec: float,
                        ion: IonSpecies) -> np.ndarray:
        """
        Simple diffusion model during annealing (Fick's 2nd law)
        
        Args:
            depth: Depth array [nm]
            concentration: Initial concentration [atoms/cm³]
            temperature_c: Anneal temperature [°C]
            time_sec: Anneal time [seconds]
            ion: Ion species (determines diffusivity)
            
        Returns:
            Concentration after anneal [atoms/cm³]
        """
        # Diffusion coefficient: D = D0 * exp(-Ea / kT)
        # Arrhenius parameters for dopants in Si
        if ion.symbol == 'B':
            D0 = 0.76  # cm²/s
            Ea = 3.46  # eV
        elif ion.symbol == 'P':
            D0 = 3.85
            Ea = 3.66
        elif ion.symbol == 'As':
            D0 = 0.066
            Ea = 3.44
        else:  # Default to B
            D0 = 0.76
            Ea = 3.46
        
        # Temperature in Kelvin
        T_K = temperature_c + 273.15
        
        # Calculate diffusion coefficient
        D = D0 * np.exp(-Ea * Q_E / (K_B * T_K))  # cm²/s
        
        # Diffusion length
        L_diff = np.sqrt(4 * D * time_sec)  # cm
        L_diff_nm = L_diff * 1e7  # nm
        
        print(f"Diffusion coefficient: {D:.2e} cm²/s")
        print(f"Diffusion length: {L_diff_nm:.1f} nm")
        
        # Simple Gaussian broadening (convolution approximation)
        # This is a simplified model - real diffusion is more complex
        dx = depth[1] - depth[0]  # Grid spacing
        sigma_diff = L_diff_nm / np.sqrt(2)  # Equivalent Gaussian width
        
        # Create Gaussian kernel for convolution
        kernel_width = int(5 * sigma_diff / dx)
        if kernel_width < 3:
            return concentration  # Negligible diffusion
        
        x_kernel = np.arange(-kernel_width, kernel_width + 1) * dx
        kernel = np.exp(-(x_kernel ** 2) / (2 * sigma_diff ** 2))
        kernel = kernel / np.sum(kernel)  # Normalize
        
        # Convolve (simple diffusion model)
        conc_diffused = np.convolve(concentration, kernel, mode='same')
        
        return conc_diffused
    
    def calculate_activation(self, concentration: np.ndarray,
                            temperature_c: float,
                            ion: IonSpecies) -> np.ndarray:
        """
        Calculate activated (substitutional) dopant concentration
        Limited by solid solubility
        
        Args:
            concentration: Total implanted concentration [atoms/cm³]
            temperature_c: Anneal temperature [°C]
            ion: Ion species
            
        Returns:
            Activated concentration [atoms/cm³]
        """
        # Solid solubility limits at given temperature (empirical)
        # These are approximate values for typical RTA temperatures
        T_K = temperature_c + 273.15
        
        if ion.symbol == 'B':
            # Boron solid solubility
            C_max = 5e20 * np.exp(0.0003 * (T_K - 1273))
        elif ion.symbol == 'P':
            C_max = 1.5e21 * np.exp(0.0002 * (T_K - 1273))
        elif ion.symbol == 'As':
            C_max = 2e21 * np.exp(0.0002 * (T_K - 1273))
        else:
            C_max = 5e20
        
        # Activation limited by solubility
        activated = np.minimum(concentration, C_max)
        
        # Typical activation efficiency (~80-95%)
        activation_efficiency = 0.90
        activated = activated * activation_efficiency
        
        return activated


def plot_implant_profiles(simulator: ImplantSimulator,
                         implants: List[dict],
                         max_depth: float = 500):
    """
    Plot multiple implant profiles for comparison
    
    Args:
        simulator: ImplantSimulator instance
        implants: List of implant dictionaries with keys:
                  'ion', 'energy_kev', 'dose', 'label'
        max_depth: Maximum depth to plot [nm]
    """
    depth = np.linspace(0, max_depth, 1000)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    colors = ['b', 'r', 'g', 'm', 'c', 'orange']
    
    for i, impl in enumerate(implants):
        ion = impl['ion']
        energy = impl['energy_kev']
        dose = impl['dose']
        label = impl['label']
        
        # Calculate profile
        conc = simulator.implant_profile(depth, dose, energy, ion)
        
        # Find junction depth
        x_j = simulator.find_junction_depth(depth, conc)
        
        # Get range parameters
        Rp, delta_Rp = simulator.calculate_range(energy, ion)
        
        # Linear scale
        ax1.semilogy(depth, conc, colors[i % len(colors)], 
                    linewidth=2, label=label)
        ax1.axvline(x_j, color=colors[i % len(colors)], 
                   linestyle='--', alpha=0.5)
        
        # Log scale
        ax2.semilogy(depth, conc, colors[i % len(colors)], 
                    linewidth=2, label=label)
        ax2.axvline(Rp, color=colors[i % len(colors)], 
                   linestyle=':', alpha=0.7, linewidth=1)
        
        print(f"\n{label}:")
        print(f"  Rp = {Rp:.1f} nm, ΔRp = {delta_Rp:.1f} nm")
        print(f"  Peak concentration: {np.max(conc):.2e} /cm³")
        print(f"  Junction depth: {x_j:.1f} nm")
    
    # Substrate doping line
    ax1.axhline(simulator.substrate_doping, color='k', 
               linestyle='--', alpha=0.3, label='Substrate')
    ax2.axhline(simulator.substrate_doping, color='k', 
               linestyle='--', alpha=0.3, label='Substrate')
    
    # Formatting
    ax1.set_xlabel('Depth (nm)', fontsize=12)
    ax1.set_ylabel('Concentration (atoms/cm³)', fontsize=12)
    ax1.set_title('Ion Implantation Profiles', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=10)
    ax1.set_ylim([1e14, 1e22])
    
    ax2.set_xlabel('Depth (nm)', fontsize=12)
    ax2.set_ylabel('Concentration (atoms/cm³)', fontsize=12)
    ax2.set_title('Profiles with Projected Range (Rp)', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=10)
    ax2.set_ylim([1e14, 1e22])
    
    plt.tight_layout()
    return fig


def plot_anneal_comparison(simulator: ImplantSimulator):
    """
    Compare as-implanted vs. annealed profiles
    """
    depth = np.linspace(0, 400, 1000)
    
    # Typical NMOS S/D implant
    ion = ARSENIC
    energy = 50  # keV
    dose = 5e15  # atoms/cm²
    
    # As-implanted profile
    conc_as_implanted = simulator.implant_profile(depth, dose, energy, ion)
    
    # After RTA (1000°C, 5 seconds)
    conc_after_rta = simulator.anneal_diffusion(
        depth, conc_as_implanted, 1000, 5, ion)
    
    # With activation limit
    conc_activated = simulator.calculate_activation(
        conc_after_rta, 1000, ion)
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 7))
    
    ax.semilogy(depth, conc_as_implanted, 'b-', linewidth=2, 
               label='As-implanted')
    ax.semilogy(depth, conc_after_rta, 'r--', linewidth=2, 
               label='After RTA (1000°C, 5s)')
    ax.semilogy(depth, conc_activated, 'g:', linewidth=3, 
               label='Activated (solubility limited)')
    
    # Junction depths
    x_j_initial = simulator.find_junction_depth(depth, conc_as_implanted)
    x_j_annealed = simulator.find_junction_depth(depth, conc_after_rta)
    
    ax.axvline(x_j_initial, color='b', linestyle='--', alpha=0.5)
    ax.axvline(x_j_annealed, color='r', linestyle='--', alpha=0.5)
    
    ax.axhline(simulator.substrate_doping, color='k', 
              linestyle='--', alpha=0.3, label='Substrate')
    
    ax.set_xlabel('Depth (nm)', fontsize=12)
    ax.set_ylabel('Concentration (atoms/cm³)', fontsize=12)
    ax.set_title('Effect of RTA on Implant Profile (As S/D)', 
                fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11)
    ax.set_ylim([1e14, 1e22])
    
    plt.tight_layout()
    
    print(f"\nJunction depth shift due to anneal:")
    print(f"  As-implanted: {x_j_initial:.1f} nm")
    print(f"  After RTA: {x_j_annealed:.1f} nm")
    print(f"  Shift: {x_j_annealed - x_j_initial:.1f} nm")
    
    return fig


def compare_ion_species():
    """
    Compare different ion species at same energy
    """
    simulator = ImplantSimulator(substrate_doping=1e15, substrate_type='p')
    
    implants = [
        {'ion': BORON, 'energy_kev': 50, 'dose': 3e15, 
         'label': 'B⁺ 50keV'},
        {'ion': BF2, 'energy_kev': 50, 'dose': 3e15, 
         'label': 'BF₂⁺ 50keV (shallower)'},
        {'ion': PHOSPHORUS, 'energy_kev': 50, 'dose': 5e15, 
         'label': 'P⁺ 50keV'},
        {'ion': ARSENIC, 'energy_kev': 50, 'dose': 5e15, 
         'label': 'As⁺ 50keV (shallowest)'},
    ]
    
    fig = plot_implant_profiles(simulator, implants, max_depth=400)
    fig.suptitle('Comparison of Dopant Species at 50 keV', 
                fontsize=16, fontweight='bold', y=1.02)
    return fig


def compare_energies():
    """
    Compare different energies for same ion
    """
    simulator = ImplantSimulator(substrate_doping=1e16, substrate_type='p')
    
    implants = [
        {'ion': ARSENIC, 'energy_kev': 20, 'dose': 5e15, 
         'label': 'As⁺ 20keV (shallow S/D extension)'},
        {'ion': ARSENIC, 'energy_kev': 50, 'dose': 5e15, 
         'label': 'As⁺ 50keV (S/D)'},
        {'ion': ARSENIC, 'energy_kev': 100, 'dose': 3e15, 
         'label': 'As⁺ 100keV (deep contact)'},
    ]
    
    fig = plot_implant_profiles(simulator, implants, max_depth=300)
    fig.suptitle('Effect of Implant Energy on Depth (Arsenic)', 
                fontsize=16, fontweight='bold', y=1.02)
    return fig


def simulate_cmos_process():
    """
    Simulate typical CMOS transistor implants
    """
    simulator = ImplantSimulator(substrate_doping=5e15, substrate_type='p')
    
    print("\n" + "="*60)
    print("CMOS TRANSISTOR IMPLANT SIMULATION")
    print("="*60)
    
    # NMOS transistor implants
    print("\n--- NMOS Transistor ---")
    implants_nmos = [
        {'ion': BORON, 'energy_kev': 30, 'dose': 2e12, 
         'label': 'NMOS Vth adjust (B⁺)'},
        {'ion': ARSENIC, 'energy_kev': 10, 'dose': 3e14, 
         'label': 'NMOS LDD (As⁺)'},
        {'ion': ARSENIC, 'energy_kev': 40, 'dose': 5e15, 
         'label': 'NMOS S/D (As⁺)'},
    ]
    
    fig1 = plot_implant_profiles(simulator, implants_nmos, max_depth=250)
    fig1.suptitle('NMOS Implant Stack', fontsize=16, fontweight='bold', y=1.02)
    
    # PMOS transistor implants
    print("\n--- PMOS Transistor ---")
    simulator_n = ImplantSimulator(substrate_doping=5e15, substrate_type='n')
    
    implants_pmos = [
        {'ion': PHOSPHORUS, 'energy_kev': 50, 'dose': 2e12, 
         'label': 'PMOS Vth adjust (P⁺)'},
        {'ion': BF2, 'energy_kev': 10, 'dose': 2e14, 
         'label': 'PMOS LDD (BF₂⁺)'},
        {'ion': BF2, 'energy_kev': 25, 'dose': 3e15, 
         'label': 'PMOS S/D (BF₂⁺)'},
    ]
    
    fig2 = plot_implant_profiles(simulator_n, implants_pmos, max_depth=200)
    fig2.suptitle('PMOS Implant Stack', fontsize=16, fontweight='bold', y=1.02)
    
    return fig1, fig2


# Main execution
if __name__ == "__main__":
    print("\n" + "="*70)
    print("ION IMPLANTATION PROFILE SIMULATOR")
    print("="*70)
    
    print("\nThis simulator demonstrates:")
    print("  1. Gaussian concentration profiles")
    print("  2. Range-energy relationships")
    print("  3. Junction depth calculation")
    print("  4. Annealing effects (diffusion & activation)")
    print("  5. Comparison of different ions and energies")
    
    # Example 1: Compare different ion species
    print("\n" + "-"*70)
    print("Example 1: Comparing Ion Species (B, BF₂, P, As)")
    print("-"*70)
    fig1 = compare_ion_species()
    
    # Example 2: Compare different energies
    print("\n" + "-"*70)
    print("Example 2: Energy Effects on Depth (Arsenic)")
    print("-"*70)
    fig2 = compare_energies()
    
    # Example 3: Annealing effects
    print("\n" + "-"*70)
    print("Example 3: Annealing Effects (RTA)")
    print("-"*70)
    simulator = ImplantSimulator(1e15, 'p')
    fig3 = plot_anneal_comparison(simulator)
    
    # Example 4: Full CMOS process
    print("\n" + "-"*70)
    print("Example 4: CMOS Transistor Implant Stack")
    print("-"*70)
    fig4, fig5 = simulate_cmos_process()
    
    # Save figures
    print("\n" + "="*70)
    print("Saving figures...")
    output_species = OUTPUT_DIR / "ion_implant_species_comparison.png"
    output_energy = OUTPUT_DIR / "ion_implant_energy_comparison.png"
    output_anneal = OUTPUT_DIR / "ion_implant_anneal_effects.png"
    output_nmos = OUTPUT_DIR / "nmos_implant_stack.png"
    output_pmos = OUTPUT_DIR / "pmos_implant_stack.png"

    fig1.savefig(output_species, dpi=300, bbox_inches='tight')
    fig2.savefig(output_energy, dpi=300, bbox_inches='tight')
    fig3.savefig(output_anneal, dpi=300, bbox_inches='tight')
    fig4.savefig(output_nmos, dpi=300, bbox_inches='tight')
    fig5.savefig(output_pmos, dpi=300, bbox_inches='tight')
    
    print("\n✓ Figures saved successfully!")
    print(f"  - {output_species}")
    print(f"  - {output_energy}")
    print(f"  - {output_anneal}")
    print(f"  - {output_nmos}")
    print(f"  - {output_pmos}")
    
    print("\n" + "="*70)
    print("Simulation complete!")
    print("="*70 + "\n")
    
    # Display all plots
    plt.show()
