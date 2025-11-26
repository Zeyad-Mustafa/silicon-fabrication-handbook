##### C. Shallow Trench Isolation (STI) Stress

**Compressive Stress from STI Oxide**:

```
Mechanism:
  STI oxide fills trenches
       ↓
  Oxide deposited at 400-800°C
       ↓
  Cool to room temperature
       ↓
  Oxide contracts more than Si (higher CTE)
       ↓
  Compressive stress on active region

Structure:
   ┌─────────┐
   │ Active  │ ← Compressed by STI
   │  Area   │
   └─────────┘
   ▓▓▓▓▓▓▓▓▓▓▓  STI oxide squeezes
   
Stress magnitude: 100-500 MPa (compressive)
```

**Optimization**:
```
STI width: Narrower → Higher stress
  But limited by isolation requirements
  
STI depth: Deeper → More stress
  Typical: 200-400nm
  
Process integration:
  Can be beneficial for PMOS (compressive)
  Detrimental for NMOS (needs tensile)
  → Layout-dependent stress
```

**Layout Effects**:
```
Stress varies with:
  - Distance to STI edge (SA parameter)
  - Number of sides surrounded by STI
  - Active area width/length ratio
  
Models needed for circuit simulation!
```

#### 3. Hybrid Orientation Technology (HOT)

**Different Crystal Orientations for NMOS vs. PMOS**:

```
Concept:
  NMOS: (100) surface (standard)
        Electron mobility best on (100)
        
  PMOS: (110) surface
        Hole mobility 2× better on (110)!

Implementation:
1. Start with (100) wafer
2. Etch deep trenches where PMOS will be
3. Regrow Si with (110) orientation (epitaxy)
4. Planarize
5. Fabricate NMOS on (100), PMOS on (110)

    ════════ NMOS (100)
    ╱╲╱╲╱╲  PMOS (110)
    ════════
    
Challenge: Difficult integration (CMP, defects)
Status: Research only, not in production
```

**Mobility Enhancement**:
```
On (110) surface:
  Hole mobility: 2× increase vs. (100)
  Electron mobility: 0.7× (worse!)
  
Combined with strain:
  Can achieve >100% PMOS improvement
```

### Strain Characterization

#### Measurement Techniques

**1. Raman Spectroscopy**:
```
Principle: Laser light scatters off phonons
           Strained lattice → Shifted phonon frequency

Setup:
  Laser (532nm) → Focused spot (1μm²) → Si
       ↓
  Raman scattered light
       ↓
  Spectrometer measures shift

Results:
  Unstrained Si: Raman peak at 520 cm⁻¹
  Compressive: Peak shifts to higher wavenumber
  Tensile: Peak shifts to lower wavenumber
  
  Shift = 4-5 cm⁻¹ per 1% strain
  
Example:
  Peak at 516 cm⁻¹ → Δ = -4 cm⁻¹
               → ~0.8% tensile strain
```

**Advantages**: Non-destructive, spatial resolution ~1μm

**Limitations**: Averages through depth, requires exposed Si

**2. Nano-Beam Diffraction (NBD) in TEM**:
```
Principle: Electron diffraction from strained lattice
           Lattice spacing changes → Diffraction angle changes

Process:
  1. Prepare TEM cross-section sample
  2. Focus e-beam to <10nm spot
  3. Measure diffraction pattern
  4. Extract lattice spacing
  5. Calculate strain: ε = (d - d₀)/d₀

Resolution: 5-10nm spatial, 0.05% strain

Can map 2D strain field!
```

**3. Electrical Characterization**:
```
Split-CV method extracts mobility:
  μ_eff = (g_m / C_ox) × (L / W) × (1 / V_ds)
  
Compare:
  μ_strained / μ_unstrained = Enhancement factor
  
Typical:
  PMOS with SiGe S/D: 1.4-1.8× enhancement
  NMOS with CESL: 1.1-1.2× enhancement
```

### Strain Optimization Strategies

#### Trade-offs

**More Strain ≠ Always Better**:

```
Issue 1: Defect Generation
  High strain → Dislocations, stacking faults
  Critical threshold: ~1.5-2% strain
  Above threshold: Device fails
  
Issue 2: Mobility Saturation
  Mobility enhancement saturates at high fields
  At V_ds = V_dd, benefit reduced
  Strain helps most at low V_ds
  
Issue 3: Parasitic Resistance
  Strained S/D may have higher resistivity
  SiGe: ρ increases with Ge%
  Si:C: ρ increases with C%
  
  If R_sd > R_channel, no net benefit!
```

**Optimal Strain Levels** (empirical):
```
PMOS SiGe S/D:
  Ge content: 25-35% (1.0-1.5% strain)
  Above 40%: Defects increase, yield drops
  
NMOS CESL:
  Liner stress: +1.5 to +2.0 GPa
  Above 2.5 GPa: Film cracks, peels
  
Combined techniques:
  Can achieve 2-3% total strain without defects
```

#### Process Integration Challenges

**Thermal Budget**:
```
Problem: Strain relaxes at high temperature
  SiGe: Stable up to 700-800°C
  Si:C: Stable up to 600-700°C (C precipitates)
  CESL: Stress relaxes above 500°C

Implications:
  - Source/drain anneal: Must be rapid (RTA/laser)
  - No long furnace anneals after S/D
  - Gate-last helps (S/D done before final anneal)

Example sequence:
  1. SiGe S/D epi (650°C)
  2. RTA activation (1050°C, 1 sec) ← Quick!
  3. CESL deposition (400°C)
  4. No more high-T steps
```

**Strain Symmetry**:
```
For matched devices, need symmetric strain

Layout rules:
  - NMOS/PMOS spacing: Controlled
  - Dummy fins: Keep stress environment consistent
  - Same number of fins for matching pairs
  
Otherwise:
  Mismatch in current mirrors, diff pairs
```

---

## Part 3: Advanced HKMG Integration

### Challenges at Sub-7nm Nodes

#### EOT Scaling Limits

**Fundamental Constraint**:

```
EOT = t_IL × (ε_SiO₂ / ε_SiO₂) + t_HK × (ε_SiO₂ / ε_HK)

Where:
  t_IL = Interfacial layer thickness (0.4-0.8nm)
  t_HK = High-κ thickness (1.5-2.5nm)

Problem:
  IL contributes 30-50% of EOT!
  IL cannot be eliminated (interface quality)
  
At 7nm/5nm:
  Target EOT: 0.6-0.8nm
  IL = 0.5nm → Only 0.1-0.3nm budget for HK contribution
  Need κ > 50 (doesn't exist with good properties)
```

**Approaches to Minimize IL**:

1. **Lanthanum Doping**:
```
Add La to HfO₂ or as separate LaOₓ layer
      ↓
La scavenges oxygen from IL during anneal
      ↓
IL thickness reduced by 0.1-0.2nm

Mechanism:
  HfO₂ + La → HfLaO + (scavenges O from IL)
  SiO₂ (IL) → Partially consumed
  
Result: Thinner IL, lower EOT
Side benefit: La also adjusts work function (good for NMOS)
```

2. **Aluminum Oxide Capping**:
```
Deposit thin Al₂O₃ layer (0.5-1nm) on HfO₂
      ↓
Prevents oxygen diffusion through HfO₂
      ↓
Limits IL regrowth during anneals

Structure:
  TiN
  ════  Al₂O₃ cap (0.5nm) ← Oxygen barrier
  ════  HfO₂ (1.5nm)
  ────  IL (0.5nm, stays thin)
  ════  Si
```

3. **Rapid Thermal Processing**:
```
Use laser or flash anneals instead of RTA
  Duration: <1 millisecond
  Temperature: Very high (>1200°C at surface)
  
IL growth kinetic:
  Δt_IL ∝ √(t × exp(-E_a/kT))
  
Short time → Minimal IL growth even at high T
```

#### Work Function Fine-Tuning

**Requirement**: V_th within ±20mV for performance/power targets

**Challenge**: 
```
ΔΦ_m = 50meV changes V_th by ~50mV
TiN work function: 4.3-5.0eV (tunable)
But need precision: ±20meV

Factors affecting Φ_m:
  - TiN composition (Ti/N ratio)
  - Deposition temperature
  - Anneal conditions
  - Interface with HfO₂
  - Film thickness (thin films show quantum effects)
```

**Advanced Tuning Methods**:

**1. Al Doping in TiN**:
```
Ti_(1-x)Al_x N alloy
  x = 0: Φ_m = 4.3-4.6eV
  x = 0.1: Φ_m = 4.5-4.7eV
  x = 0.3: Φ_m = 4.8-5.0eV
  
Control:
  Co-sputtering Ti and Al targets
  Power ratio determines composition
  
Precision: ±10meV achievable
```

2. **Dipole Engineering**:
```
Insert ultra-thin dipole layer between HfO₂ and metal

For NMOS (lower Φ_m):
  La dipole layer (1-2 monolayers)
  Creates negative interface dipole
  Effective Φ_m shift: -0.3 to -0.5eV
  
For PMOS (raise Φ_m):
  Al dipole layer
  Creates positive interface dipole
  Shift: +0.2 to +0.4eV

Precision control by ALD cycles (atomic layer!)
```

3. **Thickness-Dependent Work Function**:
```
Quantum size effects in thin TiN:
  t_TiN < 3nm: Φ_m depends on thickness
  
Example:
  t = 2nm: Φ_m = 4.4eV
  t = 5nm: Φ_m = 4.6eV
  t = 10nm: Φ_m = 4.65eV (bulk value)

Use for fine-tuning: Adjust metal thickness
Typical adjustment range: ±50-100meV
```

#### Gate Leakage Reduction

**Trap-Assisted Tunneling** (dominant at sub-1nm EOT):

```
Mechanism:
  Electron → Trap in HfO₂ → Tunnel to gate
  
  Conduction band
  ═══════════════════
       ↓ e⁻ tunnel
  ● Trap (oxygen vacancy)
       ↓ e⁻ tunnel
  ═══════════════════
  
TAT allows lower energy tunneling than direct
Leakage higher than expected from band gap alone
```

**Defect Reduction Strategies**:

1. **Oxygen Vacancy Passivation**:
```
Problem: O vacancies act as electron traps

Solutions:
  a) Higher O₂ partial pressure during ALD
     Fewer vacancies formed
     
  b) Post-deposition oxygen anneal
     Temperature: 300-500°C in O₂
     Fills existing vacancies
     
  c) Fluorine incorporation
     F substitutes for missing O
     F-passivated defects less active
```

2. **Optimized ALD Recipes**:
```
Pulse/purge timing critical:
  Short purge → Incomplete reaction → Defects
  Long purge → Better quality but slow
  
Optimal conditions (HfO₂):
  Precursor pulse: 0.5s
  Purge 1: 3-5s (critical for quality)
  Oxidant pulse: 0.5s
  Purge 2: 2-3s
  
Result: Lower defect density
  D_it: <10¹⁰ cm⁻²eV⁻¹
  Leakage: 0.1-1 A/cm² @ EOT=0.7nm
```

3. **Multi-Layer Stacks**:
```
Use bilayer or trilayer dielectrics:

Example: HfO₂/Al₂O₃/HfO₂
  ════  HfO₂ (1nm)    ← High κ
  ════  Al₂O₃ (0.5nm) ← Defect blocker, higher bandgap
  ════  HfO₂ (1nm)    ← High κ
  ────  IL
  
Al₂O₃ layer:
  - Larger bandgap (8.8eV vs. 5.8eV)
  - Blocks trap-assisted tunneling
  - Small thickness → Minimal EOT penalty
```

### Gate Stack for FinFETs and GAA

#### Conformal Deposition Requirements

**Challenge**: Coat 3D structures uniformly

```
FinFET gate wraps around fin:

     Top
      │
  ────┼────  Gate wraps
  │   │   │  3 sides
  │   Fin │
  │   │   │
  ────┴────
  
Need uniform:
  - HfO₂ thickness (±0.1nm)
  - TiN thickness (±0.5nm)
  - Work function (±20meV)
  
On all surfaces: top, both sidewalls
```

**ALD Advantage**:
```
Step coverage:
  ALD: >98% (nearly perfect)
  CVD: 70-90% (worse on sidewalls)
  PVD: 30-50% (terrible, line-of-sight)
  
Why ALD wins:
  Self-limiting surface reactions
  Gas-phase precursors reach all surfaces
  Not ballistic deposition
```

**Practical Considerations**:

1. **Aspect Ratio Limits**:
```
Fin spacing: 20-30nm (pitch 40-60nm)
Fin height: 40-50nm

Aspect ratio: H/S = 50/20 = 2.5:1

ALD can coat up to ~10:1 aspect ratio
FinFET: Well within capability

GAA nanosheets:
  Vertical spacing: 10-15nm
  Gate length: 15-20nm
  Aspect ratio when filling: ~5:1
  Still manageable with ALD
```

2. **Purge Time Requirements**:
```
For high aspect ratio:
  Need longer purge to remove all by-products
  Standard: 3-5 seconds
  High AR: 8-12 seconds
  
Otherwise: Incomplete reactions, defects

Trade-off: Longer purge = slower throughput
  But necessary for quality
```

3. **Gap Fill**:
```
W metal fill between fins:

    ╔══════╗ Fin
  ══╬══════╬══  Gate metal (W)
    ╚══════╝ Fin
    
Gap: 20-30nm after HfO₂/TiN
Must fill with W without voids

CVD W conditions:
  - Nucleation layer: WF₆ + SiH₄ (5nm)
  - Bulk fill: WF₆ + H₂
  - Conformal growth (not gap-fill optimized)
  
For narrow gaps: May need bottom-up fill techniques
```

#### Interface Engineering for Multi-Gate

**Fin Sidewall Quality**:

```
Challenge: Sidewalls rougher than (100) top surface

Fin etch:
  RIE creates damaged sidewalls
  Roughness: 0.5-1nm RMS
       ↓
  High interface trap density
       ↓
  Poor mobility

Solution: Sidewall smoothing
  1. Wet etch (HF:HCl mix)
     Removes damage, smooths surface
     
  2. H₂ anneal (800-900°C)
     Atomic-scale smoothing
     Si atoms migrate to minimize energy
     
  3. Sacrificial oxidation
     Grow 1-2nm oxide (consumes rough Si)
     Strip oxide → Smooth Si surface
     
Result: Roughness <0.3nm, D_it similar to (100)
```

**Orientation-Dependent Properties**:

```
FinFET has different crystal orientations:

Top surface: (100)
Sidewalls: (110) or (010) depending on fin direction

Interface properties vary:
  D_it on (110): 1.5-2× higher than (100)
  Mobility on (110): Depends on strain/carrier
  
Need optimization for each surface!
```

### Reliability in Advanced HKMG

#### BTI at Low Voltage

**Challenge**: Low V_dd doesn't mean low stress

