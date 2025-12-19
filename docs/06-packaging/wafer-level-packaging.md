# Wafer-Level Packaging (WLP)

## Table of Contents
- [Introduction](#introduction)
- [Fan-In WLCSP](#fan-in-wlcsp)
- [Fan-Out WLP](#fan-out-wlp)
- [MEMS-Specific WLP](#mems-specific-wlp)
- [Advanced Techniques](#advanced-techniques)
- [Reliability](#reliability)
- [References](#references)

## Introduction

Wafer-Level Packaging (WLP) performs packaging operations at the wafer level before dicing, enabling smaller packages, lower costs, and better electrical performance compared to traditional packaging.

### Key Advantages

| Benefit | Impact | Quantification |
|---------|--------|----------------|
| Size | Chip-scale package | Package = die size + 100-500 μm |
| Cost | Parallel processing | 50-70% lower than conventional |
| Performance | Shortest interconnect | Inductance <0.5 nH, resistance <10 mΩ |
| Throughput | Batch processing | 100-1000× faster than single die |
| Thermal | Thin package | <500 μm total thickness |

### Technology Comparison

**Package Size Evolution:**

```
Traditional QFN (5×5 mm die):
- Package: 7×7 mm
- Overhead: 40% area

WLCSP (5×5 mm die):
- Package: 5.1×5.1 mm
- Overhead: 4% area

Result: 2.3× more dies per PCB area
```

### Market Overview

```
Market size: $5-7 billion/year (2025)
Growth: 10-15% CAGR

Applications:
- Smartphones (>50% of WLCSP)
- MEMS sensors (accelerometers, gyros)
- Image sensors (CMOS)
- RF devices
- Power management ICs

Leading manufacturers:
- TSMC, ASE, Amkor, JCET, Nepes
```

### WLP Categories

```
1. Fan-In WLCSP:
   - I/O within die footprint
   - Redistribution layer (RDL)
   - Smallest package
   - Limited I/O count (<100)

2. Fan-Out WLP (FOWLP):
   - I/O beyond die footprint
   - Higher I/O count (>200)
   - Better thermal performance
   - Allows passive integration

3. MEMS-Specific:
   - Wafer-level cavity/cap
   - Hermetic sealing
   - Vacuum or controlled atmosphere
   - Getter materials
```

## Fan-In WLCSP

Most common WLP technology for low I/O count devices.

### Process Flow

**Standard Fan-In WLCSP:**

```
1. Wafer preparation
   - Complete functional wafers
   - Back-side grind (optional, 100-300 μm)
   - Passivation deposition

2. Redistribution Layer (RDL)
   - Polymer layer (polyimide, BCB, PBO)
   - Cu trace formation
   - Multiple levels if needed (1-3 typical)

3. Under Bump Metallization (UBM)
   - Ti/Cu/Ni or Ti/Cu stack
   - Adhesion + barrier + solderable

4. Bump formation
   - Solder balls (250-500 μm diameter)
   - Electroplating or ball placement
   - Reflow to form spheres

5. Dicing
   - Blade saw or laser
   - Individual WLCSP dies

6. Testing
   - Electrical test on wafer
   - Known good die (KGD)
```

### Redistribution Layer (RDL)

**Purpose:**
- Route signals from bond pads to solder balls
- Pitch conversion (fine pad → coarse ball)
- Allow area array I/O arrangement

**Materials:**

| Layer | Material | Thickness | Function |
|-------|----------|-----------|----------|
| Dielectric | Polyimide (PI) | 5-15 μm | Insulation, stress buffer |
| | BCB (Benzocyclobutene) | 5-10 μm | Low-k, excellent properties |
| | PBO (Polybenzoxazole) | 5-12 μm | High temperature |
| Metal | Copper (Cu) | 2-8 μm | Conductivity |
| | Aluminum (Al) | 2-5 μm | Lower cost, lower conductivity |

**Single-Level RDL:**

```
Al Pad (on die)
  ↓
Passivation opening
  ↓
Polymer dielectric (10 μm)
  ↓
Cu trace (3-5 μm)
  ↓
UBM (Ti/Cu, 0.5 μm)
  ↓
Solder ball

Pitch conversion:
- Input: 50 μm (bond pad pitch)
- Output: 400 μm (ball pitch)
- Trace width/spacing: 10/10 μm typical
```

**Multi-Level RDL:**

```
For complex routing (>100 I/O):

Layer 1 (M1): Fine pitch routing
Via 1
Layer 2 (M2): Coarse routing
Via 2 (optional)
Layer 3 (M3): Ball pads

Via diameter: 20-50 μm
Aspect ratio: <2:1 (for reliable fill)
```

### RDL Fabrication Process

**Photolithography Method:**

```
1. Spin/laminate polymer dielectric
   - Thickness: 5-15 μm
   - Pre-cure: 150-200°C, soft bake

2. Pattern via openings (photolithography)
   - Expose and develop
   - Open to bond pads

3. Deposit seed layer (sputter)
   - Ti adhesion: 50 nm
   - Cu seed: 200-500 nm

4. Pattern photoresist (plating mask)
   - Thick resist: 8-15 μm
   - Define trace pattern

5. Electroplate Cu
   - Thickness: 3-8 μm
   - Current: 1-3 A/dm²
   - Time: 30-90 min

6. Strip resist

7. Etch seed layer (flash etch)

8. Final cure polymer
   - Temperature: 350-400°C (PI)
   - Time: 1-2 hours
```

**Semi-Additive Process (SAP):**

```
Higher resolution alternative:

1. Deposit full-field seed layer
2. Pattern resist (negative)
3. Plate Cu in openings only
4. Strip resist
5. Etch exposed seed layer

Result:
- Finer features (L/S: 5/5 μm vs 10/10 μm)
- Better for high I/O count
```

### Solder Ball Formation

**Ball Placement Method:**

```
Most common for WLCSP:

1. UBM deposition (sputtering)
   - Ti/Cu or Ti/Cu/Ni
   - Total: 0.5-1 μm

2. Flux application
   - Screen print or spray
   - Tacky flux holds balls

3. Ball placement
   - Pre-formed solder balls (250-500 μm)
   - Vacuum pick-and-place
   - Throughput: 10,000-50,000 balls/hour

4. Reflow
   - SAC305: Peak 245-260°C
   - Forms metallurgical bond to UBM
   - Ball height: 200-400 μm (after reflow)

5. Flux cleaning (optional)
   - DI water for water-soluble flux
   - Or use no-clean flux
```

**Ball Sizes:**

| Ball Diameter | Pitch | I/O Count | Applications |
|---------------|-------|-----------|--------------|
| 250 μm | 400 μm | <50 | Small sensors, simple ICs |
| 300 μm | 500 μm | 50-100 | Standard MEMS, medium ICs |
| 400 μm | 600 μm | 100-200 | Higher I/O, better reliability |
| 500 μm | 800 μm | >200 | High reliability, BGAs |

**Electroplating Method:**

```
Alternative to ball placement:

1. Pattern photoresist (ball locations)
2. Electroplate solder (20-80 μm)
3. Strip resist
4. Reflow to form spheres

Advantages:
- Better coplanarity (±10 μm)
- Finer pitch possible (<300 μm)
- No ball placement equipment

Disadvantages:
- Additional lithography step
- Plating uniformity challenges
```

### Typical Specifications

**Standard WLCSP:**

```
Die size: 2×2 to 10×10 mm
Package size: Die + 100-200 μm per side
Ball count: 4-200 balls
Ball pitch: 400-800 μm
Ball diameter: 250-500 μm
Package height: 400-600 μm
RDL levels: 1-2 (occasionally 3)

Electrical:
- Resistance: 5-20 mΩ per connection
- Inductance: 0.2-0.8 nH

Cost: $0.10-0.40 per package
```

## Fan-Out WLP (FOWLP)

Extends interconnect area beyond die footprint for higher I/O count.

### Process Flow

**eWLB (embedded Wafer-Level BGA):**

```
1. Wafer dicing
   - Separate individual dies
   - Known good die (KGD)

2. Die placement on carrier
   - Temporary adhesive wafer (glass/Si)
   - Face-down placement
   - Spacing between dies (fan-out area)

3. Molding (encapsulation)
   - Epoxy molding compound (EMC)
   - Covers dies and fill spaces
   - Thickness: 200-600 μm
   - Creates "reconstituted wafer"

4. Carrier debonding
   - Thermal/UV release
   - Flip molded panel

5. RDL formation
   - Multiple metal layers (2-5)
   - Routes I/O beyond die edge
   - Polymer dielectrics between

6. UBM and ball formation
   - Standard solder balls
   - Now extended to fan-out area

7. Dicing
   - Singulate packages
   - Package size > die size
```

**Fan-Out Advantages:**

```
Higher I/O density:
- Fan-In limit: ~100 I/O (400 μm pitch)
- Fan-Out: >500 I/O possible

Better thermal:
- Heat spreads into mold compound
- Larger exposed area

Passive integration:
- Capacitors, resistors in mold
- Thinner overall package

Examples:
- Apple A-series processors
- Intel EMIB (Embedded Multi-die Interconnect Bridge)
```

### Panel-Level Fan-Out

**Scaling for Higher Throughput:**

```
Wafer-level: 300 mm diameter
- Area: 707 cm²
- Dies: 100-500 (depending on size)

Panel-level: 510×515 mm
- Area: 2627 cm²
- Dies: 400-2000 (3.7× more)

Advantages:
- Lower cost per unit
- Compatible with PCB equipment
- Better material utilization

Challenges:
- Warpage management (>510 mm span)
- Uniform molding
- RDL process adaptation
```

### Advanced Fan-Out Structures

**2.5D Integration:**

```
Multiple dies side-by-side:

Die 1 (CPU) | Die 2 (Memory) | Die 3 (I/O)
     ↓             ↓                ↓
  RDL interconnect (high density)
     ↓             ↓                ↓
        Package balls

Benefits:
- Heterogeneous integration
- Known good die selection
- Shorter interconnects than 2D
- Lower cost than 3D TSV
```

**System-in-Package (SiP):**

```
Active + passive components:

Die | Capacitor | Inductor
     ↓      ↓         ↓
    EMC (embedded)
         ↓
   RDL routing
         ↓
    Package balls

Miniaturization:
- 30-50% smaller than discrete
- Better electrical performance
- Lower assembly cost
```

## MEMS-Specific WLP

MEMS devices often require cavities for moving structures and controlled atmosphere.

### Wafer-Level Capping

**Purpose:**
- Protect fragile MEMS structures
- Maintain vacuum (resonators, gyroscopes)
- Control atmosphere (prevent stiction)
- Hermetic sealing

**Cap Wafer Structures:**

```
Method 1 - Recess in Cap:

Cap Wafer (Si or glass)
  ↓
Cavity (etched, 5-500 μm deep)
  ↓
Seal ring (glass frit, metal, polymer)
  ↓
Device Wafer (MEMS)
```

**Cavity Formation:**

| Method | Depth Range | Sidewall | Cost | Volume |
|--------|-------------|----------|------|--------|
| DRIE | 10-500 μm | Vertical | High | Medium-High |
| Wet etch (KOH) | 50-500 μm | 54.7° slope | Low | High |
| Sandblasting | 100-1000 μm | Rough | Very low | Low-Medium |
| Plasma etch | 1-100 μm | Vertical | Medium | High |

### Bonding Methods

**1. Anodic Bonding:**

```
Glass cap to silicon MEMS:

Process:
- Temperature: 300-450°C
- Voltage: 200-1000 V DC
- Pressure: 100-500 kPa
- Time: 10-30 minutes
- Atmosphere: Vacuum or controlled

Mechanism:
- Na⁺ ions migrate in glass under field
- Si-O-Si bonds form at interface
- Hermetic seal

Bond strength: 10-20 MPa

Advantages:
- Hermetic
- Transparent (optical access)
- No intermediate layer
- Vacuum compatible

Limitations:
- High temperature (stress)
- Requires conductive wafer
- Glass cap only
```

**2. Glass Frit Bonding:**

```
Low melting point glass paste:

Composition:
- Glass powder (PbO-B₂O₃-SiO₂ or Bi-based)
- Organic binder
- Melting point: 400-450°C (Pb-based)
                 430-480°C (Pb-free)

Process:
1. Screen print frit paste on cap
2. Dry at 150°C
3. Align cap to device wafer
4. Bond:
   - Temperature: Tm + 50°C
   - Pressure: 100-1000 kPa
   - Time: 10-30 min
   - Atmosphere: As desired (vacuum, N₂, etc)

Seal width: 100-500 μm
Bond strength: 5-15 MPa

Advantages:
- Hermetic
- Controlled atmosphere
- Si or glass caps
- Established process

Limitations:
- High temperature
- Outgassing during bond
- Thick seal ring
```

**3. Eutectic Bonding:**

```
Metal alloy bonding:

Common systems:
- Au-Si: 363°C eutectic (97%Au-3%Si)
- Au-Sn: 280°C eutectic (80%Au-20%Sn)
- Al-Ge: 424°C eutectic
- Cu-Sn: 217°C (SLID bonding)

Au-Si Process:
1. Deposit Au on cap (0.5-2 μm)
2. Align and contact wafers
3. Heat to 400°C under vacuum/N₂
4. Pressure: 1-5 MPa
5. Time: 10-30 min
6. Cool slowly

Bond line: 1-5 μm (thin!)
Bond strength: 50-100 MPa

Advantages:
- Excellent hermeticity
- Thin seal (low parasitic)
- Strong bond
- Si-Si compatible

Limitations:
- High cost (Au expensive)
- Process control critical
- Voids possible
```

**4. Polymer/Adhesive Bonding:**

```
Low-temperature option:

Materials:
- Epoxy (thermo-setting)
- BCB (benzocyclobutene)
- Polyimide
- Silicone (for stress relief)

Process:
1. Spin/laminate adhesive
2. Soft cure (80-150°C)
3. Align and bond
   - Pressure: 0.1-1 MPa
   - Temperature: 150-250°C
   - Time: 30-120 min

Bond line: 5-50 μm
Bond strength: 5-20 MPa

Advantages:
- Low temperature (<200°C)
- Low cost
- Tolerates particles
- Stress relieving

Limitations:
- Not truly hermetic
- Outgassing
- Limited temperature range
- Moisture permeation
```

### Getter Materials

**Purpose:** Maintain vacuum or absorb contaminants

```
Types:
1. Non-evaporable getter (NEG):
   - Ti, Zr, V alloys
   - Absorbs H₂, H₂O, CO, CO₂, O₂
   - Activation: 400-450°C (releases active sites)
   
2. Evaporable getter:
   - Ba, Sr
   - Evaporates and deposits on surfaces
   - Activation: >600°C

3. Chemical getter:
   - CaO, BaO for moisture
   - Room temperature activation

Placement:
- Inside cavity on cap or substrate
- Typically 1-10 mm² area
- Thin film (1-10 μm) or thick (50-200 μm)

Performance:
- Maintains <1 Pa for 10+ years
- Critical for MEMS resonators (Q>10,000)
```

### Through-Wafer Vias

For electrical feedthrough in capped devices:

```
Via Formation:
1. DRIE through device wafer
   - Diameter: 20-100 μm
   - Depth: 200-700 μm (wafer thickness)
   
2. Insulation layer
   - Thermal oxide: 0.5-1 μm
   - PECVD oxide: 1-2 μm
   
3. Barrier/seed layer
   - Ti/Cu or Ta/Cu: 50/500 nm

4. Via fill
   - Electroplate Cu
   - Or polymer fill + metal liner

Resistance: 10-100 mΩ per via
Capacitance: 50-200 fF per via
```

## Advanced Techniques

### Chip-Scale Packaging Variations

**1. WLCSP with Cavity:**

```
For MEMS requiring air gap:

Substrate
  ↓
Solder balls (perimeter only)
  ↓
Space for MEMS motion (center)
  ↓
MEMS die (face-down)

Examples:
- Microphones
- Pressure sensors
- Accelerometers (some)

Package height: 0.6-1.2 mm
Acoustic port: Opening in substrate/PCB
```

**2. LGA (Land Grid Array) WLCSP:**

```
Alternative to solder balls:

Cu pads (instead of balls)
  ↓
Solder paste on PCB
  ↓
Reflow to connect

Advantages:
- Thinner (by 200-300 μm)
- Better for thin devices

Disadvantages:
- Less self-alignment
- Requires precise placement
```

### 3D Integration

**Wafer-Level Stacking:**

```
Multiple wafers bonded vertically:

Wafer 1 (MEMS sensor)
  ↓ (TSV + bonding)
Wafer 2 (ASIC)
  ↓ (TSV + bonding)
Wafer 3 (Interposer, optional)
  ↓
RDL + balls

Advantages:
- Highest integration density
- Shortest interconnects (<10 μm)
- Best electrical performance

Challenges:
- Thermal management
- Yield (multiplicative)
- Cost
- Test before stack

Applications:
- Image sensors (stacked CMOS)
- Advanced MEMS IMUs
- Memory (HBM)
```

## Reliability

### Failure Mechanisms

**1. Ball Shear/Pull:**

```
Test: Apply force until ball detaches

Ball shear strength:
- Standard: >5 gf/ball (250 μm ball)
- High reliability: >10 gf/ball

Failure modes:
✓ Solder fracture: Good (expected)
✓ UBM pull-off: Acceptable
✗ Pad cratering: Substrate damage
✗ Trace lift: RDL adhesion issue
```

**2. Package Warpage:**

```
Cause: CTE mismatch, thin package

Acceptable warpage:
- Before reflow: <200 μm for 10×10 mm
- After reflow: <50 μm

Measurement:
- Shadow moiré
- Laser scanning

Impact:
- Ball coplanarity issues
- Assembly yield loss
- Solder joint reliability
```

**3. Moisture Sensitivity:**

```
Moisture Sensitivity Level (MSL):

MSL 1: Unlimited floor life
MSL 2: 1 year at <30°C/60% RH
MSL 3: 168 hours at <30°C/60% RH
MSL 4: 72 hours
MSL 5: 48 hours
MSL 6: Mandatory bake before reflow

WLCSP typically MSL 3-4

Issue: "Popcorning"
- Moisture absorbed in polymer
- Vaporizes during reflow (260°C)
- Internal pressure cracks package
```

### Reliability Testing

**Temperature Cycling:**

```
Standard: -40°C ↔ +125°C
Automotive: -55°C ↔ +150°C

Dwell: 10-15 min each extreme
Ramp: 10-20°C/min
Cycles: 500-1000

Failure criterion:
- >20% resistance increase
- Or >5% of population fails

WLCSP performance:
- With underfill: >2000 cycles
- Without underfill: 500-1000 cycles
```

**Drop Test:**

```
JEDEC JESD22-B111:

Height: 1.5 m
Orientation: 6 surfaces, 8 corners, 12 edges
Impacts: 3-5 per orientation

Acceptance:
- No mechanical damage
- Electrical continuity maintained

Critical for:
- Smartphones
- Portable devices
- All handheld electronics

WLCSP challenge:
- Solder joint close to neutral point
- Better than perimeter-only packages
```

**Board-Level Reliability (BLR):**

```
Mounted on test board:

Temperature cycling: -40 to 125°C
Test vehicle: PCB (typically FR-4)
Joint construction:
- WLCSP ball → solder paste → PCB pad
- Optional: Underfill for reliability

Characteristic life (Weibull):
- No underfill: 500-800 cycles
- With underfill: 2000-5000 cycles

Corner balls fail first (highest stress)
```

### Design for Reliability

**Best Practices:**

```
Ball layout:
✓ Symmetrical pattern
✓ Ground/power balls distribute load
✓ Avoid large open areas (warpage)
✓ Peripheral balls for mechanical strength

Package design:
✓ Ball pitch ≥400 μm (for hand solder)
✓ Keep package thin but not too thin (<400 μm risky)
✓ Use low-stress RDL materials
✓ Design for <100 μm warpage

PCB design:
✓ Solder mask defined (SMD) pads
✓ Pad size: 80-90% of ball diameter
✓ Thermal vias under package (if high power)
✓ No vias in pad (VIPPO)
```

## Cost Analysis

**Fan-In WLCSP:**

```
Equipment (wafer level):
- RDL process: $1M-3M (litho + plating)
- Ball placement: $300K-800K
- Test: $500K-2M

Wafer cost (300 mm):
- RDL materials: $100-300
- Balls: $50-150
- Test: $200-500
Total: $350-950 per wafer

Per die cost (for 5×5 mm die, 500 die/wafer):
- Materials: $0.70-1.90
- Amortized equipment: $0.10-0.30
- Labor/overhead: $0.20-0.50
Total: $1.00-2.70 per package

Compare to:
- Wire bond package: $0.50-1.50
- QFN: $0.80-2.00
- Flip chip: $1.50-4.00
```

**Fan-Out WLP:**

```
Additional costs:
- Molding: $200-400 per panel
- Reconstitution: $100-200
- Additional RDL: $200-500

Total: $500-1100 per panel (higher than fan-in)

But: Amortized over more area
Result: Similar $/mm² to fan-in
```

**Cost Drivers:**

```
Economies of scale:
- High volume (>10M/year): Fan-out competitive
- Medium volume (1-10M/year): Fan-in preferred
- Low volume (<1M/year): Traditional package

Technology selection:
- I/O count <100: Fan-in WLCSP
- I/O count 100-500: Fan-out
- I/O count >500: Advanced fan-out or flip chip
```

## Design Guidelines

### General Rules ✓

```
✓ Ball pitch ≥400 μm (standard assembly)
✓ Ball diameter: 0.6-0.7× pitch
✓ Keep-out zone at die edge: 100-300 μm
✓ RDL trace width/space: ≥10/10 μm
✓ Via diameter ≥20 μm
✓ Polymer thickness: 5-15 μm per layer
✓ Cu thickness: 3-8 μm (1-2 oz)
✓ Include test balls for monitoring
✓ Fiducial marks for alignment (≥3)
✓ Design for ≤100 μm warpage target
```

### Avoid ✗

```
✗ Ball pitch <400 μm (without fine-pitch capability)
✗ Asymmetric ball pattern (warpage)
✗ Trace width <10 μm (yield risk)
✗ Via aspect ratio >2:1 (fill issues)
✗ Large copper areas (stress)
✗ Balls over active circuits
✗ Thin package (<400 μm) without warpage control
✗ Mixed ball sizes
✗ No test structures
```

## References

1. Braun, T., et al. (2006). Wafer-level packaging. *Advanced Packaging*, 15(1), 21-24.

2. Lau, J. H., & Lee, R. (2009). *Chip Scale Package (CSP): Design, Materials, Processes, Reliability, and Applications*. McGraw-Hill.

3. Meyer, T., et al. (2008). Embedded wafer level ball grid array (eWLB). *Electronic Components and Technology Conference*, 994-998.

4. Tummala, R. R. (2008). *System-on-Package: Miniaturization of the Entire System*. McGraw-Hill.

5. Zoschke, K., et al. (2015). Wafer level packaging and system integration: technology and applications. *Chip Scale Review*, 19(5), 18-24.

---

**Document Information:**
- **Created:** December 16, 2025
- **Version:** 1.0
- **Status:** Complete
- **Part of:** Silicon Fabrication Handbook
- **Next Chapter:** [Hermetic Sealing](hermetic-sealing.md)
- **Previous Chapter:** [Flip Chip](flip-chip.md)

**License:** CC BY 4.0 - Free to use with attribution

---

*For questions, corrections, or contributions, please visit:*
https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook