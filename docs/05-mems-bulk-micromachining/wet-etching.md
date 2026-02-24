# Wet Etching for Bulk Micromachining

## Table of Contents
- [Overview](#overview)
- [Silicon Crystal Structure and Etching](#silicon-crystal-structure-and-etching)
  - [Crystal Planes](#crystal-planes)
  - [Standard Wafer Orientations](#standard-wafer-orientations)
- [KOH Etching (Potassium Hydroxide)](#koh-etching-potassium-hydroxide)
  - [Chemistry and Properties](#chemistry-and-properties)
  - [Selectivity to Mask Materials](#selectivity-to-mask-materials)
  - [Process Recipe Example](#process-recipe-example)
  - [Advantages and Limitations](#advantages-and-limitations)
- [TMAH Etching (Tetramethylammonium Hydroxide)](#tmah-etching-tetramethylammonium-hydroxide)
  - [Properties and Advantages](#properties-and-advantages)
  - [Key Benefits Over KOH](#key-benefits-over-koh)
  - [Selectivity Comparison](#selectivity-comparison)
  - [TMAH Process Optimization](#tmah-process-optimization)
- [Anisotropic Etching Behavior](#anisotropic-etching-behavior)
  - [Cavity Formation in (100) Silicon](#cavity-formation-in-100-silicon)
  - [Convex and Concave Corners](#convex-and-concave-corners)
- [EDP Etching (Ethylenediamine Pyrocatechol)](#edp-etching-ethylenediamine-pyrocatechol)
  - [Composition and Use](#composition-and-use)
- [Etch-Stop Techniques](#etch-stop-techniques)
  - [1. P++ Electrochemical Etch Stop](#1-p-electrochemical-etch-stop)
  - [2. SOI (Silicon-on-Insulator) Etch Stop](#2-soi-silicon-on-insulator-etch-stop)
  - [3. Timing-Based (Non-Selective)](#3-timing-based-non-selective)
- [Practical Process Design](#practical-process-design)
  - [Design Rules](#design-rules)
  - [Cavity Depth Calculation](#cavity-depth-calculation)
  - [Process Flow Example: Pressure Sensor](#process-flow-example-pressure-sensor)
- [Troubleshooting Common Issues](#troubleshooting-common-issues)
  - [Problem: Rough Surface (Hillocks)](#problem-rough-surface-hillocks)
  - [Problem: Excessive Undercut](#problem-excessive-undercut)
  - [Problem: Non-Uniform Etch Rate](#problem-non-uniform-etch-rate)
- [Safety and Environmental Considerations](#safety-and-environmental-considerations)
  - [Chemical Hazards](#chemical-hazards)
  - [Waste Disposal](#waste-disposal)
- [Comparison with Dry Etching (DRIE)](#comparison-with-dry-etching-drie)
- [Advanced Topics](#advanced-topics)
  - [Time-Multiplexed Etching](#time-multiplexed-etching)
  - [Etch Rate Dependence on Doping](#etch-rate-dependence-on-doping)
  - [Black Silicon Effect](#black-silicon-effect)
- [Design Examples](#design-examples)
  - [Example 1: V-Groove for Optical Fiber Alignment](#example-1-v-groove-for-optical-fiber-alignment)
  - [Example 2: Inkjet Nozzle Plate](#example-2-inkjet-nozzle-plate)
- [Summary Table](#summary-table)
- [References and Further Reading](#references-and-further-reading)
- [Related Documentation](#related-documentation)


## Overview

Wet chemical etching is a fundamental process in MEMS bulk micromachining, enabling the creation of 3D structures through selective material removal. Unlike dry etching (RIE/DRIE), wet etching uses liquid chemical solutions to dissolve silicon and other materials. The anisotropic nature of silicon wet etching allows precise formation of cavities, membranes, and suspended structures.

**Key Applications:**
- Pressure sensor membranes
- Inkjet printer nozzles
- Accelerometer proof masses
- Microfluidic channels
- Through-wafer vias

---

## Silicon Crystal Structure and Etching

### Crystal Planes

Silicon's diamond cubic crystal structure has distinct planes with different atomic densities:

- **{100} planes**: Moderate atom density, medium etch rate
- **{110} planes**: High atom density, slow etch rate  
- **{111} planes**: Highest atom density, slowest etch rate (~100× slower than {100})

**Anisotropic Etching Principle:**  
Etchants like KOH attack different crystal planes at vastly different rates, enabling controlled 3D geometry.

### Standard Wafer Orientations

| Orientation | Surface | Common Use |
|-------------|---------|------------|
| (100) | {100} plane | Most MEMS devices, standard CMOS |
| (110) | {110} plane | Vertical sidewalls, V-grooves |
| (111) | {111} plane | Etch-stop applications |

**Key Relationship:**  
When etching (100) silicon, the {111} planes are exposed at **54.74°** to the surface, creating the characteristic trapezoidal cavity profile.

```
         Top surface (100)
    ___________________________
    \                         /
     \                       /  54.74°
      \                     /   {111} sidewalls
       \___________________/
           Bottom
```

---

## KOH Etching (Potassium Hydroxide)

### Chemistry and Properties

**Chemical Reaction:**
```
Si + 2OH⁻ + 2H₂O → Si(OH)₂²⁺ + 2H₂ + 4e⁻
Si(OH)₂²⁺ + 4OH⁻ → SiO₂(OH)₂²⁻ + 2H₂O
```

**Typical Solution Parameters:**
- **Concentration**: 20-40 wt% KOH in water
- **Temperature**: 60-90°C
- **Etch rate {100}**: 0.5-2.0 μm/min
- **Etch rate {111}**: ~0.01 μm/min
- **Anisotropy ratio**: 100:1 to 400:1

### Selectivity to Mask Materials

| Material | Selectivity (Si:Material) | Notes |
|----------|---------------------------|-------|
| Si₃N₄ (LPCVD) | 1000:1 | Excellent mask |
| SiO₂ (thermal) | 30:1 | Fair mask, thickness limited |
| SiO₂ (PECVD) | 10:1 | Poor mask |
| Silicon (p++ doped) | ∞ | Etch-stop layer |

### Process Recipe Example

```
Solution: 30% KOH in DI water
Temperature: 80°C
Time: Calculate based on desired depth
Expected rate: ~1.0 μm/min for {100}

Depth (μm) = Rate (μm/min) × Time (min)
Lateral undercut = Depth × √2 (for (100) wafer)
```

### Advantages and Limitations

**Advantages:**
- High selectivity to Si₃N₄
- Smooth {111} surfaces (Ra < 10 nm)
- Low cost, simple equipment
- Excellent uniformity over large areas
- Built-in etch stop (p++ doping)

**Limitations:**
- Fixed sidewall angle (54.74°)
- Undercutting at mask edges
- Not compatible with aluminum
- Generates hydrogen gas (safety concern)
- Temperature control critical

---

## TMAH Etching (Tetramethylammonium Hydroxide)

### Properties and Advantages

TMAH ((CH₃)₄NOH) is an organic alkaline etchant offering improved compatibility with CMOS processes.

**Typical Conditions:**
- **Concentration**: 20-25 wt% in water
- **Temperature**: 80-90°C
- **Etch rate {100}**: 0.5-1.0 μm/min
- **pH**: ~14

### Key Benefits Over KOH

1. **Aluminum compatible**: Can etch Si without attacking Al metallization
2. **Lower surface roughness**: Better for optical applications
3. **CMOS-friendly**: Won't damage IC structures
4. **Safer handling**: Less aggressive than KOH

### Selectivity Comparison

```
Material         KOH (80°C)    TMAH (90°C)
────────────────────────────────────────
Si {100}         1.0 μm/min    0.8 μm/min
Si {111}         0.01 μm/min   0.02 μm/min
Thermal SiO₂     0.03 μm/min   0.01 μm/min
Si₃N₄            0.001 μm/min  0.001 μm/min
Aluminum         ATTACKED      SAFE
```

### TMAH Process Optimization

**Additives for enhanced performance:**
- **Surfactants** (Triton X-100): Reduce surface roughness
- **Silicon powder**: Stabilize etch rate
- **Ammonium persulfate**: Improve {100}/{111} selectivity

---

## Anisotropic Etching Behavior

### Cavity Formation in (100) Silicon

When etching a square opening in (100) silicon:

**Mask aligned to <110>:**
```
        100 μm
    ┌───────────┐
    │           │ Mask opening
    │           │
    └───────────┘
         ↓
    ┌───────────┐
    │╲         ╱│ 54.74° sidewalls
    │ ╲       ╱ │
    │  ╲     ╱  │
    │   ╲   ╱   │
    │    ╲ ╱    │
    └─────▽─────┘
    
Bottom width = Top width - 2h√2
where h = etch depth
```

**Critical dimension:**  
For through-wafer etch (525 μm thick), minimum mask opening ≥ 1.48 mm to avoid pinch-off.

### Convex and Concave Corners

**Convex corners**: Undercut rapidly due to multiple exposed {111} planes
- **Solution**: Corner compensation structures (octagon shapes)

**Concave corners**: Self-limiting, form sharp features
- **Application**: V-grooves, microchannels

---

## EDP Etching (Ethylenediamine Pyrocatechol)

### Composition and Use

EDP is a less common but specialized etchant:
- **Components**: Ethylenediamine + pyrocatechol + water
- **Temperature**: 90-120°C
- **Advantages**: Higher selectivity to SiO₂ (50:1), good uniformity
- **Disadvantages**: Toxic, carcinogenic, being phased out

**Modern trend**: TMAH has largely replaced EDP due to safety concerns.

---

## Etch-Stop Techniques

### 1. P++ Electrochemical Etch Stop

**Principle:**  
Heavily boron-doped silicon (>10²⁰ cm⁻³) etches 100× slower in KOH.

**Implementation:**
```
1. Create p++ layer by boron diffusion or implantation
2. Etch from backside
3. Etch stops automatically at p++ layer
4. Thickness control: ±0.5 μm
```

**Application:** Pressure sensor membranes with precise thickness

### 2. SOI (Silicon-on-Insulator) Etch Stop

**Advantages:**
- Perfect selectivity (oxide stops etch completely)
- Uniform membrane thickness across wafer
- Compatible with both KOH and TMAH

**Structure:**
```
Device Si (1-50 μm)
─────────────────── Buried oxide (BOX)
Handle wafer (525 μm)
```

### 3. Timing-Based (Non-Selective)

**Method:** Calculate etch time based on:
- Initial wafer thickness
- Etch rate calibration
- Desired final thickness

**Accuracy:** ±5-10 μm (lower than etch-stop methods)

---

## Practical Process Design

### Design Rules

1. **Mask alignment**: Always align rectangular openings to <110> directions
2. **Corner compensation**: Add 10-20 μm extensions at convex corners
3. **Minimum feature size**: 10 μm for reliable masking
4. **Aspect ratio**: Depth/width < 10:1 for uniform etching

### Cavity Depth Calculation

```python
# For square cavity in (100) silicon
mask_width = 200e-6  # m
depth = 100e-6       # m

# Bottom width
bottom_width = mask_width - 2 * depth * np.sqrt(2)

# Required mask width for through-etch
wafer_thickness = 525e-6  # m
min_mask_width = 2 * wafer_thickness * np.sqrt(2)
# min_mask_width ≈ 1485 μm
```

### Process Flow Example: Pressure Sensor

```
1. Start: (100) Si wafer with 500 nm LPCVD Si₃N₄
2. Photolithography: Pattern 2×2 mm membrane area
3. Si₃N₄ etch: RIE to open backside
4. KOH etch: 30% at 80°C until p++ layer
5. Remove Si₃N₄: Hot phosphoric acid
6. Front-side processing: Piezoresistors, metallization
```

---

## Troubleshooting Common Issues

### Problem: Rough Surface (Hillocks)

**Causes:**
- Contamination in etchant
- Low temperature
- Poor wafer quality

**Solutions:**
- Filter etchant (0.2 μm)
- Increase temperature by 5-10°C
- Add surfactant (0.1% Triton X-100)

### Problem: Excessive Undercut

**Causes:**
- Mask misalignment to crystal axes
- Thin or poor-quality mask
- Prolonged etching

**Solutions:**
- Use wafer flat alignment
- Increase Si₃N₄ thickness to >200 nm
- Monitor etch depth regularly

### Problem: Non-Uniform Etch Rate

**Causes:**
- Temperature gradients
- Bubble accumulation (H₂ generation)
- Etchant depletion

**Solutions:**
- Use heated water bath with stirring
- Add ultrasonic agitation
- Refresh etchant after 50% Si consumption

---

## Safety and Environmental Considerations

### Chemical Hazards

**KOH:**
- Corrosive: Severe skin/eye burns
- Hydrogen evolution: Explosion risk
- PPE: Face shield, rubber gloves, apron

**TMAH:**
- Moderate corrosivity
- Flammable vapors above 90°C
- Better safety profile than KOH

### Waste Disposal

- Neutralize alkaline solutions with acid before disposal
- Separate silicon-contaminated waste
- Follow local environmental regulations
- Typical neutralization: Add HCl until pH 7-8

---

## Comparison with Dry Etching (DRIE)

| Parameter | Wet Etching | DRIE (Bosch) |
|-----------|-------------|--------------|
| **Sidewall angle** | Fixed 54.74° | Vertical (90°) |
| **Selectivity** | Crystal-dependent | Mask-limited |
| **Surface roughness** | <10 nm | 50-200 nm |
| **Throughput** | High (batch) | Low (serial) |
| **Equipment cost** | Low ($10k) | High ($1-2M) |
| **Feature size** | >10 μm | <1 μm possible |
| **Aspect ratio** | <10:1 | >30:1 |

**Selection Guide:**
- **Wet etching**: Large features, simple geometry, low cost
- **DRIE**: Vertical walls, high aspect ratio, complex shapes

---

## Advanced Topics

### Time-Multiplexed Etching

Alternate between different etchants to create complex profiles:
```
1. KOH etch: 50 μm (fast, rough)
2. TMAH etch: Final 10 μm (slow, smooth)
Result: Fast process with smooth finish
```

### Etch Rate Dependence on Doping

```
Doping level (cm⁻³)    Relative etch rate
─────────────────────────────────────────
<10¹⁵ (intrinsic)      1.0×
10¹⁶-10¹⁸ (n-type)     1.0×
10¹⁹ (n+ type)         1.2×
>10²⁰ (p++ type)       0.01× (etch stop)
```

### Black Silicon Effect

**Observation:** Microtexturing of Si surface in certain etchants
**Cause:** Catalytic metal contamination (Fe, Cu, Ni)
**Prevention:** Ultra-clean processing, avoid metal tools

---

## Design Examples

### Example 1: V-Groove for Optical Fiber Alignment

```
Wafer: (100) silicon
Mask: 100 μm wide stripe along <110>
Etchant: 25% TMAH at 90°C
Time: 50 minutes

Result: V-groove with:
- Depth: ~71 μm
- Bottom width: ~0 μm (sharp)
- Sidewall angle: 54.74°
- Application: Self-aligning fiber mount
```

### Example 2: Inkjet Nozzle Plate

```
Process:
1. Double-side polished (100) Si, 400 μm
2. Pattern nozzle array (50 μm circles)
3. KOH backside etch to 50 μm membrane
4. Frontside RIE to pierce nozzles
5. Critical dimensions: ±2 μm uniformity
```

---

## Summary Table

| Etchant | Temp (°C) | Rate {100} | Anisotropy | Al Safe? | Best For |
|---------|-----------|------------|------------|----------|----------|
| **KOH** | 70-90 | 1-2 μm/min | 100:1 | No | General bulk etching |
| **TMAH** | 80-95 | 0.5-1 μm/min | 50:1 | Yes | CMOS-compatible |
| **EDP** | 100-115 | 0.75 μm/min | 35:1 | No | High oxide selectivity |

---

## References and Further Reading

1. **Kovacs, G.T.A.** - *Micromachined Transducers Sourcebook* (1998)
2. **Williams, K.R., Muller, R.S.** - "Etch Rates for Micromachining Processing" *J. MEMS* 5(4), 1996
3. **Seidel, H., et al.** - "Anisotropic Etching of Crystalline Silicon" *J. Electrochem. Soc.* 137(11), 1990
4. **Tabata, O., et al.** - "Anisotropic Etching of Silicon in TMAH Solutions" *Sensors and Actuators A* 34, 1992

---

## Related Documentation

- [Deep RIE (Bosch Process)](./deep-rie.md) - Dry etching alternative
- [SOI Processes](./soi-processes.md) - Etch-stop substrates
- [Wafer Bonding](./wafer-bonding.md) - Creating sealed cavities
- [Pressure Sensors](./pressure-sensors.md) - Application example

---

**Next Steps:**
1. Review crystal structure fundamentals
2. Practice cavity depth calculations
3. Study the SOI etch-stop process
4. Design a simple membrane structure

**Document Status:** Complete  
**Last Updated:** December 2025  
**Part of:** [Silicon Fabrication Handbook](https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook)
