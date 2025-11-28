# Damascene Process

## Table of Contents
- [Introduction](#introduction)
- [Historical Context](#historical-context)
- [Process Overview](#process-overview)
- [Single Damascene Process](#single-damascene-process)
- [Dual Damascene Process](#dual-damascene-process)
- [Key Process Steps](#key-process-steps)
- [Barrier and Seed Layer Deposition](#barrier-and-seed-layer-deposition)
- [Copper Electroplating](#copper-electroplating)
- [Chemical Mechanical Polishing](#chemical-mechanical-polishing)
- [Process Variations](#process-variations)
- [Design Considerations](#design-considerations)
- [Challenges and Solutions](#challenges-and-solutions)
- [Advanced Topics](#advanced-topics)
- [Metrology and Characterization](#metrology-and-characterization)
- [Further Reading](#further-reading)

---

## Introduction

The **damascene process** is a revolutionary metallization technique that enabled the transition from aluminum to copper interconnects in advanced semiconductor manufacturing. Named after the ancient art of Damascus metalworking, this subtractive patterning approach fundamentally changed how metal lines and vias are formed in integrated circuits.

### Why Damascene?

Traditional metal patterning involves:
1. Deposit metal film
2. Pattern photoresist
3. Etch metal
4. Strip resist

**Problem with Copper**: Copper cannot be easily dry-etched due to:
- Non-volatile copper halides (CuCl₂, CuF₂)
- Poor anisotropy in plasma etching
- Contamination issues
- Difficult residue removal

**Damascene Solution**: Reverse the process order:
1. Pattern and etch dielectric
2. Deposit barrier/seed layers
3. Fill trenches with copper
4. Polish away excess copper

This "dig first, fill later" approach perfectly suits copper's superior electrical properties while avoiding its etching limitations.

### Key Advantages

| Aspect | Advantage |
|--------|-----------|
| **Electrical** | Lower resistance (Cu: 1.7 µΩ·cm vs Al: 2.7 µΩ·cm) |
| **Reliability** | Better electromigration resistance |
| **Performance** | Higher current density capability |
| **Scaling** | Enables smaller feature sizes |
| **Process** | Fewer lithography steps (dual damascene) |
| **Gap Fill** | Excellent conformality with electroplating |

### Applications

- **Logic ICs**: Microprocessors (Intel, AMD, Apple)
- **Memory**: DRAM, Flash, SRAM
- **Analog/RF**: High-frequency circuits
- **Advanced Nodes**: 7nm and below require damascene Cu

---

## Historical Context

### The Copper Transition

**Pre-1997**: Aluminum interconnects dominated
- Easy to etch and pattern
- Adequate for feature sizes > 0.5 µm
- Mature manufacturing processes

**1997**: IBM introduces copper damascene
- First commercial implementation at 0.25 µm
- Demonstrated 35% speed improvement
- Established new industry standard

**2000s**: Industry-wide adoption
- Intel transitions to Cu (180nm, 2001)
- TSMC, Samsung, others follow
- Damascene becomes standard for advanced nodes

### The Damascus Connection

The process is named after **Damascus steel**, famous for its:
- Intricate surface patterns
- Inlaid gold/silver decoration
- Superior mechanical properties

Similarly, damascene metallization creates:
- Intricate interconnect patterns
- Inlaid copper in dielectric
- Superior electrical properties

---

## Process Overview

### Single vs. Dual Damascene

```
SINGLE DAMASCENE (Via-First)
═══════════════════════════════
Step 1: Etch via
┌─────────────────┐
│    Dielectric   │
│       ╔═╗       │  ← Via hole
│    ───╚═╝───    │  ← Metal line
└─────────────────┘

Step 2: Deposit barrier/seed
Step 3: Electroplate Cu
Step 4: CMP
┌─────────────────┐
│    Dielectric   │
│       ║█║       │  ← Cu-filled via
│    ───╚█╝───    │
└─────────────────┘

Repeat for trench...


DUAL DAMASCENE (Combined)
═══════════════════════════════
Step 1: Etch via and trench
┌─────────────────┐
│  ╔═══════════╗  │  ← Trench
│  ║     ╔═╗   ║  │  ← Via
│  ╚═════╚═╝═══╝  │
│    ───────────  │
└─────────────────┘

Step 2: Deposit barrier/seed
Step 3: Electroplate Cu
Step 4: CMP
┌─────────────────┐
│  ╔███████████╗  │  ← Cu line
│  ║     ║█║   ║  │  ← Cu via
│  ╚═════╚█╝═══╝  │
│    ───────────  │
└─────────────────┘

ONE metallization cycle!
```

### Process Flow Comparison

| Feature | Single Damascene | Dual Damascene |
|---------|-----------------|----------------|
| **Cycles per Metal Layer** | 2 (via + line) | 1 (combined) |
| **Lithography Steps** | 2 | 2 or 3* |
| **CMP Steps** | 2 | 1 |
| **Barrier Layers** | 2 interfaces | 1 interface |
| **Throughput** | Lower | Higher |
| **Complexity** | Simple | Moderate |
| **Typical Use** | Early Cu nodes | Advanced nodes |

*Via-first dual damascene uses 2 litho steps; trench-first may need 3

---

## Single Damascene Process

### Via-First Single Damascene

**Step 1: Via Dielectric Deposition**
```
Material: SiO₂, FSG, or low-k dielectric
Thickness: 300-800 nm
Method: PECVD or spin-on
```

**Step 2: Via Lithography**
```
Process:
1. Apply photoresist (thickness: 500-800 nm)
2. Expose via pattern (i-line, DUV, or EUV)
3. Develop resist
4. Post-exposure bake (PEB)

Critical Dimension: 
- Via diameter: 0.2-0.5 µm (advanced nodes)
- Alignment tolerance: ±10-30 nm
```

**Step 3: Via Etch**
```
Etch Chemistry:
- Main etch: CF₄/CHF₃/Ar (for oxide)
- Overetch: CHF₃/CO (endpoint detection)
- Selectivity: >10:1 (oxide:resist)

Parameters:
- Pressure: 50-200 mTorr
- RF power: 500-1500 W
- DC bias: 300-800 V
- Aspect ratio: 1:1 to 3:1
```

**Step 4: Resist Strip and Clean**
```
Plasma ash: O₂ plasma (300-400°C)
Wet clean: Dilute HF (remove native oxide)
Pre-clean: Ar sputter (remove bottom residue)
```

**Step 5: Barrier/Seed Deposition**
```
Barrier Layer:
- Material: Ta, TaN, Ti/TiN
- Thickness: 5-20 nm
- Method: PVD or CVD
- Purpose: Prevent Cu diffusion, improve adhesion

Seed Layer:
- Material: Copper
- Thickness: 50-150 nm
- Method: PVD (sputtering)
- Purpose: Conduction path for electroplating
```

**Step 6: Copper Electroplating**
```
Electrolyte: CuSO₄ + H₂SO₄ + additives
Current density: 10-30 mA/cm²
Temperature: 20-25°C
Overplating: 10-30% (ensures complete fill)
```

**Step 7: CMP (Via Level)**
```
Stop layer: Dielectric surface
Removal rate: 200-400 nm/min
Uniformity: <5% variation
Dishing: <10 nm
```

**Repeat for Trench Level**:
Steps 1-7 repeated to form metal line connecting vias

---

## Dual Damascene Process

Dual damascene eliminates one CMP step by forming vias and trenches simultaneously. Three main approaches exist:

### Via-First Dual Damascene

**Most Common Approach** - Better via profile control

```
PROCESS FLOW:
═══════════════════════════════════════════════════

1. DIELECTRIC STACK DEPOSITION
┌─────────────────────────────┐
│    Trench Dielectric (ILD)  │ ← 500-800 nm
├─────────────────────────────┤
│         Etch Stop           │ ← 20-50 nm (SiN, SiC)
├─────────────────────────────┤
│     Via Dielectric (ILD)    │ ← 300-500 nm
├─────────────────────────────┤
│        Lower Metal          │
└─────────────────────────────┘


2. VIA LITHOGRAPHY AND ETCH
┌─────────────────────────────┐
│                             │
│            ╔═╗              │ ← Via etched through
│            ║ ║              │   via dielectric only
├────────────╚═╝──────────────┤ ← Etch stop
│                             │
├─────────────────────────────┤
│          ──────────          │
└─────────────────────────────┘

Via etch stops on etch stop layer!


3. TRENCH LITHOGRAPHY AND ETCH
┌─────────────────────────────┐
│      ╔═════════════╗        │ ← Trench pattern
│      ║     ╔═╗     ║        │
│      ║     ║ ║     ║        │
├──────╚═════╚═╝═════╝────────┤
│                             │
├─────────────────────────────┤
│          ──────────          │
└─────────────────────────────┘


4. ETCH STOP REMOVAL
┌─────────────────────────────┐
│      ╔═════════════╗        │
│      ║     ║█║     ║        │ ← Via now open
│      ║     ╚█╝     ║        │   to lower metal
│      ╚═════════════╝        │
├─────────────────────────────┤
│          ──█───────          │ ← Exposed metal
└─────────────────────────────┘


5. BARRIER/SEED/FILL/CMP
┌─────────────────────────────┐
│      ╔█████████████╗        │ ← Cu line
│      ║     ║█║     ║        │ ← Cu via
│      ║     ╚█╝     ║        │
│      ╚═════════════╝        │
├─────────────────────────────┤
│          ──█───────          │
└─────────────────────────────┘
```

### Trench-First Dual Damascene

**Alternative Approach** - Better trench profile

```
1. Deposit dielectric stack
2. Trench lithography and etch (partial depth)
3. Via lithography and etch (through-etching)
4. Clean and barrier/seed deposition
5. Copper fill and CMP

Advantage: Trench patterned first (easier critical dimension)
Disadvantage: Via profile more challenging
```

### Self-Aligned Via (SAV)

**Advanced Technique** - Eliminates via lithography misalignment

```
Process:
1. Deposit dielectric with embedded metal hard mask
2. Via etch self-aligns to metal cap below
3. Trench lithography defines line pattern
4. Combined structure enables aggressive scaling

Benefit: Via can overlap metal without shorts
Application: 7nm nodes and below
```

---

## Key Process Steps

### Dielectric Deposition

**Inter-Layer Dielectric (ILD) Requirements**:
- Low dielectric constant (k < 3.0)
- Good gap fill capability
- Chemical compatibility with Cu
- Mechanical strength for CMP

**Common Materials**:

| Material | k-value | Deposition | Notes |
|----------|---------|------------|-------|
| **SiO₂** | 4.0-4.2 | PECVD | Baseline, good mechanical |
| **FSG** | 3.5-3.7 | PECVD | Fluorine-doped silica glass |
| **SiOC(H)** | 2.7-3.0 | PECVD | Carbon-doped oxide |
| **Porous SiOC** | 2.3-2.7 | PECVD | Advanced low-k |
| **Spin-on** | 2.2-2.5 | Spin-coat | Ultra-low-k (porous) |

**Deposition Example (PECVD SiO₂)**:
```
Precursors: SiH₄ + N₂O
Temperature: 350-400°C
Pressure: 2-9 Torr
RF power: 100-500 W
Deposition rate: 100-300 nm/min
```

### Etch Stop Layer

**Purpose**:
- Control via etch depth
- Protect lower metal during trench etch
- Provide etch selectivity

**Materials**:
```
SiN (Si₃N₄):
- k-value: 7.0 (high, but thin layer)
- Thickness: 25-50 nm
- Etch selectivity: >20:1 vs SiO₂

SiC (Silicon Carbide):
- k-value: 4.0-5.0 (lower than SiN)
- Thickness: 20-40 nm
- Better for low-k integration
```

---

## Barrier and Seed Layer Deposition

### Barrier Layer Requirements

**Functions**:
1. **Diffusion barrier**: Prevent Cu migration into dielectric
2. **Adhesion layer**: Bond Cu to dielectric
3. **Nucleation layer**: Support seed layer growth

**Key Properties**:
- High density (minimize grain boundaries)
- Conformal coverage (bottom and sidewalls)
- Low resistivity (minimize RC delay)
- Thermal stability (>400°C)

### Barrier Materials

**Tantalum-Based (Industry Standard)**:

```
Ta/TaN Bilayer Stack:
═══════════════════════════════
Top: Ta (5-10 nm)
- Better Cu adhesion
- Lower resistivity (15-20 µΩ·cm)
- Acts as seed for Cu

Bottom: TaN (5-15 nm)  
- Superior diffusion barrier
- Better dielectric adhesion
- Higher resistivity (200-500 µΩ·cm)

Total thickness: 10-25 nm
```

**Deposition Methods**:

1. **PVD (Physical Vapor Deposition)**:
```
Method: DC magnetron sputtering
Target: Ta or Ta/TaN compound
Pressure: 1-5 mTorr
Power: 3-10 kW
Temperature: 25-200°C

Advantages:
+ Mature technology
+ High purity
+ Good adhesion

Disadvantages:
- Poor step coverage (~30-50%)
- Thicker barriers needed
- Challenges at <100nm features
```

2. **CVD/ALD (Chemical Vapor Deposition/Atomic Layer Deposition)**:
```
TaN ALD:
Precursor: TaCl₅ or PDMAT
Reactant: NH₃
Temperature: 250-350°C
Growth rate: 0.5-1.0 Å/cycle

Advantages:
+ Excellent conformality (>95%)
+ Precise thickness control
+ Enables thinner barriers

Disadvantages:
- Higher resistivity
- Precursor challenges
- Throughput limitations
```

### Seed Layer

**Requirements**:
- Continuous, uniform coverage
- Low resistivity (<2.5 µΩ·cm)
- Good adhesion to barrier
- Smooth surface for plating

**Copper Seed Deposition**:
```
Method: PVD sputtering
Target: High-purity Cu (99.999%)
Pressure: 1-5 mTorr
Power: 5-15 kW
Temperature: 25-150°C
Thickness: 50-200 nm

Challenges at Advanced Nodes:
- Thin seed breaks (non-continuous)
- Poor via bottom coverage
- High via aspect ratios (>5:1)

Solutions:
- Long-throw PVD (improve bottom coverage)
- Ionized PVD (directional deposition)
- CVD seed layers (conformal)
```

---

## Copper Electroplating

Electroplating fills the damascene trenches and vias with copper. This is a critical step requiring precise chemistry and control.

### Electroplating Fundamentals

**Electrochemical Reaction**:
```
Cathode (wafer): Cu²⁺ + 2e⁻ → Cu(s)
Anode: Cu(s) → Cu²⁺ + 2e⁻

Net result: Cu transfer from anode to wafer
```

**Faraday's Law**:
```
Deposition rate (nm/min) = (j × M) / (n × F × ρ) × 60 × 10⁷

Where:
j = current density (A/cm²)
M = atomic weight of Cu (63.5 g/mol)
n = number of electrons (2)
F = Faraday constant (96,485 C/mol)
ρ = Cu density (8.96 g/cm³)

Example: j = 20 mA/cm² → rate ≈ 250 nm/min
```

### Plating Solution Chemistry

**Standard Bath Composition**:
```
Component                Concentration    Purpose
────────────────────────────────────────────────────
CuSO₄·5H₂O              0.6-1.0 M        Cu²⁺ source
H₂SO₄                   0.5-2.0 M        Conductivity, acidity
Cl⁻                     30-80 ppm        Inhibitor activation
HCl                     0-50 ppm         pH control

Organic Additives:
────────────────────────────────────────────────────
Suppressor (PEG)        50-500 ppm       Surface blocking
Accelerator (SPS)       1-20 ppm         Via bottom enhancement
Leveler                 1-10 ppm         Field suppression
```

**Additive Roles**:

1. **Suppressor (Polyethylene Glycol, PEG)**:
- Adsorbs on field regions
- Increases overpotential
- Slows deposition rate
- Typical MW: 1,000-10,000

2. **Accelerator (SPS, MPS)**:
- Competes at via/trench bottoms
- Lowers overpotential
- Increases local deposition
- Enables bottom-up fill

3. **Leveler**:
- Preferentially adsorbs on high points
- Reduces top corner deposition
- Prevents overhangs
- Improves uniformity

### Bottom-Up Fill Mechanism

```
SUPERFILLING PROCESS:
═══════════════════════════════════════════════════

Stage 1: Initial State
────────────────────────
Suppressor everywhere
Slow, uniform deposition
┌─────────────────┐
│                 │
│   ╔═════════╗   │ ← Trench opening
│   ║ ░░░░░░░ ║   │ ← Seed layer
│   ║         ║   │
│   ╚═════════╝   │
└─────────────────┘


Stage 2: Accelerator Accumulation
──────────────────────────────────
Accelerator builds at bottom
Fast deposition starts
┌─────────────────┐
│                 │
│   ╔═════════╗   │
│   ║ ░░░░░░░ ║   │
│   ║   ███   ║   │ ← Cu deposits fast
│   ╚═══███═══╝   │    at bottom
└─────────────────┘


Stage 3: Bottom-Up Growth
──────────────────────────
Feature fills from bottom
No voids form
┌─────────────────┐
│                 │
│   ╔═════════╗   │
│   ║ ░░░░░░░ ║   │
│   ║ ███████ ║   │ ← Upward growth
│   ╚═███████═╝   │
└─────────────────┘


Stage 4: Complete Fill
──────────────────────
Void-free filling
Slight overplating
┌─────────────────┐
│   ███████████   │ ← Overplate
│   ╔█████████╗   │
│   ║█████████║   │ ← Complete fill
│   ║█████████║   │
│   ╚═════════╝   │
└─────────────────┘
```

**Critical Parameters**:
```
Current Density: 10-40 mA/cm²
- Low J: Better uniformity, slower
- High J: Faster, risk of voids

Temperature: 20-28°C
- Higher T: Better additive diffusion
- Lower T: More stable chemistry

Agitation: 100-500 rpm paddle
- Improves mass transport
- Removes H₂ bubbles
- Enhances uniformity

Plating Time: 2-10 minutes
- Depends on feature size
- 10-30% overplating typical
```

### Advanced Plating Techniques

**Pulse Plating**:
```
Waveform: Square wave
On-time: 1-10 ms
Off-time: 1-20 ms
Duty cycle: 10-50%

Benefits:
+ Reduced stress
+ Better grain structure
+ Improved fill for high AR
+ Less additive depletion
```

**Fountain Plating**:
```
Configuration: Upward flow through anode
Flow rate: 5-15 L/min
Benefit: Superior additive distribution
Application: 300mm wafers, advanced nodes
```

---

## Chemical Mechanical Polishing

CMP is the final damascene step, removing excess copper and planarizing the surface.

### CMP Fundamentals

**Preston's Equation**:
```
Removal Rate = k_p × P × V

Where:
k_p = Preston coefficient (depends on slurry)
P = down pressure (1-7 psi)
V = relative velocity (0.5-2.0 m/s)

Typical RR: 200-500 nm/min (bulk Cu)
```

**Multi-Step Process**:

```
STEP 1: BULK COPPER REMOVAL
═══════════════════════════════════
Goal: Remove 80-90% of Cu overburden
Slurry: Aggressive (H₂O₂ + glycine + abrasive)
Pressure: 3-5 psi
RR: 400-600 nm/min
Selectivity: Cu:barrier = 50:1

Before:
┌─────────────────────────────┐
│     █████████████████       │ ← Cu overburden
│   ╔═══════════════════╗     │
│   ║   ║█║   ║█║   ║█║ ║     │
│   ╚═══╚═╝═══╚═╝═══╚═╝═╝     │
└─────────────────────────────┘

After Step 1:
┌─────────────────────────────┐
│         ████████            │ ← Thin Cu remains
│   ╔═══════════════════╗     │
│   ║   ║█║   ║█║   ║█║ ║     │
│   ╚═══╚═╝═══╚═╝═══╚═╝═╝     │
└─────────────────────────────┘


STEP 2: BARRIER REMOVAL
═══════════════════════════════════
Goal: Clear Cu from field, expose barrier
Slurry: Moderate selectivity
Pressure: 2-4 psi
RR: 200-300 nm/min
Selectivity: Cu:barrier = 10-20:1

After Step 2:
┌─────────────────────────────┐
│         ▓▓▓▓▓▓▓▓            │ ← Barrier exposed
│   ╔═══════════════════╗     │
│   ║   ║█║   ║█║   ║█║ ║     │
│   ╚═══╚═╝═══╚═╝═══╚═╝═╝     │
└─────────────────────────────┘


STEP 3: SOFT LANDING (OPTIONAL)
═══════════════════════════════════
Goal: Remove barrier, stop on dielectric
Slurry: High selectivity to oxide
Pressure: 1-2 psi
RR: 50-100 nm/min
Selectivity: barrier:oxide = 20-50:1

After Step 3:
┌─────────────────────────────┐
│                             │ ← Clean dielectric
│   ╔═══════════════════╗     │
│   ║   ║█║   ║█║   ║█║ ║     │ ← Cu lines intact
│   ╚═══╚═╝═══╚═╝═══╚═╝═╝     │
└─────────────────────────────┘
```

### CMP Slurry Chemistry

**Copper Slurry Components**:
```
Abrasive:
- Alumina (Al₂O₃) or Silica (SiO₂)
- Particle size: 50-200 nm
- Concentration: 1-5 wt%

Oxidizer:
- H₂O₂ (hydrogen peroxide): 1-5 wt%
- Fe(NO₃)₃ or (NH₄)₂S₂O₈ (alternatives)
- Function: Oxidize Cu to Cu²⁺

Complexing Agent:
- Glycine, ammonia, or organic acids
- Solubilize Cu²⁺ ions
- Prevent redeposition

pH Buffer:
- Typically pH 3-10
- Affects oxidation rate
- Controls selectivity
```

**Reaction Mechanism**:
```
1. Oxidation:   Cu + H₂O₂ → CuO + H₂O
2. Complexation: CuO + complexer → Cu-complex (soluble)
3. Abrasion:    Particles remove passivation layer
```

### CMP Defects and Control

**Dishing**:
```
Definition: Cu surface depression in wide features

Causes:
- High Cu removal rate
- Pad compliance
- Pattern density effects

Control:
- Slurry selectivity optimization
- Pad hardness adjustment
- Overpolish time minimization

Specification: <10 nm for 1 µm lines
```

**Erosion**:
```
Definition: Dielectric thinning in dense patterns

Causes:
- Non-uniform pattern density
- Cumulative pad wear
- Slurry selectivity

Control:
- Dummy fill structures
- Multi-zone polishing
- Endpoint detection

Specification: <20 nm across die
```

**Scratches and Defects**:
```
Types:
- Large particles (>1 µm)
- Pad debris
- Slurry agglomeration

Detection:
- Bright field inspection
- Dark field inspection
- Wafer surface scan (WSS)

Control:
- Slurry filtration (0.2 µm)
- Pad conditioning
- Clean post-CMP process
```

### Endpoint Detection

**Methods**:

1. **Motor Current Monitoring**:
```
Principle: Current changes with friction
Cu removal: High friction, high current
Barrier exposure: Current drops
Oxide exposure: Further current drop
```

2. **Optical Endpoint**:
```
Principle: Reflectivity changes
Cu: High reflectivity (~60%)
Barrier: Low reflectivity (~10%)
Oxide: Medium reflectivity (~20%)

Detection: Eddy current or laser interferometry
```