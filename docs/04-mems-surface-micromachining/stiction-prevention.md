# Stiction Prevention in MEMS Surface Micromachining

## Table of Contents
- [Introduction](#introduction)
- [Physics of Stiction](#physics-of-stiction)
- [Drying Techniques](#drying-techniques)
- [Surface Modifications](#surface-modifications)
- [Design Strategies](#design-strategies)
- [In-Use Stiction Prevention](#in-use-stiction-prevention)
- [Characterization Methods](#characterization-methods)
- [Case Studies](#case-studies)
- [References](#references)

## Introduction

Stiction (static friction) is one of the most critical failure mechanisms in MEMS devices, occurring when released microstructures permanently adhere to the substrate or to each other. It can occur during fabrication (release stiction) or during device operation (in-use stiction).

### Types of Stiction

1. **Release Stiction**: During wet etching and drying of sacrificial layers
2. **In-Use Stiction**: During device operation due to contact between surfaces
3. **Charging Stiction**: Electrostatic adhesion from trapped charges

### Impact on Devices

- **Yield Loss**: 20-80% of devices may fail due to stiction
- **Reliability Issues**: Intermittent failures during operation
- **Performance Degradation**: Increased actuation voltage, hysteresis
- **Device Inoperability**: Complete loss of functionality

## Physics of Stiction

### Capillary Forces (Release Stiction)

During drying from aqueous solutions, meniscus formation creates capillary pressure:

```
P_cap = 2γ cosθ / h

Where:
P_cap = capillary pressure (Pa)
γ = surface tension of liquid (N/m)
θ = contact angle (degrees)
h = gap height (m)
```

**For water:**
```
γ_water = 72 mN/m at 20°C
θ ≈ 0° (hydrophilic Si surface)

For h = 2 μm gap:
P_cap = 2 × 0.072 × 1 / (2×10⁻⁶)
P_cap ≈ 72 kPa
```

**Adhesion Force on Beam:**

```
F_adhesion = P_cap × A_contact

For cantilever: L = 200 μm, w = 20 μm
A_contact = L × w = 4 × 10⁻⁹ m²

F_adhesion = 72,000 × 4×10⁻⁹ = 288 μN
```

**Restoring Force:**

For cantilever beam:
```
F_restore = (3EI/L³) × δ

Where:
E = Young's modulus (poly-Si: 160 GPa)
I = moment of inertia = wt³/12
δ = gap height
```

**Stiction occurs when:**
```
F_adhesion > F_restore
```

### Van der Waals Forces

Attractive forces between surfaces in contact:

```
F_vdW = (A_H × A) / (6πD³)

Where:
A_H = Hamaker constant (Si-Si: 1.5-2.5 × 10⁻¹⁹ J)
A = contact area (m²)
D = separation distance (typically 0.2-0.4 nm)
```

**Example Calculation:**
```
For 100 μm × 10 μm contact area:
A = 10⁻⁹ m²
D = 0.3 nm

F_vdW = (2×10⁻¹⁹ × 10⁻⁹) / (6π × (3×10⁻¹⁰)³)
F_vdW ≈ 12 μN
```

### Adhesion Energy

Work required to separate surfaces:

```
W_adhesion = γ₁ + γ₂ - γ₁₂

Where:
γ₁, γ₂ = surface energies of materials
γ₁₂ = interfacial energy
```

**For hydrophobic surfaces (SAM-coated):**
```
γ ≈ 20-30 mJ/m²

For hydrophilic Si:
γ ≈ 70-80 mJ/m²
```

### Critical Length

Maximum beam length before stiction occurs:

```
L_crit = [2Ewt³γ / (3(1-ν²))]^(1/4)

Where:
E = 160 GPa (poly-Si)
w = beam width
t = beam thickness
γ = effective surface energy
ν = Poisson's ratio (0.22 for Si)
```

**Example:**
```
For t = 2 μm, γ = 30 mJ/m²:
L_crit ≈ 150 μm (hydrophobic)
L_crit ≈ 80 μm (hydrophilic)
```

## Drying Techniques

### Critical Point Drying (CPD)

Eliminates liquid-vapor interface by drying through the critical point of CO₂.

**Process Steps:**

1. **Solvent Exchange:**
   ```
   H₂O → IPA (or Ethanol) → Liquid CO₂
   
   Steps:
   - Rinse in DI water
   - 25% IPA, 5 min
   - 50% IPA, 5 min
   - 75% IPA, 5 min
   - 100% IPA, 3× 5 min
   ```

2. **CO₂ Exchange:**
   ```
   - Fill chamber with liquid CO₂
   - Purge 10-15 times
   - Hold at 10°C, 55 bar
   - Exchange for 30-60 min
   ```

3. **Supercritical Drying:**
   ```
   - Heat to 40°C (T_crit = 31°C)
   - Pressure rises to 80-90 bar
   - Slowly vent (1-2 bar/min)
   - No liquid-vapor interface formed
   ```

**Advantages:**
- Near 100% success for properly designed structures
- No capillary forces
- Widely available equipment

**Limitations:**
- Requires specialized equipment
- Time-consuming (1-2 hours per batch)
- Solvent exchange needed
- Cost: $50-200 per batch

**Equipment:**
- Autosamdri-815 (Tousimis)
- Leica EM CPD300
- Typical cost: $30,000-60,000

### Freeze Drying (Sublimation)

Freeze the liquid and sublimate ice directly to vapor.

**Process:**

```
1. Solvent exchange: H₂O → t-Butanol
   - Freezing point: 25.5°C
   - Low surface tension: 20 mN/m
   
2. Freeze structures:
   - Rapid cooling to -20°C
   - Hold for 15 min
   
3. Sublimation:
   - Vacuum: <10 mTorr
   - Temperature: -10 to 0°C
   - Time: 2-4 hours
```

**Advantages:**
- No critical point equipment needed
- Lower cost than CPD
- Can use vacuum chamber

**Limitations:**
- Ice crystal formation can damage structures
- Slower than CPD
- Requires complete solvent exchange

### Supercritical IPA Drying

Alternative to CO₂ CPD using isopropanol.

**Process:**
```
Critical point of IPA:
T_crit = 235°C
P_crit = 47 bar

Process:
1. Direct IPA rinse (no CO₂ exchange)
2. Heat to 250°C in sealed chamber
3. Vent slowly above critical point
```

**Advantages:**
- No solvent exchange needed
- Faster than CO₂ CPD

**Limitations:**
- High temperature (may affect some materials)
- Safety concerns (flammable)
- Specialized equipment required

### Vapor HF Release

Eliminates liquid entirely by using vapor-phase etching.

**Process:**
```
1. XeF₂ or HF vapor etch
   - No liquid rinse needed
   - Direct gas-phase release
   
2. Parameters (HF vapor):
   - Temperature: 30-40°C
   - Pressure: 1-10 Torr
   - Etch rate: 10-50 nm/min
```

**Advantages:**
- Completely avoids stiction during release
- No drying step needed
- Excellent for high aspect ratio structures

**Limitations:**
- Specialized equipment
- Slower etch rates
- Material selectivity constraints

## Surface Modifications

### Self-Assembled Monolayers (SAMs)

Hydrophobic coatings that reduce surface energy and prevent stiction.

#### Silane-Based SAMs

**Common Materials:**

1. **FDTS (Perfluorodecyltrichlorosilane):**
   ```
   Formula: CF₃(CF₂)₇(CH₂)₂SiCl₃
   Contact angle: 110-120°
   Thickness: 1.5-2.0 nm
   Surface energy: 10-15 mJ/m²
   ```

2. **OTS (Octadecyltrichlorosilane):**
   ```
   Formula: CH₃(CH₂)₁₇SiCl₃
   Contact angle: 105-110°
   Thickness: 2.5 nm
   Surface energy: 20-25 mJ/m²
   ```

3. **HMDS (Hexamethyldisilazane):**
   ```
   Formula: (CH₃)₃Si-NH-Si(CH₃)₃
   Contact angle: 80-90°
   Thickness: 0.5-1.0 nm
   Surface energy: 30-35 mJ/m²
   ```

**Deposition Process (Vapor Phase):**

```
Equipment: Vacuum chamber or N₂-purged glove box

Process:
1. Pre-clean wafers:
   - O₂ plasma: 100 W, 2 min (creates OH groups)
   - Alternative: UV/Ozone, 10 min
   
2. SAM deposition:
   - Place wafers in chamber
   - Add 5-10 drops of FDTS (or other silane)
   - Evacuate to 1-10 Torr (or N₂ purge)
   - Temperature: 25-80°C
   - Time: 30-60 min
   
3. Cure (optional):
   - Heat to 120°C, 30 min
   - Improves durability
   
4. Rinse:
   - IPA, 5 min
   - N₂ dry
```

**Liquid Phase Deposition:**

```
Solution preparation:
- FDTS: 0.1-1% in hexane or toluene
- Add dropwise to avoid polymerization

Process:
1. Immerse wafers in solution
2. Time: 5-30 min
3. Rinse in pure solvent (3×)
4. IPA rinse
5. N₂ dry
6. Cure at 120°C, 30 min
```

**Quality Control:**

Contact angle measurement:
```
Good coating: θ > 105°
Acceptable: θ > 95°
Poor: θ < 90° (repeat coating)
```

**Durability:**

- Thermal stability: Up to 200-300°C
- Wear resistance: Moderate (degrades with contact)
- Re-coating: May be needed after high-cycle operation

### Fluorocarbon Plasma Treatment

**C₄F₈ Plasma Coating:**

```
Process:
- Gas: C₄F₈
- Power: 20-50 W
- Pressure: 50-200 mTorr
- Time: 30-120 sec
- Temperature: Room temperature

Result:
- Fluorocarbon polymer layer: 5-20 nm
- Contact angle: 90-110°
- Conformal coating
```

**Advantages:**
- Conformal (reaches all surfaces)
- No liquid handling
- Rapid process
- Inexpensive

**Limitations:**
- Less durable than SAMs
- May degrade at high temperature (>200°C)
- Rougher surface than SAMs

### Alternative Coatings

**1. Parylene:**
```
CVD deposition:
- Thickness: 0.5-5 μm
- Contact angle: 85-95°
- Very conformal
- Biocompatible

Applications:
- Bio-MEMS
- Hermetic sealing
- Long-term protection
```

**2. Diamond-Like Carbon (DLC):**
```
Sputtering or PECVD:
- Thickness: 10-100 nm
- Very hard (wear resistant)
- Contact angle: 70-90°

Applications:
- High contact force devices
- Switches
- Relays
```

## Design Strategies

### Geometric Approaches

#### 1. Dimples and Bumps

Create point contacts instead of large area contact:

```
Dimple design:
- Diameter: 2-5 μm
- Height: 0.5-1 μm
- Spacing: 20-50 μm
- Pattern: Array across contact area

Benefit:
A_contact reduced by 90-99%
F_adhesion ∝ A_contact
```

**Fabrication:**
- Add mask layer for dimple patterning
- Etch dimples in sacrificial layer before structural deposition
- Or use grayscale lithography

#### 2. Surface Roughness

Controlled roughness reduces contact area:

```
RMS roughness: 50-200 nm
Spacing: 1-5 μm

Methods:
- Textured deposition conditions
- Post-deposition etch
- Nanoparticle incorporation
```

**Caution:**
- Too rough: affects device performance
- Not uniform: unpredictable behavior

#### 3. Rib Structures

Elevated ribs instead of flat surfaces:

```
Design:
- Rib width: 1-3 μm
- Spacing: 10-30 μm
- Height: 0.2-0.5 μm above plane

Contact area reduction: 80-95%
```

### Mechanical Design

#### 1. Increased Stiffness

Design stiffer structures to overcome adhesion forces:

```
For cantilever:
k = 3EI/L³

Strategies to increase k:
- Reduce length L (most effective: k ∝ 1/L³)
- Increase thickness t (k ∝ t³)
- Increase width w (k ∝ w)
- Use folded beam designs
```

**Trade-off:**
- Higher stiffness → more force needed for actuation
- Balance between stiction resistance and sensitivity

#### 2. High Aspect Ratio Structures

Increase restoring force through geometry:

```
Folded beam suspension:
- Meander pattern
- Same compliance in desired direction
- Higher stiffness against pull-down

Comb drives:
- Tall fingers (5-20 μm)
- Narrow gaps (2-5 μm)
- Large lateral stiffness
```

#### 3. Curved Structures

Reduce contact area through curvature:

```
Initial curvature:
- Radius: 100-500 μm
- Prevents full surface contact
- Created by stress gradient

Methods:
- Bilayer with different stress
- Thermal mismatch
- Doping gradient
```

### Operational Strategies

#### 1. Overtravel Stops

Limit displacement to prevent contact:

```
Design:
- Hard stops at d_max
- d_max < gap height
- Ensures air gap remains

Gap: 2 μm
Max travel: 1.5 μm
Safety factor: 1.33
```

#### 2. Actuation During Release

Apply voltage during or immediately after release:

```
Process:
1. Begin release etch
2. When ~80% complete, apply voltage
3. Electrostatic force counteracts capillary force
4. Continue etch to completion
5. Maintain voltage until completely dry

Voltage:
V = √(2kd²g₀/εA)
Where:
k = spring constant
d = desired displacement
g₀ = initial gap
```

**Success Rate:**
- Can improve yield from 60% to >95%
- Requires in-situ electrical contact
- Complex setup

#### 3. Anti-Stiction Coatings Before Release

Apply coating before final release:

```
Process flow:
1. Complete device fabrication
2. Apply SAM coating through etch holes
3. Perform final release
4. Structures pre-coated before contact

Advantage:
- Coating present during drying
- Maximum protection
```

## In-Use Stiction Prevention

### Charging Effects

Charge accumulation causes electrostatic stiction:

```
Electrostatic pressure:
P_elec = (ε₀V²)/(2g²)

For V = 50 V, g = 2 μm:
P_elec ≈ 27 kPa

Mitigation:
- Conductive coatings (doped poly-Si)
- AC actuation (prevents charge buildup)
- UV illumination (Si photoconduction)
```

### Contact Force Reduction

Minimize impact force during contact:

```
Soft landing:
- Gradual actuation profile
- Reduced acceleration
- Lower impact velocity

Controlled damping:
- Squeeze film damping
- Optimal gap design
- Q-factor control
```

### Hermetic Packaging

Eliminate moisture and contaminants:

```
Requirements:
- He leak rate: <5×10⁻⁹ atm·cc/s
- Atmosphere: N₂ or Ar, <100 ppm H₂O
- Getter material to absorb residual moisture

Benefits:
- No capillary condensation
- Prevents corrosion
- Eliminates environmental particles
```

### Active Anti-Stiction

Continuous or periodic actuation:

```
Strategies:
1. AC drive signal:
   - Prevents static contact
   - Frequency: 1-100 Hz
   
2. Periodic "shake":
   - Brief high voltage pulse
   - Breaks van der Waals bonds
   - Every 1-10 seconds
   
3. Contact-free operation:
   - Design for no-contact operation
   - Capacitive sensing only
```

## Characterization Methods

### Release Yield Measurement

**Visual Inspection:**
```
Method:
1. Optical microscope survey
2. Count stuck vs. free structures
3. Calculate % yield

Criteria for "stuck":
- No visible gap
- No response to air flow
- Electrical short (if applicable)
```

**Resonance Testing:**
```
Actuate structures at resonance:
- Free structures: clear resonance peak
- Stuck structures: no response or heavily damped

Automated testing:
- Measure Q-factor
- Q < 10: likely stuck
- Q > 50: definitely free
```

### Contact Angle Measurement

Verify coating effectiveness:

```
Equipment:
- Goniometer or contact angle analyzer
- Drop size: 1-5 μL

Procedure:
1. Place drop on coated surface
2. Measure angle within 5 sec
3. Repeat 5-10 locations
4. Calculate mean and std dev

Acceptance criteria:
- Mean θ > 105° (excellent)
- Std dev < 5° (uniform)
```

### Pull-Off Force Measurement

Direct measurement of adhesion:

```
Method:
1. Bring structures into contact
2. Gradually increase separation force
3. Measure force at release

Equipment:
- Nanoindenter with lateral force sensor
- AFM with modified tips
- Custom micro-tensile tester

Typical values:
- Hydrophilic Si: 10-100 μN/μm²
- SAM-coated: 0.1-1 μN/μm²
```

### Kelvin Probe for Surface Potential

Measure charging effects:

```
Kelvin probe force microscopy (KPFM):
- Resolution: 10-50 nm
- Potential resolution: 1-10 mV
- Maps surface charge distribution

Indicates:
- Charge accumulation regions
- Dielectric charging
- Work function variations
```

## Case Studies

### Case Study 1: Accelerometer Comb Drive

**Problem:**
- 150 μm long comb fingers
- 2 μm gap
- 40% yield after wet release

**Analysis:**
```
Capillary force per finger pair:
F_cap = 2γLh / g ≈ 11 μN

Restoring force:
k = 1 N/m
F_restore = k × δ = 1 × 2×10⁻⁶ = 2 μN

Result: F_cap >> F_restore → Stiction!
```

**Solutions Implemented:**

1. **Critical Point Drying:**
   - Yield improved to 85%
   - Cost: +$15/wafer
   
2. **FDTS Coating:**
   - Applied after CPD
   - Final yield: 96%
   - Total cost: +$25/wafer

3. **Design Change:**
   - Added dimples (3 μm diameter)
   - Reduced contact area by 95%
   - Enabled successful water drying
   - Yield: 92% without CPD

**Result:**
- Production uses: CPD + FDTS for 98% yield
- Backup process: Dimples + water dry for cost-sensitive applications

### Case Study 2: RF MEMS Switch

**Problem:**
- Contact switch with Au surfaces
- In-use stiction after 10⁶ cycles
- Stored in ambient conditions

**Root Cause Analysis:**
```
Factors:
1. Capillary condensation from humidity
2. Au-Au cold welding
3. Hydrocarbon contamination buildup
```

**Solutions:**

1. **DLC Coating on Contacts:**
   ```
   Thickness: 20 nm DLC
   Hardness: 15-20 GPa
   Contact resistance: <2 Ω
   
   Result: Cycles improved to >10⁸
   ```

2. **Hermetic Packaging:**
   ```
   Package: Ceramic with Au-Sn eutectic seal
   Atmosphere: 90% N₂, 10% H₂
   Humidity: <50 ppm H₂O
   
   Result: No stiction failures to 10⁹ cycles
   ```

3. **Hot Switching:**
   ```
   Apply RF power during switching
   Self-cleaning effect
   Prevents contamination buildup
   ```

### Case Study 3: Optical MEMS Mirror

**Problem:**
- 500 μm × 500 μm mirror plate
- Torsional hinges: 200 μm × 2 μm × 2 μm
- 70% release yield

**Analysis:**
```
Mirror sticks to substrate during drying
Contact area: 500 × 500 = 250,000 μm²
Capillary force: ~18 mN
Hinge restoring torque: ~5 mN at edge → Insufficient!
```

**Solutions:**

1. **Design Modifications:**
   ```
   - Added 5 μm tall posts under mirror (2.5% area)
   - Contact area reduced by 97.5%
   - Yield improved to 90%
   ```

2. **Actuation During Dry:**
   ```
   - Apply voltage during final IPA evaporation
   - Mirror held at 5° angle
   - Prevents full contact
   - Yield: 98%
   ```

3. **Vapor HF Release:**
   ```
   - Eliminated wet process
   - HF vapor: 3 Torr, 2 hours
   - Yield: 99%
   - Higher cost but justified for low-volume
   ```

## Best Practices Summary

### For Process Engineers

**Release Protocol:**
1. Always use CPD for critical devices
2. Apply SAM coating after release
3. Verify contact angle >105°
4. Store in N₂ cabinet if possible
5. Handle with care (no touching with tweezers)

**Quality Control:**
```
Per batch:
- Visual yield check (minimum)
- Contact angle on witness wafer
- Resonance test on sample devices

Per month:
- Full electrical characterization
- Reliability testing (1000 cycles)
- SEM inspection for coating degradation
```

### For Device Designers

**Design Checklist:**
- [ ] Critical length: L < L_crit (calculate!)
- [ ] Contact area minimized (dimples, ribs)
- [ ] Adequate stiffness (k × factor > 5)
- [ ] Overtravel stops implemented
- [ ] Etch release holes properly sized
- [ ] Test structures included
- [ ] Coating compatibility verified

**Safety Margins:**
```
Restoring force: >5× adhesion force
Gap spacing: >2 μm (if possible)
Dimple coverage: >90% area reduction
SAM coating: Verify every batch
```

### For Researchers

**Experimental Design:**
1. Always include control samples (no treatment)
2. Test multiple coating methods
3. Characterize before and after use
4. Document failure modes
5. Report statistical significance (n ≥ 5)

**Metrics to Report:**
- Release yield (% free structures)
- Contact angle (degrees)
- Pull-off force (if measured)
- Cycle lifetime (for in-use stiction)
- Coating durability (hours, cycles)

## Advanced Topics

### Molecular Dynamics Simulations

Predict adhesion at atomic scale:

```
Tools:
- LAMMPS
- GROMACS
- Materials Studio

Parameters:
- Force fields: Tersoff (Si), OPLS (organics)
- System size: 10-100 nm
- Simulation time: 1-100 ns
- Temperature: 300 K

Outputs:
- Adhesion energy (mJ/m²)
- Force-distance curves
- Molecular orientation
```

### In-Situ TEM Studies

Direct observation of stiction:

```
Capabilities:
- Real-time contact formation
- Nanoscale resolution
- Force measurement (with AFM)

Findings:
- Amorphous layer formation at contact
- Plastic deformation mechanisms
- Effect of surface chemistry
```

### Statistical Yield Modeling

Predict yield from design parameters:

```
Model:
Y = 1 - exp(-L/L_crit)^n

Where:
Y = yield (fraction)
L = structure length
L_crit = critical length
n = fitting parameter (2-4)

Use:
- Optimize design for target yield
- Compare coating effectiveness
- Cost-benefit analysis
```

## Troubleshooting Guide

| Symptom | Possible Cause | Solution |
|---------|----------------|----------|
| Low release yield (<50%) | Insufficient CPD | Verify CO₂ exchange, increase purge cycles |
| | Poor SAM coating | Check contact angle, re-coat |
| | Design issue | Calculate L_crit, add dimples |
| Non-uniform yield | Process variation | Improve uniformity (temperature, flow) |
| | Large area structures | Segment into smaller sections |
| Yield degrades over time | Coating degradation | Re-coat periodically |
| | Storage conditions | Store in N₂ or vacuum |
| In-use stiction | Charging | Use AC actuation, conductive coating |
| | Contamination | Hermetic packaging, cleaning |
| | Wear | DLC coating, reduce contact force |
| Coating non-uniform | Poor surface preparation | Improve cleaning, O₂ plasma |
| | Shadowing in vapor deposition | Rotate wafers, multiple exposures |
| High contact resistance | Thick coating | Reduce coating thickness or use thinner SAM |
| | Contamination | Clean before coating |

## References

1. Mastrangelo, C. H., & Hsu, C. H. (1993). Mechanical stability and adhesion of microstructures under capillary forces—Part I: Basic theory. *Journal of Microelectromechanical Systems*, 2(1), 33-43.

2. Mastrangelo, C. H., & Hsu, C. H. (1993). Mechanical stability and adhesion of microstructures under capillary forces—Part II: Experiments. *Journal of Microelectromechanical Systems*, 2(1), 44-55.

3. Maboudian, R., & Howe, R. T. (1997). Critical review: Adhesion in surface micromechanical structures. *Journal of Vacuum Science & Technology B*, 15(1), 1-20.

4. Tas, N., Sonnenberg, T., Jansen, H., Legtenberg, R., & Elwenspoek, M. (1996). Stiction in surface micromachining. *Journal of Micromechanics and Microengineering*, 6(4), 385.

5. Srinivasan, U., Houston, M. R., Howe, R. T., & Maboudian, R. (1998). Alkyltrichlorosilane-based self-assembled monolayer films for stiction reduction in silicon micromachines. *Journal of Microelectromechanical Systems*, 7(2), 252-260.

6. Ashurst, W. R., Yau, C., Carraro, C., Maboudian, R., & Dugger, M. T. (2001). Dichlorodimethylsilane as an anti-stiction monolayer for MEMS: A comparison to the octadecyltrichlosilane self-assembled monolayer. *Journal of Microelectromechanical Systems*, 10(1), 41-49.

7. Yee, Y., Park, K., & Kang, S. (2001). A method to prevent stiction problems using pulsed voltage and its application to RF MEMS switch. *Proceedings of TRANSDUCERS '01*, 879-882.

---

**Document Information:**
- **Created:** December 9, 2025
- **Version:** 1.0
- **Status:** Complete
- **Part of:** Silicon Fabrication Handbook
- **Next Chapter:** [Device Examples](device-examples.md)
- **Previous Chapter:** [Sacrificial Layers](sacrificial-layers.md)

**License:** CC BY 4.0 - Free to use with attribution

---

*For questions, corrections, or contributions, please visit:*
https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook