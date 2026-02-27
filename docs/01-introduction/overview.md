# Introduction to Silicon Fabrication

## Table of Contents
- [Overview](#overview)
- [Why Silicon?](#why-silicon)
  - [Material Properties](#material-properties)
- [Silicon Wafer Basics](#silicon-wafer-basics)
  - [Wafer Sizes](#wafer-sizes)
  - [Crystal Structure](#crystal-structure)
  - [Crystal Growth: Czochralski Process](#crystal-growth-czochralski-process)
  - [Wafer Doping](#wafer-doping)
- [The Cleanroom Environment](#the-cleanroom-environment)
  - [Why Cleanrooms?](#why-cleanrooms)
  - [ISO Cleanroom Classes](#iso-cleanroom-classes)
  - [Cleanroom Protocols](#cleanroom-protocols)
- [Fabrication Process Categories](#fabrication-process-categories)
  - [Front-End-Of-Line (FEOL)](#front-end-of-line-feol)
  - [Back-End-Of-Line (BEOL)](#back-end-of-line-beol)
  - [MEMS-Specific Processes](#mems-specific-processes)
- [Typical Process Flows](#typical-process-flows)
  - [CMOS Transistor (Simplified)](#cmos-transistor-simplified)
  - [MEMS Accelerometer (Surface Micromachining)](#mems-accelerometer-surface-micromachining)
- [Key Fabrication Technologies](#key-fabrication-technologies)
  - [Lithography](#lithography)
  - [Etching](#etching)
  - [Deposition](#deposition)
  - [Doping](#doping)
- [Process Integration Challenges](#process-integration-challenges)
  - [Thermal Budget](#thermal-budget)
  - [Film Stress](#film-stress)
  - [Contamination Control](#contamination-control)
- [Design Rules and Constraints](#design-rules-and-constraints)
  - [Minimum Feature Sizes](#minimum-feature-sizes)
  - [MEMS Design Considerations](#mems-design-considerations)
- [Cost and Economics](#cost-and-economics)
  - [Wafer Cost Breakdown](#wafer-cost-breakdown)
  - [Moore's Law Economics](#moores-law-economics)
- [Safety Considerations](#safety-considerations)
- [Next Steps](#next-steps)
- [Further Reading](#further-reading)

## Overview

Silicon fabrication is the process of creating integrated circuits (ICs) and microelectromechanical systems (MEMS) on silicon wafers through a series of highly controlled chemical and physical processes. This handbook covers both **CMOS (Complementary Metal-Oxide-Semiconductor)** technology for electronics and **MEMS** devices for sensing and actuation.

## Why Silicon?

Silicon has become the dominant semiconductor material for several key reasons:

1. **Abundant Material**: Second most abundant element in Earth's crust (after oxygen)
2. **Native Oxide**: Forms high-quality SiO₂ at the surface, essential for MOSFET gates
3. **Band Gap**: 1.12 eV at 300K - ideal for room temperature operation
4. **Mechanical Properties**: Excellent for MEMS (comparable strength to steel at microscale)
5. **Mature Technology**: Decades of process development and infrastructure

### Material Properties

| Property | Value | Units |
|----------|-------|-------|
| Lattice Constant | 5.431 | Å |
| Density | 2.329 | g/cm³ |
| Melting Point | 1414 | °C |
| Thermal Conductivity | 148 | W/(m·K) |
| Young's Modulus | 130-180 | GPa |
| Dielectric Constant | 11.7 | - |

## Silicon Wafer Basics

### Wafer Sizes

Modern fabrication uses standardized wafer diameters:

- **100mm (4")** - Research and legacy production
- **150mm (6")** - MEMS, power devices
- **200mm (8")** - Mature nodes, analog ICs
- **300mm (12")** - Advanced CMOS (7nm-90nm)
- **450mm (18")** - Future technology (under development)

**Economic Driver**: Larger wafers = more dies per wafer = lower cost per die

### Crystal Structure

Silicon wafers are single-crystal material with specific orientations:

- **<100> Wafers**: Most common for CMOS (better oxide quality)
- **<110> Wafers**: Used for specific MEMS applications
- **<111> Wafers**: Anisotropic wet etching (KOH)

### Crystal Growth: Czochralski Process

```
Polysilicon → Melt (1414°C) → Seed Crystal → Pull & Rotate → 
Cylindrical Ingot → Wire Saw → Individual Wafers → Polish
```

**Key Parameters**:
- Pull rate: 50-200 mm/hr
- Rotation: 10-20 RPM
- Oxygen content: 10¹⁷-10¹⁸ atoms/cm³ (from quartz crucible)

### Wafer Doping

Silicon is doped to control electrical conductivity:

**P-Type (Acceptor)**:
- Dopant: Boron (B), Gallium (Ga)
- Creates "holes" as majority carriers
- Typical concentration: 10¹⁵ atoms/cm³

**N-Type (Donor)**:
- Dopant: Phosphorus (P), Arsenic (As), Antimony (Sb)
- Creates electrons as majority carriers
- Typical concentration: 10¹⁵ atoms/cm³

## The Cleanroom Environment

### Why Cleanrooms?

Particle contamination is the #1 cause of yield loss. A single dust particle (>0.5μm) can:
- Short circuit metal lines
- Create defects in gate oxide
- Block lithography patterns
- Damage MEMS structures

### ISO Cleanroom Classes

| ISO Class | Particles/m³ (≥0.5μm) | Application |
|-----------|----------------------|-------------|
| ISO 3 | 35 | Critical lithography |
| ISO 4 | 352 | Advanced CMOS fab |
| ISO 5 | 3,520 | Standard IC production |
| ISO 6 | 35,200 | Packaging, testing |

**Comparison**: Normal room air is ~35 million particles/m³ (ISO 9)

### Cleanroom Protocols

1. **Gowning**: Full-body suits, gloves, masks, shoe covers
2. **Air Flow**: HEPA-filtered, laminar flow (ceiling to floor)
3. **Pressure**: Positive pressure to prevent contamination ingress
4. **Temperature**: 20-22°C (±0.5°C stability)
5. **Humidity**: 40-45% RH (±2% control)
6. **Electrostatic Discharge (ESD)**: Grounded surfaces, ionizers

## Fabrication Process Categories

### Front-End-Of-Line (FEOL)

Processes that create active devices on the wafer:
- Oxidation and cleaning
- Lithography
- Etching
- Doping (ion implantation, diffusion)
- Deposition (CVD, PVD)
- Gate stack formation
- Source/drain creation

### Back-End-Of-Line (BEOL)

Processes that create interconnects:
- Metallization (Cu or Al)
- Dielectric deposition
- Chemical-mechanical polishing (CMP)
- Via and trench filling
- Passivation

### MEMS-Specific Processes

- Deep reactive ion etching (DRIE)
- Wafer bonding (anodic, fusion, eutectic)
- Sacrificial layer release
- Critical point drying
- Anti-stiction coatings

## Typical Process Flows

### CMOS Transistor (Simplified)

```
1. Start: P-type <100> wafer
2. STI (Shallow Trench Isolation) formation
3. Gate oxide growth (thermal oxidation)
4. Polysilicon gate deposition
5. Gate patterning (lithography + etch)
6. Source/drain implants (n+ for NMOS, p+ for PMOS)
7. Dopant activation anneal
8. Silicide formation (reduce contact resistance)
9. BEOL: ILD, contacts, M1-M8 interconnects
10. Passivation and pad opening
```

### MEMS Accelerometer (Surface Micromachining)

```
1. Start: Silicon wafer
2. Thermal oxide (sacrificial layer 1)
3. PSG deposition (sacrificial layer 2)
4. Structural poly-Si deposition (2-3μm)
5. Pattern proof mass and comb fingers
6. Metallization for electrical contact
7. HF release etch (remove sacrificial oxide)
8. Critical point dry
9. Anti-stiction coating (SAM)
10. Wafer-level packaging
```

## Key Fabrication Technologies

### Lithography

The pattern transfer process:
- **Photolithography**: UV light through masks (DUV 193nm, EUV 13.5nm)
- **Resolution**: λ/NA (wavelength / numerical aperture)
- **State-of-art**: 3nm node uses EUV multi-patterning

### Etching

Material removal:
- **Wet Etch**: Chemical solutions (isotropic, high selectivity)
- **Dry Etch**: Plasma-based (anisotropic, precise)
- **DRIE**: Bosch process for high aspect ratio MEMS

### Deposition

Adding material layers:
- **CVD**: Chemical vapor deposition (SiO₂, Si₃N₄, poly-Si)
- **PVD**: Physical vapor deposition (sputtering for metals)
- **ALD**: Atomic layer deposition (conformal, ultra-thin)

### Doping

Adding impurities:
- **Ion Implantation**: Accelerate dopants into silicon (keV-MeV)
- **Diffusion**: Thermal drive-in at high temperature
- **Epitaxy**: Grow doped single-crystal layers

## Process Integration Challenges

### Thermal Budget

Each high-temperature step causes dopant diffusion:
- Modern processes use **low-temperature** approaches
- **Rapid thermal anneal (RTA)**: 1000°C for <1 second

### Film Stress

Deposited films have intrinsic stress:
- **Tensile stress**: Film wants to expand (can curl wafers)
- **Compressive stress**: Film wants to contract
- **MEMS**: Must carefully balance stress for suspended structures

### Contamination Control

Critical elements to avoid:
- **Alkali metals** (Na, K): Cause device instability
- **Heavy metals** (Fe, Cu, Au): Create traps in bandgap
- **Particles**: Physical defects

## Design Rules and Constraints

### Minimum Feature Sizes

| Technology Node | Gate Length | Metal Pitch | Application |
|-----------------|-------------|-------------|-------------|
| 180nm | 180nm | 450nm | Automotive, IoT |
| 90nm | 90nm | 220nm | Displays, power |
| 28nm | 28nm | 90nm | Mobile SoCs |
| 7nm | 7nm | 36nm | High-end CPUs |
| 3nm | 3nm | 24nm | Leading edge |

### MEMS Design Considerations

- **Etch holes**: Required for sacrificial release (typically 2-5μm squares)
- **Anchor points**: Structural connections to substrate
- **Gap spacing**: Minimum 1-2μm to prevent stiction
- **Aspect ratio**: DRIE can achieve 30:1 (depth:width)

## Cost and Economics

### Wafer Cost Breakdown

For a modern 300mm fab:
- **Capital equipment**: $3-15 billion (entire fab)
- **Raw wafer**: $50-200 each
- **Processing cost**: $1000-5000 per wafer (depending on complexity)
- **Yield**: 70-95% for mature processes

### Moore's Law Economics

**Observation**: Transistor density doubles every ~2 years

**Reality Today**: 
- Physical scaling slowing down
- Cost per transistor no longer decreasing at 7nm and below
- Focus shifting to chiplet architectures and 3D integration

## Safety Considerations

Semiconductor fabs use hazardous materials:

**Toxic Gases**: AsH₃ (arsine), PH₃ (phosphine), SiH₄ (silane)
**Acids**: HF (hydrofluoric acid), H₂SO₄ (sulfuric acid)
**Solvents**: Acetone, isopropanol, photoresist thinners

**Safety Systems**:
- Gas detection and auto-shutoff
- Scrubbers for exhaust treatment
- Emergency showers and eyewash stations
- Continuous monitoring

## Next Steps

This introduction provides the foundation for understanding silicon fabrication. The following chapters dive deep into specific processes:

- **Chapter 2**: CMOS FEOL - How transistors are built
- **Chapter 3**: CMOS BEOL - Creating the interconnect network
- **Chapter 4**: MEMS Surface Micromachining - Polysilicon structures
- **Chapter 5**: MEMS Bulk Micromachining - Silicon etching techniques

## Further Reading

1. "VLSI Fabrication Principles" - Ghandhi
2. "Semiconductor Manufacturing Handbook" - Quirk & Serda
3. "Fundamentals of Microfabrication" - Madou
4. IEEE/SEMI standards documents

---

**Ready to proceed?** Start with [Chapter 2: CMOS FEOL](../02-cmos-feol/)
