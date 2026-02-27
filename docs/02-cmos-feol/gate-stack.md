# Gate Stack Formation: The Heart of the MOSFET

## Table of Contents
- [Introduction](#introduction)
- [MOSFET Gate Stack Fundamentals](#mosfet-gate-stack-fundamentals)
  - [Basic Structure and Function](#basic-structure-and-function)
  - [Gate Capacitance](#gate-capacitance)
  - [Equivalent Oxide Thickness (EOT)](#equivalent-oxide-thickness-eot)
  - [Key Gate Stack Requirements](#key-gate-stack-requirements)
- [Traditional SiO₂ Gate Oxide](#traditional-sio₂-gate-oxide)
  - [Thermal Oxidation Process](#thermal-oxidation-process)
  - [Deal-Grove Oxidation Model](#deal-grove-oxidation-model)
  - [Oxide Quality Characterization](#oxide-quality-characterization)
  - [Limitations of SiO₂](#limitations-of-sio₂)
- [High-κ Dielectrics](#high-κ-dielectrics)
  - [Material Selection Criteria](#material-selection-criteria)
  - [Interfacial Layer (IL) Formation](#interfacial-layer-il-formation)
  - [HfO₂ Deposition by Atomic Layer Deposition (ALD)](#hfo₂-deposition-by-atomic-layer-deposition-ald)
  - [Post-Deposition Anneal (PDA)](#post-deposition-anneal-pda)
  - [Advanced High-κ Materials](#advanced-high-κ-materials)
- [Gate Electrode Materials](#gate-electrode-materials)
  - [Polysilicon Gates (Legacy >45nm)](#polysilicon-gates-legacy-45nm)
  - [Metal Gate Electrodes](#metal-gate-electrodes)
  - [Gate-Last (Replacement Gate) Process](#gate-last-replacement-gate-process)
- [Complete HKMG Stack Structure](#complete-hkmg-stack-structure)
  - [Layer-by-Layer Breakdown](#layer-by-layer-breakdown)
  - [FinFET Gate Stack](#finfet-gate-stack)
- [Gate Patterning](#gate-patterning)
  - [Critical Dimension (CD) Control](#critical-dimension-cd-control)
  - [Patterning Challenges](#patterning-challenges)
  - [Etch Process](#etch-process)
- [Reliability and Degradation Mechanisms](#reliability-and-degradation-mechanisms)
  - [Bias Temperature Instability (BTI)](#bias-temperature-instability-bti)
  - [Time-Dependent Dielectric Breakdown (TDDB)](#time-dependent-dielectric-breakdown-tddb)
  - [Hot Carrier Injection (HCI)](#hot-carrier-injection-hci)
- [Work Function Engineering](#work-function-engineering)
  - [Dual Work Function Gates](#dual-work-function-gates)
  - [Multi-Threshold Devices](#multi-threshold-devices)
- [Process Integration Challenges](#process-integration-challenges)
  - [Thermal Budget Management](#thermal-budget-management)
  - [Contamination Control](#contamination-control)
  - [Interface Engineering](#interface-engineering)
- [Metrology and Characterization](#metrology-and-characterization)
  - [Electrical Characterization](#electrical-characterization)
  - [Physical Characterization](#physical-characterization)
- [Advanced Topics](#advanced-topics)
  - [Gate-All-Around (GAA) Transistors](#gate-all-around-gaa-transistors)
  - [Ferroelectric FETs (FeFETs)](#ferroelectric-fets-fefets)
- [Summary](#summary)
- [Further Reading](#further-reading)
  - [Textbooks](#textbooks)
  - [Seminal Papers](#seminal-papers)
  - [Review Articles](#review-articles)
  - [Standards](#standards)

## Introduction

The gate stack is the most critical structure in a MOSFET transistor, controlling the flow of current between source and drain. Modern gate stacks have evolved from simple SiO₂/polysilicon structures to complex high-κ metal gate (HKMG) systems that enable continued device scaling. This chapter covers gate dielectric formation, 
gate electrode deposition, and the transition to advanced materials.

> **Key Concept**: The gate stack must provide excellent capacitive coupling while minimizing leakage current and maintaining thermal stability through all subsequent processing steps.

## MOSFET Gate Stack Fundamentals

### Basic Structure and Function

```
Traditional Gate Stack (>90nm):        Modern HKMG Stack (<28nm):

   Poly-Si Gate (150nm)                Metal Gate (10nm TiN/TaN)
   ══════════════════                  ══════════════════
   SiO₂ (1.5-3nm)                      HfO₂ (2-3nm)
   ──────────────────                  ──────────────────
   IL (Interfacial Layer, 0.5-1nm)
   ══════════════════                  ──────────────────
   Silicon Channel                     Silicon Channel
   ──────────────────                  ──────────────────
```

### Gate Capacitance

The gate controls the channel through capacitive coupling:

$$
C_{ox} = \frac{\varepsilon_0 \varepsilon_r}{t_{ox}}
$$

Where:
- **C_ox** = Gate oxide capacitance per unit area [F/cm²]
- **ε₀** = Vacuum permittivity (8.854×10⁻¹⁴ F/cm)
- **ε_r** = Relative dielectric constant
- **t_ox** = Physical oxide thickness

**Drive Current** depends on C_ox:
$$
I_D \propto C_{ox} \times (V_{GS} - V_{th})
$$

Higher C_ox → Higher drive current → Faster transistor

### Equivalent Oxide Thickness (EOT)

For high-κ dielectrics, we use EOT to compare to SiO₂:

$$
EOT = t_{physical} \times \frac{\varepsilon_{SiO_2}}{\varepsilon_{high-\kappa}}
$$

**Example**:
```
HfO₂: ε_r = 25, t_physical = 2.5nm
SiO₂: ε_r = 3.9

EOT = 2.5nm × (3.9/25) = 0.39nm

Electrical performance of 0.39nm SiO₂
Physical robustness of 2.5nm film!
```

### Key Gate Stack Requirements

| Property | Requirement | Typical Value |
|----------|-------------|---------------|
| EOT | Minimize for drive | 0.5-1.5nm (advanced) |
| Leakage current | <1 A/cm² | 10⁻³-1 A/cm² @ V_dd |
| Breakdown field | >8 MV/cm | 10-15 MV/cm |
| Interface trap density (D_it) | <10¹¹ cm⁻²eV⁻¹ | 10¹⁰ cm⁻²eV⁻¹ |
| Fixed charge | <10¹¹ cm⁻² | 10¹⁰ cm⁻² |
| Thermal stability | Survive 1000°C | Up to 1050°C |
| Threshold voltage (V_th) | Controlled by work function | 0.2-0.5V |

## Traditional SiO₂ Gate Oxide

### Thermal Oxidation Process

**Most common method for legacy nodes (≥65nm)**:

#### Dry Oxidation

**Reaction**:
```
Si + O₂ → SiO₂

Temperature: 900-1100°C
Ambient: Pure O₂
Growth rate: 10-30 nm/hour (slower but higher quality)
```

**Process Setup**:
```
   O₂ inlet
      ↓
  ┌─────────────┐
  │   Furnace   │  Temperature: 1000°C
  │  (quartz    │  
  │   tube)     │  ← Wafers (50-150 in batch)
  │             │
  └─────────────┘
      ↓
   Exhaust
   
Time: 30-60 minutes for 3-5nm oxide
```

**Advantages**:
- Excellent interface quality (low D_it)
- High breakdown strength
- Uniform across wafer
- Low fixed charge

#### Wet Oxidation

**Reaction**:
```
Si + 2H₂O → SiO₂ + 2H₂

Temperature: 900-1000°C
Ambient: H₂O vapor (steam)
Growth rate: 100-300 nm/hour (faster, lower quality)
```

**H₂O Generation**:
```
Method 1: Bubbler
   O₂ → Water bath (95°C) → H₂O/O₂ mix → Furnace
   
Method 2: Pyrogenic (in-situ combustion)
   H₂ + O₂ → 2H₂O (at furnace inlet)
   Ratio: 2:1 H₂:O₂
```

**Use Cases**:
- Thick field oxides (200-500nm)
- Isolation structures
- Passivation layers

### Deal-Grove Oxidation Model

**Governing Equation**:
$$
x_{ox}^2 + A x_{ox} = B(t + \tau)
$$

Where:
- **x_ox** = Oxide thickness
- **t** = Oxidation time
- **A** = Linear rate constant (related to reaction rate)
- **B** = Parabolic rate constant (related to diffusion)
- **τ** = Accounts for initial oxide

**Growth Regimes**:

```
Thickness (nm)
     |          Parabolic regime
1000 |            (diffusion limited)
     |          ╱
     |        ╱
 100 |      ╱
     |    ╱  Linear regime
     |  ╱    (reaction limited)
  10 |╱_______________________ Time
     0   1   10  100  1000 (min)
     
Thin oxides (<30nm): Linear growth
Thick oxides (>100nm): Parabolic growth
```

**Rate Constants** (1000°C):

| Ambient | B (nm²/hr) | A (nm) | Growth Type |
|---------|------------|--------|-------------|
| Dry O₂ | 35 | 165 | Slow, high quality |
| Wet O₂ | 400 | 25 | Fast, lower quality |

### Oxide Quality Characterization

#### Interface Trap Density (D_it)

**Measurement**: High-frequency C-V and conductance methods

```
D_it vs. Energy in bandgap:

D_it (cm⁻²eV⁻¹)
     |
10¹² |    ╱     ╲
     |   ╱       ╲
10¹¹ |  ╱         ╲
     | ╱___________╲___
10¹⁰ |_________________ E_v  E_i  E_c
     
Good oxide: D_it < 10¹¹ at midgap
Poor oxide: D_it > 10¹² (causes Vth shift, subthreshold slope degradation)
```

#### Breakdown Characteristics

**Time-Dependent Dielectric Breakdown (TDDB)**:
```
Stress at elevated voltage and temperature
      ↓
Measure time to failure
      ↓
Extrapolate to operating conditions

E-model: t_BD ∝ exp(-γE)
1/E-model: t_BD ∝ exp(β/E)

Where:
t_BD = Time to breakdown
E = Electric field
γ, β = Material constants
```

**Typical Specs**:
- Breakdown field: >10 MV/cm
- TDDB lifetime: >10 years at operating conditions
- Charge-to-breakdown (Q_BD): >1 C/cm²

### Limitations of SiO₂

**Scaling Crisis at ~1.2nm Physical Thickness**:

1. **Direct Tunneling Leakage**:
   ```
   Leakage current (A/cm²)
        |
   10²  |             ╱
        |            ╱
   10⁰  |          ╱  Direct tunneling
        |        ╱    dominates
   10⁻² |      ╱
        |    ╱
   10⁻⁴ |__╱____________ 
        0  1  2  3  4  Thickness (nm)
        
   At 1nm: J_leak > 1 A/cm² (unacceptable!)
   Power = V × I × Area (battery dies in minutes)
   ```

2. **Variability**: Few atomic layers → statistical variation

3. **Reliability**: Thin oxide more susceptible to defects

**Solution**: High-κ dielectrics

## High-κ Dielectrics

### Material Selection Criteria

**Thermodynamic Stability**:

Materials must be stable in contact with Si:

```
Band Diagram Requirements:

     E_c (Si)
   ──────────── Conduction band
        Δ > 1eV (barrier for electrons)
   ══════════  High-κ dielectric
        Δ > 1eV (barrier for holes)
   ──────────── Valence band
     E_v (Si)
```

**Candidate Materials**:

| Material | ε_r (κ) | Band Gap (eV) | ΔE_c (eV) | ΔE_v (eV) | Status |
|----------|---------|---------------|-----------|-----------|---------|
| SiO₂ | 3.9 | 9.0 | 3.5 | 4.4 | Standard (legacy) |
| Si₃N₄ | 7.5 | 5.0 | 2.4 | 2.0 | Too leaky |
| Al₂O₃ | 9 | 8.8 | 2.8 | 3.4 | Good, but mobility loss |
| **HfO₂** | **25** | **5.8** | **1.5** | **3.4** | **Industry standard** |
| ZrO₂ | 25 | 5.8 | 1.4 | 3.4 | Similar to HfO₂ |
| La₂O₃ | 30 | 6.0 | 2.3 | 2.5 | Hygroscopic |
| HfSiOₓ | 15 | 6.5 | 2.0 | 3.0 | HfO₂/SiO₂ alloy |

**Why HfO₂ Won**:
1. High κ (25) → Thick physical layer for low leakage
2. Adequate band offsets (>1 eV)
3. Thermodynamically stable on Si (with IL)
4. CMOS process compatible
5. Established supply chain

### Interfacial Layer (IL) Formation

**Critical Component**: SiO₂ or SiOₓ layer between Si and high-κ

```
Metal Gate
══════════════════
HfO₂ (1.5-2nm)
──────────────────
IL - SiO₂ (0.5-1nm)  ← Critical for interface quality
══════════════════
Silicon
──────────────────
```

**Why IL is Necessary**:
1. **Interface quality**: HfO₂ directly on Si has high D_it
2. **Stability**: Prevents HfSi formation (low-κ)
3. **Mobility**: Maintains good carrier mobility

**Formation Methods**:

**Chemical Oxidation**:
```
Ozone (O₃) exposure at 300°C
or
NO₂ ambient at 400-500°C
      ↓
Forms 0.5-1nm SiO₂
      ↓
Controlled, reproducible
```

**Thermal Budget**:
```
Cannot use high-temperature oxidation (>600°C)
  → Would grow thick SiO₂ (defeats purpose of high-κ)
  
Use low-temperature methods:
  - Chemical oxidation: 300-500°C
  - ALD naturally forms IL during HfO₂ deposition
```

### HfO₂ Deposition by Atomic Layer Deposition (ALD)

**Why ALD?**
- Atomic-level thickness control
- Excellent conformality (>95% on 3D structures)
- Uniform across wafer (<1% variation)
- Low temperature (250-350°C)

**ALD Cycle**:

```
Step 1: Precursor Pulse
   HfCl₄ or TDMA-Hf + Surface -OH groups
        ↓
   Hf-O-Surface (monolayer adsorption)
        ↓
   Purge with N₂
   
Step 2: Oxidant Pulse
   H₂O or O₃ + Hf-surface
        ↓
   Forms HfO₂ + regenerates -OH groups
        ↓
   Purge with N₂
   
Repeat cycles until target thickness reached
```

**Process Parameters**:
```
Temperature: 250-350°C
Precursor: HfCl₄ (most common) or TDMA-Hf
Oxidant: H₂O or O₃
Cycle time: 3-5 seconds per cycle
Growth rate: 0.8-1.2 Å per cycle
Cycles for 2nm: ~20 cycles
```

**Advantages over CVD**:
- Self-limiting reactions (thickness = # cycles)
- No thickness non-uniformity
- Perfect conformality (critical for FinFETs)

**Film Properties**:
```
As-deposited: Amorphous HfO₂
After anneal: Crystallizes (monoclinic or tetragonal)
Crystalline grain size: 5-10nm
Critical: Control crystallization to avoid high leakage paths
```

### Post-Deposition Anneal (PDA)

**Purpose**: Densify film, reduce defects, control IL growth

```
Method: Rapid Thermal Anneal (RTA)
Temperature: 600-1000°C
Time: 10-60 seconds
Ambient: N₂, NH₃, or N₂O

Effects:
1. Densification → Reduces leakage
2. IL thickening → Increases EOT (trade-off)
3. Crystallization → Can increase leakage if uncontrolled
4. Defect passivation → Reduces D_it
```

**Optimization Challenge**:
```
Low temperature anneal:
  (+) Thin IL
  (−) High defects, poor density
  
High temperature anneal:
  (+) Good quality HfO₂
  (−) Thick IL (negates high-κ advantage)
  
Optimal: 800-1000°C, 10-30 seconds
```

### Advanced High-κ Materials

**HfSiOₓ (Hafnium Silicate)**:
```
Composition: Hf_x Si_(1-x) O₂
x = 0.3-0.7 (30-70% Hf)

Advantages:
- Higher crystallization temperature than pure HfO₂
- Reduced leakage (remains amorphous)
- κ = 12-18 (between SiO₂ and HfO₂)

Trade-off: Lower κ than pure HfO₂
```

**Rare Earth Doping**:
```
Add La, Dy, or Er to HfO₂

Benefits:
- Suppress crystallization
- Reduce oxygen vacancies (defects)
- Improve NBTI reliability
```

## Gate Electrode Materials

### Polysilicon Gates (Legacy >45nm)

#### Deposition

**Low-Pressure Chemical Vapor Deposition (LPCVD)**:
```
Reaction: SiH₄ → Si + 2H₂

Temperature: 580-650°C
Pressure: 200-400 mTorr
Deposition rate: 10-30 nm/min
Thickness: 100-200nm
Film: Polycrystalline (grain size 30-100nm)
```

**As-Deposited Properties**:
- Resistivity: ~10³ Ω·cm (too high!)
- Grain boundaries: Carrier scattering
- Requires heavy doping

#### Doping Methods

**1. In-Situ Doping** (during deposition):
```
Add PH₃ (n-type) or B₂H₆ (p-type) to SiH₄
      ↓
Doped poly-Si film deposited
      ↓
Uniform doping throughout film

Typical doping: 10²⁰ cm⁻³
Resistivity after doping: 500-1000 μΩ·cm
```

**2. Ion Implantation + Anneal**:
```
Deposit undoped poly-Si
      ↓
Pattern gate (lithography + etch)
      ↓
N-type implant (P or As) for NMOS regions
P-type implant (B) for PMOS regions
      ↓
RTA 900-1000°C to activate

Advantage: Dual work function (different Vth for NMOS/PMOS)
```

**3. POCl₃ Diffusion** (n-type only):
```
Expose poly-Si to POCl₃ vapor at 900°C
      ↓
Phosphorus diffuses into poly-Si
      ↓
Heavy n+ doping (>10²⁰ cm⁻³)

Simple but only n-type
```

#### Polysilicon Depletion Effect

**Problem at Thin Oxides**:

```
   Poly-Si gate (n+)
   ══════════════════
      Depletion region (~2nm at inversion)
   ──────────────────
   Gate oxide (1-2nm)
   ══════════════════
   Silicon channel
   
Effective capacitance:
1/C_total = 1/C_ox + 1/C_poly_depletion

Poly depletion adds ~0.3-0.5nm to EOT!
```

**Impact**:
- Reduces drive current (10-15%)
- Performance degradation
- Solved by metal gates (no depletion)

### Metal Gate Electrodes

**Transition Point**: 45nm node (Intel) to 28nm (others)

#### Work Function Requirements

**Definition**: Energy difference between metal Fermi level and vacuum

```
Work Function Engineering:

Vacuum level ──────────────────────
              ↑
              │ Φ_m (metal work function)
              ↓
Metal E_f ────────────────────────
              ↑
              │ Φ_B (barrier height)
              ↓
High-κ ───────────────────────────
              
Si E_c ───────────────────────────
              E_g (1.12 eV)
Si E_v ───────────────────────────
```

**Target Work Functions**:
```
NMOS: Φ_m ≈ 4.0-4.2 eV (near Si conduction band)
      → Low Vth, good electron conduction
      
PMOS: Φ_m ≈ 5.0-5.2 eV (near Si valence band)
      → Low |Vth|, good hole conduction

Si mid-gap: 4.6 eV (mid-point of bandgap)
```

#### Metal Gate Materials

**Early Candidates** (exhaustive screening 2000-2005):

| Material | Φ_m (eV) | For Device | Issues |
|----------|----------|------------|--------|
| Al | 4.1 | NMOS | Reacts with HfO₂ |
| Ta | 4.3 | NMOS | Oxidizes easily |
| **TiN** | **4.5-4.7** | **Mid-gap** | **Tunable, stable** |
| TaN | 4.7 | Mid-gap | Good stability |
| Mo | 4.5 | Mid-gap | High resistivity |
| Ru | 4.7 | Mid-gap | Expensive |
| TiAlN | 4.3-4.9 | Tunable | Complex composition |
| Pt | 5.3 | PMOS | Very expensive |
| Ni | 5.0 | PMOS | Silicide formation |

**Industry Standard**: TiN-based stacks

#### TiN Metal Gate

**Why TiN?**
1. Work function tunable: 4.3-5.0 eV (varies with deposition)
2. CMOS compatible (survives 1000°C anneal)
3. Good conductivity (50-200 μΩ·cm)
4. Excellent adhesion to HfO₂
5. Mature deposition technology

**Deposition Methods**:

**Physical Vapor Deposition (PVD)**:
```
DC or RF sputtering
Target: Ti
Ambient: N₂ + Ar
Temperature: 200-400°C
Thickness: 5-15nm
      ↓
Forms TiN film
Sheet resistance: 10-50 Ω/sq
```

**Atomic Layer Deposition (ALD)**:
```
Precursor: TiCl₄
Reactant: NH₃
Temperature: 350-450°C
      ↓
Superior conformality for FinFETs
Excellent thickness control
```

**Chemical Vapor Deposition (CVD)**:
```
Reaction: TiCl₄ + NH₃ → TiN + HCl + H₂
Temperature: 400-600°C
Good step coverage
```

#### Work Function Tuning

**Methods to Adjust Φ_m**:

**1. Composition Control**:
```
TiN (stoichiometric): Φ_m = 4.6 eV
Ti-rich TiN: Φ_m = 4.3-4.4 eV
N-rich TiN: Φ_m = 4.8-5.0 eV

Control by N₂/Ar ratio during sputtering
```

**2. Alloying**:
```
TiAlN: Add Al to shift work function
  Al content 0-30%:
    Φ_m = 4.3-4.9 eV (tunable)
    
TaN: Alternative mid-gap material
  Φ_m ≈ 4.7 eV
```

**3. Capping Layers**:
```
TiN base layer
    ↓
Thin capping layer (1-2nm):
  - TiAl cap → Lower Φ_m (NMOS)
  - TaN cap → Higher Φ_m (PMOS)
    ↓
Work function set by interface dipole
```

**4. Lanthanum Doping** (for NMOS):
```
La-doped HfO₂ or LaAlO₃ interface
    ↓
Creates interface dipole
    ↓
Shifts effective Φ_m by -0.3 to -0.5 eV
    ↓
Ideal for NMOS (lowers Vth)
```

### Gate-Last (Replacement Gate) Process

**For 28nm and below**: Gate stack patterned after S/D activation

```
Traditional Gate-First:           Gate-Last (Replacement):

1. Deposit gate stack             1. Deposit dummy gate (poly-Si)
2. Pattern gate                   2. Pattern dummy gate
3. S/D implants                   3. S/D implants + anneal (1000°C)
4. Anneal (1000°C)                4. Deposit ILD
   → Degrades high-κ!             5. CMP to expose dummy gate
5. Continue BEOL                  6. Remove dummy gate (wet etch)
                                  7. Deposit HKMG stack (no high temp!)
                                  8. CMP to planarize
                                  9. Continue BEOL

Advantage: HKMG never sees S/D anneal temperature
```

**Detailed Gate-Last Flow**:

```
Step 1-3: Dummy Gate Process
   Deposit poly-Si + hard mask
        ↓
   Pattern and etch
        ↓
   S/D extensions and implants
        ↓
   Anneal at 1050°C (poly-Si stable, HfO₂ would degrade)
        
Step 4-5: ILD and CMP
   Deposit 500nm SiO₂ (ILD)
        ↓
   CMP to expose poly-Si top
        ↓
   Poly-Si acts as CMP stop

Step 6: Dummy Gate Removal
   Wet etch: TMAH or H₃PO₄
        ↓
   Removes poly-Si selectively
        ↓
   Leaves trench where gate will be
   
Step 7-8: HKMG Deposition
   ALD HfO₂ (2nm) - conformal
        ↓
   ALD TiN (10nm) - conformal
        ↓
   CVD W or Al fill (bulk conductor)
        ↓
   CMP to remove excess metal
        ↓
   Final gate structure

Result: HKMG with minimal thermal budget!
```

## Complete HKMG Stack Structure

### Layer-by-Layer Breakdown

**Modern 14nm Logic HKMG Stack**:

```
        W or Al fill (bulk metal, 40-80nm)
        ═══════════════════════════════════
        TiN work function metal (8-12nm)
        ───────────────────────────────────
        TaN barrier layer (1-2nm, optional)
        ───────────────────────────────────
        HfO₂ high-κ dielectric (1.5-2.5nm)
        ═══════════════════════════════════
        IL (SiO₂ interfacial layer, 0.5-1nm)
        ───────────────────────────────────
        Silicon channel
        ═══════════════════════════════════
        
Total EOT: 0.6-1.0nm
Physical thickness: ~50-90nm
```

**Purpose of Each Layer**:

| Layer | Thickness | Function |
|-------|-----------|----------|
| W/Al fill | 40-80nm | Low resistance bulk conductor |
| TiN | 8-12nm | Work function setting, adhesion |
| TaN (opt) | 1-2nm | Diffusion barrier |
| HfO₂ | 1.5-2.5nm | High capacitance (high-κ) |
| IL (SiO₂) | 0.5-1nm | Interface quality |

### FinFET Gate Stack

**3D Structure Considerations**:

```
Top View:               Cross-Section:
                        
   Gate wraps            ╔══════╗ Gate
   around fin            ║ Fin  ║ wraps
                         ║(Si)  ║ around
   ═══╤═══               ║      ║ 3 sides
      │                  ╚══════╝
   ───┴───               
   Silicon               Gate controls channel
                         from 3 sides → Better control
```

**Requirements**:
1. **Conformal deposition**: ALD essential (not PVD)
2. **Fin height**: 30-50nm → Need 100% step coverage
3. **Work function uniformity**: Must be same on all fin surfaces
4. **Gap fill**: Between closely spaced fins (pitch 40-60nm)

**Stack Optimization**:
```
TiN thickness: Thinner than planar (5-8nm)
  → Avoid pinch-off between fins
  
W fill: Critical for gap fill
  → CVD W with good step coverage
  → Avoid voids between fins
```

## Gate Patterning

### Critical Dimension (CD) Control

**Gate Length = Channel Length = Technology Node**

```
Technology Node:  45nm  32nm  22nm  14nm  7nm
Gate Length:      35nm  26nm  18nm  14nm  7nm  (slightly smaller than node)
CD tolerance:     ±3nm  ±2nm  ±1.5nm ±1nm ±0.5nm

Tolerance tightens with scaling!
```

**Impact of CD Variation**:
```
ΔL = ±1nm on L = 14nm (±7%)
      ↓
ΔI_d ≈ 10-15% variation
      ↓
ΔV_th ≈ 20-50mV
      ↓
Frequency binning (chip speed variation)
```

### Patterning Challenges

**At 14nm and below**:

```
Challenge 1: Resolution Limit
  193nm ArFi: R_min ≈ 38nm (k₁=0.25)
  For 14nm: Need multi-patterning or EUV
  
Challenge 2: Line Edge Roughness (LER)
  LER (3σ): 2-4nm
  For 14nm gate: LER = 30% of CD!
  → Vth variation
  
Challenge 3: Line Width Roughness (LWR)
  Causes: Photoresist roughness, etch variation
  Impact: Device-to-device mismatch
```

**Solution - Self-Aligned Double Patterning (SADP)**:

```
Step 1: Core pattern (32nm pitch)
   ████    ████    ████
   
Step 2: Deposit spacer (8nm)
   ╔██╗  ╔██╗  ╔██╗
   ║██║  ║██║  ║██║
   
Step 3: Remove core
   ╔╗    ╔╗    ╔╗
   ║║    ║║    ║║
   
Step 4: Etch (spacers as mask)
   ██    ██    ██
   
Result: 16nm pitch (2× density)
Gate width = Spacer thickness
```

### Etch Process

**Gate Stack Etch Sequence**:

```
Layer to Etch:        Etch Chemistry:        Challenges:

W/Al fill             Cl₂/BCl₃/SF₆          High selectivity to TiN
  ↓                   RIE, 20 mTorr
  
TiN electrode         Cl₂/BCl₃/Ar           Anisotropic profile
  ↓                   Bias 300-500V         Sidewall protection
  
HfO₂ dielectric       BCl₃/CH₄ or          Low damage to Si
  ↓                   CxFy plasma           Minimal IL consumption
  
Stop on Si channel    Endpoint detect       Critical: Don't damage channel!
```

**Key Requirements**:
1. **Anisotropy**: Vertical sidewalls (>85°)
2. **Selectivity**: 20:1 to underlying layer
3. **Low damage**: Minimize plasma damage to HfO₂
4. **Uniformity**: <3% CD variation across wafer

## Reliability and Degradation Mechanisms

### Bias Temperature Instability (BTI)

#### Negative BTI (NBTI) - PMOS Degradation

**Mechanism**: Holes + stress → interface trap generation

```
Stress Conditions:
  V_gate = -1.5V (negative for PMOS)
  T = 125°C
  Time = hours to years
        ↓
  Si-H bonds at interface break
        ↓
  Creates interface traps (Si dangling bonds)
        ↓
  ΔV_th increases (more positive)
        ↓
  Device degrades over time
```

**Mathematical Model**:
$
\Delta V_{th} = A \times t^n \times \exp\left(\frac{E_a}{k_B T}\right) \times \exp(\gamma V_{ox})
$

Where:
- **A** = Pre-factor
- **n** = Time exponent (0.15-0.25)
- **E_a** = Activation energy (0.1-0.2 eV)
- **γ** = Field acceleration factor

**Typical Degradation**:
```
After 10 years at 85°C, V_dd:
  ΔV_th = 30-80mV (specification: <100mV)
  
HfO₂ generally better than SiO₂ for NBTI
```

#### Positive BTI (PBTI) - NMOS Degradation

**Mechanism**: Electrons trapped in high-κ bulk

```
Stress: V_gate = +1.5V, T = 125°C
      ↓
Electrons tunnel into HfO₂ traps (oxygen vacancies)
      ↓
Negative charge in dielectric
      ↓
ΔV_th increases (more positive)
```

**Key Difference from NBTI**:
- NBTI: Interface traps (permanent)
- PBTI: Bulk traps (partially recoverable)

**Mitigation**:
- La doping in HfO₂ (fills oxygen vacancies)
- Optimized annealing (reduce defects)
- Al₂O₃ capping layer

### Time-Dependent Dielectric Breakdown (TDDB)

**Failure Mode**: Catastrophic gate oxide failure

```
Percolation Model:
  Stress → Defect generation in dielectric
        ↓
  Defects accumulate over time
        ↓
  Defects form conductive path (percolation)
        ↓
  Gate shorts to channel (device dead)
```

**Lifetime Projection**:
$
t_{BD} = A \times \exp\left(\frac{\beta}{E_{ox}}\right)
$

**Accelerated Testing**:
```
Lab test: V_ox = 3V, T = 150°C → t_BD = 10 hours
          ↓ (extrapolate)
Operating: V_ox = 0.9V, T = 85°C → t_BD = 10 years

Acceleration factors: 10⁶-10⁹×
```

**Design Margins**:
- Target lifetime: >10 years
- Safety factor: 10× (design for 100 years)

### Hot Carrier Injection (HCI)

**Mechanism**: High-energy carriers damage gate oxide

```
High V_ds (drain voltage)
      ↓
Large lateral E-field near drain
      ↓
Carriers accelerated (become "hot")
      ↓
Hot carriers gain energy > barrier height
      ↓
Inject into gate oxide
      ↓
Create traps → ΔV_th, Δg_m (transconductance)
```

**Most Critical**: NMOS at V_gs ≈ V_ds/2 (peak substrate current)

**Mitigation**:
- LDD implants (reduce drain E-field)
- Lower V_dd (reduced at advanced nodes)
- Halo implants (increase channel doping near drain)

## Work Function Engineering

### Dual Work Function Gates

**Requirement**: Different Φ_m for NMOS vs. PMOS

```
NMOS:                    PMOS:
  Low Φ_m (4.1-4.3 eV)     High Φ_m (5.0-5.2 eV)
        ↓                          ↓
  Low V_th                     Low |V_th|
        ↓                          ↓
  High I_on                    High I_on
```

**Implementation Strategies**:

#### 1. Dual Metal Deposition

```
Process:
  1. Deposit metal A (NMOS regions)
  2. Mask and etch (remove from PMOS)
  3. Deposit metal B (PMOS regions)
  4. Pattern gates
  
Metals:
  NMOS: TiAlN (Φ_m = 4.3 eV)
  PMOS: TiN + TaN cap (Φ_m = 5.1 eV)
  
Challenge: Two metal depositions → Cost
```

#### 2. Single Metal + Doping

```
Process:
  1. Deposit TiN (mid-gap, Φ_m = 4.6 eV)
  2. Implant La into NMOS regions
     → La shifts Φ_m down to 4.2 eV
  3. PMOS regions remain at 4.6 eV
  4. (Optional) P implant into PMOS → 5.0 eV
  
Advantage: Single metal deposition
Challenge: Ion implant damage control
```

#### 3. Capping Layers

```
Process:
  1. Deposit base TiN on both NMOS and PMOS
  2. Deposit TiAl cap on NMOS only
     → Interface dipole lowers Φ_m
  3. Deposit TaN cap on PMOS only
     → Raises Φ_m
     
Advantage: Precise control, thin caps (1-2nm)
```

### Multi-Threshold Devices

**Different V_th for Different Applications**:

| Device Type | V_th (V) | Application | Gate Stack |
|-------------|----------|-------------|------------|
| High V_th (HVT) | 0.5-0.7 | Standby, low leakage | Mid-gap metal |
| Standard V_th (SVT) | 0.3-0.5 | General logic | Tuned Φ_m |
| Low V_th (LVT) | 0.15-0.3 | Critical path, speed | Band-edge metal |

**Implementation**:
```
Use different gate metals or cap layers:
  HVT: No cap (mid-gap)
  SVT: Thin cap
  LVT: Thick cap or different metal
  
All on same wafer! → Mask adder for each V_th type
```

## Process Integration Challenges

### Thermal Budget Management

**Problem**: High-κ materials degrade at high temperatures

```
Temperature Effects on HfO₂:

T < 600°C: Stable, amorphous
T = 600-800°C: Begins crystallization
T > 800°C: Full crystallization → grain boundaries → leakage paths
T > 1000°C: Reaction with Si (forms HfSi, low-κ)

IL growth:
T = 800°C, 10s: +0.2nm IL
T = 1000°C, 10s: +0.5nm IL → Negates high-κ advantage!
```

**Solutions**:
1. **Gate-Last**: Avoid S/D anneal (most effective)
2. **Laser Anneal**: Localized heating (S/D only, not gate)
3. **Low-Temperature Processes**: Minimize thermal steps after gate
4. **Capping Layers**: Al₂O₃ cap prevents HfO₂ crystallization

### Contamination Control

**Critical Impurities**:

| Contaminant | Source | Effect | Control |
|-------------|--------|--------|---------|
| Carbon | Organic precursors | Reduces κ, increases leakage | High-purity precursors, O₃ cleans |
| Hydrogen | H₂O, NH₃ | Interface states | Deuterium anneal (D replaces H, stronger bond) |
| Fluorine | Chamber residue | Etches high-κ | Dedicated chambers |
| Chlorine | TiCl₄, HfCl₄ | Corrosion, etching | Post-dep anneal removes Cl |

**Clean Room Requirements**:
- High-κ deposition: ISO 4 or better
- ALD chambers: <10 ppm O₂, H₂O (inert ambient)

### Interface Engineering

**Optimizing Si/SiO₂/HfO₂ Interface**:

```
Key Parameters:
  1. IL thickness: 0.5-1.0nm (trade-off)
     Too thin: High D_it
     Too thick: High EOT
     
  2. IL composition: SiO₂ vs. SiOₓN_y
     Pure SiO₂: Best interface
     SiOₓN_y: Better barrier to oxygen diffusion
     
  3. Forming gas anneal (FGA):
     H₂/N₂ or D₂/N₂ at 400-500°C
     Passivates interface traps (Si-H bonds)
     Deuterium (D) preferred: Stronger Si-D bond
```

**Surface Preparation Before ALD**:
```
1. Pre-clean:
   SC-1 (particle removal)
   HF dip (strip native oxide)
   SC-2 (metal removal)
   
2. Chemical oxide:
   O₃ or NO exposure
   Forms 0.5nm controlled SiO₂
   
3. ALD within 1 hour:
   Minimize native oxide regrowth
   
4. In-situ plasma treatment (optional):
   Ar or H₂ plasma (10s)
   Activates surface
```

## Metrology and Characterization

### Electrical Characterization

#### C-V (Capacitance-Voltage) Measurements

**Purpose**: Measure EOT, flat-band voltage, interface states

```
MOS Capacitor Structure:
   Metal dot (100×100 μm²)
   ═══════════════════
   HfO₂ + IL
   ───────────────────
   Silicon
   
Sweep V_gate: -2V to +2V
Measure C at each voltage
```

**C-V Curve Analysis**:
```
Capacitance
     |     
C_ox |════════════      Accumulation (high freq)
     |          ╲╲
     |            ╲╲    Depletion
     |              ╲╲
C_min|________________  Inversion
     |
     -2  -1   0  +1  +2  V_gate
     
Extract:
- EOT = ε₀ ε_SiO₂ / C_ox
- Flat-band voltage V_fb
- D_it from stretch-out
```

**High-Frequency vs. Low-Frequency**:
- High-freq (1 MHz): Minority carriers can't follow → Deep depletion
- Low-freq (quasi-static): Equilibrium → True C_min

#### I-V (Current-Voltage) Characteristics

**Leakage Current Measurement**:
```
Stress at V_gate = ±1.5V
Measure I_gate vs. time

Specifications:
  At V_dd (0.7-1.0V): J_gate < 1 A/cm²
  At 2× V_dd: J_gate < 10 A/cm²
  
Arrhenius plot: Extract activation energy
```

**Breakdown Testing**:
```
Voltage ramp: 0 → 10V at 0.1V/s
Detect: Sudden current increase (breakdown)

Hard breakdown: I jumps to compliance limit (catastrophic)
Soft breakdown: Gradual I increase (trap-assisted)
```

### Physical Characterization

#### Transmission Electron Microscopy (TEM)

**Cross-Section TEM**:
```
Sample prep:
  1. Cut thin slice (<100nm)
  2. Ion milling to electron transparency
  3. Image at 200kV
  
Resolution: <0.5nm (atomic resolution)

Measurements:
  - HfO₂ thickness: ±0.1nm precision
  - IL thickness: Count atomic layers
  - Interface roughness: <0.3nm
  - Crystallinity: Diffraction patterns
```

**High-Resolution TEM (HRTEM)**:
```
Can resolve individual atomic planes
Si lattice spacing: 0.54nm
Distinguish crystalline vs. amorphous HfO₂
Detect defects, grain boundaries
```

#### X-Ray Photoelectron Spectroscopy (XPS)

**Purpose**: Elemental composition and chemical states

```
Detect: Hf, O, Si, Ti, N ratios
Depth profile: Ar+ sputter + XPS (layer by layer)

Analysis:
  - Hf:O ratio (should be 1:2 for HfO₂)
  - Detect Hf-Si (bad: indicates reaction)
  - Carbon contamination level
  - Oxidation states (Hf⁴⁺, Ti²⁺, Ti³⁺, Ti⁴⁺)
```

#### Ellipsometry

**Non-Destructive Thickness Measurement**:
```
Principle: Measure polarization change of reflected light
Wavelength scan: 200-1000nm
      ↓
Model film stack (HfO₂/IL/Si)
      ↓
Extract: n (refractive index), k (extinction), thickness

Accuracy: ±0.1nm for thickness
Speed: <1 second per site
```

## Advanced Topics

### Gate-All-Around (GAA) Transistors

**Next Generation After FinFET** (3nm, 2nm nodes):

```
FinFET:                    GAA Nanosheet:
  ╔══════╗                    ══════════ Gate
  ║ Gate ║                 ╔════════════╗
  ║wraps ║                 ║ Nanosheet  ║ Gate completely
  ║3 sides║                ║  (channel) ║ surrounds channel
  ╚══════╝                 ╚════════════╝
                              ══════════ Gate
                              
Gate control: 3 sides → 4 sides (top, bottom, both sidewalls)
```

**HKMG Challenges**:
- ALD conformality: Must coat all 4 sides
- Gap fill: Between stacked nanosheets (vertical spacing 10-15nm)
- Work function uniformity: All surfaces must match
- Etch: Release nanosheets without damage

**Stack Structure**:
```
Stacked nanosheets (3-5 layers):

   ══════ Si nanosheet (5nm thick)
     Gate oxide + metal (wraps completely)
   ══════ Si nanosheet
     Gate oxide + metal
   ══════ Si nanosheet
   
Vertical spacing: 10-15nm
Gate length: 5-12nm
```

### Ferroelectric FETs (FeFETs)

**Emerging Technology**: Negative capacitance for lower V_th

```
Traditional:              FeFET:
   Metal gate              Metal gate
   ═══════════             ═══════════
   HfO₂                    HfZrO₂ (ferroelectric)
   ───────────             ═══════════
   IL                      HfO₂
   ═══════════             ───────────
   Si                      IL
                           ═══════════
                           Si
                           
Ferroelectric: C_FE < 0 (negative capacitance)
Total C = (1/C_FE + 1/C_ox)⁻¹ > C_ox (amplified!)
      ↓
Lower V_th, steeper subthreshold slope (SS < 60mV/dec)
```

**Materials**: Hf₀.₅Zr₀.₅O₂ (doped HfO₂)

**Status**: Research phase, promising for low-power

## Summary

Gate stack evolution represents one of the most significant materials transitions in semiconductor history:

**Historical Progression**:
```
1970s-2000: SiO₂ / Poly-Si
  - Simple, reliable
  - Scaled from 100nm to 1.2nm
  - Fundamental limit: Tunneling leakage
  
2001-2007: High-κ Research
  - Screened 100+ materials
  - HfO₂ emerged as winner
  - Solved materials integration
  
2007-present: HfO₂ / Metal Gate
  - 45nm: First production (Intel)
  - 28nm: Industry-wide adoption
  - 7nm: Gate-last standard
  - Sub-7nm: FinFET, GAA
```

**Key Achievements**:
- EOT scaled: 3nm → 0.5nm (6× improvement)
- Leakage reduced: 10⁵× vs. SiO₂ at same EOT
- Enabled 100× transistor density increase

**Current State (2024-2025)**:
- 3nm nodes: HfO₂/TiN standard
- EOT: 0.6-0.8nm
- Gate length: 5-7nm (GAA nanosheets)
- Reliability: >10 year lifetime at 85°C

**Future Challenges**:
- EOT scaling limit: ~0.5nm (interface IL dominates)
- Atomic-scale variability (few atoms matter)
- New channel materials (Ge, III-V) require different interfaces
- 2D materials (MoS₂, WSe₂): No dangling bonds, but integration?

The gate stack remains the technological heart of the transistor, enabling continued performance scaling even as physical dimensions approach atomic limits.

---

## Further Reading

### Textbooks
1. **"High-κ Gate Dielectrics"** - Huff & Gilmer (2005)
2. **"Physics of Semiconductor Devices"** - Sze & Ng (2007)
3. **"Advanced Gate Stacks for High-Mobility Semiconductors"** - Oktyabrsky (2007)

### Seminal Papers
1. "High-κ gate dielectrics: Current status and materials properties" - *J. Appl. Phys.* (2001)
2. "A 45nm Logic Technology with High-k+Metal Gate Transistors" - Intel, *IEDM* (2007)
3. "Hafnium oxide: A review of its properties and applications" - *J. Mater. Sci.* (2012)

### Review Articles
1. "The high-κ solution" - *IEEE Spectrum* (2007)
2. "Gate stack technology for nanoscale transistors" - *Mater. Today* (2008)

### Standards
- **SEMI P47**: High-κ dielectric film measurements
- **ASTM F1393**: C-V measurements of MOS structures

---


**Previous Chapter**: [Ion Implantation](ion-implantation.md)

**Document Version**: 2.0 
**Last Updated**: November 2025  
**Contributors**: Zeyad Mustafa
