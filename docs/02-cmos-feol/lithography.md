# Lithography: Pattern Transfer in Semiconductor Manufacturing

## Table of Contents
- [Introduction](#introduction)
- [Fundamental Principles](#fundamental-principles)
  - [The Lithography Process](#the-lithography-process)
  - [Resolution and the Rayleigh Criterion](#resolution-and-the-rayleigh-criterion)
  - [Historical Evolution of Lithography Wavelengths](#historical-evolution-of-lithography-wavelengths)
- [Photoresist Chemistry](#photoresist-chemistry)
  - [Types of Photoresists](#types-of-photoresists)
  - [Photoresist Specifications](#photoresist-specifications)
- [Lithography Process Steps](#lithography-process-steps)
  - [Step 1: Surface Preparation](#step-1-surface-preparation)
  - [Step 2: Photoresist Coating](#step-2-photoresist-coating)
  - [Step 3: Soft Bake (Pre-Exposure Bake)](#step-3-soft-bake-pre-exposure-bake)
  - [Step 4: Alignment](#step-4-alignment)
  - [Step 5: Exposure](#step-5-exposure)
  - [Step 6: Post-Exposure Bake (PEB)](#step-6-post-exposure-bake-peb)
  - [Step 7: Development](#step-7-development)
  - [Step 8: Hard Bake (Post-Develop Bake)](#step-8-hard-bake-post-develop-bake)
- [Advanced Lithography Techniques](#advanced-lithography-techniques)
  - [Immersion Lithography](#immersion-lithography)
  - [Optical Proximity Correction (OPC)](#optical-proximity-correction-opc)
  - [Phase-Shift Masks (PSM)](#phase-shift-masks-psm)
  - [Multiple Patterning](#multiple-patterning)
  - [Extreme Ultraviolet (EUV) Lithography](#extreme-ultraviolet-euv-lithography)
  - [High-NA EUV (Future)](#high-na-euv-future)


## Introduction

Lithography is the most critical and expensive process in semiconductor manufacturing. It determines the minimum feature size (technology node) and directly impacts device density, performance, and cost. This chapter covers photolithography from basic principles through advanced techniques including EUV lithography and multi-patterning.

> **Key Concept**: Lithography is the "printing press" of the semiconductor industry, transferring circuit patterns from photomasks to silicon wafers with nanometer precision.

## Fundamental Principles

### The Lithography Process

The complete lithography process consists of eight major steps:

```
1. Surface Preparation (HMDS treatment)
        ↓
2. Photoresist Coating (spin-on)
        ↓
3. Soft Bake (pre-exposure bake)
        ↓
4. Alignment (wafer to mask)
        ↓
5. Exposure (UV light through mask)
        ↓
6. Post-Exposure Bake (PEB)
        ↓
7. Development (remove exposed/unexposed regions)
        ↓
8. Hard Bake (post-develop stabilization)
```

### Resolution and the Rayleigh Criterion

The fundamental limit of optical lithography is given by the **Rayleigh equation**:

$$
R = k_1 \frac{\lambda}{NA}
$$

Where:
- **R** = Minimum resolvable feature size (half-pitch)
- **k₁** = Process factor (0.25-0.8, depends on technique)
- **λ** = Wavelength of exposure light
- **NA** = Numerical Aperture of lens system

**Depth of Focus** (DOF):

$$
DOF = k_2 \frac{\lambda}{NA^2}
$$

Where:
- **k₂** = Process factor (~0.5-1.0)
- Trade-off: Higher NA → Better resolution but shallower DOF

### Historical Evolution of Lithography Wavelengths

| Era | Wavelength | Source | Technology Node | k₁ Factor |
|-----|------------|--------|----------------|-----------|
| 1980s | 436 nm | g-line (Hg lamp) | 1-2 μm | 0.8 |
| 1990s | 365 nm | i-line (Hg lamp) | 0.35-1 μm | 0.6-0.8 |
| 1995-2005 | 248 nm | KrF excimer laser | 180-350 nm | 0.4-0.6 |
| 2001-2020 | 193 nm | ArF excimer laser | 28-130 nm | 0.3-0.5 |
| 2007-present | 193 nm | ArF immersion | 14-65 nm | 0.25-0.35 |
| 2019-present | 13.5 nm | EUV (Sn plasma) | 3-7 nm | 0.3-0.5 |

**Key Insight**: As k₁ is pushed lower, process difficulty increases exponentially

## Photoresist Chemistry

### Types of Photoresists

#### 1. Positive vs. Negative Tone

**Positive Resist**:
```
Before Exposure:    After Exposure:      After Development:
  UV Mask              UV Light              Developer
    ████                  ↓↓↓                    
  ────────            ████████             ████    ████
 ▓▓▓▓▓▓▓▓            ▓▓▓▓▓▓▓▓             ▓▓▓▓    ▓▓▓▓
 ──Wafer──           ──Wafer──            ──Wafer──

Exposed area becomes soluble → Removed by developer
```

**Negative Resist**:
```
Before Exposure:    After Exposure:      After Development:
  UV Mask              UV Light              Developer
    ████                  ↓↓↓                    
  ────────            ████████                 ████
 ▓▓▓▓▓▓▓▓            ▓▓▓▓▓▓▓▓             ────    ────
 ──Wafer──           ──Wafer──            ▓▓▓▓    ▓▓▓▓
                                          ──Wafer──

Exposed area becomes insoluble → Remains after development
```

**Comparison**:

| Property | Positive Resist | Negative Resist |
|----------|----------------|-----------------|
| Resolution | Excellent (<20nm) | Good (>50nm) |
| Contrast | High | Moderate |
| Adhesion | Good | Excellent |
| Swelling in developer | Minimal | Significant |
| Application | Advanced nodes | Thick film, packaging |

#### 2. Chemically Amplified Resists (CAR)

Modern photoresists use **chemical amplification** for high sensitivity:

**Mechanism**:
```
1. Exposure:
   PAG (Photoacid Generator) + hν → H⁺ (acid)
   
2. Post-Exposure Bake (PEB):
   H⁺ + Polymer → Deprotection reaction (catalytic)
   
3. Development:
   Deprotected polymer → Soluble in developer
```

**Key Components**:
- **Polymer**: Protected phenolic resin (e.g., poly(hydroxystyrene))
- **PAG**: Onium salts (sulfonium, iodonium)
- **Solvent**: PGMEA (propylene glycol methyl ether acetate)
- **Base quencher**: Controls acid diffusion

**Amplification Factor**: 1 photon → 1 acid → 1000+ deprotection events

### Photoresist Specifications

**For 193nm ArF Resist**:

| Parameter | Typical Value | Impact |
|-----------|--------------|--------|
| Sensitivity (E₀) | 15-30 mJ/cm² | Exposure dose required |
| Contrast (γ) | 4-8 | Edge sharpness |
| Etch resistance | 1.5-2.5 Å/sec (O₂ RIE) | Pattern transfer |
| Outgassing | <0.1 ng/cm²·sec | Lens contamination |
| LER (Line Edge Roughness) | 3-5 nm (3σ) | Device variability |
| Resolution | <20 nm (half-pitch) | Feature size |

## Lithography Process Steps

### Step 1: Surface Preparation

**Purpose**: Ensure photoresist adhesion and uniformity

#### Dehydration Bake

**Process**:
```
Temperature: 150-200°C
Time: 30-60 seconds (hotplate) or 30 minutes (oven)
Purpose: Remove surface moisture
```

**Why Necessary**:
- Si-OH groups on oxide surface attract water
- Water interferes with photoresist adhesion
- Moisture causes pattern defects (footing, lifting)

#### HMDS Treatment (Hexamethyldisilazane)

**Chemical Structure**:
```
    CH₃   CH₃   CH₃
     |     |     |
H₃C-Si-NH-Si-CH₃
     |     |     |
    CH₃   CH₃   CH₃
```

**Reaction with Silicon Dioxide**:
```
Si-OH + HMDS → Si-O-Si(CH₃)₃ + NH₃

Hydrophilic surface → Hydrophobic surface
```

**Application Methods**:

**A. Vapor Prime**:
```
1. Place wafer in chamber
2. Heat to 120-150°C
3. Introduce HMDS vapor (5-30 seconds)
4. Purge with N₂
5. Remove wafer

Advantages: Uniform, no liquid contamination
```

**B. Spin-On**:
```
1. Dispense HMDS liquid on wafer
2. Spin at 3000 RPM (30 seconds)
3. Hot plate bake (120°C, 60 seconds)

Advantages: Simple, fast
Disadvantages: Less uniform than vapor
```

**Result**: Water contact angle increases from ~5° to ~65°

### Step 2: Photoresist Coating

**Spin Coating Process**:

```
Phase 1: Dispense        Phase 2: Spread       Phase 3: Evaporation
   Nozzle                  High speed            Edge effects
     |                       ~~~>                    ||||
     ↓                     ▓▓▓▓▓▓▓               ▓▓▓▓▓▓▓
   ▓▓▓▓▓                  ▓▓▓▓▓▓▓               ▓▓▓▓▓▓▓
  ════════                ════════              ════════
  500 RPM                 3000-6000 RPM         1000 RPM
  3-5 sec                 20-30 sec             5-10 sec
```

**Spin Coating Parameters**:

**Viscosity Selection**:
```
Desired Thickness = k × √(η / ω)

Where:
k = constant (depends on resist)
η = viscosity (cP)
ω = angular velocity (RPM)
```

**Typical Recipe**:
```
1. Dispense: 1 mL resist at 500 RPM (5 sec)
2. Spread: Ramp to 4000 RPM at 1000 RPM/sec
3. Spin: Hold at 4000 RPM (30 sec)
4. Dry: Decelerate to 0 RPM (5 sec)

Result: 200-300 nm thickness, ±2% uniformity
```

**Edge Bead Formation**:
```
     Thick edge bead (3-5mm)
        ___/
       /
      |  Uniform resist
      |
    ══════════════
       Wafer
```

**Edge Bead Removal (EBR)**:
- Method 1: Solvent spray during spin
- Method 2: EBR tool (dedicated)
- Purpose: Prevent backside contamination, ensure flat wafer seating

### Step 3: Soft Bake (Pre-Exposure Bake)

**Purpose**:
1. Evaporate residual solvent (→ 3-8% remaining)
2. Improve film adhesion
3. Stabilize resist thickness
4. Densify film

**Process Parameters**:

**Hotplate Bake** (modern):
```
Temperature: 90-130°C (resist-dependent)
Time: 60-90 seconds
Ramp: 10-20°C/sec
Uniformity: ±0.5°C across plate
```

**Oven Bake** (legacy):
```
Temperature: 90-100°C
Time: 20-30 minutes
Uniformity: ±2°C in oven
Issue: Slower throughput
```

**Temperature Effects**:

| Too Low (<80°C) | Optimal (90-110°C) | Too High (>130°C) |
|-----------------|-------------------|-------------------|
| Poor adhesion | Good adhesion | Thermal flow |
| Solvent remains | Minimal solvent | Loss of sensitivity |
| Development issues | Sharp profiles | Reduced resolution |

**N₂ Purge**: Inert atmosphere prevents oxidation and contamination

### Step 4: Alignment

**Purpose**: Accurately position mask/reticle relative to existing wafer patterns

#### Alignment Marks

**Global Alignment Marks**:
```
Scribe Line (Between Dies):

    ╔══════════════╗
    ║              ║
    ║  ┼     ┼     ║  Cross marks
    ║              ║
    ║  ┼     ┼     ║
    ║              ║
    ╚══════════════╝
```

**Types of Marks**:

**Box-in-Box**:
```
   ┌─────────┐
   │  ┌───┐  │
   │  │   │  │  Inner box on layer N
   │  └───┘  │  Outer box on layer N-1
   └─────────┘
   
Alignment: Center boxes
```

**Verniers**:
```
   ||||||||        Mask marks
   ────────        Wafer marks
   
Alignment: Match fringe patterns
```

**Interference Gratings**:
```
≡≡≡≡≡≡≡≡≡≡  Periodic gratings
   ↕
≡≡≡≡≡≡≡≡≡≡

Alignment: Maximize diffraction signal
```

#### Alignment Strategies

**Die-by-Die Alignment**:
- Align each die individually
- Best overlay (<10nm)
- Slow throughput (~30 wafers/hour)

**Global Alignment**:
- Measure few dies, calculate wafer-level corrections
- Fast throughput (150+ wafers/hour)
- Good overlay (20-50nm for advanced nodes)

**Enhanced Global Alignment (EGA)**:
- Measure 20-40 points across wafer
- Model wafer distortion (translation, rotation, magnification, orthogonality)
- Overlay: 10-30nm

**Overlay Budget**:
```
Total Overlay Error = √(σ²align + σ²distortion + σ²process)

Target: <10nm for 7nm node
```

### Step 5: Exposure

**Illumination Geometry**:

```
Light Source (ArF Laser, 193nm)
        ↓
    Illuminator (beam shaping)
        ↓
    ████████  Reticle/Mask (4× or 5× larger than target)
        ↓
    Reduction Lens (NA = 0.93-1.35)
        ↓
    ▓▓▓▓▓▓▓▓  Photoresist on wafer
        ↓
    ════════  Silicon wafer
```

#### Exposure Systems

**Contact/Proximity Printing** (Legacy):
```
   Mask in contact or near wafer
   ████████  Mask
       ↓↓↓   UV light (1:1 imaging)
   ▓▓▓▓▓▓▓▓  Resist
   ════════  Wafer

Gap: 0 (contact) or 10-50μm (proximity)
Resolution: 1-2μm
Issue: Mask damage, defects
```

**Projection Printing** (Modern):
```
   Mask/Reticle (magnified 4× or 5×)
        ↓
   Reduction Lens System
        ↓
   Wafer (reduced image)

Advantages: No mask contact, better resolution
```

**Step-and-Repeat (Stepper)**:
```
Wafer grid:
┌───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │  Expose one field at a time
├───┼───┼───┼───┤  Step to next position
│ 5 │ 6 │ 7 │ 8 │  Repeat until wafer complete
└───┴───┴───┴───┘

Field size: 22×26mm (typical for 300mm wafer)
Throughput: 100-150 wafers/hour
```

**Step-and-Scan (Scanner)**:
```
   Reticle scans →
     ████→████→████
           ↓
   Wafer scans ← (opposite direction)
     ▓▓▓←▓▓▓←▓▓▓

Synchronous scanning (4:1 or 5:1 reduction)
Field size: 26×33mm
Throughput: 150-275 wafers/hour
Advantages: Larger field, better uniformity
```

#### Exposure Dose and Contrast

**Exposure Dose**:
```
E = P × t

Where:
E = Exposure dose (mJ/cm²)
P = Light intensity (mW/cm²)
t = Exposure time (seconds)
```

**Typical Dose**: 15-40 mJ/cm² for 193nm CAR

**Dose-to-Clear Curve**:
```
Remaining
Thickness
    |     
100%|████████
    |        ╲╲
 50%|          ╲╲_____ (cleared)
    |________________
    0   E₀  E₉₅ E₁₀₀   Dose
    
E₀ = Onset dose
E₁₀₀ = Dose to fully clear
```

**Contrast (γ)**:
```
γ = 1 / log₁₀(E₁₀₀/E₀)

High γ (6-8): Sharp edges, good resolution
Low γ (2-3): Gradual transitions, poor resolution
```

#### Illumination Techniques

**Conventional Illumination**:
```
         Source
           ●
          ╱│╲
         ╱ │ ╲
        ╱  │  ╲
       ════════  Reticle
       
Uniform circular illumination
k₁ ≈ 0.6-0.8
```

**Off-Axis Illumination (OAI)**:
```
Annular:        Quadrupole:      Dipole:
   ○ ○ ○           ● · ●           · ●·
   ○ · ○           · · ·           · · ·
   ○ ○ ○           ● · ●           · ●·
   
Improves resolution and DOF
k₁ ≈ 0.4-0.5
```

**Mechanism**: Creates interference between diffracted orders for better contrast

### Step 6: Post-Exposure Bake (PEB)

**Purpose**:
1. **Activate photoacid**: Catalytic deprotection
2. **Diffuse acid**: Smooth line edges
3. **Reduce standing waves**: Improve profile

**Process**:
```
Temperature: 100-140°C (resist-dependent)
Time: 60-90 seconds
Control: ±0.1°C critical for CD control
```

**PEB Temperature Sensitivity**:
```
CD Variation ≈ -1 to -3 nm/°C

Example: For 50nm target CD
±0.5°C → ±1.5nm CD variation
```

**Diffusion Length**:
```
L_diff = √(4 × D × t)

Where:
D = Acid diffusion coefficient (~10⁻¹³ cm²/s)
t = PEB time

Typical: L_diff ≈ 10-30nm
```

**Effects**:
- **Under-baked**: Incomplete deprotection, scum, undercutting
- **Over-baked**: Excessive acid diffusion, CD loss, line roughness

### Step 7: Development

**Purpose**: Selectively remove exposed (positive) or unexposed (negative) resist

#### Developer Chemistry

**For Positive CAR** (most common):
```
Developer: TMAH (Tetramethylammonium Hydroxide)
Concentration: 0.26N (2.38% solution)
pH: ~13.5
Temperature: 23°C ±0.1°C
```

**Development Reaction**:
```
Deprotected Polymer (acidic) + TMAH → Soluble salt

Protected Polymer + TMAH → No reaction (insoluble)
```

#### Development Methods

**Puddle Development**:
```
1. Dispense developer on stationary wafer
2. Puddle for 30-60 seconds
3. High-speed rinse spin (DI water)
4. Dry spin (3000 RPM)

Advantages: Uniform, less defects
```

**Spray Development**:
```
1. Spray developer while slowly spinning
2. Multiple spray/spin cycles
3. Rinse and dry

Advantages: Better for high aspect ratio
```

**Immersion Development** (legacy):
```
1. Immerse wafer in developer bath
2. Agitate (30-60 seconds)
3. Rinse in DI water bath
4. Dry (N₂ blow-off)

Disadvantages: Contamination, batch process
```

#### Development Time Optimization

**Development Rate Curve**:
```
Development
Rate
    |      ╱
    |     ╱
    |    ╱
    |   ╱
    |__╱___________  Exposure Dose
    
Threshold dose: Resist starts dissolving
Development time: 30-60 seconds typical
```

**Under-development**:
- Resist residue (scum)
- Poor pattern transfer

**Over-development**:
- Line width loss
- Pattern lifting
- Increased LER

### Step 8: Hard Bake (Post-Develop Bake)

**Purpose**:
1. Improve etch resistance
2. Enhance adhesion
3. Remove residual developer and water
4. Thermally stabilize pattern

**Process**:
```
Temperature: 110-140°C
Time: 60-90 seconds
Method: Hotplate (most common)
```

**Caution**:
- **Too high temperature**: Pattern reflow, CD loss
- **Skip if using resist as sacrificial**: Some processes omit hard bake

## Advanced Lithography Techniques

### Immersion Lithography

**Principle**: Insert liquid between lens and wafer to increase NA

```
          Lens
            ↓
         Water (n=1.44 at 193nm)
            ↓
         Resist
         Wafer
         
NA = n × sin(θ)

Dry: NA_max = 0.93
Immersion: NA_max = 1.35
```

**NA Enhancement**:
```
Resolution improvement:
R_immersion = R_dry / n
R_immersion ≈ 0.7 × R_dry

For 193nm with water:
- Dry: R_min ≈ 65nm
- Immersion: R_min ≈ 38nm
```

**Challenges**:

**1. Water Contamination**:
- Dissolved resist components
- Particles
- Solution: Ultra-pure water (UPW), topcoat

**2. Water Absorption**:
- Resist swelling
- Solution: Hydrophobic topcoat, optimized resist

**3. Bubble Formation**:
- Imaging defects
- Solution: Degassed water, flow control

**Immersion Exposure Head**:
```
        Lens
          ↓
    ┌────────────┐
    │   Water    │  Confined water volume
    │   bubble   │  ~1 mL
    └─────┬──────┘
       Nozzles (water supply/removal)
          ↓
       Wafer
```

**Throughput**: 275+ wafers/hour (state-of-art)

### Optical Proximity Correction (OPC)

**Problem**: Diffraction causes printed features to differ from mask design

**Without OPC**:
```
Mask:        Wafer (actual):
  ████         ╱█████╲    Corners rounded
  ████        ╱       ╲    Lines narrow
  ████        ███████     Gaps fill in
```

**With OPC**:
```
Mask (modified):    Wafer (corrected):
  ████████            ████
  ██  ██              ████  
  ████████            ████
  
Sub-resolution assist features (SRAF)
Serifs on corners
Biasing of line widths
```

**OPC Types**:

**Rule-Based OPC**:
- Apply pre-defined correction rules
- Fast, simple
- Limited accuracy

**Model-Based OPC**:
- Simulate lithography process
- Iteratively correct until target achieved
- Slow (days of computation)
- High accuracy

**Inverse Lithography Technology (ILT)**:
- Optimize mask to produce desired wafer pattern
- Ultra-complex masks
- Best resolution

### Phase-Shift Masks (PSM)

**Principle**: Use phase interference to improve contrast

**Alternating Phase-Shift Mask (Alt-PSM)**:
```
Standard Mask:           Alt-PSM:
Chrome blocks light      Chrome + phase shifters
   ████  ████               ████ 180° ████
    ↓↓    ↓↓                 ↓↓   ↓↓   ↓↓
   Light  Dark             Destructive interference
                           → Enhanced contrast

Phase shift: 180° (half wavelength)
Material: Etched quartz, MoSi
```

**Resolution Improvement**: k₁ can reach 0.25-0.30

**Attenuated PSM (Att-PSM)**:
```
   ████  Atten  ████  Chrome
    ↓↓    ↓      ↓↓    
   100%  6%+180° 100%  Transmission
   
Attenuating layer: Transmits ~6% with 180° phase shift
Advantage: Simpler layout rules than Alt-PSM
```

### Multiple Patterning

**Motivation**: Resolution limit reached at ~40nm half-pitch for 193i

**Techniques**:

#### 1. Litho-Etch-Litho-Etch (LELE)

**Double Patterning**:
```
Litho 1:      Etch 1:       Litho 2:      Etch 2:
████  ████    ████  ████    ████  ████    ████████
  ↓     ↓       ↓     ↓       ↓↓    ↓↓      ↓↓↓↓↓↓
▓▓▓▓▓▓▓▓▓▓    ████  ████    ████████      ████████
──────────    ──────────    ──────────    ──────────

Pitch: 80nm → Effective pitch: 40nm
```

**Process**:
1. First litho + etch (odd lines)
2. Deposit hardmask
3. Second litho + etch (even lines)
4. Combined pattern transfer

**Cost**: 2× lithography steps = 30-40% cost increase

#### 2. Self-Aligned Double Patterning (SADP)

**Process**:
```
1. Core Pattern:          2. Spacer Deposition:
   ████    ████              ╔██╗  ╔██╗
     ↓      ↓                ║▓▓║  ║▓▓║
   ████    ████              ╚██╝  ╚██╝
   ──────────                ──────────

3. Core Removal:          4. Final Pattern:
   ╔╗      ╔╗                ██      ██
   ║║      ║║                ██      ██
   ╚╝      ╚╝                ──────────
   ──────────
   
Pitch reduction: 2×
```

**Advantages**:
- Only one litho step
- Excellent CD uniformity (spacer thickness controlled)
- Lower cost than LELE

**Applications**: Memory (DRAM, NAND), logic metal layers

#### 3. Self-Aligned Quadruple Patterning (SAQP)

**Extension of SADP**:
```
SADP → SADP again

Pitch reduction: 4×
Example: 160nm litho → 40nm effective pitch
```

**Used at**: 7nm and 5nm logic nodes

### Extreme Ultraviolet (EUV) Lithography

**Wavelength**: 13.5 nm (92 eV photon energy)

**Why EUV?**
- Single exposure for 16nm half-pitch (vs. multi-patterning)
- k₁ = 0.5, NA = 0.33 → R ≈ 20nm
- Simplifies process (fewer masks, steps)

#### EUV System Architecture

```
Tin (Sn) Droplet Target
        ↓
CO₂ Laser (25 kW)
        ↓
Plasma (Sn ions, 13.5nm)
        ↓
Collector Mirror (Multilayer coating)
        ↓
Illuminator Mirrors (4-6 mirrors)
        ↓
Reflective Reticle (40-50 layers of Mo/Si)
        ↓
Projection Optics (6 mirrors, NA=0.33 or 0.55)
        ↓
Wafer (EUV resist)
```

**All optics are reflective** (no transmissive materials at 13.5nm)

#### EUV Source

**Laser-Produced Plasma (LPP)**:
```
1. Droplet generator: 50,000 Sn droplets/sec
2. Pre-pulse laser: Flattens droplet
3. Main pulse laser: 25 kW CO₂, creates plasma
4. Plasma emits 13.5nm EUV (in-band)
5. Collector mirror focuses EUV to intermediate focus
```

**Source Power**:
- Current: 500-750W (at intermediate focus)
- Target: 1000W for higher throughput
- Challenge: Debris mitigation (Sn contamination)

#### EUV Mirrors

**Multilayer Coating**:
```
[Mo (2.8nm) / Si (4.1nm)] × 40-50 layers
        ↑
Bragg reflection: Constructive interference

Reflectivity: 70% per mirror
6 mirrors: 0.70⁶ ≈ 12% total transmission
```

**Mirror Specifications**:
- Surface roughness: <0.1nm RMS
- Figure error: <0.5nm RMS
- Coating uniformity: <0.1%

#### EUV Resist

**Requirements**:
- High sensitivity (reduce exposure time)
- High resolution (<16nm)
- Low LER (<2nm)

**Resist Types**:

**Chemically Amplified Resist (CAR)**:
- Sensitivity: 10-20 mJ/cm²
- Resolution: 16-24nm
- Issue: LER, stochastic defects

**Metal-Oxide Resists**:
- Material: Hafnium, Zirconium, Tin oxides
- Sensitivity: 30-50 mJ/cm² (lower than CAR)
- Resolution: 12-16nm
- Better LER and etch resistance

**Challenges**:
- **Stochastic effects**: Photon shot noise at sub-20nm
- **Outgassing**: Contaminates mirrors
- **Throughput**: ~150-170 wafers/hour (vs. 275 for ArFi)

#### EUV Pellicle

**Problem**: Defects on mask surface print on wafer

**Solution**: Pellicle (protective membrane)
```
    Pellicle Frame
         ___
        /   \      Membrane (out of focus)
       /     \
      /       \
     ══════════  EUV Mask (in focus)
```

**Challenges**:
- Must transmit >90% EUV
- Extremely thin (<50nm)
- High thermal load (absorbs EUV)
- Material: Polysilicon, graphene, CNT

**Status**: Still under development (2025), some HVM without pellicle

### High-NA EUV (Future)

**Next Generation**:
- NA: 0.55 (vs. 0.33 current)
- Resolution: 8nm half-pitch (single
