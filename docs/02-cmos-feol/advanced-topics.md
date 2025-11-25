# Advanced FEOL Topics: FinFETs, Strain Engineering, and Beyond

## Introduction

As planar CMOS transistors approached fundamental scaling limits at the 22nm node, the semiconductor industry adopted revolutionary architectural and materials innovations to continue Moore's Law. This chapter covers three critical advanced topics that enabled scaling from 22nm to 3nm and beyond:

1. **FinFET Technology**: 3D transistor architecture with superior electrostatics
2. **Strain Engineering**: Mobility enhancement through mechanical stress
3. **Advanced HKMG Integration**: Materials and processes for sub-10nm nodes

These technologies represent the cutting edge of semiconductor manufacturing and are essential for understanding modern and future CMOS devices.

---

## Part 1: FinFET Technology

### The Scaling Crisis and Short-Channel Effects

#### Why Planar MOSFETs Failed Below 22nm

**Short-Channel Effects (SCE)** become dominant:

```
Planar MOSFET at 14nm:

Gate (20nm length)
══════════════════
   Gate Oxide (1nm)
──────────────────
S [n+] ← Channel (14nm) → [n+] D
       P-substrate
       
Problem: Gate loses control over channel!

Source/Drain electric fields penetrate channel
→ Drain-Induced Barrier Lowering (DIBL)
→ V_th degradation
→ Subthreshold slope > 90 mV/dec
→ Off-state leakage increases exponentially
```

**Key Short-Channel Effects**:

1. **Drain-Induced Barrier Lowering (DIBL)**:
   ```
   ΔV_th / ΔV_ds = DIBL coefficient
   
   Planar 14nm: DIBL > 200 mV/V (unacceptable!)
   FinFET 14nm: DIBL < 50 mV/V (acceptable)
   
   High DIBL → V_th varies with V_ds
              → Cannot turn transistor fully OFF
   ```

2. **Subthreshold Slope Degradation**:
   ```
   SS = ∂V_gs / ∂(log₁₀ I_d)
   
   Ideal: 60 mV/dec (at 300K)
   Planar 14nm: 80-120 mV/dec
   FinFET 14nm: 65-75 mV/dec
   
   Poor SS → Slow switching, high leakage
   ```

3. **Threshold Voltage Roll-Off**:
   ```
   V_th vs. Gate Length:
   
   V_th (V)
       |
   0.5 |────────────┐  Long channel
       |            │
   0.4 |            │
       |            └──┐  Planar
   0.3 |               └──╲╲
       |                   ╲╲ Roll-off
   0.2 |                     ╲╲ FinFET (controlled)
       └─────────────────────╲─── L_gate
         50    30    20    10nm
   ```

**Fundamental Limit**: Gate control parameter

$$
\lambda = \sqrt{\frac{\varepsilon_{Si} t_{Si} t_{ox}}{\varepsilon_{ox}}}
$$

Where:
- **λ** = Natural length (scaling parameter)
- **t_Si** = Silicon body thickness
- **t_ox** = Gate oxide thickness

**For good electrostatics**: L_gate > 3λ

```
Planar transistor: λ ≈ 8nm → Need L > 24nm
FinFET: λ ≈ 3nm → Can scale to L < 10nm
```

### FinFET Architecture

#### 3D Structure Overview

```
Top View (looking down):
                          
   ════════════════  Gate wraps around fin
        ║  ║         (like a hand around a finger)
   ═════╬══╬═════
        ║  ║
   ═════╬══╬═════
   
   Fin width: 5-8nm
   Fin height: 30-50nm
   Gate wraps 3 sides


Cross-Section (along gate):

      ┌────────────────┐  Gate electrode
      │                │
      │  ┌──────────┐  │
      │  │   Fin    │  │  Gate oxide wraps
      │  │  (Si)    │  │  around 3 sides
      │  │          │  │
      │  └──────────┘  │
      │                │
      └────────────────┘
      
   ═══════════════════  Buried Oxide (BOX)
   ───────────────────  Silicon substrate (SOI)
```

**Key Dimensions** (14nm node):
- Fin width (W_fin): 6-8nm
- Fin height (H_fin): 42-48nm
- Fin pitch: 42-48nm
- Gate length: 20nm (14nm "node" name is marketing)
- Number of fins: 2-12 per transistor (parallel)

#### Advantages Over Planar

**1. Superior Gate Control**:
```
Planar: Gate controls channel from 1 side (top)
        Electric field penetration: ~2× t_ox
        
FinFET: Gate controls from 3 sides
        Electric field wraps around fin
        Effective control: 3× better
        
Result: DIBL < 50mV/V, SS near ideal
```

**2. Reduced Leakage**:
```
Off-state current (I_off):
  Planar 14nm: 100 nA/μm
  FinFET 14nm: 10 nA/μm (10× improvement)
  
Enables lower V_dd → Lower power
```

**3. Higher Drive Current**:
```
For same footprint:
  Planar: Channel width = footprint width
  FinFET: Channel width = 2×H_fin + W_fin
          ≈ 2×45nm + 7nm = 97nm (per fin)
          
Multiple fins → Effective width = N_fins × 97nm

Example: 5 fins = 485nm effective width
```

**4. Better Scalability**:
```
Gate length scaling:
  Planar: Stopped at 22nm
  FinFET: 22nm → 14nm → 10nm → 7nm → 5nm
  
Current record: 3nm (Samsung, TSMC)
```

### FinFET Fabrication Process

#### SOI Wafer Preparation

**Silicon-On-Insulator Starting Material**:

```
Structure:
   ─────────────────  Top Si (50-60nm) ← Fins formed from this
   ═════════════════  Buried Oxide (BOX, 10-25nm) ← Isolation
   ─────────────────  Si substrate (725μm)
   
Why SOI?
  - BOX isolates fins electrically
  - Reduces parasitic capacitance
  - Prevents leakage paths under fin
  - Enables tall, narrow fins
```

**BOX Formation** (SIMOX or bonding):
```
Method 1: SIMOX (Separation by Implantation of Oxygen)
  Implant O+ at high dose/energy
       ↓
  Anneal at 1300°C
       ↓
  Buried SiO₂ layer forms
  
Method 2: Wafer Bonding (more common)
  Oxidize wafer 1 → Flip and bond to wafer 2
       ↓
  Grind/polish wafer 1 to 50nm thickness
       ↓
  SOI wafer complete
```

#### Fin Formation: Sidewall Image Transfer (SIT)

**Step-by-Step Process**:

```
Step 1: Mandrel Deposition and Pattern
   Deposit amorphous Si or SiN (80-120nm)
        ↓
   Lithography: Pattern lines at 2× final pitch
   (e.g., 80nm pitch for 40nm final pitch)
        ↓
   Etch mandrels
   
   Result:
   ████    ████    ████  Mandrel lines
   ──────────────────────


Step 2: Spacer Deposition (Conformal)
   LPCVD SiN (10-15nm) wraps around mandrels
        ↓
   ╔██╗  ╔██╗  ╔██╗
   ║██║  ║██║  ║██║  Spacers on sidewalls
   ╚══╝  ╚══╝  ╚══╝
   ──────────────────────
   
   Spacer width = Final fin width (6-8nm)


Step 3: Spacer Etch (Anisotropic RIE)
   Vertical etch removes horizontal spacer
        ↓
   Leaves spacers only on mandrel sidewalls
   
   ║    ║    ║
   ║    ║    ║  Spacers standing
   ║    ║    ║
   ──────────────────────


Step 4: Mandrel Removal (Selective Etch)
   Wet or dry etch removes mandrel
        ↓
   Leaves spacers as etch mask
   
   ║    ║    ║    ║    ║    ║
   ──────────────────────────
   
   Pitch doubled! 80nm → 40nm
   Width controlled by spacer thickness


Step 5: Fin Etch (DRIE)
   RIE using spacers as hard mask
        ↓
   Etch Si top layer (45-50nm deep)
        ↓
   Stop on BOX
   
   ║    ║    ║    ║    ║    ║  Fins formed!
   ══════════════════════════  BOX
   ──────────────────────────  Substrate
   
   Fin width: 6-8nm (precise!)
   Fin height: 45-50nm
   Aspect ratio: ~6:1


Step 6: Dummy Gate Deposition
   Deposit poly-Si (50nm)
        ↓
   Planarize to fin height
        ↓
   Pattern gates perpendicular to fins
   
      ████████  Dummy gate crosses fins
   ║    ║    ║
   ══════════════════════════
```

**Critical Control Parameters**:
```
Fin width variation: ±0.5nm (3σ)
  → Affects V_th, I_on/I_off ratio
  
Fin height uniformity: ±2nm across wafer
  → Affects effective width, matching
  
Sidewall angle: 88-92° (near vertical)
  → Poor angle → Gate control degradation
```

#### Shallow Trench Isolation (STI) for Fins

**Purpose**: Isolate adjacent fins electrically

```
Process:
1. Deposit thick oxide (SiO₂, 200-300nm)
   
   ████████  Dummy gate
   ║▓▓▓▓║  Oxide fills between fins
   ══════════════════════════

2. CMP to planarize
   Stop on dummy gate top
   
   ────────  After CMP
   ║    ║  Fin tops exposed
   ▓▓▓▓▓▓▓▓  Oxide between fins

3. STI recess etch
   Etch oxide ~20-30nm below fin top
        ↓
   Exposes fin sidewalls for gate wrapping
   
   ────────  Gate region
   ║    ║  Exposed fin (30nm)
   ▓▓▓▓▓▓▓▓  Recessed STI
   ══════════════════════════  BOX
```

**STI Recess Depth Critical**:
```
Too shallow: Gate doesn't wrap well → Poor control
Too deep: Parasitic corner transistors → Leakage

Optimal: 20-30nm below fin top
Uniformity: ±2nm across wafer
```

#### Source/Drain Formation: Epitaxial Growth

**Raised S/D Process**:

```
Step 1: Remove Dummy Gate
   Selective etch (wet or dry)
        ↓
   ║    ║  Fin exposed
   ▓▓▓▓▓▓▓▓  STI remains
   
Step 2: Source/Drain Recess (Optional)
   RIE etch fin top (5-10nm)
        ↓
   Creates recess for epi growth


Step 3: Selective Epitaxial Growth (SEG)
   
   For NMOS: Si:P epitaxy (in-situ doped)
     T = 600-700°C
     Precursors: SiH₄ or SiH₂Cl₂ + PH₃
     Doping: 1-3×10²⁰ cm⁻³ (n+)
        ↓
   For PMOS: SiGe:B epitaxy
     T = 550-650°C
     Precursors: SiH₄ + GeH₄ + B₂H₆
     Ge content: 25-40%
     Doping: 1-2×10²⁰ cm⁻³ (p+)
   
   
   Result (cross-section):
   
        ╔═══════════╗
        ║    Epi   ║  Raised S/D (diamond shape)
        ║  S/D     ║
   ║════╬═══════════╬════║  Fin
   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
   
   Epi grows from exposed Si surfaces
   No growth on oxide (selective!)
```

**Why Raised S/D?**
1. **Larger contact area**: Reduces contact resistance
2. **Strain transfer**: SiGe applies compressive strain to channel (PMOS)
3. **Lower series resistance**: Critical for short channels

**Facet Engineering**:
```
Epi growth forms diamond/hexagonal facets:
  {111} planes: Slowest growth
  {100} planes: Faster growth
  {110} planes: Fastest growth
  
Control by:
  - Temperature
  - Pressure
  - H₂/HCl partial pressure
  - Growth rate
  
Target: Symmetric facets for uniform strain
```

#### Gate Replacement (Gate-Last Process)

**High-κ Metal Gate (HKMG) Integration**:

