"""
3D Thermal Actuator Simulator
==============================
Simulates a bimorph thermal actuator with real-time 3D visualization.

Author: Silicon Fabrication Handbook
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider, Button
import matplotlib.patches as mpatches

class ThermalActuator:
    """Bimorph thermal actuator model"""
    
    def __init__(self, length=100e-6, width=20e-6, thickness=2e-6):
        # Geometry (in meters)
        self.L = length
        self.W = width
        self.t = thickness
        
        # Material properties
        self.alpha1 = 2.6e-6  # Thermal expansion Si (1/K)
        self.alpha2 = 14.2e-6  # Thermal expansion Al (1/K)
        self.E1 = 170e9  # Young's modulus Si (Pa)
        self.E2 = 70e9   # Young's modulus Al (Pa)
        
        # Thermal properties
        self.k_thermal = 148  # Thermal conductivity Si (W/m·K)
        self.c_p = 700  # Specific heat (J/kg·K)
        self.rho = 2330  # Density (kg/m³)
        
        # State
        self.T = 25  # Temperature (°C)
        self.T_ambient = 25
        self.power = 0  # Heating power (W)
        
    def compute_curvature(self, delta_T):
        """Compute beam curvature due to thermal mismatch"""
        delta_alpha = self.alpha2 - self.alpha1
        # Simplified curvature for bimorph
        kappa = (6 * delta_alpha * delta_T) / self.t
        return kappa
    
    def compute_displacement(self, delta_T):
        """Compute tip displacement"""
        kappa = self.compute_curvature(delta_T)
        # Tip displacement for cantilever
        displacement = 0.5 * kappa * self.L**2
        return displacement
    
    def update_temperature(self, dt):
        """Update temperature with thermal dynamics"""
        # Heating
        heat_in = self.power
        # Cooling (simplified convection)
        heat_out = 0.5 * (self.T - self.T_ambient)
        # Temperature change
        mass = self.rho * self.L * self.W * self.t
        dT_dt = (heat_in - heat_out) / (mass * self.c_p)
        self.T += dT_dt * dt
        self.T = max(self.T_ambient, min(self.T, 300))  # Limit range
        
    def get_beam_shape(self, n_points=50):
        """Generate 3D coordinates of bent beam"""
        x = np.linspace(0, self.L * 1e6, n_points)  # Convert to µm
        delta_T = self.T - self.T_ambient
        kappa = self.compute_curvature(delta_T)
        
        # Beam deflection (parabolic approximation)
        y = 0.5 * kappa * (x * 1e-6)**2 * 1e6  # Convert back to µm
        z = np.zeros_like(x)
        
        return x, y, z

class ThermalActuatorSimulator:
    """Interactive 3D visualization"""
    
    def __init__(self):
        self.actuator = ThermalActuator()
        self.time = 0
        self.running = False
        
        # Setup figure
        self.fig = plt.figure(figsize=(14, 8))
        self.fig.patch.set_facecolor('#0a0a14')
        
        # 3D plot
        self.ax3d = self.fig.add_subplot(121, projection='3d')
        self.ax3d.set_facecolor('#0f0f1a')
        
        # Time series plot
        self.ax_time = self.fig.add_subplot(222)
        self.ax_time.set_facecolor('#0f0f1a')
        
        # Metrics plot
        self.ax_metrics = self.fig.add_subplot(224)
        self.ax_metrics.set_facecolor('#0f0f1a')
        
        # Data storage
        self.t_history = []
        self.temp_history = []
        self.disp_history = []
        
        self.setup_plots()
        self.setup_controls()
        
    def setup_plots(self):
        """Initialize all plots"""
        # 3D beam plot
        x, y, z = self.actuator.get_beam_shape()
        self.beam_line, = self.ax3d.plot(x, y, z, 'o-', color='#ff6b35', 
                                          linewidth=3, markersize=4, label='Beam')
        
        # Base anchor
        self.ax3d.plot([0, 0], [0, 0], [-5, 5], 'o-', color='#2c3e50', 
                       linewidth=8, markersize=10, label='Anchor')
        
        self.ax3d.set_xlabel('Length (µm)', color='white', fontsize=10)
        self.ax3d.set_ylabel('Displacement (µm)', color='white', fontsize=10)
        self.ax3d.set_zlabel('Width (µm)', color='white', fontsize=10)
        self.ax3d.set_title('3D Thermal Actuator', color='white', 
                            fontsize=12, fontweight='bold', pad=10)
        self.ax3d.legend(loc='upper left', fontsize=9)
        
        # Set limits
        self.ax3d.set_xlim(0, 100)
        self.ax3d.set_ylim(-10, 30)
        self.ax3d.set_zlim(-10, 10)
        
        # Style 3D axes
        self.ax3d.tick_params(colors='white', labelsize=8)
        self.ax3d.xaxis.pane.fill = False
        self.ax3d.yaxis.pane.fill = False
        self.ax3d.zaxis.pane.fill = False
        self.ax3d.grid(True, alpha=0.2)
        
        # Temperature plot
        self.temp_line, = self.ax_time.plot([], [], 'o-', color='#ff6b35', 
                                             linewidth=2, markersize=3)
        self.ax_time.set_xlabel('Time (s)', color='white', fontsize=10)
        self.ax_time.set_ylabel('Temperature (°C)', color='white', fontsize=10)
        self.ax_time.set_title('Temperature vs Time', color='white', 
                                fontsize=11, fontweight='bold')
        self.ax_time.grid(True, alpha=0.3, color='white', linestyle='--')
        self.ax_time.tick_params(colors='white', labelsize=9)
        for spine in self.ax_time.spines.values():
            spine.set_color('white')
        
        # Metrics text
        self.metrics_text = self.ax_metrics.text(0.1, 0.5, '', 
                                                  transform=self.ax_metrics.transAxes,
                                                  fontsize=11, color='white',
                                                  family='monospace',
                                                  verticalalignment='center')
        self.ax_metrics.axis('off')
        
    def setup_controls(self):
        """Setup interactive controls"""
        # Power slider
        ax_power = plt.axes([0.15, 0.02, 0.3, 0.03])
        ax_power.set_facecolor('#1a1a2e')
        self.slider_power = Slider(ax_power, 'Power (W)', 0, 10, valinit=0,
                                    color='#ff6b35', valstep=0.1)
        self.slider_power.label.set_color('white')
        self.slider_power.valtext.set_color('white')
        self.slider_power.on_changed(self.update_power)
        
        # Start/Stop button
        ax_btn = plt.axes([0.55, 0.02, 0.1, 0.04])
        ax_btn.set_facecolor('#1a1a2e')
        self.btn_toggle = Button(ax_btn, 'Start', color='#27ae60', 
                                  hovercolor='#2ecc71')
        self.btn_toggle.label.set_color('white')
        self.btn_toggle.on_clicked(self.toggle_simulation)
        
        # Reset button
        ax_reset = plt.axes([0.67, 0.02, 0.1, 0.04])
        ax_reset.set_facecolor('#1a1a2e')
        self.btn_reset = Button(ax_reset, 'Reset', color='#e74c3c', 
                                 hovercolor='#c0392b')
        self.btn_reset.label.set_color('white')
        self.btn_reset.on_clicked(self.reset_simulation)
        
    def update_power(self, val):
        """Update heating power"""
        self.actuator.power = val
        
    def toggle_simulation(self, event):
        """Start/stop simulation"""
        self.running = not self.running
        if self.running:
            self.btn_toggle.label.set_text('Pause')
            self.btn_toggle.color = '#e74c3c'
        else:
            self.btn_toggle.label.set_text('Start')
            self.btn_toggle.color = '#27ae60'
            
    def reset_simulation(self, event):
        """Reset simulation"""
        self.running = False
        self.time = 0
        self.actuator.T = 25
        self.actuator.power = 0
        self.slider_power.set_val(0)
        self.t_history.clear()
        self.temp_history.clear()
        self.disp_history.clear()
        self.btn_toggle.label.set_text('Start')
        self.btn_toggle.color = '#27ae60'
        
    def animate(self, frame):
        """Animation update function"""
        if self.running:
            # Update physics
            dt = 0.05  # 50ms time step
            self.actuator.update_temperature(dt)
            self.time += dt
            
            # Store history
            self.t_history.append(self.time)
            self.temp_history.append(self.actuator.T)
            delta_T = self.actuator.T - self.actuator.T_ambient
            disp = self.actuator.compute_displacement(delta_T) * 1e6  # to µm
            self.disp_history.append(disp)
            
            # Keep last 100 points
            if len(self.t_history) > 100:
                self.t_history.pop(0)
                self.temp_history.pop(0)
                self.disp_history.pop(0)
            
            # Update 3D beam
            x, y, z = self.actuator.get_beam_shape()
            self.beam_line.set_data(x, y)
            self.beam_line.set_3d_properties(z)
            
            # Color based on temperature
            temp_norm = (self.actuator.T - 25) / 275
            color_intensity = min(temp_norm, 1.0)
            if color_intensity > 0.5:
                self.beam_line.set_color('#ff3300')
            else:
                self.beam_line.set_color('#ff6b35')
            
            # Update temperature plot
            self.temp_line.set_data(self.t_history, self.temp_history)
            if self.t_history:
                self.ax_time.set_xlim(0, max(10, self.time))
                self.ax_time.set_ylim(20, max(50, max(self.temp_history) + 10))
            
            # Update metrics
            metrics_str = (
                f"━━━━━ MEASUREMENTS ━━━━━\n\n"
                f"Temperature:   {self.actuator.T:6.1f} °C\n"
                f"Displacement:  {disp:6.2f} µm\n"
                f"Bend Angle:    {delta_T * 0.001 * 180/np.pi:6.2f}°\n"
                f"Power:         {self.actuator.power:6.1f} W\n"
                f"Time:          {self.time:6.2f} s\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━━"
            )
            self.metrics_text.set_text(metrics_str)
        
        return self.beam_line, self.temp_line, self.metrics_text
    
    def run(self):
        """Start the simulation"""
        self.anim = FuncAnimation(self.fig, self.animate, interval=50, 
                                   blit=False, cache_frame_data=False)
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.12, top=0.95, hspace=0.3)
        
        # Add info text
        self.fig.text(0.5, 0.95, '3D Thermal Actuator Simulator', 
                      ha='center', fontsize=14, fontweight='bold', color='white')
        self.fig.text(0.5, 0.925, 'Bimorph beam with differential thermal expansion',
                      ha='center', fontsize=10, color='#94a3b8')
        
        plt.show()

if __name__ == '__main__':
    print("="*60)
    print("  3D THERMAL ACTUATOR SIMULATOR")
    print("="*60)
    print("\n📋 Instructions:")
    print("  • Use the 'Power' slider to control heating")
    print("  • Click 'Start' to begin simulation")
    print("  • Click 'Pause' to stop")
    print("  • Click 'Reset' to restart")
    print("  • Drag the 3D plot to rotate the view")
    print("\n💡 Physics:")
    print("  Two materials with different thermal expansion")
    print("  coefficients bend when heated, creating motion.")
    print("\n" + "="*60 + "\n")
    
    simulator = ThermalActuatorSimulator()
    simulator.run()