"""
Dual Damascene Process Simulator
==================================
Comprehensive simulation of copper dual damascene interconnect fabrication
including dielectric etching, barrier deposition, seed layer, electroplating, and CMP.

Physical processes modeled:
- Anisotropic plasma etching (via and trench formation)
- PVD barrier layer deposition (Ta/TaN)
- Copper seed layer deposition
- Electrochemical copper plating with additives
- Chemical-mechanical planarization (CMP)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle
from dataclasses import dataclass
from typing import List, Tuple, Optional
from enum import Enum
import matplotlib.patches as mpatches

OUTPUT_DIR = Path(__file__).resolve().parents[2] / "images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class Material(Enum):
    """Material types in the damascene process"""
    VACUUM = 0
    SILICON = 1
    OXIDE = 2          # SiO2 dielectric (ILD)
    NITRIDE = 3        # Si3N4 etch stop
    BARRIER = 4        # Ta/TaN diffusion barrier
    COPPER_SEED = 5    # Cu seed layer
    COPPER = 6         # Electroplated Cu
    PHOTORESIST = 7


@dataclass
class ProcessParameters:
    """Parameters for damascene process steps"""
    # Geometry
    wafer_width: float = 2.0e-6      # 2 microns width
    wafer_height: float = 1.5e-6     # 1.5 microns total height
    
    # Layer thicknesses
    bottom_oxide: float = 500e-9     # 500 nm bottom ILD
    nitride_etch_stop: float = 50e-9 # 50 nm Si3N4
    top_oxide: float = 500e-9        # 500 nm top ILD
    
    # Feature dimensions
    via_width: float = 150e-9        # 150 nm via
    trench_width: float = 300e-9     # 300 nm trench
    trench_depth: float = 300e-9     # 300 nm trench depth
    
    # Etch parameters
    etch_rate_oxide: float = 100e-9  # 100 nm/s oxide etch rate
    etch_rate_nitride: float = 5e-9  # 5 nm/s nitride (etch stop)
    etch_anisotropy: float = 0.95    # 0-1, higher = more anisotropic
    
    # Barrier deposition (PVD)
    barrier_thickness: float = 10e-9  # 10 nm Ta/TaN barrier
    barrier_step_coverage: float = 0.7 # Step coverage (0-1)
    
    # Seed layer (PVD)
    seed_thickness: float = 50e-9     # 50 nm Cu seed
    seed_step_coverage: float = 0.6   # Step coverage
    
    # Electroplating parameters
    plating_rate_base: float = 50e-9  # 50 nm/s base plating rate
    plating_enhancement: float = 5.0  # Bottom-up fill enhancement
    diffusion_length: float = 100e-9  # Additive diffusion length
    
    # CMP parameters
    cmp_removal_rate: float = 200e-9  # 200 nm/s removal rate
    cmp_selectivity_cu: float = 1.0   # Cu removal rate
    cmp_selectivity_barrier: float = 0.5  # Barrier removal (slower)
    cmp_selectivity_oxide: float = 0.1    # Oxide removal (much slower)
    dishing_factor: float = 0.05      # Cu dishing fraction


class DamasceneWafer:
    """2D cross-section representation of wafer structure"""
    
    def __init__(self, params: ProcessParameters, resolution: int = 500):
        self.params = params
        self.resolution = resolution
        
        # Create 2D grid
        self.dx = params.wafer_width / resolution
        self.dy = params.wafer_height / resolution
        
        # Material grid
        self.materials = np.zeros((resolution, resolution), dtype=int)
        
        # Initialize layer structure
        self._initialize_layers()
        
        # Process state
        self.current_step = "Initial"
        self.time = 0.0
        
    def _initialize_layers(self):
        """Initialize the starting layer stack"""
        y_bottom_oxide = int(self.params.bottom_oxide / self.dy)
        y_nitride = int((self.params.bottom_oxide + self.params.nitride_etch_stop) / self.dy)
        y_top = int((self.params.bottom_oxide + self.params.nitride_etch_stop + 
                     self.params.top_oxide) / self.dy)
        
        # Silicon substrate
        self.materials[0:10, :] = Material.SILICON.value
        
        # Bottom oxide (ILD1)
        self.materials[10:y_bottom_oxide, :] = Material.OXIDE.value
        
        # Nitride etch stop
        self.materials[y_bottom_oxide:y_nitride, :] = Material.NITRIDE.value
        
        # Top oxide (ILD2)
        self.materials[y_nitride:y_top, :] = Material.OXIDE.value
        
    def get_surface_height(self) -> np.ndarray:
        """Get the topography of the wafer surface"""
        surface = np.zeros(self.resolution)
        for i in range(self.resolution):
            # Find highest non-vacuum point
            column = self.materials[:, i]
            non_vacuum = np.where(column != Material.VACUUM.value)[0]
            if len(non_vacuum) > 0:
                surface[i] = non_vacuum[-1] * self.dy
        return surface
    
    def visualize(self, ax=None, title: Optional[str] = None):
        """Visualize the current wafer cross-section"""
        if ax is None:
            fig, ax = plt.subplots(figsize=(12, 6))
        
        # Color map for materials
        colors = {
            Material.VACUUM.value: '#FFFFFF',
            Material.SILICON.value: '#808080',
            Material.OXIDE.value: '#87CEEB',
            Material.NITRIDE.value: '#90EE90',
            Material.BARRIER.value: '#FFD700',
            Material.COPPER_SEED.value: '#FF8C00',
            Material.COPPER.value: '#B87333',
            Material.PHOTORESIST.value: '#FF69B4'
        }
        
        # Create RGB image
        img = np.zeros((self.resolution, self.resolution, 3))
        for material, color in colors.items():
            mask = self.materials == material
            rgb = np.array([int(color[i:i+2], 16)/255 for i in (1, 3, 5)])
            img[mask] = rgb
        
        # Flip vertically for proper display
        img = np.flipud(img)
        
        ax.imshow(img, extent=[0, self.params.wafer_width*1e9, 
                              0, self.params.wafer_height*1e9], 
                 aspect='auto', interpolation='nearest')
        
        ax.set_xlabel('Position (nm)')
        ax.set_ylabel('Height (nm)')
        
        if title:
            ax.set_title(title)
        else:
            ax.set_title(f'{self.current_step} - Time: {self.time:.2f}s')
        
        # Add legend
        patches = [mpatches.Patch(color=colors[m.value], label=m.name) 
                  for m in Material if m.value in np.unique(self.materials)]
        ax.legend(handles=patches, loc='upper right', fontsize=8)
        
        return ax


class PlasmaEtcher:
    """Anisotropic plasma etching simulation"""
    
    def __init__(self, wafer: DamasceneWafer):
        self.wafer = wafer
        self.params = wafer.params
        
    def etch_feature(self, center_x: float, width: float, 
                     target_depth: float, dt: float, 
                     target_material: Material = Material.OXIDE) -> bool:
        """
        Etch a feature (via or trench) with anisotropic profile
        Returns True when target depth reached
        """
        # Convert to grid coordinates
        center_idx = int(center_x / self.wafer.dx)
        width_idx = int(width / self.wafer.dx)
        
        start_x = max(0, center_idx - width_idx // 2)
        end_x = min(self.wafer.resolution, center_idx + width_idx // 2)
        
        # Determine etch rates
        if target_material == Material.OXIDE:
            etch_rate = self.params.etch_rate_oxide
            etch_selectivity = 1.0
        else:
            etch_rate = self.params.etch_rate_nitride
            etch_selectivity = 0.05  # High selectivity to nitride
        
        # Calculate etch depth this timestep
        etch_depth = etch_rate * dt
        etch_pixels = int(etch_depth / self.wafer.dy)
        
        # Apply anisotropic etching
        anisotropy = self.params.etch_anisotropy
        lateral_etch = int(etch_pixels * (1 - anisotropy))
        
        current_depth = 0
        finished = False
        
        for x in range(start_x, end_x):
            # Find surface at this x position
            column = self.wafer.materials[:, x]
            surface_y = np.where(column != Material.VACUUM.value)[0]
            
            if len(surface_y) > 0:
                surface = surface_y[-1]
                
                # Etch downward
                for dy in range(etch_pixels):
                    y = surface - dy
                    if y < 0:
                        break
                    
                    current_material = Material(self.wafer.materials[y, x])
                    
                    # Check if we hit etch stop (nitride)
                    if current_material == Material.NITRIDE:
                        if np.random.random() > etch_selectivity:
                            self.wafer.materials[y, x] = Material.VACUUM.value
                    elif current_material == target_material or current_material == Material.OXIDE:
                        self.wafer.materials[y, x] = Material.VACUUM.value
                        current_depth = max(current_depth, dy * self.wafer.dy)
                
                # Lateral etching (slight)
                if lateral_etch > 0 and surface >= lateral_etch:
                    # Left side
                    if x - lateral_etch >= 0:
                        for dy in range(lateral_etch):
                            y = surface - dy
                            if y >= 0 and self.wafer.materials[y, x-lateral_etch] == target_material.value:
                                self.wafer.materials[y, x-lateral_etch] = Material.VACUUM.value
                    # Right side
                    if x + lateral_etch < self.wafer.resolution:
                        for dy in range(lateral_etch):
                            y = surface - dy
                            if y >= 0 and self.wafer.materials[y, x+lateral_etch] == target_material.value:
                                self.wafer.materials[y, x+lateral_etch] = Material.VACUUM.value
        
        if current_depth >= target_depth * 0.95:  # 95% of target
            finished = True
            
        return finished


class PVDDepositor:
    """Physical Vapor Deposition with step coverage simulation"""
    
    def __init__(self, wafer: DamasceneWafer):
        self.wafer = wafer
        self.params = wafer.params
        
    def deposit_conformal(self, material: Material, thickness: float, 
                         step_coverage: float):
        """
        Deposit a conformal layer with given step coverage
        Step coverage: 1.0 = perfect conformal, 0.0 = line-of-sight only
        """
        target_pixels = int(thickness / self.wafer.dy)
        
        # Process column by column
        for x in range(self.wafer.resolution):
            column = self.wafer.materials[:, x]
            surface_idx = np.where(column != Material.VACUUM.value)[0]
            
            if len(surface_idx) > 0:
                surface = surface_idx[-1]
                
                # Deposit on top surface
                for dy in range(target_pixels):
                    y = surface + dy + 1
                    if y < self.wafer.resolution:
                        self.wafer.materials[y, x] = material.value
                
                # Deposit on sidewalls with reduced thickness
                sidewall_thickness = int(target_pixels * step_coverage)
                
                # Check for features (vias/trenches)
                if surface < self.wafer.resolution - 10:
                    # Look for sidewall transitions
                    if x > 0:
                        left_surface = np.where(self.wafer.materials[:, x-1] != Material.VACUUM.value)[0]
                        if len(left_surface) > 0 and left_surface[-1] > surface:
                            # Deposit on left sidewall
                            for dy in range(min(sidewall_thickness, int(left_surface[-1] - surface))):
                                y = surface + dy
                                if self.wafer.materials[y, x] == Material.VACUUM.value:
                                    self.wafer.materials[y, x] = material.value
                    
                    if x < self.wafer.resolution - 1:
                        right_surface = np.where(self.wafer.materials[:, x+1] != Material.VACUUM.value)[0]
                        if len(right_surface) > 0 and right_surface[-1] > surface:
                            # Deposit on right sidewall
                            for dy in range(min(sidewall_thickness, int(right_surface[-1] - surface))):
                                y = surface + dy
                                if self.wafer.materials[y, x] == Material.VACUUM.value:
                                    self.wafer.materials[y, x] = material.value


class Electroplater:
    """
    Electrochemical copper plating with superconformal filling
    Models bottom-up fill using accelerator/suppressor additives
    """
    
    def __init__(self, wafer: DamasceneWafer):
        self.wafer = wafer
        self.params = wafer.params
        
        # Additive concentration fields
        self.accelerator = np.zeros((wafer.resolution, wafer.resolution))
        self.suppressor = np.ones((wafer.resolution, wafer.resolution))
        
    def plate_step(self, dt: float):
        """
        Perform one timestep of electroplating
        Bottom-up fill achieved through accelerator accumulation
        """
        base_rate = self.params.plating_rate_base
        
        # Update additive concentrations
        self._update_additives(dt)
        
        # Calculate local plating rate
        for x in range(self.wafer.resolution):
            column = self.wafer.materials[:, x]
            
            # Find copper seed surface
            seed_indices = np.where((column == Material.COPPER_SEED.value) | 
                                   (column == Material.COPPER.value))[0]
            
            if len(seed_indices) > 0:
                surface = seed_indices[-1]
                
                # Calculate enhancement factor based on geometry
                # Bottom of features get more accelerator accumulation
                depth_factor = self._calculate_depth_factor(x, surface)
                
                # Local plating rate
                enhancement = 1.0 + self.params.plating_enhancement * depth_factor
                local_rate = base_rate * enhancement * (self.accelerator[surface, x] / 
                                                        self.suppressor[surface, x])
                
                # Deposit copper
                growth_pixels = int(local_rate * dt / self.wafer.dy)
                for dy in range(growth_pixels):
                    y = surface + dy + 1
                    if y < self.wafer.resolution and self.wafer.materials[y, x] == Material.VACUUM.value:
                        self.wafer.materials[y, x] = Material.COPPER.value
    
    def _update_additives(self, dt: float):
        """Update accelerator and suppressor concentrations"""
        # Simplified model: accelerator accumulates in recesses
        for x in range(self.wafer.resolution):
            column = self.wafer.materials[:, x]
            copper_idx = np.where((column == Material.COPPER_SEED.value) | 
                                 (column == Material.COPPER.value))[0]
            
            if len(copper_idx) > 0:
                surface = copper_idx[-1]
                
                # Accelerator accumulates more in confined spaces
                recess_depth = self._calculate_recess_depth(x, surface)
                if recess_depth > 0:
                    self.accelerator[surface, x] += dt * recess_depth / self.params.diffusion_length
                    self.suppressor[surface, x] *= 0.99  # Suppressor depletes slowly
                    
        # Clamp values
        self.accelerator = np.clip(self.accelerator, 0, 10)
        self.suppressor = np.clip(self.suppressor, 0.1, 1)
    
    def _calculate_depth_factor(self, x: int, y: int) -> float:
        """Calculate how deep in a feature this point is"""
        # Look at surrounding heights
        neighborhood = 5
        max_height = y
        
        for dx in range(-neighborhood, neighborhood+1):
            x_check = x + dx
            if 0 <= x_check < self.wafer.resolution:
                column = self.wafer.materials[:, x_check]
                material_idx = np.where(column != Material.VACUUM.value)[0]
                if len(material_idx) > 0:
                    max_height = max(max_height, material_idx[-1])
        
        depth = (max_height - y) * self.wafer.dy
        return min(depth / 200e-9, 1.0)  # Normalize to feature depth
    
    def _calculate_recess_depth(self, x: int, y: int) -> float:
        """Calculate recess depth for additive accumulation"""
        return self._calculate_depth_factor(x, y)


class CMPPolisher:
    """Chemical-Mechanical Planarization simulation"""
    
    def __init__(self, wafer: DamasceneWafer):
        self.wafer = wafer
        self.params = wafer.params
        
    def polish_step(self, dt: float):
        """
        Perform one CMP step
        Models pressure distribution and material selectivity
        """
        # Get surface topography
        surface_heights = self.wafer.get_surface_height()
        
        # Calculate pressure distribution (higher on peaks)
        mean_height = np.mean(surface_heights)
        pressure = np.maximum(surface_heights - mean_height, 0)
        pressure = pressure / (np.max(pressure) + 1e-9)  # Normalize
        
        # Remove material based on pressure and selectivity
        for x in range(self.wafer.resolution):
            column = self.wafer.materials[:, x]
            surface_idx = np.where(column != Material.VACUUM.value)[0]
            
            if len(surface_idx) > 0:
                surface = surface_idx[-1]
                material = Material(self.wafer.materials[surface, x])
                
                # Determine removal rate based on material
                if material == Material.COPPER:
                    selectivity = self.params.cmp_selectivity_cu
                    # Model dishing in wide copper areas
                    width_factor = self._calculate_width_factor(x, surface)
                    selectivity *= (1 + self.params.dishing_factor * width_factor)
                elif material == Material.BARRIER:
                    selectivity = self.params.cmp_selectivity_barrier
                elif material == Material.OXIDE:
                    selectivity = self.params.cmp_selectivity_oxide
                else:
                    selectivity = 0.5
                
                # Calculate removal
                removal_rate = self.params.cmp_removal_rate * selectivity * (1 + pressure[x])
                removal_pixels = int(removal_rate * dt / self.wafer.dy)
                
                # Remove material
                for dy in range(removal_pixels):
                    if surface - dy >= 0:
                        self.wafer.materials[surface - dy, x] = Material.VACUUM.value
    
    def _calculate_width_factor(self, x: int, y: int) -> float:
        """Calculate width of copper line for dishing model"""
        # Count consecutive copper pixels
        width = 1
        
        # Check left
        for dx in range(1, 50):
            if x - dx < 0:
                break
            if self.wafer.materials[y, x-dx] == Material.COPPER.value:
                width += 1
            else:
                break
        
        # Check right
        for dx in range(1, 50):
            if x + dx >= self.wafer.resolution:
                break
            if self.wafer.materials[y, x+dx] == Material.COPPER.value:
                width += 1
            else:
                break
        
        # Normalize (wider lines dish more)
        return min(width / 50.0, 1.0)
    
    def is_planar(self, tolerance: float = 5e-9) -> bool:
        """Check if surface is planar within tolerance"""
        surface_heights = self.wafer.get_surface_height()
        variation = np.max(surface_heights) - np.min(surface_heights)
        return variation < tolerance


class DamasceneProcess:
    """Complete dual damascene process flow"""
    
    def __init__(self, params: ProcessParameters = None):
        if params is None:
            params = ProcessParameters()
        
        self.params = params
        self.wafer = DamasceneWafer(params)
        
        # Process tools
        self.etcher = PlasmaEtcher(self.wafer)
        self.pvd = PVDDepositor(self.wafer)
        self.plater = Electroplater(self.wafer)
        self.cmp = CMPPolisher(self.wafer)
        
        # Process sequence
        self.steps = []
        self.current_step_idx = 0
        
    def run_full_process(self, animation: bool = False):
        """Execute complete damascene process"""
        
        print("Starting Dual Damascene Process Simulation")
        print("=" * 60)
        
        # Define via and trench positions
        via_center = self.params.wafer_width / 2
        trench_center = self.params.wafer_width / 2
        
        steps = [
            ("Initial State", None),
            ("Via Etch", lambda: self._etch_via(via_center)),
            ("Trench Etch", lambda: self._etch_trench(trench_center)),
            ("Barrier Deposition", self._deposit_barrier),
            ("Seed Layer Deposition", self._deposit_seed),
            ("Copper Electroplating", self._electroplate_copper),
            ("CMP Polish", self._perform_cmp),
            ("Final Structure", None)
        ]
        
        if animation:
            return self._animate_process(steps)
        else:
            return self._run_static_process(steps)
    
    def _run_static_process(self, steps):
        """Run process and generate static plots"""
        fig, axes = plt.subplots(2, 4, figsize=(20, 10))
        axes = axes.flatten()
        
        for idx, (step_name, step_func) in enumerate(steps):
            print(f"\nStep {idx+1}: {step_name}")
            self.wafer.current_step = step_name
            
            if step_func is not None:
                step_func()
            
            # Visualize
            self.wafer.visualize(axes[idx], f"Step {idx+1}: {step_name}")
            
        plt.tight_layout()
        return fig
    
    def _etch_via(self, center_x: float):
        """Etch via through top oxide and nitride"""
        print("  Etching via to bottom metal...")
        dt = 0.1  # timestep
        total_time = 0
        max_time = 20.0
        
        while total_time < max_time:
            finished = self.etcher.etch_feature(
                center_x, 
                self.params.via_width,
                self.params.bottom_oxide + self.params.nitride_etch_stop,
                dt,
                Material.OXIDE
            )
            total_time += dt
            self.wafer.time = total_time
            
            if finished:
                print(f"  Via etch completed in {total_time:.2f}s")
                break
    
    def _etch_trench(self, center_x: float):
        """Etch trench in top oxide"""
        print("  Etching trench...")
        dt = 0.1
        total_time = 0
        max_time = 10.0
        
        while total_time < max_time:
            finished = self.etcher.etch_feature(
                center_x,
                self.params.trench_width,
                self.params.trench_depth,
                dt,
                Material.OXIDE
            )
            total_time += dt
            self.wafer.time += total_time
            
            if finished:
                print(f"  Trench etch completed in {total_time:.2f}s")
                break
    
    def _deposit_barrier(self):
        """Deposit Ta/TaN barrier layer"""
        print(f"  Depositing {self.params.barrier_thickness*1e9:.1f}nm barrier layer...")
        self.pvd.deposit_conformal(
            Material.BARRIER,
            self.params.barrier_thickness,
            self.params.barrier_step_coverage
        )
        print("  Barrier deposition complete")
    
    def _deposit_seed(self):
        """Deposit copper seed layer"""
        print(f"  Depositing {self.params.seed_thickness*1e9:.1f}nm Cu seed layer...")
        self.pvd.deposit_conformal(
            Material.COPPER_SEED,
            self.params.seed_thickness,
            self.params.seed_step_coverage
        )
        print("  Seed layer deposition complete")
    
    def _electroplate_copper(self):
        """Electroplate copper to fill features"""
        print("  Electroplating copper (bottom-up fill)...")
        dt = 0.01
        total_time = 0
        max_time = 30.0
        
        while total_time < max_time:
            self.plater.plate_step(dt)
            total_time += dt
            self.wafer.time += dt
            
            # Check if features are filled
            surface = self.wafer.get_surface_height()
            if np.std(surface) < 10e-9:  # Surface becoming flat
                break
        
        print(f"  Electroplating completed in {total_time:.2f}s")
    
    def _perform_cmp(self):
        """Perform CMP to planarize"""
        print("  Performing CMP...")
        dt = 0.05
        total_time = 0
        max_time = 20.0
        
        while total_time < max_time:
            self.cmp.polish_step(dt)
            total_time += dt
            self.wafer.time += dt
            
            if self.cmp.is_planar(tolerance=5e-9):
                print(f"  CMP completed in {total_time:.2f}s - Surface planar")
                break
        
        if total_time >= max_time:
            print(f"  CMP stopped at max time {max_time}s")


# Main execution
if __name__ == "__main__":
    # Create process with default parameters
    params = ProcessParameters()
    process = DamasceneProcess(params)
    
    # Run full process
    print("\n" + "="*60)
    print("DUAL DAMASCENE PROCESS SIMULATOR")
    print("Simulating Cu interconnect fabrication")
    print("="*60)
    
    fig = process.run_full_process(animation=False)
    output_path = OUTPUT_DIR / "damascene_process_complete.png"
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print("\n" + "="*60)
    print("Simulation Complete!")
    print(f"Output saved to: {output_path}")
    print("="*60)
    plt.show()
