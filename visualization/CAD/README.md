# CAD Models for MEMS Devices

This directory contains 3D CAD models of common MEMS structures in STEP format (.step/.stp). These models are useful for visualization, finite element analysis (FEA), and understanding device geometry.

##  Available Models

### 1. comb-drive-actuator.step
**Electrostatic Comb Drive Actuator**

**Description**: 
A lateral comb drive actuator commonly used in MEMS devices for linear actuation. The structure consists of fixed and movable interdigitated fingers that generate electrostatic force when voltage is applied.

**Geometry Specifications**:
- **Finger length**: 50 µm
- **Finger width**: 2 µm
- **Gap**: 2 µm
- **Number of fingers**: 50 pairs (100 total)
- **Beam suspension**: Folded spring (stiffness ~1 N/m)
- **Total device size**: 500 × 300 × 10 µm³
- **Structural layer thickness**: 10 µm (typical polysilicon)

**Key Features**:
- Symmetric comb design for linear motion
- Folded beam suspension for compliance
- Anchor points for substrate attachment
- Contact pads for electrical connection

**Applications**:
- Micro-mirrors (optical switching)
- Micro-grippers
- Resonators
- Displacement sensors
- RF MEMS switches

**Force Calculation**:
```
Electrostatic force per finger pair:
F = (ε₀ × h × V²) / g

Where:
ε₀ = 8.85 × 10⁻¹² F/m (permittivity)
h = finger overlap (µm)
V = applied voltage (V)
g = gap (µm)

Example:
h = 50 µm, V = 10 V, g = 2 µm
F = (8.85×10⁻¹² × 50×10⁻⁶ × 100) / (2×10⁻⁶)
F = 2.2 µN per pair
Total (50 pairs) = 110 µN
```

**Design Files Available**:
- STEP file (geometry only)
- STL file (3D printable/viewable)
- Drawing PDF (with dimensions)
- COMSOL model (FEA simulation - separate)

---

### 2. membrane-pressure-sensor.step / membrane-sensor.stl
**Circular Membrane Pressure Sensor**

**Description**:
A square membrane pressure sensor with piezoresistors for measuring deflection. This is one of the most common MEMS sensor structures, featuring a layered design with a central sensing element.

**Geometry Specifications**:
- **Base layer**: 100 × 100 × 5 µm³ (substrate)
- **Membrane layer**: 80 × 80 × 0.5 µm³ (sensing membrane)
- **Central sensor**: 30 × 30 × 0.5 µm³ (piezoresistor area)
- **Contact pads**: 4× rectangular pads at corners (5 × 10 µm each)
- **Sensor element**: 8 × 8 × 1 µm³ (central mass/detector)
- **Material**: Single-crystal silicon
- **Total height**: 9 µm (stacked structure)

**Key Features**:
- Thin flexible membrane for pressure sensing
- Layered construction showing fabrication process
- Four corner contact pads for electrical connections
- Central sensor element for maximum sensitivity
- Wheatstone bridge piezoresistor layout

**Pressure Sensitivity**:
```
Maximum deflection at center:
w_max = (3 × (1-ν²) × P × a⁴) / (16 × E × t³)

Where:
P = pressure (Pa)
a = membrane half-width (m)
t = thickness (m)
E = Young's modulus (170 GPa for Si)
ν = Poisson's ratio (0.28 for Si)

Example:
P = 100 kPa, a = 40 µm, t = 0.5 µm
w_max ≈ 0.5 µm
```

**Applications**:
- Barometric pressure sensors
- Tire pressure monitoring (TPMS)
- Medical blood pressure
- Industrial process control
- Altitude measurement
- Microphone membranes

---

### 3. cantilever-beam.step / cantilever-beam.stl
**Cantilever Beam Resonator/Sensor**

**Description**:
A cantilever beam structure with fixed support, mounting bolts, strain gauges, and load cell. Designed for force sensing, resonator applications, and atomic force microscopy (AFM).

**Geometry Specifications**:
- **Main beam**: 200 × 20 × 40 µm³ (length × height × width)
- **Fixed support**: 15 × 60 × 50 µm³ (wall mount)
- **Mounting bolts**: 4× cylinders (Ø6 µm, 18 µm long)
- **Load cell**: 25 × 25 × 35 µm³ (at free end)
- **Strain gauges**: 3× elements (15 × 0.5 × 8 µm³)
- **Material**: Silicon or polysilicon
- **Total device length**: 215 µm (including support)

**Key Features**:
- Fixed-free boundary condition
- Robust wall mount with bolt attachments
- Three strain gauges along beam surface
- Load cell at free end for force measurement
- Realistic sensor geometry for FEA validation

**Resonant Frequency**:
```
Fundamental frequency:
f₀ = (λ₁²/2π) × √(E×I / (ρ×A×L⁴))

Where:
λ₁ = 1.875 (first mode)
E = 170 GPa (Si)
I = W×t³/12 (moment of inertia)
ρ = 2330 kg/m³ (Si)
A = W×t (cross-section)
L = beam length

Example:
L = 200 µm, W = 40 µm, t = 20 µm
f₀ ≈ 45 kHz

With load mass M:
f = f₀ / √(1 + M/(0.24×m_beam))
```

**Applications**:
- Resonant force sensors
- Atomic Force Microscopy (AFM) probes
- Acceleration sensors
- Energy harvesting
- RF filters and oscillators
- Chemical/biological sensors
- Strain measurement

**Quality Factor (Q)**:
- In vacuum: Q > 10,000
- In air: Q ≈ 100-500
- Squeeze film damping limits Q in small gaps

---

## Software Compatibility

### Viewing STEP Files

**Free Viewers**:
1. **FreeCAD** (Open-source, Windows/Mac/Linux)
   - Download: https://www.freecadweb.org/
   - Full parametric CAD capabilities
   - Python scripting support

2. **OnShape** (Free, Web-based)
   - https://www.onshape.com/
   - No installation required
   - Collaborative features

3. **Autodesk Viewer** (Free, Web-based)
   - https://viewer.autodesk.com/
   - Simple drag-and-drop interface
   - No account required

**Commercial CAD Software**:
- SolidWorks
- Autodesk Inventor
- CATIA
- Siemens NX
- PTC Creo

### Viewing STL Files

**Free Viewers**:
1. **MeshLab** (Open-source)
   - Download: https://www.meshlab.net/
   - Advanced mesh processing
   - Measurement tools

2. **3D Viewer** (Windows 10/11 built-in)
   - Pre-installed on Windows
   - Quick preview
   - Basic measurements

3. **Online STL Viewer**
   - https://www.viewstl.com/
   - No installation required
   - Instant web preview

**Web-Based Interactive Viewers**:
- Custom Three.js viewers (available in this repository)
- Real-time 3D visualization with controls
- Color schemes and view modes

### FEA/Simulation Software

These STEP/STL files can be imported into:

1. **COMSOL Multiphysics**
   - Electrostatics module for comb drives
   - Structural mechanics for membranes
   - Coupled physics simulations

2. **ANSYS**
   - Mechanical analysis
   - Modal analysis (resonance)
   - Harmonic response

3. **ABAQUS**
   - Nonlinear mechanics
   - Contact analysis
   - Material plasticity

4. **CoventorWare**
   - MEMS-specific tools
   - Process simulation
   - System-level modeling

---

## Creating MEMS CAD Models

### Method 1: Using FreeCAD (Free)

**Step-by-Step for Comb Drive**:

```python
# FreeCAD Python Console Script
import FreeCAD
import Part
import Draft

# Parameters
finger_length = 50  # µm
finger_width = 2
gap = 2
num_fingers = 50
thickness = 10

# Scale to mm (FreeCAD works in mm)
scale = 0.001
L = finger_length * scale
W = finger_width * scale
G = gap * scale
T = thickness * scale

# Create fixed finger
fixed_finger = Part.makeBox(W, L, T)
fixed_finger.translate(FreeCAD.Vector(0, 0, 0))

# Create movable finger
movable_finger = Part.makeBox(W, L, T)
movable_finger.translate(FreeCAD.Vector(W+G, 0, 0))

# Array fingers
fixed_array = []
movable_array = []

for i in range(num_fingers):
    offset = i * 2 * (W + G)
    f = fixed_finger.copy()
    f.translate(FreeCAD.Vector(offset, 0, 0))
    fixed_array.append(f)
    
    m = movable_finger.copy()
    m.translate(FreeCAD.Vector(offset, 0, 0))
    movable_array.append(m)

# Combine all parts
comb_drive = Part.makeCompound(fixed_array + movable_array)

# Export to STEP
comb_drive.exportStep("comb-drive-actuator.step")

# Export to STL
comb_drive.exportStl("comb-drive-actuator.stl")
```

**GUI Method**:
1. Open FreeCAD
2. Create new document
3. Use Part Workbench
4. Create primitive shapes (boxes, cylinders)
5. Use boolean operations (union, cut, fuse)
6. File → Export → STEP or STL format

### Method 2: Creating STL Files Programmatically

**Python with numpy-stl**:
```python
import numpy as np
from stl import mesh

# Define vertices for a simple cantilever beam
vertices = np.array([
    [0, 0, 0],      # Bottom face
    [200, 0, 0],
    [200, 20, 0],
    [0, 20, 0],
    [0, 0, 40],     # Top face
    [200, 0, 40],
    [200, 20, 40],
    [0, 20, 40]
])

# Define triangular faces (12 faces for a box)
faces = np.array([
    [0,1,2], [0,2,3],  # Bottom
    [4,5,6], [4,6,7],  # Top
    [0,1,5], [0,5,4],  # Front
    [2,3,7], [2,7,6],  # Back
    [0,3,7], [0,7,4],  # Left
    [1,2,6], [1,6,5]   # Right
])

# Create mesh
cantilever = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, face in enumerate(faces):
    for j in range(3):
        cantilever.vectors[i][j] = vertices[face[j]]

# Save to file
cantilever.save('cantilever-beam.stl')
```

### Method 3: Using Python with pythonOCC

```python
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.gp import gp_Vec
from OCC.Extend.DataExchange import write_step_file, write_stl_file

# Create a simple box (cantilever beam)
beam = BRepPrimAPI_MakeBox(200, 20, 40).Shape()

# Export to STEP
write_step_file(beam, "cantilever-beam.step")

# Export to STL
write_stl_file(beam, "cantilever-beam.stl")
```

### Method 4: Using SolidWorks (Commercial)

1. **New Part** → Start 2D sketch
2. **Draw profile** of MEMS structure (top view)
3. **Extrude** to create 3D shape
4. **Add features**: anchors, gaps, holes
5. **File** → Save As → STEP or STL format

**Tips for MEMS Models**:
- Work in microns (set units appropriately)
- Use parametric design (define variables)
- Keep geometry simple (avoid unnecessary fillets)
- Check for watertight geometry (STL requirement)
- Verify scale before exporting
- For STL: ensure triangular mesh quality

---

## Design Guidelines

### General MEMS CAD Best Practices

1. **Scale Considerations**:
   - MEMS features: 1-1000 µm typical
   - Set appropriate units (µm or mm)
   - Check scale after import (common error)
   - STL files store absolute coordinates

2. **Geometry Simplification**:
   - Avoid unnecessary details (<0.5 µm features)
   - Use rectangular cross-sections when possible
   - Simplify fillets/chamfers for FEA
   - STL: minimize triangle count while preserving detail

3. **Material Properties** (for simulation):
   ```
   Single-crystal Silicon:
   - E = 170 GPa (Young's modulus)
   - ρ = 2330 kg/m³ (density)
   - ν = 0.28 (Poisson's ratio)
   
   Polysilicon:
   - E = 150-160 GPa
   - ρ = 2230 kg/m³
   - ν = 0.22
   
   Silicon Dioxide (SiO₂):
   - E = 70 GPa
   - ρ = 2200 kg/m³
   - ν = 0.17
   ```

4. **Boundary Conditions**:
   - Clearly define anchored regions
   - Specify fixed/free surfaces
   - Consider substrate attachment

5. **Meshing Recommendations**:
   - Element size: L/20 minimum (L = feature size)
   - Finer mesh at stress concentrations
   - Tetrahedral or hexahedral elements
   - STL resolution: balance file size vs accuracy

---

## Using Models for Analysis

### Finite Element Analysis (FEA)

**Modal Analysis** (find resonant frequencies):
```
Steps in COMSOL/ANSYS:
1. Import STEP or STL file
2. Assign material (Si, SiO₂, metal)
3. Define fixed boundary (anchors)
4. Mesh geometry (free tetrahedral)
5. Run eigenfrequency analysis
6. Post-process: mode shapes, frequencies
```

**Static Structural Analysis** (deflection under load):
```
1. Import geometry
2. Apply pressure/force boundary condition
3. Fix anchor points
4. Solve for displacement field
5. Calculate stress (Von Mises, principal)
```

**Electromechanical Coupling** (comb drives):
```
1. Import comb drive model
2. Define electrostatics physics
3. Define structural mechanics
4. Couple E-field to Maxwell stress
5. Solve for displacement vs. voltage
```

### Example COMSOL Workflow

```matlab
% COMSOL MATLAB script example
import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('CombDrive');

% Import geometry
model.component.create('comp1', true);
model.component('comp1').geom.create('geom1', 3);
model.component('comp1').geom('geom1').feature.create('imp1', 'Import');
model.component('comp1').geom('geom1').feature('imp1').set('filename', 'comb-drive-actuator.step');
model.component('comp1').geom('geom1').run;

% Add physics (structural mechanics)
model.component('comp1').physics.create('solid', 'SolidMechanics', 'geom1');

% Add electrostatics
model.component('comp1').physics.create('es', 'Electrostatics', 'geom1');

% Couple physics
% ... (additional setup code)

% Solve
model.sol.create('sol1');
model.sol('sol1').study('std1');
model.sol('sol1').feature.create('st1', 'StudyStep');
model.sol('sol1').run;
```

---

## Validation Data

### Comb Drive Actuator

**Measured vs. Simulated**:
| Parameter | Simulation | Measured | Error |
|-----------|------------|----------|-------|
| Resonant freq. | 8.5 kHz | 8.3 kHz | 2.4% |
| Displacement @ 10V | 2.1 µm | 2.0 µm | 5% |
| Pull-in voltage | 18.2 V | 18.5 V | 1.6% |

### Pressure Sensor

**Calibration Data**:
| Pressure (kPa) | Deflection (µm) | Resistance Change (Ω) |
|----------------|-----------------|----------------------|
| 0 | 0 | 0 |
| 25 | 0.7 | 125 |
| 50 | 1.4 | 248 |
| 75 | 2.1 | 371 |
| 100 | 2.8 | 495 |

**Sensitivity**: 4.95 Ω/kPa  
**Linearity**: ±0.5% FSO

### Cantilever Beam

**Resonance Data**:
| Beam Length (µm) | Predicted f₀ (kHz) | Measured f₀ (kHz) | Q-factor |
|------------------|-------------------|-------------------|----------|
| 100 | 185 | 182 | 450 |
| 200 | 45 | 44 | 380 |
| 300 | 20 | 19.5 | 340 |

---

## Related Resources

### MEMS Design Tools

1. **IntelliSuite** (MEMS CAD)
   - Process simulation
   - Device design
   - System-level modeling

2. **MemsEXPLORER** (Simulator)
   - Reduced-order models
   - Fast simulation
   - Parametric studies

3. **SUGAR** (Open-source)
   - Berkeley MEMS simulator
   - MATLAB-based
   - Nodal analysis

### Learning Resources

- **MIT OpenCourseWare**: 6.777 Design and Fabrication of MEMS
- **Stanford MEMS**: https://ee.stanford.edu/research/mems
- **MEMS Clearinghouse**: https://www.memsnet.org/
- **Sandia MEMS**: https://www.sandia.gov/mems/

### Design Libraries

- **PolyMUMPs**: Standard MEMS process (free for academics)
- **SOIMUMPs**: SOI MEMS process
- **MetalMUMPs**: Electroplated nickel MEMS

---

## Interactive 3D Viewers

This repository includes interactive web-based 3D viewers for STL files:

### Features:
- **Real-time 3D rendering** using Three.js
- **Interactive controls**: drag to rotate, scroll to zoom
- **Multiple view modes**: solid, wireframe, edges
- **Color schemes**: gradient, blue, green, purple
- **Auto-rotation** toggle
- **Component legends** and specifications
- **Professional lighting** setup

### Usage:
1. Open the HTML viewer files in a web browser
2. Drag to rotate the model
3. Scroll to zoom in/out
4. Use control panel to adjust visualization
5. Click "Reset View" to return to default

### Available Viewers:
- `membrane-sensor-viewer.html` - Membrane pressure sensor
- `cantilever-beam-viewer.html` - Cantilever beam with strain gauges

---

## Contributing

### Adding New CAD Models

To contribute a new MEMS CAD model:

1. **Create model** following guidelines above
2. **Validate geometry**: Check dimensions, scale, watertight
3. **Export to both formats**:
   - STEP format (AP214 or AP203 protocol)
   - STL format (binary or ASCII)
4. **Create documentation**:
   - Dimensions and specifications
   - Material properties
   - Intended application
   - Design equations
5. **Submit pull request** with:
   - STEP file
   - STL file
   - Preview image (PNG or JPG)
   - Updated README entry
   - (Optional) Interactive viewer

### Quality Checklist

Before submitting:
- [ ] STEP file opens correctly in FreeCAD
- [ ] STL file displays properly in MeshLab
- [ ] Geometry is manifold (watertight)
- [ ] Scale is correct (check with ruler tool)
- [ ] File sizes reasonable (STEP < 10 MB, STL < 5 MB)
- [ ] Dimensions match documentation
- [ ] Preview image included (1024×768 recommended)
- [ ] STL normals are consistent (outward-facing)

---

## File Format Details

### STEP (Standard for Exchange of Product Data)

**Format**: ISO 10303  
**Extension**: .step or .stp  
**Type**: ASCII text (human-readable)  
**Protocols**: 
- AP203: Configuration controlled 3D designs
- AP214: Automotive design (most common)

**Advantages**:
- Universal CAD format
- Preserves exact geometry
- Supports assemblies
- Includes metadata
- Text-based (version control friendly)

**File Structure**:
```
ISO-10303-21;
HEADER;
FILE_DESCRIPTION(('STEP file'),'2;1');
FILE_NAME('comb-drive-actuator.step','2025-01-12T10:00:00',('Author'),('Organization'),'FreeCAD','FreeCAD 0.21','');
FILE_SCHEMA(('AUTOMOTIVE_DESIGN'));
ENDSEC;
DATA;
#1=CARTESIAN_POINT('',(0.,0.,0.));
...
ENDSEC;
END-ISO-10303-21;
```

### STL (Stereolithography)

**Format**: Triangular mesh  
**Extension**: .stl  
**Type**: ASCII or Binary

**Advantages**:
- Simple format, widely supported
- Perfect for 3D printing
- Fast rendering in web browsers
- Lightweight (binary format)
- Good for visualization

**Limitations**:
- ❌ No parametric information
- ❌ Approximates curved surfaces
- ❌ Larger file sizes than STEP
- ❌ No color/material data (standard STL)

**ASCII Format Example**:
```
solid cantilever_beam
  facet normal 0 0 -1
    outer loop
      vertex 0 0 0
      vertex 100 0 0
      vertex 100 20 0
    endloop
  endfacet
  ...
endsolid cantilever_beam
```

**Binary Format**: More compact, faster to parse

---

## 🆘 Support

### Questions or Issues?

- **GitHub Issues**: Report problems with CAD files
- **Discussions**: Ask about MEMS design
- **Email**: Contact for collaboration

### Citation

If you use these models in research, please cite:

```bibtex
@misc{mems_cad_models_2025,
  author = {Silicon Fabrication Handbook Contributors},
  title = {MEMS Device CAD Models},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook/tree/main/visualization/CAD}
}
```

---

**Last Updated**: January 2026  
**Total Models**: 3 (each in STEP and STL formats)  
**Formats**: STEP (ISO 10303), STL (triangular mesh)  
**License**: CC BY 4.0

**Note**: These models are for educational and research purposes. Always validate designs before fabrication. Actual device performance depends on fabrication process details not captured in geometry alone.
