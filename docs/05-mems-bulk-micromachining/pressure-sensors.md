# MEMS Pressure Sensors

## Table of Contents
- [Introduction](#introduction)
  - [Market Overview](#market-overview)
  - [Performance Metrics](#performance-metrics)
  - [Sensor Types Comparison](#sensor-types-comparison)
- [Sensing Mechanisms](#sensing-mechanisms)
  - [Basic Principle](#basic-principle)
  - [Stress Distribution](#stress-distribution)
- [Piezoresistive Sensors](#piezoresistive-sensors)
  - [Piezoresistive Effect](#piezoresistive-effect)
  - [Wheatstone Bridge Configuration](#wheatstone-bridge-configuration)
  - [Sensitivity Calculation](#sensitivity-calculation)
  - [Design Optimization](#design-optimization)
  - [Temperature Compensation](#temperature-compensation)
- [Capacitive Sensors](#capacitive-sensors)
  - [Operating Principle](#operating-principle)
  - [Design Example](#design-example)
  - [Readout Circuits](#readout-circuits)
  - [Advantages & Limitations](#advantages-limitations)
  - [Pull-In Effect](#pull-in-effect)
- [Resonant Sensors](#resonant-sensors)
  - [Operating Principle](#operating-principle-1)
  - [Advantages](#advantages)
- [Fabrication Processes](#fabrication-processes)
  - [Bulk Micromachining Process](#bulk-micromachining-process)
  - [Anisotropic Etching](#anisotropic-etching)
  - [Surface Micromachining Alternative](#surface-micromachining-alternative)
- [Applications](#applications)
  - [1. Automotive Manifold Absolute Pressure (MAP)](#1-automotive-manifold-absolute-pressure-map)
  - [2. Tire Pressure Monitoring System (TPMS)](#2-tire-pressure-monitoring-system-tpms)
  - [3. Medical Blood Pressure](#3-medical-blood-pressure)
  - [4. Barometric Pressure (Smartphones)](#4-barometric-pressure-smartphones)
- [Performance Comparison](#performance-comparison)
  - [Commercial Examples](#commercial-examples)
- [Design Guidelines](#design-guidelines)
  - [Membrane Design](#membrane-design)
  - [Packaging Considerations](#packaging-considerations)
- [Testing & Calibration](#testing-calibration)
  - [Characterization Tests](#characterization-tests)
  - [Calibration Process](#calibration-process)
- [Future Trends](#future-trends)
  - [Advanced Technologies](#advanced-technologies)
- [References](#references)

## Introduction

MEMS pressure sensors are the most commercially successful MEMS devices, with billions produced annually for automotive, medical, industrial, and consumer applications.

### Market Overview

| Application | Volume | Typical Range | Key Requirements |
|-------------|--------|---------------|------------------|
| Automotive (MAP, TMAP) | 500M+ units/year | 20-250 kPa | High reliability, wide temp |
| Tire pressure (TPMS) | 400M+ units/year | 100-450 kPa | Battery operation, RF |
| Medical (blood pressure) | 100M+ units/year | 0-300 mmHg | Biocompatibility, accuracy |
| Barometric (smartphones) | 1B+ units/year | 30-110 kPa | Low power, small size |
| Industrial process | 50M+ units/year | 1 Pa - 100 MPa | Wide range, harsh conditions |

### Performance Metrics

**Key Specifications:**
```
Pressure Range: 1 Pa to 100 MPa
Accuracy: 0.1% to 2% FSO (Full Scale Output)
Resolution: 1 Pa to 1 kPa
Temperature Range: -40°C to 150°C (automotive)
                   -55°C to 200°C (industrial)
Response Time: 1 ms to 10 ms
Long-term Stability: <0.1% FSO per year
```

### Sensor Types Comparison

| Type | Sensitivity | Power | Temperature Drift | Cost | Applications |
|------|-------------|-------|-------------------|------|--------------|
| Piezoresistive | High | Medium | Moderate (TC ≈ 0.2%/°C) | Low | Automotive, industrial |
| Capacitive | Medium | Low | Low (TC ≈ 0.05%/°C) | Medium | Consumer, medical |
| Resonant | Very High | High | Very Low | High | Aerospace, metrology |

## Sensing Mechanisms

### Basic Principle

Pressure causes membrane deflection, which is converted to an electrical signal:

```
Pressure (P) → Membrane Deflection (w) → Signal Change (ΔR, ΔC, Δf)
```

**Membrane Deflection:**

For circular diaphragm under uniform pressure:

```
w(r) = (3(1-ν²)PR⁴)/(16Et³) × [1 - (r/R)²]²

Where:
w(r) = deflection at radius r
P = applied pressure
R = membrane radius
t = membrane thickness
E = Young's modulus
ν = Poisson's ratio
```

**Center Deflection (r = 0):**
```
w_max = (3(1-ν²)PR⁴)/(16Et³)

For silicon (E = 170 GPa, ν = 0.28):
w_max = 0.0151 × PR⁴/t³
```

**Example Calculation:**
```
Given:
P = 100 kPa
R = 500 μm
t = 20 μm
E = 170 GPa
ν = 0.28

w_max = 0.0151 × (10⁵ Pa × (500×10⁻⁶ m)⁴) / (20×10⁻⁶ m)³
w_max = 0.0151 × 10⁵ × 6.25×10⁻²⁴ / 8×10⁻¹⁸
w_max ≈ 1.18 μm
```

### Stress Distribution

Maximum stress occurs at membrane edge:

```
σ_max = (3PR²)/(4t²) × [3(1-ν)]

For above example:
σ_max = (3 × 10⁵ × (500×10⁻⁶)²)/(4 × (20×10⁻⁶)²) × 3(1-0.28)
σ_max ≈ 54 MPa

Safety factor = σ_yield / σ_max
For Si (σ_yield ≈ 7 GPa): SF = 130× (very safe)
```

## Piezoresistive Sensors

Most common type, using stress-induced resistance change in silicon.

### Piezoresistive Effect

**Resistance Change:**
```
ΔR/R = π_l σ_l + π_t σ_t

Where:
π_l = longitudinal piezoresistive coefficient
π_t = transverse piezoresistive coefficient
σ_l = longitudinal stress
σ_t = transverse stress
```

**Silicon Piezoresistive Coefficients:**

For p-type Si <110> orientation:
```
π_44 = +138.1 × 10⁻¹¹ Pa⁻¹
π_l (longitudinal) ≈ +71.8 × 10⁻¹¹ Pa⁻¹
π_t (transverse) ≈ -66.3 × 10⁻¹¹ Pa⁻¹
```

### Wheatstone Bridge Configuration

**Full Bridge (4 resistors):**
```
      R1 ——— R2
      |       |
   Vexc      Vout
      |       |
      R3 ——— R4

Voltage Output:
Vout = Vexc × [(R1×R4 - R2×R3) / ((R1+R3)(R2+R4))]

For matched bridge:
Vout/Vexc = (ΔR/R) × (π_l - π_t) × σ_max
```

**Placement Strategy:**
```
Position on Membrane:
R1, R3: Edge (radial direction) → +ΔR
R2, R4: Edge (tangential direction) → -ΔR

Result: Maximum signal, temperature compensation
```

### Sensitivity Calculation

**Example:**
```
Bridge Configuration: Full bridge, p-type Si
σ_max = 54 MPa (from earlier)
π_l - π_t = 138.1 × 10⁻¹¹ Pa⁻¹
Vexc = 5 V

ΔR/R = (π_l - π_t) × σ_max
     = 138.1×10⁻¹¹ × 54×10⁶
     = 0.00746 = 0.746%

Vout = 5 V × 0.00746 = 37.3 mV

Sensitivity = 37.3 mV / 100 kPa = 0.373 mV/kPa
            = 373 μV/kPa
```

### Design Optimization

**Membrane Thickness vs Sensitivity:**

| Thickness (μm) | w_max (μm) | σ_max (MPa) | Sensitivity (mV/100kPa) |
|----------------|------------|-------------|-------------------------|
| 10 | 9.4 | 216 | 149 |
| 20 | 1.2 | 54 | 37 |
| 30 | 0.35 | 24 | 16 |
| 50 | 0.08 | 8.6 | 6 |

Trade-off: Thinner → Higher sensitivity but lower overpressure limit

**Overpressure Protection:**
```
Maximum safe pressure:
P_max = (4t²σ_yield) / (3R²(1-ν))

For t = 20 μm, R = 500 μm, σ_yield = 7 GPa:
P_max ≈ 3.7 MPa (37 bar)
```

### Temperature Compensation

**Sources of Temperature Drift:**

1. **Resistance TCR (Temperature Coefficient of Resistance):**
   ```
   TCR ≈ +0.1 to +0.2%/°C for p-type Si
   ```

2. **Gauge Factor Temperature Dependence:**
   ```
   ~-0.2%/°C
   ```

3. **Membrane Modulus Change:**
   ```
   dE/dT ≈ -64 ppm/°C
   ```

**Compensation Techniques:**

1. **Hardware Compensation:**
   - Bridge arrangement (cancels 1st order)
   - Reference resistors on unstressed region
   - Constant current drive

2. **Software Compensation:**
   ```
   V_compensated = V_measured × [1 + α(T-T₀) + β(T-T₀)²]
   
   Typical coefficients:
   α ≈ -2000 ppm/°C
   β ≈ -10 ppm/°C²
   ```

## Capacitive Sensors

Use capacitance change between deflecting membrane and fixed electrode.

### Operating Principle

**Parallel Plate Capacitor:**
```
C = ε₀εᵣA/d

Where:
ε₀ = 8.854 × 10⁻¹² F/m (vacuum permittivity)
εᵣ = 1 (air gap)
A = electrode area
d = gap spacing

For deflecting membrane:
C(P) = ε₀A / (d₀ - w(P))

ΔC/C₀ ≈ w/d₀ (for small deflections)
```

### Design Example

**Specifications:**
```
Membrane: 1000 μm diameter, 10 μm thick
Gap: d₀ = 5 μm
Pressure range: 0-100 kPa
Electrode area: π × (500 μm)²
```

**Calculations:**
```
C₀ = (8.854×10⁻¹² × π × (500×10⁻⁶)²) / (5×10⁻⁶)
C₀ = 1.39 pF

For P = 100 kPa:
w_max = 0.0151 × 10⁵ × (500×10⁻⁶)⁴ / (10×10⁻⁶)³
w_max = 0.94 μm

ΔC/C₀ = 0.94/5 = 18.8%
ΔC = 0.26 pF

Sensitivity = 0.26 pF / 100 kPa = 2.6 fF/kPa
```

### Readout Circuits

**Charge Amplifier:**
```
Vout = Q/C_feedback = (C_sense × V_bias)/C_feedback

Typical:
V_bias = 5-10 V
C_feedback = 1-10 pF
Noise floor: 10-50 aF/√Hz
```

**Capacitance-to-Digital Converter (CDC):**
- Commercial ICs: AD7746, FDC2214
- Resolution: 1-10 aF
- Sampling rate: 10-100 Hz
- Power: 1-10 mW

### Advantages & Limitations

**Advantages:**
- Low temperature drift (0.05%/°C)
- Low power consumption
- High sensitivity
- Linear output (for small deflections)

**Limitations:**
- Complex readout circuitry
- Parasitic capacitance issues
- Pull-in instability at high pressure
- Requires hermetic sealing

### Pull-In Effect

**Critical Pressure:**
```
P_pull-in occurs when electrostatic force exceeds restoring force

P_pull-in = (2Et³)/(3R²(1-ν²)) × (d₀/3)

For d₀ = 5 μm, t = 10 μm, R = 500 μm:
P_pull-in ≈ 7.4 kPa

Design rule: Operate at < 30% of P_pull-in
```

## Resonant Sensors

Use pressure-induced stress to shift resonant frequency.

### Operating Principle

**Resonant Beam:**
```
f = (1/2π) × √(k/m_eff)

Under axial stress σ:
f(σ) = f₀ × √(1 + σ/E × (L/t)²)

Sensitivity:
Δf/f = (1/2) × (σ/E) × (L/t)²
```

**Example:**
```
Beam: L = 200 μm, t = 5 μm
f₀ = 100 kHz
Induced stress: σ = 50 MPa (at 100 kPa pressure)

Δf/f = (1/2) × (50×10⁶/170×10⁹) × (200/5)²
     = 0.5 × 2.94×10⁻⁴ × 1600
     = 0.235 = 23.5%

Δf = 23.5 kHz for 100 kPa
Sensitivity = 235 Hz/kPa
```

### Advantages

**Ultra-High Resolution:**
```
Frequency measurement resolution: 1 ppm
For f₀ = 100 kHz: 0.1 Hz
Pressure resolution: 0.1 Hz / 235 Hz/kPa = 0.4 Pa

Compare to piezoresistive: ~10 Pa typical
```

**Low Drift:**
- Digital output (frequency)
- Temperature stable (quartz reference)
- Long-term stability: <10 ppm/year

**Limitations:**
- Complex fabrication
- Higher power consumption
- Vacuum packaging required (high Q)
- Higher cost

## Fabrication Processes

### Bulk Micromachining Process

**Standard Flow (Piezoresistive):**

```
1. Start: <100> Si wafer, n-type, 400 μm thick

2. Front-side processing:
   - Thermal oxide (500 nm)
   - Implant p-type resistors (boron, 10¹⁹ cm⁻³)
   - Drive-in anneal (1100°C, 1h)
   - Metal contacts (Al, 1 μm)
   - Pattern and etch
   - Passivation (Si₃N₄, 500 nm)

3. Back-side etching:
   - Pattern oxide mask (1 μm)
   - KOH etch (80°C, 33%)
   - Etch time: ~8 hours for 380 μm
   - Stop: 20 μm membrane remains

4. Die separation and packaging
```

**Etch Stop Techniques:**

1. **Timed Etch:**
   ```
   Simple but requires tight thickness control
   Variation: ±10 μm typical
   ```

2. **Electrochemical Etch Stop (EES):**
   ```
   Uses p-n junction as etch barrier
   - Apply reverse bias during KOH etch
   - n-type stops, p-type etches
   - Accuracy: ±2 μm
   ```

3. **Boron Etch Stop:**
   ```
   High boron doping (>7×10¹⁹ cm⁻³) resists KOH
   - Diffuse boron layer (5-50 μm deep)
   - Etch selectivity: >100:1
   - Accuracy: ±0.5 μm
   ```

4. **SOI (Silicon-On-Insulator):**
   ```
   Oxide layer acts as perfect etch stop
   - Device layer = membrane thickness
   - Highest accuracy: ±0.1 μm
   - Higher wafer cost
   ```

### Anisotropic Etching

**KOH Etching:**

```
Concentration: 20-45 wt% in H₂O
Temperature: 60-90°C
Etch rate <100>: 1-1.5 μm/min
Etch rate <111>: 0.01 μm/min
Selectivity: ~100:1

Cavity angle: 54.74° (crystallographic)

Lateral undercut:
U = t × √2 (where t = etch depth)

For 380 μm etch:
U = 380 × 1.414 = 537 μm
Mask opening = Membrane size + 2×537 μm
```

**TMAH Etching:**
```
Advantages over KOH:
- CMOS compatible (doesn't attack Al)
- Lower roughness
- Temperature: 80-90°C
- Concentration: 20-25 wt%

Disadvantages:
- More expensive
- Slower etch rate (0.5-1 μm/min)
```

### Surface Micromachining Alternative

**Sacrificial Layer Process:**

```
1. Deposit PSG (2-5 μm) on substrate
2. Pattern cavity
3. Deposit poly-Si membrane (1-5 μm)
4. Pattern membrane and anchors
5. Release in HF
6. Seal with LPCVD oxide

Advantages:
- Smaller size (100-500 μm diaphragm)
- Lower cost (no backside processing)
- Batch fabrication

Limitations:
- Limited pressure range (< 200 kPa)
- Requires careful release/sealing
```

## Applications

### 1. Automotive Manifold Absolute Pressure (MAP)

**Requirements:**
```
Range: 20-250 kPa (0.2-2.5 bar)
Accuracy: ±1% FSO
Temperature: -40°C to 125°C
Response time: < 10 ms
Lifetime: 10 years, >10⁹ cycles
```

**Design:**
- Piezoresistive type
- Membrane: 500 μm × 20 μm
- Gel coating for media protection
- Plastic package with port

**Signal Conditioning:**
```
Bridge → Instrumentation Amp → ADC → Microcontroller

Features:
- Temperature compensation
- Offset trim
- Gain calibration
- Diagnostics
```

### 2. Tire Pressure Monitoring System (TPMS)

**Specifications:**
```
Range: 100-450 kPa (1-4.5 bar)
Resolution: 7 kPa (1 psi)
Accuracy: ±10 kPa
Battery life: 5-10 years
RF transmission: 315/434 MHz
```

**Special Requirements:**
- Ultra-low power: < 10 μA average
- Small size: < 15 mm diameter
- Harsh environment (chemicals, temperature)

### 3. Medical Blood Pressure

**Invasive Monitoring:**
```
Range: 0-300 mmHg (0-40 kPa)
Accuracy: ±1 mmHg
Response time: < 1 ms
Size: < 1 mm diameter (catheter tip)
```

**Key Features:**
- Biocompatible materials
- Sterilizable
- Disposable design
- Gel filling for fluid coupling

### 4. Barometric Pressure (Smartphones)

**Specifications:**
```
Range: 30-110 kPa (300-1100 mbar)
Accuracy: ±1 mbar (10 Pa)
Resolution: 0.1 mbar (10 cm altitude)
Power: < 1 μW standby
Size: < 2 × 2 × 1 mm³
```

**Applications:**
- Altitude tracking
- Weather monitoring
- Indoor navigation (floor detection)

**Technology:**
- Capacitive type
- ASIC integration
- Digital I²C/SPI output

## Performance Comparison

### Commercial Examples

| Manufacturer | Part Number | Type | Range | Accuracy | Package | Price |
|--------------|-------------|------|-------|----------|---------|-------|
| Bosch | BMP390 | Capacitive | 30-125 kPa | ±0.03 kPa | 2×2mm LGA | $2-3 |
| NXP | MPXV5004 | Piezoresistive | 0-3.9 kPa | ±2.5% | SOP-8 | $5-8 |
| Honeywell | HSC Series | Piezoresistive | 1-100 psi | ±0.25% | SIP | $20-40 |
| TE Connectivity | MS5607 | Capacitive | 10-120 kPa | ±0.015 kPa | QFN-8 | $3-5 |

## Design Guidelines

### Membrane Design

**Rules of Thumb:**
```
1. Aspect ratio: R/t = 10-50
   - Too thin (>50): Fragile, nonlinear
   - Too thick (<10): Low sensitivity

2. Overpressure margin: 3-5×
   SF = P_max / P_rated ≥ 3

3. Nonlinearity limit:
   w_max/t < 0.3 for <5% nonlinearity

4. Natural frequency:
   f₀ > 10 × bandwidth
   Ensures fast response
```

### Packaging Considerations

**Reference Pressure:**
```
Absolute: Sealed cavity (vacuum or gas)
Gauge: Vented to atmosphere
Differential: Two pressure ports
```

**Stress Isolation:**
- Use soft die attach (RTV silicone)
- Minimize package stress transfer
- Temperature cycling testing critical

**Media Compatibility:**
- Direct contact: Gel coating, Si₃N₄ passivation
- Isolated: Oil-filled, metal diaphragm transfer

## Testing & Calibration

### Characterization Tests

**1. Pressure Linearity:**
```
Apply 0-100% FSO in 10% steps
Calculate nonlinearity:
NL = (V_max_deviation / V_FSO) × 100%

Target: < 0.5% FSO
```

**2. Hysteresis:**
```
Cycle 0→100%→0 FSO
Hysteresis = Max difference / FSO × 100%

Target: < 0.1% FSO
```

**3. Temperature Coefficient:**
```
Measure at -40, 25, 85, 125°C
TCO (Offset) = ΔV_zero / ΔT
TCS (Span) = ΔV_FSO / ΔT

Typical:
TCO: ±50 ppm/°C
TCS: ±2000 ppm/°C (uncompensated)
```

### Calibration Process

**Multi-Point Calibration:**
```
1. Zero pressure offset trim
2. Full-scale span adjustment
3. Temperature compensation (3-5 points)
4. Nonlinearity correction (polynomial)

Stored in EEPROM/OTP:
- Offset coefficients
- Span coefficients
- Temperature coefficients
- Unique ID
```

## Future Trends

### Advanced Technologies

1. **CMOS-MEMS Integration:**
   - Sensor and electronics on same die
   - Reduced size and cost
   - Improved performance

2. **Wireless Sensors:**
   - Battery-less operation (RF harvesting)
   - Bluetooth Low Energy
   - IoT integration

3. **Multi-Sensor Fusion:**
   - Pressure + Temperature + Humidity
   - Single package
   - Advanced algorithms

4. **Harsh Environment:**
   - Silicon carbide (SiC) sensors
   - 300-600°C operation
   - Chemical resistance

## References

1. Bao, M. (2000). *Micro Mechanical Transducers: Pressure Sensors, Accelerometers and Gyroscopes*. Elsevier.

2. Eaton, W. P., & Smith, J. H. (1997). Micromachined pressure sensors: review and recent developments. *Smart Materials and Structures*, 6(5), 530.

3. Marek, J., et al. (2013). *Sensors for Automotive Applications*. Wiley-VCH.

4. Tian, B., et al. (2013). A novel wireless and temperature-compensated SAW vibration sensor. *Sensors*, 13(12), 17084-17094.

---

**Document Information:**
- **Created:** December 12, 2025
- **Version:** 1.0
- **Status:** Complete
- **Part of:** Silicon Fabrication Handbook
- **Previous Chapter:** [Wafer Bonding](wafer-bonding.md)
- **Section:** MEMS Bulk Micromachining

**License:** CC BY 4.0 - Free to use with attribution

---

*For questions, corrections, or contributions, please visit:*
https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook
