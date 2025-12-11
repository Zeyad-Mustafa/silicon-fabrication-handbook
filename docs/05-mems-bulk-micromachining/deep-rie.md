# Deep Reactive Ion Etching (DRIE)

## Table of Contents
- [Introduction](#introduction)
- [Bosch Process](#bosch-process)
- [Cryogenic DRIE](#cryogenic-drie)
- [Process Optimization](#process-optimization)
- [Applications](#applications)
- [Troubleshooting](#troubleshooting)
- [References](#references)

## Introduction

Deep Reactive Ion Etching (DRIE) enables high aspect ratio (>20:1) structures in silicon with nearly vertical sidewalls. It's essential for MEMS bulk micromachining, through-silicon vias (TSVs), and 3D integration.

### Key Capabilities

| Parameter | Typical Value | Best Achieved |
|-----------|--------------|---------------|
| Etch depth | 10-500 μm | >1000 μm |
| Aspect ratio | 20:1 to 50:1 | >100:1 |
| Etch rate | 1-10 μm/min | 15 μm/min |
| Sidewall angle | 88-92° | 89.5-90.5° |
| Selectivity (Si:Mask) | 50:1 to 200:1 | 300:1 |
| Uniformity | ±5% | ±2% |

### Process Comparison

**Bosch Process:**
- Time-multiplexed etch/passivation cycles
- Scalloped sidewalls (100-500 nm)
- Higher etch rates (3-6 μm/min)
- Better for deep features (>100 μm)
- Lower cost operation

**Cryogenic DRIE:**
- Continuous process with sidewall passivation
- Smooth sidewalls (<50 nm roughness)
- Moderate rates (1-3 μm/min)
- Better profile control
- Requires cryogenic cooling (-110°C)

## Bosch Process

Named after Robert Bosch GmbH, this alternating etch/passivation process is the most common DRIE technique.

### Process Principle

```
Cycle 1: SF₆ plasma etch (isotropic)
  ↓
Cycle 2: C₄F₈ polymer deposition (passivation)
  ↓
Cycle 3: Ion bombardment removes bottom polymer
  ↓
Cycle 4: SF₆ etch continues
  ↓
Repeat...
```

**Key Reactions:**

Etch step:
```
SF₆ + e⁻ → SF₅* + F* + e⁻
Si + 4F* → SiF₄ (volatile, removed by pump)
```

Passivation step:
```
C₄F₈ + e⁻ → CF₂* + CF₃* + ...
CF₂* → (CF₂)ₙ polymer (deposits on surfaces)
```

### Process Parameters

**Standard Recipe:**

```
Etch Step:
- Gas: SF₆ (100-300 sccm)
- Pressure: 10-30 mTorr
- RF Power: 600-1200 W (platen)
- ICP Power: 1500-3000 W (coil)
- Time: 5-15 seconds
- Temperature: 20°C

Passivation Step:
- Gas: C₄F₈ (50-150 sccm)
- Pressure: 10-25 mTorr
- RF Power: 0-50 W (light ion bombardment)
- ICP Power: 1500-2500 W
- Time: 3-8 seconds
```

**Cycle Optimization:**

| Parameter | Effect on Process |
|-----------|-------------------|
| Longer etch time | Higher rate, more lateral etch, rougher sidewalls |
| Longer passivation | Slower rate, better anisotropy, smoother walls |
| Higher SF₆ flow | Higher etch rate, more isotropic |
| Higher C₄F₈ flow | Thicker passivation, lower rate |
| Higher platen power | More anisotropic, faster bottom clearing |
| Higher ICP power | Higher etch rate, more radical generation |

### Sidewall Profile

**Scallop Formation:**

```
Depth per cycle: d = etch_rate × etch_time

Typical: 200-500 nm scallops

Scallop size reduction:
- Shorter cycle times (3s etch / 2s pass)
- Lower etch rates
- Optimized passivation thickness
```

**Verticality Control:**

```
Sidewall angle = 90° ± α

Factors affecting angle:
1. Mask erosion (causes positive taper)
2. Passivation uniformity
3. Ion directionality
4. Loading effects

Correction:
- Adjust platen power (bias voltage)
- Optimize polymer thickness
- Use hard masks (oxide, metal)
```

### Mask Materials

| Mask Material | Selectivity | Thickness Needed (100μm etch) | Notes |
|---------------|-------------|-------------------------------|-------|
| Photoresist | 50:1 | 2-3 μm | Low cost, easy pattern |
| Oxide (SiO₂) | 100:1 | 1-1.5 μm | Good selectivity |
| Silicon nitride | 150:1 | 0.7-1 μm | Excellent selectivity |
| Aluminum | 200:1 | 0.5-0.8 μm | Best for very deep |
| Thick resist (SU-8) | 40:1 | 3-4 μm | Thick patterns |

**Mask Design Rules:**
- Minimum feature size: 2-5 μm
- Spacing: ≥ 5 μm for >100 μm depth
- Corner compensation: Add serifs for sharp corners
- Avoid large open areas (loading effects)

### Etch Rate Calculations

**Single Cycle:**
```
Etch depth per cycle ≈ 200-500 nm

For 100 μm total depth:
Cycles needed = 100,000 nm / 300 nm = 333 cycles

Cycle time = etch_time + pass_time + switch_time
           = 7s + 5s + 2s = 14s

Total time = 333 × 14s = 4662s ≈ 78 minutes
Average etch rate = 100 μm / 78 min = 1.28 μm/min
```

**Rate Enhancement:**
- Increase etch time: 10s → 400 nm/cycle → 2 μm/min
- Increase SF₆ flow: +50% → +30% rate
- Increase power: +20% → +15% rate
- Trade-off: Profile quality vs speed

### Loading Effects

**Pattern Density Impact:**

```
Microloading: Small features etch slower
Macroloading: Dense areas etch slower than open

RIE Lag = (Depth_open - Depth_dense) / Depth_open × 100%

Typical: 5-20% lag

Mitigation:
1. Dummy fill patterns
2. Optimize pressure (lower is better)
3. Increase overetch time
4. Use cryogenic DRIE (less loading)
```

### Advanced Bosch Techniques

**1. Ramped Parameters:**
```
Start: Aggressive etch (fast rate)
Middle: Balanced (profile control)
End: Gentle (minimize notching)

Example:
Cycles 1-100: 10s etch / 5s pass
Cycles 101-200: 7s etch / 5s pass  
Cycles 201-300: 5s etch / 6s pass
```

**2. DRIE-Coil Process:**
- Multiple ICP coils for better uniformity
- Independent control of center vs edge
- <3% across-wafer variation

**3. Pulsed DRIE:**
- Time-modulated plasma power
- Reduces substrate heating
- Better for temperature-sensitive processes

## Cryogenic DRIE

Continuous process using cryogenic cooling for sidewall passivation.

### Operating Principle

At cryogenic temperatures (-110 to -140°C), oxygen forms a SiOₓFᵧ passivation layer on sidewalls while the bottom remains clear due to ion bombardment.

**Key Reactions:**
```
Si + F* → SiF₄ (etch)
Si + O* + F* → SiOₓFᵧ (passivation at cold sidewalls)

Temperature control:
Sidewall: -110°C (passivation stable)
Bottom: -90°C (local heating, passivation removed)
```

### Process Parameters

```
Gas Mixture:
- SF₆: 100-200 sccm (etchant)
- O₂: 5-15 sccm (passivation)
- Ratio SF₆:O₂ = 10:1 to 20:1

Pressure: 5-15 mTorr

RF Power:
- ICP: 800-1500 W
- Platen: 5-20 W (low bias for smooth walls)

Temperature: -110 to -130°C (LN₂ cooling)

Typical Rate: 1-3 μm/min
```

### Advantages & Limitations

**Advantages:**
- Smooth sidewalls (RMS < 50 nm)
- Excellent anisotropy (89.8-90.2°)
- No scalloping
- Better aspect ratios (>100:1 possible)
- Reduced notching at buried layers

**Limitations:**
- Requires cryogenic cooling system
- Slower etch rates
- Temperature control critical
- Higher equipment cost
- Longer process development

### Temperature Effects

```
T < -120°C: Too much passivation, rate drops
-110 to -120°C: Optimal window
T > -100°C: Insufficient passivation, profile degrades

Temperature uniformity: ±5°C across wafer
```

### Applications

Best suited for:
- Photonic devices (smooth surfaces)
- High aspect ratio TSVs
- Optical MEMS (low roughness)
- Precision accelerometers/gyroscopes

## Process Optimization

### Design of Experiments (DOE)

**Key Parameters to Optimize:**

1. **Etch Rate:**
   - Primary: SF₆ flow, ICP power
   - Secondary: Pressure, etch time

2. **Profile (Verticality):**
   - Primary: Platen power, passivation time
   - Secondary: C₄F₈ flow, pressure

3. **Selectivity:**
   - Primary: Mask material
   - Secondary: Cycle ratio, platen power

4. **Uniformity:**
   - Primary: Pressure, ICP power
   - Secondary: Gas distribution

**Typical DOE Matrix:**
```
Run  SF₆(sccm)  C₄F₈(sccm)  ICP(W)  Platen(W)  Etch(s)  Pass(s)
1    150        80          2000    800        7        5
2    200        80          2500    800        7        5
3    150        120         2000    1000       7        5
...
```

### Characterization Methods

**1. Profile Analysis (SEM):**
```
Measurements:
- Etch depth (±1 μm accuracy)
- Sidewall angle (±0.5°)
- Scallop size (50 nm resolution)
- Notching at interfaces

Sample prep:
- Cleave wafer through features
- Mount at 90° angle
- Coat with thin Au/Pd for imaging
```

**2. Etch Rate Monitoring:**
```
Methods:
- Laser interferometry (in-situ, real-time)
- Thickness measurement (post-etch)
- Endpoint detection (optical emission)

Typical measurement:
Rate = Depth / Time
For 100 μm in 30 min: Rate = 3.33 μm/min
```

**3. Uniformity Mapping:**
```
Measure at 9-49 points across wafer:

Uniformity (%) = (Max - Min) / (2 × Mean) × 100

Target: <5% for production
Excellent: <3%
```

### Common Issues & Solutions

| Problem | Cause | Solution |
|---------|-------|----------|
| Bowing (barrel shape) | Excess lateral etch | Reduce etch time, increase passivation |
| Positive taper | Mask erosion | Use harder mask, reduce overetch |
| Negative taper | Polymer buildup | Increase ion bombardment, reduce C₄F₈ |
| Notching | Charge buildup | Pulse plasma, use SOI, add O₂ |
| Micrograss | Inadequate passivation | Increase C₄F₈, optimize cycle |
| Slow rate | Too much polymer | Decrease passivation time/flow |
| Non-uniformity | Pressure too high | Reduce pressure, check gas flow |

### Notching Mechanism

Occurs at insulating layers (buried oxide in SOI):

```
Cause: Ion deflection by charging

e⁻ → Oxide surface → Negative charge
Ions deflected → Lateral etch at interface

Solutions:
1. Pulsed plasma (discharge time for neutralization)
2. Protective passivation layer
3. Endpoint detection (stop before oxide)
4. AC bias on platen
```

## Applications

### 1. Through-Silicon Vias (TSVs)

```
Requirements:
- Diameter: 5-50 μm
- Depth: 50-300 μm
- Aspect ratio: 10:1 to 20:1
- Verticality: <1° taper

Process:
1. Pattern photoresist (5 μm)
2. Bosch DRIE (optimized for high rate)
3. Strip resist
4. Oxidize sidewalls (100 nm)
5. Deposit barrier/seed layer
6. Electroplate Cu
```

**Typical Recipe:**
- 8s SF₆ etch / 5s C₄F₈ passivation
- Rate: 4-5 μm/min
- Time: 15-20 minutes for 100 μm

### 2. Accelerometer Proof Mass

```
Features:
- Thickness: 20-100 μm
- Lateral dimensions: 200-1000 μm
- Aspect ratio: 5:1 to 10:1

Process:
1. Pattern oxide mask (1 μm)
2. DRIE through device layer (SOI)
3. Stop on BOX
4. Remove oxide mask
5. Release (BOX etch)
```

### 3. Microfluidic Channels

```
Dimensions:
- Width: 10-100 μm
- Depth: 50-500 μm
- Smooth walls required

Process:
- Cryogenic DRIE preferred (smooth)
- Oxide mask
- Seal with bonded wafer or glass
```

### 4. Photonic Waveguides

```
Requirements:
- Ultra-smooth sidewalls (<20 nm Ra)
- Precise angle control (±0.1°)
- Minimal damage

Process:
- Cryogenic DRIE
- Very low bias power
- Slow rate (1-2 μm/min)
- Minimal overetch
```

## Safety Considerations

### Chemical Hazards

**SF₆ (Sulfur Hexafluoride):**
- Global warming potential: 23,500× CO₂
- Requires exhaust scrubbing
- Non-toxic but asphyxiant

**C₄F₈ (Octafluorocyclobutane):**
- PFC (perfluorocarbon)
- GWP: 8,700× CO₂
- Requires abatement

**Safety Measures:**
- Emission monitoring
- Thermal or plasma abatement
- Proper ventilation
- Personal protective equipment

### Equipment Safety

- High RF power (electrical hazard)
- Vacuum system (implosion risk)
- Cryogenic fluids (cold burns)
- Regular maintenance critical

## Cost Analysis

**Capital Equipment:**
- Basic Bosch system: $500K - $800K
- Advanced DRIE (cryogenic): $800K - $1.5M
- Maintenance: 10-15% of capital per year

**Operating Costs (per wafer run):**
```
Consumables:
- SF₆ gas: $5-10
- C₄F₈ gas: $10-15
- Mask materials: $5-20
- Chamber cleaning: $2-5

Labor:
- Process time: 1-2 hours
- Setup/cleanup: 0.5 hours

Utilities:
- Power (10-20 kW): $3-6
- Cooling water: $1-2
- Abatement: $2-4

Total: $30-65 per wafer (4-6" wafers)
```

## Future Trends

### Advanced Techniques

**1. Atomic Layer Etching (ALE):**
- Cycle-by-cycle atomic precision
- Ultimate smoothness
- Very slow rates (<100 nm/min)

**2. DRIE with In-Situ Metrology:**
- Real-time depth monitoring
- Adaptive process control
- Improved uniformity

**3. Plasma-Free DRIE:**
- Metal-assisted chemical etching
- Room temperature
- Different anisotropy mechanism

### Emerging Applications

- 3D heterogeneous integration
- Quantum device fabrication
- Advanced packaging (2.5D/3D)
- Photonic integrated circuits
- High-density interconnects

## Design Guidelines

### General Rules

```
✓ Feature size ≥ 2 μm (5 μm for >200 μm depth)
✓ Aspect ratio < 30:1 (Bosch), < 50:1 (Cryo)
✓ Spacing ≥ 2× feature size minimum
✓ Avoid isolated features (loading effects)
✓ Round corners (reduce stress concentration)
✓ Include test structures on each mask

Mask overhang for 100 μm etch:
- Photoresist (50:1): 2 μm
- Oxide (100:1): 1 μm
- Nitride (150:1): 0.7 μm
```

### Process Selection

**Choose Bosch when:**
- Deep features (>100 μm)
- High throughput needed
- Cost sensitive
- Sidewall roughness acceptable

**Choose Cryogenic when:**
- Smooth sidewalls critical
- Optical applications
- Very high aspect ratios
- Profile precision required

## References

1. Laermer, F., & Schilp, A. (1996). Method of anisotropically etching silicon. *U.S. Patent No. 5,501,893*.

2. de Boer, M. J., et al. (2002). Guidelines for etching silicon MEMS structures using fluorine high-density plasmas at cryogenic temperatures. *Journal of Microelectromechanical Systems*, 11(4), 385-401.

3. Marty, F., et al. (2005). Advanced etching of silicon based on deep reactive ion etching for silicon high aspect ratio microstructures and three-dimensional micro- and nanostructures. *Microelectronics Journal*, 36(7), 673-677.

4. Jansen, H. V., et al. (2009). A survey on the reactive ion etching of silicon in microtechnology. *Journal of Micromechanics and Microengineering*, 19(3), 033001.

5. Wu, B., Kumar, A., & Pamarthy, S. (2010). High aspect ratio silicon etch: A review. *Journal of Applied Physics*, 108(5), 051101.

---

**Document Information:**
- **Created:** December 11, 2025
- **Version:** 1.0
- **Status:** Complete
- **Part of:** Silicon Fabrication Handbook
- **Next Chapter:** [Wet Etching](wet-etching.md)
- **Previous Section:** [MEMS Surface Micromachining](../04-mems-surface-micromachining/)

**License:** CC BY 4.0 - Free to use with attribution

---

*For questions, corrections, or contributions, please visit:*
https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook