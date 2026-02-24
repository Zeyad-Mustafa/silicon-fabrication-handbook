# Wafer Bonding for MEMS

## Table of Contents
- [Overview](#overview)
- [Bonding Methods Overview](#bonding-methods-overview)
- [1. Anodic Bonding (Silicon-Glass)](#1-anodic-bonding-silicon-glass)
  - [Principle](#principle)
  - [Process Conditions](#process-conditions)
  - [Key Parameters](#key-parameters)
  - [Advantages and Limitations](#advantages-and-limitations)
  - [Applications](#applications)
- [2. Silicon Direct Bonding (Fusion Bonding)](#2-silicon-direct-bonding-fusion-bonding)
  - [Principle](#principle-1)
  - [Process Flow](#process-flow)
  - [Critical Requirements](#critical-requirements)
  - [Void Formation and Mitigation](#void-formation-and-mitigation)
  - [Low-Temperature Variants](#low-temperature-variants)
- [3. Eutectic Bonding](#3-eutectic-bonding)
  - [Principle](#principle-2)
  - [Common Eutectic Systems](#common-eutectic-systems)
  - [Au-Si Eutectic Process](#au-si-eutectic-process)
  - [Advantages](#advantages)
  - [Limitations](#limitations)
  - [Applications](#applications-1)
- [4. Adhesive Bonding (Polymer)](#4-adhesive-bonding-polymer)
  - [Materials](#materials)
  - [Process: BCB (Benzocyclobutene) Bonding](#process-bcb-benzocyclobutene-bonding)
  - [Applications](#applications-2)
- [5. Glass Frit Bonding](#5-glass-frit-bonding)
  - [Principle](#principle-3)
  - [Process](#process)
  - [Advantages](#advantages-1)
  - [Applications](#applications-3)
- [Bonding Characterization](#bonding-characterization)
  - [Bond Quality Tests](#bond-quality-tests)
  - [Hermeticity Testing](#hermeticity-testing)
- [Design Guidelines](#design-guidelines)
  - [Bond Frame Design](#bond-frame-design)
  - [Cavity Design](#cavity-design)
  - [Thermal Management](#thermal-management)
- [Process Selection Guide](#process-selection-guide)
  - [Decision Matrix](#decision-matrix)
  - [Application Examples](#application-examples)
- [Common Issues and Solutions](#common-issues-and-solutions)
  - [Problem: Voids at Bond Interface](#problem-voids-at-bond-interface)
  - [Problem: Wafer Breakage](#problem-wafer-breakage)
  - [Problem: Poor Hermetic Seal](#problem-poor-hermetic-seal)
- [Cost Comparison](#cost-comparison)
  - [Equipment Costs](#equipment-costs)
  - [Process Costs (per 150 mm wafer)](#process-costs-per-150-mm-wafer)
- [Summary Table](#summary-table)
- [References](#references)
- [Related Documentation](#related-documentation)


## Overview

Wafer bonding is the process of joining two or more wafers to create hermetically sealed cavities, multi-layer structures, and complex 3D MEMS devices. It enables fabrication of structures impossible with single-wafer processing and is essential for packaging, SOI fabrication, and advanced sensors.

**Key Applications:**
- Hermetically sealed pressure sensors
- Vacuum-packaged inertial sensors
- SOI wafer fabrication
- Microfluidic channels
- Multi-layer MEMS devices

---

## Bonding Methods Overview

| Method | Temperature | Bond Strength | Gap Tolerance | Conductivity |
|--------|-------------|---------------|---------------|--------------|
| **Anodic** | 300-500°C | 10-20 MPa | <1 μm | Insulating |
| **Fusion** | 800-1200°C | >20 MPa | <10 nm | Depends on layer |
| **Eutectic** | 350-450°C | 20-50 MPa | 1-5 μm | Conductive |
| **Adhesive** | 150-350°C | 5-15 MPa | 10-50 μm | Insulating |
| **Glass Frit** | 400-600°C | 15-25 MPa | 5-20 μm | Insulating |

---

## 1. Anodic Bonding (Silicon-Glass)

### Principle

Apply high voltage and temperature to bond silicon to glass containing mobile ions (Na⁺). Electric field drives ions away from interface, creating depletion zone that enables Si-O-Si bond formation.

**Chemistry:**
```
Si + Glass (Na₂O-SiO₂) → Si-O-Glass + Na⁺ migration
```

### Process Conditions

**Standard Recipe:**
```
Materials: Silicon (n or p-type) + Pyrex 7740 or Borofloat glass
Temperature: 350-450°C
Voltage: 200-1000 V (glass negative)
Pressure: 500-2000 N (contact force)
Time: 10-30 minutes
Atmosphere: Air or N₂
```

**Equipment Setup:**
```
    ┌─────────────┐ ← Cathode (-)
    │   Silicon   │
    │─────────────│
    │    Glass    │
    └─────────────┘
          ↓
    ┌─────────────┐ ← Anode (+), heated chuck
```

### Key Parameters

**Temperature Effects:**
- Too low (<300°C): Insufficient ion mobility, weak bond
- Optimal (350-450°C): Strong bond, manageable stress
- Too high (>500°C): Excessive stress, wafer bow

**Voltage Effects:**
- <200 V: Incomplete bonding
- 500-800 V: Optimal range
- >1000 V: Risk of electrical breakdown

**Current Signature:**
```
Current (mA)
     │
  100│    ╱╲
     │   ╱  ╲___________  Bonding complete
   50│  ╱
     │ ╱
    0└──────────────────► Time (min)
      0   5   10   15
      
Peak: Ion migration
Plateau: Bond formation
Drop: Process complete
```

### Advantages and Limitations

**Advantages:**
- Hermetic seal (leak rate <10⁻¹² mbar·L/s)
- Room temperature alignment possible
- Transparent for optical access
- Electrical feedthrough capability

**Limitations:**
- Fixed to glass-silicon combination
- Temperature limited to <450°C
- CTE mismatch (Si: 2.6 ppm/K, Pyrex: 3.2 ppm/K)
- Not CMOS-compatible (mobile ions)

### Applications

**Pressure Sensors:**
```
    Glass cap (with vacuum)
    ═══════════════════════
    │                     │ Anodic bond
    └─────────────────────┘
         Si membrane
```

**Through-Glass Vias (TGV):**
- Metal traces on glass
- Anodic bond to Si
- Electrical connection without wire bonds

---

## 2. Silicon Direct Bonding (Fusion Bonding)

### Principle

Two hydrophilic silicon surfaces form Si-O-Si bonds through hydroxyl group condensation at high temperature.

**Reaction Steps:**
```
Room Temp:    Si-OH + HO-Si → Si-O-Si + H₂O (van der Waals)
High Temp:    Si-O-Si → Covalent Si-O-Si bonds + void closure
```

### Process Flow

**1. Surface Preparation (Critical!):**
```
RCA Clean:
  SC-1: NH₄OH:H₂O₂:H₂O (1:1:5) at 75°C, 10 min
        → Remove particles and organics
  
  HF dip: 1% HF, 1 min
        → Remove native oxide
  
  SC-2: HCl:H₂O₂:H₂O (1:1:6) at 75°C, 10 min
        → Remove metallic contamination
  
  DI rinse + spin dry
```

**2. Surface Activation:**
- Plasma treatment (O₂ or N₂)
- Creates hydrophilic surface
- Increases -OH group density

**3. Room Temperature Pre-Bonding:**
- Bring wafers into contact
- Van der Waals forces hold wafers
- Initial bond energy: ~0.1 J/m²

**4. High-Temperature Anneal:**
```
Temperature: 800-1200°C
Time: 1-4 hours
Atmosphere: N₂ or forming gas
Ramp rate: 5-10°C/min

Result: Bond energy >2 J/m² (fractures Si, not bond)
```

### Critical Requirements

**Surface Quality:**
```
Parameter          Specification
──────────────────────────────────
Roughness (Ra)     <0.5 nm
Particle count     <0.1 /cm²
Bow                <20 μm
TTV (thickness)    <2 μm
Flatness (SFQR)    <0.5 μm
```

**Surface Energy:**
- Hydrophilic: >70 mJ/m² (good bonding)
- Hydrophobic: <40 mJ/m² (poor bonding)
- Measure with contact angle (<5° needed)

### Void Formation and Mitigation

**Common Causes:**
1. Particles (>100 nm create voids)
2. Gas trapping (H₂ from OH condensation)
3. Surface roughness
4. Non-uniform contact

**Mitigation Strategies:**
- Ultra-clean processing (Class 1-10 cleanroom)
- High-temperature anneal (drives out H₂)
- Bonding in vacuum (reduces gas trapping)
- Plasma activation (increases surface energy)

### Low-Temperature Variants

**Plasma-Activated Bonding:**
- Temperature: 200-400°C
- Plasma: O₂, N₂, or Ar
- Application: CMOS-compatible integration
- Bond strength: 70-90% of high-temp

**Advantages:**
- Preserves CMOS metallization
- Reduces thermal stress
- Faster process (1 hour vs. 4 hours)

---

## 3. Eutectic Bonding

### Principle

Form low-melting-point alloy at interface of two metals. Most common: Au-Si eutectic (363°C).

**Phase Diagram:**
```
Temp (°C)
1000│           Si melts (1414°C)
    │          ╱
 600│         ╱
    │        ╱
 363│───●───╱  ← Eutectic point
    │  ╱ ╲ ╱
    │ ╱   ╲
   0└────────────► Composition
     Au  18.6%  Si
           Si
```

### Common Eutectic Systems

| System | Eutectic Temp | Composition | Bond Strength |
|--------|---------------|-------------|---------------|
| **Au-Si** | 363°C | 18.6 at% Si | 20-40 MPa |
| **Au-Sn** | 280°C | 80 wt% Au | 30-50 MPa |
| **Al-Ge** | 420°C | 54 at% Al | 15-25 MPa |
| **Cu-Sn** | 227°C | 40.5 wt% Sn | 25-45 MPa |

### Au-Si Eutectic Process

**Layer Deposition:**
```
Wafer 1: Sputter/evaporate Au (0.5-2 μm)
Wafer 2: Silicon (substrate or deposited poly-Si)

Optional: Barrier layer (Ti/Pt) prevents Au diffusion
```

**Bonding Conditions:**
```
Temperature: 380-420°C (above eutectic)
Pressure: 1-5 MPa
Time: 10-60 minutes
Atmosphere: Vacuum (10⁻⁵ mbar) or forming gas
```

**Temperature Profile:**
```
Temp
 420°C ──────────┐
              │  │ 30 min soak
              │  │
              │  └────────
 363°C ────────   Eutectic
              ╱    formation
   RT ───────╱
           └──┴────────► Time
          Heat Dwell Cool
```

### Advantages

- **Hermetic seal**: Excellent for vacuum packaging
- **Electrical conduction**: Au provides low-resistance path
- **Moderate temperature**: Compatible with many MEMS
- **Forgiving**: Tolerates particles and roughness
- **Gettering**: Au absorbs residual gases

### Limitations

- **Cost**: Au is expensive
- **Diffusion**: Au migrates into Si (use barrier layers)
- **Thickness variation**: Difficult to control bond line
- **CTE mismatch**: Au (14.2 ppm/K) vs. Si (2.6 ppm/K)

### Applications

**Vacuum-Packaged Gyroscopes:**
```
    Si cap wafer
    ═══════════════════
    Au ring (eutectic)
    ─────────────────── Hermetic seal at <1 mbar
    Device wafer (SOI)
```

**Power Devices:**
- Au-Si die attach
- Thermal management
- High-current connections

---

## 4. Adhesive Bonding (Polymer)

### Materials

| Polymer | Cure Temp | Bond Strength | Application |
|---------|-----------|---------------|-------------|
| **BCB** | 250°C | 10-15 MPa | RF MEMS, low-k |
| **SU-8** | 95-200°C | 5-10 MPa | Microfluidics |
| **PDMS** | 70-120°C | 1-3 MPa | Reversible bonding |
| **Polyimide** | 300-400°C | 12-20 MPa | High-temp seals |

### Process: BCB (Benzocyclobutene) Bonding

**Steps:**
```
1. Spin-coat BCB (2-20 μm thickness)
2. Soft bake: 150°C, 5 min
3. Align and contact wafers
4. Cure: 250°C, 1 hour, N₂
5. Cool slowly to prevent stress
```

**Advantages:**
- **Low temperature**: <250°C (CMOS-safe)
- **Planarization**: Fills gaps up to 50 μm
- **Low dielectric constant**: k = 2.65 (RF applications)
- **Simple process**: No special equipment

**Disadvantages:**
- Not hermetic (outgassing)
- Lower bond strength than metals
- Thermal stability limited to ~300°C
- Aging/creep over time

### Applications

**Microfluidic Devices:**
- SU-8 bonding for channels
- Optical transparency
- Bio-compatible

**3D Integration:**
- Low-temperature bonding
- Multi-chip stacking
- Wafer-level packaging

---

## 5. Glass Frit Bonding

### Principle

Use low-melting glass paste as intermediate layer. Glass melts, flows, and solidifies to form hermetic seal.

**Frit Composition:**
- Base glass: PbO-B₂O₃-SiO₂ or ZnO-B₂O₃-SiO₂
- Fillers: Al₂O₃, ZrO₂ (control CTE)
- Organic binder: Burns off during bonding

### Process

**1. Frit Deposition:**
- Screen printing (50-200 μm thick)
- Dispensing (for patterns)
- Dry at 150°C to remove solvents

**2. Bonding:**
```
Temperature: 400-550°C
Pressure: 0.1-1 MPa (light pressure)
Time: 30-60 minutes
Atmosphere: N₂ or air
```

**3. Seal Formation:**
```
Temp  Organic burnout  Frit melts    Seal forms
      ↓                ↓             ↓
 400°C│    ╱──────────╱─────────────╱
      │   ╱          ╱             ╱
      │  ╱          ╱             ╱
   RT└─╱──────────────────────────► Time
      0  10   20   30   40   50 min
```

### Advantages

- **High bond strength**: 15-30 MPa
- **Hermetic**: Leak rate <10⁻¹⁰ mbar·L/s
- **Gap filling**: Tolerates 10-50 μm variations
- **Electrical isolation**: Insulating seal
- **Low stress**: CTE-matched formulations available

### Applications

**Chip-Level Packaging:**
- Sensor cap attachment
- Getter integration
- Through-seal feedthroughs

**MEMS Devices:**
- Ceramic packages
- Hybrid integration
- Multi-sensor modules

---

## Bonding Characterization

### Bond Quality Tests

**1. Infrared (IR) Imaging:**
```
Purpose: Detect voids and unbonded areas
Method: Transmit IR light through bonded pair
Result: Voids appear as dark regions

Acceptance: <1% void area
```

**2. Acoustic Microscopy (SAM):**
- Ultrasonic waves detect delamination
- Resolution: ~10 μm
- Non-destructive

**3. Blade Test (Destructive):**
```
Method: Insert blade between wafers, measure crack propagation
Metric: Critical strain energy release rate (Gc)

Good bond: Gc > 2 J/m² (Si fractures)
Weak bond: Gc < 1 J/m² (bond fails)
```

**4. Pull Test:**
- Attach handles to bonded wafers
- Measure tensile strength
- Typical: 10-50 MPa depending on method

### Hermeticity Testing

**Helium Leak Test:**
```
Method: Pressurize cavity with He, measure leak rate
Specification: <10⁻¹² mbar·L/s (hermetic)
Equipment: Mass spectrometer
```

**Residual Gas Analysis (RGA):**
- Measure gas composition in sealed cavity
- Detect outgassing, leaks, getter performance

---

## Design Guidelines

### Bond Frame Design

**Minimum Dimensions:**
```
Parameter              Minimum    Typical
──────────────────────────────────────────
Frame width           500 μm      1-2 mm
Feature clearance     100 μm      200 μm
Alignment tolerance   ±5 μm       ±2 μm
Surface roughness     <5 nm       <1 nm (fusion)
Flatness (bow)        <50 μm      <20 μm
```

### Cavity Design

**Pressure Differential:**
```
For vacuum cavity:
Deflection = (P × a⁴) / (E × t³)

Where: P = pressure difference
       a = membrane radius
       E = Young's modulus
       t = thickness

Design: Keep deflection < 10% of gap
```

**Getter Integration:**
- Absorbs residual gases
- Maintains vacuum over lifetime
- Placement: Inside sealed cavity

### Thermal Management

**CTE Matching:**
```
Material      CTE (ppm/K)    Match to Si
───────────────────────────────────────
Silicon       2.6            Perfect
Pyrex 7740    3.2            Good
Borofloat     3.25           Good
Glass frit    Variable       Tunable
Gold          14.2           Poor
Aluminum      23.1           Very poor
```

**Stress Calculation:**
```
σ = ΔT × Δα × E / (1-ν)

Where: ΔT = temperature change
       Δα = CTE mismatch
       E = Young's modulus
       ν = Poisson's ratio

Critical: σ < 100 MPa (Si yield strength)
```

---

## Process Selection Guide

### Decision Matrix

```
Need hermetic seal? ────Yes──→ Anodic, Eutectic, or Glass Frit
    │
    No
    ↓
Need electrical ────Yes──→ Eutectic or Metal thermocompression
conduction?
    │
    No
    ↓
CMOS compatible? ───Yes──→ Low-temp fusion or Adhesive (BCB)
    │
    No
    ↓
High strength? ─────Yes──→ Fusion bonding
    │
    No
    ↓
Use Adhesive (simplest)
```

### Application Examples

| Device | Bonding Method | Why |
|--------|----------------|-----|
| Pressure sensor | Anodic | Hermetic + optical |
| Accelerometer | Eutectic | Vacuum packaging |
| SOI wafer | Fusion | Highest quality |
| Microfluidics | Adhesive | Low temp, simple |
| Gyroscope | Eutectic | Vacuum + conduction |
| RF MEMS | BCB | Low-k dielectric |

---

## Common Issues and Solutions

### Problem: Voids at Bond Interface

**Causes:**
- Particles or contamination
- Surface roughness
- Gas entrapment
- Non-uniform pressure

**Solutions:**
- Ultra-clean processing
- Improve CMP quality
- Bond in vacuum
- Optimize pressure distribution

### Problem: Wafer Breakage

**Causes:**
- Excessive thermal stress (CTE mismatch)
- Rapid temperature changes
- Thin wafers (<200 μm)

**Solutions:**
- Match materials (CTE)
- Slow ramp rates (<5°C/min)
- Carrier wafer support

### Problem: Poor Hermetic Seal

**Causes:**
- Incomplete bonding
- Cracks in seal frame
- Outgassing from polymers

**Solutions:**
- Increase bonding time/temp
- Wider bond frames
- Pre-bake to remove volatiles

---

## Cost Comparison

### Equipment Costs

| Method | Equipment Cost | Throughput |
|--------|----------------|------------|
| Anodic | $200k-500k | 10-20 wafers/hour |
| Fusion | $500k-2M | 5-10 wafers/hour |
| Eutectic | $300k-800k | 5-15 wafers/hour |
| Adhesive | $100k-300k | 20-50 wafers/hour |

### Process Costs (per 150 mm wafer)

```
Method      Materials  Labor  Equipment  Total
─────────────────────────────────────────────
Anodic      $5        $10    $15        $30
Fusion      $2        $20    $25        $47
Eutectic    $20       $15    $20        $55
Adhesive    $15       $8     $10        $33
```

---

## Summary Table

| Method | Temp | Hermetic | Conduct | Complexity | Best For |
|--------|------|----------|---------|------------|----------|
| **Anodic** | Medium | Yes | No | Low | Si-glass sensors |
| **Fusion** | High | Yes | Variable | High | SOI, high quality |
| **Eutectic** | Medium | Yes | Yes | Medium | Vacuum packaging |
| **Adhesive** | Low | No | No | Low | Prototyping, microfluidics |
| **Glass Frit** | Medium | Yes | No | Medium | Ceramic packages |

---

## References

1. **Niklaus, F., et al.** - "Adhesive Wafer Bonding" *J. Appl. Phys.* 99, 031101 (2006)
2. **Wallis, G., Pomerantz, D.I.** - "Field Assisted Glass-Metal Sealing" *J. Appl. Phys.* 40, 3946 (1969)
3. **Tong, Q.-Y., Gösele, U.** - *Semiconductor Wafer Bonding* (Wiley, 1999)
4. **Schmidt, M.A.** - "Wafer-to-Wafer Bonding for Microstructure Formation" *Proc. IEEE* 86(8), 1998

---

## Related Documentation

- [SOI Processes](./soi-processes.md) - Fusion bonding for SOI
- [Pressure Sensors](./pressure-sensors.md) - Anodic bonding application
- [Packaging](../06-packaging/) - Die-level bonding
- [Wet Etching](./wet-etching.md) - Cavity formation before bonding

---

**Next Steps:**
1. Determine bonding requirements (hermetic, conductive, temperature)
2. Select appropriate bonding method
3. Design bond frames and alignment marks
4. Plan characterization tests

**Document Status:** Complete  
**Last Updated:** December 2025  
**Part of:** [Silicon Fabrication Handbook](https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook)