```
Step 1: S/D Anneal (RTA)
   1000-1050°C, 1-5 seconds
        ↓
   Activates dopants in epi S/D
   Poly-Si dummy gate survives


Step 2: ILD Deposition and CMP
   Deposit SiO₂ or low-κ dielectric
        ↓
   CMP to expose dummy gate top


Step 3: Dummy Gate Removal
   Selective wet etch (TMAH)
        ↓
   Leaves trench where gate will be
   
        ┌─────────┐
        │ Trench  │  (gate cavity)
   ║    │         │    ║
   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


Step 4: Interfacial Layer Formation
   Chemical oxide (O₃ or NO)
        ↓
   0.5-1.0nm SiO₂ on fin surfaces


Step 5: High-κ Deposition (ALD)
   HfO₂ (1.5-2.5nm) - conformal!
        ↓
   Coats all fin surfaces uniformly
   
        ┌─HfO₂──┐
   ║════╬═══════╬════║
   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


Step 6: Work Function Metal (ALD/PVD)
   TiN or TiAlN (5-15nm)
        ↓
   Sets V_th (different for NMOS/PMOS)


Step 7: Metal Fill
   W or Al CVD
        ↓
   Fills gate trench


Step 8: CMP
   Remove excess metal
        ↓
   Gate complete!
   
      ══W══  Metal gate
   ║══TiN══║  Work function layer
   ║═HfO₂═║  High-κ
   ║══IL══║  Interface
   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
```

**Key Advantage**: HKMG never experiences S/D anneal temperature (1050°C)
- Prevents HfO₂ degradation
- Preserves interface quality
- Enables thinner EOT

### FinFET Design Considerations

#### Quantization of Effective Width

**Discrete Nature**:
```
Cannot tune width continuously like planar!

W_eff = N_fins × (2 × H_fin + W_fin)

Example (14nm node):
  H_fin = 45nm, W_fin = 7nm
  W_eff per fin = 2×45 + 7 = 97nm
  
For different drive strengths:
  1 fin:  97nm
  2 fins: 194nm  ← Must use 2, can't use 1.5!
  3 fins: 291nm
  4 fins: 388nm
  
Granularity: ±97nm (cannot adjust finer)
```

**Design Impact**:
- Standard cell library: Multiple fin counts
- Power optimization: Choose N_fins carefully
- Matching: Ensure equal number of fins

#### Fin Width Sensitivity

**V_th Dependence on W_fin**:

$$
V_{th} \propto \frac{1}{W_{fin}}
$$

```
W_fin variation:
  ±0.5nm on 7nm fin = ±7% variation
       ↓
  ΔV_th = ±30-50mV
       ↓
  Speed binning (fast/slow chips)
```

**Quantum Confinement**:
```
At W_fin < 5nm:
  Electron wavelength ≈ 5nm
       ↓
  Quantum confinement in fin width direction
       ↓
  Energy sub-bands form
       ↓
  Increased V_th, reduced mobility
  
Not just classical anymore!
```

#### Parasitic Capacitances

**New Parasitics vs. Planar**:

```
C_fringe: Fringe capacitance between gate and S/D
  FinFET: Higher due to 3D geometry
  Mitigation: Spacer thickness optimization
  
C_overlap: Gate-to-S/D overlap
  Similar to planar but 3D
  
C_bottom: Gate-to-substrate (through BOX)
  FinFET: Much lower (isolated by BOX)
  Advantage!
```

### Advanced FinFET Nodes

#### 7nm and 5nm Scaling

**Key Changes**:

| Parameter | 14nm | 10nm | 7nm | 5nm |
|-----------|------|------|-----|-----|
| Fin pitch (nm) | 42 | 34 | 27 | 27-30 |
| Gate pitch (nm) | 70 | 54 | 40-44 | 40-51 |
| Fin height (nm) | 42 | 53 | 53 | 50-55 |
| Fin width (nm) | 7-8 | 6-7 | 5-6 | 5-6 |
| Metal layers | 10-13 | 13-15 | 14-16 | 15-16 |

**Enabling Technologies**:
- EUV lithography (7nm/5nm): Single exposure for critical layers
- Advanced SAQP (self-aligned quadruple patterning)
- Improved epi processes (taller S/D, better faceting)

#### 3nm: FinFET Limit

**Challenges at 3nm**:
```
1. Fin width approaching atomic limit (4-5nm = ~20 Si atoms)
   → Statistical variation dominates
   
2. Gate length < 15nm
   → Even with tri-gate, SCE returns
   
3. Parasitic resistance dominates
   R_contact >> R_channel
   
Solution: Move to Gate-All-Around (GAA)
```

---

## Part 2: Strain Engineering

### Motivation: Mobility Enhancement

#### Carrier Mobility Fundamentals

**Drift Velocity and Mobility**:
$$
v_d = \mu \times E
$$

**Drive Current**:
$$
I_D = W \times \mu \times C_{ox} \times (V_{GS} - V_{th}) \times V_{DS}
$$

**Higher Mobility → Higher Current → Faster Transistor**

**Silicon Mobility** (Unstrained):
```
Room Temperature (300K):
  Electrons (n-type): μ_n = 1350 cm²/(V·s)
  Holes (p-type):     μ_p = 480 cm²/(V·s)
  
Hole mobility 3× lower than electrons!
  → PMOS slower than NMOS
  → Need strain to balance
```

### Strain Basics

#### Stress vs. Strain

**Definitions**:
```
Stress (σ): Force per unit area [Pa or GPa]
Strain (ε): Relative deformation [dimensionless or %]

Relationship (Hooke's Law):
  σ = E × ε
  
Where E = Young's modulus (GPa)
```

**Types**:

**Tensile Strain** (stretching):
```
   ←───→  Applied force
   ══════  Material stretched
   
ε > 0 (positive strain)
Lattice spacing increases
```

**Compressive Strain** (squeezing):
```
   →───←  Applied force
   ══════  Material compressed
   
ε < 0 (negative strain)
Lattice spacing decreases
```

#### Strain Effects on Band Structure

**Silicon Band Structure Changes**:

```
Unstrained Si:           Strained Si:
                         
Conduction band:         Tensile: Bands split
  ╱ ╲ ╱ ╲                  Lower effective mass
 ╱   ╲   ╲                  → Higher μ_n
                         
Valence band:            Compressive: Bands split
 ╲   ╱   ╱                  Lower effective mass
  ╲ ╱ ╲ ╱                   → Higher μ_p
```

**Key Effects**:
1. **Band splitting**: Lifts degeneracy
2. **Effective mass reduction**: m* decreases
3. **Scattering reduction**: Fewer available states

**Mobility Enhancement**:
```
NMOS: Tensile strain → +20-30% μ_n
PMOS: Compressive strain → +40-60% μ_p

At 1-2% strain (biaxial)
```

### Strain Techniques

#### 1. Global Strain: Strained Silicon on Relaxed SiGe

**Substrate Engineering**:

```
Structure:
   ────────────────  Strained Si (20nm) ← Tensile!
   ════════════════  Relaxed Si_(1-x)Ge_x (1-2μm)
   ────────────────  Graded SiGe buffer
   ════════════════  Si substrate
   
Process:
1. Grow graded SiGe buffer (x: 0 → 30%)
   Composition graded over 1-5μm
   Misfit dislocations confined to buffer
   
2. Grow relaxed Si_0.7Ge_0.3 (constant composition)
   Lattice constant larger than Si
   
3. Grow thin Si on top
   Si "wants" to match SiGe lattice
   → Si stretched (tensile strain)
   Strain: ~1.0-1.5% (biaxial)
```

**Advantages**:
-  Uniform strain across wafer
-  High strain level (>1%)
-  Both NMOS and PMOS benefit (for n-channel devices)

**Disadvantages**:
-   Expensive (thick epi, long growth time)
-   PMOS needs compressive (this is tensile)
-   Threading dislocations (defects)

**Status**: Used in 90nm-65nm nodes, mostly replaced by local strain

#### 2. Local Strain: Process-Induced Stress

**Principle**: Create stress locally in channel region after transistor formation

##### A. Strained Source/Drain (Most Common)

**For PMOS - SiGe S/D (Compressive)**:

```
Process:
1. After gate formation, recess S/D regions
   RIE etch Si (20-40nm deep)
   
   Gate
    ││
   ─┴┴─  Surface
   │  │  Recesses (etched)
   
2. Epitaxial SiGe growth
   Si_(1-x)Ge_x, x = 25-40%
   Temperature: 600-700°C
   In-situ B doping (p+)
   
   Gate
    ││
   ─┴┴─
   ╔══╗  SiGe S/D (larger lattice)
   
3. Strain transfer to channel
   SiGe "wants" to expand
   Constrained by surrounding Si
   → Compressive stress in channel
   
    Compression ← Gate → Compression
                 ═══
                Channel
                (compressed)

Mechanism:
  SiGe lattice (a_SiGe) > Si lattice (a_Si)
  Lattice mismatch: Δa/a = 4.2% × (Ge fraction)
  Example: 30% Ge → 1.26% mismatch
        ↓
  SiGe pushes on Si channel
        ↓
  Longitudinal compressive strain in channel
  Strain: 0.5-1.5% (depends on Ge%, recess depth)
```

