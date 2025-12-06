# Polysilicon Processes for MEMS Surface Micromachining

## Table of Contents
- [Introduction](#introduction)
- [Polysilicon Deposition](#polysilicon-deposition)
- [Doping Techniques](#doping-techniques)
- [Annealing and Stress Control](#annealing-and-stress-control)
- [Film Properties](#film-properties)
- [Patterning Processes](#patterning-processes)
- [Multi-Layer Structures](#multi-layer-structures)
- [Common Challenges](#common-challenges)
- [Applications](#applications)

---

## Introduction

Polycrystalline silicon (polysilicon or poly-Si) is the primary structural material in surface micromachining due to its excellent mechanical properties, CMOS compatibility, and well-established processing techniques. Unlike bulk micromachining which sculpts the substrate, surface micromachining builds MEMS devices layer-by-layer on top of the wafer.

### Why Polysilicon?

**Advantages**:
- **Mechanical strength**: Young's modulus ~160 GPa (close to single-crystal Si)
- **CMOS compatible**: Can integrate with electronics
- **Low temperature**: Deposition at 580-650°C preserves underlying circuits
- **Tunable properties**: Stress and resistivity controllable via doping and annealing
- **Good etch selectivity**: Against oxides and other materials

**Key Applications**:
- Accelerometers (automotive airbags)
- Gyroscopes (smartphones)
- Resonators (RF filters)
- Microphones (consumer electronics)
- Pressure sensors

---

## Polysilicon Deposition

### Low-Pressure Chemical Vapor Deposition (LPCVD)

LPCVD is the dominant technique for depositing structural polysilicon in MEMS.

#### Process Parameters

**Typical Recipe**:
```
Precursor:      Silane (SiH₄) or disilane (Si₂H₆)
Temperature:    580-650°C
Pressure:       200-500 mTorr
Deposition rate: 10-30 nm/min
```

**Chemical Reactions**:

*Silane decomposition*:
$$\text{SiH}_4 \rightarrow \text{Si} + 2\text{H}_2$$

*Disilane decomposition* (lower temperature):
$$\text{Si}_2\text{H}_6 \rightarrow 2\text{Si} + 3\text{H}_2$$

#### Deposition Regimes

The film microstructure depends strongly on temperature:

| Temperature | Morphology | Grain Size | Applications |
|-------------|------------|------------|--------------|
| < 575°C | Amorphous | N/A | Sacrificial layers |
| 580-590°C | Fine-grain poly | 30-50 nm | Low-stress films |
| 600-625°C | Poly (standard) | 50-100 nm | Structural beams |
| > 650°C | Large-grain poly | 100-300 nm | High conductivity |

#### Equipment Considerations

**LPCVD Furnaces**:
- Hot-wall tube furnaces (most common)
- Batch processing: 50-150 wafers
- Excellent uniformity: ±2-3% across wafer
- High throughput but slow turnaround

**PECVD Alternative**:
- Plasma-Enhanced CVD for lower temperatures (250-350°C)
- Poorer mechanical properties (lower density)
- Used when thermal budget is critical
- Typical for post-CMOS MEMS integration

---

## Doping Techniques

Polysilicon is doped to control electrical conductivity and modify stress. Undoped polysilicon is too resistive (>10⁴ Ω·cm) for most applications.

### In-Situ Doping

Dopants added during deposition by flowing phosphine (PH₃) or diborane (B₂H₆).

**Process**:
```
Base flow:    100 sccm SiH₄
Dopant:       0.1-1% PH₃ or B₂H₆
Temperature:  600°C
Pressure:     300 mTorr
```

**Advantages**:
- Uniform doping throughout film thickness
- Single-step process
- Predictable resistivity

**Disadvantages**:
- Increases internal stress
- Reduces deposition rate
- Chamber contamination

**Typical Resistivity**: 0.5-5 mΩ·cm (heavily doped)

### Implantation Doping

Post-deposition ion implantation followed by annealing.

**Phosphorus Implant**:
```
Ion:          ³¹P⁺
Energy:       50-150 keV
Dose:         1×10¹⁵ to 5×10¹⁵ cm⁻²
Annealing:    1000-1100°C, 1-2 hours (N₂)
```

**Advantages**:
- Better control over doping profile
- Can create graded doping
- Less initial stress
- No furnace contamination

**Disadvantages**:
- Requires annealing step
- High-temperature annealing may affect underlying layers
- Non-uniform doping near edges

---

## Annealing and Stress Control

Residual stress is critical in MEMS – it determines whether structures curl, buckle, or remain flat after release.

### Stress Types

**Intrinsic Stress**:
- Built into film during deposition
- Depends on deposition conditions
- Tensile or compressive

**Thermal Stress**:
- Arises from CTE mismatch during cooling
- Always present when T_dep > T_ambient

$$\sigma_{\text{thermal}} = \frac{E}{1-\nu} \cdot \Delta\alpha \cdot \Delta T$$

Where:
- E = Young's modulus
- ν = Poisson's ratio
- Δα = CTE mismatch
- ΔT = Temperature change

### Stress Measurement

**Wafer Bow Method**:
- Measure wafer curvature before and after deposition
- Calculate stress using Stoney's equation:

$$\sigma_f = \frac{E_s t_s^2}{6(1-\nu_s) t_f} \left( \frac{1}{R_f} - \frac{1}{R_i} \right)$$

Where:
- σ_f = film stress
- E_s, ν_s = substrate properties
- t_s, t_f = substrate and film thickness
- R_i, R_f = initial and final radius of curvature

**Typical Values**:
- As-deposited: -300 to +100 MPa
- After anneal: -50 to +50 MPa
- Target for released structures: ±20 MPa

### Annealing Strategies

#### High-Temperature Anneal

**Standard Recipe**:
```
Temperature:  1000-1050°C
Atmosphere:   N₂ or Ar
Time:         1-2 hours
Ramp rate:    5-10°C/min
```

**Effects**:
- Grain growth (50 nm → 200 nm)
- Stress relief through atomic rearrangement
- Dopant activation and redistribution
- Hydrogen outdiffusion

#### RTA (Rapid Thermal Anneal)

**Process**:
```
Temperature:  1000-1100°C
Time:         30-60 seconds
Lamp heating
```

**Advantages**:
- Minimal thermal budget
- Reduced dopant diffusion
- Quick turnaround

---

## Film Properties

### Mechanical Properties

| Property | Typical Value | Notes |
|----------|---------------|-------|
| Young's Modulus | 140-170 GPa | Depends on grain size |
| Poisson's Ratio | 0.22 | Similar to single-crystal Si |
| Density | 2.25-2.33 g/cm³ | Lower than c-Si (2.33) |
| Fracture Strength | 1-3 GPa | Much higher than bulk Si |
| Hardness | 8-12 GPa | Varies with doping |

### Electrical Properties

**Resistivity vs Doping**:

| Doping Level (cm⁻³) | Resistivity (mΩ·cm) | Application |
|---------------------|---------------------|-------------|
| < 10¹⁷ | > 100 | Semi-insulating |
| 10¹⁸ - 10¹⁹ | 10-100 | Moderate conductivity |
| 10²⁰ - 10²¹ | 0.5-5 | Structural + electrode |
| > 10²¹ | < 0.5 | Highly conductive paths |

**Temperature Coefficient of Resistance (TCR)**:
- Undoped: -0.1% to -0.3% /°C
- Heavily doped: +0.05% to +0.15% /°C
- Important for piezoresistive sensors

### Optical Properties

- Refractive index (n): 3.5-4.0 at 633 nm
- Extinction coefficient (k): 0.01-0.1
- Reflectivity: 30-40%
- Opaque to visible light (unlike amorphous Si)

---

## Patterning Processes

### Lithography

**Standard Photoresist Process**:
```
1. HMDS vapor prime (adhesion)
2. Spin PR: 1-2 μm thick
3. Soft bake: 90°C, 60 sec
4. Expose: i-line (365 nm)
5. Develop: 60 sec
6. Hard bake: 120°C, 90 sec
```

**Critical Dimensions**:
- Minimum feature: 0.5-2 μm (contact lithography)
- Minimum gap: 1-3 μm
- Alignment tolerance: ±0.5 μm

### Dry Etching

**RIE (Reactive Ion Etching)**:

*Chemistry*:
- SF₆ + O₂ (isotropic component)
- CF₄ + O₂ (more anisotropic)
- HBr + Cl₂ + O₂ (highly anisotropic)

**Typical Recipe**:
```
Gas:          SF₆ 30 sccm / O₂ 5 sccm
Pressure:     20-50 mTorr
RF Power:     150-300 W
Etch rate:    100-300 nm/min
Selectivity:  30:1 to SiO₂
```

**Profile Control**:
- Lower pressure → more anisotropic
- Higher RF power → faster etch, more damage
- O₂ addition → sidewall passivation

### Wet Etching

Less common for polysilicon MEMS due to undercutting.

**KOH Etch** (anisotropic):
```
Solution:     30% KOH in H₂O
Temperature:  80°C
Etch rate:    ~1 μm/min
```

- Attacks <100> planes faster
- Not practical for fine features
- Used in hybrid processes

---

## Multi-Layer Structures

Most practical MEMS devices require multiple structural layers.

### Poly0 - Poly1 - Poly2 Process

**Standard Surface Micromachining Stack**:

```
Layer       | Thickness | Purpose
------------|-----------|-------------------------
Poly0       | 0.3-0.5 μm| Ground plane, fixed electrode
Oxide 1     | 2.0 μm    | Sacrificial spacer
Poly1       | 2.0 μm    | Primary structural layer
Oxide 2     | 0.5-1.0 μm| Sacrificial (dimples, anchors)
Poly2       | 1.5 μm    | Upper electrode, cap
```

**Example Process Flow** (Analog Devices ADXL50):

1. **Poly0 deposition and pattern**
   - LPCVD polysilicon: 0.5 μm
   - Dope: POCl₃, 1000°C
   - Pattern: RIE
   
2. **First sacrificial oxide**
   - PSG deposition: 2.0 μm
   - Pattern dimples: 0.5 μm deep
   
3. **Poly1 structural layer**
   - LPCVD polysilicon: 2.0 μm
   - Anneal: 1050°C, 1 hr
   - Pattern: beams, anchors
   
4. **Second sacrificial oxide**
   - PSG: 0.75 μm
   - Pattern via holes
   
5. **Poly2 deposition**
   - LPCVD polysilicon: 1.5 μm
   - Pattern: cap structures
   
6. **Release**
   - HF etch: 49%, 2-5 min
   - Rinse and dry

### Design Considerations

**Anchor Design**:
- Must penetrate all sacrificial layers
- Typical size: 10×10 μm minimum
- Multiple anchors for large structures

**Dimples**:
- Prevent stiction to substrate
- Height: 0.3-0.5 μm
- Spacing: 20-50 μm

**Etch Holes**:
- Allow HF access for release
- Diameter: 2-5 μm
- Spacing: 20-100 μm
- Affect squeeze-film damping

---

## Common Challenges

### Stress Gradients

**Problem**: Through-thickness stress variation causes curl after release.

**Causes**:
- Temperature ramp during deposition
- Dopant segregation at grain boundaries
- Incomplete annealing

**Solutions**:
- Optimize deposition temperature profile
- Multi-step annealing
- Compensating bi-layer structures

**Quantification**:

Curl radius for cantilever beam:
$$R = \frac{t^2}{6 \Delta \sigma}$$

Where Δσ is the stress gradient (MPa/μm).

### Grain Boundary Effects

**Issues**:
- Scatter in mechanical properties
- Dopant segregation → non-uniform conductivity
- Preferred etch paths

**Mitigation**:
- Higher deposition temperature → larger grains
- Post-deposition anneal
- Use of <110> oriented poly

### Adhesion to Oxide

**Problem**: Delamination during processing or release.

**Solutions**:
- Plasma cleaning before deposition
- Anneal at 450°C in N₂ before poly deposition
- Minimize stress mismatch
- Use roughened oxide surface

---

## Applications

### Accelerometer (Analog Devices ADXL)

**Structure**:
- Proof mass: 200 × 200 μm, 2 μm thick poly
- Flexures: 2 μm wide, 100 μm long
- Comb fingers: 2 μm wide, 2 μm gap, 50 μm long

**Poly Processing**:
- Poly1: structural, low-stress (< 10 MPa tensile)
- Phosphorus doped: 5×10²⁰ cm⁻³
- Anneal: 1050°C, 1 hr

**Performance**:
- Range: ±2-50 g
- Sensitivity: ~20 mV/g
- Noise floor: ~100 μg/√Hz

### MEMS Resonator (SiTime)

**Structure**:
- Resonant beam: 50 μm × 5 μm × 2 μm
- Drive/sense electrodes: 1 μm gap
- Anchor: center-supported

**Poly Processing**:
- Ultra-low stress: ±5 MPa
- Heavy doping: minimize TCF
- Encapsulated in poly2 cap

**Performance**:
- Frequency: 1-100 MHz
- Q-factor: 10,000-50,000
- Temperature stability: ±50 ppm

### Micromirror (Texas Instruments DLP)

**Structure**:
- Mirror: 10-16 μm square
- Hinge: 1 μm wide torsional beam
- Yoke: connects mirror to hinge

**Poly Processing**:
- Three poly layers
- Aluminum coating on top poly
- Precise stress control for flat mirrors

**Performance**:
- Tilt angle: ±10-12°
- Switching speed: < 20 μsec
- Millions of cycles lifetime

---

## Summary

Polysilicon surface micromachining is a mature technology that enables mass production of complex MEMS devices. Key success factors include:

1. **Stress control** through deposition optimization and annealing
2. **Doping strategy** for desired electrical and mechanical properties
3. **Multi-layer design** for increased functionality
4. **Careful release** to avoid stiction and fracture
5. **CMOS compatibility** for integrated systems

The technique continues to evolve with new applications in RF, timing, and sensing requiring ever-better control of film properties and dimensional tolerances.

---

## Further Reading

### Essential Papers
- Howe, R.T. and Muller, R.S., "Polycrystalline Silicon Micromechanical Beams," *J. Electrochem. Soc.*, 1983
- Zhang, X. et al., "Residual Stress and Fracture in Thick LPCVD Polysilicon Films," *Sensors and Actuators A*, 1998
- Kim, C.J., "Release and Packaging of MEMS," *IEEE*, 1998

### Standards
- SEMI MF1530: Test Method for Measuring Residual Stress in Thin Films
- ASTM E2245: Test Method for Residual Strain Measurements of Thin Films

---

**Next Chapter**: [Sacrificial Layers](./sacrificial-layers.md) →

**Related Topics**: 
- [CMOS FEOL Processing](../02-cmos-feol/transistor-fabrication.md)
- [Release Techniques](./release-techniques.md)
- [Stiction Prevention](./stiction-prevention.md)

**Last Updated**: November 2025  
**Contributors**: Zeyad Mustafa
**Chapter:** 4.1 -mems-surface-micromachining  