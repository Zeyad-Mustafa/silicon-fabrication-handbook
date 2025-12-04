import numpy as np
import matplotlib.pyplot as plt

class InterconnectModel:
    """Model interconnect scaling behavior across technology nodes"""
    
    def __init__(self):
        # Material properties
        self.rho_cu = 1.7e-8  # Copper resistivity (Ω·m)
        self.k_sio2 = 4.0     # SiO2 dielectric constant
        self.epsilon_0 = 8.854e-12  # Vacuum permittivity
        
    def wire_resistance(self, length, width, height):
        """Calculate wire resistance"""
        area = width * height
        return self.rho_cu * length / area
    
    def wire_capacitance(self, length, width, spacing, k_eff):
        """Simplified parallel-plate capacitance model"""
        epsilon = k_eff * self.epsilon_0
        return epsilon * length * width / spacing
    
    def rc_delay(self, length, width, height, spacing, k_eff):
        """Calculate interconnect RC delay"""
        R = self.wire_resistance(length, width, height)
        C = self.wire_capacitance(length, width, spacing, k_eff)
        return R * C
    
    def scaling_analysis(self, base_feature_size=90e-9):
        """Analyze interconnect behavior across technology nodes"""
        scaling_factors = np.array([1, 0.7, 0.5, 0.35, 0.25])  # Technology scaling
        nodes = base_feature_size / scaling_factors * 1e9  # Convert to nm
        
        # Base wire parameters (at 90nm node)
        base_length = 1000e-9  # 1 µm wire
        base_width = 90e-9
        base_height = 180e-9
        base_spacing = 90e-9
        
        # Dielectric evolution
        k_values = [4.0, 3.6, 3.0, 2.7, 2.5]
        
        delays = []
        resistances = []
        capacitances = []
        
        for i, s in enumerate(scaling_factors):
            # Scaled dimensions
            length = base_length / s  # Wire length scales with chip size
            width = base_width * s
            height = base_height * s
            spacing = base_spacing * s
            
            R = self.wire_resistance(length, width, height)
            C = self.wire_capacitance(length, width, spacing, k_values[i])
            delay = R * C
            
            resistances.append(R / 1e3)  # Convert to kΩ
            capacitances.append(C / 1e-15)  # Convert to fF
            delays.append(delay / 1e-12)  # Convert to ps
        
        return nodes, resistances, capacitances, delays
    
    def plot_scaling_trends(self):
        """Visualize interconnect scaling challenges"""
        nodes, R, C, delays = self.scaling_analysis()
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle('Interconnect Scaling Trends', fontsize=16, fontweight='bold')
        
        # Resistance vs node
        axes[0, 0].plot(nodes, R, 'o-', color='#e74c3c', linewidth=2, markersize=8)
        axes[0, 0].set_xlabel('Technology Node (nm)', fontweight='bold')
        axes[0, 0].set_ylabel('Resistance (kΩ)', fontweight='bold')
        axes[0, 0].set_title('Wire Resistance Increases')
        axes[0, 0].grid(True, alpha=0.3)
        axes[0, 0].invert_xaxis()
        
        # Capacitance vs node
        axes[0, 1].plot(nodes, C, 's-', color='#3498db', linewidth=2, markersize=8)
        axes[0, 1].set_xlabel('Technology Node (nm)', fontweight='bold')
        axes[0, 1].set_ylabel('Capacitance (fF)', fontweight='bold')
        axes[0, 1].set_title('Wire Capacitance (with Low-k)')
        axes[0, 1].grid(True, alpha=0.3)
        axes[0, 1].invert_xaxis()
        
        # RC Delay vs node
        axes[1, 0].plot(nodes, delays, '^-', color='#9b59b6', linewidth=2, markersize=8)
        axes[1, 0].set_xlabel('Technology Node (nm)', fontweight='bold')
        axes[1, 0].set_ylabel('RC Delay (ps)', fontweight='bold')
        axes[1, 0].set_title('RC Delay Challenge')
        axes[1, 0].grid(True, alpha=0.3)
        axes[1, 0].invert_xaxis()
        
        # Normalized comparison
        axes[1, 1].plot(nodes, R / R[0], 'o-', label='Resistance', linewidth=2, markersize=8)
        axes[1, 1].plot(nodes, C / C[0], 's-', label='Capacitance', linewidth=2, markersize=8)
        axes[1, 1].plot(nodes, delays / delays[0], '^-', label='RC Delay', linewidth=2, markersize=8)
        axes[1, 1].set_xlabel('Technology Node (nm)', fontweight='bold')
        axes[1, 1].set_ylabel('Normalized Value', fontweight='bold')
        axes[1, 1].set_title('Normalized Scaling (90nm = 1.0)')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].invert_xaxis()
        
        plt.tight_layout()
        plt.savefig('interconnect_scaling.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Print summary
        print("\n=== Interconnect Scaling Analysis ===")
        print(f"{'Node (nm)':<12} {'R (kΩ)':<12} {'C (fF)':<12} {'Delay (ps)':<12}")
        print("-" * 50)
        for i in range(len(nodes)):
            print(f"{nodes[i]:<12.1f} {R[i]:<12.3f} {C[i]:<12.3f} {delays[i]:<12.3f}")

# Run simulation
if __name__ == "__main__":
    model = InterconnectModel()
    model.plot_scaling_trends()