```
V_dd scaling:
  65nm: V_dd = 1.0-1.2V
  14nm: V_dd = 0.7-0.8V
  7nm:  V_dd = 0.6-0.7V
  
But:
  EOT also scaled: 2.5nm → 0.7nm
  
Electric field: E = V / EOT
  E_65nm = 1.0V / 2.5nm = 4 MV/cm
  E_7nm = 0.7V / 0.7nm = 10 MV/cm
  
Field actually increased!
```

**BTI Mechanisms Evolve**:

```
Thick oxide (>2nm): Interface trap generation dominant
  Recoverable component: Small
  Permanent damage: Large
  
Thin HK (<1.5nm): Charge trapping dominant
  Recoverable: Large (50-80%)
  Permanent: Small
  
Recovery time: 1μs to 1 second

Implication: AC stress less damaging than DC
  Dynamic operation helps!
```

**Mitigation**:

1. **Optimized Annealing**:
```
Forming gas anneal: D₂/N₂ at 400-450°C, 30 min
  Deuterium passivates traps better than hydrogen
  Si-D bond stronger than Si-H (0.3eV difference)
  
Result: 2-3× improvement in NBTI lifetime
```

2. **Nitrogen Incorporation**:
```
Add N to HfO₂ (HfOₓN_y)
  Plasma nitridation after HfO₂ deposition
  Or: Ammonia anneal
  
Effect:
  - Reduces oxygen vacancy density
  - Improves PBTI (traps in HfO₂ reduced)
  - Maintains high κ (20-22)
  
Trade-off: Slightly increases EOT (κ reduced from 25)
```

#### TDDB Lifetime Projection

**Percolation Model at Thin EOT**:

```
Defect generation:
  Stress → Oxygen ions hop → Create V_o
       ↓
  Defects accumulate near cathode (gate)
       ↓
  Percolation path forms
       ↓
  Breakdown (short)

Time to breakdown:
  t_BD = A × exp(B/E_ox) × exp(E_a / kT)
  
At 0.7nm EOT, 0.7V:
  E_ox = 10 MV/cm (very high!)
  Acceleration vs. operating: 10⁸-10⁹×
```

**Hard vs. Soft Breakdown**:

```
Hard BD:
  Complete short, I_gate → Amps
  Device dead
  
Soft BD:
  Partial path, I_gate → mA
  Device still functions but degraded
  Can have multiple soft BD before hard BD
  
At thin EOT: Soft BD more common
  Digital logic: May tolerate 1-2 soft BD per transistor
  Analog: Cannot tolerate (matching ruined)
```

**Design Margins**:
```
Lifetime requirement: 10 years @ 125°C, V_dd
Safety factor: 10-100×

Test conditions must predict 100-1000 year lifetime!
  Stress: 2× V_dd, 150-175°C
  Duration: Hours to days
  Extrapolation: Arrhenius + E-model
```

### Future Directions

#### Gate-All-Around (GAA) Nanosheets

**Structure** (3nm, 2nm nodes):

```
Cross-section through gate:

   ══════════════  Gate (wraps completely)
   ╔════════════╗
   ║ Nanosheet  ║  Si channel (5nm thick)
   ╚════════════╝
   ══════════════  Gate (top, bottom, sides)
   ╔════════════╗
   ║ Nanosheet  ║
   ╚════════════╝
   ══════════════
   ╔════════════╗
   ║ Nanosheet  ║  3-5 stacked sheets
   ╚════════════╝
   ══════════════
   ══════════════  Source              Drain

Vertical spacing: 10-15nm
Gate length: 12-20nm (true dimension!)
Sheet width: 20-50nm
```

**HKMG Challenges**:

1. **Conformal Coating on 4 Sides**:
```
Must coat:
  - Top of sheet
  - Bottom of sheet (hardest!)
  - Both sidewalls
  
ALD must reach bottom surface through 10nm gap
Requires:
  - Long purge times (10-15 sec)
  - Low pressure (enhance diffusion)
  - Thin sheets (<5nm) to reduce shadowing
```

2. **Work Function Uniformity**:
```
All 4 surfaces must have same Φ_m (±20meV)

Challenge: Bottom surface sees different process
  - Less precursor exposure
  - Different thermal environment
  - Potential incomplete reactions
  
Solution: Optimize ALD recipe for bottom surface
  - Higher precursor dose
  - Longer exposure time
  - Intermediate anneals between layers
```

3. **Inner Spacer Formation**:
```
Spacer must be between sheets:

   ════Gate════
   ┌──────────┐ Sheet
   │  Spacer  │ ← Must fill this gap
   └──────────┘ Sheet
   
Process:
  1. Selectively remove SiGe between sheets
  2. Deposit spacer (SiN) into cavities
  3. Must be conformal and void-free
  
Critical: Spacer prevents gate-S/D short
```

#### 2D Materials Integration

**Monolayer Channels** (research):

```
Replace Si channel with 2D material:
  - MoS₂ (molybdenum disulfide)
  - WSe₂ (tungsten diselenide)
  - Graphene (too metallic, no bandgap)
  
Advantages:
  - Atomic thickness (0.7nm)
  - No dangling bonds at surface
  - High mobility (MoS₂: 200-500 cm²/V·s)
  
HKMG integration:
  Van der Waals contact (no covalent bonding)
  → No interfacial layer needed!
  → Can achieve EOT < 0.5nm
```

**Challenges**:
```
1. Growth: Large-area, uniform MoS₂/WSe₂
2. Transfer: Move to target wafer
3. Contacts: Ohmic contact to 2D material (high resistance)
4. Doping: Cannot implant (too thin!)
5. Integration: Completely different process flow

Status: Research phase, >10 years from production
```

#### Negative Capacitance FETs

**Ferroelectric Gate Stacks**:

```
Structure:
   Metal gate
   ═══════════  TiN
   ═══════════  HfZrO₂ (ferroelectric) ← Negative C!
   ═══════════  HfO₂ (dielectric)
   ───────────  IL
   ═══════════  Si channel
   
Principle:
  C_ferro < 0 (negative capacitance)
  C_total = 1/(1/C_FE + 1/C_ox)
  
If |C_FE| > C_ox:
  C_total > C_ox (amplification!)
       ↓
  Higher transconductance
  Steeper subthreshold slope (SS < 60mV/dec theoretically)
```

**Materials**:
```
Hf_(0.5)Zr_(0.5)O₂ (HZO):
  Ferroelectric phase at specific composition/thickness
  Process: ALD HfO₂ + ZrO₂, anneal to crystallize
  
Properties:
  Remnant polarization: 10-30 μC/cm²
  Coercive field: 0.5-1.5 MV/cm
  Endurance: 10⁶-10⁹ cycles
```

**Status**:
```
Demonstrated: SS < 60mV/dec over limited range
Challenges:
  - Hysteresis (memory effect)
  - Stability over temperature/time
  - Integration with CMOS flow
  
Timeline: Possible for 1nm node (2028-2030?)
```

---

## Summary and Outlook

### Technology Evolution

**Historical Progression**:

```
                Planar        FinFET         GAA          Future?
                (2000s)       (2012-2025)    (2024+)      (2030+)
                  
Gate control:     1-side        3-side        4-side      Atomic
EOT:              1-3nm         0.7-1.2nm     0.5-0.7nm   <0.5nm
Strain:           None/CESL     Embedded S/D  Optimized   2D materials
V_dd:             1.0-1.2V      0.7-0.9V      0.6-0.75V   0.4-0.5V
Stopped at:       22nm          3nm (limit)   1nm?        ???
```

### Current State (2024-2025)

**3nm Production** (TSMC N3, Samsung 3GAE):
- Technology: FinFET (last generation)
- Gate length: ~12-15nm (actual)
- EOT: 0.6-0.8nm
- Strain: SiGe S/D (30-40% Ge) + optimized CESL
- Fins: 5-7 per standard cell transistor
- Density: 300M transistors/mm²

**2nm Development** (planned 2025-2026):
- Technology: GAA nanosheets (first production)
- Gate length: 10-12nm
- Nanosheets: 3-4 stacked, 5nm thick each
- EOT: 0.5-0.7nm (La-doped HfO₂)
- Work function metals: Multi-layer TiN/TaN stacks

### Key Enablers Recap

**FinFET**:
-   Enabled 22nm → 3nm scaling
-   10× leakage reduction vs. planar
-   Better electrostatics (DIBL, SS)
-  Quantized width (design challenge)
-  Parasitic capacitance (3D geometry)

**Strain Engineering**:
-   20-80% mobility enhancement
-   PMOS improved most (critical bottleneck)
-   Multiple techniques stackable
-  Process complexity increased
-  Layout-dependent effects

**Advanced HKMG**:
-   EOT scaled 4× (3nm → 0.7nm)
-   Leakage 10⁵× lower than SiO₂ equivalent
-   Work function precision ±20meV
-  IL limits further EOT scaling
-  Reliability challenges at high fields

### Open Questions

**1. EOT Scaling**:
```
Can we go below 0.5nm?
  - IL contributes 0.3-0.5nm (unavoidable?)
  - Leakage increases exponentially
  - 2D materials may be only path forward
```

**2. Contact Resistance**:
```
R_contact now dominates R_total at 3nm
  Schottky barrier at metal-Si interface
  Shrinking contact area
  
Solutions?
  - Silicides (NiSi, PtSi)
  - Doped contacts (heavily doped epi)
  - Novel contact materials (semi-metal)
```

**3. Power Delivery**:
```
V_dd → 0.5V: Current increases (P = V×I constant)
  Wire resistance limits
  IR drop across chip
  
Need:
  - Backside power delivery
  - Superconducting interconnects?
  - New architectures (3D stacking)
```

**4. Variability**:
```
At 5nm gate, atomic-scale variations matter:
  - Single dopant atoms affect V_th
  - Line edge roughness = multiple atoms
  - Work function granularity (metal grains)
  
Mitigation:
  - Statistical design
  - Error correction
  - Redundancy
```

### The Path Forward

