# Functional Testing for MEMS

## Table of Contents
- [Introduction](#introduction)
  - [Parametric vs Functional Testing](#parametric-vs-functional-testing)
  - [Test Flow](#test-flow)
- [Sensor Testing](#sensor-testing)
  - [Accelerometer Testing](#accelerometer-testing)
  - [Pressure Sensor Testing](#pressure-sensor-testing)
  - [Gyroscope Testing](#gyroscope-testing)
  - [Microphone Testing](#microphone-testing)
- [Actuator Testing](#actuator-testing)
  - [MEMS Switch Testing](#mems-switch-testing)
  - [Optical MEMS Testing](#optical-mems-testing)
- [System-Level Testing](#system-level-testing)
  - [Inertial Measurement Unit (IMU)](#inertial-measurement-unit-imu)
  - [TPMS (Tire Pressure Monitoring System)](#tpms-tire-pressure-monitoring-system)
- [Production Testing](#production-testing)
  - [Test Strategy](#test-strategy)
  - [Parallel Testing](#parallel-testing)
  - [Automated Test Equipment (ATE)](#automated-test-equipment-ate)
- [Test Coverage](#test-coverage)
  - [Fault Coverage](#fault-coverage)
  - [Escape Rate](#escape-rate)
  - [Test Limits and Guard Bands](#test-limits-and-guard-bands)
- [Cost Optimization](#cost-optimization)
  - [Test Cost Breakdown](#test-cost-breakdown)
  - [Optimization Strategies](#optimization-strategies)
- [Best Practices](#best-practices)
  - [Test Development](#test-development)
  - [Common Mistakes ✗](#common-mistakes)
- [References](#references)

## Introduction

Functional testing validates that MEMS devices operate correctly under real-world conditions. Unlike parametric testing (DC/static), functional testing applies dynamic stimuli and verifies complete system behavior.

### Parametric vs Functional Testing

| Aspect | Parametric | Functional |
|--------|------------|------------|
| Purpose | Verify individual parameters | Verify system operation |
| Conditions | Static, DC | Dynamic, real-world |
| Time | Fast (sec/die) | Moderate to slow (min/device) |
| Equipment | General (SMU, LCR) | Specialized (stimulus + measurement) |
| Coverage | Component-level | System-level |
| When | Wafer-level, early | Package-level, final |
| Cost | Low | Medium-High |

### Test Flow

```
Wafer Level:
- Parametric test (electrical)
- Basic functionality (if possible)
- Known Good Die (KGD)

Package Level:
- Power-up test
- Functional test (full stimulus)
- Calibration
- Final parametric
- Burn-in (sample or 100%)
- Final functional verification

Shipping:
- Mark with calibration data
- Traceability
```

## Sensor Testing

### Accelerometer Testing

**Test Setup:**

```
Equipment:
- Shaker table (vibration exciter)
- Accelerometer reference sensor
- Signal generator (sine/random)
- Oscilloscope or DAQ
- Amplifier (if needed)

Frequency range: DC to 10 kHz typical
Acceleration: 0.01g to 100g
Position: 6-axis (±X, ±Y, ±Z)

Cost: $10K (basic) to $200K (precision)
```

**Test Sequence:**

```
1. Zero-G Offset:
   - Device horizontal (perpendicular to gravity)
   - No stimulus
   - Measure output voltage
   - Spec: Typically ±50 mg offset
   - Record: Store for calibration

2. 1-G Sensitivity:
   - Rotate device +90° (sensitive axis up)
   - Measure output: V_up
   - Rotate -90° (sensitive axis down)
   - Measure output: V_down
   - Sensitivity = (V_up - V_down) / 2g
   
   Example:
   V_up = +525 mV
   V_down = -475 mV
   S = (525 - (-475)) / 2 = 500 mV/g
   Spec: 450-550 mV/g → Pass

3. Frequency Response:
   - Apply sine wave: 10 Hz to 1 kHz
   - Measure output amplitude and phase
   - Verify bandwidth: -3dB point > 500 Hz
   - Check resonance: Not in band
   
4. Linearity:
   - Apply 0.1g to 10g in steps
   - Plot output vs input
   - Calculate non-linearity
   - Spec: <2% FSO (Full Scale Output)

5. Cross-Axis Sensitivity:
   - Apply acceleration perpendicular to sense axis
   - Measure output
   - Spec: <2% (ideally <1%)
```

**Pass/Fail Criteria:**

| Parameter | Min | Typ | Max | Units |
|-----------|-----|-----|-----|-------|
| Sensitivity | 450 | 500 | 550 | mV/g |
| Zero-g offset | -50 | 0 | +50 | mg |
| Bandwidth | 500 | 800 | - | Hz |
| Non-linearity | - | 0.5 | 2.0 | % FSO |
| Noise density | - | 100 | 200 | μg/√Hz |
| Cross-axis | - | 1 | 2 | % |

**Test Time:**
- Quick test (sensitivity only): 5-10 sec
- Full test (all parameters): 30-60 sec
- Characterization: 5-15 min

### Pressure Sensor Testing

**Test Setup:**

```
Equipment:
- Pressure controller (pneumatic/hydraulic)
- Reference pressure sensor
- Voltage measurement (DMM or DAQ)
- Chamber (for absolute sensors)

Pressure range: 0 to P_max
Resolution: 0.01% FSO typical
Reference accuracy: 0.02-0.05% FSO

Cost: $15K (basic) to $100K (precision)
```

**Test Sequence:**

```
1. Zero Pressure Test:
   - For gauge sensors: Vent to atmosphere
   - For absolute: Evacuate chamber
   - Measure output voltage
   - Spec: Within ±1% FSO

2. Full Scale Test:
   - Apply maximum rated pressure
   - Measure output
   - Calculate span: V_FS - V_zero
   - Verify within spec

3. Linearity:
   - Apply 5-11 pressure points (0-100%)
   - Steps: 0, 10%, 25%, 50%, 75%, 90%, 100%
   - Calculate best-fit line
   - Measure deviations
   - Non-linearity = (Max deviation / FSO) × 100%
   
4. Hysteresis:
   - Sweep up: 0 → 100%
   - Sweep down: 100% → 0%
   - Compare readings at same pressure
   - Hysteresis = Max difference / FSO × 100%
   
   Spec: <0.1% FSO (high quality)
         <0.5% FSO (standard)

5. Repeatability:
   - Apply same pressure 5-10 times
   - Calculate standard deviation
   - Repeatability = 3σ / FSO × 100%
```

**Example Test:**

```
Pressure sensor: 0-100 kPa
Output: 0.5-4.5V (4V span)

Test points:
P (kPa) | V_up (V) | V_down (V) | Avg (V)
--------|----------|------------|--------
0       | 0.500    | 0.505      | 0.503
25      | 1.503    | 1.497      | 1.500
50      | 2.501    | 2.499      | 2.500
75      | 3.498    | 3.502      | 3.500
100     | 4.497    | 4.503      | 4.500

Linearity: ±0.3% FSO (good)
Hysteresis: 0.1% FSO (excellent)
```

**Test Time:**
- Quick test: 10-15 sec (zero + full scale)
- Standard test: 30-45 sec (11 points)
- Full characterization: 5-10 min

### Gyroscope Testing

**Test Setup:**

```
Equipment:
- Rate table (rotation platform)
- Angle encoder (position feedback)
- Temperature chamber
- Data acquisition system

Angular rate: ±50 to ±6000°/s
Accuracy: 0.001-0.01°/s
Cost: $50K-500K (most expensive MEMS test)

Alternative (low-cost):
- Earth rate test (15°/hr)
- Simple rotation fixture
- Only for basic validation
```

**Test Sequence:**

```
1. Bias (Zero-Rate Output):
   - No rotation
   - Measure output
   - Calculate: Bias (°/s)
   - Spec: ±10°/s typical (consumer)
           ±1°/s (automotive)
           ±0.1°/s (tactical grade)

2. Scale Factor:
   - Apply known rotation rate: ±100°/s
   - Measure output voltage
   - Calculate: Sensitivity (mV/(°/s))
   - Verify within spec

3. Scale Factor Linearity:
   - Sweep rate: -300 to +300°/s
   - 5-7 points each direction
   - Plot output vs input
   - Calculate non-linearity

4. Cross-Axis Sensitivity:
   - Rotate about orthogonal axis
   - Measure output on sense axis
   - Spec: <2% (good), <1% (excellent)

5. Bandwidth:
   - Apply sinusoidal rotation
   - Sweep frequency: 1-100 Hz
   - Measure -3dB point
   - Typical: 50-200 Hz bandwidth
```

**Simplified Earth-Rate Test:**

```
For low-cost validation:

1. Orient sensor Z-axis vertical
   - Rotation rate = 15.04°/hr × sin(latitude)
   - At 45° latitude: 10.6°/hr

2. Measure output for 1 minute
   - Average readings
   - Convert to °/s or °/hr

3. Rotate 180° (flip sensor)
   - Repeat measurement
   - Sign should reverse

Sensitivity = (V₁ - V₂) / (2 × Earth_rate)

Limitations:
- Very slow (minutes per test)
- Low accuracy
- Only detects gross failures
- Not for production (rate table required)
```

**Test Time:**
- Quick test (bias + scale factor): 10-20 sec
- Full test: 2-5 min
- Multi-axis (3-axis IMU): 5-15 min

### Microphone Testing

**Test Setup:**

```
Equipment:
- Sound source (speaker)
- Anechoic chamber or controlled environment
- Reference microphone (calibrated)
- Audio analyzer
- Function generator

Frequency: 20 Hz - 20 kHz (audio)
SPL range: 30-120 dB
THD analyzer: Measure distortion

Cost: $5K (basic) to $50K (precision)
```

**Test Sequence:**

```
1. Sensitivity:
   - Apply 1 kHz tone at 94 dB SPL
   - Measure output voltage
   - Calculate sensitivity (dBV/Pa or mV/Pa)
   
   Example:
   Output: 10 mV at 94 dB SPL (1 Pa)
   Sensitivity: -40 dBV = 10 mV/Pa

2. Frequency Response:
   - Sweep 100 Hz to 10 kHz
   - Constant SPL (94 dB)
   - Measure amplitude
   - Plot response curve
   - Spec: ±3 dB from 100 Hz to 8 kHz

3. THD (Total Harmonic Distortion):
   - Apply 1 kHz at 100 dB SPL
   - Measure harmonics (2f, 3f, 4f...)
   - Calculate THD%
   - Spec: <1% at 100 dB, <5% at 120 dB

4. Signal-to-Noise Ratio (SNR):
   - Measure noise floor (no signal)
   - Apply 1 kHz at 94 dB SPL
   - SNR = 20 × log₁₀(V_signal / V_noise)
   - Spec: >60 dB (good), >70 dB (excellent)
```

**Test Time:**
- Quick test: 5-10 sec
- Full frequency response: 30-60 sec

## Actuator Testing

### MEMS Switch Testing

**Test Setup:**

```
Equipment:
- DC power supply (actuation)
- High-voltage supply (if needed: 20-100V)
- Network analyzer or DMM
- Pulse generator (switching test)
- Microscope (visual inspection)
```

**Test Sequence:**

```
1. Pull-In Voltage:
   - Ramp voltage from 0V
   - Measure capacitance or contact resistance
   - V_pi: Voltage where sudden change
   - Spec: Within ±10% of design

2. Release Voltage:
   - Ramp voltage down from actuated state
   - V_release: Where contact opens
   - Hysteresis = V_pi - V_release
   - Spec: Minimal hysteresis (<5V typical)

3. Contact Resistance (closed state):
   - Apply actuation voltage
   - 4-wire measurement
   - R_contact: Typically <2 Ω
   - Monitor over cycles (degradation check)

4. Isolation (open state):
   - No actuation voltage
   - Measure resistance or capacitance
   - R_open: >10 MΩ (DC)
   - Isolation: >20 dB (RF, at 1 GHz)

5. Switching Time:
   - Apply voltage step
   - Measure time to closure
   - t_on: 1-50 μs typical
   - t_off: 1-50 μs typical

6. Cycling Test:
   - Actuate ON/OFF repeatedly
   - 1000-10,000 cycles (screening)
   - Monitor contact resistance
   - Check for degradation or stiction
```

**RF MEMS Switch (Additional Tests):**

```
7. Insertion Loss (ON state):
   - S21 measurement
   - Frequency: 1-40 GHz
   - Spec: <0.5 dB (excellent)
           <1.5 dB (acceptable)

8. Isolation (OFF state):
   - S21 measurement
   - Spec: >20 dB (good)
           >40 dB (excellent)

9. Return Loss (S11):
   - Both ON and OFF states
   - Spec: >15 dB (impedance match)

Test Time: 30-60 sec per device (DC)
           2-5 min (full RF characterization)
```

### Optical MEMS Testing

**Micromirror (DLP):**

```
Test Setup:
- Laser source
- Position-sensitive detector
- High-speed camera (optional)
- Drive electronics

Tests:
1. Tilt Angle:
   - Laser reflection method
   - Measure deflection angle
   - Spec: ±12° (DLP standard)

2. Switching Speed:
   - Apply voltage step
   - Measure with photodetector
   - t_switch: 10-20 μs typical

3. Uniformity (array):
   - Test multiple mirrors
   - Angle variation: <±0.1°
   - Critical for image quality

Test Time: 1-5 sec per mirror (sampling)
           1-10 min for array characterization
```

## System-Level Testing

### Inertial Measurement Unit (IMU)

**6-Axis IMU (3-axis accel + 3-axis gyro):**

```
Test Sequence:
1. Power-up test (5 sec)
   - Apply power
   - Check supply current
   - Verify communication (I²C/SPI)
   - Read device ID

2. Self-test (10 sec)
   - Built-in test mode
   - Internal actuation
   - Verify response
   - Pass/fail flag

3. Per-axis testing (60 sec)
   - 6 orientations (±X, ±Y, ±Z)
   - Measure all 6 outputs
   - Verify crosstalk <2%

4. Dynamic test (30 sec)
   - Apply rotation + vibration
   - Verify sensor fusion
   - Check for anomalies

Total test time: 105 sec per unit

Multi-site testing:
- 4-8 units in parallel
- Throughput: 100-200 units/hour
```

### TPMS (Tire Pressure Monitoring System)

**Complete Module Test:**

```
Components:
- Pressure sensor
- Accelerometer (motion detection)
- RF transmitter (315/434 MHz)
- Battery
- Microcontroller

Test Sequence:
1. Pressure test (20 sec)
   - Apply 200 kPa
   - Verify reading within ±7 kPa

2. Accelerometer test (10 sec)
   - Shake fixture
   - Verify motion detection
   - Verify sleep mode

3. RF test (15 sec)
   - Trigger transmission
   - Measure frequency: ±50 kHz
   - Measure power: -10 to +10 dBm
   - Verify data integrity

4. Battery test (5 sec)
   - Measure voltage: >2.8V (3V coin cell)
   - Estimated life: >5 years

5. Programming (10 sec)
   - Write unique ID
   - Store calibration data

Total: 60 sec per unit
Throughput: 60 units/hour (single station)
```

## Production Testing

### Test Strategy

**Coverage vs Cost:**

```
100% Testing:
- Critical parameters
- Safety-related
- Customer specifications
- Example: Automotive sensors

Sampling:
- Non-critical parameters
- Stable processes (Cpk > 1.67)
- Example: Detailed characterization
- Sample: 1-5% of production

AQL (Acceptable Quality Level):
- Define acceptable defect rate
- Sample based on MIL-STD-105E
- Example: AQL 0.65% → sample ~125 from 1000
```

**Test Level Selection:**

| Level | Coverage | Time/Unit | Cost | When |
|-------|----------|-----------|------|------|
| Quick | Essential only | 5-15 sec | Low | 100% screening |
| Standard | Key specs | 30-60 sec | Medium | Production release |
| Full | All parameters | 2-10 min | High | Sample, qualification |
| Characterization | Extended | 30-120 min | Very high | Development, FA |

### Parallel Testing

**Benefits:**

```
Single-site: 60 sec/unit → 60 units/hr
Quad-site: 60 sec/4 units → 240 units/hr
16-site: 60 sec/16 units → 960 units/hr

Cost consideration:
- 4× throughput ≈ 2× equipment cost
- ROI depends on volume

Suitable for:
- High volume (>100K/month)
- Test time dominated (not handling)
- Consistent test (not sequential stimulus)
```

### Automated Test Equipment (ATE)

**Handler Integration:**

```
Flow:
1. Pick device from tray/tape
2. Insert into test socket
3. Apply power and stimulus
4. Measure response
5. Compare to limits (pass/fail)
6. Sort to output bin
7. Record data
8. Next device

Handler types:
- Gravity feed: Simple, low cost
- Pick-and-place: Flexible, accurate
- Turret: High speed (>1000 UPH)

Cost: $50K-500K depending on speed
```

**Throughput Calculation:**

```
Test time: 30 sec
Index time: 3 sec (pick, place, sort)
Total cycle: 33 sec

UPH = 3600 / 33 = 109 units/hour

With 8-site parallel:
UPH = 8 × 109 = 872 units/hour

Monthly capacity (85% uptime):
- Hours/month: 720 × 0.85 = 612 hr
- Units/month: 872 × 612 = 534K

Check: Meets 500K/month target ✓
```

## Test Coverage

### Fault Coverage

**Goal:** Detect all possible failures

```
Stuck-at faults:
- Node stuck at logic 1 or 0
- Detected by: Functional vectors

Bridging faults:
- Shorts between nets
- Detected by: IDDQ or functional

Open circuits:
- Broken connections
- Detected by: Continuity or functional

Parametric faults:
- Out-of-spec values
- Detected by: Parametric tests

Coverage = (Faults detected / Total faults) × 100%

Target: >95% for production test
        >99% for automotive/medical
```

### Escape Rate

**Defective Parts Per Million (DPPM):**

```
DPPM = (Defects escaped to customer / Units shipped) × 10⁶

Industry targets:
- Consumer: <500 DPPM (0.05%)
- Automotive: <10 DPPM (0.001%)
- Medical: <1 DPPM (0.0001%)

Calculation example:
Shipped: 1,000,000 units
Customer returns: 100 defective

DPPM = (100 / 1,000,000) × 10⁶ = 100 DPPM
```

**Reducing Escapes:**

```
Methods:
1. Comprehensive test coverage
   - All specifications tested
   - Guard bands applied

2. Test correlation
   - Wafer test vs final test
   - Identify weak correlation

3. Statistical outlier screening
   - Flag devices near limits
   - Extended testing or reject

4. Reliability screening
   - Burn-in (stress testing)
   - Weed out infant mortality

5. Root cause analysis
   - Investigate every escape
   - Improve test or process
```

### Test Limits and Guard Bands

**Setting Limits:**

```
Specification: 50 ± 5 units (45-55)

Test limits with guard band:
Test_min = Spec_min + Guard
Test_max = Spec_max - Guard

Guard band: 10-20% typical

Example:
Spec: 45-55
Guard: 10% (0.5 units)
Test limits: 45.5-54.5

Result:
- Devices 45-45.5: Rejected (but would pass spec)
- Devices 45.5-54.5: Pass
- Devices 54.5-55: Rejected (but would pass spec)

Reduces customer escapes
Slight yield loss acceptable
```

## Cost Optimization

### Test Cost Breakdown

```
Total test cost per device:

Component               | Cost    | % Total
------------------------|---------|--------
Equipment depreciation  | $0.05   | 25%
Labor                   | $0.03   | 15%
Consumables (sockets)   | $0.02   | 10%
Facilities (space)      | $0.02   | 10%
Test time (throughput)  | $0.06   | 30%
Data management         | $0.02   | 10%
------------------------|---------|--------
Total                   | $0.20   | 100%

As % of device ASP:
$0.20 / $2.00 = 10%

Target: <15% of ASP
```

### Optimization Strategies

```
1. Reduce test time:
   - Eliminate redundant tests
   - Optimize test sequence
   - Parallel testing
   Target: 50% reduction

2. Increase throughput:
   - Multi-site testing
   - Faster handlers
   - Better fixturing
   Target: 2-4× improvement

3. Reduce equipment cost:
   - Commercial off-the-shelf (COTS)
   - Modular design (upgrade later)
   - Lease vs buy

4. Improve yield:
   - Better test coverage
   - Reduce false failures
   - Tighter process control
   Target: Each 1% yield = significant savings
```

## Best Practices

### Test Development

```
✓ Specify test requirements early (design phase)
✓ Develop test plan in parallel with design
✓ Use statistical sampling (not 100% unless required)
✓ Implement guard bands (prevent escapes)
✓ Correlate wafer to package test
✓ Validate test repeatability (R&R < 10%)
✓ Calibrate equipment regularly (monthly/quarterly)
✓ Monitor test escapes (feedback loop)
✓ Document procedures thoroughly
✓ Train operators and engineers
```

### Common Mistakes ✗

```
✗ Testing too much (gold-plating)
✗ Testing too little (escapes)
✗ No guard bands (customer failures)
✗ Ignoring outliers (miss systemic issues)
✗ Poor test coverage (faults not detected)
✗ No calibration schedule (drift)
✗ Inadequate documentation
✗ Single-site when multi-site needed (low throughput)
✗ Expensive equipment for simple tests
✗ No correlation study (wafer vs package)
```

## References

1. Semiconductor Equipment and Materials International (SEMI). (2020). *Test Methods Standards*.

2. Burns, M., & Roberts, G. W. (2012). *An Introduction to Mixed-Signal IC Test and Measurement* (2nd ed.). Oxford University Press.

3. IEEE Std 1149.1. (2013). *IEEE Standard for Test Access Port and Boundary-Scan Architecture*.

4. MIL-STD-883. (2016). *Test Method Standard: Microcircuits*. Department of Defense.

5. Bushnell, M. L., & Agrawal, V. D. (2000). *Essentials of Electronic Testing for Digital, Memory, and Mixed-Signal VLSI Circuits*. Springer.

---

**Document Information:**
- **Created:** December 20, 2025
- **Version:** 1.0
- **Status:** Complete
- **Part of:** Silicon Fabrication Handbook
- **Next Chapter:** [Reliability Testing](reliability-testing.md)
- **Previous Chapter:** [Parametric Testing](parametric-testing.md)

**License:** CC BY 4.0 - Free to use with attribution

---

*For questions, corrections, or contributions, please visit:*
https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook
