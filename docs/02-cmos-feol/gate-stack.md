# Gate Stack Formation: The Heart of the MOSFET

## Introduction

The gate stack is the most critical structure in a MOSFET transistor, controlling the flow of current between source and drain. Modern gate stacks have evolved from simple SiO₂/polysilicon structures to complex high-κ metal gate (HKMG) systems that enable continued device scaling. This chapter covers gate dielectric formation, gate electrode deposition, and the transition to advanced materials.

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
4. **Uniformity**: <3

## Reliability and Degradation Mechanisms

### Bias Temperature Instability (BTI)
- **NBTI (Negative BTI)**: Occurs in PMOS devices due to hole trapping in HfO₂.
- **PBTI (Positive BTI)**: Occurs in NMOS devices due to electron trapping.
- **Impact**: Threshold voltage shift (ΔV_th), reduced drive current, long-term reliability issues.

**Equation (empirical model):**
$$
\Delta V_{th} \propto t^n \cdot \exp\left(-\frac{E_a}{kT}\right)
$$
Where:
- \(t\) = stress time  
- \(n\) = time exponent (0.15–0.25)  
- \(E_a\) = activation energy (~0.1–0.2 eV)

---

### Hot Carrier Injection (HCI)
- High-energy carriers damage the Si/oxide interface.
- Leads to mobility degradation and increased interface trap density.
- More severe in short-channel devices.

---

### Stress-Induced Leakage Current (SILC)
- Trap-assisted tunneling through ultra-thin oxides.
- Increases standby power consumption.
- Mitigation: optimized annealing and defect passivation.

---

## Integration Challenges

### Thermal Budget
- HKMG stacks are sensitive to high-temperature steps.
- **Gate-last process** avoids exposing HfO₂ to >1000°C anneals.

### Work Function Variability
- TiN composition fluctuations → threshold voltage variation.
- Requires precise control of deposition parameters.

### Scaling to Sub-10nm Nodes
- FinFETs and Gate-All-Around (GAA) require:
  - 100% conformal ALD deposition
  - Void-free gap fill
  - Uniform work function on 3D surfaces

---

## Future Directions

### 2D Material Channels
- MoS₂, WS₂, and other transition metal dichalcogenides.
- Challenge: achieving low-defect interfaces with high-κ dielectrics.

### Ferroelectric HfO₂
- Polarization switching enables **FeFETs** (non-volatile memory).
- Potential for embedded memory in logic devices.

### Gate-All-Around (GAA) Nanosheets
- Gate stack fully wraps nanosheet channels.
- Requires ultra-conformal ALD and advanced gap-fill techniques.

### Carbon-Based Electrodes
- Graphene or CNT gates for ultimate scaling.
- Still experimental, but promising for ultra-low resistance.

---

## Characterization Techniques

### Electrical
- **C-V measurements**: Extract EOT, interface trap density.
- **I-V measurements**: Leakage current, breakdown voltage.

### Physical
- **TEM cross-sections**: Layer thickness and uniformity.
- **XPS**: Chemical composition and bonding states.
- **AFM**: Surface roughness.

### Reliability Testing
- **TDDB**: Time-dependent dielectric breakdown.
- **BTI stress tests**: Accelerated lifetime prediction.
- **Charge-to-breakdown (Q_BD)**: Robustness metric.

---