**Short Term (2025-2027)**: 
- GAA nanosheets in production (2nm, 1.4nm nodes)
- HKMG optimization (La doping, optimized anneals)
- Advanced strain (SiGe >40% Ge, optimized layouts)

**Medium Term (2028-2032)**:
- Complementary FET (CFET): Stacked NMOS/PMOS
- Negative capacitance FETs (if hysteresis solved)
- Backside power delivery

**Long Term (2032+)**:
- 2D material channels (MoS₂, WSe₂)
- Novel device concepts (tunneling FETs, spin FETs?)
- Quantum effects become dominant
- New computing paradigms (neuromorphic, quantum)

---

## Conclusion

The transition from planar to FinFET, combined with strain engineering and advanced HKMG, enabled 15+ years of continued scaling from 22nm to 3nm. These innovations showcase the semiconductor industry's ability to overcome fundamental physics limits through clever engineering and materials science.

Key lessons:
1. **3D architecture** (FinFET → GAA) improved electrostatics
2. **Mechanical strain** enhanced mobility without new materials
3. **High-κ dielectrics** broke the SiO₂ barrier
4. **Atomic-level control** (ALD) enabled precise manufacturing

The next decade will test whether silicon CMOS can continue to 1nm and beyond, or whether fundamentally new materials and device architectures will be required. The combination of GAA transistors, aggressive strain engineering, and sub-0.5nm EOT will push the boundaries of what's physically possible.

---

## Further Reading

### Textbooks

1. **"FinFETs and Other Multi-Gate Transistors"** - Colinge, J.-P. (2008)
   - Comprehensive coverage of 3D transistor architectures
   - Theory and experimental results

2. **"Strain-Engineered MOSFETs"** - Takagi, S., et al. (2007)
   - Detailed physics of strain effects
   - Process integration strategies

3. **"High-κ Gate Dielectrics for CMOS Technology"** - Huff, H.R. (2012)
   - Materials science and integration
   - Reliability and characterization

### Seminal Papers

#### FinFET Technology

1. **"FinFET—A Self-Aligned Double-Gate MOSFET Scalable to 20 nm"**
   - Huang, X. et al., *IEEE TED*, 2001
   - First demonstration of practical FinFET
   - DOI: 10.1109/16.974760

2. **"A 22nm SoC Platform Technology Featuring 3-D Tri-Gate and High-k/Metal Gate"**
   - Jan, C.-H. et al. (Intel), *IEDM*, 2012
   - First high-volume FinFET manufacturing
   - DOI: 10.1109/IEDM.2012.6479001

3. **"Evolution of Fin Sidewall Damage During Fin-Etch Processes"**
   - Doris, B. et al., *VLSI Technology*, 2012
   - Critical process issues and solutions

#### Strain Engineering

4. **"A 90nm High Volume Manufacturing Logic Technology Featuring Strained-Silicon"**
   - Ghani, T. et al. (Intel), *IEEE TED*, 2003
   - First production strain engineering
   - DOI: 10.1109/TED.2003.815326

5. **"Strain: A Solution for Higher Carrier Mobility in Nanoscale MOSFETs"**
   - Thompson, S.E. et al., *Ann. Rev. Mater. Res.*, 2006
   - Comprehensive review of strain techniques
   - DOI: 10.1146/annurev.matsci.36.090804.095159

6. **"Stress Memorization Technique (SMT) by Selectively Strained-Nitride Capping"**
   - Shimizu, A. et al., *VLSI Technology*, 2002
   - CESL strain technique

#### Advanced HKMG

7. **"High-κ/Metal Gate Stack and Its MOSFET Characteristics"**
   - Choi, J.H. et al., *IEEE EDL*, 2005
   - Early integration results

8. **"Gate-Last vs. Gate-First Technology for High-k/Metal Gates"**
   - Veloso, A. et al., *IMW*, 2011
   - Process comparison and trade-offs

9. **"Replacement Gate Process for High Performance Transistors"**
   - Packan, P. et al., *IEDM*, 2008
   - Gate-last process details

### Review Articles

10. **"The Future of CMOS Scaling: Challenges and Opportunities"**
    - Bohr, M., *IEEE Solid-State Circuits Magazine*, 2017
    - Industry perspective on advanced nodes

11. **"Gate-All-Around Nanowire and Nanosheet FETs"**
    - Loubet, N. et al., *IEEE Symposium on VLSI Technology*, 2017
    - GAA device architecture and integration

12. **"Strained Silicon Technology: Progress and Challenges"**
    - Rim, K., *MRS Bulletin*, 2009
    - Comprehensive strain engineering review

### Standards and Roadmaps

- **IRDS (International Roadmap for Devices and Systems)**: Annual updates on technology trends
- **IEEE IEDM**: Annual conference proceedings (cutting-edge research)
- **VLSI Technology Symposium**: Biennial symposium proceedings
- **SEMI Standards**: Process and metrology standards

### Online Resources

**Intel Technology Publications**:
- Process architecture papers (publicly available)
- Technology backgrounders

**TSMC/Samsung Technology Days**:
- Annual presentations on node advancement
- YouTube recordings available

