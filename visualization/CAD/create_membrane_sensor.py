"""
Membrane Pressure Sensor Simulation
For Silicon Fabrication Handbook Project
https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.constants import epsilon_0

class MembranePressureSensor:
    """
    Simulates a MEMS membrane pressure sensor
    Based on silicon fabrication techniques
    """
    
    def __init__(self, length=100e-6, width=100e-6, thickness=2e-6, 
                 gap=2e-6, youngs_modulus=169e9, poisson_ratio=0.22,
                 dielectric_constant=3.9):
        """
        Initialize membrane pressure sensor parameters
        
        Parameters:
        -----------
        length : float
            Membrane length (m)
        width : float
            Membrane width (m)
        thickness : float
            Membrane thickness (m)
        gap : float
            Initial gap between membrane and substrate (m)
        youngs_modulus : float
            Young's modulus of silicon (Pa)
        poisson_ratio : float
            Poisson's ratio of silicon
        dielectric_constant : float
            Relative dielectric constant of insulator
        """
        self.length = length
        self.width = width
        self.thickness = thickness
        self.gap = gap
        self.E = youngs_modulus
        self.v = poisson_ratio
        self.eps_r = dielectric_constant
        self.eps_0 = epsilon_0
        
        # Calculate derived parameters
        self.area = length * width
        self.damping_coefficient = self.calculate_damping()
        
    def calculate_plate_constant(self):
        """Calculate plate constant D"""
        D = (self.E * self.thickness**3) / (12 * (1 - self.v**2))
        return D
    
    def calculate_max_deflection(self, pressure):
        """
        Calculate maximum deflection at center for rectangular membrane
        Using small deflection theory
        """
        D = self.calculate_plate_constant()
        a = self.length / 2
        b = self.width / 2
        
        # Coefficients for rectangular plate with all edges clamped
        alpha = 0.0284  # for a/b = 1
        if abs(a/b - 1) > 0.1:
            # Different aspect ratio
            alpha = 0.0284 * (1 + 0.5*(b/a)**4)
        
        w_max = alpha * (pressure * a**4) / D
        return w_max
    
    def calculate_capacitance(self, pressure, voltage=0):
        """
        Calculate capacitance under pressure
        Includes electrostatic effects if voltage > 0
        """
        w_max = self.calculate_max_deflection(pressure)
        
        if w_max >= self.gap:
            print("Warning: Membrane touching substrate!")
            return np.inf
        
        # Approximate capacitance for deflected membrane
        # Using parallel plate approximation with average gap
        avg_gap = self.gap - w_max/2
        C = (self.eps_r * self.eps_0 * self.area) / avg_gap
        
        return C
    
    def calculate_damping(self):
        """Calculate squeeze film damping coefficient"""
        # For air at room temperature
        viscosity = 1.8e-5  # Pa·s
        damping = (12 * viscosity * self.area**2) / (self.gap**3)
        return damping
    
    def calculate_sensitivity(self, pressure_range=(0, 100000)):
        """
        Calculate sensitivity in F/Pa
        """
        p_min, p_max = pressure_range
        pressures = np.linspace(p_min, p_max, 100)
        capacitances = [self.calculate_capacitance(p) for p in pressures]
        
        # Linear fit for sensitivity
        coeffs = np.polyfit(pressures, capacitances, 1)
        sensitivity = coeffs[0]  # Slope in F/Pa
        
        return sensitivity
    
    def pull_in_analysis(self, max_voltage=50):
        """
        Analyze pull-in voltage and instability
        """
        voltages = np.linspace(0, max_voltage, 100)
        pull_in_voltage = None
        
        for V in voltages:
            # Electrostatic pressure
            P_elec = (self.eps_r * self.eps_0 * V**2) / (2 * self.gap**2)
            w_max = self.calculate_max_deflection(P_elec)
            
            if w_max > self.gap / 3:  # Approximate pull-in condition
                pull_in_voltage = V
                break
        
        return pull_in_voltage
    
    def generate_fabrication_steps(self):
        """Generate typical fabrication steps for this sensor"""
        steps = [
            "1. Silicon wafer cleaning and oxidation",
            "2. LPCVD deposition of silicon nitride (500 nm)",
            "3. Photolithography for backside cavity mask",
            "4. RIE etching of silicon nitride",
            "5. KOH etching of silicon for cavity",
            "6. Photolithography for membrane definition",
            "7. DRIE etching for membrane release",
            "8. Aluminum deposition and patterning for electrodes",
            "9. Critical point drying for release",
            "10. Packaging and wire bonding"
        ]
        return steps

def simulate_pressure_response():
    """Main simulation function"""
    # Create sensor instance
    sensor = MembranePressureSensor(
        length=200e-6,
        width=200e-6,
        thickness=2e-6,
        gap=3e-6
    )
    
    # Pressure sweep
    pressures = np.linspace(0, 200000, 100)  # 0 to 2 bar
    capacitances = []
    deflections = []
    
    for p in pressures:
        w_max = sensor.calculate_max_deflection(p)
        C = sensor.calculate_capacitance(p)
        
        deflections.append(w_max)
        capacitances.append(C)
    
    # Convert to more readable units
    pressures_kpa = pressures / 1000
    capacitances_pf = np.array(capacitances) * 1e12
    deflections_nm = np.array(deflections) * 1e9
    
    # Plot results
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Capacitance vs Pressure
    ax1.plot(pressures_kpa, capacitances_pf, 'b-', linewidth=2)
    ax1.set_xlabel('Pressure (kPa)')
    ax1.set_ylabel('Capacitance (pF)')
    ax1.set_title('Membrane Pressure Sensor Response')
    ax1.grid(True, alpha=0.3)
    
    # Deflection vs Pressure
    ax2.plot(pressures_kpa, deflections_nm, 'r-', linewidth=2)
    ax2.set_xlabel('Pressure (kPa)')
    ax2.set_ylabel('Maximum Deflection (nm)')
    ax2.grid(True, alpha=0.3)
    
    # Calculate sensitivity
    sensitivity = sensor.calculate_sensitivity()
    print(f"Sensor Parameters:")
    print(f"  Membrane size: {sensor.length*1e6:.1f} x {sensor.width*1e6:.1f} µm²")
    print(f"  Membrane thickness: {sensor.thickness*1e6:.1f} µm")
    print(f"  Initial gap: {sensor.gap*1e6:.1f} µm")
    print(f"  Sensitivity: {sensitivity*1e15:.2f} fF/Pa")
    
    plt.tight_layout()
    plt.savefig('membrane_sensor_response.png', dpi=150)
    plt.show()
    
    return sensor, pressures_kpa, capacitances_pf, deflections_nm

if __name__ == "__main__":
    sensor, pressures, capacitances, deflections = simulate_pressure_response()