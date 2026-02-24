# CMOS Front-End-Of-Line (FEOL) Processes

## Table of Contents
- [Introduction](#introduction)
- [MOSFET Fundamentals](#mosfet-fundamentals)
  - [Device Structure](#device-structure)
  - [Operating Principle](#operating-principle)
  - [Key Electrical Parameters](#key-electrical-parameters)
- [Complete FEOL Process Flow](#complete-feol-process-flow)
  - [Step 1: Wafer Preparation and Cleaning](#step-1-wafer-preparation-and-cleaning)
  - [Step 2: Shallow Trench Isolation (STI)](#step-2-shallow-trench-isolation-sti)
  - [Step 3: Well Formation (N-Well and P-Well)](#step-3-well-formation-n-well-and-p-well)
  - [Step 4: Threshold Voltage Adjustment](#step-4-threshold-voltage-adjustment)
  - [Step 5: Gate Oxide Growth](#step-5-gate-oxide-growth)
  - [Step 6: Poly-Silicon Gate Deposition](#step-6-poly-silicon-gate-deposition)
  - [Step 7: Gate Patterning](#step-7-gate-patterning)
  - [Step 8: Lightly Doped Drain (LDD) Formation](#step-8-lightly-doped-drain-ldd-formation)
  - [Step 9: Spacer Formation](#step-9-spacer-formation)
  - [Step 10: Source/Drain Implantation](#step-10-sourcedrain-implantation)
  - [Step 11: Rapid Thermal Anneal (RTA)](#step-11-rapid-thermal-anneal-rta)
  - [Step 12: Silicide Formation (Salicide Process)](#step-12-silicide-formation-salicide-process)
  - [Step 13: Contact Oxide and Pre-Metal Dielectric (PMD)](#step-13-contact-oxide-and-pre-metal-dielectric-pmd)
- [Advanced FEOL Technologies](#advanced-feol-technologies)
  - [FinFET (14nm and below)](#finfet-14nm-and-below)
  - [Strain Engineering](#strain-engineering)
  - [High-κ Metal Gate (HKMG)](#high-κ-metal-gate-hkmg)
- [FEOL Characterization and Metrology](#feol-characterization-and-metrology)
  - [Electrical Testing](#electrical-testing)
  - [Physical Characterization](#physical-characterization)
- [Yield and Defect Control](#yield-and-defect-control)
  - [Common FEOL Defects](#common-feol-defects)
  - [Statistical Process Control (SPC)](#statistical-process-control-spc)
- [Summary](#summary)


## Introduction

FEOL encompasses all fabrication steps that create the active transistor devices on a silicon wafer, from the bare substrate to the completed transistors before metallization. This chapter covers the fundamental processes for creating CMOS (Complementary Metal-Oxide-Semiconductor) transistors.

## MOSFET Fundamentals

### Device Structure

A MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) consists of:

```
       Gate (Poly-Si or Metal)
              |
      --------+---------
      |   Gate Oxide   |  (SiO₂, 1-10nm)
------|----------------|-------
|  S  |   Channel     |  D   |  Silicon substrate
| n+  | (p-type/n)    | n+   |
|     |               |      |
```

**Key Components**:
- **Source (S)**: Electron injection point (for NMOS)
- **Drain (D)**: Electron collection point
- **Gate**: Controls channel conductivity
- **Gate Oxide**: Insulator between gate and channel
- **Channel**: Conductive path formed by gate voltage

### Operating Principle

**NMOS Transistor**:
1. Substrate: P-type silicon
2. Source/Drain: N+ heavily doped regions
3. **OFF State** (Vgs < Vth): No channel, transistor blocks current
4. **ON State** (Vgs > Vth): Inversion layer forms, current flows S→D

**PMOS Transistor**: Opposite polarity (N-substrate, P+ S/D)

**CMOS Advantage**: Zero static power consumption (one transistor always OFF)

### Key Electrical Parameters

| Parameter | Symbol | Typical Value | Notes |
|-----------|--------|---------------|-------|
| Threshold Voltage | Vth | 0.3-0.7V | Voltage to turn ON |
| Gate Oxide Thickness | tox | 1.2-2.5nm | 7nm-28nm nodes |
| Channel Length | L | 7-180nm | Technology node |
| Drain Current | Id | 500-1000 μA/μm | At Vds=Vdd |
| Subthreshold Slope | SS | 70-90 mV/dec | Switching speed |

## Complete FEOL Process Flow

### Step 1: Wafer Preparation and Cleaning

**Starting Material**: 
- 300mm diameter, <100> orientation
- P-type, 10¹⁵ cm⁻³ doping (for NMOS regions)
- Or N-type for PMOS regions

**RCA Clean Process**:
```
SC-1: NH₄OH:H₂O₂:H₂O (1:1:5), 75°C, 10 min
      → Removes organic contaminants and particles

HF Dip: Dilute HF (1-2%), room temp, 30 sec
        → Strips native oxide

SC-2: HCl:H₂O₂:H₂O (1:1:5), 75°C, 10 min
      → Removes metallic contaminants
```

**Result**: Atomically clean, hydrophobic silicon surface

### Step 2: Shallow Trench Isolation (STI)

**Purpose**: Electrically isolate adjacent transistors

**Process Sequence**:

1. **Pad Oxide Growth**: 10nm thermal SiO₂ (stress buffer)
2. **Nitride Deposition**: 100nm Si₃N₄ by LPCVD (hard mask)
3. **Lithography**: Pattern trench locations
4. **Reactive Ion Etch (RIE)**: Etch Si₃N₄ + Si to depth of 300-500nm
5. **Trench Oxidation**: Grow thin liner oxide (seal sidewalls)
6. **Gap Fill**: Deposit thick oxide by HDP-CVD or SACVD
7. **CMP (Chemical-Mechanical Polish)**: Planarize to nitride layer
8. **Nitride Strip**: Hot H₃PO₄ removes Si₃N₄

**Cross-Section**:
```
    |-------|         |-------|
    |  Si₃N₄|         |  Si₃N₄|
----|-------|---------|-------|----- Pad Oxide
|           |  STI    |           |
|   Active  |  Oxide  |  Active   | Silicon
|   Area    |         |   Area    |
```

**Critical Parameters**:
- Trench width: 0.2-1.0μm
- Trench depth: 300-500nm
- Corner rounding: Avoid sharp edges (field concentration)

### Step 3: Well Formation (N-Well and P-Well)

**Purpose**: Create regions for NMOS (in P-well) and PMOS (in N-well)

**Twin-Well Process**:

1. **N-Well Formation**:
   - Mask: Protect NMOS regions
   - Implant: Phosphorus (P), 200-400keV, dose 5×10¹³ cm⁻²
   - Profile: Deep well extending 2-3μm

2. **P-Well Formation**:
   - Mask: Protect PMOS regions
   - Implant: Boron (B), 150-300keV, dose 5×10¹³ cm⁻²

3. **Drive-In Anneal**: 1000-1100°C, 2-4 hours in N₂
   - Activates dopants
   - Diffuses wells to target depth

**Doping Profile**:
```
Concentration
     |     /\  (P-well)
     |    /  \
10¹⁷ |   /    \____
     |  /          ----___
10¹⁵ | /                  ----____
     |/__________________________
     0    1    2    3    4   Depth(μm)
```

### Step 4: Threshold Voltage Adjustment

**Purpose**: Fine-tune Vth for NMOS and PMOS independently

**Channel Implants**:
- **NMOS**: Boron implant, 20-80keV, dose 1-5×10¹² cm⁻²
  - Increases Vth (adds P-type dopant to channel)
- **PMOS**: Phosphorus implant, 40-100keV, dose 1-3×10¹² cm⁻²
  - Increases |Vth| for PMOS

**Result**: Vth,NMOS ≈ +0.4V, Vth,PMOS ≈ -0.45V

### Step 5: Gate Oxide Growth

**Critical Layer**: Determines transistor performance and reliability

**Thermal Oxidation Process**:

**Dry Oxidation** (for high-quality thin oxide):
```
Si + O₂ → SiO₂
Temperature: 800-1000°C
Ambient: Pure O₂
Growth rate: 10-30nm/hour
Thickness: 1.2-3.0nm
```

**Deal-Grove Model** (oxide growth kinetics):
```
x²ₒₓ + Axₒₓ = B(t + τ)

Where:
x = oxide thickness
t = time
A, B = constants (temperature dependent)
τ = initial condition correction
```

**For Modern Nodes (≤28nm)**:
- **High-κ Dielectrics**: HfO₂ (κ≈25) replaces SiO₂ (κ=3.9)
- **Equivalent Oxide Thickness (EOT)**: 0.8-1.5nm
- **Deposition**: Atomic Layer Deposition (ALD)

**Quality Metrics**:
- Breakdown field: >10 MV/cm
- Interface trap density: <10¹⁰ cm⁻² eV⁻¹
- Leakage current: <1 A/cm² at operating voltage

### Step 6: Poly-Silicon Gate Deposition

**Purpose**: Form the gate electrode

**LPCVD Poly-Silicon**:
```
SiH₄ → Si + 2H₂
Temperature: 580-650°C
Pressure: 200-400 mTorr
Thickness: 100-200nm
Grain size: 30-100nm
```

**Properties**:
- As-deposited: Resistivity ~10³ Ω·cm (too high)
- After doping: Resistivity ~500 μΩ·cm (low enough)

**Gate Doping**:
- **NMOS Gate**: N+ doped (POCl₃ diffusion or implant)
- **PMOS Gate**: P+ doped (Boron implant)
- **Dual Work Function**: Match gate material to channel type

**Modern Alternative - Metal Gates**:
- TiN, TaN for high-κ dielectrics
- Better performance at advanced nodes
- Part of "high-κ metal gate" (HKMG) stack

### Step 7: Gate Patterning

**Critical Dimension**: Gate length defines transistor performance

**Lithography**:
1. **Photoresist Coating**: Spin coat, 200-300nm thick
2. **Soft Bake**: 90-120°C, remove solvent
3. **Exposure**: 
   - 193nm DUV (ArF excimer laser)
   - EUV (13.5nm) for advanced nodes
   - Immersion lithography (water, NA=1.35)
4. **Post-Exposure Bake**: 110-130°C
5. **Develop**: TMAH-based developer
6. **Hard Bake**: 120-150°C

**Optical Proximity Correction (OPC)**:
- Add sub-resolution features to mask
- Compensate for diffraction effects
- Ensure printed gate length = design target

**Plasma Etch**:
```
Chemistry: Cl₂/HBr/O₂ plasma
Pressure: 5-20 mTorr
RF Power: 500-1500W
Etch rate: 100-300nm/min
Selectivity: >50:1 (Poly:Oxide)
```

**Result**: Precisely defined gate length (7nm to 180nm depending on node)

### Step 8: Lightly Doped Drain (LDD) Formation

**Purpose**: Reduce hot carrier effects and prevent junction breakdown

**Problem with Abrupt Junctions**:
- High electric field at drain edge
- Hot carriers damage gate oxide
- Reduced reliability

**Solution - LDD Structure**:

1. **N-LDD Implant** (for NMOS):
   - Mask: Cover PMOS
   - Species: Phosphorus or Arsenic
   - Energy: 5-20keV (shallow)
   - Dose: 1-5×10¹³ cm⁻²

2. **P-LDD Implant** (for PMOS):
   - Mask: Cover NMOS
   - Species: BF₂ (boron with mass)
   - Energy: 5-15keV
   - Dose: 1-3×10¹³ cm⁻²

**Cross-Section After LDD**:
```
        |-- Gate --|
        |          |
--------|          |--------
    n-  |          |  n-     (LDD regions)
        |          |
        |----------|
```

### Step 9: Spacer Formation

**Purpose**: Offset heavy S/D implants from gate edge

**Process**:

1. **Oxide Deposition**: 
   - LPCVD or PECVD SiO₂, 40-80nm conformal
2. **Nitride Deposition**: 
   - LPCVD Si₃N₄, 40-80nm conformal
3. **Anisotropic Etch**: 
   - RIE, vertical etch only
   - Leaves spacers on gate sidewalls

**Resulting Structure**:
```
         |--- Gate ---|
         |            |
---------|            |---------
     |  ||            ||  |
   n-|  ||            ||  |n-    Spacers prevent heavy
     |  ||            ||  |      implant near gate edge
     |  ||____________||  |
```

**Spacer Width**: 30-100nm (controls LDD extent)

### Step 10: Source/Drain Implantation

**Purpose**: Create heavily doped S/D regions for low contact resistance

**N+ Implant** (NMOS S/D):
- Mask: Cover PMOS
- Species: Arsenic (As) preferred over P (less diffusion)
- Energy: 20-80keV
- Dose: 3-8×10¹⁵ cm⁻²
- Result: n+ concentration ~10²⁰ cm⁻³

**P+ Implant** (PMOS S/D):
- Mask: Cover NMOS
- Species: Boron (B) or BF₂
- Energy: 5-30keV
- Dose: 2-6×10¹⁵ cm⁻²
- Result: p+ concentration ~10²⁰ cm⁻³

**As-Implanted Profile**:
- Amorphous silicon (damaged lattice)
- Dopants not electrically active
- Requires activation anneal

### Step 11: Rapid Thermal Anneal (RTA)

**Purpose**: Activate dopants and repair crystal damage

**Process**:
```
Temperature: 950-1050°C
Ramp rate: 50-200°C/sec
Hold time: 1-10 seconds
Ambient: N₂ or forming gas (N₂/H₂)
```

**Spike Anneal**:
- Peak temperature reached and immediately cool
- Minimizes dopant diffusion
- Preserves shallow junctions

**Physics**:
1. **Dopant Activation**: Dopants move to substitutional sites
   - As → As⁺ (donates electron)
   - B → B⁻ (accepts electron)
2. **Defect Annealing**: Repair ion implant damage
3. **Minimize Diffusion**: Short time at temperature

**Result**: 
- Dopant activation: >95%
- Junction depth: 20-100nm (depending on node)
- Sheet resistance: 50-200 Ω/square

### Step 12: Silicide Formation (Salicide Process)

**Purpose**: Reduce S/D and gate contact resistance

**Self-Aligned Silicide (Salicide)**:

1. **Metal Deposition**:
   - Cobalt (Co) for ≥28nm: CoSi₂ forms at 600-800°C
   - Nickel (Ni) for <28nm: NiSi forms at 400-500°C
   - Thickness: 10-30nm

2. **First RTA**:
   - 400-550°C, 30 sec
   - Forms metal-rich silicide (Co₂Si or Ni₂Si)

3. **Selective Etch**:
   - Remove unreacted metal from oxide/nitride surfaces
   - Leaves silicide only on Si surfaces (self-aligned)

4. **Second RTA**:
   - 650-850°C, 30 sec
   - Converts to low-resistivity phase (CoSi₂ or NiSi)

**Reaction**:
```
2Co + Si → Co₂Si (First RTA, 400°C)
Co₂Si + Si → 2CoSi₂ (Second RTA, 800°C)

Or for Nickel:
Ni + Si → NiSi (400-500°C)
```

**Resistivity**:
- CoSi₂: 10-20 μΩ·cm
- NiSi: 14-18 μΩ·cm
- Compare to poly-Si: 500 μΩ·cm

**Cross-Section After Silicide**:
```
      |--Silicide--|
      |--- Gate ---|
      |            |
------SiSi--------SiSi------
    n+ |            | n+
       |            |
```

### Step 13: Contact Oxide and Pre-Metal Dielectric (PMD)

**Purpose**: Insulate transistors before metal interconnects

**Process**:

1. **PMD Deposition**:
   - Material: USG (undoped silicate glass) or PSG
   - Method: PECVD or HDP-CVD
   - Thickness: 300-600nm

2. **Chemical-Mechanical Polishing (CMP)**:
   - Planarize surface
   - Remove topography from gates
   - Roughness: <5nm RMS

**Planarization Importance**:
- Lithography depth of focus
- Uniform metal deposition
- Reliable contacts

## Advanced FEOL Technologies

### FinFET (14nm and below)

**3D Transistor Structure**:
```
     |--Gate--|         (Gate wraps around fin)
    /|        |\
   / |        | \
  /  |   Fin  |  \
 /   |        |   \
/    |        |    \
-----S--------D----- (Source and Drain)
```

**Advantages**:
- Better gate control (3 sides vs. 1)
- Reduced short-channel effects
- Lower leakage current
- Steeper subthreshold slope

**Fabrication Differences**:
- Sidewall Image Transfer (SIT) lithography
- Fin patterning by RIE
- Fin width: 5-10nm
- Fin height: 30-50nm

### Strain Engineering

**Purpose**: Enhance carrier mobility

**Techniques**:

1. **SiGe Source/Drain** (for PMOS):
   - Replace Si with SiₓGe₁₋ₓ (x=0.7-0.8)
   - Larger lattice constant induces compressive strain in channel
   - Hole mobility increase: 30-50%

2. **Embedded SiC Source/Drain** (for NMOS):
   - SiₓC₁₋ₓ (x=0.98-0.99)
   - Smaller lattice constant induces tensile strain
   - Electron mobility increase: 20-30%

3. **Stress Liners**:
   - Tensile Si₃N₄ film over NMOS
   - Compressive Si₃N₄ film over PMOS

### High-κ Metal Gate (HKMG)

**Gate Stack for ≤28nm**:
```
Metal Gate (TiN/TaN)
HfO₂ (4-6nm physical, 1.0nm EOT)
IL (Interfacial Layer, SiO₂, 0.5nm)
Silicon Channel
```

**Benefits**:
- Reduced gate leakage (10³-10⁴× vs. SiO₂)
- Lower EOT (scaled capacitance)
- Reduced polysilicon depletion effect

## FEOL Characterization and Metrology

### Electrical Testing

**Parameters Measured**:
1. **Threshold Voltage (Vth)**: Gate voltage at threshold of inversion
2. **Drive Current (Idsat)**: Maximum drain current at Vgs=Vds=Vdd
3. **Subthreshold Slope (SS)**: ∂Vgs/∂(log Id)
4. **Off-State Leakage (Ioff)**: Drain current when Vgs=0V
5. **Gate Leakage (Ig)**: Current through gate oxide

**Test Structures**:
- Long-channel transistors (L=10μm)
- Ring oscillators (speed metric)
- Kelvin resistor structures (sheet resistance)

### Physical Characterization

**Techniques**:
1. **SEM (Scanning Electron Microscopy)**: CD measurement, profile
2. **TEM (Transmission Electron Microscopy)**: Oxide thickness, crystal structure
3. **AFM (Atomic Force Microscopy)**: Surface roughness
4. **SIMS (Secondary Ion Mass Spectrometry)**: Dopant profiles
5. **Ellipsometry**: Film thickness (non-destructive)
6. **XRD (X-Ray Diffraction)**: Crystal strain measurement

## Yield and Defect Control

### Common FEOL Defects

1. **Gate Oxide Pinholes**: Cause gate leakage or shorts
2. **Poly Stringers**: Residual poly-Si after etch
3. **Silicide Spiking**: Silicide penetrates shallow junction
4. **Well Proximity Effects**: Doping variations near boundaries
5. **STI Stress**: Can crack adjacent gates

### Statistical Process Control (SPC)

**Monitored Parameters**:
- Oxide thickness: Target ±0.1nm
- Gate CD: Target ±3%
- Sheet resistance: Target ±5%
- Vth distribution: σ < 30mV

**Control Charts**: Track process drift before yield impact

## Summary

FEOL creates the active devices:
- **Isolation**: STI trenches separate transistors
- **Wells**: Define NMOS and PMOS regions
- **Gate Stack**: Oxide + poly-Si (or HKMG)
- **Doping**: LDD and S/D implants
- **Silicide**: Low-resistance contacts

**Next**: Chapter 3 covers BEOL - the metal interconnect layers that connect transistors into functional circuits.

---

**Key Takeaway**: FEOL requires atomic-level precision. A 1nm variation in gate oxide or 10nm shift in dopant profile can destroy transistor performance.