**Optimization Parameters**:
```
Ge content:
  Higher Ge → More strain BUT harder to grow defect-free
  Optimal: 25-35% for 65nm-22nm nodes
           35-50% for 14nm-7nm nodes
           
Recess depth:
  Deeper → More strain BUT more S/D resistance
  Optimal: 30-50nm
  
S/D proximity to gate:
  Closer → More strain transfer
  Limited by spacer width (10-20nm)
```

**Results**:
- Hole mobility increase: +40-80%
- PMOS I_on improvement: +25-35%
- Strain in channel: 0.8-1.5% (longitudinal compressive)

**For NMOS - Embedded SiC S/D (Tensile)**:

```
Process:
1. Recess S/D (similar to PMOS)

2. Epitaxial Si:C growth
   Si_(1-y)C_y, y = 1-2%
   Carbon substitutional in Si lattice
   
   Gate
    ││
   ─┴┴─
   ╔══╗  Si:C S/D (smaller lattice)

3. Strain transfer
   SiC lattice < Si lattice
        ↓
   SiC "pulls" on Si channel
        ↓
   Longitudinal tensile strain

Mechanism:
  C atom smaller than Si
  Lattice contracts by ~0.2% per 1% C
  Example: 1.5% C → 0.3% lattice contraction
        ↓
  Si:C pulls Si channel (tensile)
```

**Challenges**:
```
Carbon solubility in Si: Very low (<10¹⁸ cm⁻³ equilibrium)
  → Must use non-equilibrium growth (low T, high rate)
  → Metastable, can precipitate during anneal
  
Carbon activation:
  Some C interstitial (doesn't create strain)
  Need >70% substitutional for effective strain
  
Trade-off:
  High C% → More strain BUT stability issues
  Typical: 1.0-1.5% C (substitutional)
```

**Results**:
- Electron mobility increase: +15-25%
- NMOS I_on improvement: +10-15%
- Strain: 0.3-0.6% (tensile)

**Less effective than SiGe for PMOS because**:
- Lower achievable strain
- Carbon precipitation limits
- Electron mobility less sensitive to uniaxial tensile

##### B. Contact Etch Stop Layer (CESL)

**Nitride Liner Stress**:

```
Process:
1. After S/D formation, deposit Si₃N₄ liner
   PECVD, 50-100nm thick
   
2. Control intrinsic film stress
   NMOS: Tensile Si₃N₄ (σ = +1 to +2 GPa)
   PMOS: Compressive Si₃N₄ (σ = -1 to -2 GPa)
   
3. Stress transfer to channel
   
   NMOS:                    PMOS:
   ║→→→→║ Tensile liner    ║←←←║ Compressive liner
   ══Gate══                ══Gate══
   
   Liner pulls/pushes on Si
        ↓
   Strain in channel
```

**Stress Tuning Methods**:
```
PECVD Si₃N₄ stress control:
  - RF power: Higher → More tensile
  - Pressure: Lower → More tensile
  - Temperature: Higher → More compressive
  - Gas ratio (SiH₄/NH₃): Affects stoichiometry
  - Post-dep UV cure: Increases tensile
  
Typical range: -2 GPa to +2 GPa
```

**Advantages**:
-  Easy to integrate (standard PECVD)
-  Different stress for NMOS/PMOS (mask and etch)
-  Additive with S/D strain

**Disadvantages**:
-   Lower strain than embedded S/D (0.2-0.5%)
-   Decays with distance from gate

**Effectiveness**:
```
Strain magnitude vs. distance:

Strain (%)
     |
 0.5 |╲╲
     |  ╲╲
 0.3 |    ╲╲
     |      ╲╲___
 0.1 |___________╲____
     0  10  20  30  40  Distance from gate (nm)
     
Effective only in first 20-30nm
```

##### C. Shallow Trench Isolation (STI) Stress

