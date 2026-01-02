# Interface Circuits for MEMS-CMOS Integration

## Table of Contents
1. [Introduction](#introduction)
2. [Signal Conditioning Basics](#signal-conditioning-basics)
3. [Capacitive Interface Circuits](#capacitive-interface-circuits)
4. [Piezoresistive Interface Circuits](#piezoresistive-interface-circuits)
5. [Resonant MEMS Interfaces](#resonant-mems-interfaces)
6. [Actuation Drivers](#actuation-drivers)
7. [Noise and Performance](#noise-and-performance)
8. [Power Management](#power-management)
9. [Design Examples](#design-examples)

## Introduction

### Why Interface Circuits Matter

MEMS sensors produce small electrical signals that require careful amplification, filtering, and processing. Interface circuits bridge the gap between the MEMS transducer and digital processing:

**Key Functions**:
- **Amplification**: Boost weak MEMS signals (μV to V range)
- **Filtering**: Remove noise and interference
- **Conversion**: Analog-to-digital conversion
- **Calibration**: Offset and gain correction
- **Actuation**: Drive MEMS actuators with controlled signals

**Typical MEMS Signal Levels**:
```
Accelerometer (capacitive): 10-100 fF/g → 1-10 mV/g
Gyroscope (Coriolis): 1-10 aF/°/s → 10-100 μV/°/s
Pressure sensor (piezoresistive): 1-10 mV/kPa
Microphone: 10-50 mV/Pa (at 1 kHz)
```

### Interface Architecture Overview

```
┌─────────┐   ┌─────────┐   ┌──────┐   ┌─────┐   ┌────────┐
│  MEMS   │──▶│  Front  │──▶│ ADC  │──▶│ DSP │──▶│ Output │
│ Sensor  │   │   End   │   │      │   │     │   │        │
└─────────┘   └─────────┘   └──────┘   └─────┘   └────────┘
     ▲             │
     │        ┌────┴────┐
     └────────│ Driver  │ (for actuation/feedback)
              └─────────┘

Front End:
- Charge amplifier / Transimpedance amplifier
- Instrumentation amplifier
- Low-pass filter
- Programmable gain amplifier (PGA)
```

## Signal Conditioning Basics

### Key Performance Metrics

**Resolution**:
```
Smallest detectable signal change
= Noise Floor / Signal Range

Example:
Noise: 10 μg/√Hz
Bandwidth: 100 Hz
Total noise: 10 × √100 = 100 μg
Range: ±2g
Resolution: 100μg / 4g = 25 ppm = 15.6 bits
```

**Sensitivity**:
```
Output voltage change per unit input
S = ΔV_out / Δx_input

Capacitive accelerometer:
S = (V_bias × C_sens × G_amp) / (C_total × g)
  = (1.5V × 200fF/g × 1000) / (2pF × 1g)
  = 150 mV/g
```

**Bandwidth**:
```
Frequency range of operation
Typically: DC to 100 Hz (accelerometer)
           DC to 500 Hz (gyroscope)
           20 Hz to 20 kHz (microphone)
```

### Common Circuit Blocks

#### Operational Amplifiers

**Key Specifications**:
- **Offset voltage**: 50-500 μV (critical for DC signals)
- **Input bias current**: 1-100 pA
- **Noise**: 5-50 nV/√Hz
- **CMRR**: >80 dB at DC
- **Power**: 10-500 μW

**Chopper-Stabilized Op-Amps**:
```
Advantages:
- Ultra-low offset (<5 μV)
- Low 1/f noise
- High CMRR

Disadvantages:
- Chopping artifacts
- Higher power
- Limited bandwidth

Used for: DC-coupled sensors (pressure, temperature)
```

#### Analog-to-Digital Converters

**SAR ADC** (Successive Approximation):
- **Resolution**: 10-16 bits
- **Sample rate**: 100 kSPS - 5 MSPS
- **Power**: 100 μW - 10 mW
- **Use**: General-purpose MEMS readout

**Sigma-Delta (ΣΔ) ADC**:
- **Resolution**: 16-24 bits
- **Sample rate**: 1-1000 SPS
- **Power**: 50 μW - 5 mW
- **Use**: High-resolution DC measurements

**Pipeline ADC**:
- **Resolution**: 8-14 bits
- **Sample rate**: 10-100 MSPS
- **Power**: 10-100 mW
- **Use**: Fast sampling (high-g accelerometers)

## Capacitive Interface Circuits

### Charge Amplifier

The most common front-end for capacitive MEMS sensors.

**Basic Circuit**:
```
         C_MEMS
    ──────||──────┐
                  │
    V_bias ───────┤
                  │    C_f
                  │  ──||──
                  │  ┌────┐
                  └──┤-   │
                     │  A │──── V_out
    V_ref ───────────┤+   │
                     └────┘
                     Op-Amp

V_out = -V_bias × (ΔC_MEMS / C_f)
```

**Design Equations**:
```
Sensitivity:
S = V_bias / C_f

Noise:
V_n = √(kT/C_f) × √(1 + C_MEMS/C_f)

Example:
C_f = 1 pF
C_MEMS = 2 pF (nominal)
ΔC = 100 fF (signal)
V_bias = 1.5 V

V_out = -1.5 × (100fF / 1pF) = -150 mV
Noise = √(1.38×10⁻²³ × 300 / 10⁻¹²) × √3
      = 203 μV × 1.73 = 351 μV
SNR = 150mV / 351μV = 428 = 52.6 dB
```

**Practical Considerations**:
- **C_f selection**: Compromise between sensitivity and noise
- **Reset mechanism**: Periodic discharge to prevent saturation
- **Parasitic capacitance**: Minimize C_par at input node
- **Bias voltage**: Higher V_bias improves SNR but affects MEMS

### Switched-Capacitor Interface

For differential capacitive sensors (common in accelerometers/gyroscopes).

**Operating Principle**:
```
Phase 1 (φ1): Charge C_MEMS to V_bias
Phase 2 (φ2): Transfer charge to C_f

Switched-capacitor gain:
G = (C_MEMS / C_f) × f_clk

Typical:
f_clk = 100 kHz to 1 MHz
C_MEMS = 1-5 pF
C_f = 100-500 fF
G = 10-100× voltage gain
```

**Advantages**:
- No DC path (eliminates offset)
- Programmable gain (by changing f_clk)
- Inherent anti-aliasing
- Compatible with ΣΔ ADCs

**Disadvantages**:
- Clock feedthrough
- Charge injection
- kT/C noise
- More complex layout

### Continuous-Time Interface

**Transimpedance Amplifier (TIA)**:
```
Used for current-output capacitive sensors

         C_MEMS
    ──────||──────┐
                  │ i_sens
    V_bias ───────┤
                  │    R_f
                  │  ──────
                  │  ┌────┐
                  └──┤-   │
                     │  A │──── V_out
    GND ─────────────┤+   │
                     └────┘

i_sens = V_bias × ω × ΔC_MEMS
V_out = -i_sens × R_f
      = -V_bias × ω × ΔC_MEMS × R_f

At 1 kHz:
ω = 2π × 1000 = 6283 rad/s
ΔC = 100 fF
R_f = 10 MΩ
V_bias = 1.5 V

V_out = -1.5 × 6283 × 100×10⁻¹⁵ × 10×10⁶
      = -9.4 mV
```

### Capacitance-to-Digital Converter (CDC)

**Integrated CDC Architecture**:
```
Modern approach: Direct C-to-D conversion

┌──────────┐    ┌────────────┐    ┌──────┐
│  MEMS    │───▶│ Charge-to- │───▶│  ΣΔ  │───▶ Digital
│ C_sens   │    │ Voltage    │    │ ADC  │     Output
└──────────┘    └────────────┘    └──────┘
                      │
                 ┌────┴────┐
                 │ Clock   │
                 │ & Bias  │
                 └─────────┘

Example ICs:
- AD7746 (Analog Devices): 24-bit, 10 Hz update
- FDC2214 (Texas Instruments): 28-bit, 4-channel
```

**Performance**:
- **Resolution**: 20-28 bits (sub-aF resolution)
- **Update rate**: 10-4000 Hz
- **Power**: 0.5-5 mW
- **Interface**: I²C or SPI

## Piezoresistive Interface Circuits

### Wheatstone Bridge

Standard configuration for piezoresistive pressure sensors, strain gauges.

**Full Bridge Configuration**:
```
         R1            R2
    V+ ○─────┐    ┌─────○ V-
             │    │
         ┌───┴────┴───┐
         │            │
    V+ ──┤            ├── GND
         │            │
         └───┬────┬───┘
             │    │
    V- ○─────┘    └─────○ V+
         R3            R4

V_diff = V+ × (R2/(R1+R2) - R4/(R3+R4))

For balanced bridge with strain:
ΔR/R = ε × GF (GF = gauge factor ≈ 100-200)

V_diff ≈ V+ × (ΔR/R) = V+ × GF × ε
```

**Design Example**:
```
Pressure sensor:
R = 5 kΩ (nominal)
GF = 150
Strain ε = 0.001 (at full scale)
V+ = 5 V

ΔR = 5000 × 0.001 × 150 = 0.75 kΩ
V_diff = 5 × 150 × 0.001 = 0.75 V (at full scale)

Typical output: 10-100 mV/V (output per volt of excitation)
```

### Instrumentation Amplifier

Essential for amplifying differential bridge signals while rejecting common-mode noise.

**Three Op-Amp Configuration**:
```
             R_g
    ┌─────────────────┐
    │                 │
    │   ┌────┐   ┌────┐
V+ ─┴───┤+  1│   │+  3│
        │ A1 │   │ A3 │─── V_out
V- ─┬───┤-   │   │-   │
    │   └────┘   └────┘
    │      │   ┌────┐ │
    │      └───┤-  2│ │
    └──────────┤+   │─┘
               │ A2 │
               └────┘

Gain = (1 + 2R/R_g) × (R_3/R_2)

Typical:
R_g programmable: 100Ω to 100kΩ
Gain range: 1 to 1000×
CMRR: >100 dB
```

**Key Specifications**:
- **Input offset**: <50 μV
- **Drift**: <0.5 μV/°C
- **CMRR**: 80-120 dB
- **Noise**: 10-50 nV/√Hz
- **Power**: 100 μW - 5 mW

**Commercial ICs**:
- INA128 (Texas Instruments): G = 1-10000, 50 μV offset
- AD8221 (Analog Devices): Rail-to-rail, 25 μV offset
- LT1167 (Linear Technology): Low power, 100 μV offset

### Signal Chain Example

```
┌─────────┐  ┌──────┐  ┌─────┐  ┌──────┐  ┌─────┐
│ Bridge  │─▶│ INA  │─▶│ LPF │─▶│ PGA  │─▶│ ADC │─▶ Output
│ 10 mV/V │  │ G=10 │  │50 Hz│  │ G=4  │  │12bit│   (SPI)
└─────────┘  └──────┘  └─────┐  └──────┘  └─────┘
                             │
                        ┌────┴────┐
                        │ V_ref   │
                        │ Buffer  │
                        └─────────┘

Signal levels:
Bridge output: 50 mV (at 5V excitation, full scale)
After INA: 500 mV
After LPF: 500 mV (clean)
After PGA: 2000 mV = 2V
ADC: 2V / 3.3V × 4096 = 2482 counts

Resolution: 4096 counts / full_scale
          = 12 bits effective
```

## Resonant MEMS Interfaces

### Phase-Locked Loop (PLL)

Used for MEMS resonators (gyroscopes, oscillators) to maintain resonance and extract frequency.

**Closed-Loop Oscillator**:
```
┌─────────────┐
│    MEMS     │
│  Resonator  │ ω₀, Q
└──────┬──────┘
       │ Motion → Capacitance change
       ▼
  ┌─────────┐
  │ C-to-V  │ Sense
  │ (TIA)   │
  └────┬────┘
       │
       ▼
  ┌─────────┐
  │  AGC    │ Amplitude control
  │ (VGA)   │
  └────┬────┘
       │
       ▼
  ┌─────────┐
  │ Phase   │ π/2 shift for oscillation
  │ Shifter │
  └────┬────┘
       │
       └──────────────┐
                      ▼
               ┌──────────┐
               │  Drive   │ Electrostatic actuation
               │  Amp     │
               └────┬─────┘
                    │
                    └──▶ Back to MEMS

Oscillation condition:
- Loop gain = 1
- Phase shift = 2πn (or 360°)
```

**Frequency Detection**:
```
For gyroscope Coriolis detection:

f_drive = f₀ (resonant frequency, e.g., 10 kHz)
Ω = rotation rate

Output frequency:
f_sense = f_drive (but amplitude proportional to Ω)

Demodulation:
V_sense(t) × sin(2πf_drive × t) → DC component ∝ Ω
```

### Automatic Gain Control (AGC)

Maintains constant oscillation amplitude.

**Implementation**:
```
┌────────┐    ┌─────────┐    ┌──────┐
│ Signal │───▶│ Rectify │───▶│ LPF  │───┐
│        │    │         │    │      │   │
└────────┘    └─────────┘    └──────┘   │
                                         ▼
                                    ┌─────────┐
                                    │ Compare │
                                    │ to V_ref│
                                    └────┬────┘
                                         │
                                         ▼
                                    ┌─────────┐
                                    │  Error  │
                                    │   Amp   │
                                    └────┬────┘
                                         │
                                         ▼
                                    ┌─────────┐
                                    │   VGA   │──▶ Controlled output
                                    └─────────┘

Loop equation:
V_out = V_desired
Gain = V_ref / |V_sense|
```

**Settling Time**:
```
τ_AGC = 1 / (2π × f_AGC_bandwidth)

Typical:
f_AGC = 10-100 Hz (much slower than resonator)
τ_AGC = 1-10 ms
```

## Actuation Drivers

### Electrostatic Drivers

For capacitive MEMS actuators (mirrors, switches, varactors).

**High-Voltage Driver**:
```
┌──────────┐    ┌────────────┐    ┌─────────┐
│ Digital  │───▶│  DAC or    │───▶│   HV    │───▶ MEMS
│ Control  │    │  PWM       │    │ Amplif  │     Actuator
└──────────┘    └────────────┘    └─────────┘
                                      │
                                      ▼
                                  V_drive
                                  (10-100V)

Electrostatic force:
F = (ε₀ × A × V²) / (2 × d²)

Example:
A = 100 × 100 μm²
d = 2 μm (gap)
V = 50 V

F = (8.85×10⁻¹² × 10⁻⁸ × 2500) / (2 × 4×10⁻¹²)
  = 27.7 μN
```

**Charge Pump**:
```
For generating high voltage from low supply:

V_in = 3.3 V
V_out = 50 V (15× boost)

Efficiency: 60-85%
Output current: 1-100 μA (sufficient for capacitive load)
Ripple: <100 mV

Used in: MEMS mirrors, RF switches, tunable capacitors
```

### Electromagnetic Drivers

For magnetic MEMS (actuators with coils).

**H-Bridge Driver**:
```
         V+
          │
      ┌───┴───┐
      │  Q1   │  Q2
      └───┬───┴───┬───┐
          │       │   │
       ┌──┴──┐ ┌──┴──┐│
  Out+ │     │ │     ││ Out-
       └──┬──┘ └──┬──┘│
          │       │   │
      ┌───┴───┬───┴───┘
      │  Q3   │  Q4
      └───┬───┘
          │
         GND

Coil current:
I = V_drive / R_coil

PWM control:
I_avg = I_max × duty_cycle
Frequency: 20-100 kHz
```

**Current Control**:
```
For precise force control:

I_set ─▶ ┌──────────┐
         │ Current  │
         │ Sense    │
         └────┬─────┘
              │
              ▼
         ┌──────────┐    ┌─────────┐
         │ Error    │───▶│  PWM    │───▶ H-Bridge
         │ Amplif   │    │  Gen    │
         └──────────┘    └─────────┘

Sense resistor: 0.1-1 Ω
Current range: 10-500 mA
Accuracy: ±1%
```

### Thermal Drivers

For thermal MEMS actuators (thermal microgrippers, optical switches).

**Resistive Heater Driver**:
```
Power = V² / R_heater

Temperature rise:
ΔT = P × R_thermal

Example:
R_heater = 100 Ω
V_drive = 5 V
P = 25 / 100 = 250 mW

R_thermal = 200 °C/W (typical for microheater)
ΔT = 250mW × 200 = 50°C

Response time: 1-10 ms (thermal time constant)
```

## Noise and Performance

### Noise Sources

**Thermal Noise (Johnson-Nyquist)**:
```
v_n = √(4kTRΔf)

For R = 10 kΩ, T = 300K, Δf = 100 Hz:
v_n = √(4 × 1.38×10⁻²³ × 300 × 10⁴ × 100)
    = 4.08 μV RMS
```

**1/f Noise (Flicker)**:
```
v_n,1/f = K_f / √f

Dominates below corner frequency:
f_c = 100 Hz to 10 kHz (depends on device)

Mitigation:
- Chopper stabilization
- AC coupling (if possible)
- Larger devices (lower K_f)
```

**Quantization Noise**:
```
For N-bit ADC:

V_LSB = V_ref / 2^N
Q_noise = V_LSB / √12

12-bit ADC, V_ref = 3.3V:
V_LSB = 3.3 / 4096 = 0.806 mV
Q_noise = 0.233 mV RMS
ENOB ≈ 11.5 bits (accounting for real ADC nonidealities)
```

### Total Noise Budget

```
v_n,total = √(v_n,thermal² + v_n,1/f² + v_n,shot² + v_n,quant²)

Example signal chain:
- Sensor: 1 μV RMS
- Amplifier: 2 μV RMS
- Filter: 0.5 μV RMS
- ADC: 10 μV RMS

Total: √(1² + 2² + 0.5² + 10²) = 10.3 μV RMS
```

### Dynamic Range

```
DR = 20 × log₁₀(V_max / V_noise)

Example:
V_max = 2V (full scale)
V_noise = 10 μV RMS

DR = 20 × log₁₀(2 / 10×10⁻⁶)
   = 20 × log₁₀(200,000)
   = 106 dB
```

## Power Management

### Supply Regulation

**Low-Dropout Regulator (LDO)**:
```
V_in ───┐
        ▼
   ┌─────────┐
   │   LDO   │
   │ 3.3V→1.8V│
   └────┬────┘
        │
        ▼
   Analog supply (clean, low noise)

Key specs:
- Dropout: 100-300 mV
- PSRR: 60-80 dB @ 1 kHz
- Noise: 10-50 μVRMS
- Quiescent current: 10-100 μA
```

### Power Consumption

**Typical MEMS Interface Power Budget**:
```
Component             Power
─────────────────────────────
MEMS sensor           10-100 μW
Bias generation       50-200 μW
Front-end amplifier   100-500 μW
Filter                50-200 μW
ADC                   100-1000 μW
Digital logic         50-500 μW
Reference             10-50 μW
─────────────────────────────
Total                 370-2550 μW

Average: ~1 mW (typical consumer MEMS)
```

**Low-Power Techniques**:
- Duty cycling (power down between samples)
- Clock gating
- Dynamic voltage scaling
- Subthreshold operation
- Power-optimized bias currents

## Design Examples

### Example 1: Accelerometer Interface (Capacitive)

**Specifications**:
- Range: ±2g
- Sensitivity: 100 fF/g
- Noise: <100 μg/√Hz
- Bandwidth: DC to 100 Hz
- Supply: 1.8V

**Solution**:
```
1. Charge amplifier:
   C_f = 1 pF
   V_bias = 1.5 V
   V_out/g = 1.5 × 100fF / 1pF = 150 mV/g

2. Noise:
   kT/C noise = √(kT/C_f) = 64 μV RMS
   Equivalent to: 64μV / 150mV/g = 0.43 mg = 430 μg
   
3. Over 100 Hz BW:
   Noise density = 430μg / √100 = 43 μg/√Hz ✓

4. Following stages:
   - 2nd order LPF (Butterworth, fc=100Hz)
   - PGA with G=2-8 (programmable)
   - 12-bit SAR ADC
```

### Example 2: Pressure Sensor Interface (Piezoresistive)

**Specifications**:
- Range: 0-100 kPa
- Bridge resistance: 5 kΩ
- Sensitivity: 20 mV/V/100kPa
- Accuracy: 0.1% FS

**Solution**:
```
1. Bridge excitation: 5V

2. Full-scale output:
   V_FS = 5V × 20mV/V = 100 mV

3. INA gain:
   Target ADC input: 2V
   G_INA = 2V / 100mV = 20×

4. ADC selection:
   Resolution needed: 0.1% = 10 bits minimum
   Choose: 12-bit SAR ADC
   LSB = 2V / 4096 = 0.488 mV
   Pressure per LSB = 100kPa / 4096 = 24.4 Pa

5. Offset nulling:
   Use INA with offset adjust (typ. ±10mV range)
   Digital calibration in software
```

### Example 3: Gyroscope Readout

**Specifications**:
- Drive frequency: 10 kHz
- Sense bandwidth: 100 Hz
- Angular rate: ±250 °/s
- Noise: <0.01 °/s/√Hz

**Solution**:
```
1. Drive loop:
   - PLL locks to mechanical resonance
   - AGC maintains constant amplitude (1V RMS)
   - Drive signal feeds electrostatic comb drive

2. Sense path:
   - Capacitive pickup (charge amplifier)
   - Demodulation at 10 kHz (mixer + LPF)
   - Baseband amplification (G=100)
   - 16-bit ΣΔ ADC

3. Signal processing:
   - Quadrature cancellation (digital)
   - Temperature compensation
   - Calibration coefficients in EEPROM
```

---

## Summary

### Key Takeaways

1. **Capacitive sensors** → Charge amplifiers, switched-cap circuits
2. **Piezoresistive sensors** → Instrumentation amplifiers, bridge circuits
3. **Resonant sensors** → PLLs, AGC, demodulation
4. **Noise is critical** → Design for minimum noise at front-end
5. **Integration** → Modern trend toward full signal chain on single ASIC


### Further Reading

- "MEMS and Microstructures in Aerospace Applications" - R. Osiander
- "Capacitive Sensors: Design and Applications" - L. Baxter
- "Op Amps for Everyone" - R. Mancini (Texas Instruments)
- Application notes from Analog Devices, Texas Instruments, STMicroelectronics

---

**Document Version**: 1.0  
**Last Updated**: January 2026  
**Part of**: Silicon Fabrication Handbook - Chapter 08