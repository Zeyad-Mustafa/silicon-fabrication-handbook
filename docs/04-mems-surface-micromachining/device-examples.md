# MEMS Device Examples

## Table of Contents
- [Introduction](#introduction)
  - [Device Classification](#device-classification)
- [Accelerometers](#accelerometers)
  - [Capacitive Comb-Drive Accelerometer](#capacitive-comb-drive-accelerometer)
  - [Commercial Example: ADXL Series (Analog Devices)](#commercial-example-adxl-series-analog-devices)
- [Gyroscopes](#gyroscopes)
  - [Z-Axis Vibratory Gyroscope](#z-axis-vibratory-gyroscope)
- [Resonators](#resonators)
  - [Clamped-Clamped Beam Resonator](#clamped-clamped-beam-resonator)
  - [Disk Resonator](#disk-resonator)
- [Pressure Sensors](#pressure-sensors)
  - [Capacitive Membrane Sensor](#capacitive-membrane-sensor)
- [RF MEMS](#rf-mems)
  - [Capacitive Shunt Switch](#capacitive-shunt-switch)
- [Optical MEMS](#optical-mems)
  - [Micromirror for Digital Light Processing (DLP)](#micromirror-for-digital-light-processing-dlp)
  - [2D Scanning Mirror](#2d-scanning-mirror)
- [Design Guidelines Summary](#design-guidelines-summary)
  - [General Principles](#general-principles)
  - [Scaling Effects](#scaling-effects)
- [Manufacturing Considerations](#manufacturing-considerations)
  - [Yield Enhancement](#yield-enhancement)
  - [Cost Reduction Strategies](#cost-reduction-strategies)
- [Future Trends](#future-trends)
  - [Integration](#integration)
  - [Materials](#materials)
  - [Applications](#applications)
- [References](#references)

## Introduction

This chapter presents practical examples of MEMS devices fabricated using surface micromachining. Each example includes design principles, fabrication process, and key performance metrics.

### Device Classification

| Device Type | Sensing Mechanism | Typical Applications |
|-------------|-------------------|---------------------|
| Accelerometer | Capacitive displacement | Automotive, smartphones, gaming |
| Gyroscope | Coriolis effect | Navigation, image stabilization |
| Resonator | Mechanical resonance | Timing, frequency references |
| Pressure Sensor | Membrane deflection | Automotive, medical, industrial |
| RF Switch | Contact resistance | Wireless communications |
| Optical Mirror | Electrostatic actuation | Display, optical switching |

## Accelerometers

### Capacitive Comb-Drive Accelerometer

**Design Overview:**

```
Structure:
├── Proof Mass: 200 × 200 × 2 μm³ (poly-Si)
├── Suspension: 4 folded beams
├── Sensing: Differential capacitors
└── Anchors: Fixed to substrate
```

**Operating Principle:**

When acceleration occurs, the proof mass displaces, changing the capacitance of fixed and movable comb fingers.

```
Acceleration → Force → Displacement → ΔCapacitance

F = m × a
x = F/k = ma/k

ΔC = 2ε₀Nh(x/g₀²)

Where:
m = proof mass (kg)
k = spring constant (N/m)
N = number of comb finger pairs
h = finger height (m)
g₀ = initial gap (μm)
```

**Design Parameters:**

```
Proof mass: 
- Material: Poly-Si (ρ = 2330 kg/m³)
- Dimensions: 200 × 200 × 2 μm³
- Mass: m = 1.86 × 10⁻¹⁰ kg

Suspension beams (folded):
- Length per segment: 100 μm
- Width: 3 μm
- Thickness: 2 μm
- Spring constant: k = 2 N/m

Comb fingers:
- Number of pairs: N = 50
- Length: 20 μm
- Gap: g₀ = 2 μm
- Height: h = 2 μm
```

**Performance Calculations:**

```
Sensitivity:
S = Δx/a = m/k = 1.86×10⁻¹⁰/2 = 9.3 × 10⁻¹¹ m/(m/s²)
S = 93 nm/g

Capacitance change per g:
C₀ = ε₀Nh/g₀ = 8.85×10⁻¹² × 50 × 2×10⁻⁶ / 2×10⁻⁶
C₀ = 0.44 pF

ΔC/g = 2C₀(x/g₀) = 2 × 0.44 × (93×10⁻⁹/2×10⁻⁶)
ΔC/g ≈ 41 aF/g

Resonant frequency:
f₀ = (1/2π)√(k/m) = (1/2π)√(2/1.86×10⁻¹⁰)
f₀ ≈ 16.5 kHz

Bandwidth (Q = 10, air damping):
BW = f₀/Q ≈ 1.65 kHz
```

**Fabrication Process (4-Mask):**

```
Layer 1 - Anchors:
1. Thermal oxide (2 μm)
2. Pattern and etch oxide
3. Define anchor regions

Layer 2 - Structural poly-Si:
1. LPCVD poly-Si (2 μm, 585°C)
2. POCl₃ doping (n+, 1×10²⁰ cm⁻³)
3. Anneal (1000°C, 1h)
4. Pattern structural layer

Layer 3 - Metal contacts:
1. Sputter Al (500 nm)
2. Pattern metal

Release:
1. HF release (6:1 BHF, 45 min)
2. IPA rinse
3. Critical point dry
4. FDTS coating
```

**Typical Performance:**

| Parameter | Value | Units |
|-----------|-------|-------|
| Range | ±2 to ±50 | g |
| Sensitivity | 30-100 | aF/g |
| Noise floor | 50-200 | μg/√Hz |
| Bandwidth | 1-5 | kHz |
| Power | 10-100 | μW |
| Size | 1 × 1 | mm² |

### Commercial Example: ADXL Series (Analog Devices)

**Key Features:**
- Differential sensing (cancels common-mode errors)
- Self-test capability (electrostatic actuation)
- Temperature compensation (on-chip)
- Digital output (SPI/I²C)

## Gyroscopes

### Z-Axis Vibratory Gyroscope

**Operating Principle:**

Uses Coriolis effect: When a vibrating mass experiences rotation, a perpendicular force appears.

```
Drive mode: Oscillation in x-direction
Sense mode: Coriolis force in y-direction

F_Coriolis = 2m × v_drive × Ω_z

Where:
m = proof mass
v_drive = drive velocity
Ω_z = rotation rate (rad/s)
```

**Design Structure:**

```
Components:
├── Proof mass: 300 × 300 × 20 μm³
├── Drive combs: 100 pairs, 2 μm gap
├── Sense combs: 100 pairs, 2 μm gap
├── Drive suspension: k_x = 100 N/m
└── Sense suspension: k_y = 500 N/m
```

**Operating Parameters:**

```
Drive frequency: f_drive = 10 kHz
Drive amplitude: x₀ = 1 μm
Drive velocity: v = 2πf × x₀ = 62.8 mm/s

For Ω = 100°/s = 1.75 rad/s:
F_Coriolis = 2 × m × v × Ω
F_Coriolis = 2 × 5×10⁻⁹ × 0.0628 × 1.75
F_Coriolis ≈ 1.1 nN

Sense displacement:
y = F/k_y = 1.1×10⁻⁹/500 = 2.2 pm

Capacitance change:
ΔC = 2ε₀Nh(y/g₀²) ≈ 0.1 aF per °/s
```

**Fabrication (Through-Silicon Process):**

```
1. SOI wafer (device layer: 20 μm)
2. DRIE etch device layer
3. Pattern anchors
4. Release (BOX etch)
5. Metal deposition
6. Wire bonding
7. Vacuum packaging (Q > 10,000)
```

**Key Performance:**

| Parameter | Value | Units |
|-----------|-------|-------|
| Range | ±300 | °/s |
| Sensitivity | 0.1 | aF/(°/s) |
| Noise | 0.01 | °/s/√Hz |
| Bandwidth | 100 | Hz |
| Quadrature error | <1 | °/s |

**Challenges:**

1. **Quadrature Error**: Manufacturing imperfections cause coupling between drive and sense modes
   - Solution: Electronic cancellation, precise fabrication

2. **Mode Matching**: Drive and sense frequencies must be close
   - Solution: Post-fabrication tuning (electrostatic)

3. **Temperature Drift**: Frequency shifts with temperature
   - Solution: Compensation circuitry, oven control

## Resonators

### Clamped-Clamped Beam Resonator

**Design:**

```
Beam dimensions:
- Length: L = 50 μm
- Width: w = 5 μm
- Thickness: t = 2 μm
- Material: Poly-Si

Actuation: Electrostatic (parallel plate)
- Gap: g₀ = 1 μm
- Electrode area: 50 × 5 μm²

Detection: Capacitive
```

**Resonant Frequency:**

```
f₀ = (1/2π) × √(k/m_eff)

For clamped-clamped beam:
k = 32EI/L³
I = wt³/12
m_eff = 0.37 × ρ × V

Calculation:
E = 160 GPa (poly-Si)
I = 5×10⁻⁶ × (2×10⁻⁶)³/12 = 3.33×10⁻²⁴ m⁴
k = 32 × 160×10⁹ × 3.33×10⁻²⁴/(50×10⁻⁶)³
k = 136 N/m

m_eff = 0.37 × 2330 × 50×5×2×10⁻¹⁸
m_eff = 4.3×10⁻¹³ kg

f₀ = (1/2π) × √(136/4.3×10⁻¹³)
f₀ ≈ 2.84 MHz
```

**Quality Factor:**

```
In vacuum (10⁻³ Torr):
Q = 10,000 - 100,000

In air (1 atm):
Q = 100 - 1,000

Q determines frequency stability:
Δf/f₀ = 1/(2Q)
```

**Fabrication Process:**

```
1. Sacrificial oxide (1 μm PSG)
2. Poly-Si beam (2 μm)
3. Doping and anneal
4. Pattern beam
5. Bottom electrode (before beam)
6. Release in HF
7. Hermetic packaging (vacuum)
```

**Applications:**

- Timing references (replacing quartz crystals)
- Frequency filters
- Mass sensors (frequency shift with added mass)

**Performance:**

| Parameter | Value | Units |
|-----------|-------|-------|
| Frequency | 1-100 | MHz |
| Q-factor | 10,000 | (vacuum) |
| Frequency stability | 1-10 | ppm/°C |
| Power | 10-100 | μW |

### Disk Resonator

**Advantages over beam:**
- Higher frequency (100-1000 MHz)
- Better temperature stability
- Smaller size

**Design:**
```
Disk diameter: 10-50 μm
Thickness: 2-5 μm
Mode: Radial contour mode
Actuation: Capacitive gap around perimeter
```

## Pressure Sensors

### Capacitive Membrane Sensor

**Structure:**

```
Membrane:
- Diameter: D = 500 μm
- Thickness: t = 2 μm
- Material: Poly-Si

Cavity:
- Depth: h₀ = 2 μm (sacrificial layer)
- Reference pressure: sealed at fabrication
```

**Operating Principle:**

External pressure causes membrane deflection, changing capacitance.

```
Capacitance:
C = ε₀A/h(x,y)

Where h(x,y) = gap as function of position

For small deflections:
ΔC/C₀ ≈ w_center/h₀
```

**Deflection Analysis:**

```
Maximum deflection (center):
w_max = (3(1-ν²)P₀R⁴)/(16Et³)

For P₀ = 100 kPa:
E = 160 GPa, ν = 0.22
R = 250 μm, t = 2 μm

w_max = (3(1-0.22²)×10⁵×(250×10⁻⁶)⁴)/(16×160×10⁹×(2×10⁻⁶)³)
w_max ≈ 360 nm

ΔC/C₀ = 360×10⁻⁹/2×10⁻⁶ = 0.18 = 18%
```

**Fabrication:**

```
1. PSG sacrificial layer (2 μm)
2. Etch access holes
3. LPCVD poly-Si membrane (2 μm)
4. Pattern membrane
5. Release in HF
6. Seal access holes (LPCVD oxide, 500 nm)
7. Package (defines reference pressure)
```

**Performance:**

| Parameter | Value | Units |
|-----------|-------|-------|
| Range | 0-200 | kPa |
| Sensitivity | 0.1-1 | %/kPa |
| Accuracy | ±0.1 | % full scale |
| Temperature range | -40 to 125 | °C |

**Design Trade-offs:**

```
Sensitivity vs. Linearity:
- Thin membrane → high sensitivity, nonlinear
- Thick membrane → low sensitivity, linear

Solution: Bossed membrane
- Thick center (stiffness)
- Thin rim (compliance)
- Optimizes both
```

## RF MEMS

### Capacitive Shunt Switch

**Structure:**

```
Bridge:
- Length: 200 μm
- Width: 100 μm  
- Thickness: 2 μm
- Height (up-state): 3 μm

Transmission line:
- CPW (coplanar waveguide)
- Gold, 2 μm thick
- 50 Ω impedance
```

**Operating Principle:**

```
Up-state: Bridge suspended, RF passes (low C)
Down-state: Bridge pulled down, RF shorted (high C)

Actuation:
V_pull-in = √(8kg₀³/27ε₀A)

For k = 10 N/m, g₀ = 3 μm, A = 2×10⁻⁸ m²:
V_pull-in ≈ 35 V
```

**RF Performance:**

```
Insertion loss (up-state):
IL = -20log₁₀|S₂₁| < 0.5 dB @ 10 GHz

Isolation (down-state):
ISO = -20log₁₀|S₂₁| > 20 dB @ 10 GHz

Switching time:
t_switch = 3.67/ω₀ = 3.67√(m/k)
t_switch ≈ 5-20 μs
```

**Fabrication:**

```
1. CPW on substrate (Au, 2 μm)
2. Sacrificial layer (polyimide, 3 μm)
3. Seed layer (Ti/Au, 100 nm)
4. Electroplate Au bridge (2 μm)
5. Pattern bridge
6. Release (O₂ plasma)
7. FDTS coating (anti-stiction)
```

**Key Specifications:**

| Parameter | Value | Units |
|-----------|-------|-------|
| Frequency | DC-40 | GHz |
| Insertion loss | <0.5 | dB |
| Isolation | >20 | dB |
| Actuation voltage | 20-80 | V |
| Switching time | 5-20 | μs |
| Power handling | 0.1-1 | W |
| Lifetime | 10⁹-10¹² | cycles |

**Reliability Issues:**

1. **Dielectric Charging**: Trapped charge shifts V_pull-in
   - Solution: Charge-free dielectrics, AC actuation

2. **Contact Resistance Degradation**: Surface contamination
   - Solution: Hermetic packaging, noble metals

3. **Creep**: Time-dependent deformation
   - Solution: High-stiffness designs

## Optical MEMS

### Micromirror for Digital Light Processing (DLP)

**Design:**

```
Mirror:
- Size: 10.8 × 10.8 μm² (1080p pixel)
- Material: Al coating on poly-Si
- Thickness: 500 nm Al on 1 μm poly-Si

Torsion hinges:
- Length: 8 μm
- Width: 1 μm
- Thickness: 500 nm

Rotation: ±12° (digital, two stable states)
```

**Electrostatic Actuation:**

```
Torque balance:
τ_electrostatic = τ_mechanical

τ_elec = (1/2)(∂C/∂θ)V²

τ_mech = κθ

Where:
κ = torsional spring constant
θ = rotation angle

For bistable operation:
- Mechanical stops at ±12°
- Latching mechanism
- Low hold voltage
```

**Fabrication (Texas Instruments Process):**

```
1. CMOS circuitry (substrate)
2. Sacrificial layers (3 layers)
3. Hinge layer (poly-Si, 500 nm)
4. Mirror support posts
5. Mirror layer (poly-Si + Al)
6. Pattern all layers
7. Release (vapor HF or plasma)
8. Package with window
```

**Performance:**

| Parameter | Value | Units |
|-----------|-------|-------|
| Mirror size | 5-14 | μm |
| Rotation angle | ±12 to ±17 | degrees |
| Switching time | 10-20 | μs |
| Contrast ratio | >2000:1 | |
| Lifetime | >10¹⁵ | cycles |
| Reflectivity | >90 | % |

**Applications:**
- Digital projectors (DLP)
- Optical cross-connects
- Adaptive optics
- Beam steering

### 2D Scanning Mirror

**For laser scanning (LIDAR, displays):**

```
Design:
- Mirror: 1 × 1 mm²
- 2 axes of rotation
- Inner axis: fast (kHz)
- Outer axis: slow (Hz)

Actuation:
- Electrostatic comb drives
- Resonant drive for fast axis
- DC for slow axis
```

**Scan Parameters:**

```
Fast axis:
- Frequency: 20 kHz
- Amplitude: ±15°
- Q-factor: 100-500

Slow axis:
- Frequency: 60 Hz
- Amplitude: ±20°
- Q-factor: 10-50

Optical scan angle: 2θ_mech
```

## Design Guidelines Summary

### General Principles

**Mechanical Design:**
```
1. Minimize mass (faster response, lower damping)
2. Optimize stiffness (control resonance)
3. Symmetry (cancel unwanted modes)
4. Adequate stiffness against stiction
5. Include test structures
```

**Electrical Design:**
```
1. Differential sensing (noise rejection)
2. Guard rings (parasitic reduction)
3. Shielding (EMI protection)
4. On-chip reference capacitors
5. ESD protection
```

**Fabrication Considerations:**
```
1. Process compatibility
2. Stress management
3. Release strategy
4. Anti-stiction measures
5. Packaging requirements
```

### Scaling Effects

As devices shrink, dominant forces change:

| Force Type | Scaling | Impact |
|------------|---------|--------|
| Inertial | L³ | Decreases rapidly |
| Elastic | L | Decreases slowly |
| Electrostatic | L² | Medium decrease |
| Surface | L² | Becomes dominant |

**Implications:**
- Small devices: Surface forces dominate (stiction)
- Large devices: Inertial forces dominate (slow)
- Optimal size: 10-1000 μm range

## Manufacturing Considerations

### Yield Enhancement

**Design for Manufacturing:**
```
1. Generous spacing (avoid shorts)
2. Rounded corners (reduce stress)
3. Dummy fill structures (CMP uniformity)
4. Test structures on each die
5. Process monitors
```

**Common Yield Limiters:**
- Release stiction (40-60% of failures)
- Particle contamination (20-30%)
- Pattern defects (10-20%)
- Packaging issues (5-10%)

### Cost Reduction Strategies

```
1. Standard CMOS-compatible process
2. Minimize mask layers (4-6 typical)
3. Batch fabrication (wafer-level)
4. Self-test capability (reduce test time)
5. Simple packaging (standard IC packages)
```

**Cost Breakdown (per die):**
- Fabrication: 40-60%
- Testing: 20-30%
- Packaging: 20-30%
- Overhead: 10-20%

## Future Trends

### Integration

**CMOS-MEMS Co-fabrication:**
- Monolithic integration
- Post-CMOS MEMS modules
- Through-silicon vias (3D)

**Multi-functional Devices:**
- 6-axis IMU (3-axis accel + 3-axis gyro)
- Environmental sensors (P, T, humidity)
- Single-chip solutions

### Materials

**Beyond Silicon:**
- Piezoelectric (AlN, PZT) for actuation
- Diamond for extreme environments
- Graphene for ultra-sensitive sensors

### Applications

**Emerging Markets:**
- Medical diagnostics (lab-on-chip)
- Energy harvesting
- Quantum sensing
- Bio-interfaces

## References

1. Yazdi, N., Ayazi, F., & Najafi, K. (1998). Micromachined inertial sensors. *Proceedings of the IEEE*, 86(8), 1640-1659.

2. Xie, H., & Fedder, G. K. (2002). Integrated microelectromechanical gyroscopes. *Journal of Aerospace Engineering*, 16(2), 65-75.

3. Nguyen, C. T. C. (2007). MEMS technology for timing and frequency control. *IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control*, 54(2), 251-270.

4. Rebeiz, G. M. (2003). *RF MEMS: Theory, Design, and Technology*. Wiley.

5. Hornbeck, L. J. (1998). Digital light processing for high-brightness, high-resolution applications. *Electronic Imaging*, 3013, 27-40.

6. Van Spengen, W. M. (2003). MEMS reliability from a failure mechanisms perspective. *Microelectronics Reliability*, 43(7), 1049-1060.

---

**Document Information:**
- **Created:** December 10, 2025
- **Version:** 1.0
- **Status:** Complete
- **Part of:** Silicon Fabrication Handbook
- **Previous Chapter:** [Stiction Prevention](stiction-prevention.md)
- **Next Section:** [MEMS Bulk Micromachining](../05-mems-bulk-micromachining/)

**License:** CC BY 4.0 - Free to use with attribution

---

*For questions, corrections, or contributions, please visit:*
https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook

**Contact**: 
- GitHub: [@Zeyad-Mustafa](https://github.com/Zeyad-Mustafa)
-Linkedin: [@Zeyad_Mustafa] (https://www.linkedin.com/in/zeyad-mustafa-905793ab/)
