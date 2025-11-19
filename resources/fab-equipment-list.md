# Semiconductor Fabrication Equipment Reference

A comprehensive guide to common equipment used in semiconductor and MEMS fabrication facilities.

## 📋 Table of Contents

1. [Lithography](#lithography)
2. [Deposition Systems](#deposition-systems)
3. [Etching Equipment](#etching-equipment)
4. [Thermal Processing](#thermal-processing)
5. [Ion Implantation](#ion-implantation)
6. [Chemical-Mechanical Polishing](#chemical-mechanical-polishing)
7. [Metrology & Inspection](#metrology--inspection)
8. [Wafer Handling](#wafer-handling)

---

## Lithography

### Photolithography Steppers & Scanners

#### ASML DUV Systems

**ASML PAS 5500/1150C**
- **Application**: I-line lithography (365nm)
- **Resolution**: 350nm minimum feature size
- **Wafer Size**: 150mm, 200mm
- **Typical Use**: Mature nodes, MEMS
- **Throughput**: 90-120 wafers/hour
- **Price Range**: $2-5M (used)

**ASML TWINSCAN NXT:1980Di**
- **Application**: ArF immersion (193nm)
- **Resolution**: 38nm minimum pitch
- **Wafer Size**: 300mm
- **NA**: 1.35 (water immersion)
- **Overlay**: <2nm (3σ)
- **Throughput**: 275 wafers/hour
- **Price**: $70-90M

**ASML TWINSCAN NXE:3600D (EUV)**
- **Application**: Extreme UV (13.5nm)
- **Resolution**: Sub-10nm features
- **Wafer Size**: 300mm
- **NA**: 0.33
- **Throughput**: 170 wafers/hour
- **Price**: ~$150M
- **Power**: 1 MW facility requirement

#### Canon FPA-6300ES6a
- **Application**: ArF dry lithography
- **Resolution**: 65nm node
- **Wafer Size**: 300mm
- **Overlay**: 8nm
- **Throughput**: 135 wafers/hour

#### Nikon NSR-S630D
- **Application**: ArF immersion
- **Resolution**: 45nm half-pitch
- **Wafer Size**: 300mm
- **Double patterning capable**

### Contact/Proximity Aligners

**SUSS MicroTec MA6/BA6**
- **Application**: Research, MEMS, packaging
- **Wafer Size**: Up to 200mm
- **Resolution**: 1-3μm (contact mode)
- **Alignment Accuracy**: ±1μm
- **Price**: $150-350K
- **UV Source**: Hg lamp (i-line, g-line, broadband)

**EV Group EVG 620**
- **Application**: Advanced packaging, MEMS
- **Wafer Size**: Up to 200mm
- **Resolution**: <1μm (vacuum contact)
- **Features**: Automated alignment, NIL capable

### Mask Writers

**Heidelberg DWL 66+**
- **Technology**: Direct-write laser (405nm)
- **Min Feature**: 600nm
- **Application**: Photomask fabrication, R&D
- **Substrate Size**: Up to 8"
- **Price**: $400-600K

**Vistec SB3054**
- **Technology**: E-beam mask writing
- **Resolution**: 30nm
- **Application**: Advanced photomask production
- **Throughput**: 1-2 masks/day

---

## Deposition Systems

### Chemical Vapor Deposition (CVD)

#### Low-Pressure CVD (LPCVD)

**Tempress Vertical LPCVD Furnace**
- **Films**: Polysilicon, Si₃N₄, SiO₂, doped films
- **Wafer Capacity**: 25-150 wafers/batch
- **Temperature**: 400-900°C
- **Pressure**: 100-600 mTorr
- **Uniformity**: <2% (1σ)
- **Throughput**: ~50-100 wafers/hour
- **Price**: $800K-1.5M

**Applications**:
- Polysilicon gates: 580-620°C, SiH₄
- LPCVD nitride: 750-850°C, SiH₂Cl₂ + NH₃
- TEOS oxide: 650-750°C

#### Plasma-Enhanced CVD (PECVD)

**Applied Materials Centura 5200**
- **Films**: SiO₂, Si₃N₄, SiC, a-Si, SiCN
- **Wafer Size**: 200mm, 300mm
- **Temperature**: 250-400°C (low-temp capability)
- **Frequency**: 13.56 MHz, 400kHz (dual-frequency)
- **Uniformity**: <1.5%
- **Throughput**: 60-90 wafers/hour
- **Price**: $2-4M

**Lam Research Vector**
- **Application**: Dielectric deposition
- **Films**: USG, FSG, PSG, nitride
- **Gap fill capability**: High aspect ratio
- **Throughput**: 120+ wafers/hour

#### Atomic Layer Deposition (ALD)

**ASM Pulsar 3000**
- **Films**: Al₂O₃, HfO₂, TiN, TaN, Ru
- **Wafer Size**: 300mm
- **Temperature**: 50-400°C
- **Thickness Control**: Ångström-level
- **Conformality**: >95% on high AR structures
- **Price**: $2-3M

**Cambridge Nanotech Savannah**
- **Application**: R&D, low volume
- **Wafer Size**: Up to 200mm
- **Films**: Oxides, nitrides, metals
- **Price**: $300-600K

### Physical Vapor Deposition (PVD)

#### Sputtering Systems

**Applied Materials Endura**
- **Metals**: Cu, Al, Ti, TiN, Ta, TaN, W
- **Wafer Size**: 300mm
- **Cluster tool**: Multiple chambers
- **Process**: PVD + CVD + preclean
- **Applications**: BEOL metallization
- **Throughput**: 80-120 wafers/hour
- **Price**: $3-6M

**Features**:
- Ionized metal plasma (IMP) for Cu
- Self-ionized plasma (SIP)
- Collimation for via filling

**CVC Sputterer**
- **Application**: R&D, specialty films
- **Wafer Size**: Up to 150mm
- **Targets**: 2-4 cathodes
- **Base Pressure**: <1×10⁻⁷ Torr
- **Price**: $200-500K

#### Evaporation Systems

**Temescal BJD-1800**
- **Technology**: E-beam evaporation
- **Wafer Size**: Up to 200mm
- **Materials**: Metals (Au, Pt, Cr, Ti)
- **Rate**: 0.1-50 Å/s
- **Application**: Lift-off processes, contacts
- **Price**: $150-400K

---

## Etching Equipment

### Dry Etch (Plasma) Systems

#### Reactive Ion Etch (RIE)

**Oxford Instruments Plasmalab System 100**
- **Application**: Dielectric and metal etch
- **Wafer Size**: 100mm, 150mm, 200mm
- **Chemistry**: CF₄, SF₆, Cl₂, BCl₃, CHF₃, O₂
- **Frequency**: 13.56 MHz
- **Features**: ICP optional, load lock
- **Price**: $300-700K

**Lam Research Rainbow 4520**
- **Application**: Oxide, nitride, poly-Si etch
- **Wafer Size**: 200mm
- **Chemistry**: Multiple gas manifolds
- **Selectivity**: >50:1 typical
- **Uniformity**: <3%

#### Inductively Coupled Plasma (ICP)

**Oxford Instruments PlasmaLab System 100 ICP**
- **Application**: High-density plasma etch
- **Features**: Independent RF and ICP control
- **Etch Rate**: 2-10× higher than RIE
- **Anisotropy**: Excellent for high AR
- **Price**: $500K-1M

**Panasonic (Anelva) ICP Etcher**
- **Application**: Dielectric and conductor etch
- **Wafer Size**: 300mm capable
- **Magnetic field enhancement**

#### Deep Reactive Ion Etch (DRIE)

**SPTS Rapier DRIE**
- **Application**: High aspect ratio Si etch (MEMS)
- **Wafer Size**: 100mm, 150mm, 200mm
- **Process**: Bosch process (SF₆/C₄F₈ cycle)
- **Etch Rate**: 2-5 μm/min
- **Aspect Ratio**: >30:1
- **Selectivity**: >100:1 (Si:photoresist)
- **Price**: $600K-1.2M

**Oxford Instruments PlasmaPro 100 Cobra**
- **Application**: Advanced DRIE
- **Features**: Cryogenic etch capability
- **Sidewall angle control**: ±1°
- **Mask compatibility**: Oxide, metal, thick resist

### Wet Etch Stations

**Standard Wet Bench**
- **Configuration**: 6-12 bath modules
- **Materials**: PFA, PTFE tanks
- **Common Baths**:
  - RCA clean (SC-1, SC-2)
  - HF dip (1-10% HF)
  - BOE (buffered oxide etch)
  - H₃PO₄ (nitride strip, 160°C)
  - Piranha (H₂SO₄:H₂O₂)
- **Features**: N₂ sparging, temperature control
- **Wafer Size**: Up to 300mm
- **Price**: $100-300K (per bench)

**Semitool Raider Spin Processor**
- **Application**: Single-wafer wet processing
- **Processes**: Clean, etch, strip
- **Wafer Size**: 200mm, 300mm
- **Throughput**: 60-120 wafers/hour
- **Chemical delivery**: Automated
- **Price**: $400-800K

---

## Thermal Processing

### Oxidation and Diffusion Furnaces

**Thermco Vertical Furnace**
- **Application**: Thermal oxidation, diffusion, anneal
- **Wafer Capacity**: 25-150 wafers/batch
- **Temperature**: Up to 1200°C
- **Zones**: 3-zone heating (top, center, bottom)
- **Atmosphere**: O₂, H₂O, N₂, HCl
- **Uniformity**: <±2°C across zone
- **Price**: $300-800K

**Processes**:
- Dry oxidation: 900-1150°C in O₂
- Wet oxidation: 900-1050°C in H₂O
- Drive-in diffusion: 1000-1150°C
- Anneal: 400-1100°C in N₂

**Kokusai Quixace Vertical Furnace**
- **Application**: High-throughput oxidation
- **Wafer Size**: 300mm, 150 wafer capacity
- **Features**: Automated loading, fast ramp

### Rapid Thermal Processing (RTP)

**Applied Materials Radiance RTP**
- **Application**: Spike anneal, oxidation, CVD
- **Wafer Size**: 200mm, 300mm
- **Temperature**: Up to 1250°C
- **Ramp Rate**: 50-150°C/sec
- **Uniformity**: <1.5% (1σ)
- **Lamp Configuration**: Array of tungsten-halogen
- **Price**: $800K-1.5M

**Processes**:
- Dopant activation: 1000-1050°C, 1-10 sec
- Gate oxide: 800-1000°C
- Silicidation: 400-850°C

**Mattson Technology Helios RTP**
- **Features**: Multi-zone heating
- **Temperature ramp**: Up to 400°C/sec
- **Process monitoring**: Pyrometry, reflectometry

---

## Ion Implantation

### Medium-Current Implanters

**Applied Materials Quantum X**
- **Application**: General purpose implantation
- **Species**: B, BF₂, P, As, In, Sb
- **Energy Range**: 1-200 keV
- **Current**: Up to 10 mA
- **Wafer Size**: 300mm
- **Throughput**: 200-400 wafers/hour
- **Price**: $2-4M

**Axcelis Purion H**
- **Features**: High current, high throughput
- **Energy**: 1-180 keV
- **Dose range**: 1×10¹¹ to 1×10¹⁶ cm⁻²
- **Angle**: 0-60° tilt

### High-Current Implanters

**Axcelis Purion XE**
- **Application**: High-dose implants (S/D, wells)
- **Current**: Up to 30 mA
- **Energy**: 1-80 keV
- **Throughput**: 350+ wafers/hour

### High-Energy Implanters

**Applied Materials Quantum XHE**
- **Application**: Deep well, retrograde doping
- **Energy**: 50 keV to 3 MeV
- **Species**: P, As, B, In
- **Typical Use**: Deep n-wells, isolated structures

---

## Chemical-Mechanical Polishing

### CMP Tools

**Applied Materials Reflexion LK**
- **Application**: Oxide, tungsten, Cu CMP
- **Wafer Size**: 300mm
- **Stations**: 4 polishing + 2 cleaning
- **Platen**: 20-30" diameter
- **Throughput**: 80-120 wafers/hour
- **Within-wafer uniformity**: <2%
- **Price**: $3-6M

**Consumables**:
- Oxide slurry: Silica particles, KOH
- Cu slurry: Alumina + oxidizer + inhibitor
- Pads: IC1000, SubaIV (different hardness)

**Ebara EPO-222**
- **Application**: Oxide, metal CMP
- **Wafer Size**: 200mm
- **Force control**: Pneumatic pressure
- **End-point detection**: Motor current

---

## Metrology & Inspection

### Critical Dimension (CD) Measurement

**Hitachi S-9380 CD-SEM**
- **Resolution**: <1nm
- **Application**: Gate CD, trench measurements
- **Wafer Size**: 300mm
- **Throughput**: 30-50 measurements/hour
- **Price**: $1.5-3M

**KLA Archer 600**
- **Technology**: Optical overlay and CD
- **Wavelength**: Multi-wavelength
- **Spot Size**: <20μm

### Film Thickness

**Filmetrics F40**
- **Technology**: Spectroscopic reflectometry
- **Thickness Range**: 10nm to 70μm
- **Films**: Oxides, nitrides, polymers, metals
- **Spot Size**: 2mm to 25μm
- **Price**: $30-80K

**KLA-Tencor SpectraFx**
- **Application**: Film thickness, optical properties
- **Wafer Size**: 300mm
- **Mapping**: Automated full-wafer scans

### Defect Inspection

**KLA-Tencor 2930**
- **Technology**: Brightfield optical inspection
- **Sensitivity**: 90nm defects
- **Wafer Size**: 300mm
- **Throughput**: 150 wafers/hour
- **Price**: $2-4M

**Applied Materials SEMVision G7**
- **Technology**: E-beam inspection
- **Resolution**: Sub-20nm defects
- **Application**: Advanced node defect review

### Profilometry

**KLA-Tencor P-17**
- **Technology**: Stylus profilometry
- **Vertical Resolution**: 1Å
- **Scan Length**: Up to 200mm
- **Application**: Step height, roughness
- **Price**: $80-150K

**Bruker DektakXT**
- **Vertical Range**: 2mm
- **Scan Speed**: Up to 3mm/sec
- **Application**: MEMS structures, thin films

### Ellipsometry

**J.A. Woollam M-2000**
- **Wavelength**: 210-1690nm
- **Measurement Time**: <1 second
- **Thickness Range**: 1nm to several μm
- **Application**: Gate oxide, high-κ films
- **Price**: $80-150K

---

## Wafer Handling

### Wafer Cleaning

**FSI Mercury HP**
- **Technology**: Megasonic cleaning
- **Chemistry**: SC-1, SC-2, HF, rinse
- **Wafer Size**: 200mm, 300mm
- **Throughput**: 100-200 wafers/hour
- **Particle removal**: >99% efficiency
- **Price**: $600K-1.2M

### Wafer Bonding

**EV Group EVG520**
- **Application**: Wafer-to-wafer bonding
- **Processes**: Fusion, anodic, adhesive
- **Wafer Size**: Up to 200mm
- **Alignment Accuracy**: <1μm
- **Pressure**: Up to 50 kN
- **Temperature**: Up to 500°C
- **Price**: $500K-1M

### Wafer Dicing

**Disco DAD3350**
- **Application**: Wafer singulation
- **Blade Type**: Resin-bond diamond
- **Cutting Speed**: 50-300 mm/sec
- **Wafer Size**: Up to 300mm
- **Street Width**: 40-100μm typical
- **Price**: $200-500K

---

## Cost Summary

### Typical Cleanroom Setup Costs

| Equipment Category | Budget Range | Critical? |
|--------------------|--------------|-----------|
| Lithography (Stepper) | $2M-90M | Yes |
| Deposition (CVD/PVD) | $2M-5M | Yes |
| Etch (RIE/ICP) | $500K-2M | Yes |
| Thermal (Furnace/RTP) | $500K-2M | Yes |
| Ion Implanter | $2M-4M | CMOS only |
| CMP | $3M-6M | Advanced nodes |
| Metrology Suite | $2M-8M | Yes |
| **Minimum R&D Lab** | **$8M-15M** | - |
| **Full 200mm Line** | **$50M-150M** | - |
| **Advanced 300mm Fab** | **$3B-15B** | - |

### Operating Costs

- **Cleanroom**: $300-1000/sq ft/year
- **Utilities**: $2-5M/year (200mm fab)
- **Consumables**: $500K-2M/year
- **Maintenance**: 10-15% of equipment cost/year
- **Personnel**: $50-150K/engineer/year

---

## Vendor Directory

### Major Equipment Manufacturers

- **ASML** - Lithography
- **Applied Materials** - Deposition, etch, implant, metrology
- **Lam Research** - Etch, deposition
- **Tokyo Electron (TEL)** - Deposition, etch, coat/develop
- **KLA** - Metrology, inspection
- **Axcelis** - Ion implantation
- **Hitachi** - Etch, metrology
- **Oxford Instruments** - Etch, deposition
- **SPTS (Orbotech)** - DRIE, PVD, ALD
- **Veeco** - ALD, lithography (Ultratech)

---

**Last Updated**: November 2025  
**Note**: Prices are approximate and vary based on configuration, support contracts, and market conditions.
