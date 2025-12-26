# Reliability Testing for MEMS

## Table of Contents
- [Introduction](#introduction)
- [Environmental Testing](#environmental-testing)
- [Mechanical Reliability](#mechanical-reliability)
- [Electrical Reliability](#electrical-reliability)
- [Accelerated Testing](#accelerated-testing)
- [Lifetime Prediction](#lifetime-prediction)
- [References](#references)

## Introduction

Reliability testing validates that MEMS devices operate correctly over their intended lifetime under specified environmental conditions. Testing identifies failure mechanisms and predicts field performance.

### Reliability Metrics

**Key Definitions:**

```
MTTF (Mean Time To Failure):
- Average time until first failure
- Units: Hours, years
- For non-repairable devices

MTBF (Mean Time Between Failures):
- Average time between failures
- For repairable systems
- MTTF = MTBF for first failure

FIT (Failures In Time):
- Number of failures per 10⁹ device-hours
- FIT = 10⁹ / MTTF
- Common in automotive/aerospace

Example:
MTTF = 100,000 hours
FIT = 10⁹ / 100,000 = 10,000 FIT
```

**Reliability Goals by Application:**

| Application | MTTF Target | FIT Rate | Failure Rate |
|-------------|-------------|----------|--------------|
| Consumer | 50K hours (5.7 years) | 20,000 | 2% per year |
| Industrial | 100K hours (11.4 years) | 10,000 | 1% per year |
| Automotive | 200K hours (22.8 years) | 5,000 | 0.5% per year |
| Aerospace | 500K hours (57 years) | 2,000 | 0.2% per year |
| Medical implant | 1M hours (114 years) | 1,000 | 0.1% per year |

### Test Standards

**Common Standards:**

```
MIL-STD-883: Military semiconductor test methods
JEDEC JESD22: Reliability test methods for ICs
AEC-Q100/Q200: Automotive qualification
ISO 16750: Road vehicles environmental conditions
IEC 60068: Environmental testing
```

## Environmental Testing

### Temperature Cycling

**Purpose:** Detect failures due to CTE mismatch, material fatigue

**Test Conditions:**

```
Condition A (Military):
- Temperature: -65°C to +150°C
- Dwell: 15 min each extreme
- Ramp: <1 min
- Cycles: 500-1000

Condition B (Commercial):
- Temperature: -55°C to +125°C
- Dwell: 15 min each extreme
- Ramp: <1 min
- Cycles: 500-1000

Condition C (Automotive - AEC-Q100):
- Temperature: -40°C to +150°C
- Dwell: 10 min each extreme
- Ramp: 10-20°C/min
- Cycles: 1000

Condition D (Extended):
- Temperature: -40°C to +85°C
- Dwell: 30 min each extreme
- Cycles: 200 minimum
```

**Failure Mechanisms:**

| Mechanism | Symptom | Typical Onset |
|-----------|---------|---------------|
| Solder joint fatigue | Electrical open/intermittent | 100-500 cycles |
| Wire bond heel crack | Open circuit | 200-1000 cycles |
| Die attach delamination | Thermal resistance increase | 300-1000 cycles |
| Package cracking | Hermeticity loss | 500-2000 cycles |
| Metallization stress | Resistance increase | Variable |

**Monitoring:**

```
Electrical:
- Continuity check (every 100 cycles)
- Resistance measurement
- Functional test (every 200 cycles)

Physical:
- X-ray inspection (before/after)
- Acoustic microscopy (delamination)
- Visual inspection (cracks)

Failure criteria:
- >20% parameter shift
- Intermittent opens (>1 ms)
- Complete functional failure
```

**Example Data:**

```
Sample size: 77 units (JEDEC)
Test: -40°C to 125°C, 1000 cycles

Results:
Cycles | Failures | Cumulative %
-------|----------|-------------
0-200  | 0        | 0%
200-400| 1        | 1.3%
400-600| 2        | 3.9%
600-800| 3        | 7.8%
800-1000| 4       | 13%

Characteristic life (Weibull): 850 cycles
β (shape): 2.1 (wear-out)
```

### High Temperature Operating Life (HTOL)

**Purpose:** Accelerated aging at elevated temperature

**Test Conditions:**

```
Standard (JEDEC JESD22-A108):
- Temperature: 125°C
- Duration: 1000 hours
- Voltage: Nominal or slightly elevated (1.1×)
- Sample size: 77 units minimum

Extended (Automotive):
- Temperature: 150°C
- Duration: 1000-2000 hours
- Voltage: Maximum rated
- Sample size: 231 units

High Temp Storage (no power):
- Temperature: 150-175°C
- Duration: 1000 hours
- Sample size: 77 units
```

**Acceleration Factor:**

```
Arrhenius equation:
AF = exp[(Ea/k) × (1/T_use - 1/T_test)]

Where:
Ea = activation energy (eV)
k = Boltzmann constant (8.617×10⁻⁵ eV/K)
T = absolute temperature (K)

Example:
Ea = 0.7 eV (typical for wear-out)
T_use = 85°C = 358K
T_test = 125°C = 398K

AF = exp[(0.7/8.617×10⁻⁵) × (1/358 - 1/398)]
AF = exp[8124 × 0.000280]
AF = exp[2.27]
AF = 9.7

Result: 1000 hours at 125°C ≈ 9700 hours at 85°C
```

**Failure Mechanisms:**

```
Time-dependent:
- Electromigration (metal migration)
- Stress migration
- Dielectric breakdown (TDDB)
- Intermetallic growth
- Corrosion (if moisture present)
- Diffusion effects

Monitoring: Every 168 hours (weekly)
- Functional test
- Parametric measurements
- Leakage current
```

### Temperature Humidity Bias (THB)

**Purpose:** Detect moisture-related failures

**Test Conditions:**

```
85/85 THB (JEDEC JESD22-A101):
- Temperature: 85°C
- Humidity: 85% RH
- Bias voltage: Applied (3.3V, 5V typical)
- Duration: 1000 hours
- Sample size: 77 units

HAST (Highly Accelerated Stress Test):
- Temperature: 110-130°C
- Humidity: 85% RH
- Pressure: 2 atm (accelerates)
- Bias voltage: Applied
- Duration: 96-264 hours
- Sample size: 77 units

Unbiased (storage):
- 85°C / 85% RH
- No voltage applied
- Duration: 1000 hours
```

**Failure Mechanisms:**

```
Corrosion:
- Aluminum metallization most susceptible
- Galvanic corrosion (dissimilar metals)
- Bond pad corrosion

Electrochemical migration:
- Dendrite growth between conductors
- Requires bias voltage + moisture
- Time to failure: 100-1000 hours

Package degradation:
- Delamination
- Wire bond corrosion
- Lead frame oxidation
```

**Acceleration Factor:**

```
Peck's equation:
AF = (RH_test/RH_use)^n × exp[(Ea/k) × (1/T_use - 1/T_test)]

Typical values:
n = 2.7-3.0 (humidity exponent)
Ea = 0.8-0.9 eV

Example:
RH_use = 60%, T_use = 40°C
RH_test = 85%, T_test = 85°C
n = 2.7, Ea = 0.8 eV

AF ≈ 150-200×

Result: 1000 hours THB ≈ 20+ years field use
```

### Thermal Shock

**Purpose:** Maximum thermal stress, rapid temperature transitions

**Test Conditions:**

```
MIL-STD-883 Method 1011:
Condition A:
- Cold: -65°C (liquid bath)
- Hot: +150°C (liquid bath)
- Transfer: <10 seconds
- Dwell: 5 min minimum
- Cycles: 15 minimum

Condition B:
- Cold: -55°C to -65°C
- Hot: +125°C to +150°C
- Transfer: <1 minute
- Dwell: 15 min
- Cycles: 100-200

2-Chamber Air-to-Air:
- Cold: -40°C (air)
- Hot: +125°C (air)
- Transfer: 10-30 seconds
- Dwell: 10-30 min
- Cycles: 200-500
```

**More Severe than Temperature Cycling:**
- Faster transitions (higher stress)
- Liquid baths provide faster heat transfer
- Detects weak interfaces quickly

**Typical Failures:**
- Die cracking
- Package cracking
- Wire bond failure (heel or ball)
- Delamination (sudden vs gradual)

## Mechanical Reliability

### Vibration Testing

**Purpose:** Simulate transportation, operation vibration

**Test Types:**

```
1. Sinusoidal Vibration (JESD22-B103):
   - Frequency: 10-2000 Hz
   - Amplitude: 1.5 mm (10-55 Hz)
              : 20g (55-2000 Hz)
   - Sweep rate: 1 octave/min
   - Duration: 12 cycles (4 per axis)

2. Random Vibration:
   - Power spectral density (PSD)
   - Frequency: 20-2000 Hz
   - Level: 0.04 g²/Hz (typical)
   - Duration: 1-2 hours per axis

3. Mechanical Shock:
   - Half-sine pulse: 1500g, 0.5 ms
   - Or: 500g, 1 ms
   - 3 shocks per direction
   - 6 directions (±X, ±Y, ±Z)
```

**Failure Modes:**

| Component | Failure | Typical G-level |
|-----------|---------|-----------------|
| Wire bonds | Flexure fatigue | >50g (cycling) |
| Die attach | Shear failure | >1000g (shock) |
| Solder joints | Fatigue | >20g (vibration) |
| MEMS structure | Fracture | >1000g (shock) |
| Package | Cracking | >2000g (shock) |

**MEMS-Specific Concerns:**

```
Resonance amplification:
- MEMS structure may have resonance 1-100 kHz
- If vibration excites resonance → high Q → large amplitude
- Can cause:
  * Self-contact (stiction)
  * Structure fracture
  * Anchor failure

Design mitigation:
- Damping (lower Q)
- Stops (limit displacement)
- Out-of-band resonance
```

### Drop Test

**Purpose:** Simulate product drops (smartphones, devices)

**Test Standards:**

```
JEDEC JESD22-B111 (Board Level Drop):
- Height: 1.5 m
- Surface: Hard (steel/concrete)
- Orientation: 6 surfaces, 8 corners, 12 edges
- Drops: 3-5 per orientation
- Pass: No functional failure, no cracks

JEDEC JESD22-B110 (Mechanical Shock):
- 1500g half-sine, 0.5 ms
- Or 2900g half-sine, 0.3 ms
- Package-level test

MIL-STD-883 Method 2002:
- Condition A: 1500g, 0.5 ms
- Condition B: 3000g, 0.2 ms
- 5 shocks per axis
```

**Board-Level Drop:**

```
Setup:
- PCB: 132 × 77 mm (standard test board)
- Support: 4 screws at corners
- Component locations: Defined

Impact orientation:
- Corner impact (most severe)
- Edge impact
- Flat impact

Typical performance:
- Wire bond package: 10-30 drops
- Flip chip (no underfill): 5-15 drops
- Flip chip (underfill): 50-150 drops
- WLCSP (underfill): 50-100 drops
```

**High-Speed Camera Analysis:**

```
Capture during drop:
- Frame rate: 10,000-100,000 fps
- Observe:
  * PCB bending
  * Component displacement
  * Crack initiation/propagation

Strain gauge data:
- Measure strain at component location
- Typical: 1000-3000 με (micro-strain)
- Correlate to solder joint stress
```

### Constant Acceleration

**Purpose:** High-G continuous load

**Applications:**
- Centrifuge testing
- Missile/artillery applications
- Crash scenarios

**Test Conditions:**

```
MIL-STD-883 Method 2001:
- 20,000g to 100,000g
- Duration: 1 minute
- Radial or axial orientation

Commercial:
- 1,000g to 5,000g
- Duration: 1-30 minutes

Failure modes:
- Wire bond fracture
- Die cracking
- Solder joint failure
- Package deformation
```

## Electrical Reliability

### Electrostatic Discharge (ESD)

**Purpose:** Protect against static electricity damage

**Test Models:**

```
1. Human Body Model (HBM) - JEDEC JESD22-A114:
   - Capacitance: 100 pF
   - Resistance: 1500 Ω
   - Voltage: ±250V to ±8000V
   - Classification:
     * Class 0: <250V (fail)
     * Class 1A: 250-500V
     * Class 1B: 500-1000V
     * Class 2: 1000-2000V (typical target)
     * Class 3: 2000-4000V
     * Class 4: >4000V

2. Charged Device Model (CDM) - JEDEC JESD22-C101:
   - Direct discharge from charged device
   - Voltage: ±125V to ±2000V
   - Classification:
     * Class C1: <125V
     * Class C2: 125-250V (typical target)
     * Class C3: 250-500V
     * Class C4: 500-1000V
     * Class C5: >1000V

3. Machine Model (MM):
   - Capacitance: 200 pF
   - Resistance: 0 Ω (direct discharge)
   - Voltage: ±100V to ±400V
   - Less common now
```

**Testing Procedure:**

```
1. Pre-test measurement:
   - All pins characterized
   - Record baseline parameters

2. ESD stress:
   - Apply to each pin
   - Positive and negative polarity
   - 3 zaps per pin per polarity
   - Incrementing voltage levels

3. Post-test measurement:
   - Compare to baseline
   - Check functionality

Failure criteria:
- >20% parameter shift
- Functional failure
- Visible damage (SEM)

Sample size: 3 units minimum per condition
```

**Failure Mechanisms:**

```
Gate oxide breakdown:
- Thin oxide (<10 nm) most vulnerable
- Breakdown voltage: 8-12 MV/cm
- Failure: Permanent short or high leakage

Junction damage:
- PN junction reverse breakdown
- Localized melting
- Increased leakage current

Metallization damage:
- Fusing (open circuit)
- Melting/vaporization
- Typical: Narrow metal lines
```

### Electrical Overstress (EOS)

**Purpose:** Test robustness against overvoltage/overcurrent

**Test Conditions:**

```
Overvoltage:
- Apply 1.5× to 2× rated voltage
- Duration: 1-100 ms
- Monitor for damage

Overcurrent:
- Apply 2× to 10× rated current
- Duration: 100 ms to 1 sec
- Check for metallization failure

Latch-up (CMOS devices):
- Force current into output pin
- Trigger parasitic thyristor
- Check if device recovers
- Spec: No latch-up at 125°C, 1.1× Vdd
```

**Typical Robustness:**

| Device Type | Overvoltage Tolerance | Overcurrent |
|-------------|----------------------|-------------|
| CMOS logic | 1.3× Vdd | 2-5× nominal |
| Power devices | 1.5-2× rated | 10-20× for 1ms |
| MEMS sensors | 2-3× supply | Limited by bondwires |
| RF devices | 1.5× Vdd | 5-10× |

## Accelerated Testing

### Burn-In

**Purpose:** Screen early failures (infant mortality)

**Process:**

```
Dynamic Burn-In (preferred):
- Temperature: 125-150°C
- Voltage: 1.1-1.3× nominal
- Activity: Functional patterns running
- Duration: 48-168 hours
- Sample: 100% (high-rel) or sampling (consumer)

Static Burn-In:
- Temperature: 125-150°C
- Voltage: Maximum rated
- No functional activity
- Duration: 48-168 hours
- Lower cost but less effective

Typical screen-out: 0.1-1% of devices fail
```

**Bathtub Curve:**

```
Failure Rate vs Time:

    |         Infant       Useful Life    Wear-out
    |       Mortality      (Random)        Phase
    |           ___________________________
    |          /                           \___
    |    _____/                                \___
    |____|__________________________________|______|___
         0    1000hr    10,000hr      100,000hr    Time

Burn-in removes infant mortality failures
Target: Reach useful life phase before shipping
```

**Cost-Benefit:**

```
Example:
- Field failure cost: $50 per failure
- Burn-in cost: $2 per device
- Screen rate: 0.5% (5000 ppm)

For 1M devices:
- Burn-in cost: 1M × $2 = $2M
- Field failures prevented: 1M × 0.005 = 5000
- Savings: 5000 × $50 = $250K

Decision: Burn-in not cost-effective for consumer
         Burn-in justified for automotive/medical
```

### Accelerated Life Testing (ALT)

**Purpose:** Predict lifetime under normal conditions

**Common Stresses:**

```
1. Temperature (Arrhenius)
2. Voltage (Power law or exponential)
3. Humidity (Peck's equation)
4. Mechanical cycling
5. Combined stress

Multiple stress levels:
- Typical: 3-4 stress levels
- Sample size: 30-77 per level
- Duration: Until sufficient failures (≥10)
```

**Example ALT Design:**

```
Device: MEMS accelerometer
Use condition: 40°C, 5V, 5 years

Test matrix:
Level | Temp | Voltage | Sample | Duration
------|------|---------|--------|----------
1     | 85°C | 6.0V    | 77     | 2000 hrs
2     | 100°C| 6.5V    | 77     | 1000 hrs
3     | 125°C| 7.0V    | 77     | 500 hrs

Analysis:
- Fit Weibull distribution to failures
- Calculate acceleration factors
- Extrapolate to use conditions
- Estimate MTTF with confidence bounds
```

## Lifetime Prediction

### Weibull Analysis

**Weibull Distribution:**

```
Cumulative failure:
F(t) = 1 - exp[-(t/η)^β]

Where:
η = characteristic life (63.2% failure point)
β = shape parameter
  β < 1: Infant mortality
  β = 1: Random failures (exponential)
  β > 1: Wear-out

Reliability:
R(t) = exp[-(t/η)^β]

MTTF = η × Γ(1 + 1/β)
Where Γ is gamma function
```

**Plotting:**

```
Linearized form:
ln[-ln(1-F)] = β × ln(t) - β × ln(η)

Plot: ln[-ln(1-F)] vs ln(t)
Slope = β (shape parameter)
Intercept determines η

Example data (temperature cycling):
Cycles | Failed | Cumulative F(%)
-------|--------|----------------
200    | 0      | 0%
400    | 1      | 1.3%
600    | 3      | 5.2%
800    | 7      | 14.3%
1000   | 12     | 29.9%

Result from plot:
β = 2.8 (wear-out mechanism)
η = 950 cycles

Prediction:
F(1000) = 1 - exp[-(1000/950)^2.8] = 32%
(close to observed 30%)
```

### Physics of Failure

**Mechanistic Models:**

```
1. Coffin-Manson (Thermal Cycling):
   N_f = C × (ΔT)^(-n)
   
   Where:
   N_f = cycles to failure
   ΔT = temperature range
   n = 2-3 typical
   C = material constant

2. Black's Equation (Electromigration):
   MTTF = A × j^(-n) × exp(Ea/kT)
   
   Where:
   j = current density (A/cm²)
   n = 1-2 (typically 2)
   Ea = 0.5-1.0 eV

3. Eyring Model (Multi-stress):
   MTTF = A × exp(B/T) × V^(-n) × S^(-m)
   
   Combines temperature, voltage, other stresses
```

**Example Calculation:**

```
Solder joint thermal cycling:

Test conditions:
ΔT_test = 165°C
N_test = 500 cycles (10% failure)

Use conditions:
ΔT_use = 100°C

Coffin-Manson with n=2:
N_use = N_test × (ΔT_test/ΔT_use)^n
N_use = 500 × (165/100)^2
N_use = 500 × 2.72
N_use = 1360 cycles

Annual cycles in field:
- Daily: 1 cycle (-20°C to 80°C)
- Annual: 365 cycles

Predicted life: 1360/365 = 3.7 years to 10% failure
                13,600/365 = 37 years to 63% failure (η)
```

### Confidence Intervals

**Small Sample Statistics:**

```
For reliability predictions with limited failures:

Chi-squared method:
Lower bound: χ²(2r, 1-CL/2) / (2T)
Upper bound: χ²(2r+2, CL/2) / (2T)

Where:
r = number of failures
T = total test time (all samples)
CL = confidence level (e.g., 0.9 for 90%)

Example:
77 samples, 1000 hours each
10 failures observed
Confidence level: 90%

Total time: 77 × 1000 = 77,000 hours

χ²(20, 0.05) = 10.85 (from tables)
χ²(22, 0.95) = 33.92

MTTF_lower = 77,000 / (33.92/2) = 4,540 hours
MTTF_upper = 77,000 / (10.85/2) = 14,200 hours

90% confidence: MTTF = 7,700 hours (4,540-14,200)
FIT = 130,000 (70,400-220,200)
```

## Quality Standards

### Automotive (AEC-Q100)

**Key Requirements:**

```
Group A - Accelerated Environmental:
- Temperature cycling: 1000 cycles
- HTOL: 1000 hours at 150°C
- Temperature/humidity/bias: 1000 hours
- Power temperature cycling: 1000 cycles
- Autoclave: 96 hours at 121°C, 100% RH
- Highly accelerated stress test: 96 hours

Group B - Lifetime:
- Early life failure rate: 1000 hours at 125°C
- Operating life: 1000 hours at 125°C

Group C - Package Assembly:
- Wire bond shear/pull
- Die shear
- Solderability
- Physical dimensions

Group D - Die Fabrication:
- ESD protection (HBM: ≥2 kV)
- Latch-up immunity
- Electrical parametric

Sample sizes: 77 or 231 units typical
Pass criteria: 0 failures or per reliability target
```

### Medical (ISO 13485)

**Requirements:**

```
Device Classification:
- Class I: Low risk (general controls)
- Class II: Moderate risk (special controls)
- Class III: High risk (pre-market approval)

Reliability testing:
- Lifetime: 10+ years typical
- Sterilization compatibility
- Biocompatibility (ISO 10993)
- Packaging integrity
- Shelf life validation

Documentation:
- Design history file (DHF)
- Device master record (DMR)
- Risk management (ISO 14971)
- Traceability (all units)
```

### Aerospace (MIL-PRF-38534)

**Class Requirements:**

```
Class H (Hermetic, High Reliability):
- 100% screening (burn-in, etc.)
- Group A, B, C, D testing
- QPL (Qualified Products List)

Class K (Similar to H):
- Alternative to Class H
- Slightly relaxed requirements

Quality Conformance Inspection:
- Periodic (quarterly, annual)
- Lot sampling and testing
- Failure analysis required

Typical FIT targets: <10 FIT (extremely reliable)
```

## Best Practices

### Test Planning

```
✓ Define requirements early (design phase)
✓ Use industry standards (JEDEC, MIL, AEC)
✓ Plan sample sizes (statistical significance)
✓ Include stress levels (3-4 levels for ALT)
✓ Monitor throughout test (not just end)
✓ Perform failure analysis on all failures
✓ Document test procedures thoroughly
✓ Maintain traceability (samples, data)
✓ Review and update based on field data
✓ Budget time and resources adequately
```

### Common Mistakes ✗

```
✗ Insufficient sample size (no statistical power)
✗ Single stress level (cannot extrapolate)
✗ No failure analysis (miss root cause)
✗ Testing too late (after design frozen)
✗ Wrong stress (doesn't match use case)
✗ No monitoring (only pass/fail at end)
✗ Poor documentation (cannot reproduce)
✗ Ignoring field failures (no feedback)
✗ Over-testing (gold-plating, costly)
✗ Under-testing (escapes to field)
```

### Cost Optimization

```
Reliability test costs:
- Equipment: $50K-500K (chambers, testers)
- Sample units: $2-100 per unit × 77-231 units
- Test duration: weeks to months
- Labor: Engineering + technician time
- Failure analysis: $1K-10K per failure

Total program: $100K-1M typical

ROI:
- Prevents costly field failures
- Qualifies for high-value markets
- Builds customer confidence
- Reduces warranty costs
```

## References

1. JEDEC Solid State Technology Association. (2020). *JESD22 Test Methods*.

2. AEC - Automotive Electronics Council. (2020). *AEC-Q100: Failure Mechanism Based Stress Test Qualification for Integrated Circuits*.

3. MIL-PRF-38534. (2018). *Performance Specification: Hybrid Microcircuits, General Specification for*.

4. ReliaSoft Corporation. (2015). *Life Data Analysis Reference*. ReliaSoft Publishing.

5. O'Connor, P. D. T., & Kleyner, A. (2011). *Practical Reliability Engineering* (5th ed.). Wiley.

---

**Document Information:**
- **Created:** December 21, 2025
- **Version:** 1.0
- **Status:** Complete
- **Part of:** Silicon Fabrication Handbook
- **Next Chapter:** [Failure Analysis](failure-analysis.md)
- **Previous Chapter:** [Functional Testing](functional-testing.md)

**License:** CC BY 4.0 - Free to use with attribution

---

*For questions, corrections, or contributions, please visit:*
https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook