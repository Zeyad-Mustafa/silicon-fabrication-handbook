# Integration Strategies for MEMS-CMOS

## Table of Contents
- [Introduction](#introduction)
  - [Benefits of Integration](#benefits-of-integration)
  - [Market Drivers](#market-drivers)
- [Integration Approaches](#integration-approaches)
  - [Monolithic Integration](#monolithic-integration)
  - [Multi-Chip Module (MCM)](#multi-chip-module-mcm)
  - [3D Integration (Vertical Stack)](#3d-integration-vertical-stack)
- [Process Compatibility](#process-compatibility)
  - [Thermal Budget](#thermal-budget)
  - [Material Compatibility](#material-compatibility)
  - [Chemical Compatibility](#chemical-compatibility)
- [Design Considerations](#design-considerations)
  - [Interface Circuits](#interface-circuits)
  - [Layout Considerations](#layout-considerations)
  - [Packaging Requirements](#packaging-requirements)
- [Commercial Examples](#commercial-examples)
  - [Accelerometers](#accelerometers)
  - [Gyroscopes](#gyroscopes)
  - [Pressure Sensors](#pressure-sensors)
  - [Inertial Measurement Units (IMU)](#inertial-measurement-units-imu)
- [Trade-offs Analysis](#trade-offs-analysis)
  - [Performance vs Cost](#performance-vs-cost)
  - [Volume Economics](#volume-economics)
  - [Technology Maturity](#technology-maturity)
- [Future Trends](#future-trends)
  - [Advanced Integration](#advanced-integration)
  - [AI/ML Integration](#aiml-integration)
- [Best Practices](#best-practices)
  - [Selection Criteria](#selection-criteria)
  - [Common Mistakes ✗](#common-mistakes)
- [References](#references)

## Introduction

MEMS-CMOS integration combines micromechanical sensors/actuators with signal conditioning electronics on the same chip or package, enabling complete system-on-chip (SoC) or system-in-package (SiP) solutions.

### Benefits of Integration

**Performance Advantages:**

| Benefit | Impact | Quantification |
|---------|--------|----------------|
| Reduced parasitic capacitance | Higher sensitivity | 10-100× less capacitance |
| Shorter interconnects | Lower noise | 5-20× SNR improvement |
| Matched impedance | Better signal integrity | <1 pF vs 5-20 pF external |
| Temperature tracking | Better stability | TCO reduced 50-80% |
| Faster response | Higher bandwidth | 10-100× faster signal path |

**System Advantages:**

```
Size reduction:
- Discrete: 10-50 mm² PCB area
- Integrated: 2-10 mm² die area
- Reduction: 5-10× smaller

Cost reduction:
- Fewer components (1 vs 3-5)
- Fewer assembly steps
- Higher yield (no interconnects)
- Typical: 30-60% lower system cost

Reliability improvement:
- Fewer solder joints
- Shorter signal paths
- Better thermal matching
- 2-5× better MTTF
```

### Market Drivers

**Application Requirements:**

```
Consumer electronics:
- Smartphones: Accelerometer, gyroscope, pressure
- Wearables: IMU, heart rate, pressure
- Earbuds: Accelerometer, pressure

Automotive:
- TPMS (tire pressure): Pressure, temperature
- Airbag: Accelerometer, gyroscope
- Stability control: IMU (6-axis)

Industrial/IoT:
- Condition monitoring: Accelerometer
- Environmental sensing: Pressure, humidity
- Asset tracking: IMU

Medical:
- Continuous monitoring: Pressure, flow
- Implantables: Pressure, acceleration
- Diagnostics: Lab-on-chip
```

## Integration Approaches

### Monolithic Integration

**MEMS and CMOS on Same Die:**

```
Advantages:
+ Best electrical performance
+ Smallest size
+ Lowest parasitic capacitance (<0.5 pF)
+ Best temperature tracking
+ Single die handling and test

Disadvantages:
- Process complexity (30-50 masks)
- Lower CMOS performance (process constraints)
- Lower MEMS performance (thermal budget)
- Long development time (2-4 years)
- High NRE cost ($2M-10M)

Best for:
- High volume (>10M units/year)
- Performance-critical applications
- Mature products (long lifetime)
```

**Integration Sequence:**

```
1. CMOS-First:
   Complete CMOS → MEMS post-processing
   
   Flow:
   ├─ Standard CMOS (front-end)
   ├─ Standard CMOS (back-end, partial)
   ├─ MEMS release (post-CMOS)
   └─ Final passivation and metallization
   
   Advantages:
   - Protect CMOS during MEMS processing
   - Standard CMOS process
   - Better CMOS performance
   
   Disadvantages:
   - MEMS thermal budget limited (<450°C)
   - MEMS process must not damage CMOS
   
   Used by: Bosch, STMicroelectronics

2. MEMS-First:
   Complete MEMS → CMOS on top
   
   Flow:
   ├─ MEMS structures (buried)
   ├─ Seal/planarize MEMS
   ├─ Standard CMOS on top
   └─ Open MEMS (if needed)
   
   Advantages:
   - No thermal budget limit for MEMS
   - MEMS fully optimized
   - CMOS process unmodified
   
   Disadvantages:
   - MEMS must survive CMOS thermal cycles (1000°C)
   - Planarization challenges
   - Limited MEMS access
   
   Used by: Analog Devices

3. Interleaved:
   Alternating CMOS and MEMS steps
   
   Flow:
   ├─ CMOS front-end
   ├─ MEMS layers (within BEOL)
   ├─ CMOS back-end (around MEMS)
   └─ MEMS release (final step)
   
   Advantages:
   - Optimize both CMOS and MEMS
   - Flexible design
   
   Disadvantages:
   - Most complex process
   - Highest development cost
   - Process interdependencies
   
   Used by: Advanced research
```

### Multi-Chip Module (MCM)

**Side-by-Side Dies:**

```
Configuration:
MEMS die + CMOS die on common substrate

Connection methods:
1. Wire bonding (most common)
2. Flip chip (higher performance)
3. Through-silicon vias (TSV, 3D)

Advantages:
+ Independent optimization (best MEMS + best CMOS)
+ Mature processes (no development)
+ Fast time to market (6-12 months)
+ Lower NRE ($100K-500K)
+ Die yield independent
+ Mix and match (multiple suppliers)

Disadvantages:
- Larger size (2-3× monolithic)
- Higher parasitic capacitance (2-10 pF)
- More assembly steps
- Temperature mismatch possible

Best for:
- Medium volume (100K-10M/year)
- Quick time to market
- Technology demonstration
- Multiple MEMS + CMOS options
```

**Typical Configuration:**

```
Package structure:

    ┌──────────────────────┐
    │  Package/Cap         │
    ├──────────────────────┤
    │  MEMS  │   CMOS      │  ← Dies on substrate
    │  Die   │   ASIC      │
    ├────────┴─────────────┤
    │  Substrate/Leadframe │
    └──────────────────────┘

Interconnect:
- Wire bonds: 25-50 μm Au/Al wire
- Bond length: 1-3 mm
- Capacitance: 0.2-0.5 pF per mm
- Total: 2-5 pF typical

Performance impact:
- SNR: 5-10× worse than monolithic
- Still adequate for most applications
```

### 3D Integration (Vertical Stack)

**Stacked Dies with TSV:**

```
Configuration:
MEMS die stacked on top of CMOS die
Connected via through-silicon vias (TSV)

Types:
1. Wafer-to-wafer bonding:
   - Bond full wafers, then dice
   - Best alignment (<1 μm)
   - Highest throughput
   
2. Die-to-wafer bonding:
   - Known good die on wafer
   - Better yield
   - Moderate alignment (2-5 μm)
   
3. Die-to-die bonding:
   - Individual die stacking
   - Maximum flexibility
   - Lower alignment (5-10 μm)

Advantages:
+ Smallest footprint (same as single die)
+ Short interconnects (<50 μm via TSV)
+ Low capacitance (0.1-0.5 pF)
+ Excellent electrical performance
+ Independent process optimization

Disadvantages:
- Complex process (TSV, thinning, bonding)
- High cost (equipment, yield)
- Thermal management challenges
- Limited availability (few fabs)

Best for:
- High-end applications (aerospace, medical)
- Maximum performance required
- Small form factor critical
```

**TSV Specifications:**

```
Typical TSV:
- Diameter: 5-10 μm
- Depth: 50-100 μm (through MEMS die)
- Pitch: 20-50 μm
- Aspect ratio: 5:1 to 10:1

Electrical:
- Resistance: 50-200 mΩ per via
- Capacitance: 50-200 fF per via
- Inductance: ~10 pH

Process:
- Via etch: DRIE (Bosch process)
- Isolation: Thermal oxide (0.5-1 μm)
- Seed layer: Ti/Cu (50/200 nm)
- Fill: Cu electroplating
- CMP: Planarization

Cost: +$50-200 per wafer (depending on volume)
```

## Process Compatibility

### Thermal Budget

**Critical Issue:** CMOS metal cannot exceed ~450°C

```
Process temperature limits:

Standard CMOS:
- Front-end (transistors): 900-1100°C
- Silicidation: 850-1000°C
- Backend (Al metal): <450°C
- Cu metallization: <400°C

MEMS processes:
- Polysilicon deposition: 585-620°C
- Doping anneal: 900-1100°C
- Oxide deposition (LPCVD): 400-800°C
- Nitride deposition: 700-900°C

Compatibility strategies:

1. Low-temperature MEMS (<450°C):
   - PECVD instead of LPCVD
   - Surface micromachining only
   - Sacrificial polymers
   - Plasma doping (no high-temp anneal)
   
2. Pre-metal MEMS (before BEOL):
   - MEMS structures in FEOL
   - High-temperature allowed
   - Metal added after MEMS
   
3. Protected metallization:
   - Tungsten plugs (survive 1000°C)
   - Refractory metal barriers
   - Localized heating (laser annealing)
```

### Material Compatibility

**Common Materials Matrix:**

| Material | CMOS Use | MEMS Use | Compatibility |
|----------|----------|----------|---------------|
| Silicon | Substrate, poly-Si gate | Structural | ✓ Excellent |
| SiO₂ | Gate oxide, ILD | Sacrificial, isolation | ✓ Excellent |
| Si₃N₄ | Passivation | Structural, etch stop | ✓ Excellent |
| Aluminum | Metallization | Structural (some) | ✓ Good (T<450°C) |
| Copper | Metallization | No | ⚠ Limited (T<400°C) |
| Tungsten | Plugs, local interconnect | Structural | ✓ Excellent |
| Polysilicon | Gate, resistor | Structural | ✓ Excellent |
| TiN | Barrier | Electrode | ✓ Good |

**Contamination Concerns:**

```
Cross-contamination risks:

Heavy metals (Cu, Fe, Ni):
- CMOS: Catastrophic (minority carrier lifetime killer)
- Prevention: Dedicated MEMS tools
            : Barrier layers (TiN, Ta)
            : Clean protocols

Particles:
- MEMS: Critical (stiction, reliability)
- CMOS: Critical (shorts, gate oxide integrity)
- Prevention: Cleanroom Class 1-10
            : In-situ cleaning
            : Wet cleaning between steps

Mobile ions (Na, K):
- CMOS: Threshold voltage shift
- MEMS: Charging, drift
- Prevention: Avoid glass substrates
            : Clean chemicals
            : Gettering (phosphorus glass)
```

### Chemical Compatibility

**Etchants and CMOS:**

```
HF (for oxide removal):
- Attacks SiO₂ (desired)
- Attacks Al metallization (problem!)
- Solution: Protect Al with resist
          : Use alternative (BOE slower)
          : Cu compatible (if Cu BEOL)

KOH (for bulk Si etch):
- Attacks Al aggressively
- Attacks SiO₂ slowly
- Solution: Si₃N₄ hard mask
          : No exposed Al
          : Post-CMOS only if protected

TMAH (alternative to KOH):
- CMOS compatible (less Al attack)
- Still attacks Al over time
- Preferred for post-CMOS

XeF₂ (silicon vapor etch):
- Highly selective to metals
- CMOS compatible
- Expensive
- Good for release with metallization present
```

## Design Considerations

### Interface Circuits

**MEMS Output to CMOS Input:**

```
Capacitive sensor:
- MEMS: 0.1-10 pF variable capacitor
- CMOS: Charge amplifier or C-to-V converter

Piezoresistive sensor:
- MEMS: 1-10 kΩ resistor, 1-10% change
- CMOS: Wheatstone bridge + instrumentation amp

Resonant sensor:
- MEMS: Resonator, 10 kHz to 10 MHz
- CMOS: Oscillator circuit, PLL

Typical interface specs:
- Input capacitance: <1 pF (CMOS input)
- Input resistance: >1 GΩ (to avoid loading)
- Noise: <10 nV/√Hz (amplifier)
- Bandwidth: Match MEMS (1-10 kHz typical)
```

**Circuit Examples:**

```
1. Charge Integrator (capacitive):
   
   C_sense (MEMS) → [Op-amp integrator] → V_out
   
   V_out = Q / C_feedback
        = (C_sense × V_bias) / C_feedback
   
   Design:
   - C_feedback: 1-10 pF
   - Reset switch: Periodic discharge
   - Correlated double sampling (CDS) for offset

2. Switched Capacitor Amplifier:
   
   Gain = C_sense / C_feedback
   Noise = kT/C_feedback
   
   Advantage: High gain, low offset
   Typical gain: 10-100×

3. Continuous-Time Interface:
   
   MEMS → Buffer → Amplifier → ADC
   
   Buffer: Source follower, low input C
   Gain: 20-60 dB
   Filter: Anti-aliasing before ADC
```

### Layout Considerations

**Floorplan:**

```
Monolithic integration:

Option 1 - Side-by-side:
┌──────────────────────┐
│  MEMS     │  CMOS    │
│  Sensor   │  ASIC    │
│           │          │
└──────────────────────┘

Advantages:
- Independent optimization
- No overlay alignment critical
- Easy to modify

Disadvantages:
- Larger die area
- Longer interconnect

Option 2 - CMOS under MEMS:
┌──────────────────────┐
│     MEMS Sensor      │
│   (released above)   │
├──────────────────────┤
│   CMOS Circuitry     │
│   (underneath)       │
└──────────────────────┘

Advantages:
- Smaller die area
- Shorter interconnect

Disadvantages:
- CMOS must survive MEMS release
- Thermal dissipation challenges
- Limited CMOS area

Option 3 - Perimeter MEMS:
┌──────────────────────┐
│ M │              │ M │
│ E │     CMOS     │ E │
│ M │              │ M │
│ S │              │ S │
└──────────────────────┘

Used for: Multiple MEMS devices (IMU)
```

**Pad Placement:**

```
Separate pads by function:
- MEMS bias: Low noise, stable
- Analog supply: Clean, regulated
- Digital supply: Noisy, can toggle
- Ground: Multiple, star configuration

Pad assignment priority:
1. MEMS sense outputs (minimize C)
2. MEMS drive inputs (clean signals)
3. Analog power (low noise)
4. Digital I/O (separated from analog)
5. Digital power (most tolerant)

Guard rings:
- Around MEMS capacitive sensors
- Around sensitive analog circuits
- Reduce substrate noise coupling
```

### Packaging Requirements

**MEMS-Specific Needs:**

```
Environmental access:
- Pressure sensor: Vent hole required
- Accelerometer: Sealed, no vent
- Gyroscope: Vacuum or controlled atmosphere
- Microphone: Acoustic port

Protection:
- Die coating: Parylene, silicone gel
- Vent protection: Membrane, filter
- Contamination: Hermetic seal (if needed)

Stress isolation:
- Soft die attach (pressure sensors)
- Stress relief (all MEMS)
- CTE matching: Die, package, PCB

Electrical:
- Low-capacitance leads (<1 pF)
- Shielding (for low-level signals)
- Multiple grounds (analog/digital)
```

## Commercial Examples

### Accelerometers

**Analog Devices ADXL series:**

```
Technology: Surface micromachining, CMOS-first
Process: 5-6 μm BiCMOS + MEMS post-process

Structure:
- Polysilicon proof mass (2-3 μm thick)
- Differential capacitive sensing
- CMOS amplifier and ADC on same die

Performance:
- Range: ±2g to ±16g
- Noise: 150 μg/√Hz
- Bandwidth: 1600 Hz
- Supply: 2.0-3.6V
- Current: 140 μA

Die size: ~3×3 mm (varies by model)
Package: LGA, size: 3×3×1 mm
Cost: $1-3 in volume

Key feature: Self-test capability (electrostatic)
```

**Bosch BMA series:**

```
Technology: Surface micromachining, CMOS-first
Process: Proprietary process

Structure:
- Closed-loop force-feedback
- Capacitive sensing
- Integrated oscillator

Performance:
- Range: ±2g to ±16g
- Noise: 120 μg/√Hz
- Power: 130 μA normal, 3 μA suspend
- Interface: I²C, SPI

Die size: ~2×2 mm
Package: LGA, 2×2×0.65 mm
Cost: $0.50-1.50

Key feature: Ultra-low power for wearables
```

### Gyroscopes

**STMicroelectronics L3GD20:**

```
Technology: THELMA (Thick Epipoly Layer for MEMs Accelerometers & gyros)
Integration: Monolithic (MEMS + CMOS)

Structure:
- Tuning fork resonator
- Drive mode: 30 kHz
- Coriolis sensing (perpendicular)

Performance:
- Range: ±250/500/2000 dps
- Sensitivity: 8.75-70 mdps/digit
- Noise: 0.03 dps/√Hz
- Zero-rate level: ±10 dps

Die size: ~4×4 mm
Package: LGA, 4×4×1 mm
Interface: I²C/SPI, 16-bit output

Key feature: 3-axis gyroscope + temperature sensor
```

### Pressure Sensors

**Bosch BMP280:**

```
Technology: Surface micromachining
Integration: Monolithic (MEMS + ASIC)

Structure:
- Suspended membrane (piezoresistive)
- Wheatstone bridge
- On-chip calibration data
- Temperature sensor

Performance:
- Range: 300-1100 hPa
- Accuracy: ±1 hPa (±8.5 m altitude)
- Resolution: 0.16 Pa (13 cm altitude)
- Power: 2.7 μA @ 1 Hz

Die size: ~2×2 mm
Package: LGA, 2×2.5×0.95 mm
Interface: I²C, SPI

Application: Smartphones (altitude, weather)
Cost: $0.80-1.50

Key feature: Ultra-low power, integrated ADC
```

### Inertial Measurement Units (IMU)

**InvenSense ICM-20602:**

```
Technology: 6-axis IMU (3-axis accel + 3-axis gyro)
Integration: Monolithic MEMS + separate CMOS die (MCM)

Structure:
- MEMS die: 3-axis gyroscope + 3-axis accelerometer
- ASIC die: Signal processing, ADC, digital filters

Performance:
Gyroscope:
- Range: ±250 to ±2000 dps
- Noise: 0.005 dps/√Hz
- Bias: ±10 dps

Accelerometer:
- Range: ±2g to ±16g
- Noise: 100 μg/√Hz

Package: QFN, 3×3×0.75 mm
Power: 0.9 mA (gyro + accel)
Interface: I²C, SPI

Application: Smartphones, gaming, robotics
Cost: $1-2

Key feature: Digital Motion Processor (DMP) on-chip
```

## Trade-offs Analysis

### Performance vs Cost

**Integration Level Comparison:**

```
Metric            | Discrete | MCM  | Monolithic | 3D Stack
------------------|----------|------|------------|----------
Parasitic C (pF)  | 10-50    | 2-5  | 0.2-0.5    | 0.1-0.3
SNR improvement   | 1×       | 3×   | 10×        | 15×
Size (mm²)        | 100-500  | 20-50| 4-20       | 4-15
NRE cost          | $50K     | $200K| $3M        | $5M
Unit cost (1M/yr) | $2-5     | $1-3 | $0.5-1.5   | $2-5
Time to market    | 6 mo     | 12 mo| 24-36 mo   | 36 mo
Yield             | 85-90%   | 90-95%| 85-90%    | 70-80%
```

### Volume Economics

**Break-Even Analysis:**

```
Example: Accelerometer product

Discrete solution:
- MEMS die: $0.30 (external vendor)
- ASIC die: $0.40 (standard cell)
- Package: $0.20 (2-die MCM)
- Assembly: $0.30
Total: $1.20 per unit

Monolithic solution:
- Combined die: $0.60 (larger, complex)
- Package: $0.15 (single die)
- Assembly: $0.20
Total: $0.95 per unit
Savings: $0.25 per unit

NRE difference: $3M - $200K = $2.8M

Break-even volume:
$2.8M / $0.25 = 11.2M units

Recommendation:
- Volume <10M/year: Use MCM
- Volume >15M/year: Monolithic
- Volume 10-15M: Case-by-case

Additional factors:
- Product lifetime (amortize NRE)
- Competitive advantage (performance)
- Strategic IP development
```

### Technology Maturity

**Readiness Level:**

| Approach | TRL | Availability | Risk |
|----------|-----|--------------|------|
| MCM (wire bond) | 9 | Universal | Low |
| Monolithic CMOS-first | 8-9 | Major foundries | Medium |
| Monolithic MEMS-first | 7-8 | Limited | Medium |
| 3D TSV stacking | 6-7 | Few fabs | High |
| Monolithic interleaved | 4-5 | Research | Very high |

**Foundry Availability:**

```
MEMS-CMOS integration foundries:

Tier 1 (High volume, proven):
- STMicroelectronics
- Bosch Sensortec
- TSMC (limited MEMS)

Tier 2 (Medium volume, specialized):
- X-FAB
- Teledyne DALSA
- Sony (image sensors + IMU)

Tier 3 (Research, prototyping):
- IMEC (Belgium)
- Fraunhofer (Germany)
- MIT Lincoln Labs (USA)

Lead time:
- Standard process: 3-6 months
- Process development: 12-24 months
- New technology node: 24-36 months
```

## Future Trends

### Advanced Integration

**Beyond Current State-of-Art:**

```
1. Monolithic Multi-MEMS:
   - 6-axis IMU + pressure + microphone
   - Single die, multiple MEMS types
   - Challenge: Process compatibility

2. MEMS-More-than-Moore:
   - MEMS + advanced CMOS (5nm, 3nm)
   - Heterogeneous integration
   - 3D stacking (MEMS + logic + memory)

3. Analog/RF co-integration:
   - MEMS resonators + RF circuits
   - On-chip antennas (MEMS switches)
   - Tunable filters

4. Photonics integration:
   - MEMS optical switches
   - MEMS + silicon photonics
   - Optical MEMS on CMOS

5. Flexible/stretchable:
   - MEMS on flexible substrates
   - Wearable/biomedical applications
```

### AI/ML Integration

**Intelligent Sensors:**

```
On-chip machine learning:
- Edge AI processing
- Sensor fusion algorithms
- Pattern recognition
- Anomaly detection

Architecture:
MEMS → Interface → ADC → DSP → ML Accelerator → Output

Examples:
- Voice recognition (microphone + ML)
- Gesture recognition (IMU + ML)
- Predictive maintenance (vibration + ML)
- Health monitoring (multi-sensor + ML)

Benefits:
- Reduced data transmission (privacy)
- Lower power (local processing)
- Faster response (no cloud latency)
- Always-on capability
```

## Best Practices

### Selection Criteria

```
✓ Start with clear requirements (performance, cost, volume)
✓ Evaluate technology readiness (proven vs cutting-edge)
✓ Consider time-to-market constraints
✓ Assess foundry availability and capability
✓ Plan for yield and test strategy
✓ Budget for NRE and prototyping
✓ Secure IP ownership and licensing
✓ Build in design margin (process variation)
✓ Consider second-source options
✓ Plan for product lifecycle (5-10 years)
```

### Common Mistakes ✗

```
✗ Over-optimizing (monolithic when MCM sufficient)
✗ Under-estimating development time
✗ Ignoring process compatibility issues
✗ Insufficient thermal budget planning
✗ Neglecting packaging constraints
✗ Poor yield planning (multiplicative not additive)
✗ Inadequate testing strategy
✗ Not protecting CMOS during MEMS release
✗ Forgetting about second-source / end-of-life
✗ Underestimating total cost of ownership
```

## References

1. Fedder, G. K., et al. (2008). Technologies for cofabricating MEMS and electronics. *Proceedings of the IEEE*, 96(2), 306-322.

2. Baltes, H., et al. (2005). CMOS-MEMS. *Wiley-VCH*.

3. Yazdi, N., et al. (1998). Micromachined inertial sensors. *Proceedings of the IEEE*, 86(8), 1640-1659.

4. Senturia, S. D. (2001). *Microsystem Design*. Springer.

5. Bustillo, J. M., et al. (1998). Surface micromachining for microelectromechanical systems. *Proceedings of the IEEE*, 86(8), 1552-1574.

---

**Document Information:**
- **Created:** December 25, 2025
- **Version:** 1.0
- **Status:** Complete
- **Part of:** Silicon Fabrication Handbook
- **Next Chapter:** [Monolithic Integration](monolithic-integration.md)
- **Section:** Integrated MEMS-CMOS

**License:** CC BY 4.0 - Free to use with attribution

---

*For questions, corrections, or contributions, please visit:*
https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook
