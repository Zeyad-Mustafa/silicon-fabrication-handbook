# Release Techniques in MEMS Surface Micromachining

## Table of Contents

1. [Introduction](#introduction)
2. [Wet Release Methods](#wet-release-methods)
3. [Dry Release Methods](#dry-release-methods)
4. [Vapor-Phase Release](#vapor-phase-release)
5. [Supercritical Drying](#supercritical-drying)
6. [Freeze Drying](#freeze-drying)
7. [Release Etchant Selection](#release-etchant-selection)
8. [Stiction Mechanisms and Prevention](#stiction-mechanisms-and-prevention)
9. [Process Optimization](#process-optimization)
10. [Characterization and Quality Control](#characterization-and-quality-control)
11. [Advanced Techniques](#advanced-techniques)
12. [Case Studies](#case-studies)
13. [Common Problems and Solutions](#common-problems-and-solutions)

---

## Introduction

The **release process** is the critical final step in surface micromachining where sacrificial layers are selectively removed to create freely suspended mechanical structures. This step transforms integrated thin films into functional MEMS devices capable of mechanical motion.

### Why Release is Critical

The release step determines:
- **Structural integrity**: Whether devices survive without damage
- **Yield**: Percentage of functional devices after release
- **Reliability**: Long-term performance of released structures
- **Cost**: Process time and material consumption

### Key Challenges

1. **Stiction**: Released structures adhering to substrate
2. **Etch selectivity**: Removing sacrificial layer without damaging structural layer
3. **Uniformity**: Complete release across entire wafer
4. **Particle contamination**: Residues preventing proper release
5. **Surface tension**: Capillary forces during drying

### Common Sacrificial Materials

| Material | Typical Etchant | Structural Material | Selectivity | Applications |
|----------|----------------|---------------------|-------------|--------------|
| SiO₂ | HF (49%) | Polysilicon, Si₃N₄ | >1000:1 | General MEMS |
| PSG | HF (diluted) | Polysilicon | >5000:1 | RF MEMS, resonators |
| Silicon | TMAH, KOH | SiO₂, Si₃N₄ | >100:1 | Cantilevers, membranes |
| Photoresist | Acetone, O₂ plasma | Metals, polymers | >50:1 | Soft MEMS |
| Al | H₃PO₄/HNO₃/CH₃COOH | Polysilicon, SiO₂ | >100:1 | Specific applications |
| Polyimide | O₂ plasma | Metals | >20:1 | Flexible MEMS |

---

## Wet Release Methods

### 2.1 Hydrofluoric Acid (HF) Etching

**Most common release method** for oxide sacrificial layers.

#### Chemistry

```
SiO₂ + 6HF → H₂SiF₆ + 2H₂O
```

For PSG (phosphosilicate glass):
```
SiO₂·P₂O₅ + 6HF → H₂SiF₆ + H₃PO₄ + H₂O
```

#### Process Parameters

**Typical Conditions**:
- **Concentration**: 49% HF (concentrated) or 5-10% HF (diluted)
- **Temperature**: 20-25°C (room temperature)
- **Etch rate (SiO₂)**: 
  - 49% HF: ~1 μm/min
  - 10% HF: ~100 nm/min
  - 1% HF: ~10 nm/min
- **Agitation**: Ultrasonic or mechanical stirring
- **Time**: 5-60 minutes depending on gap height and structure complexity

#### Selectivity

| Material | Etch Rate in 49% HF | Selectivity to SiO₂ |
|----------|---------------------|---------------------|
| Thermal SiO₂ | 1.0 μm/min | 1:1 (reference) |
| PECVD SiO₂ | 1.2-1.5 μm/min | 0.7:1 |
| PSG (8% P) | 5-10 μm/min | 0.1-0.2:1 |
| Si₃N₄ | 1-2 nm/min | 500-1000:1 |
| Polysilicon | <0.1 nm/min | >10,000:1 |
| Aluminum | 1-5 nm/min | 200-1000:1 |

#### Process Flow Example

```
1. Initial Cleaning
   └─ Remove photoresist: Acetone + IPA
   └─ Piranha clean (H₂SO₄:H₂O₂ = 3:1)
   └─ DI water rinse

2. HF Release
   └─ 10% HF etch: 20 minutes
   └─ Gentle agitation every 5 minutes
   └─ Monitor etch progress optically

3. Rinse Sequence
   └─ DI water rinse: 5 minutes
   └─ Methanol rinse: 2 minutes
   └─ IPA rinse: 2 minutes

4. Drying
   └─ Supercritical CO₂ drying
   └─ or vapor drying in IPA
```

#### Advantages
- ✓ High selectivity to silicon and nitride
- ✓ Room temperature process
- ✓ Isotropic etching (good for complex geometries)
- ✓ Well-established process
- ✓ Low cost

#### Disadvantages
- ✗ Strong capillary forces during drying (stiction risk)
- ✗ Hazardous chemical (safety concerns)
- ✗ Attacks many materials (limited compatibility)
- ✗ Requires special handling and disposal
- ✗ Hydrogen bubble formation can cause incomplete release

### 2.2 Buffered Oxide Etch (BOE)

A mixture of HF and NH₄F that provides more controlled etching.

#### Composition

**Common Formulations**:
- **BOE 7:1** → NH₄F:HF = 7:1 (volume ratio)
- **BOE 10:1** → NH₄F:HF = 10:1
- **BOE 20:1** → NH₄F:HF = 20:1

#### Chemistry

```
SiO₂ + 4HF → SiF₄ + 2H₂O
SiO₂ + 4NH₄F + 2HF → (NH₄)₂SiF₆ + 2H₂O
```

The NH₄F acts as a buffer, maintaining pH ~5-6 and providing consistent etch rates.

#### Etch Rates (BOE 7:1)

- **Thermal oxide**: 80-100 nm/min at 25°C
- **PECVD oxide**: 100-150 nm/min at 25°C
- **Temperature coefficient**: ~5%/°C

#### Advantages over Pure HF
- ✓ Better photoresist compatibility
- ✓ More stable etch rate
- ✓ Reduced undercutting of aluminum
- ✓ Less sensitive to contamination
- ✓ Safer handling (lower HF concentration)

### 2.3 KOH/TMAH Silicon Release

Used when **silicon** is the sacrificial layer.

#### KOH Etching

**Typical Conditions**:
- **Concentration**: 20-40 wt% KOH in water
- **Temperature**: 60-80°C
- **Etch rate {100}**: 0.5-1.5 μm/min at 80°C
- **Etch rate {111}**: <0.001 μm/min (effectively zero)
- **Anisotropy ratio**: >100:1

**Chemistry**:
```
Si + 2OH⁻ + 2H₂O → Si(OH)₂²⁺ + 3H₂ + 4e⁻
Si(OH)₂²⁺ + 4OH⁻ → SiO₂(OH)₂²⁻ + 2H₂O
```

#### TMAH Etching

**Tetramethylammonium hydroxide** - CMOS compatible alternative.

**Typical Conditions**:
- **Concentration**: 5-25 wt% TMAH
- **Temperature**: 70-90°C
- **Etch rate {100}**: 0.3-1.0 μm/min at 80°C
- **Aluminum compatibility**: Better than KOH

#### Comparison

| Parameter | KOH | TMAH |
|-----------|-----|------|
| CMOS compatible | No | Yes |
| Al compatibility | Poor | Good |
| Cost | Low | Higher |
| {100} etch rate | Higher | Lower |
| Surface roughness | Better | Good |
| Safety | Caustic | Less caustic |

### 2.4 XeF₂ Gas-Phase Etching

**Spontaneous isotropic** silicon etch without plasma.

#### Process

- **Gas**: Xenon difluoride (XeF₂)
- **Pressure**: 1-5 Torr
- **Temperature**: Room temperature
- **Etch rate**: 0.5-3 μm/min (pulsed mode)
- **Selectivity**: >1000:1 to SiO₂, Si₃N₄, photoresist, most metals

#### Chemistry

```
2XeF₂ + Si → 2Xe + SiF₄
```

#### Process Modes

**Pulsed Etching**:
```
1. Introduce XeF₂ gas (3 Torr)
2. Wait for reaction (30-60 seconds)
3. Pump out products
4. Repeat until complete
```

**Continuous Flow**:
- Constant XeF₂ pressure
- Faster overall process
- Less control

#### Advantages
- ✓ No stiction (dry process)
- ✓ Room temperature
- ✓ Excellent selectivity
- ✓ No charging damage
- ✓ Isotropic (reaches complex geometries)

#### Disadvantages
- ✗ Expensive gas
- ✗ Requires specialized equipment
- ✗ Slow compared to wet etching
- ✗ Limited mask materials (attacks aluminum)

---

## Dry Release Methods

### 3.1 Plasma Release

#### Oxygen Plasma (Organic Sacrificial Layers)

**Used for**: Photoresist, polyimide sacrificial layers

**Typical Conditions**:
- **Gas**: O₂ or O₂/CF₄
- **Pressure**: 100-500 mTorr
- **Power**: 100-500 W
- **Temperature**: 20-150°C
- **Etch rate**: 0.5-2 μm/min

**Chemistry**:
```
Organic + O* → CO₂ + H₂O + volatiles
```

#### Reactive Ion Etching (RIE)

**For silicon sacrificial layers**:
- **Gas**: SF₆, SF₆/O₂, or CF₄/O₂
- **Pressure**: 10-100 mTorr
- **Bias**: 50-300 V
- **Temperature**: 0-20°C

#### Advantages
- ✓ No liquid-induced stiction
- ✓ Directional control possible
- ✓ In-situ monitoring
- ✓ Clean process (volatile products)

#### Disadvantages
- ✗ Charging damage risk
- ✗ Equipment cost
- ✗ Lower selectivity than wet
- ✗ Notching effects possible

### 3.2 Vapor HF Etching

**Anhydrous HF vapor** - combines benefits of wet and dry release.

#### Process

- **Temperature**: 30-40°C
- **Pressure**: Atmospheric or reduced
- **Catalyst**: Water vapor or alcohol vapor
- **Etch rate**: 50-500 nm/min
- **Uniformity**: Good across wafer

#### Chemistry

```
SiO₂ + 4HF(g) + H₂O(g) → SiF₄(g) + 2H₂O(g)
```

Water or alcohol vapor acts as catalyst, increasing etch rate by 10-100×.

#### Equipment

**Vapor HF Etcher Components**:
```
┌─────────────────────────────────┐
│  HF Vapor Source (30-40°C)      │
│  ├─ Liquid HF reservoir         │
│  └─ Temperature control          │
└──────────────┬──────────────────┘
               │
┌──────────────▼──────────────────┐
│  Reaction Chamber               │
│  ├─ Wafer chuck (heated)        │
│  ├─ Vapor distribution          │
│  └─ Exhaust scrubber            │
└──────────────┬──────────────────┘
               │
┌──────────────▼──────────────────┐
│  Catalyst Injection             │
│  ├─ H₂O or IPA vapor            │
│  └─ Flow control                │
└─────────────────────────────────┘
```

#### Advantages
- ✓ Reduced stiction (no bulk liquid)
- ✓ Better uniformity than immersion
- ✓ Minimal contamination
- ✓ Anisotropic possible with directional delivery
- ✓ In-situ monitoring

#### Disadvantages
- ✗ Specialized equipment required
- ✗ Safety concerns with HF vapor
- ✗ Slower than liquid HF
- ✗ Difficult to scale

---

## Supercritical Drying

### 4.1 Principle

**Eliminates liquid-vapor interface** that causes capillary forces.

#### Phase Diagram of CO₂

```
Pressure
  ^
  │     Supercritical
  │        Region
73│    ╱──────────
  │   ╱ Critical Point
  │  ╱  (31.1°C, 73.8 bar)
  │ ╱
  │╱    Liquid
──┼────────────────> Temperature
  │  Gas            31.1°C
```

At **supercritical conditions**:
- No surface tension
- No meniscus formation
- No capillary forces

### 4.2 Process Flow

**Standard Supercritical CO₂ Drying**:

```
1. Release in HF
   └─ Complete oxide removal
   └─ DI water rinse

2. Solvent Exchange
   └─ Water → Methanol (5 min)
   └─ Methanol → IPA (5 min)
   └─ IPA → Liquid CO₂ (10 min)
   (CO₂ miscible with IPA but not water)

3. Supercritical Transition
   └─ Heat chamber to 40°C
   └─ Increase pressure to 100 bar
   └─ Hold for 10 minutes

4. Depressurization
   └─ Slowly vent CO₂ (1 bar/min)
   └─ Maintain temperature > 31°C
   └─ Complete at atmospheric pressure
```

### 4.3 Equipment

**Critical Point Dryer Components**:
- **Pressure vessel**: Rated to 150+ bar
- **Temperature control**: ±1°C precision
- **CO₂ delivery system**: Liquid CO₂ cylinder
- **Pressure monitoring**: High-precision gauges
- **Exhaust**: Slow release valve

#### Commercial Systems

| Vendor | Model | Capacity | Pressure | Cost |
|--------|-------|----------|----------|------|
| Tousimis | Autosamdri-931 | 2 wafers | 150 bar | $35k |
| Quorum | K850 | 6 wafers | 120 bar | $45k |
| Leica | EM CPD300 | 4 wafers | 100 bar | $55k |

### 4.4 Advantages and Limitations

**Advantages**:
- ✓ Near 100% stiction prevention
- ✓ No surface damage
- ✓ Compatible with all structures
- ✓ Gentle process
- ✓ Repeatable

**Limitations**:
- ✗ Equipment cost ($30-60k)
- ✗ Long process time (30-60 min)
- ✗ Solvent exchange steps
- ✗ Limited batch size
- ✗ Safety concerns (high pressure)

---

## Freeze Drying

### 5.1 Principle

**Sublimation of ice** bypasses liquid-vapor transition.

#### Phase Diagram Approach

```
Pressure
  ^
  │   ╱ Liquid
  │  ╱
  │ ╱  Triple Point
──┼╱───────────────> Temperature
  │╲
  │ ╲ Solid (Ice)
  │  ╲
  │   ╲ Vapor
  │
```

Process path: Liquid → Frozen → Sublimation → Vapor

### 5.2 Process Flow

```
1. Release and Rinse
   └─ Standard HF release
   └─ DI water rinse

2. Freezing
   └─ Cool to -20°C to -40°C
   └─ Rapid freezing preferred (smaller ice crystals)
   └─ Hold for 5-10 minutes

3. Vacuum Sublimation
   └─ Apply vacuum (<100 mTorr)
   └─ Heat slowly to room temperature
   └─ Monitor pressure (should decrease as ice sublimates)
   └─ Complete when pressure stabilizes (1-2 hours)

4. Return to Atmosphere
   └─ Backfill with dry nitrogen
   └─ Remove samples
```

### 5.3 Critical Parameters

**Freezing Rate**:
- **Fast freezing** (liquid N₂ immersion): Small ice crystals, less damage
- **Slow freezing** (gradual cooling): Large crystals, potential structure damage

**Sublimation Temperature**:
- Too low: Very slow process (hours)
- Too high: Risk of melting before complete sublimation
- Optimal: -10°C to 0°C under vacuum

**Vacuum Level**:
- Must be below vapor pressure of ice at operating temperature
- Typical: <100 mTorr

### 5.4 Advantages and Limitations

**Advantages**:
- ✓ Low equipment cost
- ✓ No hazardous solvents
- ✓ Simple setup
- ✓ Good for large structures

**Limitations**:
- ✗ Ice crystal formation can damage delicate structures
- ✗ Long process time (1-3 hours)
- ✗ Lower success rate than supercritical drying
- ✗ Not suitable for very small gaps (<1 μm)
- ✗ Some residual stiction (5-20%)

---

## Release Etchant Selection

### 6.1 Decision Matrix

| Criterion | HF (49%) | BOE | KOH/TMAH | XeF₂ | O₂ Plasma |
|-----------|----------|-----|----------|------|-----------|
| Etch rate | ★★★★★ | ★★★ | ★★★★ | ★★ | ★★★★ |
| Selectivity | ★★★★★ | ★★★★★ | ★★★★ | ★★★★★ | ★★★ |
| Cost | ★★★★★ | ★★★★ | ★★★★★ | ★★ | ★★★ |
| Safety | ★★ | ★★★ | ★★ | ★★★★ | ★★★★ |
| CMOS compatible | ★★★ | ★★★★ | ★★★ | ★★★★ | ★★★★★ |
| Stiction risk | ★★ | ★★ | ★★ | ★★★★★ | ★★★★★ |

### 6.2 Application-Specific Selection

#### High-Aspect-Ratio Structures
**Best choice**: Vapor HF or XeF₂
- Isotropic etching reaches deep gaps
- Reduced stiction with vapor-phase

#### Fragile Suspended Membranes
**Best choice**: Supercritical CO₂ drying after HF release
- Minimal stress during drying
- Near-zero stiction

#### CMOS-Integrated MEMS
**Best choice**: TMAH (if Si sacrificial) or vapor HF (if oxide sacrificial)
- CMOS compatibility critical
- Controlled process

#### Low-Cost Production
**Best choice**: HF with IPA vapor drying
- Proven process
- Acceptable yield for many applications

#### RF MEMS Switches
**Best choice**: HF release + supercritical drying
- Critical to prevent stiction
- High-value devices justify cost

---

## Stiction Mechanisms and Prevention

### 7.1 Stiction Mechanisms

#### Capillary Adhesion

**Most common cause** of release failure.

**Capillary Force**:
```
F_capillary = 2γLW cosθ / g
```

Where:
- γ = surface tension of liquid (water: 72 mN/m)
- L = beam length
- W = beam width
- θ = contact angle
- g = gap height

**Example Calculation**:
```
For water drying:
- L = 100 μm, W = 10 μm
- g = 2 μm, θ = 70° (hydrophilic Si)
- γ = 72 mN/m

F_capillary = 2 × 0.072 × 100 × 10 × cos(70°) / 2
           = 12.3 μN

For beam with t = 2 μm, E = 160 GPa:
Restoring force ≈ 8 μN

Result: STICTION OCCURS (capillary force > restoring force)
```

#### van der Waals Forces

**Surface adhesion energy**:
```
W_adhesion = A_Hamaker / (12πz₀²)
```

Where:
- A_Hamaker ≈ 10⁻¹⁹ J (typical for Si-Si)
- z₀ = separation distance ≈ 0.4 nm

**Adhesion pressure** for contacting surfaces:
```
P_adhesion ≈ 100-500 MPa
```

This is sufficient to permanently deform structures.

#### Electrostatic Adhesion

For charged surfaces:
```
F_electrostatic = (ε₀εᵣAV²) / (2g²)
```

Can be significant if charge trapped during processing.

### 7.2 Anti-Stiction Coatings

#### Self-Assembled Monolayers (SAMs)

**Most common**: Fluorinated silanes

**Process**:
```
1. Release in HF
2. Rinse: DI water → IPA
3. Vapor phase coating
   └─ Chamber: 100-200 mTorr
   └─ Precursor: FDTS or OTS
   └─ Temperature: 100-150°C
   └─ Time: 30-60 minutes
4. Bake: 150°C, 10 minutes
```

**Common SAM Materials**:

| Material | Formula | Contact Angle | Stability |
|----------|---------|---------------|-----------|
| FDTS | CF₃(CF₂)₇(CH₂)₂SiCl₃ | 110-115° | Excellent |
| OTS | CH₃(CH₂)₁₇SiCl₃ | 105-110° | Good |
| PFOTS | CF₃(CF₂)₇(CH₂)₂Si(OMe)₃ | 112-118° | Excellent |

**FDTS Structure**:
```
        F  F  F  F  F  F  F  F
        │  │  │  │  │  │  │  │
    F─C─C─C─C─C─C─C─C─C─H
        │  │  │  │  │  │  │  │
        F  F  F  F  F  F  F  H
                            │
                            H─C─H
                            │
                            H─C─H
                            │
                            Si─O─Si (surface)
```

**Effectiveness**:
- Reduces surface energy from 72 mN/m to 10-20 mN/m
- Increases contact angle from 70° to 110°
- Reduces capillary force by 5-10×

#### Alternative Coatings

**Polytetrafluoroethylene (PTFE)**:
- Contact angle: 110-120°
- Applied by plasma deposition
- Good durability

**Diamond-Like Carbon (DLC)**:
- Contact angle: 70-90°
- Excellent wear resistance
- Applied by PECVD

**Parylene-C**:
- Contact angle: 90-95°
- Conformal coating
- Good for complex geometries

### 7.3 Structural Design for Stiction Prevention

#### Design Guidelines

**1. Maximize Gap Height**
```
g > 2μm for most applications
g > 5μm for robust designs
```

**2. Minimize Contact Area**
- Use dimples or posts
- Typical dimple: 0.5-2 μm diameter, 0.2-0.5 μm height
- Reduces contact area by 100-1000×

**3. Increase Beam Stiffness**
```
For cantilever:
k = EWt³/(4L³)

Strategies:
- Decrease length L
- Increase thickness t
- Increase width W (less effective)
```

**4. Add Release Holes**
- Accelerate sacrificial etch
- Provide escape path for etchant
- Typical: 2-5 μm diameter, spaced 10-50 μm

**Example Design**:
```
Top View:
┌─────────────────────────┐
│ ╭─╮  ╭─╮  ╭─╮  ╭─╮  ╭─╮│ Suspended Plate
│ ╰─╯  ╰─╯  ╰─╯  ╰─╯  ╰─╯│ with Release Holes
│                         │
│  ·    ·    ·    ·    ·  │ Anti-stiction Dimples
└─────────────────────────┘

Cross-Section:
    Structural Layer
    ┌───┐  ┌───┐  ┌───┐
    │   │  │   │  │   │  ← Dimples
────┴───┴──┴───┴──┴───┴──
    Substrate
    ↑     ↑     ↑
    Gap = 2-3 μm
```

---

## Process Optimization

### 8.1 Release Time Estimation

#### Lateral Etch Rate Model

For isotropic etching under a structure:

```
t_release = (L_max / 2) / R_etch

Where:
- L_max = maximum distance from edge to release point
- R_etch = lateral etch rate
```

**With release holes**:
```
L_max = spacing between holes / 2
```

#### Example Calculation

**Device**: 500 μm × 500 μm plate
**Gap**: 2 μm oxide
**Etchant**: 10% HF (R_etch = 100 nm/min lateral)

**Without release holes**:
```
t_release = 250 μm / 0.1 μm/min = 2500 min ≈ 42 hours!
```

**With 5 μm holes spaced 50 μm**:
```
t_release = 25 μm / 0.1 μm/min = 250 min ≈ 4 hours
```

**With 5 μm holes spaced 20 μm**:
```
t_release = 10 μm / 0.1 μm/min = 100 min ≈ 1.7 hours
```

### 8.2 Over-Etch Consideration

Always etch **longer than calculated** to ensure complete release:

```
t_actual = 1.5 × t_release (minimum)
         = 2-3 × t_release (recommended)
```

**Reason**: 
- Etch rate variation across wafer
- Difficult-to-reach corners
- Particle contamination
- Etchant depletion

### 8.3 Process Monitoring

#### In-Situ Monitoring Methods

**1. Optical Inspection**
- View through transparent substrate
- Look for interference color change
- Indicates oxide removal

**2. Acoustic Monitoring**
- Resonance frequency changes when released
- Real-time feedback

**3. Electrical Monitoring**
- Capacitance change when gap opens
- Requires integrated electrodes

#### Ex-Situ Testing

**1. Mechanical Probing**
- Use probe needle to deflect structure
- Check for free movement

**2. Optical Profilometry**
- Measure gap height
- Confirm full release

**3. SEM Inspection**
- Cross-sectional view
- Verify sacrificial layer removal

---

## Characterization and Quality Control

### 9.1 Release Quality Metrics

#### Yield Analysis

```
Release Yield = (Functional Devices / Total Devices) × 100%
```

**Typical yields**:
- Optimized process: 95-99%
- Development process: 60-80%
- Challenging structures: 30-50%

#### Defect Classification

| Defect Type | Cause | Frequency | Fix |
|-------------|-------|-----------|-----|
| Stiction | Capillary forces | 50-70% | Supercritical drying |
| Incomplete release | Under-etch | 20-30% | Longer etch time |
| Structural damage | Over-etch | 5-10% | Better selectivity |
| Contamination | Particles | 5-10% | Cleaner process |

### 9.2 Measurement Techniques

#### Resonance Testing

**Method**: Excite structure and measure frequency response

**Setup**:
```
┌─────────────────────────┐
│  Network Analyzer       │
└──────┬──────────┬───────┘
       │          │
   ┌───▼──┐   ┌──▼────┐
   │ VNA  │   │ LDV   │ Laser Doppler
   │ Port │   │ Probe │ Vibrometer
   └──┬───┘   └───────┘
      │
   ┌──▼────────────────┐
   │  MEMS Device      │
   │  (on wafer)       │
   └───────────────────┘
```

**Typical Result**:
- Released structure: Sharp resonance peak at design frequency
- Stuck structure: No resonance or shifted frequency

#### Gap Height Measurement

**Method**: White light interferometry

**Procedure**:
