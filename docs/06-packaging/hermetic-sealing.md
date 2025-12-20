# Hermetic Sealing for MEMS Packaging

## Table of Contents
- [Introduction](#introduction)
- [Metal Sealing](#metal-sealing)
- [Glass Sealing](#glass-sealing)
- [Ceramic Packaging](#ceramic-packaging)
- [Leak Testing](#leak-testing)
- [Reliability](#reliability)
- [References](#references)

## Introduction

Hermetic sealing prevents moisture, oxygen, and contaminants from entering the package, essential for high-reliability MEMS devices and harsh environment applications.

### Hermeticity Definition

**Leak Rate Standards:**

```
True hermetic: Leak rate <5×10⁻⁹ atm·cm³/s (He)
                        <1×10⁻⁸ atm·cm³/s (air)

Equivalent to:
- <0.1 μm³ He per year at 1 atm
- Internal pressure change <1% over 10 years

Non-hermetic (for comparison):
- Plastic packages: 10⁻⁴ to 10⁻⁶ atm·cm³/s
- Orders of magnitude higher leakage
```

### Applications Requiring Hermetic Sealing

| Application | Environment | Leak Rate Required | Package Type |
|-------------|-------------|-------------------|--------------|
| MEMS gyroscope | Vacuum (0.01 Pa) | <10⁻¹⁰ atm·cm³/s | Metal/ceramic |
| MEMS resonator | Vacuum/controlled | <10⁻⁹ atm·cm³/s | Metal/ceramic |
| Pressure sensor | Absolute reference | <10⁻⁹ atm·cm³/s | Metal/glass |
| Aerospace sensor | -55 to 125°C, radiation | <10⁻⁹ atm·cm³/s | Ceramic |
| Automotive sensor | -40 to 150°C, humidity | <10⁻⁸ atm·cm³/s | Metal/ceramic |
| Medical implant | Body fluids, 37°C | <10⁻⁹ atm·cm³/s | Ceramic/Ti |

### Hermetic vs Non-Hermetic

**Lifetime Comparison:**

```
Non-hermetic package:
- Moisture ingress: Days to months
- Corrosion starts: Weeks to months
- Device failure: Months to few years

Hermetic package:
- Moisture ingress: Negligible over decades
- Corrosion: Minimal (initial trapped moisture only)
- Device lifetime: 20-30 years typical
```

### Sealing Technologies Overview

| Technology | Temperature | Materials | Leak Rate | Cost | Volume |
|------------|-------------|-----------|-----------|------|--------|
| Resistance welding | 800-1400°C | Kovar, steel | 10⁻¹⁰ | Medium | High |
| Laser welding | Local >1000°C | Most metals | 10⁻¹⁰ | Medium | Medium-High |
| Solder sealing | 180-450°C | Many alloys | 10⁻⁹ | Low | High |
| Glass frit | 400-500°C | Glass/metal | 10⁻⁹ | Low | High |
| Anodic bonding | 300-450°C | Si/glass | 10⁻⁹ | Medium | Medium |
| Eutectic bonding | 280-420°C | Metal alloys | 10⁻⁹ | Medium | Medium |

## Metal Sealing

### Resistance Seam Welding

Most common for metal can packages.

**Process:**

```
Equipment: Roller electrodes

Parameters:
- Current: 50-500 A (pulsed)
- Voltage: 2-10 V
- Roller force: 50-500 N
- Speed: 10-100 mm/s
- Pulse frequency: 50-500 Hz

Process:
1. Position lid on base (with die inside)
2. Apply pressure via rollers
3. Pass current through metal-to-metal interface
4. Localized heating melts metal
5. Pressure creates weld seam
6. Move rollers to weld entire perimeter

Seam width: 0.5-2 mm
Penetration: 20-50% of material thickness
```

**Materials:**

```
Common alloys:
- Kovar (Fe-29Ni-17Co)
  - CTE: 5.5 ppm/°C (matches ceramic, glass)
  - Weldable, good hermeticity
  - Cost: High

- Alloy 42 (Fe-42Ni)
  - CTE: 4.5 ppm/°C
  - Lower cost than Kovar
  - Good for sealing

- Stainless steel 304/316
  - CTE: 17 ppm/°C
  - Lower cost
  - CTE mismatch with Si/ceramic

Metal thickness: 0.2-0.8 mm typical
Sealing ring width: 0.5-2 mm
```

**Package Configuration:**

```
Standard metal can:

Lid (metal)
  ↓ (seam weld)
Frame (metal ring)
  ↓ (braze or weld)
Ceramic base
  ↓
Die attach
  ↓
MEMS die

Package sizes: 5×5 to 50×50 mm
Height: 1-10 mm
Volume: 0.1-10 cm³
```

**Advantages:**
- Excellent hermeticity (<10⁻¹⁰ atm·cm³/s)
- High reliability
- Proven technology (60+ years)
- High volume capable
- Reworkable (re-weld if needed)

**Limitations:**
- Requires flat sealing surfaces
- Metal parts add cost
- Larger package size
- Limited to metal lids

### Laser Welding

Precise, localized heating for hermetic seals.

**Process Types:**

```
1. Conduction welding:
   - Laser heats surface
   - Heat conducts through material
   - Melting at interface
   - Lower power (50-500 W)

2. Keyhole welding:
   - High power penetrates material
   - Creates vapor cavity
   - Deeper weld (1-3 mm)
   - Higher power (500-5000 W)
```

**Laser Types:**

| Type | Wavelength | Power | Beam Quality | Cost | Applications |
|------|------------|-------|--------------|------|--------------|
| Nd:YAG | 1064 nm | 10-500 W | Good | Medium | General, pulsed |
| Fiber laser | 1070 nm | 100-10000 W | Excellent | Medium | High power, CW |
| Diode laser | 808-980 nm | 10-500 W | Fair | Low | Low precision |
| Green laser | 532 nm | 10-100 W | Good | High | Reflective metals |

**Process Parameters:**

```
Pulsed welding:
- Power: 100-500 W peak
- Pulse width: 0.5-10 ms
- Frequency: 10-100 Hz
- Spot size: 0.1-1 mm
- Speed: 10-100 mm/s

Continuous wave (CW):
- Power: 50-500 W
- Spot size: 0.05-0.5 mm
- Speed: 50-500 mm/s

Typical depth: 0.2-1 mm
Weld width: 0.2-0.8 mm
```

**Atmosphere Control:**

```
Critical for reactive metals (Ti, Al):

Chamber: Sealed glove box or local shield
Atmosphere: 
- Ar or N₂ (>99.99% purity)
- <100 ppm O₂
- <50 ppm H₂O

Benefits:
- Prevents oxidation
- Better weld quality
- Improved hermeticity
- Required for Ti packages
```

**Advantages:**
- Non-contact (no mechanical stress)
- Precise control
- Small heat-affected zone (HAZ)
- Suitable for thin materials (<0.5 mm)
- Flexible shapes

**Limitations:**
- Higher equipment cost ($100K-500K)
- Requires good surface preparation
- Sensitive to joint fit-up (<50 μm gap)
- Operator skill dependent

### Solder Sealing

Lower temperature hermetic sealing using solder alloys.

**Solder Materials:**

```
High-Temperature Solders (>250°C):

Au-Sn (80/20 eutectic):
- Melting point: 280°C
- Excellent hermeticity
- High cost ($500-1000/kg)
- Applications: High-rel, aerospace

Au-Si (97/3 eutectic):
- Melting point: 363°C
- Si substrate compatible
- Very high cost
- Wafer-level bonding

Pb-Sn (95/5):
- Melting point: 300-320°C
- RoHS exempt (high-temp)
- Good for automotive
- Cost: Medium ($20-50/kg)

Low-Temperature Solders (<250°C):

Sn-Ag-Cu (SAC305):
- Melting point: 217°C
- Lead-free standard
- Good reliability
- Cost: Low ($15-30/kg)

Sn-Pb (63/37 eutectic):
- Melting point: 183°C
- Legacy, RoHS restricted
- Excellent properties
- Cost: Low ($10-20/kg)
```

**Preform vs Paste:**

| Method | Form | Thickness Control | Cost | Volume | Void Rate |
|--------|------|-------------------|------|--------|-----------|
| Preform | Solid ring | ±10 μm | Medium | Medium-High | <1% |
| Paste | Screen print | ±20 μm | Low | High | 2-5% |
| Electroplate | Plated layer | ±5 μm | High | Low-Medium | <0.5% |

**Sealing Process:**

```
Preform method:

1. Surface preparation
   - Clean with solvent (IPA)
   - Plasma clean (optional)
   - Apply flux (tacky flux holds preform)

2. Place preform
   - Align on sealing ring
   - Ensure good contact

3. Position lid
   - Align with fixture
   - Light weight for stability

4. Reflow
   - Ramp: 2-5°C/min to peak
   - Peak: Tm + 20-40°C
   - Time above liquidus: 30-90 sec
   - Atmosphere: N₂ or forming gas
   - Pressure: Ambient or controlled

5. Cool
   - Rate: 2-5°C/min (controlled)
   - Avoid thermal shock
   - To <150°C before handling

Seal width: 0.3-1.5 mm
Thickness after reflow: 10-50 μm
Bond strength: 20-50 MPa
```

**Metallization Requirements:**

```
For solder wetting:

Base metallization:
- Ti/Pt/Au: 50/100/200 nm (sputtered)
- Ti/Ni/Au: 50/300/100 nm
- Cr/Cu/Au: 50/500/100 nm

Purpose:
- Ti/Cr: Adhesion to Si/ceramic
- Pt/Ni/Cu: Diffusion barrier
- Au: Solderable, prevents oxidation

Alternative (plating):
- Ni(P) electroless: 3-5 μm
- Au flash: 0.05-0.1 μm (immersion)
```

**Advantages:**
- Lower temperature than welding
- Lower equipment cost
- Reworkable (reheat and reseal)
- Suitable for complex geometries
- Good for mixed materials

**Limitations:**
- Flux residue (requires cleaning)
- Thermal cycling can cause fatigue
- Intermetallic growth over time
- Lower temperature capability

## Glass Sealing

### Glass Frit Bonding

Low-melting-point glass for hermetic sealing.

**Glass Composition:**

```
Traditional (leaded):
- PbO-B₂O₃-SiO₂
- Melting point: 400-450°C
- CTE: 4-9 ppm/°C (adjustable)
- Best properties
- RoHS restricted (electronics)

Lead-free:
- Bi₂O₃-B₂O₃-SiO₂-ZnO
- Melting point: 430-480°C
- CTE: 5-10 ppm/°C
- Environmental compliance
- Slightly lower performance

Vanadium-based:
- V₂O₅-P₂O₅-BaO
- Melting point: 350-400°C
- Very low temp option
- Higher cost
```

**Process:**

```
Screen printing method:

1. Prepare frit paste
   - Glass powder: 70-85 wt%
   - Organic binder: 10-20 wt%
   - Solvent: 5-10 wt%
   - Particle size: 1-10 μm

2. Screen print on substrate/lid
   - Mesh: 200-325 (openings/inch)
   - Thickness wet: 50-150 μm
   - Pattern: Seal ring (0.3-1 mm width)

3. Dry
   - Temperature: 150°C
   - Time: 30 min
   - Removes solvent

4. Align and bond
   - Position lid on base
   - Apply pressure: 0.1-1 MPa
   - Heat profile:
     * Ramp: 5-10°C/min
     * Peak: Tm + 50-80°C
     * Dwell: 10-30 min at peak
     * Cool: 5-10°C/min

5. Final bond line: 10-50 μm
```

**Advantages:**
- True hermetic seal
- CTE can be tailored
- Transparent options (inspection)
- Established process
- Suitable for ceramic, Si, metal

**Limitations:**
- Relatively high temperature (>400°C)
- Outgassing during bonding
- Requires good surface flatness
- Brittle material

### Anodic Bonding

Electric field-assisted glass-to-silicon bonding.

**Process Principle:**

```
Mechanism:
- Glass (usually Pyrex) contains Na⁺ ions
- Apply voltage: Glass negative, Si positive
- Na⁺ migrate away from interface under field
- Leaves negative charge at interface
- Electrostatic attraction pulls surfaces together
- Si-O-Si bonds form (chemical bonding)

Permanent, strong, hermetic seal
```

**Process Parameters:**

```
Standard conditions:

Temperature: 300-450°C
Voltage: 200-1000 V DC
Pressure: 0.1-1 MPa
Time: 10-30 minutes
Atmosphere: Vacuum, N₂, or air

Current profile:
- Initial: High current (100-500 mA)
- As bonding progresses: Current drops
- Complete: <10 mA (indicator)

Bond wave:
- Starts at anode contact point
- Propagates across wafer
- Visible in real-time (Newton rings)
```

**Material Requirements:**

```
Silicon:
- Conductivity: 0.1-100 Ω·cm (doped)
- Highly doped or metal layer needed
- Intrinsic Si: Too resistive

Glass:
- Pyrex 7740 (Corning)
- CTE: 3.3 ppm/°C (matches Si: 2.6 ppm/°C)
- Na₂O content: 4-5%
- Thickness: 0.3-1.5 mm

Surface requirements:
- Flatness: <2 μm (across bond area)
- Roughness: Ra <10 nm
- Clean: Particles >1 μm cause voids
```

**Advantages:**
- Excellent hermeticity
- Transparent glass (optical access)
- No intermediate layer
- Strong bond (10-20 MPa)
- Suitable for vacuum encapsulation

**Limitations:**
- Requires conductive Si wafer
- High temperature (stress)
- Glass only (not metal, ceramic)
- Requires very flat surfaces
- Not reworkable

**Applications:**

```
Common uses:
- Pressure sensor caps
- MEMS resonator caps (transparent)
- Microfluidic chips
- Lab-on-chip devices
- Vacuum reference cavities

Example: Absolute pressure sensor
- Si die with piezoresistors
- Vacuum cavity (reference)
- Glass cap (anodic bonded)
- Pressure access from backside
```

## Ceramic Packaging

Industry standard for high-reliability hermetic packages.

### Package Styles

**1. Flatpack:**

```
Structure:
- Ceramic base (Al₂O₃, AlN)
- Metal leads brazed in (Kovar)
- Die attach area (Au-plated)
- Metal lid (seam weld or solder seal)

Sizes: 5×5 to 30×30 mm
Height: 1-3 mm
Leads: 8-64 (perimeter)

Cost: $5-20 per package
Volume: Medium-High

Applications:
- Military/aerospace
- Automotive sensors
- Industrial
```

**2. Ceramic DIP (Dual In-line Package):**

```
Through-hole package:
- Ceramic body (Al₂O₃)
- Leads: 8-64 pins
- 0.1" (2.54 mm) spacing
- Metal lid (seam weld)

Advantages:
- Easy prototyping
- Socket-able
- High reliability
- Good for harsh environment

Cost: $2-10 per package
```

**3. Ceramic LCC (Leadless Chip Carrier):**

```
Surface mount:
- Castellated contacts
- No leads (J-leads optional)
- Compact (1-2 mm height)

Sizes: 3×3 to 15×15 mm
I/O: 20-100 contacts

Cost: $3-15 per package
```

**4. Ceramic PGA (Pin Grid Array):**

```
High I/O count:
- Pins on bottom (grid)
- 100-500 pins possible
- Large die (10-30 mm)

Cost: $20-100 per package
Applications: High-end processors, FPGAs
```

### Ceramic Materials

**Alumina (Al₂O₃):**

```
Properties:
- Purity: 96-99.6%
- Thermal conductivity: 20-30 W/m·K (96%)
                        30-40 W/m·K (99.6%)
- CTE: 6.5-7.5 ppm/°C
- Dielectric constant: 9-10
- Color: White

Cost: Low ($0.10-0.50/cm²)
Volume: Very high

Advantages:
- Standard material
- Good electrical insulation
- Adequate thermal performance
- Low cost

Limitations:
- CTE mismatch with Si (2.6 ppm/°C)
- Moderate thermal conductivity
```

**Aluminum Nitride (AlN):**

```
Properties:
- Thermal conductivity: 150-180 W/m·K
  (5-6× better than Al₂O₃)
- CTE: 4.5 ppm/°C (closer to Si)
- Dielectric constant: 8-9
- Color: Gray

Cost: High ($2-10/cm²)

Advantages:
- Excellent thermal performance
- Better CTE match to Si
- High power applications
- RF applications (low loss)

Limitations:
- Higher cost (5-10× Al₂O₃)
- More difficult to process
- Limited suppliers
```

**Other Ceramics:**

| Material | Thermal Cond. | CTE | Cost | Applications |
|----------|---------------|-----|------|--------------|
| BeO | 250 W/m·K | 7.5 ppm/°C | Very high | Legacy high power |
| AlSiC (metal matrix) | 120-200 W/m·K | 6-9 ppm/°C | High | RF, high power |
| LTCC (Low-temp co-fired) | 3-5 W/m·K | 5-7 ppm/°C | Medium | Integrated passive |

### Metallization

**Thick Film:**

```
Process:
1. Screen print metal paste
   - Au: 80-90 wt% in organic binder
   - Ag: Lower cost alternative
   - Thickness wet: 20-30 μm

2. Dry at 150°C

3. Fire in belt furnace
   - Temperature: 850-900°C (Au)
                 650-750°C (Ag)
   - Atmosphere: Air or N₂
   - Time: 10-60 min

4. Final thickness: 8-15 μm

Advantages:
- Low cost tooling
- Flexible design
- Quick turnaround

Limitations:
- Lower resolution (100 μm min)
- Rough surface (Ra: 0.5-2 μm)
- Electrical resistance higher than thin film
```

**Thin Film:**

```
Process:
1. Sputter Ti adhesion: 50-100 nm
2. Sputter metal:
   - Cu: 2-5 μm (low resistance)
   - Au: 0.5-2 μm (corrosion resistant)

3. Pattern by photolithography

4. Plate additional metal if needed
   - Electroplate Au: 3-10 μm
   - For wire bonding or soldering

Final thickness: 3-15 μm

Advantages:
- Fine features (10-20 μm)
- Smooth surface (Ra: <50 nm)
- Low electrical resistance
- Better for high frequency

Limitations:
- Higher tooling cost
- More process steps
- Longer lead time
```

### Ceramic Sealing Methods

**Kovar Ring Brazing:**

```
Process:
1. Attach Kovar ring to ceramic
   - Brazing alloy: 72%Ag-28%Cu (eutectic, 780°C)
   - Or: Au-Ni, Au-Sn for lower temp
   - Furnace braze: 800-900°C, vacuum

2. Result: Metal ring permanently attached

3. Seal lid to ring (welding or solder)
   - Seam weld: Standard
   - Laser weld: Alternative
   - Solder: Lower temperature option

Advantages:
- Strong, reliable
- Industry standard
- Proven over decades

Cost: +$2-5 per package (ring + braze)
```

## Leak Testing

Critical for qualifying hermetic packages.

### Fine Leak Test (Helium)

**MIL-STD-883 Method 1014:**

```
Process:
1. Bomb (pressurize with He):
   - Helium pressure: 2-5 atm
   - Temperature: 85-125°C
   - Time: 2-12 hours
   - He permeates into package through leaks

2. Remove, wipe exterior

3. Place in He leak detector
   - Mass spectrometer
   - Sensitivity: 10⁻¹² atm·cm³/s
   - Measurement time: 1-5 min

4. He leaks out through same path
   - Measured leak rate
   - Rejection if > specification

Typical limits:
- Hermetic: <5×10⁻⁹ atm·cm³/s
- High-rel: <1×10⁻⁹ atm·cm³/s
```

**Calculated Leak Rate:**

```
R = (ΔP × V) / (P_atm × t)

Where:
R = leak rate (atm·cm³/s)
ΔP = He partial pressure rise
V = package volume (cm³)
P_atm = atmospheric pressure (1 atm)
t = time (s)

Example:
Package volume: 0.1 cm³
Measured: 5×10⁻⁹ atm·cm³/s

Internal pressure change per year:
ΔP = (R × t × P_atm) / V
   = (5×10⁻⁹ × 3.15×10⁷ × 1) / 0.1
   = 0.0016 atm = 0.16% per year

Acceptable for 20-year life
```

### Gross Leak Test

**Methods:**

```
1. Bubble test:
   - Immerse package in fluorocarbon liquid
   - Heat to 125°C
   - Look for bubbles (gross leaks)
   - Detect: >10⁻⁵ atm·cm³/s

2. Radioisotope (Krypton-85):
   - Bomb with Kr-85
   - Measure radioactivity of package
   - Detects: >10⁻⁷ atm·cm³/s

3. Weight gain (moisture):
   - Expose to steam (121°C, 100% RH)
   - Weigh before/after
   - Moisture ingress indicates leak
```

### Acceptance Criteria

**MIL-STD-883:**

```
Package Volume (V):

V < 0.05 cm³:    R < 5×10⁻⁸ atm·cm³/s
0.05 ≤ V < 0.5:  R < 5×10⁻⁸ atm·cm³/s
0.5 ≤ V < 1.0:   R < 1×10⁻⁷ atm·cm³/s
V ≥ 1.0 cm³:     R < 1×10⁻⁶ atm·cm³/s

For high-reliability:
R < 1×10⁻⁹ atm·cm³/s (all volumes)

Automotive (AEC-Q100):
R < 5×10⁻⁹ atm·cm³/s

Medical implants:
R < 1×10⁻⁹ atm·cm³/s
```

## Reliability

### Failure Mechanisms

**1. Seal Degradation:**

```
Causes:
- Intermetallic growth (solder seals)
- Stress cracking (thermal cycling)
- Corrosion (moisture, contaminants)
- Mechanical damage

Prevention:
- Proper material selection
- Adequate seal width (>0.5 mm)
- Stress relief features
- Clean room assembly
```

**2. Moisture Ingress:**

```
Effects:
- Metal corrosion (Al especially)
- Delamination
- Electrical shorts
- Device drift

Sources:
- External (through leak)
- Internal (trapped during sealing)

Getters help absorb internal moisture:
- Molecular sieve
- CaO pellets
- Metal getters (Ti, Zr)
```

**3. Outgassing:**

```
Materials that outgas:
- Adhesives (die attach)
- Wires (insulation)
- Labels, markings
- Flux residues

Effects:
- Contamination
- Pressure rise
- Surface deposition

Prevention:
- Bake before sealing (150°C, 24h)
- Use low-outgassing materials
- High-vacuum seal (<1 Pa)
- Getters
```

### Reliability Testing

**Temperature Cycling:**

```
MIL-STD-883, Method 1010:

Condition C: -65°C to +150°C
- Dwell: 15 min each extreme
- Ramp: <1 min
- Cycles: 100-1000

Condition B: -55°C to +125°C
- Similar profile
- More common for commercial

Automotive (AEC-Q100):
- -40°C to +150°C
- 1000 cycles minimum

Acceptance:
- No seal cracks (visual/X-ray)
- Leak rate unchanged
- Electrical parameters within spec
```

**High Temperature Storage:**

```
Conditions:
- Temperature: 150°C (standard)
                175°C (harsh)
                200°C (extreme)
- Duration: 500-2000 hours

Monitors:
- Seal integrity (leak test before/after)
- Internal atmosphere (if possible)
- Electrical continuity

Failure modes:
- Intermetallic growth (solder)
- Oxidation (if not inert atmosphere)
- Material diffusion
```

**HAST/Autoclave:**

```
Highly Accelerated Stress Test:

Unbiased:
- 130°C, 85% RH
- 96-264 hours

Biased:
- Same temp/humidity
- Apply voltage
- Accelerates corrosion/migration

Autoclave (milder):
- 121°C, 100% RH, 2 atm
- 96-336 hours

For hermetic packages:
- Should show no degradation
- If failure: seal leak detected
```

**Thermal Shock:**

```
MIL-STD-883, Method 1011:

Conditions:
- Cold: -65°C (liquid bath)
- Hot: +150°C (liquid bath)
- Transfer time: <10 seconds
- Dwell: 5-15 min each
- Cycles: 15-100

Stress:
- Maximum thermal gradient
- Tests CTE mismatch
- Seal robustness

Common for:
- Ceramic packages
- Glass seals
- Mixed material systems
```

## Cost Comparison

**Package Cost vs Performance:**

| Package Type | Cost | Hermeticity | Thermal | Complexity |
|--------------|------|-------------|---------|------------|
| Plastic QFN | $0.10-0.50 | Poor | Medium | Low |
| WLCSP | $1-3 | Poor | Good | Medium |
| Solder seal ceramic | $3-8 | Excellent | Good | Medium |
| Welded metal can | $5-15 | Excellent | Excellent | High |
| AlN ceramic | $10-30 | Excellent | Excellent | High |

**When to Use Hermetic:**

```
Required:
- Military/aerospace
- Long life (>10 years)
- Harsh environment
- High reliability (99.9%+)
- MEMS requiring vacuum/inert gas

Optional (cost trade-off):
- Automotive (some use hermetic, some polymer)
- Industrial (depends on environment)
- Medical (implantable: yes, disposable: no)

Not needed:
- Consumer electronics (short life acceptable)
- Indoor benign environment
- Cost-sensitive applications
```

## Design Guidelines

### Best Practices ✓

```
✓ Seal width ≥0.5 mm (wider for reliability)
✓ Flat sealing surfaces (<2 μm variation)
✓ Surface finish: Ra <1 μm (better sealing)
✓ Clean assembly (Class 100 clean room)
✓ Avoid trapped voids (vent paths during seal)
✓ Use getters for vacuum/controlled atmosphere
✓ Bake components before sealing (150°C, 24h)
✓ Specify leak rate in design requirements
✓ Test 100% for high-reliability applications
✓ Document internal atmosphere composition
```

### Avoid ✗

```
✗ Narrow seal rings (<0.3 mm)
✗ Rough surfaces (poor seal quality)
✗ Contaminated surfaces (oils, particles)
✗ Excessive internal volume (more outgassing)
✗ High-outgassing materials inside
✗ Sharp corners (stress concentration)
✗ Mismatched CTEs without stress relief
✗ Overly complex seal geometries