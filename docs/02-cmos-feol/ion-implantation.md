# Ion Implantation: Precision Doping for Semiconductor Devices

## Table of Contents
- [Introduction](#introduction)
- [Fundamental Principles](#fundamental-principles)
  - [Why Ion Implantation?](#why-ion-implantation)
  - [The Ion Implantation Process](#the-ion-implantation-process)
  - [Basic Physics](#basic-physics)
  - [Gaussian Profile Approximation](#gaussian-profile-approximation)
- [Ion Implanter Systems](#ion-implanter-systems)
  - [System Architecture](#system-architecture)
  - [1. Ion Source](#1-ion-source)
  - [2. Mass Analyzer](#2-mass-analyzer)
  - [3. Acceleration Column](#3-acceleration-column)
  - [4. Beam Scanning System](#4-beam-scanning-system)
  - [5. End Station](#5-end-station)
- [Implantation Physics](#implantation-physics)
  - [Stopping Power](#stopping-power)
  - [Range Statistics](#range-statistics)
  - [Channeling](#channeling)
  - [Lattice Damage](#lattice-damage)
- [Implant Parameters and Recipes](#implant-parameters-and-recipes)
  - [Common Implant Types](#common-implant-types)
  - [Dose and Energy Selection](#dose-and-energy-selection)
- [Annealing and Activation](#annealing-and-activation)
  - [Why Annealing is Necessary](#why-annealing-is-necessary)
  - [Annealing Techniques](#annealing-techniques)
  - [Activation Percentage](#activation-percentage)
  - [Transient Enhanced Diffusion (TED)](#transient-enhanced-diffusion-ted)
- [Advanced Implantation Techniques](#advanced-implantation-techniques)
  - [Tilt and Twist](#tilt-and-twist)
  - [Pre-Amorphization Implant (PAI)](#pre-amorphization-implant-pai)
  - [Plasma Doping (PLAD)](#plasma-doping-plad)
  - [Molecular Ion Implantation](#molecular-ion-implantation)
- [Metrology and Process Control](#metrology-and-process-control)
  - [Dose Measurement](#dose-measurement)
  - [Depth Profiling](#depth-profiling)
  - [Process Monitoring](#process-monitoring)
- [Safety and Environmental](#safety-and-environmental)
  - [Gas Toxicity](#gas-toxicity)
  - [Radiation Hazards](#radiation-hazards)
  - [Waste Management](#waste-management)
- [Cost and Economics](#cost-and-economics)
  - [Equipment Costs](#equipment-costs)
  - [Operating Costs](#operating-costs)
  - [Throughput Analysis](#throughput-analysis)
- [Troubleshooting](#troubleshooting)
  - [Common Issues](#common-issues)
- [Python Simulation](#python-simulation)
- [Summary](#summary)
- [Further Reading](#further-reading)
  - [Textbooks](#textbooks)
  - [Papers](#papers)
  - [Standards](#standards)
  - [Software Tools](#software-tools)

## Introduction

Ion implantation is the process of introducing dopant atoms into a semiconductor substrate by accelerating ionized atoms to high energies and directing them into the target material. Unlike thermal diffusion, ion implantation provides precise control over dopant concentration, depth, and lateral distribution, making it essential for modern CMOS fabrication.

> **Key Advantage**: Ion implantation allows independent control of dose and depth, enabling the complex doping profiles required for sub-100nm transistors.

## Fundamental Principles

### Why Ion Implantation?

**Comparison with Thermal Diffusion**:

| Property | Ion Implantation | Thermal Diffusion |
|----------|-----------------|-------------------|
| Temperature | Room temp to 500°C | 900-1200°C |
| Depth control | Precise (energy control) | Limited (time/temp) |
| Dose control | Excellent (±1-2%) | Poor (±10-20%) |
| Profile shape | Gaussian, controlled | Erfc, complementary error function |
| Lateral diffusion | Minimal | Significant |
| Damage | High (requires anneal) | Low |
| Throughput | High (batch) | Low (serial) |
| Cost | High equipment | Low equipment |

**Modern Applications**:
- Source/drain doping (all nodes)
- Well formation (twin-well CMOS)
- Threshold voltage adjustment (Vth implants)
- Halo/pocket implants (short-channel control)
- Pre-amorphization (reduce channeling)

### The Ion Implantation Process

```
Ion Source → Mass Analysis → Acceleration → Beam Scanning → Wafer
    ↓            ↓               ↓              ↓            ↓
Generate     Select         Energy        Uniform       Target
dopant       desired        control       coverage      substrate
ions         species        (keV-MeV)     (raster)      (Si wafer)
```

### Basic Physics

#### Energy and Penetration Depth

**Ion Energy**:
```
E = q × V

Where:
E = Ion energy (eV)
q = Ion charge (typically +1)
V = Acceleration voltage (V)

Example: 
V = 50 kV → E = 50 keV per ion
```

**Projected Range (Rp)**:

The average depth of implanted ions follows approximately:

$$
R_p \propto \frac{E}{M_{\text{ion}}}
$$

Where:
- **Rp** = Projected range (depth)
- **E** = Ion energy
- **M_ion** = Mass of ion

**Typical Ranges** (in Silicon):

| Ion | Energy (keV) | Rp (nm) | Application |
|-----|--------------|---------|-------------|
| B⁺ | 10 | 35 | Ultra-shallow junctions |
| B⁺ | 50 | 160 | Source/drain |
| BF₂⁺ | 50 | 80 | Shallow S/D (heavier) |
| P⁺ | 50 | 100 | NMOS S/D |
| As⁺ | 50 | 55 | Deep S/D, contact |
| P⁺ | 300 | 420 | N-well |
| B⁺ | 200 | 580 | P-well |

#### Dose and Concentration

**Implant Dose** (Φ):
```
Φ = ∫ I dt / (q × A)

Where:
Φ = Dose (atoms/cm²)
I = Beam current (A)
t = Time (seconds)
q = Elementary charge (1.602×10⁻¹⁹ C)
A = Implant area (cm²)

Typical doses: 10¹² - 10¹⁶ atoms/cm²
```

**Peak Concentration**:
```
N_peak = Φ / (√(2π) × ΔRp)

Where:
N_peak = Peak concentration (atoms/cm³)
ΔRp = Straggle (standard deviation of depth)

Example:
Φ = 5×10¹⁵ /cm²
ΔRp = 30 nm
N_peak = 5×10¹⁵ / (2.5 × 30×10⁻⁷) ≈ 6.6×10²⁰ /cm³
```

### Gaussian Profile Approximation

For most implants, the concentration profile is approximately Gaussian:

$$
N(x) = \frac{\Phi}{\sqrt{2\pi} \Delta R_p} \exp\left(-\frac{(x - R_p)^2}{2\Delta R_p^2}\right)
$$

Where:
- **N(x)** = Concentration at depth x
- **Φ** = Implant dose
- **Rp** = Projected range (peak position)
- **ΔRp** = Straggle (spread)

```
Concentration
     |
N_pk |    ╱‾‾╲
     |   ╱    ╲
     |  ╱      ╲
     | ╱        ╲___
     |╱______________╲___ 
     0    Rp    2Rp      Depth
     
     ←→ ΔRp (straggle)
```

## Ion Implanter Systems

### System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    ION IMPLANTER                         │
│                                                          │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐           │
│  │   Ion    │   │  Mass    │   │ Accel.   │           │
│  │  Source  │→→ │ Analyzer │→→ │  Column  │→→→→→→→   │
│  │ (dopant) │   │(magnet)  │   │ (0-200kV)│           │
│  └──────────┘   └──────────┘   └──────────┘           │
│                                                          │
│                                      ↓                   │
│                                                          │
│                              ┌──────────────┐           │
│                              │   Scanner    │           │
│                              │  (X-Y beam)  │           │
│                              └──────┬───────┘           │
│                                     ↓                    │
│                              ┌──────────────┐           │
│                              │    Wafer     │           │
│                              │   Chamber    │           │
│                              │  (process)   │           │
│                              └──────────────┘           │
└─────────────────────────────────────────────────────────┘
```

### 1. Ion Source

**Purpose**: Generate ionized dopant atoms

#### Freeman Ion Source (Most Common)

```
     Gas inlet (BF₃, PH₃, AsH₃)
           ↓
    ┌────────────┐
    │  Plasma    │  ← RF power (13.56 MHz, 1-3 kW)
    │  Chamber   │     Ionization: e⁻ + Gas → Ion⁺ + 2e⁻
    └─────┬──────┘
          ↓
    Extraction electrode (-10 to -40 kV)
          ↓
    Ion beam (B⁺, BF₂⁺, P⁺, As⁺)
```

**Source Gases**:

| Dopant | Source Gas | Ion Species | Notes |
|--------|-----------|-------------|-------|
| Boron | BF₃ | B⁺, BF₂⁺ | BF₂⁺ preferred (less channeling) |
| Phosphorus | PH₃ | P⁺ | Toxic, requires scrubber |
| Arsenic | AsH₃ | As⁺ | Extremely toxic |
| Antimony | Solid Sb | Sb⁺ | High-temp source |
| Indium | Solid In | In⁺ | High-temp source |

**Source Lifetime**: 
- Gas sources: Continuous (tank replacement)
- Solid sources: 100-500 hours

#### Bernas Ion Source (High Current)

**Features**:
- Higher beam current (>10 mA)
- Better for high-dose implants
- Longer source life

### 2. Mass Analyzer

**Purpose**: Select desired ion species and remove contaminants

```
   Ion beam (mixed species)
        ↓
   ╔═════════════╗
   ║   Magnet    ║  Magnetic field B
   ║  (sector)   ║  Lorentz force: F = qvB
   ╚═════════════╝
        ↓
   Only ions with correct m/q ratio pass
        ↓
   Pure ion beam
```

**Mass Selection**:
```
R = (m × v) / (q × B)

Where:
R = Radius of curvature
m = Ion mass
v = Ion velocity
q = Ion charge
B = Magnetic field strength

Different masses → Different radii → Spatial separation
```

**Resolving Power**:
```
M/ΔM = R / (s₁ + s₂)

Where:
s₁, s₂ = Slit widths

Typical: M/ΔM > 100 (sufficient to separate adjacent masses)
```

**Example**: Separating ¹¹B⁺ (mass 11) from ¹⁰B⁺ (mass 10)

### 3. Acceleration Column

**Purpose**: Accelerate ions to desired energy

```
   ─────────────  Ground (0 V)
        Gap
   ═════════════  High voltage terminal (-10 to -200 kV)
        ↓
   Ions accelerated through potential difference
        ↓
   Final energy = q × V
```

**Energy Ranges**:

| Implanter Type | Energy Range | Applications |
|----------------|--------------|--------------|
| Low energy | 0.1-10 keV | Ultra-shallow junctions (<20nm) |
| Medium current | 10-200 keV | S/D, extensions, Vth adjust |
| High current | 10-80 keV | Wells, high-dose S/D |
| High energy | 200 keV - 3 MeV | Deep wells, buried layers |

**Beam Transport**:
- Quadrupole focusing lenses (electrostatic or magnetic)
- Maintain beam collimation
- Minimize divergence

### 4. Beam Scanning System

**Purpose**: Uniformly cover entire wafer

#### Hybrid Scan (Most Common)

```
   Electrostatic X-scan (fast, ~1 kHz)
   ════════════════════════════════
         ║    ║    ║    ║
         ↓    ↓    ↓    ↓
   ┌────────────────────────────┐
   │         Wafer              │  Mechanical Y-scan
   │    (moves vertically)      │  (slow, ~1 Hz)
   └────────────────────────────┘
   
Raster pattern ensures uniform dose
```

**Uniformity Specification**: ±1-2% (3σ) across wafer

#### Batch Processing

Modern implanters can hold 13-25 wafers:
```
   Wafer cassette
   ┌──┬──┬──┬──┐
   │W1│W2│W3│W4│ ... up to 25 wafers
   └──┴──┴──┴──┘
        ↓
   Sequential implantation
        ↓
   Throughput: 200-400 wafers/hour (depends on dose)
```

### 5. End Station

**Wafer Handling**:
- Wafer holder (platen) at ground potential
- Tilt capability: 0-60° (controls channeling)
- Rotation: 0-360° (for non-uniform implants)
- Temperature control: Cooling or heating

**Process Monitoring**:
- Faraday cup: Measures beam current
- Dose integrator: Calculates total dose
  ```
  Dose = ∫ (I / q × A) dt
  ```
- End-point detection: Stops at target dose

**Pressure**:
- High vacuum: 10⁻⁵ to 10⁻⁷ Torr
- Prevents ion scattering from gas molecules
- Reduces contamination

## Implantation Physics

### Stopping Power

Ions lose energy through two mechanisms:

#### 1. Nuclear Stopping (Elastic Collisions)

**Mechanism**: Direct collisions with target nuclei

```
   Ion ○ ───→ ●─● Target atom
              ╲
               ╲ Recoil
                ●
                
Dominant at: Low energies (<10 keV)
Causes: Most lattice damage
```

**Nuclear Stopping Power**:
```
Sn = (dE/dx)nuclear ∝ 1/E

Lower energy → Higher Sn → More damage/less penetration
```

#### 2. Electronic Stopping (Inelastic)

**Mechanism**: Coulombic interaction with electron clouds

```
   Ion ○ ───→  ~e⁻~ Electron cloud
              Energy transfer to electrons
              
Dominant at: High energies (>50 keV)
Causes: Less lattice damage, deeper penetration
```

**Electronic Stopping Power**:
```
Se = (dE/dx)electronic ∝ √E

Higher energy → Higher Se → Deeper penetration
```

**Total Stopping**:
```
Stotal = Sn + Se

Energy loss: dE/dx (eV/Å)
```

### Range Statistics

**Projected Range (Rp)**: Average penetration depth

**Range Straggle (ΔRp)**: Standard deviation of depth distribution

**Lateral Straggle (ΔRp⊥)**: Lateral spread perpendicular to beam

```
Top view:             Side view:
                      
    ╱│╲                  ↓ Ion beam
   ╱ │ ╲                 │
  ╱  │  ╲                ├─ Surface
 ○───┼───○               │
  ╲  │  ╱                ├─ Rp (avg depth)
   ╲ │ ╱                 │
    ╲│╱                  ├─ ΔRp (straggle)
     v                   │
     
←→ ΔRp⊥ (lateral)
```

**Typical Values** (50 keV B⁺ in Si):
- Rp ≈ 160 nm
- ΔRp ≈ 60 nm
- ΔRp⊥ ≈ 50 nm

### Channeling

**Definition**: Ions align with crystal lattice channels → much deeper penetration

```
Random (amorphous):   Channeled (aligned):
    ↓ ↓ ↓                 ↓   ↓   ↓
    ●─●─●                 ●───●───●
    │ │ │    Shallow      │   │   │  Deep penetration
    ●─●─●    (normal)     │   │   │  (channeling)
    │ │ │                 │   │   │
    ●─●─●                 ●───●───●
```

**Major Crystal Directions**:
- <100>: Easiest channeling
- <110>: Moderate
- <111>: Difficult

**Channeling Fraction**: 
- 0° tilt: 20-50% of ions channel
- 7° tilt: <5% channel (standard practice)

**Mitigation Strategies**:

1. **Wafer Tilt**: 7° off-axis (most common)
2. **Wafer Rotation**: Twist orientation
3. **Pre-Amorphization Implant (PAI)**:
   ```
   Si⁺ or Ge⁺ implant first
         ↓
   Amorphizes surface layer
         ↓
   No channels exist
         ↓
   Dopant implant (controlled depth)
   ```

### Lattice Damage

**Damage Cascade**:
```
   Primary ion (50 keV)
         ↓
   Collides with Si atom
         ↓
   Recoil atom (5 keV)
         ↓
   Secondary collisions
         ↓
   Tertiary collisions
         ↓
   Damage region (~10nm diameter)
```

**Defect Types**:

1. **Point Defects**:
   - Vacancies (missing atom)
   - Interstitials (extra atom)
   - Frenkel pairs (vacancy + interstitial)

2. **Extended Defects**:
   - Clusters (aggregates of point defects)
   - Dislocation loops
   - Stacking faults

3. **Amorphization**:
   - Complete loss of crystal structure
   - Threshold dose: ~10¹⁴-10¹⁵ /cm² (depends on energy)

**Amorphous Layer Depth**:
```
Concentration
     |   Crystalline  Amorphous    Crystalline
     |      Si          layer          Si
     |      ↓            ↓              ↓
     |  ════════════════════════════════
     |               ╱‾‾╲
     |              ╱    ╲
     |_____________╱______╲____________ Depth
                  └───────┘
              Amorphous region (damaged)
              
Typical: 50-200 nm deep (for S/D implants)
```

## Implant Parameters and Recipes

### Common Implant Types

#### 1. Well Formation

**N-Well (for PMOS)**:
```
Species: Phosphorus (P⁺) or Arsenic (As⁺)
Energy: 200-400 keV
Dose: 5×10¹² - 5×10¹³ /cm²
Depth: ~1-2 μm
Purpose: Create N-type region for PMOS transistors
```

**P-Well (for NMOS)**:
```
Species: Boron (B⁺)
Energy: 150-300 keV
Dose: 5×10¹² - 5×10¹³ /cm²
Depth: ~1-2 μm
Purpose: Create P-type region for NMOS transistors
```

#### 2. Threshold Voltage (Vth) Adjustment

**NMOS Vth Implant**:
```
Species: Boron (B⁺) or BF₂⁺
Energy: 20-80 keV
Dose: 1×10¹² - 5×10¹² /cm²
Depth: 50-150 nm (channel region)
Purpose: Adjust NMOS threshold voltage
Result: Increases Vth (adds P-type dopant)
```

**PMOS Vth Implant**:
```
Species: Phosphorus (P⁺) or Arsenic (As⁺)
Energy: 40-120 keV
Dose: 1×10¹² - 3×10¹² /cm²
Purpose: Adjust PMOS threshold voltage
Result: Increases |Vth| for PMOS
```

#### 3. Source/Drain Extensions (LDD)

**NMOS LDD**:
```
Species: Arsenic (As⁺) or Phosphorus (P⁺)
Energy: 5-20 keV (shallow)
Dose: 1×10¹⁴ - 5×10¹⁴ /cm²
Depth: 20-50 nm
Purpose: Reduce hot carrier effects
```

**PMOS LDD**:
```
Species: BF₂⁺ (preferred over B⁺)
Energy: 5-15 keV
Dose: 1×10¹⁴ - 3×10¹⁴ /cm²
Depth: 15-40 nm
Purpose: Shallow P-type extension
```

#### 4. Source/Drain (Heavy Doping)

**NMOS S/D**:
```
Species: Arsenic (As⁺) - less diffusion than P
Energy: 20-80 keV
Dose: 3×10¹⁵ - 8×10¹⁵ /cm²
Depth: 50-150 nm
Concentration: >10²⁰ /cm³
Purpose: Low-resistance contacts
```

**PMOS S/D**:
```
Species: BF₂⁺ or B⁺
Energy: 5-30 keV
Dose: 2×10¹⁵ - 6×10¹⁵ /cm²
Purpose: P⁺ contacts
```

#### 5. Halo/Pocket Implants

**Purpose**: Suppress short-channel effects (SCE)

```
   Gate
    ││
────┼┼────  ← Surface
  H │  │ H   H = Halo (counter-doped)
  A │  │ A   Tilted implant (20-45°)
  L │  │ L   Higher doping near S/D
  O │  │ O   Increases Vth for short channels
    └──┘
    
NMOS Halo: P⁺ or In⁺ (into N⁺ S/D regions)
PMOS Halo: As⁺ or Sb⁺ (into P⁺ S/D regions)

Implant angles: 4 quadrants (0°, 90°, 180°, 270° rotation)
```

### Dose and Energy Selection

**General Guidelines**:

```
Target Concentration:
  Low (10¹⁵-10¹⁷ /cm³): Wells, Vth adjust
  Medium (10¹⁷-10¹⁹ /cm³): LDD, extensions
  High (10¹⁹-10²⁰ /cm³): S/D contacts

Target Depth:
  Shallow (<50nm): Low energy (5-20 keV)
  Medium (50-200nm): Medium energy (20-80 keV)
  Deep (>200nm): High energy (>100 keV)

Energy-Depth Rule of Thumb:
  Rp (nm) ≈ (E/keV) × k
  
  Where k depends on ion mass:
  B: k ≈ 3-4
  P: k ≈ 2-2.5
  As: k ≈ 1-1.5
```

## Annealing and Activation

### Why Annealing is Necessary

**As-Implanted State**:
1. **Lattice damage**: Amorphous or heavily damaged crystal
2. **Inactive dopants**: Dopants not on substitutional sites
3. **High resistivity**: No free carriers

**After Annealing**:
1. **Crystal repair**: Epitaxial regrowth from substrate
2. **Dopant activation**: Dopants move to substitutional sites
3. **Low resistivity**: Free carriers available

### Annealing Techniques

#### 1. Furnace Annealing (Legacy)

```
Temperature: 900-1000°C
Time: 30-60 minutes
Atmosphere: N₂ or Ar
Ramp: 5-10°C/min

Advantages: 
- Complete damage repair
- High activation (>95%)

Disadvantages:
- Long time → Excessive diffusion
- Not suitable for shallow junctions
```

#### 2. Rapid Thermal Annealing (RTA)

**Most Common for Modern Devices**:

```
Temperature: 950-1050°C
Time: 1-10 seconds (spike anneal)
Ramp rate: 50-200°C/sec
Atmosphere: N₂, forming gas (N₂/H₂)

Process:
    Temp
     |      ╱‾╲ Peak: 1000°C
1000°|     ╱   ╲ 1-5 seconds
     |    ╱     ╲
     |   ╱       ╲
  RT |__╱_________╲______ Time
     0   5   10  15  20 sec
```

**Advantages**:
- Minimal dopant diffusion
- Preserves shallow junctions
- High throughput

**Lamp Configuration**:
```
   Tungsten-halogen lamps (×100-150)
   ════════════════════════════════
              ↓↓↓ Heat
        ┌────────────┐
        │   Wafer    │  Temperature: Pyrometry
        │  (Si/Ge)   │  Uniformity: ±2-5°C
        └────────────┘
              ↑↑↑ Reflection
        Reflective chamber
```

#### 3. Laser Annealing

**Pulsed Laser Annealing**:
```
Laser: Excimer (XeCl, 308nm)
Pulse width: 10-100 nanoseconds
Energy density: 0.5-2 J/cm²
Penetration: 50-200 nm

Mechanism:
- Surface melting (~1414°C for Si)
- Liquid-phase epitaxial regrowth
- Ultra-fast cooling (10¹⁰ K/sec)
```

**Advantages**:
- No dopant diffusion (too fast)
- Ultra-shallow activation
- Selective area processing

**Challenges**:
- Requires amorphous layer (melting threshold)
- Non-uniform beams → CD variation
- Expensive equipment

#### 4. Flash Annealing

```
Method: High-intensity flash lamps
Duration: <1 millisecond
Temperature: 1200-1400°C (surface)
Depth: 50-100 nm

Applications:
- Ultra-shallow junctions (<20nm)
- FinFET S/D activation
- Advanced nodes (<14nm)
```

### Activation Percentage

**Definition**: Fraction of implanted dopants on substitutional sites

$$
\text{Activation} = \frac{N_{\text{active}}}{N_{\text{total}}} \times 100\%
$$

**Typical Activation** (after RTA):
- Boron: 80-95%
- Phosphorus: 85-95%
- Arsenic: 70-90% (lower due to clustering)

**Solid Solubility Limit**:
```
Maximum active concentration at given temperature

T = 1000°C:
  Boron: 5×10²⁰ /cm³
  Phosphorus: 1.5×10²¹ /cm³
  Arsenic: 2×10²¹ /cm³
  
Implanted dose > Solubility → Excess forms inactive clusters
```

### Transient Enhanced Diffusion (TED)

**Problem**: Implant damage causes enhanced dopant diffusion during anneal

```
Mechanism:
  Implant damage → Excess interstitials (Si_i)
          ↓
  Anneal → Interstitials mobile
          ↓
  Interstitials + Dopant → Dopant-interstitial pairs
          ↓
  Enhanced diffusion (10-100× normal)
          ↓
  Junction deeper than expected
```

**Duration**: First 1-10 seconds of anneal

**Mitigation**:
1. **Spike anneal**: Minimize time at temperature
2. **Pre-amorphization**: Creates vacancy-rich region (suppresses TED)
3. **Carbon co-implant**: Traps interstitials

## Advanced Implantation Techniques

### Tilt and Twist

**Wafer Orientation**:

```
Tilt Angle:          Twist Angle:
                     
    ↓ 7°                Top view:
    ╲ Ion                  ↻ 22°
     ╲                   ╱─╲
      ╲                 │   │
   ════════             ╲─╱
     Wafer              Wafer
     
Tilt: 7° (standard)    Twist: 22° or 45°
Purpose: Avoid        Purpose: Avoid
channeling            planar channels
```

### Pre-Amorphization Implant (PAI)

**Process**:
```
Step 1: Si⁺ or Ge⁺ implant
   Energy: 10-40 keV
   Dose: 1×10¹⁴ - 5×10¹⁴ /cm²
        ↓
   Creates amorphous layer (50-100nm)
        ↓
Step 2: Dopant implant (As, B, P)
   No channeling (no crystal!)
   Controlled depth
        ↓
Step 3: Anneal
   SPER (Solid Phase Epitaxial Regrowth)
   Amorphous → Single crystal
```

**Advantages**:
- Eliminates channeling
- Sharper profiles
- Better activation (Ge-PAI especially)

**SPER Mechanism**:
```
   Crystalline Si    Amorphous    Crystalline
        │                │              │
        ├────────────────┤              │
        │    Interface   │              │
        │    moves →     ├──────────────┤
        │                │   Regrowth   │
   Temperature: 500-700°C
   Rate: 1-10 nm/sec
   Result: Perfect crystal restoration
```

### Plasma Doping (PLAD)

**Alternative to Ion Implantation**:

```
Process:
  Plasma (B₂H₆, PH₃) generated near wafer
        ↓
  Ions accelerated by sheath potential (0.1-5 kV)
        ↓
  Ultra-shallow implant (<10nm)
        ↓
  Low damage (low energy)
```

**Advantages**:
- Conformal doping (3D structures, FinFETs)
- Lower damage than beam-line implant
- No mass analysis needed

**Applications**:
- FinFET S/D (wraps around fin)
- 3D NAND (channel doping)

### Molecular Ion Implantation

**Cluster Ions**: BF₂⁺, B₁₀H₁₄⁺, etc.

**Advantages of BF₂⁺ vs. B⁺**:
```
Same energy (50 keV):
  B⁺: E_eff = 50 keV per B atom
      Rp ≈ 160 nm
      
  BF₂⁺: E_eff = 50/3 ≈ 17 keV per B atom
        Rp ≈ 80 nm (shallower!)
        Less channeling (heavier molecule)
```

**Decaborane (B₁₀H₁₄⁺)**:
- Contains 10 boron atoms
- Ultra-shallow implants (<20nm)
- Reduced damage per boron atom

## Metrology and Process Control

### Dose Measurement

**Faraday Cup**:
```
   Ion beam
        ↓
   ┌────────┐
   │  Cup   │  Suppressor electrode (-100V)
   │        │  Prevents secondary electron escape
   └───┬────┘
       │ Current measurement
       └─→ Integrator
       
Dose = Q / (q × A)

Where:
Q = Total charge collected (Coulombs)
q = Elementary charge (1.602×10⁻¹⁹ C)
A = Implant area (cm²)

Accuracy: ±1-2%
```

### Depth Profiling

#### Secondary Ion Mass Spectrometry (SIMS)

**Principle**: Sputter surface with ion beam, analyze ejected ions

```
Primary ion beam (Cs⁺, O₂⁺)
        ↓↓↓
   ═══════════  Surface
   │ Dopant  │  Sample
   │ Profile │
        ↑
   Mass spectrometer
   (detects Si, B, P, As, etc.)
```

**Specifications**:
- Depth resolution: 2-5 nm
- Detection limit: 10¹⁴-10¹⁶ /cm³
- Depth range: 0-10 μm
- Destructive technique

**Analysis**:
```
Count Rate
     |     ╱‾‾╲
     |    ╱    ╲
     |   ╱      ╲___
     |__╱____________ Sputter time (depth)
     
Convert time → depth using sputter rate
Extract Rp, ΔRp, and peak concentration
```

#### Four-Point Probe

**Measures Sheet Resistance**:
```
    I⁺    V⁺    V⁻    I⁻
    │     │     │     │
    ●─────●─────●─────●
    └──s──┴──s──┴──s──┘
          Sample
          
Sheet resistance: Rsh = (π/ln2) × (V/I) × CF

Units: Ω/square (Ω/□)

Infer dose and activation from Rsh
```

**Typical Values** (after activation):

| Implant Type | Rsh (Ω/□) |
|--------------|-----------|
| N⁺ S/D (As, 5×10¹⁵) | 50-100 |
| P⁺ S/D (B, 3×10¹⁵) | 80-150 |
| N-well (P, 5×10¹³) | 500-2000 |
| P-well (B, 5×10¹³) | 800-3000 |

### Process Monitoring

**Statistical Process Control (SPC)**:
```
Monitor Parameters:
- Dose: ±1-2% control
- Energy: ±0.5-1% control
- Uniformity: ±2% (3σ) across wafer
- Beam current: Stability <5%

Control charts:
  Xbar-R charts for dose
  Individual-Moving Range for energy
```

**Acceptance Criteria**:
```
Example: As S/D implant
  Target dose: 5×10¹⁵ /cm²
  Spec limits: 4.9-5.1×10¹⁵ /cm²
  Control limits (3σ): 4.95-5.05×10¹⁵
  
Out of control → Stop, investigate, recalibrate
```

## Safety and Environmental

### Gas Toxicity

**Hydride Gases** - Extremely Toxic:

| Gas | TLV (ppm) | Hazard |
|-----|-----------|--------|
| AsH₃ (Arsine) | 0.05 | Hemolytic, fatal at 25 ppm |
| PH₃ (Phosphine) | 0.3 | Pulmonary, pyrophoric |
| B₂H₆ (Diborane) | 0.1 | Pulmonary, pyrophoric |

**Safety Systems**:
1. **Gas cabinets**: Ventilated, sealed, monitored
2. **Scrubbers**: Burn box or wet scrubber (NaOH)
   ```
   Exhaust → Burn Box (1000°C, O₂) → HCl scrubber → Vent
   
   Example: 
   PH₃ + 2O₂ → H₃PO₄ (phosphoric acid)
   Scrubbed with base
   ```
3. **Leak detection**: Continuous monitors (<0.01 ppm alarm)
4. **Emergency shutdown**: Auto-close valves, purge with N₂

### Radiation Hazards

**X-Ray Generation**:
```
High-energy ions (>100 keV) hit metal →
Bremsstrahlung X-rays generated

Dose rate: 1-10 mSv/hr (unshielded at beam stop)

Shielding:
- Lead shielding (5-10 cm) around high-energy sections
- Interlocks prevent access during operation
- Dosimetry badges for operators
```

**Regulatory Limits**:
- Occupational: 50 mSv/year
- Public: 1 mSv/year
- ALARA principle (As Low As Reasonably Achievable)

### Waste Management

**Solid Waste**:
- Ion source components (contaminated with dopants)
- Replaced every 500-2000 hours
- Dispose as hazardous waste (As, P compounds)

**Pump Oil**:
- Vacuum pump oil (contaminated with dopants)
- Classified as hazardous waste
- Recycling or incineration

## Cost and Economics

### Equipment Costs

| Implanter Type | Cost (USD) | Throughput |
|----------------|------------|------------|
| Medium current | $2-4M | 300-400 wph |
| High current | $3-5M | 400-600 wph |
| High energy | $4-7M | 100-200 wph |

wph = wafers per hour (depends on dose)

### Operating Costs

**Per Wafer** (300mm):
```
Ion implantation: $10-30 per layer
  - Consumables: $2-5 (source gas, parts)
  - Maintenance: $3-8
  - Utilities: $2-5 (electricity, cooling water)
  - Labor: $3-10

Total for device:
  20-30 implant layers × $20 = $400-600
  
Implant cost: 10-15% of total wafer processing cost
```

**Source Gas Costs**:
- BF₃: $200-400 per cylinder
- PH₃: $300-600 per cylinder
- AsH₃: $500-1000 per cylinder

### Throughput Analysis

**Dose-Limited Throughput**:
```
Time = Dose / (Beam current / Area)

Example:
Dose: 5×10¹⁵ /cm²
Beam current: 10 mA
Wafer area: 707 cm² (300mm wafer)

Time = (5×10¹⁵ × 1.602×10⁻¹⁹ C × 707 cm²) / (10×10⁻³ A)
     = 56.6 seconds per wafer
     
Throughput = 3600/56.6 ≈ 64 wafers/hour (this layer only)
```

**Batch Processing**:
- Modern implanters: 13-25 wafer batch
- Parallel processing increases effective throughput

## Troubleshooting

### Common Issues

#### 1. Dose Non-Uniformity

**Symptoms**: CD variation, Vth variation across wafer

**Causes**:
- Scanner malfunction (X or Y scan failure)
- Beam current instability
- Faraday cup calibration drift

**Diagnosis**:
```
Measure Rsh at 49 points across wafer:
  Center  Edge  Corner
    O      O      O
     ╲     |     ╱
      ╲    |    ╱
       O───O───O
      ╱    |    ╲
     ╱     |     ╲
    O      O      O
    
Uniformity = (Max - Min) / (2 × Average) × 100%

Target: <2% (3σ)
```

**Solutions**:
- Recalibrate scanner waveforms
- Replace Faraday cup
- Check beam current stability

#### 2. Depth Variation

**Symptoms**: Junction depth not meeting spec

**Causes**:
- Energy drift (acceleration voltage)
- Channeling (wafer tilt incorrect)
- Photoresist thickness variation

**Diagnosis**:
- SIMS depth profiling
- Measure Rp and compare to target
- Check wafer tilt angle (should be 7°)

**Solutions**:
- Calibrate high-voltage supply
- Verify and reset tilt/twist angles
- Use PAI to eliminate channeling

#### 3. Contamination

**Symptoms**: Yield loss, device leakage

**Causes**:
- Metal contamination (Fe, Cu from source)
- Particle contamination (source spitting)
- Cross-contamination (previous implant species)

**Prevention**:
- Dedicated implanters per dopant type (B, P, As)
- Regular source cleaning
- Beam line cryopumps (capture contaminants)

## Python Simulation

See companion Python script: `simulation-examples/python/ion_implant_profile.py`

The simulation demonstrates:
1. Gaussian profile calculation
2. Range (Rp) and straggle (ΔRp) from ion energy
3. Junction depth calculation
4. Diffusion during anneal (simple model)
5. Activation vs. solid solubility
6. Profile plotting for multiple implant conditions

**Key equations implemented**:
```python
# Projected range (empirical)
Rp = a * (E ** b) / (M_ion ** c)

# Concentration profile
N(x) = (Dose / (sqrt(2*pi) * straggle)) * 
       exp(-(x - Rp)**2 / (2 * straggle**2))

# Junction depth (where N = substrate doping)
x_j: N(x_j) = N_substrate
```

Run the simulation to visualize implant profiles!

## Summary

Ion implantation has enabled the semiconductor industry to achieve:

**Key Capabilities**:
1. **Dose control**: ±1-2% precision
2. **Depth control**: Predictable from energy
3. **Abrupt junctions**: <5 nm/decade (with proper annealing)
4. **Reproducibility**: Excellent batch-to-batch
5. **Flexibility**: Any dopant, any substrate

**Critical Parameters**:
```
Ion Species → Determines dopant type
Energy → Controls depth (Rp)
Dose → Controls concentration (N_peak)
Tilt/Twist → Prevents channeling
Anneal → Activates dopants, repairs damage
```

**Technology Evolution**:
- 1960s-1970s: Introduction, replaces diffusion for S/D
- 1980s-1990s: Wells, Vth adjust, high-energy
- 2000s-2010s: Ultra-shallow (<50nm), PAI, halo implants
- 2010s-2020s: FinFETs (plasma doping, conformal), flash anneal
- 2020s-future: 3D structures, atomic-scale control

**Challenges Ahead**:
- Sub-10nm junctions (atoms counting regime)
- 3D device architectures (GAA, CFET)
- Novel materials (Ge, III-V channels)
- Dopant activation limits at low temperatures

Ion implantation remains indispensable for CMOS manufacturing, evolving to meet the demands of advanced nodes and new device architectures.

---

## Further Reading

### Textbooks
1. **"Ion Implantation: Science and Technology"** - Ziegler, J.F.
2. **"Ion Implantation and Beam Processing"** - Williams, J.S.
3. **"The Stopping and Range of Ions in Matter" (SRIM)** - Ziegler software/manual

### Papers
1. "Transient enhanced diffusion" - *J. Appl. Phys.*, 1996
2. "Ultra-shallow junction formation" - *Mater. Sci. Eng. R*, 2006
3. "Flash lamp annealing" - *Appl. Phys. Lett.*, 2014

### Standards
- **SEMI MF374**: Resistivity measurement
- **SEMI MF673**: Implant dose uniformity
- **ASTM F1378**: SIMS depth profiling

### Software Tools
- **SRIM/TRIM**: Monte Carlo implant simulation (free)
- **Sentaurus Process**: Commercial TCAD
- **Athena (Silvaco)**: Process simulation

---

**Next Chapter**: [Gate Stack Formation](gate-stack.md) - Dielectrics and electrode materials

**Document Version**: 1.0  
**Last Updated**: November 2025  
**Contributors**: Silicon Fabrication Handbook Team
