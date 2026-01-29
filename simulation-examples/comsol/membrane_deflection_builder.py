"""
COMSOL Membrane Deflection Model Builder
=========================================

This script creates a complete membrane deflection simulation model using
COMSOL Multiphysics Python API (mph library).

Requirements:
    - COMSOL Multiphysics with valid license
    - Python interface for COMSOL (mph library)
    
Installation:
    pip install mph

Usage:
    python membrane_deflection_builder.py
    
Author: Silicon Fabrication Handbook Project
Date: January 2026
"""

import mph
import numpy as np
from pathlib import Path

class MembraneDeflectionModel:
    """
    Builder class for COMSOL membrane deflection simulation model.
    """
    
    def __init__(self, output_path='membrane_deflection.mph'):
        """
        Initialize the model builder.
        
        Args:
            output_path: Path where the .mph file will be saved
        """
        self.output_path = Path(output_path)
        self.client = None
        self.model = None
        
        # Default parameters
        self.params = {
            'r_mem': '500[um]',           # Membrane radius
            't_mem': '2[um]',             # Membrane thickness
            'h_cavity': '10[um]',         # Cavity depth
            'w_support': '50[um]',        # Support width
            'p_applied': '1[kPa]',        # Applied pressure
            'E_si': '170[GPa]',           # Young's modulus
            'nu_si': '0.28',              # Poisson's ratio
            'rho_si': '2329[kg/m^3]',     # Density
            'sigma_residual': '50[MPa]',   # Residual stress
            'T_ambient': '293.15[K]',     # Ambient temperature
        }
        
    def connect(self):
        """Connect to COMSOL server."""
        print("Connecting to COMSOL Multiphysics...")
        self.client = mph.start(cores=4)
        print("Connected successfully!")
        
    def create_model(self):
        """Create new COMSOL model."""
        print("\nCreating new model...")
        self.model = self.client.create('Membrane_Deflection')
        print("Model created: Membrane_Deflection")
        
    def setup_parameters(self):
        """Define global parameters."""
        print("\nSetting up global parameters...")
        
        # Create parameter group
        param = self.model.parameter()
        
        for name, value in self.params.items():
            param.set(name, value)
            print(f"  {name} = {value}")
            
    def create_geometry(self, dimension='2D_axisym'):
        """
        Create model geometry.
        
        Args:
            dimension: '2D_axisym' for axisymmetric, '3D' for full 3D model
        """
        print(f"\nCreating {dimension} geometry...")
        
        if dimension == '2D_axisym':
            self._create_2d_axisymmetric_geometry()
        elif dimension == '3D':
            self._create_3d_geometry()
        else:
            raise ValueError(f"Unknown dimension type: {dimension}")
            
    def _create_2d_axisymmetric_geometry(self):
        """Create 2D axisymmetric geometry."""
        
        # Set up 2D axisymmetric component
        comp = self.model.component().create('comp1', True)
        comp.geom().create('geom1', 2)
        comp.geom('geom1').lengthUnit('um')
        comp.geom('geom1').axisymmetric(True)
        
        geom = comp.geom('geom1')
        
        # Create membrane rectangle
        r1 = geom.create('r1', 'Rectangle')
        r1.set('size', ['r_mem', 't_mem'])
        r1.set('pos', ['0', '0'])
        r1.label('Membrane')
        
        # Create support ring rectangle
        r2 = geom.create('r2', 'Rectangle')
        r2.set('size', ['w_support', 't_mem'])
        r2.set('pos', ['r_mem', '0'])
        r2.label('Support_Ring')
        
        # Form union
        uni = geom.create('uni1', 'Union')
        uni.selection('input').set(['r1', 'r2'])
        
        # Build geometry
        geom.run()
        print("  2D axisymmetric geometry created successfully")
        
    def _create_3d_geometry(self):
        """Create 3D geometry for square membrane."""
        
        comp = self.model.component().create('comp1', True)
        comp.geom().create('geom1', 3)
        comp.geom('geom1').lengthUnit('um')
        
        geom = comp.geom('geom1')
        
        # Create work plane
        wp = geom.create('wp1', 'WorkPlane')
        wp.set('quickplane', 'xy')
        
        # Create square on work plane
        sq = wp.geom().create('sq1', 'Square')
        sq.set('size', '2*r_mem')
        sq.set('pos', ['-r_mem', '-r_mem'])
        
        # Extrude to create 3D membrane
        ext = geom.create('ext1', 'Extrude')
        ext.selection('input').set(['wp1'])
        ext.setIndex('distance', 't_mem', 0)
        
        geom.run()
        print("  3D geometry created successfully")
        
    def add_material(self):
        """Add silicon material."""
        print("\nAdding materials...")
        
        comp = self.model.component('comp1')
        
        # Create material
        mat = comp.material().create('mat1', 'Common')
        mat.label('Silicon')
        
        # Set material properties
        mat.propertyGroup('def').set('density', 'rho_si')
        mat.propertyGroup('def').set('youngsmodulus', 'E_si')
        mat.propertyGroup('def').set('poissonsratio', 'nu_si')
        
        # Assign to all domains
        mat.selection().all()
        
        print("  Silicon material added")
        
    def setup_physics(self):
        """Set up solid mechanics physics."""
        print("\nSetting up physics...")
        
        comp = self.model.component('comp1')
        
        # Add Solid Mechanics physics
        solid = comp.physics().create('solid', 'SolidMechanics', 'geom1')
        solid.label('Solid_Mechanics')
        
        # Linear elastic material (default)
        lemm = solid.feature('lemm1')
        
        # Add initial stress
        inits = lemm.create('inits1', 'InitialStressandStrain', 2)
        inits.selection().all()
        inits.set('Sil', [['sigma_residual', '0', '0'],
                          ['0', 'sigma_residual', '0'],
                          ['0', '0', '0']])
        inits.label('Residual_Stress')
        
        # Fixed constraint at outer edge
        fix = solid.create('fix1', 'Fixed', 1)
        # Select outer boundary (manual selection required in GUI)
        fix.label('Fixed_Support')
        
        # Boundary load (pressure)
        bndl = solid.create('bndl1', 'BoundaryLoad', 1)
        # Select bottom surface (manual selection required in GUI)
        bndl.set('LoadType', 'Pressure')
        bndl.set('Pressure', 'p_applied')
        bndl.label('Applied_Pressure')
        
        print("  Solid mechanics physics configured")
        
    def create_mesh(self):
        """Create mesh."""
        print("\nCreating mesh...")
        
        comp = self.model.component('comp1')
        mesh = comp.mesh().create('mesh1')
        
        # Set element size
        size = mesh.create('size1', 'Size')
        size.selection().geom('geom1', 2)
        size.selection().all()
        size.set('hauto', 1)  # Extra fine
        size.set('custom', 'on')
        size.set('hmax', 't_mem/4')
        size.set('hmin', 't_mem/10')
        
        # Build mesh
        mesh.run()
        print("  Mesh created successfully")
        
    def add_study(self, study_type='stationary'):
        """
        Add study.
        
        Args:
            study_type: 'stationary', 'parametric', or 'eigenfrequency'
        """
        print(f"\nAdding {study_type} study...")
        
        if study_type == 'stationary':
            self._add_stationary_study()
        elif study_type == 'parametric':
            self._add_parametric_study()
        elif study_type == 'eigenfrequency':
            self._add_eigenfrequency_study()
        else:
            raise ValueError(f"Unknown study type: {study_type}")
            
    def _add_stationary_study(self):
        """Add stationary study."""
        std = self.model.study().create('std1')
        std.label('Stationary_Study')
        
        step = std.create('stat', 'Stationary')
        step.label('Stationary')
        
        print("  Stationary study added")
        
    def _add_parametric_study(self):
        """Add parametric sweep study."""
        std = self.model.study().create('std1')
        std.label('Parametric_Study')
        
        step = std.create('stat', 'Stationary')
        step.label('Stationary')
        
        # Add parametric sweep
        param = std.create('param', 'Parametric')
        param.setIndex('pname', 'p_applied', 0)
        param.setIndex('plistarr', 'range(0,1[kPa],10[kPa])', 0)
        param.label('Pressure_Sweep')
        
        print("  Parametric study added")
        
    def _add_eigenfrequency_study(self):
        """Add eigenfrequency study."""
        std = self.model.study().create('std1')
        std.label('Eigenfrequency_Study')
        
        step = std.create('eig', 'Eigenfrequency')
        step.set('neigs', 6)
        step.set('shift', '10[kHz]')
        step.label('Eigenfrequency')
        
        print("  Eigenfrequency study added")
        
    def add_results(self):
        """Add result plots."""
        print("\nAdding result plots...")
        
        # 3D displacement plot
        plot3d = self.model.result().create('pg1', 'PlotGroup3D')
        plot3d.label('Displacement')
        plot3d.set('data', 'dset1')
        
        surf = plot3d.create('surf1', 'Surface')
        surf.set('expr', 'solid.disp')
        surf.set('unit', 'um')
        surf.set('descr', 'Total displacement')
        
        # Deformation
        surf.set('resolution', 'normal')
        
        # Stress plot
        plot3d_stress = self.model.result().create('pg2', 'PlotGroup3D')
        plot3d_stress.label('von_Mises_Stress')
        
        surf_stress = plot3d_stress.create('surf1', 'Surface')
        surf_stress.set('expr', 'solid.mises')
        surf_stress.set('unit', 'MPa')
        surf_stress.set('descr', 'von Mises stress')
        
        print("  Result plots configured")
        
    def solve(self):
        """Run the simulation."""
        print("\nSolving...")
        print("This may take several minutes...")
        
        self.model.study('std1').run()
        
        print("  Solution completed successfully!")
        
    def export_results(self, export_dir='results'):
        """
        Export results to files.
        
        Args:
            export_dir: Directory to save exported results
        """
        print(f"\nExporting results to {export_dir}/...")
        
        export_path = Path(export_dir)
        export_path.mkdir(exist_ok=True)
        
        # Export displacement data
        # Note: Actual export commands depend on COMSOL API version
        
        print("  Results exported")
        
    def save_model(self):
        """Save the COMSOL model."""
        print(f"\nSaving model to {self.output_path}...")
        
        self.model.save(str(self.output_path))
        
        print(f"  Model saved successfully: {self.output_path}")
        
    def disconnect(self):
        """Disconnect from COMSOL server."""
        if self.client:
            print("\nDisconnecting from COMSOL...")
            self.client.disconnect()
            print("Disconnected")
            
    def build_complete_model(self, dimension='2D_axisym', study_type='stationary',
                            solve=False):
        """
        Build complete model from start to finish.
        
        Args:
            dimension: '2D_axisym' or '3D'
            study_type: 'stationary', 'parametric', or 'eigenfrequency'
            solve: Whether to solve after building
        """
        try:
            self.connect()
            self.create_model()
            self.setup_parameters()
            self.create_geometry(dimension=dimension)
            self.add_material()
            self.setup_physics()
            self.create_mesh()
            self.add_study(study_type=study_type)
            self.add_results()
            
            if solve:
                self.solve()
                
            self.save_model()
            
            print("\n" + "="*60)
            print("Model building completed successfully!")
            print("="*60)
            
        except Exception as e:
            print(f"\nError occurred: {str(e)}")
            raise
        finally:
            self.disconnect()


def main():
    """Main execution function."""
    
    print("="*60)
    print("COMSOL Membrane Deflection Model Builder")
    print("="*60)
    
    # Create model builder
    builder = MembraneDeflectionModel(
        output_path='membrane_deflection.mph'
    )
    
    # Customize parameters if needed
    builder.params['r_mem'] = '500[um]'
    builder.params['t_mem'] = '2[um]'
    builder.params['p_applied'] = '1[kPa]'
    
    # Build complete model
    builder.build_complete_model(
        dimension='2D_axisym',      # or '3D'
        study_type='stationary',     # or 'parametric' or 'eigenfrequency'
        solve=False                  # Set to True to solve immediately
    )
    
    print("\nNext steps:")
    print("1. Open the .mph file in COMSOL Multiphysics")
    print("2. Review and adjust boundary condition selections")
    print("3. Run the study")
    print("4. Analyze results")
    

if __name__ == '__main__':
    main()