# Case Studies: MEMS-CMOS Integration

## Table of Contents
1. [Automotive IMU System](#automotive-imu-system)
2. [Smartphone MEMS Microphone](#smartphone-mems-microphone)
3. [Tire Pressure Monitoring System (TPMS)](#tire-pressure-monitoring-system-tpms)
4. [Medical Implantable Pressure Sensor](#medical-implantable-pressure-sensor)
5. [Consumer Smartwatch IMU](#consumer-smartwatch-imu)

---

## Automotive IMU System

### Application Overview

**Product**: 6-axis Inertial Measurement Unit for Electronic Stability Control (ESC)  
**Manufacturer**: Bosch (SMI230 family)  
**Integration**: Monolithic (MEMS + ASIC in single package)

### System Requirements

```
Performance Specifications:
├── Accelerometer
│   ├── Range: ±16g
│   ├── Noise: 150 μg/√Hz
│   ├── Bandwidth: 1600 Hz
│   └── Temperature: -40°C to +125°C
│
└── Gyroscope
    ├── Range: ±2000 °/s
    ├── Noise: 0.014 °/s/√Hz
    ├── Bandwidth: 532 Hz
    └── Zero-rate offset: <1 °/s

Reliability:
- Automotive grade (AEC-Q100)
- Lifetime: 15 years
- Vibration: 20g RMS (10-2000 Hz)
- Shock: 10,000g (0.2ms)
```

### Integration Strategy

**Two-Die System-in-Package**:
```
┌─────────────────────────────┐
│      Package (LGA 3×4.5mm)  │
│  ┌──────────┐  ┌──────────┐ │
│  │   MEMS   │  │   ASIC   │ │
│  │  Sensor  │  │  (CMOS)  │ │
│  │          │  │          │ │
│  │ 3-axis   │  │ 16-bit   │ │
│  │ Accel +  │  │ ADCs     │ │
│  │ 3-axis   │  │ + DSP    │ │
│  │ Gyro     │  │          │ │
│  └────┬─────┘  └─────┬────┘ │
│       │              │      │
│       └──────┬───────┘      │
│              │              │
│      ┌───────┴────────┐     │
│      │  Interconnect  │     │
│      │  (Wire bonds)  │     │
│      └────────────────┘     │
└─────────────────────────────┘
```

### MEMS Fabrication

**Process Flow**:
1. **Substrate**: 100mm silicon wafers
2. **Accelerometer**: Surface micromachined, capacitive
   - Poly-Si structural layer (10 μm thick)
   - Comb-drive fingers (2 μm gap)
   - Proof mass: 100 × 100 μm²
3. **Gyroscope**: Dual-mass tuning fork design
   - Drive frequency: 14 kHz
   - Q-factor: 10,000 (vacuum sealed)
   - Coriolis sense electrodes
4. **Packaging**: Wafer-level vacuum encapsulation
   - Cap wafer bonded at 400°C
   - Getter material for pressure maintenance
   - Pressure: <10 mTorr

### ASIC Architecture

**Signal Chain**:
```
MEMS → C-to-V → CDS → PGA → ΣΔ ADC → DSP → SPI/I²C
       Converter  Corr  G=1-8  16-bit  Calib   Output

Key Blocks:
├── Capacitive readout (6 channels)
├── Correlated Double Sampling (CDS)
├── 16-bit Sigma-Delta ADCs
├── Digital filtering (configurable)
├── Temperature sensor + compensation
├── Self-test circuitry
└── SPI/I²C interface (up to 10 MHz)

Power Budget:
- Active mode: 1.8 mA @ 3.3V = 5.9 mW
- Low power: 0.5 mA = 1.65 mW
- Suspend: 3 μA = 10 μW
```

### Manufacturing & Testing

**Yield Optimization**:
- MEMS yield: 92% (after wafer-level test)
- ASIC yield: 95% (0.18 μm CMOS)
- Assembly yield: 98%
- **Overall yield**: 85.7%

**Test Strategy**:
1. Wafer-level probe (MEMS + ASIC separately)
2. Known-good-die selection
3. Package assembly
4. Final test on multi-axis rate table
5. Calibration (temperature sweep -40 to +125°C)
6. Programming of trim coefficients

### Results & Impact

**Performance Achieved**:
- Accelerometer offset: <±40 mg over temperature
- Gyro zero-rate drift: <±0.5 °/s over temperature
- Package size: 3 × 4.5 × 0.95 mm³
- Cost: ~$2 (high volume)

**Market Impact**:
- >500 million units shipped (2015-2024)
- Enabled advanced driver assistance systems (ADAS)
- Standard in modern ESC systems

---

## Smartphone MEMS Microphone

### Application Overview

**Product**: Digital MEMS Microphone  
**Example**: Knowles SPH0641LU4H-1  
**Integration**: MCM (MEMS die + ASIC die in single package)

### System Requirements

```
Acoustic Performance:
├── Sensitivity: -26 dBFS (at 94 dB SPL, 1 kHz)
├── SNR: 64 dB (A-weighted)
├── Dynamic Range: 64 dB
├── Distortion: <1% THD (110 dB SPL)
├── Frequency Response: 100 Hz - 10 kHz (±2 dB)
└── Acoustic Overload: 120 dB SPL

Electrical:
├── Supply: 1.8V (I²S/PDM compatible)
├── Current: 600 μA (active)
├── Interface: PDM (Pulse Density Modulation)
└── Clock: 2.4 MHz typical

Mechanical:
├── Package: 3.5 × 2.65 × 0.98 mm³
├── Acoustic port: Top or bottom
└── SMT compatible (reflow)
```

### MEMS Diaphragm Design

**Structure**:
```
     Sound Port (Ø 0.6mm)
          ↓
    ┌─────────────┐
    │   Backplate │ (perforated, fixed)
    │   ·  ·  ·  │
    ├─────────────┤ Air gap (3-5 μm)
    │  Diaphragm  │ (movable, Si)
    │             │
    └─────────────┘
    
    Capacitive sensor:
    C = ε₀ε_r A / d
    
    ΔC/Δp = sensitivity to pressure
```

**Key Dimensions**:
- Diaphragm: 800 × 800 μm² (silicon, 1 μm thick)
- Backplate: Perforated poly-Si (holes for air flow)
- Bias voltage: 10V (charge pump on ASIC)
- Capacitance: 0.5-1.5 pF (nominal)
- ΔC: ±10 fF at 94 dB SPL

### ASIC Implementation

**Architecture**:
```
MEMS → Charge → Low-Noise → HPF → ADC → Decimation → PDM
Cap    Amp      Amp (40dB)   100Hz  ΣΔ    Filter      Output
                                     4th    CIC+FIR
                                     order

Process: 0.18 μm CMOS
Die size: 1 × 1 mm²

Key Features:
├── Integrated charge pump (10V from 1.8V)
├── 4th-order Sigma-Delta ADC
├── Digital HPF (removes DC offset)
├── Decimation filters (64× typical)
└── PDM output (1-bit bitstream)

Noise Contributors:
├── Thermal noise: 25 dB SPL
├── ADC quantization: 10 dB SPL
├── Amplifier noise: 15 dB SPL
└── Total: ~30 dB SPL (noise floor)
```

### Packaging Technology

**Stacked Die in Molded Package**:
```
Cross-section view:

    ┌──────────────┐  ← Acoustic port
    │   Lid/PCB    │
    ├──────────────┤
    │    ASIC      │ ← Wire bonds
    ├──────────────┤
    │    MEMS      │ ← Die attach
    ├──────────────┤
    │  Substrate   │
    └──────┬───────┘
           │
         Solder balls

Acoustic Design:
- Back volume: Defined by package cavity
- Acoustic compliance: Controlled for frequency response
- Damping: Mesh screen for EMI + dust protection
```

### Manufacturing Process

**MEMS Fabrication** (SOI wafer):
1. DRIE etch of diaphragm (front side)
2. Backplate deposition (LPCVD poly-Si)
3. Perforation holes (DRIE)
4. Release etch (backside cavity)
5. Thin-film metallization
6. Wafer dicing

**Assembly**:
1. ASIC die attach to substrate
2. MEMS die attach to ASIC (stacked)
3. Wire bonding (Au, 25 μm)
4. Molding compound application
5. Acoustic port formation (laser drilling)
6. Testing (on acoustic test station)

### Performance & Cost

**Achieved Performance**:
- SNR: 64 dB (A-weighted) ✓
- Power: 600 μA @ 1.8V = 1.08 mW
- Package size: 3.5 × 2.65 × 0.98 mm³
- Cost: $0.30-0.50 (high volume)

**Applications**:
- Smartphones (2-4 mics per phone)
- True wireless stereo (TWS) earbuds
- Smart speakers
- Laptops and tablets

---

## Tire Pressure Monitoring System (TPMS)

### Application Overview

**Product**: Integrated TPMS Sensor Module  
**Example**: Infineon SP37  
**Integration**: SiP with MEMS pressure sensor + MCU + RF

### System Requirements

```
Sensing:
├── Pressure range: 0-450 kPa (0-65 psi)
├── Accuracy: ±1.5 kPa
├── Temperature range: -40°C to +125°C
└── Temperature accuracy: ±2°C

Wireless:
├── Frequency: 315 MHz (US) / 433 MHz (EU)
├── Protocol: Proprietary or ISO 11898
├── Transmit power: +10 dBm
├── Range: >10 meters
└── Data rate: 1-10 kbps

Power (Battery):
├── Battery: CR2032 (3V, 220 mAh)
├── Lifetime: >10 years
├── Sleep current: <3 μA
└── Active: <20 mA (transmit)
```

### System Architecture

**Three-Die MCM**:
```
┌───────────────────────────────┐
│  Plastic Package (13×7mm)     │
│                               │
│  ┌─────┐  ┌─────┐  ┌──────┐  │
│  │MEMS │  │ MCU │  │  RF  │  │
│  │Press│  │8-bit│  │ TX   │  │
│  │Temp │  │ +   │  │315MHz│  │
│  │     │  │ ADC │  │      │  │
│  └──┬──┘  └──┬──┘  └───┬──┘  │
│     │        │         │     │
│     └────────┴─────────┘     │
│         Wire Bonds            │
│                               │
│  ┌─────────────────────────┐  │
│  │   Pressure Port          │  │
│  │   (Gel-filled)          │  │
│  └─────────────────────────┘  │
└───────────────────────────────┘
```

### MEMS Pressure Sensor

**Piezoresistive Design**:
```
Silicon diaphragm with implanted resistors:

    ┌────── Wheatstone Bridge ──────┐
    │                               │
    │  R1 (+ΔR)     R2 (-ΔR)       │
    │     │           │             │
    │     ├───────────┤             │
    │     │           │             │
    │  R3 (-ΔR)     R4 (+ΔR)       │
    │                               │
    └───────────────────────────────┘

Diaphragm:
- Size: 1.2 × 1.2 mm²
- Thickness: 20 μm
- Deflection: <1 μm at 450 kPa

Sensitivity: 15 mV/V/100kPa
Bridge resistance: 5 kΩ
```

### MCU & Interface

**Microcontroller**:
- Core: 8-bit RISC (low power)
- Flash: 8 KB (code + calibration data)
- RAM: 512 bytes
- Peripherals:
  - 12-bit SAR ADC (pressure + temperature)
  - SPI for RF interface
  - LF receiver (125 kHz, for wake-up)
  - Watchdog timer

**Power Management**:
```
Operating Modes:
├── Sleep: 2.5 μA (RTC running)
├── Measurement: 8 mA, 10 ms (pressure read)
├── Processing: 5 mA, 5 ms (data format)
└── Transmit: 18 mA, 20 ms (RF burst)

Duty Cycle:
- Normal: Transmit every 60s
- Active mode: 35 ms / 60s = 0.058%
- Average current: 18mA × 0.00058 + 2.5μA × 0.999
                 = 10.4 μA + 2.5 μA = 12.9 μA

Battery Life:
220 mAh / 12.9 μA = 17,054 hours = 2 years

With optimizations (adaptive sampling):
→ 10+ years achievable
```

### Packaging Challenges

**Pressure Port Design**:
```
Critical requirements:
1. Media isolation (tire air, water, salt)
2. Pressure transmission (no damping)
3. Temperature compensation
4. Long-term stability

Solution:
- Silicone gel fill (protects die)
- Stainless steel port
- O-ring seal
- Conformal coating on electronics
```

### Calibration & Manufacturing

**Two-Point Calibration**:
1. Atmospheric pressure (101.3 kPa, 25°C)
2. Full scale (450 kPa, 25°C)
3. Temperature sweep (-40°C to +125°C)
4. Store 8 coefficients in flash

**Production Flow**:
1. MEMS wafer test (pressure chamber)
2. MCU wafer test (probe)
3. RF die test
4. Assembly (die attach + wire bond)
5. Gel dispensing
6. Calibration (pressure + temp)
7. Final test (RF functionality)

**Cost Breakdown**:
- MEMS die: $0.20
- MCU die: $0.15
- RF die: $0.10
- Package + assembly: $0.40
- Test + calibration: $0.15
- **Total**: ~$1.00 (volume)

---

## Medical Implantable Pressure Sensor

### Application Overview

**Product**: Wireless Pressure Monitor for Heart Failure  
**Example**: CardioMEMS HF System (Abbott)  
**Integration**: Monolithic MEMS + Custom hybrid packaging

### Clinical Requirements

```
Medical Specifications:
├── Pressure range: 0-300 mmHg (0-40 kPa)
├── Accuracy: ±2 mmHg
├── Resolution: 0.5 mmHg
├── Biocompatibility: ISO 10993
├── MRI compatibility: 3 Tesla safe
└── Lifetime: >10 years implanted

Physical:
├── Size: 15 × 3.4 × 2 mm (capsule)
├── Weight: <150 mg
├── Hermetic seal: Titanium case
└── No battery (passive telemetry)
```

### MEMS Design

**LC Resonant Sensor**:
```
Pressure-sensitive capacitor + fixed inductor = LC tank

    L (coil)
    ─────┐
         │
    ─────┴───── C(P) = f(pressure)
    
Resonant frequency:
f₀ = 1 / (2π√(LC))

As pressure increases:
→ Diaphragm deflects
→ Capacitance changes
→ Resonant frequency shifts

Sensitivity: ~10 kHz/mmHg at 30 MHz carrier
```

**Fabrication**:
- Silicon diaphragm (500 μm thick)
- Anodically bonded glass substrate
- Titanium metallization (biocompatible)
- Hermetic cavity (vacuum reference)
- Planar coil (100 μH, 20 turns)

### Wireless Telemetry

**Passive Operation** (No Battery):
```
External Reader (Wand):
    ↓ RF Power (30 MHz)
    ↓ Interrogation
    
Implanted Sensor:
    → Receives RF energy
    → Powers up briefly
    → Reflects modulated signal
    → Reader detects frequency shift

Communication:
- Inductive coupling (near-field)
- Range: 5-10 cm
- Measurement time: <1 second
- No active electronics (fully passive)
```

### Biocompatible Packaging

**Materials**:
```
Sensor Core:
├── Silicon MEMS (pressure transducer)
├── Glass substrate (anodic bonding)
└── Titanium case (hermetic seal)

Coating:
├── Parylene-C (10 μm, primary barrier)
├── Silicone (additional protection)
└── Biocompatible adhesive

Sterilization:
└── Ethylene oxide (EtO) compatible
```

**Implantation Site**:
- Pulmonary artery
- Anchored with nitinol loops
- Encapsulates in tissue over 4-8 weeks

### Clinical Performance

**Study Results** (CHAMPION Trial):
- 550 patients monitored
- Heart failure hospitalizations reduced by 33%
- Remote monitoring enabled proactive treatment
- >98% sensor functionality at 1 year

**Regulatory**:
- FDA approved (2014)
- CE Mark (EU)
- Class III medical device

---

## Consumer Smartwatch IMU

### Application Overview

**Product**: 9-axis Motion Sensor for Wearables  
**Integration**: All-in-one SiP (3×3mm package)

### Specifications

```
Sensors:
├── 3-axis Accelerometer (±4g)
├── 3-axis Gyroscope (±500 °/s)
└── 3-axis Magnetometer (±8 gauss)

Performance:
├── Power: 1.5 mA (all sensors active)
├── Noise: 90 μg/√Hz (accel), 0.01 °/s/√Hz (gyro)
└── Update rate: 400 Hz

Package: 3×3×1 mm³ LGA
Supply: 1.8-3.6V
Interface: I²C/SPI (up to 10 MHz)
```

### Ultra-Low Power Design

**Power Budget**:
```
Sensor          Active    Low Power
─────────────────────────────────────
Accelerometer   150 μA    20 μA
Gyroscope       1200 μA   100 μA
Magnetometer    150 μA    —
Digital core    100 μA    5 μA
─────────────────────────────────────
Total           1600 μA   125 μA

Smartwatch Usage:
- Active tracking: 1.6 mA × 2 hrs/day
- Always-on pedometer: 125 μA × 22 hrs/day
- Average: (1.6×2 + 0.125×22) / 24 = 0.25 mA
```

**Battery Impact**:
```
Smartwatch battery: 300 mAh
IMU consumption: 0.25 mA
Percentage: (0.25 / 300) × 100% = 0.08% per hour
Daily: 2% of battery (acceptable)
```

### Applications & Algorithms

**Sensor Fusion**:
- Orientation tracking (quaternion calculation)
- Step counting (pedometer)
- Fall detection
- Gesture recognition
- Fitness metrics (running dynamics)

**On-chip Features**:
- FIFO buffer (1 KB)
- Programmable interrupts
- Motion detection wake-up
- Tap/double-tap detection

---

## Summary Table

| Application | Integration | Package Size | Power | Cost | Volume |
|-------------|-------------|--------------|-------|------|--------|
| Auto IMU | 2-die SiP | 3×4.5mm | 6 mW | $2 | 500M+ |
| MEMS Mic | Stacked MCM | 3.5×2.7mm | 1 mW | $0.40 | 5B+ |
| TPMS | 3-die SiP | 13×7mm | 13 μW avg | $1 | 200M+ |
| Implant | Monolithic | 15×3mm | 0 (passive) | $1000+ | 100K+ |
| Smartwatch | All-in-one | 3×3mm | 1.5 mW | $3 | 100M+ |

---

**Key Lessons**:
1. **Integration strategy** depends on application requirements
2. **Power** is critical for battery-operated devices
3. **Packaging** must match environmental needs
4. **Cost** scales dramatically with volume
5. **Reliability** requirements drive design choices

**Document Version**: 1.0  
**Last Updated**: January 2026  
**Part of**: Silicon Fabrication Handbook - Chapter 08