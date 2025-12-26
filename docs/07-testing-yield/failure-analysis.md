# Failure Analysis for MEMS

## Table of Contents
- [Introduction](#introduction)
- [FA Process Flow](#fa-process-flow)
- [Non-Destructive Analysis](#non-destructive-analysis)
- [Destructive Analysis](#destructive-analysis)
- [Root Cause Analysis](#root-cause-analysis)
- [Case Studies](#case-studies)
- [References](#references)

## Introduction

Failure Analysis (FA) identifies the root cause of device failures to improve design, process, and reliability. FA is critical for yield improvement and preventing field failures.

### FA Objectives

```
Primary goals:
1. Identify failure mechanism
2. Determine root cause
3. Recommend corrective action
4. Prevent recurrence
5. Improve reliability

Types of analysis:
- Design FA: Design weaknesses
- Process FA: Manufacturing defects
- Reliability FA: Wear-out mechanisms
- Customer return FA: Field failures
```

### FA Priority

**Failure Classification:**

| Priority | Description | Response Time | Resources |
|----------|-------------|---------------|-----------|
| P1 - Critical | Line down, customer impact | <24 hours | All resources |
| P2 - High | Yield loss, reliability risk | 2-3 days | Dedicated team |
| P3 - Medium | Quality concern, escapes | 1-2 weeks | Standard FA |
| P4 - Low | Isolated, engineering sample | As available | Minimal |

### FA Team

```
Required expertise:
- FA engineer (lead)
- Process engineer (fab knowledge)
- Design engineer (circuit/layout)
- Package engineer (if package-related)
- Reliability engineer (if stress-related)
- Equipment specialist (if tool issue)

External resources:
- Analytical lab (SEM, TEM, FIB)
- Material analysis (EDX, SIMS, XPS)
- Vendor support (equipment, materials)
```

## FA Process Flow

### Standard FA Flow

```
Stage 1: Information Gathering (1-2 hours)
├── Failure symptoms
├── Test data and logs
├── Manufacturing history
├── Known good unit for comparison
└── Preliminary hypothesis

Stage 2: Non-Destructive Analysis (1-4 hours)
├── Visual inspection (optical microscope)
├── X-ray imaging
├── Acoustic microscopy (SAM)
├── Electrical characterization
└── Thermal imaging (if applicable)

Stage 3: Destructive Analysis (1-3 days)
├── Decapsulation
├── Cross-sectioning
├── SEM/EDX analysis
├── FIB circuit edit (if needed)
└── TEM (if material analysis needed)

Stage 4: Root Cause & Recommendations (1-2 days)
├── Failure mechanism identified
├── Root cause determined
├── Corrective action plan
├── Preventive measures
└── Documentation and report

Total time: 3-7 days typical
           1-2 days for expedited
           2-4 weeks for complex cases
```

### Documentation Requirements

```
FA report must include:
1. Executive summary (1 page)
2. Failure description
3. Sample information and history
4. Analysis techniques used
5. Findings (photos, data)
6. Root cause analysis
7. Recommendations
8. Action items and owners
9. Appendices (detailed data)

Distribution:
- FA database (searchable)
- Engineering teams
- Management (summary)
- Customer (if required)
```

## Non-Destructive Analysis

### Visual Inspection

**Optical Microscopy:**

```
Equipment:
- Stereo microscope: 7-45× magnification
- Metallurgical microscope: 50-1000×
- Brightfield, darkfield, polarized light

Look for:
- Package damage (cracks, delamination)
- Die surface anomalies
- Wire bond issues
- Contamination
- Discoloration (overheating)
- Corrosion

Advantages:
- Fast (minutes)
- Non-destructive
- Low cost
- Good overview

Limitations:
- Surface only
- Limited resolution (~1 μm)
- No sub-surface defects
```

**Typical Observations:**

| Defect | Appearance | Likely Cause |
|--------|------------|--------------|
| Cratering | Concave pit at bond | Excessive bonding force |
| Wire discoloration | Purple/black | Overheating, EOS |
| Die cracking | Visible crack lines | Mechanical stress, thermal |
| Corrosion | White/green residue | Moisture + contamination |
| Delamination | Gap, non-uniform color | Poor adhesion |
| Contamination | Particles, foreign material | Process contamination |

### X-Ray Inspection

**2D Transmission X-Ray:**

```
Equipment:
- X-ray source: 50-150 kV
- Detector: Flat panel or camera
- Magnification: 10-1000×
- Resolution: 1-10 μm

Applications:
- Wire bond integrity
- Die attach voids
- Solder joint quality
- Package cracking
- Internal structure

Grayscale:
- Dark: High density (metal, Si)
- Light: Low density (void, air)
- Crack: Sharp dark line

Time: 1-5 minutes per sample
Cost: $50-200 per sample
```

**3D Computed Tomography (CT):**

```
Advanced X-ray:
- Multiple angles (360° rotation)
- 3D reconstruction
- Sub-micron resolution possible

Applications:
- Complex 3D structures
- Exact void location/size
- Package integrity
- MEMS structure verification

Advantages:
- True 3D visualization
- Precise void quantification
- Non-destructive

Limitations:
- Time-consuming (30-60 min/sample)
- Expensive ($500-2000 per sample)
- Limited availability

When to use:
- High-value failures
- Complex geometry
- Exact void measurement needed
```

### Acoustic Microscopy (SAM)

**Scanning Acoustic Microscopy:**

```
Principle:
- Ultrasonic waves (10-400 MHz)
- Reflection at interfaces
- Delamination detected by echo

Equipment:
- Transducer (ultrasonic probe)
- Water coupling medium
- Scan stage
- Display (C-SAM image)

Applications:
- Die attach delamination
- Underfill voids
- Package delamination
- Cracks in passivation
- Mold compound defects

Image interpretation:
- White: Good adhesion (no reflection)
- Dark/black: Delamination (strong reflection)
- Gray: Partial or subsurface

Resolution: 5-50 μm depending on frequency
Time: 5-15 minutes per sample
Cost: $100-300 per sample
```

**Frequency Selection:**

```
High frequency (100-400 MHz):
- Better resolution (5-10 μm)
- Shallow penetration (<1 mm)
- Use for: Near-surface defects

Low frequency (10-50 MHz):
- Lower resolution (20-50 μm)
- Deep penetration (>5 mm)
- Use for: Package-level defects

Typical: 50 MHz for most MEMS FA
```

### Electrical Characterization

**Curve Tracing:**

```
I-V Curve Analysis:

Normal behavior:
- Diode: Forward voltage ~0.7V, reverse block
- Resistor: Linear I-V
- Capacitor: Charging current only

Failure signatures:
- Short: High current, low voltage
- Open: No current flow
- High leakage: Excessive current
- Soft breakdown: Non-linear, unstable

Equipment:
- Curve tracer: Tektronix 370/371
- SMU: Keithley 2400 series
- Oscilloscope + function generator

Time: 5-30 minutes
```

**Comparison Testing:**

```
Side-by-side comparison:
- Failing unit
- Known good unit (from same lot)
- Golden reference

Parameters to compare:
- Supply current (IDDQ)
- Leakage current (all pins)
- Capacitance values
- Resistance values
- Functional outputs
- Frequency response

Identify differences:
- Pin-point failure location
- Characterize severity
- Guide subsequent analysis
```

### Thermal Imaging

**Infrared (IR) Thermography:**

```
Equipment:
- IR camera: 8-14 μm wavelength
- Spatial resolution: 10-50 μm
- Temperature resolution: 0.1°C
- Frame rate: 30-1000 Hz

Applications:
- Hot spot detection
- Short circuit location
- Thermal resistance mapping
- Current crowding

Procedure:
1. Remove packaging if opaque
2. Power device (normal or elevated voltage)
3. Capture IR image
4. Identify anomalous heating
5. Correlate to physical location

Time: 10-30 minutes
Advantages: Fast, pinpoints location
Limitations: Requires IR-transparent materials
```

**Lock-In Thermography:**

```
Advanced technique:
- Pulsed power (on/off cycles)
- Phase-sensitive detection
- Detects very small heating

Sensitivity: <0.01°C
Use case: Low-power failures

Example:
- Leakage current 10 μA @ 5V = 50 μW
- Can detect and locate
```

## Destructive Analysis

### Decapsulation

**Chemical Decapsulation:**

```
For plastic packages:

Acid: Fuming nitric acid (HNO₃) or sulfuric acid (H₂SO₄)
Temperature: 100-150°C
Time: 1-4 hours

Process:
1. Mount device in holder
2. Submerge in hot acid
3. Monitor progress (check every 15 min)
4. Stop when die exposed
5. Rinse thoroughly (DI water)
6. Neutralize (if needed)
7. Dry

Safety:
- Fume hood required
- PPE: Face shield, apron, double gloves
- Acid-resistant container
- Emergency procedures

Result: Exposes die with minimal damage
```

**Mechanical Decapsulation:**

```
For metal/ceramic packages:

Method 1 - Grinding:
- Belt sander or grinding wheel
- Remove lid layer by layer
- Stop before reaching die
- Polish to final surface

Method 2 - Milling:
- End mill or ball mill
- CNC controlled for precision
- Remove specific areas
- Good for side access

Method 3 - Laser ablation:
- UV laser removes material
- Precise, minimal damage
- Expensive equipment
- Best for small areas

Time: 30 minutes to 2 hours
```

### Cross-Sectioning

**Sample Preparation:**

```
Standard metallographic process:

1. Mounting:
   - Epoxy encapsulation (cold or hot mount)
   - Position sample at desired angle
   - Cure: 15 min (hot) or overnight (cold)

2. Grinding:
   - SiC paper: 240, 400, 600, 1200 grit
   - Wet grinding to prevent damage
   - Stop near region of interest

3. Polishing:
   - Diamond paste: 6 μm, 3 μm, 1 μm, 0.25 μm
   - Final: Colloidal silica (0.05 μm)
   - Each step: 5-10 minutes
   - Check frequently under microscope

4. Cleaning:
   - Ultrasonic in DI water
   - Dry with N₂

Total time: 2-4 hours for high-quality cross-section
```

**Focused Ion Beam (FIB) Cross-Section:**

```
Precision cross-sectioning:

Equipment:
- FIB-SEM (dual beam)
- Gallium (Ga⁺) ion beam
- Beam current: 1 pA to 20 nA
- Spot size: 5-50 nm

Process:
1. Locate region of interest (SEM)
2. Deposit protective layer (Pt, 1-2 μm)
3. Mill cross-section with ion beam
4. Polish surface (low current)
5. Image with SEM (in-situ)

Advantages:
- Site-specific (±0.5 μm accuracy)
- Minimal damage
- High resolution
- In-situ imaging

Disadvantages:
- Slow (2-6 hours)
- Expensive ($500-2000 per sample)
- Small area only (10-50 μm wide)

When to use:
- Precise location needed
- Small features (<1 μm)
- Minimal damage required
- Layered structures
```

### Scanning Electron Microscopy (SEM)

**Capabilities:**

```
Magnification: 20× to 1,000,000×
Resolution: 1-5 nm (high-end: <1 nm)
Depth of field: 100× optical microscope

Detectors:
1. Secondary Electron (SE):
   - Topography imaging
   - Surface features
   - Resolution: 1-5 nm

2. Backscattered Electron (BSE):
   - Atomic number contrast
   - Material composition
   - Resolution: 10-50 nm

3. Energy Dispersive X-ray (EDX):
   - Elemental analysis
   - Composition mapping
   - Detection: Elements >Be (Z=4)

Typical operation:
- Voltage: 1-30 kV
- Current: 1-100 nA
- Vacuum: 10⁻⁵ to 10⁻⁷ Torr
```

**Failure Analysis Applications:**

```
Common observations:

1. Crack analysis:
   - Crack path and morphology
   - Crack opening (ductile vs brittle)
   - Crack initiation point
   
2. Delamination:
   - Interface identification
   - Contamination at interface
   - Adhesion failure mode

3. Corrosion:
   - Corrosion products (identify with EDX)
   - Extent of damage
   - Corrosion mechanism

4. Electromigration:
   - Void formation
   - Hillock growth
   - Conductor thinning

5. Wire bond failure:
   - Fracture surface analysis
   - Intermetallic identification
   - Bond quality assessment

Imaging time: 15 minutes to 2 hours
Analysis time: Additional 1-4 hours
Cost: $200-1000 per sample
```

### Energy Dispersive X-ray (EDX)

**Elemental Analysis:**

```
Principle:
- Electron beam excites atoms
- Characteristic X-rays emitted
- Energy identifies element
- Intensity indicates concentration

Capabilities:
- Elements: Be (Z=4) to U (Z=92)
- Detection limit: 0.1-1 wt%
- Spatial resolution: 0.5-2 μm
- Quantitative analysis: ±2-5% absolute

Applications:
- Contaminant identification
- Verify material composition
- Corrosion product analysis
- Failure mechanism confirmation
- Foreign material identification

Analysis modes:
1. Point analysis (specific location)
2. Line scan (composition profile)
3. Area map (element distribution)

Time: 1-5 minutes per analysis
```

**Example Analysis:**

```
Failure: White residue on bond pad

EDX results:
Element | Wt%   | Likely Source
--------|-------|---------------
Al      | 65%   | Bond pad
O       | 20%   | Oxide
Cl      | 10%   | Contamination
Na      | 5%    | Contamination

Conclusion: Sodium chloride contamination
Root cause: Flux residue or handling
Action: Improve cleaning, use gloves
```

### Transmission Electron Microscopy (TEM)

**Ultra-High Resolution:**

```
Capabilities:
- Magnification: 50,000× to 50,000,000×
- Resolution: 0.1-0.2 nm (atomic!)
- Imaging: Atomic lattice structure
- Diffraction: Crystal structure
- EDX: Elemental analysis (nm scale)

Sample preparation:
- Must be electron transparent (<100 nm)
- FIB lamella extraction
- Ion milling to final thickness
- Preparation time: 4-8 hours

When to use:
- Atomic-level defects
- Gate oxide analysis
- Grain boundary studies
- Interfacial reactions
- Crystal defects

Cost: $1000-5000 per sample
Time: 1-2 days (prep + analysis)
Availability: Limited (specialized labs)
```

**Applications in MEMS FA:**

```
Examples:

1. Gate oxide breakdown:
   - Defect path visualization
   - Oxide quality assessment
   - Breakdown mechanism

2. Electromigration:
   - Grain structure
   - Void nucleation sites
   - Interface diffusion

3. Solder joint:
   - Intermetallic compounds
   - Grain orientation
   - Crack propagation path

4. Material defects:
   - Dislocations
   - Precipitates
   - Phase boundaries
```

## Root Cause Analysis

### 5-Why Analysis

**Method:**

```
Ask "Why?" repeatedly to find root cause

Example: Wire bond failure

1. Why did the device fail?
   → Wire bond open circuit

2. Why did the wire bond open?
   → Crack at heel of bond

3. Why was there a crack?
   → Excessive stress during temperature cycling

4. Why was stress excessive?
   → Wire loop height too low (75 μm vs 150 μm spec)

5. Why was loop height low?
   → Bonding parameter drift, not caught by monitoring

Root cause: Inadequate process monitoring
Corrective action: Add loop height measurement to SPC
```

### Fishbone Diagram (Ishikawa)

**Categories of Causes:**

```
        Materials        Methods
            \              /
             \            /
              \          /
               \        /
                \      /
                 \    /
        ----------FAILURE----------
                 /    \
                /      \
               /        \
              /          \
             /            \
            /              \
        Machine          Measurement
       (Equipment)       Environment

Example: High leakage current

Materials:
- Contaminated chemicals
- Impure gases
- Defective wafers

Methods:
- Incorrect process recipe
- Operator error
- Poor handling

Machine:
- Equipment malfunction
- Tool out of calibration
- Chamber contamination

Measurement:
- Test equipment drift
- Wrong test conditions
- Probe damage

Environment:
- Temperature variation
- Humidity
- Cleanroom particles
```

### Fault Tree Analysis (FTA)

**Top-Down Approach:**

```
Top event: Device failure

            Device Failure
                  |
         _________|_________
        |                   |
    Electrical          Mechanical
    Failure              Failure
        |                   |
    ____|____           ____|____
   |         |         |         |
Short     Open     Crack    Delamination
   |         |         |         |
  [AND]    [OR]     [OR]      [OR]
   |         |         |         |
 ESD    Wire  Die   Package  Material
      bond  attach   stress
```

**Probability Calculation:**

```
Assign probabilities:
- ESD: 10%
- Wire bond: 5%
- Die attach: 3%
- Package stress: 2%
- Material: 1%

Calculate:
P(Open) = P(Wire) + P(Die) = 5% + 3% = 8%
P(Crack) = P(Package) + P(Material) = 3%
P(Electrical) = P(Short) + P(Open) = 10% + 8% = 18%
P(Failure) = P(Electrical) + P(Mechanical) = 21%

Identify: ESD is highest contributor (10% of 21%)
Action: Focus on ESD protection
```

## Case Studies

### Case Study 1: Accelerometer Offset Drift

**Problem:**

```
Symptom: Zero-g offset increases over time
Onset: After 500 hours at 85°C
Shift: +200 mg (spec: ±50 mg)
Sample: 15% failure rate
```

**FA Approach:**

```
1. Non-destructive (2 hours):
   - Visual: No obvious defects
   - X-ray: No package cracks
   - Electrical: Offset confirmed, other params OK

2. Decapsulation (1 hour):
   - Chemical decap, expose die
   - Visual: No contamination visible

3. SEM Analysis (3 hours):
   - Inspect MEMS structure
   - Finding: Asymmetric residue on proof mass
   - EDX: Residue contains Al, O, C

4. Process Investigation (2 days):
   - Review wafer fab process
   - Finding: Piranha clean step skipped on affected lot
   - Residue: Photoresist not fully removed
```

**Root Cause:**

```
- Process step skipped due to equipment down
- Temporary workaround not documented
- Photoresist residue on MEMS mass
- Residue density changes with temperature
- Causes apparent mass asymmetry → offset shift
```

**Corrective Actions:**

```
Immediate:
- Identify and scrap affected lots
- Re-qualify cleaning process

Short-term:
- Implement process step verification
- Add post-release inspection
- Traveler checklist enhancement

Long-term:
- Equipment redundancy (backup tool)
- Process monitoring (residue detection)
- Traveler system upgrade (electronic)
```

### Case Study 2: Pressure Sensor Package Leak

**Problem:**

```
Symptom: Reading drift after 85/85 THB test
Onset: After 500 hours
Drift: +5% (spec: ±1%)
Sample: 30% failure rate
Impact: Fails automotive qualification
```

**FA Approach:**

```
1. Leak Test (1 hour):
   - Helium fine leak test
   - Result: 5×10⁻⁷ atm·cm³/s (vs 5×10⁻⁹ spec)
   - Conclusion: Package not hermetic

2. X-ray (30 min):
   - No visible cracks
   - Solder seal appears intact

3. Acoustic Microscopy (30 min):
   - Scan seal interface
   - Finding: Delamination in one quadrant
   - Extent: 20% of seal perimeter

4. Cross-Section (4 hours):
   - FIB cross-section through delaminated area
   - SEM imaging at 10,000×
   - Finding: Voids at solder-metal interface
```

**Root Cause:**

```
Analysis showed:
- Oxidation on sealing surface (Kovar frame)
- EDX: Oxide layer 50-100 nm thick
- Solder did not wet properly → voids
- Voids provide leak path

Investigation:
- Pre-seal surface preparation inadequate
- Plasma clean step: Too short (30 sec vs 60 sec)
- Change made to increase throughput
- Not validated for hermeticity
```

**Corrective Actions:**

```
Immediate:
- Revert plasma clean to 60 seconds
- Re-test hermeticity on all lots

Short-term:
- Add 100% helium leak test
- Process validation before changes
- Surface preparation monitoring

Long-term:
- In-line surface monitoring (contact angle)
- Automated leak test (was sampling)
- DOE for optimal clean conditions
```

### Case Study 3: RF MEMS Switch Stiction

**Problem:**

```
Symptom: Switch stuck in closed position
Onset: After 10⁶ cycles (spec: 10⁹ cycles)
Sample: 50% at 10⁶, 90% at 5×10⁶
Environment: Ambient air
Impact: Product reliability failure
```

**FA Approach:**

```
1. Visual Inspection (30 min):
   - Optical microscope: Switch appears down
   - No obvious contamination

2. SEM Analysis (2 hours):
   - Top view: Contact area shows residue
   - High magnification (50,000×)
   - Finding: Organic film 10-20 nm thick

3. EDX Analysis (1 hour):
   - Composition: C, O, trace Si
   - Conclusion: Hydrocarbon contamination

4. Environmental Investigation:
   - Lab environment analysis
   - Finding: Organic vapors from nearby coating process
   - Concentration: 10-50 ppm hydrocarbons in air
```

**Failure Mechanism:**

```
1. Hydrocarbon vapors adsorb on contact
2. Switch cycles accumulate film
3. Film thickness increases with cycles
4. Van der Waals forces increase
5. At critical thickness: Stiction >> restoring force
6. Switch sticks in closed position

Contributing factors:
- No hermetic seal (cost reduction)
- High surface area (many contact points)
- Soft gold contacts (more adhesion)
```

**Corrective Actions:**

```
Immediate:
- Move test area away from coating process
- Install carbon filters on HVAC

Short-term:
- Add getter in package (absorb organics)
- Reduce contact area (design change)
- Hermetic seal option (high-rel version)

Long-term:
- Monitor environment continuously
- Accelerated life test in controlled atmosphere
- Design for robustness (less sensitivity to contamination)
```

## Best Practices

### FA Lab Setup

```
Essential equipment:
- Optical microscope (stereo + metallurgical): $10K-30K
- X-ray system (2D): $50K-150K
- SEM with EDX: $200K-500K
- Decapsulation system: $5K-20K
- Cross-section prep: $10K-30K
- Electrical test equipment: $20K-100K

Total: $300K-800K for basic FA lab

Advanced capabilities:
- FIB-SEM: $1M-2M
- Acoustic microscopy: $100K-300K
- 3D X-ray CT: $200K-800K
- TEM: $2M-5M (usually external)

Access to:
- Chemical analysis (FTIR, XPS, SIMS)
- Material testing (tensile, TMA, DSC)
- Advanced imaging (AFM, STM)
```

### FA Guidelines

```
✓ Document everything (photos, data, observations)
✓ Compare to known good sample
✓ Start non-destructive before destructive
✓ Preserve evidence (multiple samples if possible)
✓ Follow systematic approach (don't jump to conclusions)
✓ Consider multiple failure mechanisms
✓ Verify root cause with additional samples
✓ Implement corrective actions quickly
✓ Track effectiveness of actions
✓ Share learning across organization
```

### Common Mistakes ✗

```
✗ Destroying evidence too quickly
✗ Inadequate documentation
✗ Single sample analysis (statistical insignificance)
✗ Jumping to conclusions without data
✗ Ignoring similar past failures
✗ Not verifying corrective actions
✗ Incomplete root cause analysis
✗ Poor communication of findings
✗ Not following up on actions
✗ Treating symptoms instead of root cause
```

### FA Metrics

```
Track performance:
- Average FA turnaround time
- FA success rate (root cause found)
- Recurrence rate (same failure again)
- Cost per FA
- Customer satisfaction

Targets:
- Critical FA: <24 hours
- Standard FA: <5 days
- Success rate: >90%
- Recurrence: <5%
- Cost: <$2000 per sample (average)
```

## References

1. Microelectronics Failure Analysis Desk Reference (6th ed.). (2011). ASM International.

2. Schafft, H. A., et al. (2004). Building-In reliability: From research to product. *Microelectronics Reliability*, 44(7), 1073-1080.

3. Tummala, R. R., et al. (2009). *Microelectronics Packaging Handbook: Semiconductor Packaging* (3rd ed.). Springer.

4. Ebel, G. H. (2013). *Reliability of Large Area MEMS*. Wiley-VCH.

5. EIA/JEDEC Standard EIA/JESD625. (2006). *Requirements for Handling Electrostatic Discharge Sensitive (ESDS) Devices*.

---

**Document Information:**
- **Created:** December 22, 2025
- **Version:** 1.0
- **Status:** Complete
- **Part of:** Silicon Fabrication Handbook
- **Next Chapter:** [Statistical Process Control](statistical-process-control.md)
- **Previous Chapter:** [Reliability Testing](reliability-testing.md)

**License:** CC BY 4.0 - Free to use with attribution

---

*For questions, corrections, or contributions, please visit:*
https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook