# Semiconductor Fabrication Equipment Reference

This document is a practical, up-to-date equipment map for the Silicon Fabrication Handbook project. It combines standard tool categories, representative examples, and the kinds of outputs produced in this repository.

## Scope

- Focuses on semiconductor and MEMS fabrication for 100 mm to 300 mm wafers.
- Includes research-lab and production-class equipment.
- Lists example tools, typical capabilities, and common use cases.

## Process-to-Equipment Map

| Process Step | Typical Equipment | Notes |
| --- | --- | --- |
| Wafer cleaning | Wet benches, megasonic cleaners | RCA clean, HF dip, solvent cleans |
| Thermal oxidation | Dry/wet oxidation furnaces | Deal-Grove kinetics and growth control |
| Lithography | Contact aligners, steppers, scanners | Masked pattern transfer |
| Resist processing | Spin coater, hot plates, developers | Pre-bake, exposure, post-bake |
| Etching | RIE, ICP, DRIE, wet etch | Pattern transfer into films or Si |
| Deposition | LPCVD, PECVD, ALD, PVD, evaporation | Dielectrics, metals, poly-Si |
| Doping | Ion implanters, diffusion furnaces | Junction formation and activation |
| CMP | CMP polishers | Planarization and surface control |
| Metrology | Ellipsometry, SEM, AFM, profilometer | Thickness, CD, roughness |
| Packaging | Dicers, bonders, wire/flip-chip tools | Final device assembly |

## Lithography

### Steppers and Scanners

| Tool | Application | Wafer Size | Key Capability |
| --- | --- | --- | --- |
| ASML PAS 5500/1150C | i-line DUV | 150 mm, 200 mm | Mature-node and MEMS patterning |
| ASML TWINSCAN NXT:1980Di | ArF immersion | 300 mm | High-resolution immersion lithography |
| ASML TWINSCAN NXE:3600D | EUV | 300 mm | Sub-10 nm patterning |
| Canon FPA-6300ES6a | ArF dry | 300 mm | 65 nm-class dry ArF |
| Nikon NSR-S630D | ArF immersion | 300 mm | 45 nm-class immersion lithography |

### Contact and Proximity Aligners

| Tool | Application | Wafer Size | Key Capability |
| --- | --- | --- | --- |
| SUSS MicroTec MA6/BA6 | R&D, MEMS, packaging | Up to 200 mm | 1–3 µm resolution contact lithography |
| EV Group EVG 620 | MEMS, packaging | Up to 200 mm | High-precision alignment and NIL-ready |

### Mask Writers

| Tool | Technology | Use Case | Key Capability |
| --- | --- | --- | --- |
| Heidelberg DWL 66+ | 405 nm direct-write | R&D photomasks | Sub-micron mask features |
| Vistec SB3054 | E-beam | Advanced masks | 30 nm-class features |

## Deposition Systems

### CVD

| Tool | Type | Typical Films | Notes |
| --- | --- | --- | --- |
| Tempress Vertical Furnace | LPCVD | Poly-Si, Si₃N₄, SiO₂ | Batch, high uniformity |
| Applied Materials Centura 5200 | PECVD | SiO₂, Si₃N₄, SiC | Low-temp deposition |
| Lam Research Vector | PECVD | USG, FSG, PSG, nitride | High AR gap fill |

### ALD

| Tool | Type | Typical Films | Notes |
| --- | --- | --- | --- |
| ASM Pulsar 3000 | Thermal ALD | Al₂O₃, HfO₂, TiN | Å-level control |
| Cambridge Nanotech Savannah | R&D ALD | Oxides, nitrides | Low-volume flexibility |

### PVD and Evaporation

| Tool | Type | Typical Films | Notes |
| --- | --- | --- | --- |
| Applied Materials Endura | PVD cluster | Cu, Al, Ti, TaN | BEOL metals |
| CVC Sputterer | PVD | Specialty metals | R&D scale |
| Temescal BJD-1800 | E-beam evap | Au, Pt, Cr, Ti | Lift-off processes |

## Etching Equipment

### Dry Etch

| Tool | Type | Typical Use | Notes |
| --- | --- | --- | --- |
| Oxford Plasmalab 100 | RIE/ICP | Dielectrics, metals | CF₄, SF₆, Cl₂, BCl₃ |
| Lam Research Rainbow 4520 | RIE | High-volume etch | Production-class throughput |
| STS Pegasus | DRIE | Silicon deep etch | Bosch process |

### Wet Etch

| Tool | Type | Typical Use | Notes |
| --- | --- | --- | --- |
| Wet bench (HF, H₃PO₄, KOH) | Wet | Oxide, nitride, Si anisotropic | Low damage, high selectivity |

## Thermal Processing

| Tool | Type | Typical Use | Notes |
| --- | --- | --- | --- |
| Horizontal/vertical oxidation furnace | Oxidation | SiO₂ growth | Dry or wet oxidation |
| RTP (rapid thermal processor) | Anneal | Dopant activation | Short high-temp cycles |
| Diffusion furnace | Diffusion | B, P diffusion | Junction formation |

## Ion Implantation

| Tool | Type | Typical Use | Notes |
| --- | --- | --- | --- |
| Medium-current implanter | Ion implant | Source/drain | Production process |
| High-energy implanter | Ion implant | Well formation | Deep implants |

## Chemical-Mechanical Polishing (CMP)

| Tool | Type | Typical Use | Notes |
| --- | --- | --- | --- |
| 200/300 mm CMP polisher | CMP | Planarization | STI, interconnects |

## Metrology and Inspection

| Tool | Measurement | Typical Use | Notes |
| --- | --- | --- | --- |
| Ellipsometer | Thickness, n/k | Oxides, nitrides | Non-destructive |
| SEM | CD, defects | Lithography, etch | High-resolution imaging |
| AFM | Roughness, step | Surface quality | Nanometer scale |
| Profilometer | Step height | Etch depth | Contact measurement |
| XRD | Crystallinity | Films and stress | Process control |

## Wafer Handling and Packaging

| Tool | Type | Typical Use | Notes |
| --- | --- | --- | --- |
| Wafer dicer | Dicing | Die singulation | Mechanical or laser |
| Wafer bonder | Bonding | SOI, MEMS | Anodic or fusion |
| Wire/flip-chip bonder | Packaging | Interconnect | Final assembly |

## Facility and Utilities

| System | Purpose | Notes |
| --- | --- | --- |
| Cleanroom HVAC | Particle control | Class 10–1000 typical |
| CDA and N₂ | Pneumatics, purge | Dry gas supply |
| DI water | Wet processing | Ultra-pure water |
| Exhaust and scrubbers | Chemical safety | Acid/base/solvent control |

## How This Connects to This Repository

- Oxide growth equipment maps directly to `simulation-examples/python/oxide_growth_model_3D.py`.
- Lithography, etch, and deposition are visualized in `simulation-examples/python/chip_fabrication_3d.py`.
- MEMS process flows connect to `simulation-examples/python/resonator_response_3D.py` and related scripts.

## Notes

- Tool capabilities vary by configuration and generation.
- Use this list as a reference framework, not a purchasing guide.
- For lab-scale workflows, prioritize aligners, PECVD, RIE, and metrology over high-volume tools.
