# Metallization in CMOS Backend-of-Line (BEOL)

## Table of Contents
1. [Introduction](#introduction)
2. [Metal Stack Architecture](#metal-stack-architecture)
3. [Aluminum Metallization (Legacy)](#aluminum-metallization-legacy)
4. [Copper Metallization (Modern)](#copper-metallization-modern)
5. [Interconnect Scaling Challenges](#interconnect-scaling-challenges)
6. [Via Formation and Contacts](#via-formation-and-contacts)
7. [Electromigration and Reliability](#electromigration-and-reliability)
8. [RC Delay Analysis](#rc-delay-analysis)
9. [Advanced Metallization Techniques](#advanced-metallization-techniques)
10. [Simulation Examples](#simulation-examples)
11. [Process Integration](#process-integration)

---

## Introduction

### What is BEOL Metallization?

After transistors are fabricated in the Front-End-of-Line (FEOL), the Backend-of-Line (BEOL) creates the metal interconnect system that:
- Connects transistors to form circuits
- Routes signals across the chip
- Distributes power and ground
- Provides I/O connections

**Key Challenges:**
- Minimizing RC delay as dimensions shrink
- Managing electromigration in narrow wires
- Reducing crosstalk between adjacent lines
- Maintaining mechanical integrity
- Optimizing for power and performance

### Historical Evolution

| Era | Metal | Dielectric | Node | Key Innovation |
|-----|-------|------------|------|----------------|
| 1970s-1990s | Aluminum | SiO₂ | >0.5 µm | Subtractive Al etch |
| 1997-present | Copper | Low-k | <0.25 µm | Damascene Cu, CMP |
| 2010s+ | Cu/Co | ULK/air gaps | <10 nm | Barrier scaling, Co caps |
| Future | Ru/Mo? | 2D materials | <3 nm | Beyond Cu solutions |

---

## Metal Stack Architecture

### Typical Modern BEOL Stack (7nm node)

```
┌─────────────────────────────────────┐
│  M8-M10: Global routing (thick)     │  ← Top metal (2-4 µm wide)
│  ═══════════════════════════════    │
├─────────────────────────────────────┤
│  M4-M7: Intermediate routing        │  ← 100-500 nm wide
│  ─────────────────────────          │
├─────────────────────────────────────┤
│  M1-M3: Local interconnect          │  ← Minimum pitch (40-80 nm)
│  ─── ─── ─── ─── ─── ───           │
├─────────────────────────────────────┤
│  M0: Contact level (W plugs)        │  ← Connects to transistors
│  • • • • • • • • • • • •            │
├─────────────────────────────────────┤
│  FEOL: Transistors + STI            │
└─────────────────────────────────────┘
```

### Design Hierarchy

**Local Layers (M1-M3)**
- Minimum width/space: 40-80 nm (7nm node)
- Primary function: Cell internal routing
- High density, high resistance per unit length
- Via resistance dominates

**Intermediate Layers (M4-M7)**
- Width: 100-500 nm
- Function: Block-level routing, clock distribution
- Balanced resistance and capacitance

**Global Layers (M8-M10+)**
- Width: 1-4 µm, thickness: 1-2 µm
- Function: Power grids, long-distance signals
- Low resistance critical for power delivery

---

## Aluminum Metallization (Legacy)

### Process Flow (Subtractive Etch)

**Used in technologies >0.25 µm, still relevant for some analog/power ICs**

#### Step 1: Dielectric Deposition
```
SiO₂ (PECVD or TEOS)
Thickness: 500-1000 nm
Purpose: Inter-layer dielectric (ILD)
```

#### Step 2: Via Patterning and Etch
- Lithography to define via holes
- RIE etch through oxide to lower metal
- Typical via diameter: 0.5-1 µm

#### Step 3: Barrier/Adhesion Layer
```
Ti/TiN stack: 20-50 nm total
Ti: Adhesion to SiO₂
TiN: Diffusion barrier (prevents Al-Si reaction)
```

**Deposition Method:** Sputtering (PVD)

#### Step 4: Aluminum Alloy Deposition
```
Al-Cu (0.5-2% Cu) or Al-Si-Cu
Thickness: 500-1000 nm
Method: Sputtering (DC magnetron)
```

**Why Al-Cu?**
- Pure Al has severe electromigration issues
- Cu improves EM resistance by 10-100×
- Cu precipitates at grain boundaries, blocking atomic diffusion

#### Step 5: Metal Patterning
```
Photolithography
↓
Dry etch (Cl₂/BCl₃ plasma)
↓
Strip photoresist
```

#### Step 6: Passivation
```
SiO₂ or Si₃N₄ protective layer
Prevents corrosion and mechanical damage
```

### Aluminum Key Properties

| Property | Value | Notes |
|----------|-------|-------|
| Resistivity | 2.7 µΩ·cm | Bulk value |
| Melting point | 660°C | Limits thermal budget |
| EM activation energy | 0.5-0.7 eV | Poor EM resistance |
| Hillock formation | Yes | Requires capping layer |
| Cost | Low | Abundant, easy to deposit |

### Problems with Aluminum

1. **Electromigration:** Severe at small dimensions
2. **Contact Resistance:** Schottky barrier to Si requires silicide
3. **Spiking:** Al can penetrate through shallow junctions
4. **Aspect Ratio Limits:** Poor step coverage in high-aspect-ratio vias
5. **Higher Resistance:** 1.6× higher than Cu

---

## Copper Metallization (Modern)

### Why Copper?

| Advantage | Impact |
|-----------|--------|
| Lower resistivity (1.7 vs 2.7 µΩ·cm) | 37% lower resistance |
| Better electromigration | 100× longer lifetime |
| Superior step coverage (CMP) | Enables scaling |
| Lower RC delay | Faster circuits |

**Critical Requirement:** Cu diffuses rapidly in SiO₂ and Si → **Must be fully encapsulated**

### Damascene Process

**Key Innovation:** Instead of etching metal, etch trenches in dielectric and fill with metal

#### Single Damascene (via-first or trench-first)

```
Step 1: Deposit ILD (SiO₂ or low-k)
═══════════════════════════════

Step 2: Lithography + etch trenches
─────────────────────────────
        └─┘   └─┘   └─┘

Step 3: Deposit barrier (Ta/TaN, 3-5 nm)
│     │││ │││ │││     │  ← Conformal coating
└─────┘└┘ └┘└┘ └┘─────┘

Step 4: Cu seed layer (PVD, 20-50 nm)
Cu    Cu Cu Cu Cu Cu    Cu

Step 5: Electroplating (bulk Cu fill)
██████████████████████████████  ← Overfill

Step 6: CMP (polish back to ILD surface)
─────────────────────────────
  ███    ███    ███          ← Cu lines remain
```

#### Dual Damascene (vias + trenches simultaneously)

**Advantages:**
- Fewer process steps
- Better via/line contact
- Lower cost per layer

**Process Variants:**
1. **Via-first:** Etch vias, then trenches
2. **Trench-first:** Etch trenches, then vias
3. **Self-aligned via:** Partially etch trench, full via, complete trench

### Barrier Layer Requirements

**Purpose:**
1. Prevent Cu diffusion into dielectric
2. Prevent Cu diffusion into Si
3. Provide adhesion
4. Minimize resistivity penalty

**Common Barrier Materials:**

| Material | Thickness | Resistivity | Pros | Cons |
|----------|-----------|-------------|------|------|
| Ta/TaN | 3-10 nm | ~200 µΩ·cm | Excellent barrier | High resistivity |
| TiN | 5-15 nm | ~50 µΩ·cm | Good barrier | Worse than Ta |
| Ru | 1-3 nm | ~10 µΩ·cm | Seedless Cu fill | Expensive, newer |
| Co/Mn | 2-5 nm | ~10-20 µΩ·cm | Self-forming barrier | Development stage |

**Scaling Challenge:** As lines shrink, barrier consumes more cross-section

Example: 40 nm wide trench, 5 nm barrier on each side → 30% area loss!

### Copper Electroplating

**Bath Composition:**
- CuSO₄·5H₂O: 0.8-1.0 M (Cu²⁺ source)
- H₂SO₄: 0.5-1.0 M (conductivity)
- Cl⁻: 50-100 ppm (grain refinement)
- Organic additives (proprietary):
  - **Suppressor:** PEG (polyethylene glycol) - slows deposition
  - **Accelerator:** SPS (sulfopropyl sulfonate) - speeds deposition
  - **Leveler:** Nitrogen compounds - improves planarization

**Key Mechanism:** Bottom-up fill (superfilling)
- Accelerator accumulates at bottom of trenches
- Suppressor dominates at top
- Result: Voids eliminated, overfill controlled

**Plating Conditions:**
- Current density: 10-50 mA/cm²
- Temperature: 20-30°C
- Deposition rate: 100-300 nm/min
- Uniformity: <3% across 300 mm wafer

### Chemical Mechanical Polishing (CMP)

**Three-Body Abrasion:**
```
Polishing pad (soft polyurethane)
    ↓ downforce
Slurry (alumina/silica nanoparticles + chemistry)
    ↓
Wafer surface (Cu + barrier + dielectric)
```

**Cu CMP Slurry:**
- Abrasive: Al₂O₃ or SiO₂ (30-200 nm particles)
- Oxidizer: H₂O₂ (1-10%) - converts Cu to CuO
- pH: 4-10 (alkaline for faster removal)
- Corrosion inhibitor: Benzotriazole (BTA)
- Selectivity: Cu removal 50× faster than barrier

**Process Steps:**
1. **Bulk Cu removal:** High downforce, fast pad
2. **Soft landing:** Detect barrier breakthrough
3. **Barrier removal:** Different slurry (lower selectivity)
4. **Overpolish:** Ensure barrier fully removed

**Critical Parameters:**
- Uniformity: <5% within-wafer non-uniformity
- Dishing: Cu recess in wide lines (<10 nm)
- Erosion: Dielectric loss in dense areas (<20 nm)
- Scratches: <0.1 defects/cm²

---

## Interconnect Scaling Challenges

### Resistivity Increase at Small Dimensions

**Bulk Cu resistivity:** ρ₀ = 1.7 µΩ·cm

**Size Effects:**

1. **Surface Scattering** (Fuchs-Sondheimer model)
   - Electrons scatter at line edges
   - Mean free path in Cu: λ = 40 nm at 300K
   - Significant when line width < 3λ

2. **Grain Boundary Scattering** (Mayadas-Shatzkes model)
   - Cu grain size ≈ line width for narrow lines
   - Additional resistance from grain boundaries

3. **Barrier Thickness Penalty**
   - Barrier doesn't scale with linewidth
   - Consumes increasing fraction of cross-section

**Effective Resistivity:**

```
ρₑff = ρ₀ × [1 + (3λ/8w)(1-p)] × [1 + (barrier area / Cu area)]
```

Where:
- w = linewidth
- p = specularity parameter (0 = diffuse, 1 = specular)
- Typical p ≈ 0.5 for Cu/Ta barrier

**Example:** 
- 1 µm line: ρₑff ≈ 1.8 µΩ·cm (6% increase)
- 40 nm line: ρₑff ≈ 4-6 µΩ·cm (3× increase!)

### Capacitance: Why Low-k Dielectrics?

**Parallel Plate Capacitance:**
```
C = ε₀ · εᵣ · A / d
```

**SiO₂:** k = 3.9 (reference)
**Problem:** As metal pitch shrinks, C/length increases

**Low-k Materials:**

| Material | k value | Method | Issues |
|----------|---------|--------|--------|
| FSG (F-doped SiO₂) | 3.5-3.7 | PECVD | Moisture absorption |
| SiOCH (carbon-doped) | 2.7-3.0 | PECVD | Weak mechanical |
| Porous SiOCH | 2.3-2.5 | Porogen | Very fragile |
| Air gaps | 1.0 | Self-forming | Complex integration |

**Ultra-low-k (ULK) Challenges:**
- Poor mechanical strength (modulus <10 GPa)
- Moisture uptake → dielectric breakdown
- Plasma damage during etch
- CMP sensitivity

### RC Delay Analysis

**Elmore Delay for Interconnect:**
```
τ = 0.69 × R × C
```

**Per-unit-length parameters:**
- R = ρ / (w × t) [Ω/µm]
- C = ε₀ · k · w / s [fF/µm] (simplified)

Where:
- ρ = resistivity
- w = linewidth
- t = line thickness
- s = line spacing
- k = dielectric constant

**Scaling Impact:**

| Node | Metal pitch | R (Ω/µm) | C (fF/µm) | RC (ps/µm²) |
|------|-------------|----------|-----------|-------------|
| 180 nm | 500 nm | 0.1 | 0.2 | 0.02 |
| 90 nm | 250 nm | 0.3 | 0.3 | 0.09 |
| 45 nm | 140 nm | 0.8 | 0.35 | 0.28 |
| 22 nm | 80 nm | 2.0 | 0.4 | 0.80 |
| 7 nm | 40 nm | 5.0 | 0.45 | 2.25 |

**Conclusion:** RC delay increases exponentially! Limits maximum wire length.

---

## Via Formation and Contacts

### Contact to Silicon (M0 level)

**Challenge:** Form low-resistance Ohmic contact to doped Si

**Process:**
1. **Silicide formation** (done in FEOL)
   - NiSi, CoSi₂, or TiSi₂
   - Typical thickness: 10-20 nm
   - Contact resistance: 1-5 Ω·µm²

2. **Pre-metal dielectric (PMD)**
   - Deposited: SiO₂ or low-k
   - Planarized by CMP

3. **Contact via etch**
   - Stop on silicide
   - Aspect ratio: 2:1 to 5:1

4. **Contact plug fill**
   - **Legacy:** Tungsten (W) CVD
   - **Modern:** W or Co CVD
   - Requires barrier: TiN or TaN

**Tungsten CVD:**
```
WF₆ + 3H₂ → W + 6HF   (reduction)
Temperature: 350-450°C
```

**Cobalt (emerging):**
- Lower resistivity than W (6 vs 9 µΩ·cm)
- Better gap fill in high-aspect-ratio contacts
- Enables continued scaling

### Via Between Metal Layers

**Via Resistance Calculation:**
```
Rᵥᵢₐ = ρ · L / A + 2Rᶜ
```

Where:
- ρ = Cu resistivity (with size effects)
- L = via height (~100-200 nm)
- A = via area (πr²)
- Rᶜ = contact resistance at top/bottom interfaces

**Typical Values (7nm node):**
- Via diameter: 30-40 nm
- Via resistance: 5-20 Ω per via
- Line resistance: 10-50 Ω/µm

**Design Impact:** Multiple vias in parallel reduce resistance
- 1 via: 10 Ω
- 2 vias: 5 Ω
- 4 vias: 2.5 Ω

---

## Electromigration and Reliability

### Physical Mechanism

**Electromigration (EM):** Mass transport due to momentum transfer from electrons

**Drift Velocity:**
```
v = (D/kT) · Z* · e · ρ · j
```

Where:
- D = diffusivity
- Z* = effective charge (1-10 for Cu)
- e = electron charge
- ρ = resistivity
- j = current density

**Failure Modes:**
1. **Void formation** (cathode end) → open circuit
2. **Hillock formation** (anode end) → short circuit
3. **Via depletion** → increased resistance

### Black's Equation

**Median Time to Failure (MTF):**

```
MTF = A · j⁻ⁿ · exp(Eₐ / kT)
```

Where:
- A = constant (depends on material, geometry)
- j = current density (A/cm²)
- n = current exponent (1-2, typically 1.5)
- Eₐ = activation energy
- k = Boltzmann constant
- T = temperature (Kelvin)

**Typical Parameters:**

| Metal | Eₐ (eV) | Max j (MA/cm²) | Notes |
|-------|---------|----------------|-------|
| Al | 0.5-0.7 | 0.5-1 | Poor EM resistance |
| Al-Cu | 0.7-0.9 | 2-5 | Much improved |
| Cu (bare) | 0.9-1.0 | 5-10 | Grain boundary diffusion |
| Cu + cap | 1.2-1.5 | 10-20 | Interface diffusion suppressed |

### EM Mitigation Strategies

1. **Metal Capping Layers**
   - **CoWP (electroless):** Selective deposition on Cu
   - **CuMn alloy:** Mn segregates to grain boundaries
   - **Tan cap:** Diffusion barrier at top surface
   - Effect: 5-10× lifetime improvement

2. **Redundant Vias**
   - Multiple vias in parallel
   - If one fails, current redistributes

3. **Design Rules**
   - Maximum current density limits
   - Minimum wire widths for given current
   - Via doubling requirements

4. **Circuit Design**
   - Use wider wires for power/ground
   - Avoid DC current in signal lines
   - Temperature management

**Example Design Rule:**
- Signal wire (max 1 mA): w ≥ 0.1 µm
- Power wire (max 10 mA): w ≥ 1.0 µm
- Via current: <0.5 mA per via

### Stress-Induced Voiding (SIV)

**Mechanism:** Thermal stress during cooling creates voids

**Cause:** Mismatch in thermal expansion coefficients
- Cu: α = 17 ppm/K
- SiO₂: α = 0.5 ppm/K

**Prevention:**
- Proper annealing cycles
- Via placement rules (avoid trapping)
- Cu microstructure control (large grains preferred)

---

## RC Delay Analysis

### Distributed RC Line Model

**Transmission Line Equations:**

```
V(x) = V₀ · exp(-x/λ) · cos(ωt - x/λ)
λ = √(2/(ω·R·C))  [Decay length]
```

For low frequencies (digital signals):
```
τₚᵈ ≈ 0.38 · R · C · L²  [Lumped approximation]
```

### Delay Optimization Strategies

1. **Repeater Insertion**
   - Break long wires with inverters/buffers
   - Optimal spacing: L_opt ≈ √(r·c / (R·C))
   - Where r, c = driver resistance and capacitance

2. **Wire Sizing**
   - Use wider wires for critical paths
   - Tapering: Wide at driver, narrow at far end

3. **Via Minimization**
   - Keep signals on same metal layer
   - Via resistance often > line resistance

4. **Shielding**
   - Ground lines beside critical signals
   - Reduces crosstalk capacitance

### Crosstalk Analysis

**Coupling Capacitance:**

```
Cₘ = ε₀ · k · t / s  [Miller capacitance]
```

**Effect on Delay:**
- Aggressor switches same direction: 2× faster
- Aggressor switches opposite: 2× slower
- Worst-case: τ_crosstalk = τ_intrinsic × (1 + Cₘ/Cₗ)

---

## Advanced Metallization Techniques

### Self-Aligned Barrier Processes

**Challenge:** Thin barriers (1-2 nm) for minimal resistivity penalty

**Approach:**
1. Deposit Cu with Mn dopant (1-3%)
2. Anneal: Mn diffuses to surfaces
3. MnSiO₃ forms at Cu/dielectric interface
4. Self-forming barrier, no separate deposition

**Benefits:**
- Barrier thickness <2 nm
- Better Cu volume fraction
- Lower effective resistivity

### Alternative Metals

**Ruthenium (Ru):**
- Resistivity: 7 µΩ·cm (4× worse than Cu)
- Advantage: No barrier needed (doesn't diffuse)
- Target: Contacts and lower metal layers <5 nm node

**Cobalt (Co):**
- Resistivity: 6 µΩ·cm
- Use: Contact plugs, liners, local interconnect
- Advantage: Better scalability than W

**Hybrid Approaches:**
- Cu for wide wires (M3+)
- Co for narrow local interconnect (M1-M2)
- Ru for vias and contacts

### Air Gap Technology

**Concept:** Replace low-k dielectric with air (k=1) in spaces between lines

**Fabrication:**
1. Deposit sacrificial material between Cu lines
2. Deposit hard mask over Cu
3. Etch access holes
4. Remove sacrificial material (vapor HF etch)
5. Seal with dielectric cap

**Benefits:**
- Lowest possible capacitance
- 20-30% delay reduction

**Challenges:**
- Mechanical weakness
- Integration complexity
- CMP issues

### Through-Silicon Vias (TSV)

**Purpose:** Vertical connections for 3D integration

**Specifications:**
- Diameter: 5-50 µm
- Depth: 50-300 µm
- Aspect ratio: 5:1 to 20:1

**Process:**
1. DRIE etch through Si wafer
2. Thermal oxidation (isolation)
3. Barrier/seed deposition
4. Cu electroplating
5. CMP to remove overfill

**Applications:**
- Memory stacking (HBM)
- Heterogeneous integration
- MEMS + CMOS integration

---

## Simulation Examples

### Python Simulation: Interconnect RC Delay

See `simulation-examples/python/metallization_sim.py` for complete code.

**Features:**
1. Effective resistivity calculation with size effects
2. Capacitance modeling with fringing fields
3. Elmore delay computation
4. Electromigration lifetime prediction
5. Optimal repeater insertion

**Example Output:**
```
Metal Layer: M1 (local)
Width: 40 nm, Thickness: 80 nm, Length: 100 µm
Effective resistivity: 4.8 µΩ·cm
Resistance: 1500 Ω
Capacitance: 45 fF
RC delay: 67.5 ps
EM lifetime (10 MA/cm²): 5.2 years

Optimization: Insert 3 repeaters
New delay: 22.5 ps (3× improvement)
```

### MATLAB Simulation: Via Resistance Network

See `simulation-examples/matlab/via_resistance.m` for complete code.

**Analysis:**
- Via array resistance calculation
- Current distribution in parallel vias
- IR drop in power distribution network
- Redundancy analysis

---

## Process Integration

### Complete BEOL Flow (Modern 7nm node)

**Layer 1: M0 (Contacts)**
1. Pre-metal dielectric deposition (SiO₂)
2. CMP planarization
3. Contact lithography and etch
4. Barrier deposition (TiN)
5. W or Co CVD fill
6. CMP to remove excess metal

**Layers 2-10: M1-M9 (Interconnects)**

For each metal layer:
1. **Low-k dielectric deposition**
   - SiOCH by PECVD
   - Thickness: 100-300 nm

2. **Via/trench lithography** (dual damascene)
   - EUV or multi-patterning at M1-M3
   - DUV at upper layers
   - Via-first or trench-first flow

3. **Etch**
   - Via etch: stop on lower metal
   - Trench etch: stop in low-k

4. **Post-etch clean**
   - Remove polymer residues
   - Critical for low-k damage repair

5. **Barrier deposition**
   - PVD Ta/TaN (3-5 nm)
   - Or ALD Ru (1-3 nm) for advanced nodes

6. **Cu seed layer**
   - PVD Cu (20-50 nm)
   - Must cover via bottom

7. **Electroplating**
   - Bottom-up superfill
   - 200-500 nm overburden

8. **Anneal**
   - 200-400°C, 30-60 min
   - Grain growth, stress relief

9. **CMP**
   - Cu removal → barrier → overpolish
   - Endpoint detection critical

10. **Cu cap deposition**
    - CoWP or CuMn
    - 5-20 nm

11. **Etch stop layer**
    - SiCN or SiN (20-50 nm)
    - Protects Cu during next via etch

**Repeat for each metal layer**

### Thermal Budget Considerations

**Temperature Limits:**
- Cu anneal: 200-400°C
- W CVD: 350-450°C
- Low-k damage: >400°C

**Consequence:** All BEOL must be done after dopant activation anneals (>1000°C)

### Metrology and Inspection

**Critical Measurements:**

1. **Line Width/Space** - CD-SEM, optical scatterometry
2. **Line Resistance** - 4-point probe, sheet resistance
3. **Via Resistance** - Kelvin test structures
4. **Defects** - Optical inspection, e-beam review
5. **CMP Uniformity** - Ellipsometry, profilometry
6. **Barrier Integrity** - TEM cross-sections, SIMS

**Yield Monitors:**
- Comb-serpent structures (leakage)
- Via chains (opens/shorts)
- Kelvin resistors (contact resistance)

---

## Summary and Future Trends

### Key Takeaways

1. **Copper damascene** is the industry standard for <0.25 µm nodes
2. **Barrier scaling** is the critical challenge at advanced nodes
3. **RC delay** increases exponentially with scaling → limits performance
4. **Electromigration** requires design rules and careful current management
5. **Low-k dielectrics** reduce capacitance but create integration challenges

### Future Directions (3nm and beyond)

**Materials:**
- Ruthenium interconnects for M1-M2
- Cobalt for vias and contacts
- Topological insulators for quantum computing

**Architecture:**
- Backside power delivery networks
- Monolithic 3D integration
- Buried power rails

**Processes:**
- Fully self-aligned vias
- Subtractive Cu etch (reverting from damascene!)
- Selective deposition techniques

**Design:**
- AI-driven routing optimization
- Thermal-aware placement
- Reliability-driven design rules

---

## References

### Foundational Papers
1. Edelstein et al., "Full Copper Wiring in a Sub-0.25 μm CMOS ULSI Technology," *IEDM* (1997)
2. Black, "Electromigration—A Brief Survey," *IEEE Trans. ED* (1969)
3. Steinhogl et al., "Size-dependent resistivity of metallic wires," *Phys. Rev. B* (2002)

### Industry Standards
- ITRS Roadmap (2015) - Interconnect chapter
- SEMI Standards for CMP processes
- JEDEC JESD61 (Electromigration testing)

### Recommended Textbooks
- Rossnagel et al., *Handbook of Semiconductor Interconnection Technology*
- Ohring, *Reliability and Failure of Electronic Materials*
- Ghani, *CMOS Back-End-of-Line Technology* (SPIE)

---

## Related Handbook Chapters

- **Previous:** [Gate Stack Formation](../02-cmos-feol/gate-stack.md)
- **Next:** [Damascene Process Deep Dive](damascene-process.md)
- **See Also:** [Low-k Dielectrics](low-k-dielectrics.md), [CMP Process](cmp-process.md)

---

**Last Updated**: November 2025  
**Contributors**: Zeyad Mustafa
**Chapter:** 3.1 - CMOS BEOL Metallization  
**Simulation Code:** `simulation-examples/python/metallization_sim.py`