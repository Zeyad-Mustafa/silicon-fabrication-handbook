# Parametric Testing for MEMS

## Table of Contents
- [Introduction](#introduction)
- [Electrical Testing](#electrical-testing)
- [Mechanical Testing](#mechanical-testing)
- [Test Equipment](#test-equipment)
- [Wafer-Level Testing](#wafer-level-testing)
- [Statistical Analysis](#statistical-analysis)
- [References](#references)

## Introduction

Parametric testing validates that MEMS devices meet specifications before packaging. Testing occurs at wafer level (pre-dicing) and package level (post-assembly).

### Test Hierarchy

```
Level 1 - Process Control Monitor (PCM):
- Test structures on scribe lines
- Basic electrical parameters
- Every wafer or lot
- Fast (<5 min per wafer)

Level 2 - Wafer Acceptance Test (WAT):
- Key device parameters
- Sample devices across wafer
- Every wafer
- Moderate time (10-30 min)

Level 3 - Device Characterization:
- Full parametric sweep
- All specifications verified
- Sample wafers per lot
- Slow (1-4 hours per wafer)

Level 4 - Final Test (Package):
- Functional and parametric
- 100% testing or sampling
- After packaging
- Fast to moderate (1-60 sec per device)
```

### Key Metrics

| Parameter | Purpose | Typical Value | Test Method |
|-----------|---------|---------------|-------------|
| Resistance | Contact quality | 10-100 Ω | 4-wire Kelvin |
| Capacitance | Electrode area/gap | 0.1-100 pF | LCR meter, 1 MHz |
| Resonance frequency | MEMS structure | 1 kHz - 10 MHz | Network analyzer |
| Quality factor (Q) | Damping | 10-100,000 | Resonance measurement |
| Sensitivity | Output/input ratio | Device specific | Stimulus + measure |
| Noise | Resolution limit | nV/√Hz to mV/√Hz | Spectrum analyzer |
| Leakage current | Insulation quality | <1 nA to 1 μA | Picoammeter |

## Electrical Testing

### Resistance Measurements

**4-Wire Kelvin Measurement:**

```
Why 4-wire?
- Eliminates probe resistance
- Critical for low resistance (<100 Ω)
- Standard method for contacts, traces

Setup:
    Force+  Sense+
      |       |
      |-------|----DUT----|-------|
                           |       |
                        Sense-  Force-

Current flows through Force terminals
Voltage measured at Sense terminals (no current = no drop in probes)

Measurement:
R = V_sense / I_force

Accuracy: ±0.1% typical
Range: 1 mΩ to 100 MΩ
```

**Test Structures:**

```
Greek Cross (Van der Pauw):
- Measures sheet resistance
- Eliminates contact effects
- 4 pads in cross configuration

R_sheet = (π/ln2) × (V/I) × f
Where f = geometry correction factor

Kelvin Contact:
- Tests contact resistance specifically
- Separate force/sense pads
- Typical: 10-100 Ω for Al contacts
```

**Pass/Fail Criteria:**

| Structure | Parameter | Min | Typical | Max | Units |
|-----------|-----------|-----|---------|-----|-------|
| Metal trace | Resistance | - | 50 mΩ/sq | 80 mΩ/sq | Al, 1 μm |
| Via contact | Resistance | - | 2 Ω | 10 Ω | per via |
| Poly-Si | Sheet resistance | 10 | 20-50 | 100 | Ω/sq |
| Isolation | Resistance | 1 MΩ | >1 GΩ | - | - |

### Capacitance Measurements

**LCR Meter Method:**

```
Typical settings:
- Frequency: 100 kHz to 1 MHz
- Voltage: 0.1-1.0 V AC
- DC bias: 0-50 V (if needed)
- Measurement time: 10-100 ms

For parallel plate capacitor:
C = ε₀ × ε_r × A / d

Measured C vs expected:
- Higher C: Gap smaller than design
- Lower C: Gap larger than design
- Variation: Uniformity across wafer

Example: Pressure sensor
Design: 2 pF (1 mm² area, 2 μm gap)
Measured: 1.8-2.2 pF (±10% acceptable)
Out-of-spec: Investigate gap variation
```

**C-V Characteristics:**

```
Sweep DC bias, measure capacitance:
- Varactor: Voltage-controlled capacitor
- MOS capacitor: Accumulation/depletion/inversion
- MEMS actuator: Pull-in detection

Pull-in voltage detection:
- Apply voltage in steps (0.5-1V increments)
- Monitor capacitance
- Pull-in: Sudden C increase (gap collapse)
- Typical: Occurs at V_pi ± 5%

Example:
Design V_pi: 40V
Measured: 38-42V (acceptable)
          <35V or >45V (fails)
```

### Leakage Current

**Measurement Setup:**

```
Equipment: Picoammeter or SMU (Source-Measure Unit)

Test conditions:
- Apply voltage: 1-100V DC
- Measure current: Range 1 pA to 1 mA
- Integration time: 100 ms to 1 sec
- Guard connections: Minimize leakage

Typical specifications:
- Isolation: <1 nA @ 100V
- ESD diodes: <100 nA @ 5V
- Good dielectric: <10 pA/cm²
```

**Common Failure Modes:**

| Symptom | Cause | Action |
|---------|-------|--------|
| High leakage (>1 μA) | Short or pinhole | Reject |
| Medium leakage (100-1000 nA) | Marginal insulation | Investigate |
| Variable leakage | Contamination | Clean, re-test |
| Time-dependent | Charging effects | Extend settling time |

## Mechanical Testing

### Resonance Frequency

**Measurement Methods:**

```
1. Electrical Actuation + Detection:
   - Apply AC voltage (sweep frequency)
   - Measure current or capacitance
   - Peak indicates resonance
   - Works for capacitive structures

2. Laser Doppler Vibrometry (LDV):
   - Laser measures displacement
   - Non-contact, high accuracy
   - Resolution: 0.1 nm
   - Best for characterization

3. Network Analyzer:
   - S-parameter measurement
   - For RF MEMS
   - Phase/amplitude vs frequency
```

**Typical Test:**

```
Frequency sweep:
- Start: f₀ × 0.5
- Stop: f₀ × 1.5
- Points: 100-1000
- Actuation: 0.1-1.0V AC

Analysis:
- f₀: Resonance frequency (Hz)
- Q: Quality factor (dimensionless)
- Bandwidth: BW = f₀/Q

Example: MEMS resonator
Design: f₀ = 10 MHz, Q = 10,000
Measured: f₀ = 9.95-10.05 MHz (±0.5%)
          Q = 8,000-12,000
```

**Quality Factor (Q) Measurement:**

```
Q = f₀ / Δf_3dB

Where:
f₀ = resonance frequency
Δf_3dB = bandwidth at -3dB points

Or from ring-down:
Q = π × f₀ × τ

Where:
τ = decay time constant

High Q indicates:
- Low damping (vacuum package)
- High frequency stability
- Better sensor resolution

Low Q indicates:
- High damping (air, squeeze film)
- Package leak
- Anchor losses
```

### Sensitivity Testing

**Accelerometer Example:**

```
Test setup:
- Mount on shaker table
- Apply known acceleration
- Measure output voltage

Stimulus:
- Frequency: 10 Hz to 10 kHz
- Amplitude: 0.1g to 10g
- Sweep or discrete points

Measurement:
Sensitivity = ΔV_out / Δa_in (mV/g)

Example:
Input: 1.000g @ 100 Hz
Output: 50.0 mV
Sensitivity: 50 mV/g

Spec: 45-55 mV/g
Result: Pass
```

**Pressure Sensor:**

```
Test setup:
- Pneumatic or hydraulic pressure source
- Calibrated reference sensor
- Apply known pressure

Stimulus:
- Range: 0 to P_max
- Steps: 10-20 points
- Include zero pressure

Measurement:
Sensitivity = ΔV_out / ΔP_in (mV/kPa)

Linearity:
Non-linearity = (Max deviation / Full scale) × 100%

Typical spec: <0.5% FSO (Full Scale Output)
```

**Gyroscope:**

```
Test setup:
- Rate table (rotation platform)
- Apply known angular rate
- Measure output

Challenge:
- Requires expensive equipment ($50K-500K)
- Rate table accuracy critical
- Temperature stabilization needed

Sensitivity: mV/(°/s)
Bias stability: °/hr
Angular random walk: °/√hr

Often tested at package level, not wafer level
```

### Mechanical Pull/Shear Tests

**Wire Bond Pull Test:**

```
Method:
- Hook tool under wire at mid-span
- Pull vertically until failure
- Record break force and mode

Acceptance:
- Force: >8 gf for 25 μm Au wire
- Mode: Wire break (preferred)
        Bond interface (acceptable if >min force)
        Cratering (reject)

Sample size: 3-10 bonds per unit
Frequency: Per lot or sample basis
```

**Die Shear Test:**

```
Method:
- Shear tool at die edge
- Push horizontally
- Record force at detachment

Acceptance:
- Force: >5 MPa (or >10 kgf for 5×5 mm die)
- Mode: Cohesive failure in adhesive (good)
        Die fracture (excellent bond but fragile)

Sample: 1-3 units per lot
Destructive: Cannot ship tested units
```

## Test Equipment

### Probe Station

**Key Components:**

```
1. Chuck:
   - Holds wafer (vacuum)
   - Temperature control: -60 to +300°C
   - Positioning: X-Y stage (μm accuracy)

2. Probes:
   - Tungsten or BeCu needles
   - Pitch: 50-150 μm typical
   - Fine pitch: 30-50 μm
   - Configuration: 2-4+ probes

3. Microscope:
   - Magnification: 5-100×
   - Camera for documentation
   - Pattern recognition (auto-align)

4. Instruments:
   - Connected via cables
   - GPIB, USB, or Ethernet
   - Automated test software

Cost: $20K (manual) to $500K+ (automated)
```

**Probe Types:**

| Type | Use | Pitch | Force | Notes |
|------|-----|-------|-------|-------|
| Needle probe | DC measurements | >50 μm | 1-5 gf | Standard |
| Cantilever | High frequency | >75 μm | 2-10 gf | Low inductance |
| Membrane probe | Very fine pitch | 30-50 μm | 0.5-2 gf | Expensive |
| MEMS probe | Ultra-fine | <30 μm | <1 gf | Advanced |

**Probing Damage:**

```
Concerns:
- Pad surface damage (scratches)
- Pad metal removal (probe wear)
- Contamination (probe residue)

Mitigation:
- Proper probe force (<5 gf typical)
- Regular probe cleaning
- Controlled overtravel (10-20 μm)
- Soft metal pads (Al better than Cu)
- Passivation opening sufficient size
```

### Parameter Analyzers

**SMU (Source-Measure Unit):**

```
Capabilities:
- Source voltage: ±200V typical
- Measure current: 100 fA to 1A
- Or source current, measure voltage
- 4-wire measurements

Applications:
- I-V curves
- Leakage current
- Breakdown voltage
- Contact resistance

Models:
- Keithley 2400 series
- Keysight B2900 series
- Tektronix 2600 series

Cost: $3K-15K per channel
```

**LCR Meter:**

```
Measures:
- Capacitance (C)
- Inductance (L)
- Resistance (R)
- At AC frequencies

Frequency range: 20 Hz to 110 MHz
Accuracy: 0.05-0.1%
Measurement speed: 10-100 ms

Models:
- Keysight E4980A (standard)
- Wayne Kerr 6500B
- Hioki IM3570

Cost: $5K-30K
```

**Network Analyzer:**

```
For RF measurements:
- S-parameters (S11, S21)
- Impedance
- Resonance

Frequency: 9 kHz to 50 GHz
Dynamic range: >100 dB

Applications:
- RF MEMS switches
- Resonators
- Filters

Cost: $30K-200K
```

## Wafer-Level Testing

### Wafer Mapping

**Purpose:**
```
1. Identify good vs bad die
2. Spatial pattern analysis
3. Process feedback
4. Known good die (KGD) for packaging

Bin categories:
Bin 1: Pass all tests (ship)
Bin 2: Pass with margin (ship)
Bin 3: Marginal (investigate)
Bin 4: Fail electrical
Bin 5: Fail mechanical
Bin X: Untested (edge exclusion)
```

**Typical Wafer Map:**

```
Color coding:
- Green: Pass (80-95% typical)
- Yellow: Marginal (0-5%)
- Red: Fail (5-15%)
- Gray: Edge exclusion (2-5%)

Patterns indicate:
- Center hot spot: Thermal issue
- Edge roll-off: Deposition/etch uniformity
- Cluster failures: Particle, defect
- Random: Yield loss mechanisms
- Quadrant: Equipment asymmetry
```

### Test Time Optimization

**Test Sequence Design:**

```
Priority order:
1. Continuity/shorts (fast, eliminates gross failures)
2. Critical parameters (key specs)
3. Full parametric (complete characterization)

Parallel testing:
- Test multiple sites simultaneously
- 4-16 sites common
- Reduces test time by factor of N

Adaptive testing:
- If fail basic test, skip detailed tests
- Focus time on good die
- Can save 30-50% test time
```

**Test Time Breakdown:**

```
Example: MEMS accelerometer wafer

Step                    | Time/die | Cumulative
------------------------|----------|------------
Probe touchdown         | 0.5 s    | 0.5 s
Contact resistance      | 0.2 s    | 0.7 s
Supply current          | 0.3 s    | 1.0 s
Offset voltage          | 0.5 s    | 1.5 s
Sensitivity (3 points)  | 1.5 s    | 3.0 s
Noise                   | 2.0 s    | 5.0 s
Frequency response      | 5.0 s    | 10.0 s
------------------------|----------|------------
Total per die: 10 seconds

300mm wafer: 500 die
Sequential: 5000 seconds (83 min)
8-site parallel: 625 seconds (10 min)

Throughput: 6 wafers/hour (parallel)
```

### Automated Test Equipment (ATE)

**Capabilities:**

```
Hardware:
- Multi-channel instruments
- Switching matrix (connect to probes)
- Temperature control
- Pattern recognition

Software:
- Test program (define sequence)
- Data logging (results database)
- Wafer mapping (visualization)
- Statistical analysis (SPC)
- Recipe management

Cost: $200K-2M depending on capability
```

**Probe Card:**

```
Custom interface for specific die:
- Needle arrangement matches pads
- 10-200 probes typical
- Pitch: 50-150 μm standard
- Material: Tungsten, BeCu, MEMS

Cost: $5K-50K per card
Lifetime: 50K-500K touchdowns

Maintenance:
- Cleaning: Every 1000-5000 touchdowns
- Needle replacement: As needed
- Planarization: Critical for yield
```

## Statistical Analysis

### Process Control Monitoring

**Control Charts (SPC):**

```
X-bar chart (average):
- Center line: Target value
- UCL/LCL: ±3σ (control limits)
- Warning: ±2σ

R chart (range):
- Monitors variation
- Complements X-bar chart

Rules for out-of-control:
1. Point beyond control limits
2. 7+ consecutive points above/below center
3. 7+ points trending up/down
4. 2/3 points in outer third (zone A)
```

**Cpk (Process Capability):**

```
Cpk = min[(USL - μ)/(3σ), (μ - LSL)/(3σ)]

Where:
USL = Upper specification limit
LSL = Lower specification limit
μ = Process mean
σ = Process standard deviation

Interpretation:
Cpk > 1.67: Excellent (6σ process)
Cpk > 1.33: Good (4σ process)
Cpk > 1.00: Acceptable (3σ process)
Cpk < 1.00: Poor, process not capable

Example:
Sensitivity: Spec 45-55 mV/g
Mean: 50.0 mV/g
Std dev: 1.5 mV/g

Cpk = min[(55-50)/(3×1.5), (50-45)/(3×1.5)]
    = min[1.11, 1.11]
    = 1.11 (Acceptable but should improve)
```

### Correlation Analysis

**Parameter Correlation:**

```
Identifies relationships:
- Sensitivity vs temperature
- Frequency vs pressure
- Resistance vs location

Correlation coefficient (r):
-1: Perfect negative correlation
 0: No correlation
+1: Perfect positive correlation

|r| > 0.8: Strong correlation
|r| = 0.5-0.8: Moderate
|r| < 0.5: Weak

Use to:
- Find root cause of variation
- Optimize test sequence
- Reduce redundant tests
```

### Outlier Detection

**Methods:**

```
1. 3-sigma rule:
   Outlier if |x - μ| > 3σ
   Eliminates ~0.3% of data

2. Grubbs' test:
   Statistical test for single outlier
   More rigorous than 3-sigma

3. Box plot:
   Visual identification
   Points beyond 1.5×IQR from quartiles

Action on outliers:
- Investigate cause (defect, test error?)
- Re-test if suspected measurement issue
- Exclude from statistics if confirmed anomaly
- Track frequency (too many = process issue)
```

## Test Data Management

### Database Structure

```
Wafer level:
- Wafer ID
- Lot ID
- Process recipe
- Test date/time
- Equipment used

Die level:
- Wafer ID + X,Y coordinates
- Bin assignment
- All parameter values
- Pass/fail flags

Uses:
- Yield analysis
- Trend monitoring
- Customer traceability
- Failure analysis
```

### Yield Analysis

**Yield Calculation:**

```
Die yield = (Good die / Total tested die) × 100%

Wafer yield = (Good die / Gross die) × 100%
(includes edge exclusion)

Cumulative yield:
Y_total = Y_fab × Y_test × Y_assembly × Y_final

Example:
Fab yield: 90%
Test yield: 95%
Assembly: 98%
Final test: 99%

Total: 0.90 × 0.95 × 0.98 × 0.99 = 83.3%

From 1000 wafers → 833 shipped
```

**Yield Pareto:**

```
Identify top failure modes:

Failure Mode          | Count | % | Cumulative %
---------------------|-------|---|-------------
Sensitivity out-of-spec | 45  | 45% | 45%
High leakage current    | 25  | 25% | 70%
Resonance frequency     | 15  | 15% | 85%
Open circuit            | 10  | 10% | 95%
Other                   | 5   | 5%  | 100%

Focus on top 2-3 (80/20 rule)
Address these first for max yield improvement
```

## Best Practices

### Test Development

```
✓ Define specifications clearly (min/max/typical)
✓ Develop test plan early (not after fab!)
✓ Include guard bands (margin between test limit and spec)
✓ Validate test repeatability (R&R study)
✓ Correlate wafer to package test
✓ Automate data collection
✓ Implement statistical monitoring (SPC)
✓ Regular calibration of equipment
✓ Document test procedures
✓ Train operators thoroughly
```

### Cost Optimization

```
Test cost drivers:
1. Equipment capital ($200K-2M)
2. Test time (throughput)
3. Consumables (probe cards, $5K-50K)
4. Labor

Reduction strategies:
- Parallel testing (test multiple sites)
- Adaptive test (skip tests on fails)
- Optimize sequence (fast tests first)
- Multisite probe cards
- Automation (reduce labor)

Target: Test cost <10% of device ASP
```

### Common Pitfalls ✗

```
✗ Testing without guard bands (escapes to customer)
✗ No correlation study (wafer vs package)
✗ Inadequate probe maintenance (false failures)
✗ Insufficient test time (miss marginal parts)
✗ No SPC monitoring (process drift undetected)
✗ Poor probe contact (intermittent measurements)
✗ Wrong test conditions (voltage, frequency)
✗ Ignoring outliers (miss systematic issues)
✗ No calibration schedule (drift over time)
✗ Inadequate data retention (cannot trace issues)
```

## References

1. Semiconductor Equipment and Materials International (SEMI). (2020). *Test Methods Standards*.

2. McCluskey, P., & Hakim, R. (2013). *Reliability of MEMS: Testing of Materials and Devices*. SPIE Press.

3. Tanner, D. M., et al. (2000). MEMS reliability in shock environments. *IEEE International Reliability Physics Symposium*, 129-138.

4. MIL-STD-883. (2016). *Test Method Standard: Microcircuits*. Department of Defense.

5. Sharpe, W. N., et al. (2003). Measurements of Young's modulus, Poisson's ratio, and tensile strength of polysilicon. *IEEE MEMS Conference*, 424-429.

---

**Document Information:**
- **Created:** December 19, 2025
- **Version:** 1.0
- **Status:** Complete
- **Part of:** Silicon Fabrication Handbook
- **Next Chapter:** [Functional Testing](functional-testing.md)
- **Section:** Testing & Yield

**License:** CC BY 4.0 - Free to use with attribution

---

*For questions, corrections, or contributions, please visit:*
https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook