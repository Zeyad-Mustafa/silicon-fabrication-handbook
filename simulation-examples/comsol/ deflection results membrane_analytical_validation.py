"""
Analytical Validation for Membrane Deflection
==============================================

This script provides analytical solutions for circular membrane deflection
to validate COMSOL simulation results.

References:
    - Timoshenko & Woinowsky-Krieger, "Theory of Plates and Shells" (1959)
    - Senturia, "Microsystem Design" (2001)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn, jn_zeros
from dataclasses import dataclass
import pandas as pd

@dataclass
class MembraneProperties:
    """Material and geometric properties of the membrane."""
    radius: float          # m
    thickness: float       # m
    youngs_modulus: float  # Pa
    poisson_ratio: float   # dimensionless
    density: float         # kg/m³
    residual_stress: float # Pa (tensile positive)
    

class MembraneAnalytics:
    """
    Analytical solutions for circular membrane deflection.
    """
    
    def __init__(self, props: MembraneProperties):
        """
        Initialize with membrane properties.
        
        Args:
            props: MembraneProperties object
        """
        self.props = props
        
        # Calculate derived properties
        self.D = self._calculate_flexural_rigidity()
        
    def _calculate_flexural_rigidity(self):
        """Calculate flexural rigidity D."""
        E = self.props.youngs_modulus
        nu = self.props.poisson_ratio
        t = self.props.thickness
        
        D = E * t**3 / (12 * (1 - nu**2))
        return D
    
    def small_deflection_center(self, pressure):
        """
        Calculate center deflection using small deflection theory.
        Valid when w_max << thickness.
        
        Args:
            pressure: Applied uniform pressure (Pa)
            
        Returns:
            Maximum deflection at center (m)
        """
        r = self.props.radius
        E = self.props.youngs_modulus
        nu = self.props.poisson_ratio
        t = self.props.thickness
        
        # Classical plate theory (small deflection)
        w_max = (3 * (1 - nu**2) * pressure * r**4) / (16 * E * t**3)
        
        return w_max
    
    def small_deflection_profile(self, r_points, pressure):
        """
        Calculate deflection profile for small deflections.
        
        Args:
            r_points: Radial positions (m)
            pressure: Applied pressure (Pa)
            
        Returns:
            Deflection at each radial position (m)
        """
        a = self.props.radius
        E = self.props.youngs_modulus
        nu = self.props.poisson_ratio
        t = self.props.thickness
        
        # Normalized radius
        rho = r_points / a
        
        # Deflection profile
        w = (3 * (1 - nu**2) * pressure * a**4) / (16 * E * t**3) * (1 - rho**2)**2
        
        return w
    
    def large_deflection_center(self, pressure, max_iter=100, tol=1e-9):
        """
        Calculate center deflection including geometric nonlinearity.
        Valid for large deflections (w > t/2).
        
        Uses iterative solution of the von Kármán equations.
        
        Args:
            pressure: Applied pressure (Pa)
            max_iter: Maximum iterations
            tol: Convergence tolerance
            
        Returns:
            Maximum deflection at center (m)
        """
        r = self.props.radius
        t = self.props.thickness
        
        # Initial guess using small deflection
        w0 = self.small_deflection_center(pressure)
        
        # Iterative solution
        w = w0
        for i in range(max_iter):
            # Nonlinear correction factor
            C = 1 + 0.488 * (w / t)**2
            
            w_new = w0 * C
            
            if abs(w_new - w) < tol:
                return w_new
                
            w = w_new
            
        print(f"Warning: Large deflection did not converge in {max_iter} iterations")
        return w
    
    def maximum_stress(self, pressure, use_large_deflection=False):
        """
        Calculate maximum stress in the membrane.
        
        Args:
            pressure: Applied pressure (Pa)
            use_large_deflection: Whether to use large deflection theory
            
        Returns:
            Maximum von Mises stress (Pa)
        """
        r = self.props.radius
        t = self.props.thickness
        nu = self.props.poisson_ratio
        
        if use_large_deflection:
            w_max = self.large_deflection_center(pressure)
        else:
            w_max = self.small_deflection_center(pressure)
        
        # Maximum stress occurs at edge, radial direction
        # For small deflections:
        sigma_r_max = (3 * pressure * r**2) / (2 * t**2)
        
        # For large deflections, add membrane stress
        if w_max > 0.5 * t:
            sigma_membrane = (self.props.youngs_modulus * w_max**2) / (r**2)
            sigma_r_max += sigma_membrane
        
        # von Mises stress (approximate)
        sigma_vm = sigma_r_max * np.sqrt(1 - nu + nu**2)
        
        return sigma_vm
    
    def first_resonant_frequency(self):
        """
        Calculate first (fundamental) resonant frequency.
        
        Returns:
            First resonant frequency (Hz)
        """
        r = self.props.radius
        t = self.props.thickness
        E = self.props.youngs_modulus
        nu = self.props.poisson_ratio
        rho = self.props.density
        
        # First mode shape constant for clamped circular plate
        lambda_1 = 10.21
        
        # Frequency calculation
        f1 = (lambda_1 / (2 * np.pi * r**2)) * \
             np.sqrt((E * t**2) / (12 * rho * (1 - nu**2)))
        
        return f1
    
    def resonant_frequencies(self, n_modes=6):
        """
        Calculate first n resonant frequencies.
        
        Args:
            n_modes: Number of modes to calculate
            
        Returns:
            Array of resonant frequencies (Hz)
        """
        # Mode shape constants for clamped circular plate
        lambdas = [10.21, 21.26, 34.88, 51.04, 69.65, 90.74]
        
        r = self.props.radius
        t = self.props.thickness
        E = self.props.youngs_modulus
        nu = self.props.poisson_ratio
        rho = self.props.density
        
        frequencies = []
        for i in range(min(n_modes, len(lambdas))):
            f = (lambdas[i] / (2 * np.pi * r**2)) * \
                np.sqrt((E * t**2) / (12 * rho * (1 - nu**2)))
            frequencies.append(f)
        
        return np.array(frequencies)
    
    def prestressed_frequency(self, mode_number=1):
        """
        Calculate resonant frequency with residual stress.
        
        Args:
            mode_number: Mode number (1, 2, 3, ...)
            
        Returns:
            Resonant frequency with prestress (Hz)
        """
        # Get unstressed frequency
        f0 = self.resonant_frequencies(mode_number)[mode_number-1]
        
        # Prestress effect
        sigma = self.props.residual_stress
        t = self.props.thickness
        r = self.props.radius
        E = self.props.youngs_modulus
        nu = self.props.poisson_ratio
        
        # Frequency shift due to prestress
        # Simplified model
        delta_f = (sigma * t) / (2 * np.pi * r**2 * np.sqrt(12 * self.props.density * (1 - nu**2)))
        
        return np.sqrt(f0**2 + delta_f**2)
    
    def sensitivity(self, pressure):
        """
        Calculate pressure sensitivity (deflection per pressure).
        
        Args:
            pressure: Operating pressure (Pa)
            
        Returns:
            Sensitivity (m/Pa)
        """
        return self.small_deflection_center(pressure) / pressure
    
    def burst_pressure(self, yield_stress):
        """
        Estimate burst pressure based on yield stress.
        
        Args:
            yield_stress: Material yield stress (Pa)
            
        Returns:
            Estimated burst pressure (Pa)
        """
        r = self.props.radius
        t = self.props.thickness
        
        # From maximum stress equation
        p_burst = (2 * yield_stress * t**2) / (3 * r**2)
        
        return p_burst


def compare_with_comsol(comsol_deflection, analytical_deflection, 
                        comsol_stress=None, analytical_stress=None):
    """
    Compare COMSOL results with analytical solutions.
    
    Args:
        comsol_deflection: Deflection from COMSOL (m)
        analytical_deflection: Analytical deflection (m)
        comsol_stress: Stress from COMSOL (Pa), optional
        analytical_stress: Analytical stress (Pa), optional
    """
    print("\n" + "="*60)
    print("COMSOL vs Analytical Comparison")
    print("="*60)
    
    # Deflection comparison
    error_deflection = abs(comsol_deflection - analytical_deflection) / analytical_deflection * 100
    
    print(f"\nDeflection:")
    print(f"  COMSOL:     {comsol_deflection*1e6:.4f} μm")
    print(f"  Analytical: {analytical_deflection*1e6:.4f} μm")
    print(f"  Error:      {error_deflection:.2f}%")
    
    if comsol_stress is not None and analytical_stress is not None:
        error_stress = abs(comsol_stress - analytical_stress) / analytical_stress * 100
        
        print(f"\nMaximum Stress:")
        print(f"  COMSOL:     {comsol_stress/1e6:.2f} MPa")
        print(f"  Analytical: {analytical_stress/1e6:.2f} MPa")
        print(f"  Error:      {error_stress:.2f}%")
    
    # Assessment
    print(f"\nAssessment:")
    if error_deflection < 5:
        print("  ✓ Excellent agreement (< 5% error)")
    elif error_deflection < 10:
        print("  ✓ Good agreement (< 10% error)")
    elif error_deflection < 20:
        print("  ⚠ Acceptable agreement (< 20% error)")
    else:
        print("  ✗ Poor agreement (> 20% error)")
        print("  Check: mesh quality, boundary conditions, material properties")


def plot_deflection_profile(analytics, pressure, save_path='deflection_profile.png'):
    """
    Plot deflection profile across membrane radius.
    
    Args:
        analytics: MembraneAnalytics object
        pressure: Applied pressure (Pa)
        save_path: Path to save the plot
    """
    r_points = np.linspace(0, analytics.props.radius, 100)
    w_points = analytics.small_deflection_profile(r_points, pressure)
    
    plt.figure(figsize=(10, 6))
    plt.plot(r_points*1e6, w_points*1e6, 'b-', linewidth=2, label='Analytical')
    plt.xlabel('Radial Position (μm)', fontsize=12)
    plt.ylabel('Deflection (μm)', fontsize=12)
    plt.title(f'Membrane Deflection Profile\nPressure = {pressure/1000:.1f} kPa', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=11)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Deflection profile saved to {save_path}")
    

def generate_validation_table(analytics, pressure_range):
    """
    Generate validation table for multiple pressures.
    
    Args:
        analytics: MembraneAnalytics object
        pressure_range: Array of pressures (Pa)
        
    Returns:
        Pandas DataFrame with results
    """
    data = {
        'Pressure (kPa)': [],
        'Deflection (μm)': [],
        'Stress (MPa)': [],
        'Sensitivity (nm/Pa)': []
    }
    
    for p in pressure_range:
        w = analytics.small_deflection_center(p)
        s = analytics.maximum_stress(p)
        sens = analytics.sensitivity(p)
        
        data['Pressure (kPa)'].append(p / 1000)
        data['Deflection (μm)'].append(w * 1e6)
        data['Stress (MPa)'].append(s / 1e6)
        data['Sensitivity (nm/Pa)'].append(sens * 1e9)
    
    df = pd.DataFrame(data)
    return df


def main():
    """Main execution function."""
    
    print("="*60)
    print("Membrane Deflection Analytical Validation")
    print("="*60)
    
    # Define membrane properties (example: 500 μm radius, 2 μm thickness)
    props = MembraneProperties(
        radius=500e-6,           # 500 μm
        thickness=2e-6,          # 2 μm
        youngs_modulus=170e9,    # 170 GPa (Silicon)
        poisson_ratio=0.28,
        density=2329,            # kg/m³
        residual_stress=50e6     # 50 MPa
    )
    
    # Create analytics object
    analytics = MembraneAnalytics(props)
    
    # Applied pressure
    pressure = 1e3  # 1 kPa
    
    # Calculate results
    print(f"\nMembrane Properties:")
    print(f"  Radius: {props.radius*1e6:.0f} μm")
    print(f"  Thickness: {props.thickness*1e6:.1f} μm")
    print(f"  Material: Silicon (E = {props.youngs_modulus/1e9:.0f} GPa)")
    
    print(f"\nApplied Pressure: {pressure/1000:.1f} kPa")
    
    # Small deflection analysis
    w_small = analytics.small_deflection_center(pressure)
    print(f"\nSmall Deflection Theory:")
    print(f"  Maximum deflection: {w_small*1e6:.4f} μm")
    print(f"  Deflection/thickness ratio: {w_small/props.thickness:.3f}")
    
    # Check if large deflection theory is needed
    if w_small > 0.5 * props.thickness:
        print("  ⚠ Deflection > t/2: Large deflection theory recommended")
        w_large = analytics.large_deflection_center(pressure)
        print(f"  Large deflection result: {w_large*1e6:.4f} μm")
    else:
        print("  ✓ Small deflection theory valid")
    
    # Stress analysis
    stress = analytics.maximum_stress(pressure)
    print(f"\nStress Analysis:")
    print(f"  Maximum von Mises stress: {stress/1e6:.2f} MPa")
    
    # Safety factor (assuming silicon yield ~110 MPa)
    yield_stress = 110e6  # Pa
    safety_factor = yield_stress / stress
    print(f"  Safety factor: {safety_factor:.2f}")
    
    # Burst pressure
    p_burst = analytics.burst_pressure(yield_stress)
    print(f"  Estimated burst pressure: {p_burst/1000:.1f} kPa")
    
    # Dynamic analysis
    f1 = analytics.first_resonant_frequency()
    print(f"\nDynamic Properties:")
    print(f"  First resonant frequency: {f1/1000:.2f} kHz")
    
    freqs = analytics.resonant_frequencies(6)
    print(f"  First 6 modes (kHz):", 
          ', '.join([f'{f/1000:.2f}' for f in freqs]))
    
    # Sensitivity
    sens = analytics.sensitivity(pressure)
    print(f"\nSensor Performance:")
    print(f"  Sensitivity: {sens*1e9:.3f} nm/Pa")
    
    # Generate validation table
    print(f"\nGenerating validation table...")
    pressure_range = np.linspace(0, 10e3, 11)  # 0 to 10 kPa
    df = generate_validation_table(analytics, pressure_range)
    print("\n" + df.to_string(index=False))
    
    # Save table
    df.to_csv('membrane_validation_table.csv', index=False)
    print("\nValidation table saved to membrane_validation_table.csv")
    
    # Plot deflection profile
    plot_deflection_profile(analytics, pressure)
    
    print("\n" + "="*60)
    print("Analysis Complete!")
    print("="*60)
    print("\nNext Steps:")
    print("  1. Run COMSOL simulation")
    print("  2. Export maximum deflection and stress from COMSOL")
    print("  3. Compare with analytical values above")
    print("  4. Verify mesh independence")
    

if __name__ == '__main__':
    main()