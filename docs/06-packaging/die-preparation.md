# Die Preparation for MEMS Packaging

## Table of Contents
- [Introduction](#introduction)
  - [Process Overview](#process-overview)
  - [Key Challenges](#key-challenges)
  - [Cost Breakdown](#cost-breakdown)
- [Wafer Dicing](#wafer-dicing)
  - [Dicing Methods](#dicing-methods)
  - [Dicing Tape Selection](#dicing-tape-selection)
  - [Dicing Quality Inspection](#dicing-quality-inspection)
- [Die Handling](#die-handling)
  - [Wafer Backgrinding](#wafer-backgrinding)
  - [Die Pickup and Placement](#die-pickup-and-placement)
  - [Die Sorting and Binning](#die-sorting-and-binning)
- [Die Attach](#die-attach)
  - [Die Attach Materials](#die-attach-materials)
  - [Die Attach Process](#die-attach-process)
  - [Die Attach Curing](#die-attach-curing)
  - [CTE Mismatch Management](#cte-mismatch-management)
- [Cleanliness and Inspection](#cleanliness-and-inspection)
  - [Contamination Sources](#contamination-sources)
  - [Cleaning Methods](#cleaning-methods)
  - [Visual Inspection](#visual-inspection)
  - [X-Ray Inspection](#x-ray-inspection)
- [Quality Control](#quality-control)
  - [Key Performance Indicators (KPIs)](#key-performance-indicators-kpis)
  - [Reliability Testing](#reliability-testing)
- [Best Practices Summary](#best-practices-summary)
  - [Do's ✓](#dos)
  - [Don'ts ✗](#donts)
  - [Decision Matrix](#decision-matrix)
- [Cost Optimization](#cost-optimization)
- [References](#references)

## Introduction

Die preparation is the critical transition from wafer-level fabrication to individual packaged devices. Proper die preparation ensures device reliability, yield, and performance.

### Process Overview

```
Wafer → Backgrind → Dicing → Inspection → Die Sorting → Die Attach
```

### Key Challenges

| Challenge | Impact | Mitigation |
|-----------|--------|------------|
| Chipping | Device failure, cracking | Optimized dicing, DBG |
| Contamination | Yield loss, reliability | Clean processes, handling |
| Mechanical damage | Structural failure | Proper support, gentle handling |
| Delamination | Poor adhesion | Surface preparation, adhesive selection |
| Thermal stress | Warpage, cracking | Matched CTE materials, soft die attach |

### Cost Breakdown

Packaging typically represents 40-70% of total MEMS device cost:
```
Die preparation: 10-15%
Die attach: 15-20%
Wire bonding: 20-25%
Encapsulation: 15-20%
Testing: 20-30%
```

## Wafer Dicing

### Dicing Methods

#### 1. Blade Dicing (Mechanical Saw)

Most common method for silicon wafers.

**Process Parameters:**
```
Blade:
- Type: Resin-bonded diamond
- Thickness: 20-50 μm (standard), 15 μm (thin)
- Grit size: 2-5 μm (fine), 20-30 μm (coarse)
- RPM: 20,000-40,000

Feed Rate: 10-100 mm/s
Cut Depth: Wafer thickness + 30-50 μm (into tape)
Coolant: DI water or water + surfactant
Street Width: 50-100 μm minimum
```

**Advantages:**
- High throughput (100-300 wafers/hour)
- Low cost per die
- Mature technology
- Good for thick wafers (>500 μm)

**Limitations:**
- Chipping (5-20 μm typical)
- Kerf loss (blade width)
- Mechanical stress
- Not suitable for thin wafers (<100 μm)

**Blade Selection:**

| Wafer Type | Blade Thickness | Grit Size | Application |
|------------|-----------------|-----------|-------------|
| Standard Si (200-700 μm) | 30-40 μm | 5 μm | General purpose |
| Thin Si (<200 μm) | 20-25 μm | 2-3 μm | Low stress |
| GaAs, Glass | 30-40 μm | 3-5 μm | Brittle materials |
| Thick Si (>1 mm) | 50-70 μm | 20 μm | Fast cutting |

#### 2. Stealth Dicing (Laser)

Internal laser modification followed by tape expansion.

**Process:**
```
Step 1: Laser Scribing (Internal)
- Wavelength: 1064 nm (Nd:YAG) or 532 nm
- Focus: 100-300 μm below surface
- Spot size: 1-3 μm
- Speed: 100-300 mm/s
- Damage layer: Multi-layer modification

Step 2: Tape Expansion
- Stretch dicing tape
- Wafer fractures along modified layer
- Die separation without blade contact
```

**Advantages:**
- Zero chipping
- Narrow streets (20-30 μm)
- No kerf loss
- Suitable for thin wafers
- High quality edges

**Limitations:**
- Equipment cost (>$500K)
- Limited thickness range (50-300 μm)
- Requires special tape
- Slower than blade dicing

**Typical Applications:**
- Image sensors
- RF MEMS
- Ultra-thin dies (<100 μm)

#### 3. Plasma Dicing

Uses deep reactive ion etching (DRIE) for separation.

**Process:**
```
1. Pattern dicing streets with photoresist
2. DRIE through full wafer thickness
3. Remove resist
4. Break die free from support wafer

Parameters:
- Same as DRIE (see deep-rie.md)
- Street width: 20-50 μm
- Etch rate: 3-6 μm/min
- Total time: 1-3 hours for 200 μm
```

**Advantages:**
- Perfect sidewalls (no chipping)
- Narrowest streets (20 μm)
- Process control
- Integrated with fab

**Limitations:**
- Very slow
- Expensive
- Requires lithography step
- Complex process

#### 4. Scribe and Break

Manual or automated cleaving along crystal planes.

**Process:**
```
1. Mechanical scribe or diamond tip scratch
2. Apply stress perpendicular to scribe
3. Wafer cleaves along <110> plane

Requirements:
- <100> wafer orientation
- Rectangular die shapes only
- Clean break required
```

**Use Cases:**
- Research and development
- Low volume production
- Simple die shapes
- Thick wafers (>400 μm)

### Dicing Tape Selection

Critical for holding wafer during and after dicing.

**Types:**

| Tape Type | Adhesion | UV Cure | Temperature | Application |
|-----------|----------|---------|-------------|-------------|
| Standard | Medium | No | 80°C max | General blade dicing |
| Low adhesion | Low | No | 80°C | Thin wafers |
| UV release | High → Low | Yes (5-10 min) | 120°C | Easy die pickup |
| High temp | Medium | No | 200°C | Die attach processes |

**Key Properties:**
```
Adhesion strength: 0.1-1.0 N/25mm
Base material: PVC or polyolefin
Thickness: 80-200 μm
Tape expansion: 2-5% typical, 10-20% for stealth
```

### Dicing Quality Inspection

**Critical Measurements:**

1. **Chipping Size:**
   ```
   Specification: < 20 μm for standard
                  < 5 μm for high reliability
   
   Measurement: Optical microscope, SEM
   Location: All four corners per die
   ```

2. **Sidewall Angle:**
   ```
   Target: 88-92° (slight positive taper acceptable)
   Measurement: Cross-section, SEM
   ```

3. **Die Strength:**
   ```
   Three-point bend test:
   Force at break: > 500 gf for 5×5 mm die
   
   Lower strength indicates:
   - Excessive chipping
   - Microcracks
   - Process issues
   ```

## Die Handling

### Wafer Backgrinding

Required for thin die applications (stacking, CSP, flip-chip).

**Process Flow:**
```
1. Mount wafer face-down on temporary carrier
   - Adhesive: UV-release or thermal-release
   - Carrier: Glass or Si wafer

2. Coarse grind
   - Remove bulk material
   - Leave 20-50 μm for fine grind
   - Wheel: #320-600 grit

3. Fine grind
   - Final thickness control
   - Wheel: #2000-4000 grit
   - Achieves smooth surface

4. Optional: Backside polish
   - Mirror finish
   - Thickness uniformity: ±3 μm

5. Optional: Stress relief
   - Plasma etch 5-10 μm
   - Removes damaged layer
   - Increases die strength

6. De-mount from carrier
   - UV exposure or heat
```

**Thickness Targets:**

| Application | Thickness | Considerations |
|-------------|-----------|----------------|
| Standard packaging | 200-700 μm | No backgrind needed |
| Chip-on-Board | 100-300 μm | Moderate grind |
| 3D stacking | 50-100 μm | Requires stress relief |
| Ultra-thin | 20-50 μm | Special handling, support |

**Die Strength Enhancement:**

```
Backgrind Damage Removal:
- Plasma etch: 5-10 μm removal
- Wet etch: 10-20 μm removal

Result:
- 2-3× increase in die strength
- Reduces warpage
- Better yield in assembly
```

### Die Pickup and Placement

**Methods:**

1. **Vacuum Pickup (Collet):**
   ```
   Most common method
   
   Parameters:
   - Vacuum: -50 to -80 kPa
   - Collet size: 70-90% of die size
   - Soft tip material (PEEK, rubber)
   
   Advantages:
   - Simple, reliable
   - High speed (0.5-2 sec/die)
   
   Limitations:
   - Requires back-side vacuum seal
   - Not for ultra-thin dies
   ```

2. **Needle Ejection:**
   ```
   Pins push die from bottom while vacuum picks from top
   
   For thin dies (<100 μm):
   - Multiple small pins
   - Synchronized ejection
   - Prevents die cracking
   ```

3. **Electrostatic Chuck:**
   ```
   Uses electrostatic force instead of vacuum
   
   Advantages:
   - Works for porous materials
   - Uniform holding force
   - No vacuum holes needed
   
   Voltage: 200-2000 V DC
   ```

### Die Sorting and Binning

**Automated Die Sorting:**

```
Process:
1. Wafer map from probe test
2. Vision system aligns die
3. Pick die from tape
4. Sort into bins by:
   - Pass/Fail (electrical test)
   - Performance grade (A, B, C)
   - Visual inspection
   
Throughput: 5,000-15,000 UPH (units per hour)
```

**Bin Categories:**

| Bin | Description | Yield Impact | Action |
|-----|-------------|--------------|--------|
| Bin 1 | Fully functional, Grade A | Revenue | Ship |
| Bin 2 | Functional, Grade B | Reduced margin | Sell as lower grade |
| Bin 3 | Marginal performance | Depends | Re-test or scrap |
| Bin 4 | Failed electrical test | Loss | Scrap |
| Bin 5 | Visual defects | Loss | Scrap |

## Die Attach

### Die Attach Materials

#### 1. Epoxy Adhesives

Most common for non-hermetic packages.

**Types:**

**Silver-Filled Epoxy:**
```
Composition: 70-80% Ag particles in epoxy resin
Thermal conductivity: 2-4 W/m·K
Electrical conductivity: Conductive
Cure: 150-175°C, 30-60 min
CTE: 30-50 ppm/°C

Applications:
- Power devices
- LED packages
- Standard MEMS

Cost: $50-200 per kg
```

**Non-Conductive Epoxy:**
```
Thermal conductivity: 0.5-1.5 W/m·K
Electrical: Insulating (>10¹² Ω·cm)
Cure: 120-150°C, 30 min
CTE: 40-70 ppm/°C

Applications:
- Sensors
- Low-power ICs

Cost: $20-80 per kg
```

**Thermal Epoxy:**
```
Filled with: Al₂O₃, AlN, BN
Thermal conductivity: 3-10 W/m·K
Electrical: Insulating
CTE: 20-40 ppm/°C

Applications:
- High-power devices
- Thermal management critical

Cost: $100-400 per kg
```

#### 2. Solder

For hermetic and high-reliability packages.

**Common Alloys:**

| Alloy | Melting Point | Thermal Conductivity | CTE | Application |
|-------|---------------|---------------------|-----|-------------|
| 63Sn-37Pb (eutectic) | 183°C | 50 W/m·K | 25 ppm/°C | Legacy |
| Sn-3.5Ag | 221°C | 33 W/m·K | 22 ppm/°C | Lead-free |
| 80Au-20Sn (eutectic) | 280°C | 57 W/m·K | 16 ppm/°C | High reliability |
| Sn-3.0Ag-0.5Cu (SAC305) | 217°C | 60 W/m·K | 23 ppm/°C | Standard lead-free |

**Process:**
```
1. Apply solder preform or paste
2. Place die
3. Reflow in oven or on hotplate
   - Temperature: Melting point + 20-40°C
   - Time: 1-5 minutes
   - Atmosphere: N₂ or forming gas

4. Cool naturally or controlled
```

**Advantages:**
- Excellent thermal conductivity
- Hermetic seal possible
- Reworkable
- Well-defined interface

**Disadvantages:**
- Higher temperature
- Flux residue (requires cleaning)
- Thermal cycling fatigue

#### 3. Conductive Tapes

For quick assembly or sensitive devices.

**Double-Sided Adhesive:**
```
Types:
- Acrylic adhesive (80-150°C max)
- Silicone adhesive (200°C max)

Thermal conductivity: 0.5-3 W/m·K
Thickness: 10-100 μm

Advantages:
- Room temperature process
- Fast (instant adhesion)
- No cure time
- Reworkable

Disadvantages:
- Lower thermal conductivity
- Outgassing concerns
- Limited temperature range
```

### Die Attach Process

**Dispensing Methods:**

1. **Screen Printing:**
   ```
   For large die (>5×5 mm), high volume
   
   Pattern: Metal screen with openings
   Paste: Viscosity 150-300 Pa·s
   Thickness: 25-100 μm
   Accuracy: ±25 μm
   Speed: 1000-3000 UPH
   ```

2. **Needle Dispensing:**
   ```
   For small die (<5×5 mm), flexible
   
   Needle gauge: 22-30 (larger = more flow)
   Pressure: 0.1-0.5 MPa
   Dot size: 0.2-2 mm diameter
   Thickness: 20-50 μm
   Speed: 2000-5000 UPH
   Accuracy: ±10 μm
   ```

3. **Jetting:**
   ```
   Non-contact, high precision
   
   Droplet size: 10-100 pL
   Placement accuracy: ±5 μm
   Speed: 300-1000 dots/sec
   Materials: Low viscosity (<50 Pa·s)
   ```

**Placement Accuracy:**
```
Standard: ±50 μm
Fine pitch: ±25 μm
Ultra-fine: ±10 μm

Factors affecting accuracy:
- Die size and weight
- Adhesive viscosity
- Placement speed
- Vision system resolution
```

### Die Attach Curing

**Thermal Cure (Oven):**
```
Profile:
1. Ramp: 2-5°C/min to cure temperature
2. Soak: 150-175°C for 30-60 min
3. Cool: Natural or forced air

Atmosphere: Air or N₂
Batch size: 100-1000 units
```

**Snap Cure (Hotplate):**
```
Contact heating for faster throughput

Temperature: 175-200°C
Time: 30-180 seconds
Pressure: Light contact
Throughput: 5000-10000 UPH
```

**UV Cure:**
```
For UV-curable adhesives

Wavelength: 365 nm (UV-A)
Intensity: 50-500 mW/cm²
Time: 5-60 seconds
Advantages: Fast, low temperature
Limitation: Line of sight required
```

### CTE Mismatch Management

**Thermal Stress:**
```
Stress = ΔT × ΔCTE × E

Where:
ΔT = temperature change
ΔCTE = CTE difference
E = Young's modulus

Example:
Si die (CTE = 2.6 ppm/°C) on FR-4 (CTE = 17 ppm/°C)
ΔT = 100°C (room temp to cure)
ΔCTE = 14.4 ppm/°C

Stress ∝ 1.44 mm/m over 100°C
Result: Warpage, delamination risk
```

**Solutions:**

1. **Compliant Die Attach:**
   ```
   Use soft, thick adhesive layer
   - Silicone-based (Shore A 20-40)
   - Thickness: 50-100 μm
   - Absorbs stress
   ```

2. **Matched CTE Substrates:**
   ```
   Material CTE matching:
   - Si: 2.6 ppm/°C
   - AlN: 4.5 ppm/°C (good match!)
   - Ceramic (Al₂O₃): 6.5 ppm/°C
   - Copper: 17 ppm/°C (poor match)
   - FR-4: 17 ppm/°C (poor match)
   ```

3. **Thin Die:**
   ```
   Thinner die = more flexible = less stress
   Target: <200 μm for plastic packages
   ```

## Cleanliness and Inspection

### Contamination Sources

**Particle Contamination:**
```
Sources:
- Dicing debris (Si, resin)
- Tape residue
- Handling equipment
- Ambient cleanroom

Acceptable levels:
- Class 1000 (ISO 6): <1000 particles >0.5μm per ft³
- Class 100 (ISO 5): <100 particles >0.5μm per ft³
```

**Organic Contamination:**
```
Sources:
- Adhesive outgassing
- Flux residue
- Skin oils, handling

Measurement:
- FTIR (Fourier Transform Infrared)
- Contact angle (hydrophobic = contaminated)
```

### Cleaning Methods

**1. Plasma Cleaning:**
```
Best for organic removal before die attach

Process:
- Gas: O₂ or O₂/Ar mixture
- Power: 50-200 W
- Pressure: 100-500 mTorr
- Time: 30-300 seconds

Effect:
- Removes organics
- Activates surface (improves adhesion)
- No liquid, no residue
```

**2. Solvent Cleaning:**
```
For flux residue, heavy contamination

Process:
- Solvent: IPA, acetone, or specialized
- Method: Spray, immersion, or ultrasonic
- Temperature: Room temp or 40-60°C
- Rinse: DI water
- Dry: N₂ blow or spin dry

Concerns:
- Solvent compatibility
- Residue from solvent itself
- Drying uniformity
```

**3. DI Water Rinse:**
```
Final rinse after other cleaning

Resistivity: >15 MΩ·cm
Flow: Spray or immersion
Time: 30-60 seconds
Dry: Centrifugal (spin dry) or N₂ gun
```

### Visual Inspection

**Automated Optical Inspection (AOI):**
```
Capabilities:
- Die cracks (>5 μm)
- Chipping (>10 μm)
- Contamination (>20 μm)
- Die placement (±10 μm)
- Adhesive voids (>100 μm)

Speed: 5-30 sec per unit
Resolution: 1-5 μm
```

**Defect Categories:**

| Defect Type | Severity | Action |
|-------------|----------|--------|
| Micro-crack | Critical | Reject |
| Chipping >50 μm | Critical | Reject |
| Contamination (organic) | Major | Clean and re-inspect |
| Die tilt >5° | Major | Reject or rework |
| Small particles | Minor | Accept or clean |
| Cosmetic only | Minor | Accept |

### X-Ray Inspection

For die attach void analysis.

**Capabilities:**
```
Detection:
- Voids in die attach (>50 μm)
- Delamination
- Solder joint quality
- Internal structure

Method:
- 2D transmission X-ray
- 3D CT (Computed Tomography)

Acceptance Criteria:
- Total void area: <10% for standard
                   <5% for high reliability
- No large single voids (>500 μm)
```

## Quality Control

### Key Performance Indicators (KPIs)

**1. Dicing Yield:**
```
Yield = (Good die / Total die on wafer) × 100%

Targets:
- Standard dicing: >98%
- Thin wafer: >95%
- New process: >90%

Loss mechanisms:
- Edge exclusion: 2-5 mm
- Defective die: 1-5%
- Handling damage: 0.5-2%
```

**2. Die Attach Quality:**
```
Metrics:
- Void content: <10% area
- Placement accuracy: ±25 μm
- Bond line thickness: 25-75 μm (±25%)
- Adhesion strength: >5 MPa

Test methods:
- X-ray for voids
- Cross-section for thickness
- Die shear test for adhesion
```

**3. Cleanliness Level:**
```
Particle count:
- Before cleaning: <100 particles >10μm per die
- After cleaning: <10 particles >10μm per die

Organic contamination:
- Contact angle: >60° (hydrophilic = clean)
- FTIR: No organic peaks
```

### Reliability Testing

**Die Shear Test:**
```
Method:
- Apply horizontal force at die edge
- Measure force at detachment

Specification:
- Standard: >5 MPa (or >10 kgf for 5×5 mm die)
- High reliability: >10 MPa

Failure modes:
- Cohesive (in adhesive): Good, expected
- Adhesive (at interface): Poor, investigate
- Die fracture: Excellent bond but fragile die
```

**Temperature Cycling:**
```
Test: -40°C ↔ +125°C
Dwell: 10-30 min each extreme
Ramp: 10-20°C/min
Cycles: 500-1000

Acceptance: <1% failure rate
Check: X-ray for delamination, electrical test
```

**High Temperature Storage:**
```
Temperature: 150-200°C
Duration: 500-1000 hours
Check: Delamination, adhesion degradation
```

## Best Practices Summary

### Do's ✓

```
✓ Optimize dicing parameters for each wafer type
✓ Use appropriate backing/tape for application
✓ Clean dies before attach (plasma or solvent)
✓ Control die attach material thickness (25-75 μm)
✓ Match CTE between die and substrate when possible
✓ Inspect 100% with AOI for critical applications
✓ Use X-ray to qualify die attach process
✓ Maintain cleanroom discipline (Class 1000 minimum)
✓ Track yield by lot and process variation
✓ Implement FMEA (Failure Mode Effects Analysis)
```

### Don'ts ✗

```
✗ Don't over-grind (leave adequate thickness)
✗ Don't use aggressive tape on thin dies
✗ Don't skip cleaning steps to save time
✗ Don't apply excessive die attach material (squeeze-out)
✗ Don't ignore small voids (they grow with thermal cycling)
✗ Don't handle dies with metal tweezers (use ESD-safe tools)
✗ Don't rush cure cycles (incomplete cure = poor reliability)
✗ Don't mix die attach materials from different lots
✗ Don't forget moisture sensitivity (MSL ratings)
✗ Don't skip incoming wafer inspection
```

### Decision Matrix

**Choose Die Attach Material:**

```
If: High thermal performance needed
→ Use: Silver-filled epoxy or solder

If: Electrical isolation required
→ Use: Non-conductive epoxy

If: Low process temperature needed (<100°C)
→ Use: Conductive tape or low-temp epoxy

If: Hermetic package
→ Use: Solder (Au-Sn or SAC305)

If: Large CTE mismatch
→ Use: Soft, thick epoxy (silicone-based)
```

## Cost Optimization

**Ways to Reduce Cost:**

1. **Maximize die per wafer:**
   - Minimize street width (30-50 μm)
   - Optimize die size vs yield
   - Reduce edge exclusion

2. **Process efficiency:**
   - Batch processing (larger batches)
   - Automated die sorting
   - In-line inspection (catch defects early)

3. **Material selection:**
   - Standard materials when possible
   - Optimize adhesive volume
   - Minimize waste

## References

1. Tummala, R. R. (Ed.). (2001). *Fundamentals of Microsystems Packaging*. McGraw-Hill.

2. Gilleo, K. (2005). *MEMS/MOEM Packaging: Concepts, Designs, Materials, and Processes*. McGraw-Hill.

3. Lee, N. C. (2002). *Optimizing the Reflow Profile*. Advancing Microelectronics, 29(6), 26-32.

4. Lau, J. H., & Lee, S. W. R. (1999). *Chip Scale Package: Design, Materials, Process, Reliability, and Applications*. McGraw-Hill.

---

**Document Information:**
- **Created:** December 13, 2025
- **Version:** 1.0
- **Status:** Complete
- **Part of:** Silicon Fabrication Handbook
- **Next Chapter:** [Wire Bonding](wire-bonding.md)
- **Section:** MEMS Packaging

**License:** CC BY 4.0 - Free to use with attribution

---

*For questions, corrections, or contributions, please visit:*
https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook
