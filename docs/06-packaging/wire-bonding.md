# Wire Bonding for MEMS Packaging

## Table of Contents
- [Introduction](#introduction)
  - [Market Overview](#market-overview)
  - [Bonding Methods Comparison](#bonding-methods-comparison)
  - [Process Overview](#process-overview)
  - [Key Advantages](#key-advantages)
  - [Limitations](#limitations)
- [Ball Bonding](#ball-bonding)
  - [Process Steps](#process-steps)
  - [Capillary Design](#capillary-design)
  - [Process Window](#process-window)
- [Wedge Bonding](#wedge-bonding)
  - [Process Description](#process-description)
  - [Wedge vs Ball Comparison](#wedge-vs-ball-comparison)
  - [Aluminum Wire Bonding](#aluminum-wire-bonding)
- [Wire Materials](#wire-materials)
  - [Gold Wire](#gold-wire)
  - [Copper Wire](#copper-wire)
  - [Aluminum Wire](#aluminum-wire)
  - [Wire Diameter Selection](#wire-diameter-selection)
- [Process Optimization](#process-optimization)
  - [Bond Pad Design](#bond-pad-design)
  - [Bonding Sequence](#bonding-sequence)
  - [Process Monitoring](#process-monitoring)
- [Reliability and Testing](#reliability-and-testing)
  - [Destructive Tests](#destructive-tests)
  - [Reliability Testing](#reliability-testing)
  - [Common Defects](#common-defects)
- [Advanced Techniques](#advanced-techniques)
  - [Fine Pitch Bonding](#fine-pitch-bonding)
  - [Stacked Die Bonding](#stacked-die-bonding)
  - [Long Wire Bonding](#long-wire-bonding)
  - [Ribbon Bonding](#ribbon-bonding)
- [Cost Analysis](#cost-analysis)
- [Design Guidelines](#design-guidelines)
  - [Best Practices ✓](#best-practices)
  - [Avoid ✗](#avoid)
- [Future Trends](#future-trends)
  - [Copper Wire Adoption](#copper-wire-adoption)
  - [Advanced Materials](#advanced-materials)
  - [Automation Advances](#automation-advances)
- [References](#references)

## Introduction

Wire bonding is the most widely used interconnection method in semiconductor packaging, accounting for >90% of chip-to-package connections. It provides electrical connection between die bond pads and package leads or substrates.

### Market Overview

```
Annual wire bonds: >10 trillion connections
Market size: $3-4 billion/year
Typical cost: $0.001-0.01 per bond
Equipment: $50K-500K per machine
```

### Bonding Methods Comparison

| Method | Wire Type | Bonds/sec | Pitch | Loop Height | Applications |
|--------|-----------|-----------|-------|-------------|--------------|
| Ball (thermosonic) | Au, Cu | 8-20 | 40-150 μm | 150-400 μm | High volume, fine pitch |
| Wedge (ultrasonic) | Al, Au | 3-10 | 50-200 μm | 50-150 μm | Power devices, thick wire |
| Ribbon | Al ribbon | 1-5 | 200+ μm | 100-300 μm | High current (>5A) |

### Process Overview

**Ball Bonding (2 bonds):**
```
1. Free Air Ball (FAB) formation
2. First bond (ball bond on die)
3. Wire loop formation
4. Second bond (stitch/crescent on substrate)
5. Wire break/tail formation
```

**Wedge Bonding (2 bonds):**
```
1. First bond (wedge on die)
2. Wire loop formation  
3. Second bond (wedge on substrate)
4. Wire clamp and break
```

### Key Advantages

✓ Proven technology (60+ years)
✓ High reliability (>10 billion device-hours)
✓ Flexible (multiple die, stacked die)
✓ Low cost per connection
✓ Wide process window
✓ Reworkable

### Limitations

✗ Relatively slow (vs flip chip)
✗ Loop inductance (10-20 nH)
✗ Package height (loop clearance)
✗ Sequential process (not parallel)
✗ Fine pitch limits (~30 μm min)

## Ball Bonding

Most common method, using gold or copper wire with ball formation.

### Process Steps

**1. Free Air Ball (FAB) Formation:**

```
Process:
- Apply EFO (Electronic Flame-Off) spark
- Voltage: 1-5 kV, Duration: 0.5-2 ms
- Capillary positioned above wire tip
- Surface tension forms sphere

Wire diameter: d
Ball diameter: 1.8-2.5 × d (typically 2.0×)

Example:
25 μm wire → 50 μm ball
```

**Ball Formation Parameters:**

| Parameter | Range | Effect |
|-----------|-------|--------|
| EFO current | 50-150 mA | Ball size |
| EFO voltage | 1-5 kV | Energy, consistency |
| EFO gap | 0.5-1.5 mm | Ball roundness |
| EFO time | 0.5-2 ms | Ball diameter |
| Gas flow (forming gas) | 0.2-0.5 L/min | Oxidation prevention |

**2. First Bond (Ball Bond):**

```
Bonding Parameters:
- Force: 20-80 gf (gram-force)
- Power: 30-100 mW (ultrasonic)
- Time: 10-30 ms
- Temperature: 150-250°C (substrate)

Mechanism: Thermosonic bonding
- Ultrasonic energy (60-120 kHz)
- Pressure (capillary force)
- Heat (substrate temperature)
- Result: Intermetallic formation (Au-Al for Au wire on Al pad)
```

**Bond Deformation:**

```
Bond diameter: 1.5-2.5 × wire diameter
Bond thickness: 0.4-0.6 × ball diameter

For 25 μm wire:
- Ball: 50 μm diameter
- Bond: 40-60 μm diameter
- Height: 20-30 μm
```

**Intermetallic Formation:**

```
Au wire on Al pad:

Immediate: Au + Al → Au₄Al (diffusion)
150°C, hours: Au₅Al₂, Au₂Al (purple plague)

Target: Thin intermetallic layer (0.5-2 μm)
Avoid: Thick layer (brittle, cracks)
```

**3. Wire Loop Formation:**

```
Loop Profile Parameters:
- Span: Horizontal distance between bonds
- Height: Peak of loop above die surface
- Shape: Shallow-S, deep-S, flat

Typical Ratios:
Height/Span = 0.15-0.30 (standard)
           = 0.10-0.15 (low loop)
           = 0.30-0.50 (high loop)

Example:
Span: 2000 μm
Height: 400 μm (H/S = 0.20)
```

**4. Second Bond (Stitch/Crescent):**

```
Parameters:
- Force: 30-100 gf (higher than first bond)
- Power: 40-120 mW
- Time: 15-40 ms
- Temperature: Same as first bond

Shape: Crescent or fishtail
Size: Length 2-3× wire diameter
      Width 1.5-2× wire diameter

Bond pull strength typically 90-95% of wire break load
```

**5. Wire Tail Formation:**

```
After second bond:
- Clamp wire above bond
- Move capillary up (rapid)
- Wire breaks at second bond

Tail length: 20-50 μm
Critical: Must not short adjacent bonds
```

### Capillary Design

**Key Dimensions:**

```
Hole Diameter (HD): 1.2-1.4 × wire diameter
Chamfer Diameter (CD): 2.0-3.0 × wire diameter
Chamfer Angle: 90-120° (typically 90°)
Tip Radius: 2-6 × wire diameter

Material: Ceramic (Al₂O₃, Ti-carbide coated)
Lifetime: 10-50 million bonds

For 25 μm wire:
- HD: 30-35 μm
- CD: 50-75 μm
- Tip radius: 50-150 μm
```

### Process Window

**Critical Parameters:**

```
Force: ±10 gf variation acceptable
Power: ±5 mW tolerance
Time: ±5 ms variation OK
Temperature: ±10°C substrate

Out of range:
- Too low: Weak bond, high pull test failures
- Too high: Cratering (die damage), pad damage

Sweet spot: 
- Ball shear: 40-80 gf (for 25 μm wire)
- Wire pull: 8-12 gf
```

## Wedge Bonding

Uses aluminum or gold wire without ball formation.

### Process Description

**Ultrasonic Wedge Bonding:**

```
1. First Bond (on die):
   - Wedge tool contacts wire on pad
   - Ultrasonic energy (20-200 kHz)
   - Pressure: 50-200 gf
   - Time: 20-80 ms
   - Temperature: 100-300°C

2. Wire Loop:
   - Typically low profile (50-100 μm)
   - Bonding direction sensitive

3. Second Bond (on substrate):
   - Similar parameters to first bond
   - Slightly higher force

4. Clamp and Break:
   - Wire clamped above bond
   - Tool moves laterally to break
```

### Wedge vs Ball Comparison

| Feature | Ball Bond | Wedge Bond |
|---------|-----------|------------|
| Speed | 8-20 bonds/sec | 3-10 bonds/sec |
| Wire material | Au, Cu | Al, Au |
| First bond shape | Round | Rectangular |
| Loop height | 150-400 μm | 50-150 μm |
| Directionality | Non-directional | Directional |
| Fine pitch | Down to 40 μm | 50+ μm typical |
| Equipment cost | Higher | Lower |
| Applications | General purpose | Power, RF |

### Aluminum Wire Bonding

**Advantages:**
- Low cost ($0.50/km vs $150/km for Au)
- Good electrical conductivity (61% IACS)
- Standard for power devices
- Compatible with Al bond pads

**Challenges:**
- Lower mechanical strength than Au
- Oxidation issues (requires temperature)
- Purple plague with Au metallization
- More sensitive to contamination

**Typical Parameters:**

```
Wire diameter: 25-500 μm (thick for power)
Bonding force: 50-200 gf
Ultrasonic power: 100-400 mW
Temperature: 150-300°C (higher than Au)
Frequency: 60 kHz (typical)
```

## Wire Materials

### Gold Wire

**Properties:**
```
Purity: 99.99% (4N) or 99.999% (5N)
Tensile strength: 150-250 MPa (annealed)
Elongation: 2-8%
Electrical conductivity: 70% IACS
Thermal conductivity: 318 W/m·K
Melting point: 1064°C

Cost: $50-150 per km (1 mil/25 μm)
Usage: ~2000 bonds/km for 1 mil wire
```

**Alloys (for improved strength):**

| Alloy | Addition | Tensile Strength | Elongation | Applications |
|-------|----------|------------------|------------|--------------|
| 4N (pure) | None | 150-200 MPa | 5-8% | Standard |
| Au-1%Pd | 1% Pd | 180-220 MPa | 3-5% | Fine pitch |
| Au-0.5%Be | 0.5% Be | 200-250 MPa | 2-4% | High reliability |

### Copper Wire

**Advantages over Gold:**
- Cost: $5-15/km (10-20× cheaper)
- Higher tensile strength (250-400 MPa)
- Better electrical conductivity (95% IACS)
- Reduced sagging at high temperature

**Challenges:**
- Oxidation (requires forming gas)
- Harder (more pad/die stress)
- Requires harder capillaries
- Lower ball neck strength

**Process Differences:**

```
Forming gas: 95% N₂ + 5% H₂ (prevents oxidation)
EFO settings: 20-30% higher energy than Au
Bonding force: 20-40% higher
Substrate temperature: 200-280°C (vs 150-250°C for Au)
Capillary: Harder material (Ti-C coating)
```

**Market Adoption:**

```
2010: <5% of ball bonding
2015: ~20%
2020: ~50% (smartphone, automotive)
2025: >60% projected

Drivers:
- Cost reduction
- Improved reliability
- Better electrical performance
```

### Aluminum Wire

**Properties:**
```
Purity: 99.99% (1N wire)
Tensile strength: 100-150 MPa
Elongation: 5-15%
Electrical conductivity: 61% IACS
Melting point: 660°C

Cost: $0.50-2.00/km
```

**Wire Sizes:**

| Diameter | Current Capacity | Application |
|----------|------------------|-------------|
| 25 μm (1 mil) | 0.5 A | Low power |
| 50 μm (2 mil) | 1-2 A | Standard |
| 75 μm (3 mil) | 2-3 A | Medium power |
| 125 μm (5 mil) | 4-6 A | Power devices |
| 250-500 μm | 10-20 A | Heavy power |

### Wire Diameter Selection

**Common Sizes:**

```
0.7 mil (18 μm): Ultra-fine pitch (<50 μm)
1.0 mil (25 μm): Fine pitch (50-75 μm), most common
1.2 mil (30 μm): Standard (75-100 μm)
1.5 mil (38 μm): Coarser pitch, higher current
2.0 mil (50 μm): Power devices

Rule of thumb:
Pad pitch ≥ 2 × wire diameter minimum
            ≥ 3 × wire diameter comfortable
```

## Process Optimization

### Bond Pad Design

**Pad Requirements:**

```
Minimum pad size:
Ball bond: 50-80 μm square (for 25 μm wire)
Wedge bond: 60-100 μm × 80-120 μm

Metallization:
- Aluminum: 0.5-1.5 μm thick (standard)
- Gold: 0.2-0.5 μm over Ni barrier
- Copper: Requires surface finish (OSP, ENIG)

Passivation opening:
- Pad opening size = Pad size + 10-20 μm
- Ensures no bonding on passivation edge
```

**Pad Placement:**

```
Distance from die edge: ≥ 100 μm
Pad-to-pad spacing: ≥ 50 μm (min)
                    ≥ 80 μm (comfortable)
Staggered rows: Allows denser packing

Avoid:
- Pads over active circuitry (cratering risk)
- Pads near die corners (stress concentration)
```

### Bonding Sequence

**Optimization Goals:**
1. Minimize wire sweep (adjacent bonds)
2. Avoid wire crossings
3. Balance capillary movement
4. Shortest total path length

**Typical Strategies:**

```
Center-out: Start at center pads, work outward
  - Reduces wire sweep effects
  - Better for high bond counts

Clockwise/Counter-clockwise: Spiral pattern
  - Efficient for perimeter bonding
  - Minimizes travel distance

Smart bonding: Algorithm-optimized
  - Custom sequence per die
  - 10-20% faster than standard
```

### Process Monitoring

**Real-Time Monitoring:**

```
Parameters tracked:
- Capillary force (load cell feedback)
- Ultrasonic current (generator monitoring)
- Z-axis position (bond placement height)
- Wire pull (tensile sensor)

Feedback control:
- Adaptive bonding (adjusts per bond)
- SPC (Statistical Process Control)
- Alarm limits (out of spec rejection)
```

**Non-Destructive Testing:**

```
Methods:
1. Bond pull test (sample, inline)
   - Destructive but fast
   - Target: >8 gf for 25 μm Au wire

2. Vision inspection (100%)
   - Bond placement accuracy
   - Bond shape/size
   - Wire loop profile
   
3. Acoustic monitoring
   - Ultrasonic signature analysis
   - Detects weak bonds in real-time
```

## Reliability and Testing

### Destructive Tests

**1. Wire Pull Test:**

```
Method:
- Hook under wire at mid-span
- Pull vertically until failure
- Record break force and mode

Acceptance Criteria (25 μm Au wire):
- Break force: >8 gf (typically 10-12 gf)
- Wire break strength: 10-15 gf

Failure Modes:
✓ Wire break (mid-span): Good, target mode
✓ Wire break (near bond): Acceptable
✗ Bond lift: Reject, process issue
✗ Pad peel: Reject, metallization issue
```

**2. Ball Shear Test:**

```
Method:
- Shear tool at 3-5 μm above pad
- Push horizontally until bond breaks
- Record shear force

Acceptance (25 μm Au wire, 50 μm ball):
- Shear force: >40 gf
- Typical: 60-80 gf

Failure Modes:
✓ Ball shear (at interface): Good
✓ Ball lift with residue: Acceptable
✗ Cratering (Si substrate damage): Reject
✗ Clean lift (no residue): Weak bond, reject
```

**3. Bond Pull Test:**

```
Method:
- Pull wire at angle (45° typical)
- Stress both bonds
- Higher force than wire pull

Criteria:
- Typically 2× wire pull strength
- Tests overall bond strength
```

### Reliability Testing

**Temperature Cycling:**

```
Test: -65°C ↔ +150°C
Dwell: 10-15 min each extreme
Ramp: 10-20°C/min
Cycles: 500-1000

Failure Mechanisms:
- Intermetallic growth (Au-Al)
- CTE mismatch stress
- Wire fatigue

Acceptance: <0.1% failure rate
```

**High Temperature Storage:**

```
Temperature: 150-200°C
Duration: 500-1000 hours

Monitors:
- Intermetallic thickness growth
- Bond resistance increase
- Electrical continuity

Au-Al intermetallic growth:
~1 μm after 1000h at 150°C
Becomes brittle at >5 μm thickness
```

**HAST (Highly Accelerated Stress Test):**

```
Conditions:
- Temperature: 130°C
- Relative humidity: 85%
- Bias voltage: Applied
- Duration: 96-264 hours

Accelerates:
- Corrosion
- Electrochemical migration
- Bond degradation

Equivalent: Years of field operation
```

### Common Defects

| Defect | Cause | Effect | Solution |
|--------|-------|--------|----------|
| Non-stick | Contamination, low energy | Open circuit | Clean, increase parameters |
| Cratering | Excessive force/power | Die damage, weak bond | Reduce force, optimize |
| Wire sweep | Adjacent wire interference | Short circuit | Optimize sequence, loop height |
| Lifted ball | Weak bond, over-stress | Intermittent failure | Increase bond strength |
| Thin neck | Improper FAB, old capillary | Weak point, breaks | Replace capillary, adjust EFO |
| Pad damage | Pad too thin, high force | Reliability issue | Increase pad thickness |
| Missing wire | Feed issue, clamp problem | Open circuit | Check wire feed system |
| Tail length | Improper breaking | Short risk | Adjust break parameters |

## Advanced Techniques

### Fine Pitch Bonding

**Challenges:**

```
Pitch <50 μm:
- Smaller wire required (18-20 μm)
- Tighter placement tolerance (±5 μm)
- Risk of wire-to-wire short
- Smaller bond pad size

Solutions:
- High-precision bonder (±3 μm)
- Finer capillaries
- Better vision system (1 μm resolution)
- Optimized bonding sequence
```

### Stacked Die Bonding

**Applications:**
- 3D memory (HBM - High Bandwidth Memory)
- Multi-chip modules
- System-in-Package (SiP)

**Challenges:**

```
Wire span variation:
- Bottom die: 2-3 mm span
- Middle die: 4-5 mm span  
- Top die: 6-8 mm span

Loop height management:
- Must clear lower die bonds
- Typically 500-1000 μm for stacked

Solutions:
- Reverse bonding (start from top die)
- Extended capillaries
- Multiple loop profiles
```

### Long Wire Bonding

**Requirements:**

```
For spans >5 mm:
- Larger wire diameter (1.5-2.0 mil)
- Higher loop height (>800 μm)
- Optimized loop trajectory
- May require multiple bonds (stitch bonds)

Applications:
- Multi-chip modules
- Board-level connections
- Power modules (wide spacing)
```

### Ribbon Bonding

For high-current applications:

```
Material: Aluminum or gold ribbon
Size: 125-500 μm wide × 25-75 μm thick
Current capacity: 5-50 A

Process:
- Similar to wedge bonding
- Rectangular cross-section
- Lower loop height
- Multiple ribbons for very high current

Advantages:
- High current capacity
- Lower resistance than round wire
- Better heat dissipation

Applications:
- Power MOSFET/IGBT
- LED packages
- High-power RF
```

## Cost Analysis

**Equipment Costs:**

```
Manual bonder: $50,000-100,000
  - Speed: 3-5 bonds/sec
  - Operator dependent
  - R&D, low volume

Automatic bonder: $150,000-300,000
  - Speed: 8-12 bonds/sec
  - Pattern recognition
  - Medium volume

High-speed bonder: $300,000-500,000
  - Speed: 15-20 bonds/sec
  - Multi-head option
  - High volume (>10M units/year)
```

**Operating Costs:**

```
Wire cost (per 1000 bonds):
- Au (25 μm): $0.10-0.20
- Cu (25 μm): $0.01-0.02
- Al (50 μm): $0.001-0.005

Labor:
- Manual: $20-40 per hour
- Automatic: $0.50-2.00 per hour (operator/machine)

Consumables:
- Capillaries: $50-200 each, 10-50M bonds life
- Maintenance: 5-10% of equipment cost/year

Total cost per bond: $0.001-0.01
```

**Throughput Calculation:**

```
Example: 20-pad device
Bonding time: 20 bonds × 0.1 sec = 2 sec
Index time: 0.5 sec
Cycle time: 2.5 sec/device

Throughput: 1440 devices/hour
Annual (85% uptime): 10.7M devices/year

ROI: <1 year for high volume
```

## Design Guidelines

### Best Practices ✓

```
✓ Pad pitch ≥ 3× wire diameter
✓ Pad opening 10-20 μm larger than pad
✓ Aluminum pad thickness 0.5-1.5 μm
✓ Passivation opening avoids pad edge
✓ Bond pads away from die edges (>100 μm)
✓ Avoid bonding over active circuits
✓ Use staggered pad rows for density
✓ Specify bond pad location tolerance (±25 μm)
✓ Allow clearance for loop height (+200 μm min)
✓ Design for standard wire sizes
```

### Avoid ✗

```
✗ Pads on passivation edges (weak bonds)
✗ Pads in die corners (high stress)
✗ Thin pad metal (<0.5 μm) for Al
✗ Sharp corners on pads (stress concentration)
✗ Pads over voids in die structure
✗ Inconsistent pad heights (multi-level)
✗ Tight pitch without design rule check
✗ Long spans without adequate wire diameter
✗ Mixed wire types in same package
✗ Bonding over underfilled areas
```

## Future Trends

### Copper Wire Adoption

**Status:**
- Currently 50-60% of ball bonding market
- Growing due to cost and performance
- Mainstream in automotive and smartphones

**Challenges:**
- Oxidation control
- Harder on equipment
- Requires process adaptation

### Advanced Materials

**Silver Wire:**
- Better conductivity than copper (105% IACS)
- Less oxidation than copper
- Higher cost than copper, lower than gold
- Emerging for high-frequency applications

**Insulated Wire:**
- Polymer-coated wire (parylene, polyimide)
- Allows wire crossings
- Enables denser pad layouts
- Current limitation: reliability

### Automation Advances

**AI/Machine Learning:**
- Predictive maintenance
- Adaptive process control
- Defect prediction
- Optimal bonding sequence generation

**High-Speed Multi-Head:**
- 2-4 bonding heads simultaneously
- 30-40 bonds/sec total
- Better economics for high pin count

## References

1. Harman, G. G. (2010). *Wire Bonding in Microelectronics* (3rd ed.). McGraw-Hill.

2. Chauhan, P., et al. (2005). Copper wire bonding. *Microelectronics Reliability*, 45(3-4), 583-593.

3. Horsting, C. W. (1972). Purple plague and gold purity. *International Reliability Physics Symposium*, 155-158.

4. Liu, J., et al. (2016). Thermosonic wire bonding process simulation and bond strength prediction. *IEEE Transactions on Components, Packaging and Manufacturing Technology*, 6(10), 1467-1475.

---

**Document Information:**
- **Created:** December 14, 2025
- **Version:** 1.0
- **Status:** Complete
- **Part of:** Silicon Fabrication Handbook
- **Next Chapter:** [Flip Chip](flip-chip.md)
- **Previous Chapter:** [Die Preparation](die-preparation.md)

**License:** CC BY 4.0 - Free to use with attribution

---

*For questions, corrections, or contributions, please visit:*
https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook
