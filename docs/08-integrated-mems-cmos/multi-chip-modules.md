# Multi-Chip Modules for MEMS-CMOS Integration

## Table of Contents
1. [Introduction](#introduction)
2. [MCM Technologies](#mcm-technologies)
3. [Substrate Technologies](#substrate-technologies)
4. [Interconnection Methods](#interconnection-methods)
5. [Thermal Management](#thermal-management)
6. [Design Considerations](#design-considerations)
7. [Assembly Processes](#assembly-processes)
8. [Testing and Reliability](#testing-and-reliability)
9. [Applications](#applications)
10. [Cost Analysis](#cost-analysis)

## Introduction

### What is a Multi-Chip Module?

A Multi-Chip Module (MCM) is a packaging technology that integrates multiple semiconductor dies (chips) onto a common substrate to form a single functional unit. For MEMS-CMOS integration, MCMs offer a practical alternative to monolithic integration, allowing:

- **Heterogeneous integration** of different process technologies
- **Optimization** of each die independently
- **Higher yield** than monolithic approaches
- **Flexibility** in component sourcing
- **Rapid prototyping** and iteration

### Why MCMs for MEMS-CMOS?

**Advantages**:
1. **Process independence**: MEMS and CMOS fabricated separately using optimal processes
2. **Yield optimization**: Known-good-die (KGD) testing before assembly
3. **Design flexibility**: Mix-and-match components from different vendors
4. **Cost-effective**: No need for expensive merged process development
5. **Performance**: Short interconnects between dies (reduced parasitics)
6. **Scalability**: Easy to add or remove functionality

**Challenges**:
1. **Size**: Typically larger than monolithic solutions
2. **Cost**: Additional packaging complexity
3. **Parasitics**: Inter-die connections introduce capacitance/inductance
4. **Testing**: Requires die-level and module-level testing
5. **Thermal**: Heat dissipation from multiple dies

### MCM vs. Other Integration Approaches

| Approach | Size | Cost | Yield | Flexibility | Performance |
|----------|------|------|-------|-------------|-------------|
| Monolithic | Smallest | High NRE | Lower | Low | Best |
| MCM | Medium | Medium | Higher | High | Good |
| System-in-Package | Larger | Lower | Highest | Highest | Fair |
| PCB Assembly | Largest | Lowest | Highest | Highest | Lowest |

## MCM Technologies

### MCM-L (Laminate)

Uses organic laminate substrates similar to high-end PCBs.

**Characteristics**:
- **Substrate**: FR-4, BT resin, polyimide
- **Minimum line width**: 25-50 μm
- **Dielectric constant**: 3.5-4.5
- **Layer count**: 4-20 layers
- **Cost**: Lowest MCM option

**Structure**:
```
Die #1        Die #2        Die #3
  |             |             |
  └─────────────┴─────────────┘
         Copper traces
    ──────────────────────────
        Laminate layer 1
    ──────────────────────────
         Ground plane
    ──────────────────────────
        Laminate layer 2
    ──────────────────────────
         Signal layer
    ──────────────────────────
```

**Process Flow**:
1. Laminate base substrate fabrication
2. Via formation (laser drilling)
3. Copper plating
4. Photolithography and etching
5. Dielectric layer deposition
6. Repeat for multiple layers
7. Surface finish (ENIG, OSP)
8. Die attach and wire bonding

**Applications**:
- Consumer electronics (smartphones, tablets)
- Cost-sensitive applications
- Moderate frequency (<5 GHz)
- Large volume production

### MCM-C (Ceramic)

Uses ceramic substrates (alumina, AlN, LTCC).

**Characteristics**:
- **Substrate**: Al₂O₃ (96-99.6%), AlN, LTCC
- **Minimum line width**: 50-100 μm
- **Dielectric constant**: 8-10 (alumina), 9 (AlN)
- **Thermal conductivity**: 24 W/m·K (alumina), 170 W/m·K (AlN)
- **Cost**: Medium

**LTCC Process** (Low-Temperature Co-fired Ceramic):
1. Green tape casting
2. Via punching or laser drilling
3. Via filling with conductive paste
4. Screen printing of conductor patterns
5. Tape stacking and lamination
6. Co-firing at 850-900°C
7. Surface metallization

**Advantages**:
- Excellent thermal conductivity (especially AlN)
- Hermetic packages possible
- High reliability
- Good RF performance
- Compatible with high-temperature processes

**Disadvantages**:
- Coarser feature sizes than MCM-D
- Higher cost than MCM-L
- Less flexible routing

**Applications**:
- Military/aerospace
- High-power electronics
- RF/microwave modules
- Harsh environments

### MCM-D (Deposited)

Uses thin-film deposition on silicon or ceramic substrates.

**Characteristics**:
- **Substrate**: Silicon, glass, ceramic
- **Minimum line width**: 2-10 μm
- **Dielectric**: Polyimide, BCB, SiO₂
- **Metal**: Cu, Al (thin-film processes)
- **Cost**: Highest

**Process Flow**:
1. Substrate preparation (Si wafer)
2. Dielectric deposition (spin-on polyimide)
3. Via patterning and etching
4. Metal sputtering (Ti/Cu seed layer)
5. Photolithography
6. Electroplating (Cu)
7. Metal etch and CMP
8. Repeat for multiple layers (4-8 typical)
9. Final passivation

**Thin-Film Stack Example**:
```
    Passivation (SiN)
    ─────────────────
    Metal 4 (Cu, 2 μm)
    ─────────────────
    Polyimide (10 μm)
    ─────────────────
    Metal 3 (Cu, 2 μm)
    ─────────────────
    BCB (8 μm)
    ─────────────────
    Metal 2 (Cu, 3 μm)
    ─────────────────
    Polyimide (12 μm)
    ─────────────────
    Metal 1 (Cu, 5 μm)
    ─────────────────
    Ti/W barrier
    ─────────────────
    Si substrate
```

**Advantages**:
- Fine-pitch interconnects
- Excellent electrical performance
- High routing density
- Controlled impedance
- Compatible with silicon processes

**Disadvantages**:
- Highest cost
- Longer development time
- Lower thermal conductivity (polyimide)
- Limited to smaller substrates

**Applications**:
- High-performance computing
- Advanced RF systems
- High-density interconnect requirements
- Prototype and low-volume production

### MCM-D/C Hybrid

Combines thin-film processes (MCM-D) with ceramic substrates (MCM-C).

**Features**:
- Fine-pitch interconnects on surface layers
- Ceramic base for thermal management
- Best of both technologies
- Used in high-performance RF modules

## Substrate Technologies

### Silicon Substrate

**Properties**:
- **Thermal conductivity**: 150 W/m·K
- **CTE**: 2.6 ppm/°C (excellent match to dies)
- **Dielectric constant**: 11.7
- **Resistivity**: 0.001-10,000 Ω·cm (controllable)

**Advantages**:
- CTE match eliminates thermal stress
- Can be processed like semiconductor wafer
- High routing density possible
- Flat, smooth surface

**Disadvantages**:
- Electrically conductive (needs isolation)
- Brittle
- Expensive for large substrates

**Usage**: High-performance MCMs, RF applications, stacked die packages

### Organic Substrates

#### Build-Up Substrates

**Structure**:
```
Surface layer (fine pitch, 10-25 μm)
    Buildup Layer 2 (Cu + resin)
    Buildup Layer 1 (Cu + resin)
    ──────────────────────────
         Core (FR-4, BT)
    ──────────────────────────
    Buildup Layer 1 (Cu + resin)
    Buildup Layer 2 (Cu + resin)
Bottom layer
```

**Materials**:
- **Core**: FR-4, BT resin, glass-reinforced materials
- **Buildup**: ABF (Ajinomoto Build-up Film), photo-definable resins
- **Conductor**: Electroplated copper

**Process**:
1. Core laminate with through-holes
2. Laminate buildup layers (sequential)
3. Laser via drilling
4. Desmear and copper plating
5. Pattern plating or semi-additive process
6. Solder mask application

**Applications**: Flip-chip BGA, high-density MCMs, mobile devices

#### Flex and Rigid-Flex

**Features**:
- Polyimide base (25-125 μm)
- Can bend and fold
- 3D package configurations
- Reduced weight and volume

**MEMS-CMOS Application**:
- Wearable sensors
- Implantable devices
- Space-constrained systems

### Glass Substrate

**Properties**:
- **CTE**: 3-9 ppm/°C (depends on type)
- **Dielectric constant**: 4-7
- **Loss tangent**: 0.002-0.01
- **Cost**: Medium

**Advantages**:
- Excellent electrical insulation
- Low RF loss
- Flat, smooth surface
- Transparent (optical integration)

**Process Technologies**:
- Through-glass vias (TGV)
- Thin-film metallization
- High-density interconnects

**Applications**:
- RF/mmWave modules
- MEMS timing devices
- Image sensors
- Display integration

## Interconnection Methods

### Wire Bonding in MCMs

**Gold Wire Bonding**:
- **Wire diameter**: 15-25 μm (fine pitch), 25-50 μm (standard)
- **Pitch**: 40-60 μm (minimum achievable)
- **Loop height**: 100-300 μm
- **Bonding force**: 30-80 gf
- **Temperature**: 150-250°C

**Process Steps**:
1. Die attach (die bonding)
2. Wire bonding (ball-wedge or wedge-wedge)
3. Loop formation
4. Encapsulation (optional)

**Parasitics**:
- **Inductance**: 1-3 nH per mm of wire length
- **Capacitance**: 0.1-0.5 pF per bond
- **Resistance**: 0.1-0.3 Ω for 25 μm Au wire, 25 mm length

**Calculation Example**:
```
Wire length L = 2 mm
Loop height h = 200 μm

Inductance:
L_wire ≈ 2h × ln(2h/r) × 10⁻³ μH
      ≈ 2×0.2 × ln(2×0.2/0.0125) × 10⁻³
      ≈ 2.2 nH
```

### Flip-Chip Interconnection

**Bump Technologies**:

1. **Solder Bumps** (C4 - Controlled Collapse Chip Connection):
   - Composition: SnPb (63/37), SAC305 (Sn96.5/Ag3.0/Cu0.5)
   - Bump height: 50-100 μm
   - Pitch: 100-250 μm
   - Reflow temperature: 220-260°C

2. **Copper Pillar Bumps**:
   - Structure: Cu pillar (30-50 μm) + SnAg cap (10-20 μm)
   - Pitch: 40-150 μm
   - Better electromigration resistance
   - Finer pitch capability

3. **Gold Stud Bumps**:
   - Height: 10-25 μm
   - Pitch: 30-80 μm
   - Used for ultrafine pitch
   - No reflow required

**Underfill**:
- **Material**: Epoxy resin with silica filler
- **CTE**: 25-35 ppm/°C
- **Glass transition**: 120-150°C
- **Purpose**: Mechanical support, stress redistribution

**Process Flow**:
```
1. Die preparation
   ├── Wafer bumping (UBM + bump formation)
   └── Wafer dicing

2. Substrate preparation
   ├── Solder paste printing (optional)
   └── Flux application

3. Flip-chip placement
   ├── Die pickup
   ├── Alignment (±5-10 μm)
   └── Die placement

4. Reflow soldering
   ├── Pre-heat (150°C)
   ├── Reflow (220-260°C, 60-90s)
   └── Cooling

5. Underfill dispensing
   ├── Dispense along die edge
   ├── Capillary flow
   └── Cure (150°C, 30-60 min)
```

**Electrical Performance**:
- **Inductance**: 0.1-0.5 nH (very low!)
- **Capacitance**: 0.01-0.05 pF
- **Resistance**: 10-50 mΩ

### Through-Silicon Via (TSV)

For 3D-stacked MCMs, TSVs provide vertical interconnections through silicon dies.

**TSV Specifications**:
- **Diameter**: 5-50 μm
- **Depth**: 50-300 μm
- **Aspect ratio**: 5:1 to 20:1
- **Pitch**: 10-100 μm
- **Liner**: SiO₂ or Si₃N₄ (0.2-1 μm)
- **Barrier**: Ta/TaN (50-200 nm)
- **Fill**: Cu (electroplated)

**Fabrication Process**:

**Via-First** (before transistors):
1. TSV etching (DRIE)
2. Liner deposition (PECVD oxide)
3. Barrier deposition (PVD Ta)
4. Seed layer (PVD Cu)
5. Cu electroplating
6. CMP planarization
7. Standard CMOS processing

**Via-Last** (after BEOL):
1. CMOS fabrication complete
2. TSV etching from backside
3. Isolation and barrier
4. Cu filling
5. Wafer thinning
6. Reveal and expose TSVs

**Parasitics**:
```
Resistance:
R_TSV = ρ_Cu × L / A
      = 1.7×10⁻⁸ × 100×10⁻⁶ / (π × (5×10⁻⁶)²)
      = 21.7 mΩ

Capacitance (to substrate):
C_TSV = 2πε₀ε_r L / ln(D_outer/D_inner)
      ≈ 80-200 fF (for typical dimensions)
```

### Wafer-Level Interconnects

**Micro-bump Technology**:
- **Pitch**: 20-50 μm
- **Bump height**: 5-15 μm
- **Material**: Cu, SnAg
- **Application**: High-density die-to-die connections

**Hybrid Bonding** (Direct Cu-Cu bonding):
- **Pitch**: 1-10 μm (ultra-fine)
- **Process**: Surface activation + thermal compression
- **Temperature**: 200-300°C
- **Advantages**: Highest density, lowest parasitics
- **Applications**: HBM, advanced logic stacking

## Thermal Management

### Heat Generation in MCMs

**Power Density Calculation**:
```
For a typical MCM:
- CMOS ASIC: 5W in 10×10 mm² die = 5 W/cm²
- MEMS sensor: 50 mW in 5×5 mm² die = 0.2 W/cm²

Total module: 5.05 W in 15×15 mm² = 2.24 W/cm²
```

### Thermal Resistance Network

**Simplified Model**:
```
        Junction (T_j)
             |
        θ_jc (junction to case)
             |
        Case (T_c)
             |
        θ_ca (case to ambient)
             |
        Ambient (T_a)

T_j = T_a + P × (θ_jc + θ_ca)
```

**Component Thermal Resistances**:

| Path | Typical θ (°C/W) |
|------|------------------|
| Die to die attach | 0.1-0.5 |
| Die attach material | 0.5-2.0 |
| Substrate (lateral) | 5-20 |
| Substrate (vertical) | 1-5 |
| TIM (thermal interface) | 0.2-1.0 |
| Heat sink | 0.5-10 |
| Convection to ambient | 10-50 |

### Thermal Management Strategies

#### 1. Substrate Selection

**Material Comparison**:

| Material | k (W/m·K) | CTE (ppm/°C) | Cost |
|----------|-----------|--------------|------|
| Si | 150 | 2.6 | High |
| AlN | 170 | 4.5 | High |
| Al₂O₃ | 24 | 6.7 | Medium |
| Cu-Mo-Cu | 180-220 | 6-8 | Very High |
| BT resin | 0.3-0.7 | 15-18 | Low |

**Best Choices**:
- **High power**: AlN, Cu-Mo-Cu
- **Cost-sensitive**: Al₂O₃ with thermal vias
- **Volume production**: Enhanced organic (thick Cu, thermal vias)

#### 2. Die Attach Materials

**Material Options**:

| Type | k (W/m·K) | Process Temp | Cost |
|------|-----------|--------------|------|
| Solder (SAC305) | 57 | 260°C | Low |
| Silver epoxy | 3-5 | 150°C | Medium |
| Thermal epoxy | 1-3 | 150°C | Low |
| Sinter silver | 150-250 | 200-300°C | High |

**Sintered Silver** (for high-power):
- Pressure-less sintering at 250°C
- Excellent thermal conductivity
- High reliability
- Used in automotive, power electronics

#### 3. Thermal Vias

**Design Guidelines**:
```
Via diameter: 200-300 μm (in organic substrate)
Via pitch: 400-600 μm
Cu plating: Fully filled or conformal

Thermal resistance reduction:
θ_with_vias / θ_without_vias ≈ 0.3-0.5
```

**Via Array Design**:
```
Number of vias under die:
N = A_die / (pitch²)

For 10×10 mm die with 0.5 mm pitch:
N = (10×10) / (0.5²) = 400 vias
```

#### 4. Heat Spreaders

**Integrated Heat Spreader (IHS)**:
- Material: Cu, Al, Cu-W
- Thickness: 0.5-2 mm
- Attachment: Thermal epoxy or solder
- Thermal resistance: 0.1-0.5 °C/W

**Active Cooling**:
- Forced air (fans): 5-20 W/cm²
- Liquid cooling: 20-100 W/cm²
- Thermoelectric coolers: Localized cooling

### Thermal Simulation Example

**Finite Element Analysis Setup**:

```python
# Simplified 2D thermal model (Python/NumPy)
import numpy as np
import matplotlib.pyplot as plt

# Domain setup
Lx, Ly = 15e-3, 2e-3  # 15mm × 2mm
nx, ny = 150, 20
dx = Lx / nx
dy = Ly / ny

# Material properties
k_Si = 150  # W/m·K
k_substrate = 25  # W/m·K (ceramic)
k_cu = 400  # W/m·K

# Power dissipation
P_total = 5  # W
A_die = 10e-3 * 10e-3  # m²
q = P_total / A_die  # W/m² (volumetric generation)

# Boundary conditions
T_ambient = 25  # °C
h_conv = 50  # W/m²·K (forced convection)

# Temperature field solution using finite difference
# (Simplified - actual solution uses iterative solver)
T = np.ones((ny, nx)) * T_ambient

# ... FDM iteration code ...
# Result: T_junction = 65°C, T_max = 70°C
```

## Design Considerations

### Electrical Design

#### Signal Integrity

**Transmission Line Effects**:

For MCM-D substrates with fine-pitch routing:
```
Microstrip impedance:
Z₀ = (87/√(ε_r+1.41)) × ln(5.98h/(0.8w+t))

Example:
w = 10 μm, h = 12 μm, t = 2 μm, ε_r = 3.5
Z₀ ≈ 50 Ω
```

**Crosstalk Analysis**:
```
Far-end crosstalk coefficient:
K_FEXT ≈ (π/4) × (L/λ) × (C_m/C_g)

where:
L = trace length
λ = wavelength
C_m = mutual capacitance
C_g = ground capacitance
```

**Design Rules for Low Crosstalk**:
- Spacing ≥ 3× trace width
- Guard traces between critical signals
- Ground planes between signal layers
- Differential pairs for high-speed signals

#### Power Distribution Network (PDN)

**IR Drop Analysis**:
```
For a 1.2V CMOS die drawing 2A:

Allowed voltage drop: ±5% = 60 mV

R_max = V_drop / I = 60mV / 2A = 30 mΩ

Power grid design:
- Multiple power pads (20-50)
- Wide power traces (100-500 μm)
- Power planes in substrate
- Decoupling capacitors
```

**Decoupling Strategy**:

| Capacitor | Value | Location | Purpose |
|-----------|-------|----------|---------|
| On-die | 10-50 nF | MIM caps | High-freq |
| Package | 100 nF - 1 μF | Near die | Mid-freq |
| PCB | 10-100 μF | Module | Low-freq |

#### Impedance Matching

For RF modules:
```
Die output impedance: 50 Ω
Substrate trace: Designed for 50 Ω
PCB trace: 50 Ω
Connector: 50 Ω

Minimize reflections:
ρ = (Z_L - Z_0) / (Z_L + Z_0)
  = 0 (for matched system)
```

### Mechanical Design

#### CTE Mismatch Stress

**Thermal Stress Calculation**:
```
σ = E × α × ΔT / (1 - ν)

where:
E = Young's modulus
α = CTE
ΔT = temperature change
ν = Poisson's ratio

Example (Si die on organic substrate):
α_Si = 2.6 ppm/°C
α_org = 16 ppm/°C
ΔT = 150°C (assembly)

Δα = 13.4 ppm/°C
Strain ε = Δα × ΔT = 0.2% (manageable with underfill)
```

**Stress Relief Methods**:
1. Underfill for flip-chip
2. Compliant adhesives
3. Stress relief patterns
4. CTE-matched substrates

#### Warpage Control

**Sources of Warpage**:
- CTE mismatch
- Cure shrinkage (underfill, molding compound)
- Residual stress in thin films
- Asymmetric structure

**Mitigation**:
- Balanced stack-up (symmetric)
- Low-stress materials
- Proper cure profiles
- Mechanical stiffeners

### MEMS-Specific Considerations

#### Pressure Sensitivity

For MEMS pressure sensors in MCM:
- Ensure pressure port to membrane
- Avoid stress transmission from substrate
- Use compliant die attach if needed
- Consider package-induced stress

#### Acoustic Isolation

For MEMS microphones:
- Acoustic port design
- Minimize mechanical coupling
- Damping materials
- Seal non-functional areas

#### Particle Contamination

- Clean assembly environment (Class 1000-10000)
- Cavity packages for MEMS
- Getters for hermetic packages
- Avoid particle-generating processes after MEMS exposure

## Assembly Processes

### Process Flow Overview

```
1. Substrate Fabrication
   ├── MCM-L: Lamination, drilling, plating
   ├── MCM-C: Tape casting, printing, firing
   └── MCM-D: Thin-film deposition

2. Die Preparation
   ├── Wafer testing (probe)
   ├── Backgrind (thinning)
   ├── Bumping (for flip-chip)
   └── Dicing

3. Die Attach
   ├── Pick-and-place
   ├── Adhesive or solder
   └── Cure/reflow

4. Interconnection
   ├── Wire bonding
   ├── Flip-chip bonding
   └── Underfill (if flip-chip)

5. Encapsulation (optional)
   ├── Glob-top
   ├── Molding
   └── Cavity sealing

6. Final Assembly
   ├── Lid attachment
   ├── External connections
   └── Marking

7. Testing
   ├── Electrical test
   ├── Thermal cycling
   └── Final inspection
```

### Critical Process Parameters

#### Die Bonding

**Temperature Profile**:
```
For epoxy die attach:
- Pre-cure: 80°C, 2 min
- Cure: 150°C, 30 min
- Cool: Controlled ramp (<5°C/min)

Bond line thickness: 10-50 μm
Placement accuracy: ±25 μm
```

#### Wire Bonding

**Process Window**:
- **Time**: 15-30 ms per bond
- **Force**: 30-80 gf (varies by wire size)
- **Power**: 50-200 mW (ultrasonic)
- **Temperature**: 150-250°C (substrate)

**Quality Metrics**:
- Ball size: 1.8-2.5× wire diameter
- Bond strength: >5 gf (pull test)
- Loop height variation: ±20%

#### Flip-Chip Bonding

**Alignment Accuracy**:
- Chip-to-substrate: ±10-25 μm
- Bump-to-pad: ±5 μm (after collapse)

**Reflow Profile** (for SAC305):
```
Temperature (°C)
260 ┤        ╱╲
    │       ╱  ╲
220 │    ╱─┘    └─╲
    │   ╱          ╲
150 │  ╱            ╲___
    │ ╱
25  ├┘
    └─────────────────────> Time (s)
      60  90 120  180  240

Zones:
1. Preheat: 25→150°C, 60s
2. Soak: 150-180°C, 60-90s
3. Reflow: 220-260°C, 60s (peak)
4. Cool: <5°C/s
```

### Yield Optimization

**Known-Good-Die (KGD)**:
- Wafer-level probe test
- Burn-in (optional, for high-rel)
- Visual inspection
- Target defect rate: <100 ppm

**Assembly Yield Factors**:
```
Y_module = Y_die1 × Y_die2 × ... × Y_assembly

Example:
Y_MEMS = 95%
Y_ASIC = 90%
Y_passive = 98%
Y_assembly = 95%

Y_total = 0.95 × 0.90 × 0.98 × 0.95 = 79.6%
```

## Testing and Reliability

### Module-Level Testing

#### Electrical Testing

**Parametric Tests**:
- Supply current (I_DD)
- Input/output leakage
- Threshold voltages
- Speed paths (setup/hold)
- Analog parameters (offset, gain, linearity)

**Functional Tests**:
- Built-in self-test (BIST)
- Scan chain testing
- Functional vectors
- Boundary scan (JTAG)

**MEMS-Specific Tests**:
- Sensitivity
- Frequency response
- Noise floor
- Cross-axis sensitivity
- Temperature coefficient

#### Environmental Testing

**Temperature Cycling**:
- Condition A: -55°C to +125°C
- Condition B: -40°C to +85°C (consumer)
- Dwell time: 15-30 minutes
- Cycles: 500-1000

**Failure Mechanisms**:
- Solder fatigue
- Delamination
- Wire bond failure
- Interconnect open/short

**Highly Accelerated Stress Test (HAST)**:
- Temperature: 130°C
- Humidity: 85% RH
- Pressure: 2 atm
- Duration: 96-264 hours
- Detects: Corrosion, moisture ingress

### Reliability Modeling

#### Acceleration Factors

**Arrhenius Model** (temperature):
```
AF = exp[(E_a/k) × (1/T_use - 1/T_stress)]

where:
E_a = activation energy (0.3-1.0 eV)
k = Boltzmann constant
T = absolute temperature (K)

Example:
T_use = 55°C = 328K
T_stress = 125°C = 398K
E_a = 0.7 eV

AF = exp[(0.7/(8.617×10⁻⁵)) × (1/328 - 1/398)]
   = exp[8119 × 0.000537]
   = 73
```

**Coffin-Manson Model** (thermal cycling):
```
N_f = C × (ΔT)^(-n)

where:
N_f = cycles to failure
ΔT = temperature range
n = 1.9-2.5 (fatigue exponent)
C = constant
```

#### MTTF Calculation

```
Mean Time To Failure:

MTTF = (device hours) / (failures)

Example test:
- 1000 modules
- 1000 hours @ 125°C
- 2 failures
- AF = 73 (calculate