**IEEE Xplore**:
- Access to conference proceedings and journals
- Many papers from IEDM, VLSI, EDL

---

## Practical Exercises

### Exercise 1: FinFET Effective Width Calculation

**Problem**: Design a FinFET transistor with equivalent drive current to a 1μm-wide planar transistor.

**Given**:
- Planar: W = 1000nm
- FinFET: H_fin = 45nm, W_fin = 7nm
- Current scales with W_eff

**Calculate**: Number of fins needed

**Solution**:
```
W_eff per fin = 2 × H_fin + W_fin
              = 2 × 45nm + 7nm = 97nm

N_fins = W_planar / W_eff_per_fin
       = 1000nm / 97nm
       ≈ 10.3 fins

Round to: 10 fins (slightly less current)
       or 11 fins (slightly more current)

Design choice: 11 fins for performance
                10 fins for power savings
```

### Exercise 2: Strain-Enhanced Mobility

**Problem**: Calculate expected drive current improvement from strain.

**Given**:
- PMOS with SiGe S/D (30% Ge)
- Hole mobility enhancement: 60%
- Unstrained I_on = 500 μA/μm

**Calculate**: Strained I_on

**Solution**:
```
μ_strained = μ_unstrained × 1.60

Since I_on ∝ μ:
I_on_strained = I_on_unstrained × 1.60
              = 500 μA/μm × 1.60
              = 800 μA/μm

Improvement: 60% or +300 μA/μm
```

**Consideration**: Account for parasitic resistance
```
If R_sd increases 20% due to SiGe:
  Effective improvement: ~50% (not full 60%)
```

### Exercise 3: EOT Calculation

**Problem**: Calculate total EOT for a bilayer high-κ stack.

**Given**:
- IL: SiO₂, t = 0.6nm, κ = 3.9
- HfO₂: t = 2.0nm, κ = 25

**Calculate**: Total EOT

**Solution**:
$
EOT = t_{IL} \times \frac{\kappa_{SiO_2}}{\kappa_{SiO_2}} + t_{HfO_2} \times \frac{\kappa_{SiO_2}}{\kappa_{HfO_2}}
$

$
EOT = 0.6nm \times \frac{3.9}{3.9} + 2.0nm \times \frac{3.9}{25}
$

$
EOT = 0.6nm + 0.312nm = 0.912nm
$

**Interpretation**:
- IL contributes 66% of EOT (0.6/0.912)
- HfO₂ contributes 34% despite being 3.3× thicker
- This shows why minimizing IL is critical

### Exercise 4: Work Function Target

**Problem**: Determine required metal work function for target V_th.

**Given**:
- NMOS on p-substrate
- Target V_th = 0.35V
- Substrate doping: N_A = 5×10¹⁷ cm⁻³
- EOT = 0.8nm

**Simplified calculation**:
```
Flat-band voltage:
V_fb = Φ_ms = Φ_m - (χ_Si + E_g/2 + kT/q × ln(N_A/n_i))

Where:
χ_Si = 4.05eV (Si electron affinity)
E_g = 1.12eV
n_i = 1.0×10¹⁰ cm⁻³

Silicon work function:
Φ_Si = 4.05 + 0.56 + 0.026×ln(5×10¹⁷/1×10¹⁰)
     = 4.05 + 0.56 + 0.46 = 5.07eV

For V_th = 0.35V, approximate:
Φ_m ≈ Φ_Si - 0.5V (simplified)
    ≈ 4.57eV

Target: Φ_m = 4.5-4.6eV (mid-gap metal)
```

### Exercise 5: TDDB Lifetime Extrapolation

**Problem**: Estimate 10-year lifetime voltage from accelerated test.

**Given**:
- Accelerated test: V_test = 2.0V, T_test = 150°C
- Time to 50% failure: t_50 = 100 hours
- Operating conditions: T_op = 85°C
- E-model: β = 0.8 cm/MV (field acceleration)
- E_a = 0.7eV (thermal activation)

**Calculate**: Maximum operating voltage for 10-year lifetime

**Solution**:
```
E-model extrapolation:
t_op / t_test = exp[β × (1/E_op - 1/E_test)]

Arrhenius:
t_op / t_test × exp[E_a/k × (1/T_op - 1/T_test)]

Target t_op = 10 years = 87,600 hours
Acceleration needed = 87,600 / 100 = 876×

From Arrhenius (T only):
exp[0.7eV / 0.026eV × (1/358K - 1/423K)]
= exp[26.9 × 0.000428] = exp(0.0115) ≈ 1.2×

From E-field (remaining 876/1.2 = 730×):
730 = exp[β × (1/E_op - 1/E_test)]

Solving (approximate):
E_op ≈ 0.65 × E_test = 0.65 × (2.0V/EOT)

For EOT = 0.8nm:
V_op_max ≈ 0.65 × 2.0V = 1.3V

Typical operating: 0.7-0.8V (significant margin)
```

---

## Appendix: Technology Node Naming

**Note on Node Names vs. Actual Dimensions**:

