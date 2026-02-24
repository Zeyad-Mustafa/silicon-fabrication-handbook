# Sacrificial Layers in MEMS Surface Micromachining

## Table of Contents
- [Introduction](#introduction)
  - [Key Functions](#key-functions)
  - [Selection Criteria](#selection-criteria)
- [Sacrificial Layer Materials](#sacrificial-layer-materials)
  - [Material Comparison Table](#material-comparison-table)
- [Silicon Dioxide (SiO₂)](#silicon-dioxide-sio₂)
  - [Deposition Methods](#deposition-methods)
  - [Wet Etching of SiO₂](#wet-etching-of-sio₂)
  - [Vapor HF Etching](#vapor-hf-etching)
- [Photoresist](#photoresist)
  - [Applications](#applications)
  - [Process Flow Example](#process-flow-example)
  - [Removal Methods](#removal-methods)
- [Metals (Al, Cu)](#metals-al-cu)
  - [Aluminum Sacrificial Layers](#aluminum-sacrificial-layers)
  - [Copper Sacrificial Layers](#copper-sacrificial-layers)
- [Polymers](#polymers)
  - [Polyimide](#polyimide)
  - [SU-8](#su-8)
- [Process Integration](#process-integration)
  - [Multi-Layer Stack Design](#multi-layer-stack-design)
  - [Lateral Etch Rate](#lateral-etch-rate)
  - [Sequential Release Example](#sequential-release-example)
- [Design Considerations](#design-considerations)
  - [Etch Hole Design](#etch-hole-design)
  - [Stress Management](#stress-management)
  - [Selectivity Requirements](#selectivity-requirements)
- [Troubleshooting](#troubleshooting)
  - [Common Issues and Solutions](#common-issues-and-solutions)
  - [Process Monitoring](#process-monitoring)
- [Advanced Techniques](#advanced-techniques)
  - [Vapor Release (XeF₂)](#vapor-release-xef₂)
  - [Timed Release with Monitoring](#timed-release-with-monitoring)
- [Safety and Environmental Considerations](#safety-and-environmental-considerations)
  - [HF Safety](#hf-safety)
  - [Waste Management](#waste-management)
- [Design Example](#design-example)
  - [Cantilever Beam Release](#cantilever-beam-release)
- [References](#references)

## Introduction

Sacrificial layers are temporary materials deposited between structural layers in MEMS fabrication. They define the gaps and cavities required for device operation and are removed during the release step to create free-standing structures.

### Key Functions

1. **Gap Definition**: Control separation between structural elements
2. **Support During Fabrication**: Maintain mechanical stability
3. **Pattern Transfer**: Define device geometry
4. **Anchor Protection**: Shield fixed regions during release

### Selection Criteria

The ideal sacrificial material must:
- Have high etch selectivity to structural layer (>100:1)
- Deposit uniformly and conformally
- Be compatible with subsequent process steps
- Release without attacking structural material
- Leave minimal residue after removal

## Sacrificial Layer Materials

### Material Comparison Table

| Material | Etch Chemistry | Typical Etch Rate | Selectivity to Poly-Si | Applications |
|----------|----------------|-------------------|----------------------|--------------|
| SiO₂ | HF (49%) | 100-200 nm/min | >1000:1 | General purpose |
| PSG | HF (49%) | 300-500 nm/min | >1000:1 | Fast release |
| Photoresist | O₂ plasma | 1-5 μm/min | N/A | Temporary masking |
| Al | H₃PO₄/HNO₃ | 200-400 nm/min | >500:1 | Low-temp process |
| Polyimide | O₂ plasma | 500 nm/min | N/A | Thick layers |
| a-Si | XeF₂ | 1-3 μm/min | Infinite | Vapor release |

## Silicon Dioxide (SiO₂)

The most common sacrificial material in polysilicon surface micromachining.

### Deposition Methods

**1. Thermal Oxidation**
```
Si + O₂ → SiO₂
Temperature: 900-1100°C
Growth rate: 10-100 nm/hr
```

**Advantages:**
- Excellent quality
- High density
- Good step coverage

**Limitations:**
- Requires Si substrate
- Slow for thick layers
- High temperature

**2. LPCVD PSG (Phosphosilicate Glass)**
```
SiH₄ + PH₃ + O₂ → SiO₂:P
Temperature: 400-450°C
Pressure: 200-500 mTorr
Deposition rate: 10-50 nm/min
```

**Typical Recipe:**
- SiH₄: 100 sccm
- PH₃ (2% in N₂): 50 sccm
- O₂: 200 sccm
- Temperature: 425°C
- Pressure: 300 mTorr
- P content: 4-8 wt%

**Benefits of PSG:**
- Higher etch rate than undoped oxide (3-5×)
- Planarization after reflow (900-1000°C)
- Reduced stress through P doping
- Getters mobile ions

**3. PECVD Oxide**
```
Temperature: 250-350°C
Power: 20-50 W
Pressure: 500-1000 mTorr
Deposition rate: 50-200 nm/min
```

**Advantages:**
- Low temperature
- Fast deposition
- Good gap fill

**Disadvantages:**
- Lower density
- Higher etch rate variability
- May contain H₂O

### Wet Etching of SiO₂

**HF-Based Etching**

Concentrated HF (49%):
```
SiO₂ + 6HF → H₂SiF₆ + 2H₂O
Etch rate: 100-200 nm/min
Temperature: 20-25°C
```

Buffered HF (BHF, 7:1 NH₄F:HF):
```
Etch rate: 80-120 nm/min
Better uniformity
Less surface roughness
pH buffered (~4.5)
```

**Process Parameters:**
- Etch time calculation: t = (thickness / etch_rate) × 1.5 (safety factor)
- Agitation: Improves uniformity
- Temperature control: ±1°C
- Rinse: DI water, 5-10 min

**Etch Rate Variation:**
- PSG (6% P): 3-5× faster than thermal oxide
- PECVD oxide: 1.5-2× faster than thermal oxide
- Thermal oxide: ~100 nm/min (49% HF)

### Vapor HF Etching

**Advantages over wet HF:**
- No stiction issues
- Isotropic but controlled
- Suitable for high aspect ratio structures
- Real-time monitoring possible

**Process:**
```
Temperature: 30-40°C
Pressure: 1-10 Torr
HF vapor concentration: controlled by temperature
Etch rate: 10-50 nm/min
```

## Photoresist

Temporary sacrificial material for multi-layer processes.

### Applications

1. **Molding Material**: Define cavities for electroplating
2. **Temporary Support**: During intermediate steps
3. **Planarization**: Fill trenches before deposition

### Process Flow Example

```
1. Spin resist: 1-100 μm thick
2. Soft bake: 90-110°C, 1-5 min
3. Pattern (if needed)
4. Hard bake: 120-150°C, 30 min
5. Deposit structural layer
6. Remove resist: O₂ plasma or solvent
```

### Removal Methods

**Oxygen Plasma (Ashing):**
```
O₂ + resist → CO₂ + H₂O + volatiles
Power: 100-500 W
Pressure: 200-500 mTorr
Temperature: 100-250°C
Etch rate: 1-5 μm/min
```

**Wet Stripping:**
- Acetone/IPA: Fast but may leave residue
- PRS-type strippers: Complete removal
- Temperature: 60-80°C
- Time: 10-30 min

## Metals (Al, Cu)

Used in low-temperature processes or where oxide is unsuitable.

### Aluminum Sacrificial Layers

**Deposition:**
- PVD sputtering: 100-500 nm
- E-beam evaporation: 200-1000 nm
- Temperature: <150°C

**Etching:**
```
Al etchant: H₃PO₄:HNO₃:CH₃COOH:H₂O
Ratio: 16:1:1:2 (Type A)
Temperature: 40-50°C
Etch rate: 200-400 nm/min
Selectivity to SiO₂: >20:1
Selectivity to Si: >50:1
```

**Applications:**
- Polymer MEMS (PDMS, SU-8)
- Bio-MEMS (avoid HF)
- Low-temperature processes (<400°C)

**Limitations:**
- Galvanic corrosion with other metals
- Poor selectivity to some polymers
- Surface roughness after removal

### Copper Sacrificial Layers

**Advantages:**
- Higher etch rate than Al
- Better step coverage (electroplating)
- Suitable for thick layers (>10 μm)

**Etching:**
```
FeCl₃ solution (20-40%)
Temperature: 20-40°C
Etch rate: 0.5-2 μm/min
Or: H₂SO₄ + H₂O₂
```

## Polymers

### Polyimide

**Deposition:**
- Spin coating: 1-50 μm per coat
- Cure: 350°C, N₂, 1 hr
- Multiple coats for thick layers

**Removal:**
```
O₂ plasma:
- Power: 200-500 W
- Pressure: 300 mTorr
- Etch rate: 0.5-1 μm/min

Wet etching:
- KOH solution (45%)
- Temperature: 80-100°C
- Etch rate: 1-3 μm/min
```

**Applications:**
- Thick sacrificial layers (>10 μm)
- Flexible MEMS
- Low stress requirements

### SU-8

**Properties:**
- Negative photoresist
- Thick coatings: 1-500 μm
- High aspect ratio structures
- Chemically resistant

**As Sacrificial Layer:**
- Pattern before structural deposition
- Remove with: Piranha (H₂SO₄:H₂O₂) or RIE O₂ plasma
- Time-consuming removal for thick layers
- Limited selectivity

## Process Integration

### Multi-Layer Stack Design

**Standard 3-Layer Process:**
```
Substrate (Si)
  |
  ├── PSG (2 μm) ← First sacrificial layer
  |     |
  |     └── Poly-Si (2 μm) ← First structural layer
  |           |
  |           └── PSG (2 μm) ← Second sacrificial layer
  |                 |
  |                 └── Poly-Si (3 μm) ← Second structural layer
```

**Key Considerations:**

1. **Thickness Selection:**
   - Minimum gap: 0.5-1 μm (device dependent)
   - Typical range: 1-3 μm
   - Trade-off: capacitance vs. release time

2. **Etch Access Holes:**
   - Diameter: 2-10 μm
   - Spacing: 50-200 μm
   - Shape: circular (best) or rectangular
   - Placement: symmetrical for uniform release

3. **Anchor Design:**
   - Protected during release
   - Defined in structural layer patterning
   - Overlap with substrate: 2-5 μm minimum

### Lateral Etch Rate

For structures with buried sacrificial layers:

```
Lateral etch distance: L_etch = R_etch × t

Where:
L_etch = distance from etch hole
R_etch = lateral etch rate (0.8-1.2 × vertical rate)
t = etch time
```

**Release Time Estimation:**
```
For uniform release from etch holes spaced D apart:
t_release = D / (2 × R_lateral) + safety_factor

Typical safety factor: 1.5-2.0
```

### Sequential Release Example

**Device:** Accelerometer with comb drive actuator

**Process:**
1. Deposit PSG (2 μm) - first sacrificial layer
2. Pattern etch holes in PSG
3. Deposit poly-Si (2 μm) - proof mass
4. Dope and anneal poly-Si
5. Pattern poly-Si
6. Deposit PSG (1.5 μm) - second sacrificial layer
7. Pattern etch holes
8. Deposit poly-Si (3 μm) - comb fingers
9. Dope and pattern
10. Release in HF (6:1 BHF, 30-45 min)
11. Rinse and dry (critical step)

## Design Considerations

### Etch Hole Design

**Optimal Sizing:**

Circular holes:
```
d_min = 2 μm (avoid clogging)
d_typical = 5-8 μm
d_max = 15 μm (structural integrity)
```

Spacing:
```
S = 2 × L_max
Where L_max = maximum acceptable etch distance
```

**Pattern Density:**
- High density: Faster release, weaker structure
- Low density: Slower release, stronger structure
- Typical: 1-3% open area

### Stress Management

Sacrificial layer stress affects overlying structures.

**PSG Stress Control:**
- P content: 4-8% → compressive stress (-50 to -200 MPa)
- Higher P → more compressive
- Anneal at 1000°C: stress relief

**PECVD Oxide:**
- As-deposited: tensile (50-150 MPa)
- Anneal at 450°C: reduces stress by 30-50%

**Impact on Devices:**
- Compressive: upward bowing of released structures
- Tensile: downward bowing or curling
- Gradient: more severe warping

### Selectivity Requirements

**Minimum Acceptable Selectivity:**
```
S_min = (t_structural / δt_acceptable) + safety_margin

Where:
t_structural = structural layer thickness
δt_acceptable = acceptable loss (typically 1-5%)
safety_margin = 2-5× for process variation

Example:
Poly-Si: 2 μm thick
Acceptable loss: 20 nm (1%)
Required selectivity: >100:1
```

## Troubleshooting

### Common Issues and Solutions

**1. Incomplete Release**

Symptoms:
- Structures stuck to substrate
- Partial movement
- Non-uniform release

Causes & Solutions:
- Insufficient etch time → Increase 20-50%
- Etch holes too small/sparse → Redesign mask
- Residual oxide → Check etch chemistry
- Low etch rate → Verify HF concentration
- Blocked etch holes → Pre-clean wafers

**2. Structural Layer Attack**

Symptoms:
- Thinning of poly-Si
- Surface roughness
- Device failure

Causes & Solutions:
- Poor selectivity → Change etchant
- Over-etching → Reduce time
- Contamination → Clean glassware
- Wrong chemistry → Verify recipe

**3. Stiction During Release**

Symptoms:
- Released structures adhered to substrate
- Permanent deformation

Causes & Solutions:
- Capillary forces during drying → Use critical point drying or freeze drying
- Residual oxide → Extend etch time
- Surface roughness → Improve deposition quality
- Hydrophobic issues → Use release agents (see next chapter)

**4. Non-Uniform Release**

Symptoms:
- Edge effects
- Center vs. edge variation

Causes & Solutions:
- Poor agitation → Add stirring or ultrasonic
- Temperature gradients → Use temperature-controlled bath
- Concentration variation → Fresh etchant, multiple baths
- Pattern density effects → Balance etch hole distribution

**5. Residue After Release**

Symptoms:
- White film on structures
- Reduced mobility
- Electrical shorts

Causes & Solutions:
- Incomplete rinse → Extend DI water rinse (15+ min)
- Re-deposition → Add surfactant to final rinse
- HF salts → Use HCl pre-rinse
- Organic contamination → Piranha clean before release

### Process Monitoring

**Key Metrics:**

1. **Etch Rate Calibration:**
   - Test wafers with known oxide thickness
   - Measure every batch
   - Document temperature and concentration

2. **Uniformity Check:**
   - Measure at 9 points across wafer
   - Within-wafer variation: <5%
   - Wafer-to-wafer: <3%

3. **Visual Inspection:**
   - Optical microscope: stiction, residue
   - SEM: surface quality, critical dimensions
   - Profilometer: released gap height

4. **Functional Testing:**
   - Electrical continuity
   - Mechanical resonance
   - Capacitance measurements

## Advanced Techniques

### Vapor Release (XeF₂)

Alternative to wet HF for silicon sacrificial layers.

**Process:**
```
Gas: XeF₂
Pressure: 1-3 Torr
Temperature: Room temperature
Reaction: Si + 2XeF₂ → SiF₄ + 2Xe
```

**Advantages:**
- No stiction
- High selectivity to SiO₂, metals
- Isotropic but controlled
- Real-time monitoring

**Applications:**
- High aspect ratio devices
- Multi-material systems
- Delicate structures

### Timed Release with Monitoring

Real-time etch depth monitoring:

1. **Electrical Method:**
   - Monitor resistance of buried conductor
   - Discontinuity indicates complete release

2. **Optical Method:**
   - Interferometry through transparent substrate
   - Measure gap height in real-time

3. **Mechanical Resonance:**
   - Actuate structure during etch
   - Release complete when resonance detected

## Safety and Environmental Considerations

### HF Safety

**Hazards:**
- Severe burns (penetrating, delayed pain)
- Bone damage (calcium chelation)
- Respiratory irritation

**Safety Measures:**
- Always use in fume hood
- Wear face shield, double gloves (nitrile over neoprene)
- HF-specific spill kit available
- Calcium gluconate gel for burns
- Never work alone

### Waste Management

**HF Waste:**
- Neutralize with Ca(OH)₂ before disposal
- Collect in designated containers
- Precipitate CaF₂ for safe disposal

**Metal Etchant Waste:**
- Treat as hazardous waste
- Do not mix with other chemicals
- Follow local regulations

## Design Example

### Cantilever Beam Release

**Specifications:**
- Beam: 200 μm long, 20 μm wide, 2 μm thick poly-Si
- Gap: 2 μm (PSG)
- Release: 6:1 BHF

**Etch Hole Design:**
```
Hole diameter: 5 μm
Spacing: 50 μm
Number of holes: 200/50 = 4 holes along length

Lateral etch required: 25 μm (from hole to beam edge)
Vertical etch rate: 100 nm/min (measured)
Lateral etch rate: 120 nm/min (1.2× vertical)

Etch time = 25 μm / 120 nm/min ≈ 210 min
Add 50% safety margin: 315 min total

Structural layer loss (worst case):
100 nm/min × 315 min × (1/1000 selectivity) = 32 nm
Loss: 1.6% (acceptable)
```

**Process:**
1. Pattern etch holes in PSG
2. Release in BHF for 315 min with agitation
3. Rinse in DI water, 15 min
4. IPA rinse, 5 min
5. Critical point dry or N₂ blow dry

## References

1. Bustillo, R. T., Howe, R. T., & Muller, R. S. (1998). Surface micromachining for microelectromechanical systems. *Proceedings of the IEEE*, 86(8), 1552-1574.

2. Gad-el-Hak, M. (Ed.). (2005). *MEMS: Design and Fabrication* (2nd ed.). CRC Press.

3. Senturia, S. D. (2001). *Microsystem Design*. Springer.

4. Williams, K. R., Gupta, K., & Wasilik, M. (2003). Etch rates for micromachining processing—Part II. *Journal of Microelectromechanical Systems*, 12(6), 761-778.

5. Kovacs, G. T. (1998). *Micromachined Transducers Sourcebook*. McGraw-Hill.

---

**Document Information:**
**Contributors**: Zeyad Mustafa
- **Created:** December 7, 2025
- **Version:** 1.0
- **Status:** Complete
- **Next Chapter:** [Release Techniques](release-techniques.md)
- **Previous Chapter:** [Polysilicon Processes](polysilicon-processes.md)
