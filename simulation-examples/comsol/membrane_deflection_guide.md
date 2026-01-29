# COMSOL Membrane Deflection Simulation Guide

## Overview
This guide provides detailed instructions for creating a membrane deflection simulation in COMSOL Multiphysics for MEMS applications, particularly for pressure sensors and microphones.

## Model Information
- **Physics**: Solid Mechanics (Structural Mechanics Module)
- **Dimension**: 3D or 2D Axisymmetric
- **Study Type**: Stationary, Parametric Sweep, Eigenfrequency

## Geometry Parameters

### Membrane Specifications
```
Parameter Name          Value           Unit        Description
---------------------------------------------------------------------------
membrane_radius         500             μm          Radius of circular membrane
membrane_thickness      2               μm          Silicon membrane thickness
cavity_depth            10              μm          Depth of cavity below membrane
support_width           50              μm          Width of support ring
```

### Applied Loads
```
Parameter Name          Value Range     Unit        Description
---------------------------------------------------------------------------
applied_pressure        0-10            kPa         Differential pressure
temperature_change      -40 to 125      °C          Operating temperature range
residual_stress         10-100          MPa         Process-induced stress
```

## Step-by-Step Model Creation

### 1. Model Wizard Setup

1. **Open COMSOL Multiphysics**
2. **Model Wizard**:
   - Space Dimension: **2D Axisymmetric** (for circular membrane) or **3D** (for complex geometries)
   - Physics: Select **Structural Mechanics → Solid Mechanics (solid)**
   - Study: **Stationary**

### 2. Global Definitions - Parameters

Create a parameter table with the following definitions:

```
Name                Value               Description
------------------------------------------------------------------------
r_mem               500[um]             Membrane radius
t_mem               2[um]               Membrane thickness
h_cavity            10[um]              Cavity depth
w_support           50[um]              Support width
p_applied           1[kPa]              Applied pressure
E_si                170[GPa]            Young's modulus of silicon
nu_si               0.28                Poisson's ratio of silicon
rho_si              2329[kg/m^3]        Density of silicon
sigma_residual      50[MPa]             Residual stress
```

### 3. Geometry Construction

#### For 2D Axisymmetric Model:

**Step 3.1: Create Membrane Cross-Section**
```
Geometry 1 → Rectangle
- Width: r_mem
- Height: t_mem
- Base: Corner
- Position: r = 0, z = 0
```

**Step 3.2: Create Support Ring**
```
Geometry 1 → Rectangle
- Width: w_support
- Height: t_mem
- Base: Corner
- Position: r = r_mem, z = 0
```

**Step 3.3: Create Cavity (Optional for visualization)**
```
Geometry 1 → Rectangle
- Width: r_mem
- Height: -h_cavity
- Base: Corner
- Position: r = 0, z = -h_cavity
```

**Step 3.4: Form Union**
- Select all rectangles
- Right-click → Form Union

#### For 3D Model:

**Alternative Geometry for Square Membrane:**
```
Geometry 1 → Work Plane 1
- Create square: side length = 2*r_mem
- Extrude: distance = t_mem
```

### 4. Materials

**Material 1: Single Crystal Silicon**

Navigate to: **Materials → Add Material → Built-in → Silicon**

Or define manually:
```
Property                    Value                   Unit
------------------------------------------------------------------------
Young's modulus (E)         170e9                   Pa
Poisson's ratio (nu)        0.28                    -
Density (rho)              2329                    kg/m³
Thermal expansion (alpha)   2.6e-6                  1/K
```

**For [100] orientation:**
- E₁ = 130 GPa
- E₂ = 130 GPa  
- E₃ = 170 GPa (perpendicular to wafer)

**Assign Material:**
- Select membrane domain
- Right-click → Material → Silicon

### 5. Solid Mechanics Physics Setup

#### 5.1 Linear Elastic Material
- Automatically applied with material selection
- Verify constitutive relation: Linear elastic

#### 5.2 Initial Stress (Residual Stress)
```
Physics → Solid Mechanics → Linear Elastic Material 1
- Initial stress and strain: **User defined**
- Initial stress (S₀):
  - S₀ᵣᵣ = sigma_residual
  - S₀ₜₜ = sigma_residual
  - S₀ᵣz = 0
```

#### 5.3 Boundary Conditions

**Fixed Constraint (Outer Edge):**
```
Physics → Solid Mechanics → Fixed Constraint
- Selection: Outer edge of support ring (r = r_mem + w_support)
- Constraints: All DOF fixed (u = 0)
```

**Symmetry (Center Axis for 2D Axisymmetric):**
```
Physics → Solid Mechanics → Axial Symmetry
- Selection: r = 0 boundary
- Automatically applied
```

#### 5.4 Loads

**Boundary Load (Pressure):**
```
Physics → Solid Mechanics → Boundary Load
- Selection: Bottom surface of membrane
- Load type: Pressure
- Pressure: p_applied
```

### 6. Mesh

#### 6.1 Mesh Settings
```
Mesh 1 → Size: **Extra Fine**
- Maximum element size: t_mem/4
- Minimum element size: t_mem/10
- Maximum element growth rate: 1.3
- Curvature factor: 0.3
```

#### 6.2 Mesh Refinement (Critical Areas)
```
Mesh 1 → Edge Refinement
- Selection: Edges at membrane-support interface
- Number of elements: 20
```

#### 6.3 Build Mesh
- Click **Build All**
- Verify mesh quality (check for no inverted elements)

### 7. Study Configuration

#### 7.1 Stationary Study
```
Study 1 → Step 1: Stationary
- Physics selection: Solid Mechanics
- Values of dependent variables: User controlled
```

#### 7.2 Parametric Sweep (Optional)
```
Study 1 → Parametric Sweep
- Parameter name: p_applied
- Parameter values: range(0, 1[kPa], 10[kPa])
```

#### 7.3 Eigenfrequency Study (for Resonance Analysis)
```
Add Study → Preset Studies for Selected Physics Interfaces
- Eigenfrequency
- Search for eigenfrequencies around: 10[kHz]
- Desired number of eigenfrequencies: 6
```

### 8. Solver Configuration

```
Study 1 → Solver Configurations → Solution 1
- Solver: Stationary
- Linear solver: Direct (MUMPS or PARDISO)
- Relative tolerance: 1e-6
```

### 9. Compute Solution

Click **Compute** button (=) or press F8

### 10. Results and Post-Processing

#### 10.1 3D Displacement Plot
```
Results → 3D Plot Group
- Surface: solid.disp (Total displacement)
- Deformation: Displacement field (solid)
- Scale factor: 1 (or auto)
- Color scale: Rainbow
```

#### 10.2 1D Plot - Center Deflection
```
Results → 1D Plot Group
- Line Graph
- Selection: r = 0, z = 0 to z = t_mem
- Expression: solid.uz (or w in 2D axisymmetric)
- x-axis data: Arc length
```

#### 10.3 Maximum Deflection Evaluation
```
Results → Derived Values → Global Evaluation
- Expression: minop1(solid.disp)
- Description: Maximum deflection
```

#### 10.4 Stress Analysis
```
Results → 3D Plot Group
- Surface: solid.mises (von Mises stress)
- Evaluate to identify maximum stress location
```

## Key Output Parameters

### Analytical Solution Comparison

For a circular membrane with uniform pressure:

**Maximum deflection at center (small deflection theory):**
```
w_max = (3(1-ν²)pr⁴)/(16Et³)
```

Where:
- p = applied pressure
- r = membrane radius
- E = Young's modulus
- t = membrane thickness
- ν = Poisson's ratio

**First resonant frequency (fundamental mode):**
```
f₁ = (10.21/(2πr²)) × √(Et²/(12ρ(1-ν²)))
```

### Expected Results (Example)

For the default parameters:
- Applied pressure: 1 kPa
- Membrane radius: 500 μm
- Thickness: 2 μm

**Predicted Values:**
- Maximum deflection: ~1.5 μm
- Maximum stress: ~25 MPa
- First resonant frequency: ~45 kHz
- Safety factor: ~4.4 (assuming yield stress ~110 MPa)

## Advanced Features

### 1. Nonlinear Geometry (Large Deflections)

When deflection > thickness/2:

```
Study Settings → Study Extensions
- Include geometric nonlinearity: ON
```

### 2. Prestress Analysis

```
Study 1 → Step 1: Prestress (Eigenfrequency)
Study 1 → Step 2: Eigenfrequency
- Use solution from: Step 1
```

### 3. Coupled Multiphysics

#### Electromechanical Coupling (Capacitive Sensing):
```
Add Physics → Electrostatics (es)
- Define electrode boundaries
- Add Multiphysics → Electromechanical Force
```

#### Thermal Effects:
```
Add Physics → Heat Transfer in Solids (ht)
- Thermal expansion coupling
- Temperature-dependent material properties
```

### 4. Parametric Optimization

```
Study → Optimization
- Objective function: Minimize maximum stress
- Design variable: membrane_thickness
- Constraints: w_max < 2[um]
```

## Validation and Verification

### Mesh Independence Study
1. Create multiple mesh densities
2. Compare maximum deflection values
3. Ensure < 1% difference between finest meshes

### Analytical Comparison
1. Compare COMSOL results with analytical solution
2. Expected agreement within 5% for small deflections
3. Larger differences expected for large deflections (geometric nonlinearity)

### Symmetry Check
- Verify symmetric stress distribution
- Check for numerical artifacts

## Export Results

### Data Export
```
Results → Export → Data
- Filename: membrane_deflection_data.txt
- Data format: Spreadsheet
```

### Image Export
```
Results → Export → Image
- Filename: membrane_deflection.png
- Resolution: 600 dpi
- Include: Color legend, axis labels
```

### Report Generation
```
File → Report → Automatic
- Include: Geometry, mesh, results plots
```

## Troubleshooting

### Common Issues

**1. Mesh Failed**
- Reduce maximum element size
- Repair geometry (check for small gaps)
- Simplify geometry

**2. Solver Did Not Converge**
- Check material properties (positive definite)
- Verify boundary conditions
- Enable geometric nonlinearity for large deflections
- Reduce applied load and use continuation

**3. Unexpected Results**
- Verify units consistency
- Check boundary condition assignments
- Review material orientation (anisotropic materials)

**4. Large Memory Usage**
- Use 2D axisymmetric instead of 3D
- Coarsen mesh in non-critical regions
- Use iterative solver instead of direct solver

## Best Practices

1. **Always start simple**: Begin with linear analysis before adding complexity
2. **Verify mesh quality**: Target element quality > 0.3
3. **Use parametric studies**: Understand sensitivity to design parameters
4. **Document assumptions**: Material properties, boundary conditions, loads
5. **Compare with theory**: Validate against analytical solutions when available
6. **Check stress concentrations**: Refine mesh at critical locations
7. **Consider manufacturing**: Include realistic residual stress values

## References

1. Timoshenko, S., & Woinowsky-Krieger, S. (1959). Theory of Plates and Shells
2. COMSOL Multiphysics Structural Mechanics Module User's Guide
3. Senturia, S. D. (2001). Microsystem Design
4. Madou, M. J. (2011). Fundamentals of Microfabrication and Nanotechnology

## File Naming Convention

Save your COMSOL model as:
```
membrane_deflection_[diameter]um_[thickness]um_[date].mph
```

Example: `membrane_deflection_1000um_2um_20260129.mph`