```
Node Name    Gate Length    Fin Pitch    Marketing vs Reality
-----------  ------------  -----------  ---------------------
22nm         ~26nm         ~60nm         Gate ≈ name
14nm         ~20nm         ~42nm         Gate > name (1.4×)
10nm         ~18nm         ~34nm         Gate > name (1.8×)
7nm          ~15nm         ~27nm         Gate > name (2.1×)
5nm          ~12nm         ~28nm         Gate > name (2.4×)
3nm          ~12nm         ~24nm         Gate = 4× name!

"Node" now refers to density/generation, not gate length
```

**Industry Standards**:
- **Intel**: More conservative naming (closer to gate length)
- **TSMC/Samsung**: More aggressive naming (based on density)
- **Comparison**: Intel 10nm ≈ TSMC/Samsung 7nm (similar density)

---

## Glossary of Advanced Terms

**ALD (Atomic Layer Deposition)**: Self-limiting sequential surface reactions for atomic-level thickness control

**CESL (Contact Etch Stop Layer)**: Stressed nitride liner that transfers strain to channel

**DIBL (Drain-Induced Barrier Lowering)**: Short-channel effect where drain voltage modulates threshold voltage

**EOT (Equivalent Oxide Thickness)**: Effective thickness if high-κ replaced by SiO₂

**GAA (Gate-All-Around)**: Transistor where gate electrode completely surrounds channel (4-sided control)

**HKMG (High-κ Metal Gate)**: Gate stack using HfO₂ dielectric and metal electrode (typically TiN)

**IL (Interfacial Layer)**: Thin SiO₂ layer between Si and high-κ dielectric

**LDD (Lightly Doped Drain)**: Shallow, low-doped extension of S/D to reduce hot carrier effects

**NBD (Nano-Beam Diffraction)**: TEM technique for strain measurement at <10nm resolution

**SADP (Self-Aligned Double Patterning)**: Lithography technique using spacers to double pattern density

**SIT (Sidewall Image Transfer)**: Fin formation technique using spacers

**SOI (Silicon-On-Insulator)**: Wafer with thin Si layer on buried oxide (BOX)

**STI (Shallow Trench Isolation)**: Oxide-filled trenches for device isolation

**TAT (Trap-Assisted Tunneling)**: Leakage mechanism through defect states in dielectric

**TDDB (Time-Dependent Dielectric Breakdown)**: Gradual degradation leading to gate oxide failure

**W_eff (Effective Width)**: Total channel width in FinFET = N_fins × (2H_fin + W_fin)

---

## Acknowledgments

This chapter synthesizes decades of semiconductor research and development. Key contributions from:

- **Intel**: FinFET commercialization (22nm, 2012)
- **TSMC**: Advanced FinFET nodes and GAA development
- **Samsung**: 3nm FinFET and multi-bridge channel FET
- **IBM Research**: Strain engineering fundamentals
- **Academic Institutions**: UC Berkeley, Stanford, MIT, IMEC

Special recognition to the thousands of engineers and scientists who enabled these technologies through incremental innovations in materials, processes, and device physics.

---

**End of Chapter: Advanced FEOL Topics**

**Previous**: [Gate Stack Formation](gate-stack.md)

**Next**: [Chapter 3 - CMOS BEOL](../03-cmos-beol/)

**Document Version**: 1.0  
**Last Updated**: November 2025  
**Contributors**: Silicon Fabrication Handbook Team

---

**Summary**: This chapter covered the three pillars of advanced CMOS FEOL:

1. **FinFET**: 3D architecture enabling 22nm→3nm scaling through superior electrostatics
2. **Strain Engineering**: Mechanical stress for 20-80% mobility enhancement
3. **Advanced HKMG**: EOT scaling to 0.5-0.7nm with La-doped HfO₂ and optimized metal gates

Together, these technologies have enabled 15 years of continued Moore's Law scaling beyond the planar transistor limit. The transition to GAA nanosheets at 2nm represents the next evolutionary step, while 2D materials and novel device concepts may define the path beyond silicon CMOS.

The future of transistor scaling will require not just better materials and processes, but fundamentally new thinking about device architecture, power delivery, and circuit design. The challenges are immense, but the semiconductor industry has consistently proven its ability to innovate at the boundaries of physics and engineering.# Advanced FEOL Topics: FinFETs, Strain Engineering, and Beyond

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
-   Uniform strain across wafer
-   High strain level (>1%)
-   Both NMOS and PMOS benefit (for n-channel devices)

**Disadvantages**:
-  Expensive (thick epi, long growth time)
-  PMOS needs compressive (this is tensile)
-  Threading dislocations (defects)

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
-   Easy to integrate (standard PECVD)
-   Different stress for NMOS/PMOS (mask and etch)
-   Additive with S/D strain

**Disadvantages**:
-  Lower strain than embedded S/D (0.2-0.5%)
-  Decays with distance from gate

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

**Previous Chapter**: [Gate stack](gate-stack.md)

**Document Version**: 2.2
**Last Updated**: November 2025  
**Contributors**: Zeyad Mustafa