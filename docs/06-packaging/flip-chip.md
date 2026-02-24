# Flip Chip Packaging

## Table of Contents
- [Introduction](#introduction)
  - [Key Advantages](#key-advantages)
  - [Technology Comparison](#technology-comparison)
  - [Market Overview](#market-overview)
  - [Process Overview](#process-overview)
- [Bump Formation](#bump-formation)
  - [Under Bump Metallization (UBM)](#under-bump-metallization-ubm)
  - [Solder Bump Formation](#solder-bump-formation)
- [Assembly Process](#assembly-process)
  - [Substrate Preparation](#substrate-preparation)
  - [Flux Application](#flux-application)
  - [Die Placement](#die-placement)
  - [Reflow Process](#reflow-process)
  - [Self-Alignment Effect](#self-alignment-effect)
- [Underfill](#underfill)
  - [Purpose](#purpose)
  - [Underfill Materials](#underfill-materials)
  - [Dispense Methods](#dispense-methods)
  - [Void Control](#void-control)
- [Process Variations](#process-variations)
  - [Fine Pitch Flip Chip](#fine-pitch-flip-chip)
  - [Non-Conductive Materials](#non-conductive-materials)
  - [Anisotropic Conductive Film (ACF)](#anisotropic-conductive-film-acf)
- [Reliability](#reliability)
  - [Failure Mechanisms](#failure-mechanisms)
  - [Reliability Testing](#reliability-testing)
  - [Quality Control](#quality-control)
- [Cost Analysis](#cost-analysis)
- [Design Guidelines](#design-guidelines)
  - [Best Practices ✓](#best-practices)
  - [Avoid ✗](#avoid)
- [References](#references)

## Introduction

Flip chip is an advanced packaging technology where the die is inverted and connected face-down to the substrate through solder bumps or metal pillars, eliminating wire bonds.

### Key Advantages

| Benefit | Impact | Quantification |
|---------|--------|----------------|
| Electrical performance | Lower inductance | 0.1-0.5 nH vs 10-20 nH (wire bond) |
| Thermal performance | Direct heat path | 50-70% lower thermal resistance |
| Package size | Area array I/O | 2-5× more connections in same area |
| Reliability | No wire fatigue | >10× thermal cycle life |
| Speed | Parallel assembly | >100 dies/hour vs 10-20 (wire bond) |

### Technology Comparison

**Flip Chip vs Wire Bond:**

```
Wire Bond:
Die → Wire → Package
- Sequential connections
- Perimeter I/O only
- Loop inductance
- Package height >2 mm

Flip Chip:
Die ↓ Bump ↓ Package
- Parallel connections
- Area array I/O
- Minimal inductance
- Package height <1 mm
```

### Market Overview

```
Applications:
- High-performance processors (Intel, AMD)
- Graphics processors (NVIDIA, AMD)
- RF MEMS switches
- Image sensors
- MEMS inertial sensors

Growth: 15-20% CAGR
Market size: $25-30 billion/year

Drivers:
- 5G/6G communications
- AI processors
- Advanced packaging (2.5D, 3D)
```

### Process Overview

```
Wafer Processing:
1. Bump formation (UBM + solder/Cu pillar)
2. Wafer test (probe)
3. Wafer dicing

Assembly:
4. Flux application
5. Die placement
6. Reflow (solder melting)
7. Underfill dispensing
8. Underfill cure

Testing:
9. Visual inspection
10. X-ray inspection
11. Electrical test
```

## Bump Formation

### Under Bump Metallization (UBM)

Required for adhesion and diffusion barrier between aluminum bond pads and solder.

**Standard UBM Stack:**

```
Al Pad (on die)
  ↓
Ti (50 nm): Adhesion layer
  ↓
Ni(V) or Cu (500 nm): Diffusion barrier
  ↓
Au (100-200 nm): Oxidation protection, wetting
  ↓
Solder bump

Total UBM thickness: 0.5-1 μm
```

**Alternative Stacks:**

| Stack | Thickness | Advantages | Applications |
|-------|-----------|------------|--------------|
| Ti/Cu/Au | 0.05/0.5/0.1 μm | Standard, reliable | General purpose |
| Ti/Ni(V)/Au | 0.05/0.3/0.1 μm | Better barrier | High temperature |
| Cr/Cu/Au | 0.05/0.5/0.1 μm | Good adhesion | Fine pitch |
| TiW/Au | 0.1/0.2 μm | Simple | Low cost |

**Deposition Methods:**

```
Sputtering (PVD):
- Sequential layer deposition
- Thickness control: ±5%
- Uniformity: <3% across wafer
- Throughput: 20-40 wafers/hour

Electroplating:
- For thick layers (Cu, Ni)
- Lower cost for high volume
- Requires seed layer
```

### Solder Bump Formation

#### 1. Electroplating

Most common method for high-volume production.

**Process Flow:**

```
1. Deposit UBM (sputter)
2. Apply photoresist (15-30 μm thick)
3. Pattern bump locations
4. Electroplate solder
   - Current density: 10-30 mA/cm²
   - Temperature: 25-35°C
   - Time: 20-60 min
   - Thickness: 10-50 μm
5. Strip resist
6. Etch UBM from non-bump areas
7. Reflow to form spherical bumps
```

**Solder Composition:**

| Alloy | Melting Point | Advantages | Applications |
|-------|---------------|------------|--------------|
| 63Sn-37Pb (eutectic) | 183°C | Reliable, proven | Legacy (RoHS restricted) |
| Sn-3.5Ag | 221°C | Lead-free, good strength | Standard |
| Sn-3.0Ag-0.5Cu (SAC305) | 217°C | Lead-free, reliable | Most common |
| Sn-0.7Cu | 227°C | Low cost, lead-free | Consumer |
| 95Pb-5Sn (high-Pb) | 300-320°C | High temp | Automotive, exempt from RoHS |

**Bump Dimensions:**

```
Bump diameter: 50-150 μm (typical)
Bump height: 30-100 μm (after reflow)
Bump pitch: 100-400 μm (standard)
            40-100 μm (fine pitch)

Volume calculation:
V = (π/6) × d³ (spherical)

For 80 μm diameter:
V = 268,000 μm³

Plating thickness = V / (π × pad_area)
```

#### 2. Stencil Printing

Lower cost for prototype and low-medium volume.

**Process:**

```
1. Deposit UBM
2. Align stencil over wafer
3. Apply solder paste
   - Squeegee across stencil
   - Paste fills openings
4. Remove stencil
5. Reflow in oven
   - Profile: See reflow section
   - Forms spherical bumps

Stencil:
- Material: Stainless steel or Ni
- Thickness: 75-150 μm
- Opening size: 80-90% of pad size
```

**Advantages:**
- Fast setup (<1 hour)
- Low capital cost
- Good for prototyping

**Limitations:**
- Lower accuracy (±25 μm)
- Height variation (±15%)
- Difficult for fine pitch (<150 μm)

#### 3. Evaporation (C4 Process)

IBM's controlled collapse chip connection.

**Process:**

```
1. Deposit UBM
2. Apply photoresist (thick)
3. Pattern via lithography
4. Evaporate solder
   - Multiple alloy layers
   - High Pb (97Pb-3Sn) typically
   - Thickness: 50-100 μm
5. Strip resist (leaves solder bumps)
6. Optional reflow
```

**Characteristics:**
- Very uniform height (±3 μm)
- Fine pitch capable (<50 μm)
- High cost (evaporation slow)
- Used in high-end processors

#### 4. Copper Pillar Bumps

Alternative to solder for fine pitch and high I/O.

**Structure:**

```
Pad (Al)
  ↓
UBM (Ti/Cu)
  ↓
Cu Pillar (20-80 μm height, electroplated)
  ↓
Solder Cap (10-20 μm, SAC305)
  ↓
Substrate

Advantages:
- Better electromigration resistance
- Finer pitch possible (30-50 μm)
- Reduced solder volume
- Better coplanarity
```

**Process:**

```
1. Deposit seed layer (UBM)
2. Apply thick resist (30-100 μm)
3. Pattern pillar locations
4. Electroplate Cu pillar
   - Current: 5-15 mA/cm²
   - Time: 2-6 hours
   - Additive: Brightener, leveler
5. Electroplate solder cap (5-20 μm)
6. Strip resist
7. Etch seed layer
```

**Applications:**
- High-end processors
- MEMS with fine pitch
- 3D stacking (TSV connection)
- High reliability (automotive)

## Assembly Process

### Substrate Preparation

**Substrate Types:**

| Type | Cost | Performance | Applications |
|------|------|-------------|--------------|
| Organic (BT, FR-4) | Low | Good | Consumer, standard |
| Ceramic (Al₂O₃, AlN) | Medium | Excellent | RF, power, hermetic |
| Silicon | High | Best | Interposer, 3D |
| Glass | Medium | Good electrical | High frequency |

**Pad Finish:**

```
Common finishes:
1. ENIG (Electroless Ni/Immersion Au)
   - Ni: 3-6 μm
   - Au: 0.05-0.15 μm
   - Flat, solderable
   - Cost: Medium

2. OSP (Organic Solderability Preservative)
   - Thickness: 0.2-0.5 μm
   - Low cost
   - Limited shelf life (6 months)

3. Immersion Sn or Ag
   - Thickness: 0.5-1 μm
   - Good solderability
   - Moderate cost
```

### Flux Application

**Purpose:**
- Remove oxides
- Improve wetting
- Prevent re-oxidation during reflow

**Application Methods:**

```
1. Dipping:
   - Dip substrate in flux
   - Drain excess
   - Simple, high coverage
   
2. Printing:
   - Screen or stencil print
   - Controlled volume
   - Better for selective areas

3. Spraying:
   - Atomized flux spray
   - Thin, uniform coating
   - Less residue

4. Tacky flux (on substrate):
   - Holds die during placement
   - Prevents movement before reflow
```

**Flux Types:**

| Type | Activity | Residue | Cleaning | Applications |
|------|----------|---------|----------|--------------|
| No-clean | Low | Minimal | Not required | High volume |
| Water-soluble | Medium | High | DI water | Standard |
| Rosin-based | Medium | Moderate | Solvent | Traditional |

### Die Placement

**Pick and Place:**

```
Process:
1. Pick die from wafer/film frame
   - Vacuum collet or gripper
2. Align to substrate
   - Vision system (pattern recognition)
   - Accuracy: ±10-25 μm
3. Place die on substrate
   - Light pressure (bond line control)

Throughput: 100-500 dies/hour
Placement accuracy: ±10 μm (high-end)
                    ±25 μm (standard)
```

**Alignment Methods:**

```
1. Vision alignment:
   - Camera sees fiducial marks
   - Die and substrate marks
   - Accuracy: ±5-10 μm

2. Mechanical alignment:
   - Physical guides/stops
   - Lower accuracy (±25 μm)
   - Faster, lower cost

3. Self-alignment:
   - Surface tension during reflow
   - Corrects ±25-50 μm misalignment
   - Molten solder pulls die to center
```

### Reflow Process

**Temperature Profile:**

```
SAC305 Solder (Melting point: 217°C):

Zone 1 - Preheat:
- Temperature: 150-180°C
- Time: 60-90 sec
- Rate: 1-3°C/sec
- Purpose: Activate flux, remove solvents

Zone 2 - Soak:
- Temperature: 180-200°C
- Time: 60-120 sec
- Purpose: Uniform temperature, flux activation

Zone 3 - Reflow:
- Peak temperature: 240-260°C (Tₘ + 25-40°C)
- Time above liquidus (TAL): 30-90 sec
- Ramp rate: 2-4°C/sec
- Purpose: Solder melts, wets, forms joint

Zone 4 - Cooling:
- Rate: 2-4°C/sec to 150°C
- Then natural cooling
- Purpose: Solidify with fine grain structure

Total time: 4-8 minutes
```

**Atmosphere:**

```
Air reflow:
- Simple, low cost
- May have oxidation
- Acceptable for most applications

Nitrogen (N₂) reflow:
- <100 ppm O₂
- Better wetting
- Less oxidation
- Higher cost
- Required for fine pitch, high reliability
```

**Reflow Methods:**

| Method | Heating | Advantages | Applications |
|--------|---------|------------|--------------|
| Convection oven | Hot air | Uniform, batch | High volume |
| IR reflow | Infrared radiation | Fast heating | Medium volume |
| Vapor phase | Condensing vapor | Excellent uniformity | High-end |
| Laser reflow | Focused laser | Selective, rework | Repair, R&D |

### Self-Alignment Effect

**Mechanism:**

```
During reflow, surface tension centers die:

Restoring force ∝ γ × Perimeter × sin(θ)

Where:
γ = surface tension of molten solder
θ = misalignment angle

Typical correction: ±25-50 μm
Maximum: ±100 μm (for large die)

Requirements:
- Symmetrical bump pattern
- Similar bump sizes
- Adequate wetting
```

## Underfill

Critical for reliability - distributes stress between die and substrate.

### Purpose

**Without Underfill:**
```
CTE mismatch stress concentrated at solder joints
- Si die: CTE = 2.6 ppm/°C
- Organic substrate: CTE = 17 ppm/°C
- ΔT = 100°C → 1.4 mm/m mismatch
- Result: Joint fatigue, early failure (100-500 cycles)
```

**With Underfill:**
```
Polymer fills gap, bonds die to substrate
- Distributes stress over entire die area
- Reduces strain on solder joints by 10-50×
- Result: Reliable operation (>5000 cycles)
```

### Underfill Materials

**Properties:**

| Property | Typical Value | Requirements |
|----------|---------------|--------------|
| Glass transition (Tg) | 120-160°C | >125°C for automotive |
| CTE (<Tg) | 20-40 ppm/°C | Match substrate/die |
| CTE (>Tg) | 60-120 ppm/°C | Minimize |
| Filler content | 50-70 wt% | For CTE matching |
| Viscosity | 1-50 Pa·s | Flow vs cure time |
| Cure temperature | 150-175°C | Compatible with package |
| Cure time | 30-60 min | Throughput |

**Filler Materials:**
- Silica (SiO₂): Most common, spherical
- Alumina (Al₂O₃): Higher thermal conductivity
- Size: 0.5-20 μm (smaller for fine pitch)

### Dispense Methods

#### 1. Capillary Underfill (CUF)

Most common, uses capillary action to fill gap.

**Process:**

```
1. Flip chip assembly (post-reflow)
2. Dispense underfill along die edge
   - L-pattern or U-pattern
   - Needle dispense or jetting
3. Capillary flow under die
   - Flow rate: 1-5 mm/sec
   - Time: 10-60 sec for 5-15 mm die
4. Cure in oven
   - Temperature: 150-175°C
   - Time: 30-60 min

Gap height: 30-80 μm typical
Flow distance: Half die size
```

**Flow Time Calculation:**

```
Washburn equation:
L² = (γ × D × t) / (4η)

Where:
L = flow distance (m)
γ = surface tension (N/m)
D = hydraulic diameter (gap height)
η = viscosity (Pa·s)
t = time (s)

Example:
γ = 0.03 N/m
D = 50 μm
η = 5 Pa·s
L = 7.5 mm (half of 15 mm die)

t = (4η × L²) / (γ × D)
t = (4 × 5 × 0.0075²) / (0.03 × 50×10⁻⁶)
t ≈ 75 seconds
```

**Advantages:**
- Simple process
- Good void control
- Standard equipment

**Limitations:**
- Two-step process (reflow then underfill)
- Slow for large die
- Voids possible

#### 2. No-Flow Underfill (NUF)

Underfill applied before reflow.

**Process:**

```
1. Dispense underfill on substrate
   - Controlled volume and pattern
2. Place die (bumps into underfill)
3. Reflow
   - Solder melts through underfill
   - Underfill cures during reflow
4. Single thermal cycle

Materials:
- Low viscosity (0.5-5 Pa·s)
- Stable during reflow
- Flux activity built-in
```

**Advantages:**
- Single process step
- Faster cycle time
- Lower cost

**Limitations:**
- Material more expensive
- More sensitive to process
- Requires precise volume control

#### 3. Molded Underfill

Transfer molding after flip chip assembly.

**Process:**

```
1. Flip chip assembly (standard)
2. Transfer mold
   - Epoxy molding compound
   - Fills gap and encapsulates
   - Temperature: 175-185°C
   - Pressure: 4-8 MPa
   - Time: 2-5 min
3. Post-mold cure

Material:
- Higher filler content (>80%)
- Lower CTE than liquid underfill
- Epoxy-based
```

**Advantages:**
- Very fast (minutes)
- Low void rate
- Good for high volume

**Limitations:**
- Requires molding equipment
- Higher material cost
- Fillet shape different

### Void Control

**Void Sources:**
```
1. Air entrapment during flow
2. Moisture evaporation
3. Flux volatiles
4. Poor wetting

Impact:
- Small voids (<100 μm): Minimal
- Large voids (>500 μm): Reliability risk
- Voids at bumps: Critical failure

Acceptance: <5% total void area
```

**Void Reduction:**

```
Process:
- Vacuum-assisted dispense
- Preheat substrate (50-80°C)
- Optimize dispense pattern
- Control cure profile (slow initial ramp)

Material:
- Low viscosity
- Good wetting
- Degassed material
- Controlled cure rate
```

## Process Variations

### Fine Pitch Flip Chip

**Challenges:**

```
Pitch <100 μm:
- Smaller bumps (30-80 μm)
- Tighter alignment tolerance (±5 μm)
- Finer underfill filler (0.5-2 μm)
- More sensitive to coplanarity

Solutions:
- Copper pillar bumps
- Advanced placement equipment
- Non-conductive paste (NCP) or film (NCF)
- Micro-bumping technology
```

### Non-Conductive Materials

**NCP (Non-Conductive Paste):**

```
Composition:
- Epoxy resin (thermosetting)
- Filler (silica, no conductive particles)
- Flux agents

Process:
1. Print NCP on substrate or die
2. Place die (bumps into NCP)
3. Cure while applying pressure
   - Temperature: 180-200°C
   - Pressure: 1-5 MPa
   - Time: 10-30 sec
4. Electrical connection by compression

Advantages:
- No separate underfill step
- Fine pitch capable (<50 μm)
- Fast process

Applications:
- LCD drivers
- Fine pitch ICs
```

**NCF (Non-Conductive Film):**

```
Film laminated before bonding
Similar to NCP but pre-formed
Easier handling, better uniformity
```

### Anisotropic Conductive Film (ACF)

**Structure:**

```
Film composition:
- Epoxy matrix
- Conductive particles (5-20 μm)
- Particle density: 5,000-20,000 per mm²
- Particle concentration: 1-5 vol%

Mechanism:
Z-axis (vertical): Conductive via particles
X-Y axis (lateral): Insulating (particle spacing)
```

**Process:**

```
1. Pre-bond: Tack film to substrate (80-100°C)
2. Align and place die
3. Final bond:
   - Temperature: 150-200°C
   - Pressure: 50-100 MPa
   - Time: 5-30 sec
   - Particles trapped and deformed between bumps

Result:
- Electrical connection via particles
- Mechanical bond via cured epoxy
```

**Applications:**
- Display connections (LCD, OLED)
- Flex circuits
- Low-cost devices

## Reliability

### Failure Mechanisms

**1. Thermal Cycling Fatigue:**

```
Cause: CTE mismatch between die and substrate
Effect: Shear strain on solder joints

Without underfill:
- Characteristic life: 100-500 cycles (-40 to 125°C)
- Failure: Crack propagation in solder

With underfill:
- Characteristic life: >5,000 cycles
- 10-50× improvement
```

**Coffin-Manson Model:**

```
N_f = C × (ΔT)^(-n) × (f)^(-m)

Where:
N_f = cycles to failure
ΔT = temperature range
f = frequency (cycles/hour)
C, n, m = material constants

Typical: n = 2-3, m = 0.3-0.5
```

**2. Electromigration:**

```
High current density → atomic migration

Critical current density:
j_crit ≈ 10⁴ A/cm² (SnPb solder at 100°C)
j_crit ≈ 10⁵ A/cm² (Cu pillar)

Cu pillar advantage: 10× better
```

**3. Intermetallic Growth:**

```
Solder + UBM → Intermetallic compounds (IMC)

Example: SAC305 on Cu UBM
Cu₆Sn₅ forms at interface
Growth rate ∝ √(D × t) where D = diffusion coefficient

At 125°C, 1000h:
IMC thickness: 5-10 μm (acceptable)
Too thick (>20 μm): Brittle, crack risk
```

**4. Underfill Delamination:**

```
Cause:
- Moisture absorption
- CTE mismatch
- Poor adhesion

Prevention:
- Plasma clean before underfill
- Adhesion promoter
- Moisture bake (125°C, 24h) before test
```

### Reliability Testing

**Temperature Cycling:**

```
Condition A: -55°C ↔ +125°C
Condition B: -40°C ↔ +125°C
Condition G: 0°C ↔ +100°C

Dwell time: 10-15 min each extreme
Ramp rate: 10-20°C/min
Cycles: 500-2000

Acceptance criteria:
- <1% failure at 1000 cycles (standard)
- <0.1% at 500 cycles (high reliability)

Monitor: Electrical continuity (daisy chain)
```

**High Temperature Storage:**

```
Temperature: 150°C (standard), 175°C (harsh)
Duration: 500-1000 hours

Monitors:
- Resistance increase (<10% acceptable)
- Intermetallic growth
- Delamination (SAM, X-ray)
```

**HAST (Highly Accelerated Stress Test):**

```
Conditions:
- Temperature: 130°C
- Humidity: 85% RH
- Bias voltage: 3.3-5V
- Duration: 96-264 hours

Failure modes:
- Corrosion
- Electrochemical migration
- Intermetallic growth

Equivalence: ~2-5 years field operation
```

### Quality Control

**X-Ray Inspection:**

```
Capabilities:
- Bump alignment (±5 μm detection)
- Voids in solder (>20 μm)
- Underfill voids (>50 μm)
- Cracks (>10 μm)

Methods:
- 2D transmission X-ray (standard)
- 3D CT scan (detailed analysis)

Acceptance:
- Bump void <20% area
- Underfill void <5% total area
- No cracks at bumps
```

**Acoustic Microscopy (SAM):**

```
Detects delamination via ultrasound reflection

Frequency: 15-100 MHz
Resolution: 10-50 μm
Penetration: Up to 10 mm

Indications:
- White areas: Good adhesion
- Dark areas: Delamination, voids
- Critical: Delamination at bump interface
```

**Electrical Test:**

```
Daisy chain:
- Series connection of all bumps
- Measures total resistance
- Detects opens, high resistance

4-wire measurement:
- Eliminates probe resistance
- Resolution: 0.1 mΩ
- Acceptance: <100 mΩ per bump (typical)
```

## Cost Analysis

**Equipment:**

```
Bumping (wafer level):
- Sputtering tool: $500K-1M
- Electroplating: $200K-500K
- Reflow oven: $100K-300K

Assembly:
- Pick & place: $200K-500K
- Reflow oven: $100K-200K
- Underfill dispense: $150K-300K

Inspection:
- X-ray: $100K-500K
- AOI: $150K-300K
```

**Operating Costs (per die):**

```
Materials:
- Bumping: $0.05-0.20 (200-500 bumps)
- Flux: $0.001-0.005
- Underfill: $0.02-0.10
- Substrate: $0.10-1.00 (depends on type)

Total materials: $0.17-1.30 per die

Labor + overhead: $0.50-2.00 per die
Testing: $0.10-0.50 per die

Total cost: $1-4 per assembled die
(vs $0.50-1.50 for wire bond)

Cost justified by:
- Performance benefits
- Smaller package
- Higher reliability
```

## Design Guidelines

### Best Practices ✓

```
✓ Bump pitch ≥100 μm (standard), ≥40 μm (fine pitch)
✓ Bump diameter: 0.5-0.7× pitch
✓ Keep-out zone at die edge: 200-500 μm
✓ Symmetrical bump pattern (for self-alignment)
✓ Ground/power bumps in center (thermal)
✓ Test bumps for electrical monitoring
✓ Fiducial marks for alignment (3 minimum)
✓ UBM pad 10-20 μm larger than solder
✓ Substrate pad slightly larger than bump
✓ Underfill compatible with die passivation
```

### Avoid ✗

```
✗ Bumps near die corners (high stress)
✗ Large bump size variation (>10%)
✗ Asymmetric patterns (poor self-alignment)
✗ Bumps over fragile structures
✗ Mixed bump types on same die
✗ Inadequate UBM thickness (<0.5 μm)
✗ Narrow streets between bumps (<pitch/2)
✗ Large area without bumps (warpage risk)
✗ Bumps too close to edge (<200 μm)
```

## References

1. Lau, J. H. (1996). *Flip Chip Technologies*. McGraw-Hill.

2. Liu, J., & Lai, Z. (1999). Underfill flow characteristics and void formation in flip-chip encapsulation. *IEEE Transactions on Components and Packaging Technologies*, 22(2), 331-337.

3. Tu, K. N. (2007). Solder joint technology. *Springer*.

4. Gerber, M., et al. (2011). Next generation fine pitch Cu pillar technology. *IEEE Electronic Components and Technology Conference*, 612-618.

---

**Document Information:**
- **Created:** December 15, 2025
- **Version:** 1.0
- **Status:** Complete
- **Part of:** Silicon Fabrication Handbook
- **Next Chapter:** [Wafer-Level Packaging](wafer-level-packaging.md)
- **Previous Chapter:** [Wire Bonding](wire-bonding.md)

**License:** CC BY 4.0 - Free to use with attribution

---

*For questions, corrections, or contributions, please visit:*
https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook
