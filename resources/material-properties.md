# Material Properties in Semiconductor and MEMS Fabrication

**A comprehensive reference for the electrical, mechanical, thermal, and optical properties of every major material encountered in silicon device fabrication.**

Material selection is one of the most consequential decisions in device engineering. The same silicon that forms the transistor channel, the polysilicon that forms the gate, the silicon dioxide that insulates it, and the copper that connects it to the outside world — each of these materials has a unique set of properties that determines whether the final device works, how reliably it works, and how long it lasts.

This document covers the core materials used in CMOS and MEMS fabrication in the order a process engineer encounters them: starting with the silicon substrate, moving through dielectrics, gate materials, conductors, and finishing with MEMS structural layers and hard masks. Each section provides the key property values with brief explanations of *why that property matters* in practice.

All values are given at room temperature (300 K, 27 °C) unless otherwise stated. Temperature dependence is discussed where it significantly affects device or process behaviour.

---

## Table of Contents

1. [Silicon (Si)](#1-silicon-si)
2. [Silicon Dioxide (SiO₂)](#2-silicon-dioxide-sio₂)
3. [Silicon Nitride (Si₃N₄)](#3-silicon-nitride-si₃n₄)
4. [Polycrystalline Silicon (Polysilicon)](#4-polycrystalline-silicon-polysilicon)
5. [High-k Gate Dielectrics](#5-high-k-gate-dielectrics)
6. [Aluminium (Al)](#6-aluminium-al)
7. [Copper (Cu)](#7-copper-cu)
8. [Tungsten (W)](#8-tungsten-w)
9. [Titanium and Titanium Nitride (Ti / TiN)](#9-titanium-and-titanium-nitride-ti--tin)
10. [Tantalum and Tantalum Nitride (Ta / TaN)](#10-tantalum-and-tantalum-nitride-ta--tan)
11. [Low-k Dielectrics](#11-low-k-dielectrics)
12. [Silicon Carbide (SiC)](#12-silicon-carbide-sic)
13. [Gallium Arsenide (GaAs)](#13-gallium-arsenide-gaas)
14. [MEMS Structural Materials](#14-mems-structural-materials)
15. [Quick-Reference Property Tables](#15-quick-reference-property-tables)

---

## 1. Silicon (Si)

Silicon is the substrate on which nearly every modern semiconductor device is built. Its dominance is not accidental — it combines adequate electrical properties with exceptionally stable native oxide formation, mechanical robustness, and a well-developed industrial supply chain.

### Crystal Structure and Basic Properties

Silicon crystallises in the diamond cubic structure, a face-centred cubic lattice with a two-atom basis. The lattice constant is **0.5431 nm** at 300 K. Each silicon atom forms four covalent bonds in a tetrahedral arrangement. This strong, directional bonding gives silicon its mechanical stiffness and chemical stability.

| Property | Value | Notes |
|----------|-------|-------|
| Crystal structure | Diamond cubic | Space group Fd3̄m |
| Lattice constant | 0.5431 nm | At 300 K |
| Density | 2.329 g/cm³ | Used to calculate film mass |
| Atomic number | 14 | — |
| Melting point | 1414 °C | Limits high-T processing |

### Electrical Properties

| Property | Value | Notes |
|----------|-------|-------|
| Bandgap (E_g) | 1.12 eV | Indirect bandgap |
| Intrinsic carrier concentration (n_i) | 1.0 × 10¹⁰ cm⁻³ | At 300 K; doubles every ~11 °C |
| Intrinsic resistivity | ~230 kΩ·cm | Undoped silicon |
| Electron mobility (µ_n) | 1,400 cm²/V·s | Bulk, lightly doped |
| Hole mobility (µ_p) | 450 cm²/V·s | Bulk, lightly doped |
| Dielectric constant (ε_r) | 11.7 | Used in depletion calculations |
| Breakdown field | ~3 × 10⁵ V/cm | Avalanche breakdown |

**Why the indirect bandgap matters:** Silicon cannot emit light efficiently because the conduction band minimum and valence band maximum occur at different crystal momenta — a phonon is required for a radiative transition. This is why silicon cannot be used for LEDs or laser diodes, and why III-V materials (GaAs, GaN, InP) dominate photonics.

**Carrier mobility and doping:** Mobility decreases as doping increases because ionised impurities scatter carriers. At N_D = 10¹⁸ cm⁻³, electron mobility drops to ~200 cm²/V·s. At 10²⁰ cm⁻³ (source/drain), it falls to ~100 cm²/V·s. This trade-off between low contact resistance (high doping) and high channel mobility (low doping) is fundamental to MOSFET design.

### Mechanical Properties

| Property | Value | Notes |
|----------|-------|-------|
| Young's modulus | 130–188 GPa | Anisotropic; 130 GPa for <100>, 169 GPa for <110> |
| Poisson's ratio | 0.22–0.28 | Depends on crystal direction |
| Yield strength | ~7 GPa | No plastic deformation below fracture |
| Fracture toughness (K_Ic) | 0.7–0.9 MPa·m^0.5 | Brittle fracture |
| Hardness (Vickers) | ~1,000 HV | Very hard — wears diamond dicing blades |
| Knoop hardness | ~1,150 HK | — |

**Why silicon is mechanically ideal for MEMS:** Silicon is a near-perfect elastic material — it does not creep, does not exhibit fatigue in the traditional sense, and deforms perfectly linearly up to fracture. A silicon beam deflected a million times returns to exactly its original position. This makes silicon the preferred structural material for precision MEMS sensors.

**Anisotropy matters for MEMS:** Young's modulus varies with crystal direction. The <100> direction (perpendicular to the most common wafer surface) has E = 130 GPa; the <110> direction has E = 169 GPa. MEMS designers must account for this when calculating spring constants of beams oriented in different directions on the wafer.

### Thermal Properties

| Property | Value | Notes |
|----------|-------|-------|
| Thermal conductivity | 150 W/m·K | Excellent heat spreader |
| Thermal diffusivity | 88 mm²/s | Fast thermal equilibration |
| Specific heat | 700 J/kg·K | — |
| Linear CTE | 2.6 ppm/K | At 300 K; increases at high T |
| Debye temperature | 640 K | — |

**Thermal conductivity in context:** Silicon's thermal conductivity of 150 W/m·K is dramatically higher than that of SiO₂ (1.4 W/m·K) or low-k dielectrics (<1 W/m·K). This means power dissipated in transistors spreads through the silicon substrate effectively, but is blocked by back-end-of-line dielectrics. Thermal management in advanced nodes requires careful attention to the heat path from junction to package.

### Orientation-Dependent Etch Properties

| Etchant | <100> Rate | <110> Rate | <111> Rate | Selectivity |
|---------|-----------|-----------|-----------|-------------|
| KOH (40%, 80°C) | ~1 µm/min | ~2 µm/min | ~0.01 µm/min | <111> stop layer |
| TMAH (25%, 80°C) | ~0.5 µm/min | ~1 µm/min | ~0.01 µm/min | <111> stop layer |
| DRIE (Bosch) | ~5 µm/min | ~5 µm/min | ~5 µm/min | Anisotropic plasma |

The extreme selectivity of KOH and TMAH against <111> planes is exploited to form precisely angled sidewalls and cavities in bulk MEMS micromachining.

---

## 2. Silicon Dioxide (SiO₂)

Silicon dioxide is the most important dielectric in semiconductor manufacturing. Its ability to form a thermally stable, electrically excellent interface with silicon — something no other semiconductor achieves so naturally — is the primary reason silicon won the substrate competition over germanium.

### Formation Methods

SiO₂ can be grown or deposited by several routes, each producing slightly different material:

| Method | Temperature | Density | Applications |
|--------|------------|---------|--------------|
| Thermal (dry O₂) | 900–1100 °C | 2.27 g/cm³ | Gate oxide, tunnel oxide |
| Thermal (wet H₂O) | 900–1100 °C | 2.18 g/cm³ | Field oxide, thick isolation |
| LPCVD TEOS | 650–750 °C | 2.2 g/cm³ | ILD conformal coverage |
| PECVD | 200–400 °C | 2.0–2.2 g/cm³ | BEOL, passivation |
| HDP-CVD | 300–450 °C | 2.2 g/cm³ | STI gap fill |

### Electrical Properties

| Property | Value | Notes |
|----------|-------|-------|
| Dielectric constant (ε_r) | 3.9 | Lowest of common dielectrics |
| Bandgap | 9 eV | Wide-bandgap insulator |
| Breakdown field | ~10 MV/cm | Thermal oxide; PECVD lower |
| Resistivity | >10¹⁶ Ω·cm | Excellent insulator |
| Fixed charge density (Q_f) | 1–5 × 10¹⁰ cm⁻² | At Si/SiO₂ interface |
| Interface trap density (D_it) | <10¹⁰ cm⁻²eV⁻¹ | State-of-art gate oxide |
| Flat-band voltage shift | −0.1 to +0.5 V | Depends on fixed charge |

**Interface trap density and device performance:** The Si/SiO₂ interface has a small density of electrically active defects (dangling bonds, structural disorder). These interface traps capture and emit carriers, causing threshold voltage instability, reduced channel mobility, and 1/f noise. Hydrogen annealing (forming gas, 400–450 °C) passivates dangling bonds and reduces D_it to <10¹⁰ cm⁻²eV⁻¹ — the standard final step in gate dielectric processing.

### Mechanical Properties

| Property | Value | Notes |
|----------|-------|-------|
| Young's modulus | 70 GPa | Amorphous; direction-independent |
| Poisson's ratio | 0.17 | — |
| Hardness (Vickers) | ~600 HV | Softer than silicon |
| Fracture toughness | 0.7–0.8 MPa·m^0.5 | Similar to silicon |
| Residual stress (thermal oxide) | −300 to −500 MPa | Compressive |
| Residual stress (PECVD) | −100 to +300 MPa | Tunable by deposition conditions |

**Compressive stress in thermal oxide:** During oxidation, SiO₂ grows in place on the silicon surface. The molar volume of SiO₂ (22.8 cm³/mol) is larger than that of Si (12.1 cm³/mol per O₂ consumed), so the growing film is under compressive stress. This stress causes wafer bow (important for lithography flatness) and drives the well-known LOCOS bird's beak encroachment at field oxide edges.

### Thermal Properties

| Property | Value | Notes |
|----------|-------|-------|
| Thermal conductivity | 1.4 W/m·K | ~100× lower than silicon |
| CTE | 0.5 ppm/K | Much lower than Si (2.6 ppm/K) |
| Softening point | ~1600 °C | Can flow under stress at high T |

The large CTE mismatch between SiO₂ (0.5 ppm/K) and Si (2.6 ppm/K) means that any temperature change creates differential thermal stress at interfaces. This is the origin of the compressive stress in thermally grown oxide after cooling from the oxidation temperature.

---

## 3. Silicon Nitride (Si₃N₄)

Silicon nitride is the second most important dielectric in silicon fabrication. Its combination of high Young's modulus, chemical inertness, and tensile stress makes it indispensable as a hard mask, etch stop, passivation layer, and MEMS structural film.

### Deposition Methods

| Method | Si:N Ratio | Hydrogen Content | Stress | Applications |
|--------|-----------|-----------------|--------|--------------|
| LPCVD (780 °C, SiH₂Cl₂/NH₃) | Stoichiometric (0.75) | Low (<1 at%) | +1000 MPa tensile | Hard mask, etch stop |
| LPCVD Si-rich nitride | >0.75 | Low | Tunable 0–+1200 MPa | MEMS membranes |
| PECVD (300–400 °C, SiH₄/NH₃) | Sub-stoichiometric | High (20–30 at%) | −100 to +100 MPa | Low-T passivation |

### Electrical Properties

| Property | Value | Notes |
|----------|-------|-------|
| Dielectric constant (ε_r) | 7.5 (LPCVD) / 6–7 (PECVD) | Higher than SiO₂ |
| Bandgap | 5.3 eV | — |
| Breakdown field | ~10 MV/cm | LPCVD; PECVD lower |
| Resistivity | 10¹³–10¹⁶ Ω·cm | Good insulator |
| Refractive index | 2.0 (LPCVD) / 1.8–1.9 (PECVD) | Used for ellipsometry thickness monitoring |

### Mechanical Properties

| Property | Value | Notes |
|----------|-------|-------|
| Young's modulus | 270–290 GPa | Much stiffer than SiO₂ |
| Poisson's ratio | 0.25 | — |
| Hardness (Vickers) | ~1,700 HV | Extremely hard |
| Fracture strength | 6–7 GPa | Higher than silicon |
| Residual stress (LPCVD stoichiometric) | +1,000 to +1,200 MPa | Strong tensile |
| Residual stress (LPCVD Si-rich) | Tunable | Controlled by Si/N ratio and T |

**Stress engineering in MEMS:** LPCVD stoichiometric Si₃N₄ has ~1 GPa of tensile residual stress — useful for pre-tensioning membranes (improves stability and flatness) but detrimental for cantilevers (causes bending). By adjusting the Si:N ratio or using PECVD, engineers can dial in the stress from compressive to highly tensile. Low-stress silicon-rich nitride (Si:N ≈ 0.8–0.9) with ~200 MPa tensile stress is widely used for MEMS membranes.

**Etch selectivity in STI:** LPCVD Si₃N₄ has essentially zero etch rate in HF — the standard SiO₂ etchant. This makes it the ideal hard mask and polish stop in shallow trench isolation (STI) CMP. After trench fill and CMP, the nitride is removed by hot phosphoric acid (H₃PO₄ at 160 °C), which etches Si₃N₄ at ~10 nm/min but is essentially inert to SiO₂.

### Thermal Properties

| Property | Value | Notes |
|----------|-------|-------|
| Thermal conductivity | 19–30 W/m·K | Significantly higher than SiO₂ |
| CTE | 2.8–3.2 ppm/K | Close to silicon |
| Maximum use temperature | >1200 °C | Stable in N₂ ambient |

---

## 4. Polycrystalline Silicon (Polysilicon)

Polysilicon is deposited silicon that lacks long-range crystalline order — it consists of small crystalline grains (typically 10–500 nm) separated by grain boundaries. It is the gate electrode material in conventional CMOS, a resistor material, a field plate material, and a primary structural layer for surface-micromachined MEMS.

### Deposition

Polysilicon is deposited by LPCVD from silane (SiH₄) at 580–650 °C, or from disilane (Si₂H₆) at 450–500 °C for lower-temperature processes. Grain size and orientation are controlled by deposition temperature, pressure, and subsequent annealing.

### Electrical Properties

Polysilicon electrical properties depend strongly on doping:

| Condition | Resistivity |
|-----------|------------|
| Undoped (as-deposited) | 10²–10⁵ Ω·cm |
| N+ doped (phosphorus, ~10²⁰ cm⁻³) | 5 × 10⁻⁴ Ω·cm |
| P+ doped (boron, ~10²⁰ cm⁻³) | 1–3 × 10⁻³ Ω·cm |
| Silicided (TiSi₂, CoSi₂, NiSi) | ~5–15 Ω/□ sheet resistance |

Grain boundaries trap carriers and scatter them, reducing mobility well below single-crystal values. In doped polysilicon, grain boundary segregation and the formation of potential barriers at grain boundaries dominate conduction at low doping levels — hence the non-linear resistivity vs. doping curve.

### Mechanical Properties

| Property | Value | Notes |
|----------|-------|-------|
| Young's modulus | 155–175 GPa | Slightly lower than single-crystal Si |
| Poisson's ratio | 0.22 | Similar to single-crystal |
| Fracture strength | 1–3 GPa | Lower than single-crystal due to grain boundaries |
| Residual stress (undoped, LPCVD) | −100 to +500 MPa | Highly process-dependent |
| Residual stress (after anneal at 1050 °C) | <50 MPa | Stress relief at grain boundaries |

**Stress gradient and MEMS curling:** As-deposited LPCVD polysilicon often has a stress gradient through its thickness — the grain structure and residual stress at the bottom of the film differs from the top. This causes released MEMS structures to curl out of plane. A high-temperature anneal (900–1100 °C) homogenises the film and reduces both mean stress and stress gradient. The MUMPs (Multi-User MEMS Processes) foundry uses a 1050 °C, 30-minute anneal as a standard stress-relief step.

---

## 5. High-k Gate Dielectrics

Below the 45 nm node, silicon dioxide is too thin (< 1.2 nm, fewer than 5 atomic layers) to prevent quantum mechanical tunnelling current, even though the electric field for adequate gate control is present. High-k dielectrics allow a physically thicker film — reducing leakage exponentially — while maintaining the same electrostatic capacitance as a much thinner SiO₂ layer.

The electrical equivalent is expressed as the **equivalent oxide thickness (EOT)**:

> EOT = t_high-k × (ε_SiO₂ / ε_high-k)

A 4 nm film of HfO₂ (ε_r = 25) has the same gate capacitance as a 0.62 nm SiO₂ film, but its leakage current is billions of times lower.

### Hafnium Dioxide (HfO₂) — Industry Standard High-k

| Property | Value | Notes |
|----------|-------|-------|
| Dielectric constant (ε_r) | 18–25 | Depends on phase (monoclinic vs. amorphous) |
| Bandgap | 5.7 eV | — |
| Conduction band offset (vs. Si) | 1.4 eV | Limits barrier for electron tunnelling |
| Breakdown field | 5–6 MV/cm | Lower than SiO₂ |
| Crystallisation temperature | ~500 °C | Amorphous below; must stay amorphous in process |
| Density | 9.68 g/cm³ | — |

### Hafnium Silicate (HfSiO₄)

Adding silicon to HfO₂ raises the crystallisation temperature (useful for high-T compatibility) at the cost of slightly lower ε_r (~12–14). Used in early 45 nm implementations.

### Aluminium Oxide (Al₂O₃)

| Property | Value | Notes |
|----------|-------|-------|
| Dielectric constant (ε_r) | 9 | Lower than HfO₂ |
| Bandgap | 8.8 eV | Higher conduction band offset |
| Breakdown field | 8–10 MV/cm | Better than HfO₂ |
| Crystallisation temperature | ~1000 °C | More thermally stable |

Al₂O₃ is used as an interfacial layer under HfO₂, as a passivation layer for III-V channels, and as the high-k dielectric in DRAM capacitors.

### Zirconium Dioxide (ZrO₂)

| Property | Value | Notes |
|----------|-------|-------|
| Dielectric constant (ε_r) | 22–25 | Similar to HfO₂ |
| Bandgap | 5.8 eV | — |
| Crystallisation temperature | ~400 °C | Lower than HfO₂ — challenge for processing |

Used in DRAM capacitors (ZAZ: ZrO₂/Al₂O₃/ZrO₂ stacks) where its high ε_r is more important than its lower crystallisation temperature.

---

## 6. Aluminium (Al)

Aluminium was the dominant interconnect metal in CMOS from the 1960s through the mid-1990s. It remains in wide use in MEMS, power devices, compound semiconductors, and older-node CMOS.

| Property | Value | Notes |
|----------|-------|-------|
| Crystal structure | FCC | Lattice constant 0.4046 nm |
| Density | 2.70 g/cm³ | Very lightweight |
| Resistivity | 2.65 µΩ·cm | Bulk; thin films higher (~3–4 µΩ·cm) |
| Melting point | 660 °C | Low — limits post-deposition annealing |
| CTE | 23.1 ppm/K | Large mismatch with Si (2.6 ppm/K) |
| Young's modulus | 70 GPa | — |
| Electromigration activation energy | 0.5–0.7 eV | Low — limits current density |
| Maximum current density (wires) | ~1–2 × 10⁵ A/cm² | Conservative rule of thumb |

**Why aluminium was replaced:** Aluminium electromigrates readily under the high current densities required by scaled interconnects. Electromigration causes voids (open circuits) and hillocks (short circuits) that kill devices after months of operation. Al–Cu alloys (0.5–4% Cu) improve electromigration resistance substantially by segregating Cu to grain boundaries, but copper itself (as a pure interconnect) outperforms Al–Cu by 5–10× in both resistivity and electromigration lifetime.

**Al in MEMS:** Aluminium remains important for MEMS because its low Young's modulus and low residual stress (after annealing) are useful for compliant structures. It is widely used for bonding pads, top metal layers, and mirror surfaces in optical MEMS (its reflectivity >90% in visible/IR makes it ideal for digital micromirror devices).

---

## 7. Copper (Cu)

Copper has been the primary interconnect metal since IBM introduced it with their 0.25 µm CMOS process in 1997. Its lower resistivity reduces RC delay; its superior electromigration resistance enables higher current densities.

| Property | Value | Notes |
|----------|-------|-------|
| Crystal structure | FCC | Lattice constant 0.3615 nm |
| Density | 8.96 g/cm³ | ~3× heavier than Al |
| Resistivity (bulk) | 1.67 µΩ·cm | 37% lower than Al |
| Resistivity (thin film, <50 nm) | 2–5 µΩ·cm | Grain boundary and surface scattering |
| Melting point | 1085 °C | Higher than Al |
| CTE | 16.5 ppm/K | Large mismatch with Si; significant thermomechanical stress |
| Electromigration activation energy | 0.7–1.0 eV | Higher than Al — better EM resistance |
| Maximum current density | ~5–10 × 10⁵ A/cm² | 5–10× better than Al |
| Diffusion in Si | Very fast | Kills transistors — must be fully encapsulated |

**The copper diffusion problem:** Copper is a deep-level impurity in silicon, creating energy levels near the centre of the bandgap that act as highly effective recombination centres. Copper diffuses extremely rapidly through silicon and SiO₂ — a Cu atom introduced at the wafer surface can reach the gate oxide in minutes at 200 °C. This is why Cu interconnects require a complete diffusion barrier (TaN/Ta) on all surfaces except the top, and why copper-contaminated equipment must be strictly segregated from transistor fabrication areas.

**Resistivity scaling:** As copper line widths approach or fall below the electron mean free path (~40 nm at room temperature), bulk resistivity is no longer a useful predictor. Grain boundary scattering and surface scattering increase resistivity sharply for lines below ~30 nm — which is why the industry is exploring alternative metals (Ru, Mo, Co) for the narrowest back-end interconnect levels.

---

## 8. Tungsten (W)

Tungsten is the metal of choice for contact plugs (filling the vias from transistor contacts to the first metal layer) and local interconnects in advanced CMOS. Its refractory character makes it compatible with the high temperatures encountered after front-end processing.

| Property | Value | Notes |
|----------|-------|-------|
| Crystal structure | BCC | Lattice constant 0.3165 nm |
| Density | 19.25 g/cm³ | Very heavy — not used for long lines |
| Resistivity (bulk) | 5.6 µΩ·cm | Higher than Cu, adequate for plugs |
| Resistivity (CVD film) | 8–15 µΩ·cm | Depends on grain size and fluorine content |
| Melting point | 3422 °C | Highest of all metals |
| CTE | 4.5 ppm/K | Closer to Si than Al or Cu |
| Young's modulus | 411 GPa | Extremely stiff |
| Deposition method | CVD from WF₆/H₂ | Fluorine incorporation is a concern |

**Why tungsten for contacts:** Tungsten CVD from WF₆ fills sub-micron vias conformally without voids — something that PVD aluminium or copper cannot do in high aspect-ratio features. The CTE of tungsten (4.5 ppm/K) is much closer to silicon than aluminium (23 ppm/K), reducing thermomechanical stress at contacts. The main disadvantage is its high resistivity (~10 µΩ·cm for CVD films), which is acceptable for short plugs but prohibitive for long interconnect lines.

**Fluorine contamination:** WF₆ decomposition leaves trace fluorine in CVD tungsten films. Fluorine can diffuse to the Si/SiO₂ interface during subsequent thermal steps and shift the threshold voltage. A Ti adhesion/barrier layer (CVD TiN) is always deposited before W fill to prevent fluorine attack of the underlying dielectric.

---

## 9. Titanium and Titanium Nitride (Ti / TiN)

Ti and TiN serve as adhesion layers, diffusion barriers, and work-function metals throughout the CMOS and MEMS process stack.

### Titanium (Ti)

| Property | Value | Notes |
|----------|-------|-------|
| Crystal structure | HCP | Lattice constant a = 0.295 nm |
| Density | 4.51 g/cm³ | — |
| Resistivity | 40–60 µΩ·cm | Higher than Al or Cu |
| Melting point | 1668 °C | Refractory |
| CTE | 8.6 ppm/K | — |
| Reaction with Si | Forms TiSi₂ at >600 °C | Basis of salicide process |
| Reaction with N₂ | Forms TiN at >400 °C | In-situ nitridation possible |

**Salicide (self-aligned silicide):** Ti deposited over exposed silicon source/drain and gate contacts reacts during an anneal to form low-resistivity TiSi₂ (15–20 µΩ·cm) exactly where Ti contacts Si — and leaves unreacted Ti over SiO₂ isolation regions, which is then selectively etched. This selective reaction is the principle of the self-aligned silicide (salicide) process. TiSi₂ reduces contact resistance to polysilicon gates and heavily-doped S/D regions from ~1,000 Ω/□ to ~3 Ω/□.

### Titanium Nitride (TiN)

| Property | Value | Notes |
|----------|-------|-------|
| Crystal structure | FCC (NaCl type) | Lattice constant 0.424 nm |
| Density | 5.22 g/cm³ | — |
| Resistivity | 20–100 µΩ·cm | Depends on stoichiometry and microstructure |
| Melting point | 2930 °C | Extremely refractory |
| Young's modulus | 250–600 GPa | Very stiff hard coating |
| Hardness | 20–25 GPa | Used as wear-resistant coating |
| Work function | ~4.6–4.8 eV | Used as NMOS metal gate |
| CTE | 9.4 ppm/K | — |

**TiN in HKMG gates:** In high-k/metal-gate (HKMG) transistors, TiN is deposited by ALD as the metal gate electrode. Its work function (~4.6–4.7 eV) is appropriate for NMOS devices. For PMOS, a different metal (TiAl, TaN, or W) is required to achieve the ~5.2 eV work function needed to set the correct threshold voltage.

---

## 10. Tantalum and Tantalum Nitride (Ta / TaN)

Ta and TaN are the primary diffusion barriers for copper interconnects. They are deposited as a bi-layer (TaN/Ta) lining the trenches and vias before copper electroplating.

### Tantalum (Ta)

| Property | Value | Notes |
|----------|-------|-------|
| Crystal structure | BCC (α) or tetragonal (β) | α is stable; β is metastable |
| Density | 16.65 g/cm³ | Very heavy |
| Resistivity (α-Ta) | 15–20 µΩ·cm | Good for barrier |
| Resistivity (β-Ta) | 150–180 µΩ·cm | Metastable, high resistivity |
| Melting point | 2996 °C | Very refractory |
| CTE | 6.3 ppm/K | — |

**α vs. β Ta:** PVD tantalum deposits in the metastable β phase (high resistivity) unless the substrate is heated or a seed layer is used. The α phase (low resistivity) is preferred for barrier applications. Deposition conditions (temperature, Ar pressure, bias) must be carefully controlled to achieve the α phase.

### Tantalum Nitride (TaN)

| Property | Value | Notes |
|----------|-------|-------|
| Resistivity | 100–300 µΩ·cm | Higher than Ta |
| Melting point | 3090 °C | — |
| Cu diffusion barrier quality | Excellent up to 400 °C | Preferred vs. Ta alone |
| Work function | ~4.0–4.2 eV | Used as PMOS metal gate candidate |

**Why TaN/Ta bilayer for Cu barriers:** TaN is an excellent copper diffusion barrier due to its thermodynamic stability against Cu — Cu does not react with TaN at temperatures up to ~400 °C. However, TaN has poor adhesion to Cu seed layers deposited over it. The Ta top layer provides excellent adhesion for Cu electroplating while the TaN bottom layer provides the barrier function. This 5–15 nm bilayer is deposited by ionised PVD (iPVD) to achieve conformal coverage in high aspect-ratio damascene structures.

---

## 11. Low-k Dielectrics

Interconnect RC delay scales as R × C = (ρL/A) × (εA/d). Reducing the dielectric constant of the interlayer dielectric (ILD) reduces C and therefore RC delay and dynamic power consumption. Below 130 nm, SiO₂ (k = 3.9) is replaced by progressively lower-k materials.

| Material | k Value | Deposition | Trade-offs |
|----------|---------|------------|-----------|
| Fluorinated silicate glass (FSG) | 3.5 | CVD | Minor strength reduction |
| Carbon-doped oxide (CDO, Black Diamond) | 2.7–3.0 | CVD | Lower modulus, moisture absorption |
| Porous CDO (ULKD) | 2.0–2.5 | CVD | Poor mechanical strength |
| Porous SiCOH | 2.0–2.2 | CVD | Integration challenges |
| Air gap | 1.0 | — | Process complexity, structural support |

### Mechanical Impact of Low-k Integration

| Property | SiO₂ | CDO (k=3.0) | Porous CDO (k=2.2) |
|----------|------|------------|-------------------|
| Young's modulus | 70 GPa | 10–20 GPa | 3–8 GPa | 
| Hardness | 8 GPa | 1–3 GPa | 0.5–1 GPa |
| Fracture toughness | 0.7 MPa·m^0.5 | 0.1–0.3 MPa·m^0.5 | <0.1 MPa·m^0.5 |
| CTE | 0.5 ppm/K | 5–10 ppm/K | 8–15 ppm/K |

**The mechanical integration crisis:** As k decreases, mechanical strength degrades severely. Ultra-low-k (ULK) films with k < 2.5 are essentially solid foams — their porosity (30–50 vol%) reduces modulus from 70 GPa to <5 GPa. This creates a serious reliability problem: CMP planarisation exerts mechanical loads that crack or delaminate the fragile low-k film. Copper/low-k stacks must be carefully engineered for CMP compatibility, thermal cycling reliability, and resistance to packaging-induced stress.

---

## 12. Silicon Carbide (SiC)

Silicon carbide is a wide-bandgap semiconductor with exceptional properties for high-power and high-temperature applications where silicon is limited by its 1.12 eV bandgap and relatively low breakdown field.

| Property | 4H-SiC | 6H-SiC | Si (for comparison) |
|----------|--------|--------|---------------------|
| Bandgap (E_g) | 3.26 eV | 3.03 eV | 1.12 eV |
| Critical breakdown field | 2.5–3.5 MV/cm | 2.0–2.5 MV/cm | 0.3 MV/cm |
| Electron mobility | 900 cm²/V·s | 370 cm²/V·s | 1,400 cm²/V·s |
| Thermal conductivity | 370–500 W/m·K | 370–490 W/m·K | 150 W/m·K |
| Saturated electron velocity | 2 × 10⁷ cm/s | 1.9 × 10⁷ cm/s | 10⁷ cm/s |
| Melting point | 2830 °C (sublimes) | — | 1414 °C |
| Density | 3.21 g/cm³ | 3.21 g/cm³ | 2.33 g/cm³ |
| Young's modulus | 460–490 GPa | 460–490 GPa | 130–169 GPa |

**Why SiC for power devices:** The 10× higher breakdown field means SiC power MOSFETs and Schottky diodes can block the same voltage in a 10× thinner drift layer — reducing on-resistance by ~100× compared to silicon at the same voltage rating. SiC 1200 V MOSFETs have captured significant market share in electric vehicle inverters, industrial motor drives, and solar PV inverters. The thermal conductivity advantage further allows SiC devices to operate at higher junction temperatures with smaller heatsinks.

**SiC in MEMS:** SiC's hardness (~26 GPa), chemical inertness (resists KOH, HF, most acids), and stability at >500 °C make it attractive for harsh-environment MEMS sensors. SiC pressure sensors can operate continuously at 500–600 °C — far beyond silicon's limit (~150 °C for practical devices).

---

## 13. Gallium Arsenide (GaAs)

GaAs is the dominant substrate for III-V compound semiconductor devices used in RF, microwave, and photonic applications. Its direct bandgap enables efficient light emission; its high electron mobility enables high-speed transistors.

| Property | GaAs | Si (for comparison) |
|----------|------|---------------------|
| Crystal structure | Zinc blende | Diamond cubic |
| Lattice constant | 0.5653 nm | 0.5431 nm |
| Bandgap | 1.42 eV (direct) | 1.12 eV (indirect) |
| Electron mobility | 8,500 cm²/V·s | 1,400 cm²/V·s |
| Hole mobility | 400 cm²/V·s | 450 cm²/V·s |
| Saturated electron velocity | 2.1 × 10⁷ cm/s | 10⁷ cm/s |
| Breakdown field | 0.4 MV/cm | 0.3 MV/cm |
| Intrinsic carrier concentration | 1.8 × 10⁶ cm⁻³ | 10¹⁰ cm⁻³ |
| Dielectric constant | 12.9 | 11.7 |
| Thermal conductivity | 46 W/m·K | 150 W/m·K |
| Density | 5.32 g/cm³ | 2.33 g/cm³ |

**GaAs advantages and limitations:** The 6× higher electron mobility enables cutoff frequencies (f_T) exceeding 300 GHz in HEMTs, which silicon cannot approach. The semi-insulating substrate (resistivity >10⁷ Ω·cm) allows microwave circuit elements to be fabricated directly without the resistive silicon substrate losses that limit RF performance. The direct bandgap enables LEDs, laser diodes, solar cells, and photodetectors — the entire GaAs photonics industry. The main disadvantages are the 3× higher cost per wafer area (limited to 150 mm diameter in production vs. 300 mm for Si), brittleness, and the absence of a stable native oxide analogous to SiO₂.

---

## 14. MEMS Structural Materials

MEMS devices require structural materials that can be deposited in thin-film form, patterned by lithography, and released by sacrificial etching — a different set of constraints from bulk wafer materials.

### Polysilicon (MEMS context)

Already covered in Section 4. The dominant surface-micromachining structural material. Key property for MEMS: Young's modulus of 155–175 GPa, near-zero creep, and excellent fatigue resistance.

### Silicon Nitride Membranes

Low-stress LPCVD silicon-rich nitride (Si:N ≈ 0.85) with ~200 MPa tensile stress is used for free-standing membranes in pressure sensors, microphones, and AFM cantilevers. The tensile stress prevents buckling and keeps membranes flat after release.

### Gold (Au) — RF MEMS and Bonding

| Property | Value | Notes |
|----------|-------|-------|
| Resistivity | 2.2 µΩ·cm | Low; excellent for RF contacts |
| Young's modulus | 79 GPa | — |
| Hardness | 0.2–0.3 GPa | Very soft — wears and cold-welds |
| CTE | 14.2 ppm/K | — |
| Melting point | 1064 °C | — |
| Adhesion to Si/SiO₂ | Poor — requires Ti or Cr adhesion layer | — |

Gold is used for RF MEMS switches (low contact resistance, low insertion loss), wire bonding pads, and eutectic bonding (Au-Si at 363 °C, Au-Sn at 280 °C). Its softness makes it unreliable for high-cycle mechanical switches; electroplated nickel or rhodium contacts are preferred for long-life applications.

### Nickel (Ni) — LIGA and Electroplated MEMS

| Property | Value | Notes |
|----------|-------|-------|
| Young's modulus | 200 GPa | Stiff structural material |
| Tensile strength | 150–450 MPa | Depends on grain structure |
| Hardness | 1–5 GPa | Harder than Au |
| Resistivity | 6.9 µΩ·cm | — |
| CTE | 13.4 ppm/K | — |
| Electroplating bath | Nickel sulfamate | Produces low-stress deposits |

Electroplated nickel is the structural material for LIGA (Lithographie, Galvanoformung, Abformung) and deep UV MEMS — fabricating thick (10–1,000 µm), high-aspect-ratio metal structures with vertical sidewalls. Used for microactuators, gears, and injection-moulding tools.

### Diamond and Diamond-Like Carbon (DLC)

| Property | Diamond | DLC | Notes |
|----------|---------|-----|-------|
| Young's modulus | 1,050 GPa | 100–800 GPa | Hardest material |
| Hardness | 70–100 GPa | 10–40 GPa | Excellent wear resistance |
| Thermal conductivity | 2,000 W/m·K | 2–10 W/m·K | Diamond: best known conductor |
| Bandgap | 5.47 eV | 1–4 eV | Wide bandgap |
| Resistivity | 10¹³ Ω·cm (undoped) | Tunable | — |
| CTE | 1.0 ppm/K | 1–3 ppm/K | Very low |

Diamond and DLC are emerging MEMS materials for extreme environments (high temperature, aggressive chemistry, radiation) and as hard coatings on MEMS contact surfaces to prevent wear.

---

## 15. Quick-Reference Property Tables

### 15.1 Electrical Properties Comparison

| Material | Bandgap (eV) | ε_r | Resistivity (Ω·cm) | Breakdown Field (MV/cm) |
|----------|-------------|-----|---------------------|------------------------|
| Si | 1.12 (indirect) | 11.7 | 2.3 × 10⁵ (intrinsic) | 0.3 |
| SiO₂ | 9.0 | 3.9 | >10¹⁶ | 10 |
| Si₃N₄ | 5.3 | 7.5 | 10¹³–10¹⁶ | 10 |
| HfO₂ | 5.7 | 18–25 | >10¹⁴ | 5–6 |
| Al₂O₃ | 8.8 | 9 | >10¹⁴ | 8–10 |
| GaAs | 1.42 (direct) | 12.9 | ~10⁷ (semi-ins.) | 0.4 |
| 4H-SiC | 3.26 (indirect) | 9.7 | Varies | 2.5–3.5 |
| Diamond | 5.47 (indirect) | 5.7 | 10¹³ (undoped) | 10 | 

### 15.2 Mechanical Properties Comparison

| Material | Young's Modulus (GPa) | Poisson's Ratio | Density (g/cm³) | Fracture Strength (GPa) |
|----------|----------------------|-----------------|-----------------|------------------------|
| Si <100> | 130 | 0.28 | 2.33 | 4–7 |
| Si <110> | 169 | 0.24 | 2.33 | 4–7 |
| SiO₂ (thermal) | 70 | 0.17 | 2.27 | 8–10 |
| Si₃N₄ (LPCVD) | 270–290 | 0.25 | 3.19 | 6–7 |
| Polysilicon | 155–175 | 0.22 | 2.33 | 1–3 |
| SiC (4H) | 460–490 | 0.21 | 3.21 | 10–20 |
| Al | 70 | 0.35 | 2.70 | 0.1–0.4 |
| Cu | 130 | 0.34 | 8.96 | 0.1–0.4 |
| W | 411 | 0.28 | 19.25 | 1.5–2.0 |
| Au | 79 | 0.44 | 19.32 | 0.1–0.2 |
| TiN | 250–600 | 0.25 | 5.22 | 3–5 |
| Diamond | 1,050 | 0.07 | 3.51 | 6–10 |

### 15.3 Thermal Properties Comparison

| Material | Thermal Conductivity (W/m·K) | CTE (ppm/K) | Melting Point (°C) |
|----------|-----------------------------|-------------|-------------------|
| Si | 150 | 2.6 | 1414 |
| SiO₂ | 1.4 | 0.5 | ~1600 (softens) |
| Si₃N₄ | 20–30 | 2.8–3.2 | >1800 |
| Polysilicon | 30–45 | 2.8 | 1414 |
| Al | 237 | 23.1 | 660 |
| Cu | 401 | 16.5 | 1085 |
| W | 174 | 4.5 | 3422 |
| Ti | 22 | 8.6 | 1668 |
| TiN | 11–20 | 9.4 | 2930 |
| Au | 318 | 14.2 | 1064 |
| GaAs | 46 | 5.7 | 1238 |
| 4H-SiC | 370–500 | 4.0 | 2830 (sublimes) |
| Diamond | 2,000 | 1.0 | 3550 |

### 15.4 Residual Stress in Deposited Films

| Film | Deposition Method | Typical Stress | Sign | Notes |
|------|-----------------|----------------|------|-------|
| SiO₂ | Thermal (dry) | 300–500 MPa | Compressive | Increases with thickness |
| SiO₂ | PECVD | 50–300 MPa | Tunable | Depends on RF power, T |
| Si₃N₄ | LPCVD stoichiometric | 1,000–1,200 MPa | Tensile | Strong, consistent |
| Si₃N₄ | LPCVD Si-rich | 100–400 MPa | Tensile | Tunable by Si:N ratio |
| Si₃N₄ | PECVD | −100 to +100 MPa | Tunable | Low stress possible |
| Polysilicon | LPCVD as-deposited | −100 to +500 MPa | Variable | Strongly process-dependent |
| Polysilicon | LPCVD + 1050 °C anneal | <50 MPa | Near-zero | Standard MEMS process |
| Al | PVD | −200 to +200 MPa | Compressive typical | Depends on T, rate |
| Cu | Electroplated | −50 to +100 MPa | Tunable | Controlled by additives |
| W | CVD | −500 to −2000 MPa | Compressive | Can delaminate if too thick |
| TiN | PVD | +1,000 to −1,000 MPa | Tunable | By N₂ partial pressure |

### 15.5 Etch Selectivity Summary (RIE/CDE)

| Material Etched | Etchant/Chemistry | Selectivity vs. SiO₂ | Selectivity vs. Si₃N₄ | Notes |
|-----------------|------------------|----------------------|----------------------|-------|
| Si | SF₆/O₂ (RIE) | ~20:1 | ~15:1 | Standard Si etch |
| Si | Cl₂/HBr | ~30:1 | ~20:1 | Gate etch |
| SiO₂ | CHF₃/Ar | 1 (reference) | ~3:1 | Contact etch |
| SiO₂ | CF₄/CHF₃ | 1 (reference) | ~5:1 | ILD etch |
| Si₃N₄ | CF₄/O₂ | ~0.3:1 | 1 (reference) | |
| Si₃N₄ | H₃PO₄ (wet, 160°C) | >200:1 | 1 (reference) | High selectivity wet strip |
| Al | Cl₂/BCl₃ | >100:1 | >100:1 | Post-etch corrosion concern |
| W | SF₆/N₂ | >100:1 | >100:1 | Plug etch-back |

---

## Further Reading

- Neamen, *Semiconductor Physics and Devices* — foundational electrical properties treatment
- Sze & Ng, *Physics of Semiconductor Devices* (3rd ed.) — comprehensive device physics reference
- Wolf & Tauber, *Silicon Processing for the VLSI Era* (Vol. 1) — process-focused material properties
- Senturia, *Microsystem Design* — MEMS-specific mechanical and thermal properties
- Madou, *Fundamentals of Microfabrication* — material behaviour in MEMS context
- Murarka, *Silicides for VLSI Applications* — detailed treatment of silicide and metal systems
- NIST Material Properties Database — [webbook.nist.gov](https://webbook.nist.gov)
- Ioffe Physical Technical Institute Database — [matprop.ru](http://www.matprop.ru) — semiconductor property tables

---

*Part of the Silicon Fabrication Handbook — [github.com/Zeyad-Mustafa/silicon-fabrication-handbook](https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook)*  
*Last updated: February 2026*