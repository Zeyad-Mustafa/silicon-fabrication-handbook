# Industry Standards in Semiconductor and MEMS Fabrication

**A practical reference to the standards that govern how silicon devices are designed, made, tested, and qualified.**

Every semiconductor or MEMS device that reaches production passes through a web of industry standards — specifications that define wafer dimensions, contamination limits, equipment interfaces, electrical tests, reliability requirements, and safety protocols. Understanding these standards is essential for anyone working in, or entering, the semiconductor industry.

This document organises the most relevant standards by domain: wafers, process equipment, lithography, electrical test, reliability, MEMS, and quality management. Each entry explains *what the standard covers*, *why it exists*, and *who uses it*.

---

## Table of Contents

1. [Standards Bodies Overview](#1-standards-bodies-overview)
2. [Wafer and Substrate Standards](#2-wafer-and-substrate-standards)
3. [Cleanroom and Environmental Standards](#3-cleanroom-and-environmental-standards)
4. [Process Equipment and Interface Standards](#4-process-equipment-and-interface-standards)
5. [Lithography Standards](#5-lithography-standards)
6. [Electrical Test and Parametric Standards](#6-electrical-test-and-parametric-standards)
7. [Reliability and Qualification Standards](#7-reliability-and-qualification-standards)
8. [MEMS-Specific Standards](#8-mems-specific-standards)
9. [Packaging and Assembly Standards](#9-packaging-and-assembly-standards)
10. [Quality Management Standards](#10-quality-management-standards)
11. [Safety and Environmental Standards](#11-safety-and-environmental-standards)
12. [Quick-Reference Tables](#12-quick-reference-tables)

---

## 1. Standards Bodies Overview

Several organisations develop and maintain the standards used in semiconductor manufacturing. Knowing who publishes a standard tells you how widely it is adopted and how often it is revised.

### SEMI (Semiconductor Equipment and Materials International)

SEMI is the primary standards body for the semiconductor equipment and materials industry. It publishes hundreds of standards covering everything from wafer geometry to chemical purity. SEMI standards are designated with a letter indicating their domain:

| Prefix | Domain |
|--------|--------|
| **M** | Silicon and other semiconductor materials |
| **E** | Equipment automation and communication |
| **C** | Chemicals and gases |
| **G** | Packaging |
| **T** | Traceability |
| **F** | Facilities |

SEMI standards are developed by volunteer task forces of industry engineers and revised on a regular ballot cycle. They are widely adopted worldwide but are not legally mandatory unless referenced by regulation.

### JEDEC (Joint Electron Device Engineering Council)

JEDEC publishes standards for semiconductor devices and packaging, with particular strength in memory devices, packaging dimensions, and qualification procedures. Its JEP (JEDEC Engineering Publication) series covers reliability test methods extensively.

### IEC (International Electrotechnical Commission)

IEC produces internationally harmonised electrical standards. In semiconductor contexts, IEC standards govern safety of equipment (IEC 61010), EMC, and environmental tests. IEC standards carry more formal regulatory weight in many jurisdictions than SEMI or JEDEC publications.

### ASTM International

ASTM (formerly American Society for Testing and Materials) provides test methods widely used for silicon material characterisation, including resistivity, oxygen content, and defect density measurements.

### ISO (International Organization for Standardization)

ISO standards most relevant to semiconductor manufacturing cover quality management systems (ISO 9001), cleanroom classification (ISO 14644), and environmental management (ISO 14001).

### ITRS / IRDS

The International Technology Roadmap for Semiconductors (ITRS), now succeeded by the International Roadmap for Devices and Systems (IRDS), is not a standards document but a collaborative roadmap. It defines technology targets — feature sizes, power, performance, cost — that drive what the standards must eventually accommodate.

---

## 2. Wafer and Substrate Standards

Wafer geometry and material specifications are the foundation of every process flow. If the wafer is out of specification, every subsequent step is compromised.

### SEMI M1 — Silicon Wafer Specification

**What it covers:** Dimensional, mechanical, and surface quality requirements for polished single-crystal silicon wafers used in device manufacturing.

**Key parameters defined:**
- **Diameter** — standardised at 100 mm, 150 mm, 200 mm, and 300 mm
- **Thickness** — nominal thickness and total thickness variation (TTV), typically ±25 µm for 300 mm wafers
- **Bow and warp** — deviation from a reference plane; 300 mm production wafers must achieve <100 µm bow
- **Site flatness (SFQR)** — flatness measured on individual exposure sites, must be <130 nm for 90 nm node lithography
- **Edge exclusion** — region around the wafer perimeter excluded from device area
- **Primary and secondary flats / notch** — orientation indicators for wafer handling and alignment

**Why it matters:** Lithography systems hold wafers on vacuum chucks and must guarantee focal plane uniformity. A wafer with excessive warp causes defocus across the die and yield loss. Equipment suppliers design wafer-handling robots to SEMI M1 dimensions.

### SEMI M6 — Polished Monocrystalline Silicon Wafer Specification (150 mm)

Companion to M1 specifically for 150 mm wafers, which remain in production for compound semiconductor, power, and MEMS applications.

### SEMI M49 — Guide for Measuring Warp and Bow of Silicon Wafers

Defines the measurement methodology for warp and bow so that results from different equipment are comparable. Without a common measurement protocol, two labs measuring the same wafer can report different numbers.

### SEMI M59 — Terminology for Silicon Technology

A controlled vocabulary document. Defines precisely what terms like "notch," "flat zone," "bulk," "epilayer," and "substrate" mean so that contracts and specifications are unambiguous.

### SEMI M78 — 450 mm Wafer Specification

Covers the next-generation 450 mm wafer size, development of which has been ongoing. Currently only relevant for R&D lines.

### ASTM F723 — Resistivity of Silicon

Specifies how to measure resistivity of silicon wafers using a four-point probe. Resistivity directly sets the background carrier concentration and is the primary way of characterising dopant level in as-grown crystals. Values range from ~0.001 Ω·cm (heavily doped) to >100 Ω·cm (lightly doped or intrinsic).

### ASTM F1239 — Oxygen Concentration in Silicon by FTIR

Interstitial oxygen in Czochralski-grown silicon affects mechanical strength, gettering behaviour, and thermal donor formation. This standard defines infrared absorption measurements at the 9.05 µm oxygen absorption peak, with calibration to a universally accepted conversion factor (currently the ASTM F-value = 4.81 × 10¹⁷ cm⁻²).

### SEMI M57 — SOI Wafer Specification

Silicon-on-insulator (SOI) wafers require additional parameters beyond bulk silicon specifications: buried oxide thickness, top silicon thickness uniformity, and defect density at the Si/BOX interface. SOI is used for fully depleted FD-SOI CMOS and for MEMS devices requiring a well-defined etch-stop layer.

---

## 3. Cleanroom and Environmental Standards

Contamination is the primary enemy of semiconductor yield. A single 100 nm particle on a wafer can kill a transistor. Standards define particle counts, chemical purity, and human behaviour inside the fabrication environment.

### ISO 14644-1 — Cleanroom Classification

**What it covers:** Defines cleanroom classes by airborne particle count. Replaced the older US Federal Standard 209E (which used classes like Class 100, Class 10) with a new ISO classification system.

**Classification scheme:**

| ISO Class | Max particles ≥ 0.5 µm per m³ | Equivalent FED-STD 209E |
|-----------|-------------------------------|-------------------------|
| ISO 1 | 10 | — |
| ISO 2 | 100 | — |
| ISO 3 | 1,000 | Class 1 |
| ISO 4 | 10,000 | Class 10 |
| ISO 5 | 100,000 | Class 100 |
| ISO 6 | 1,000,000 | Class 1,000 |
| ISO 7 | 10,000,000 | Class 10,000 |

**Why it matters:** Advanced lithography (sub-10 nm) requires ISO 1–3 environments at the exposure station. Wafer storage may be acceptable at ISO 5. The classification drives HVAC design, gowning protocols, and the cost of running the facility.

### ISO 14644-2 — Cleanroom Monitoring

Specifies how frequently cleanrooms must be re-tested and how monitoring systems (particle counters, airflow sensors) should be calibrated and positioned. A cleanroom that passes its annual certification but is not continuously monitored may be out of specification between tests.

### ISO 14644-5 — Cleanroom Operations

Covers the human factors: gowning procedures, movement speeds, behaviour protocols, and material introduction. People are the largest source of contamination in a cleanroom — each person sheds ~100,000 particles per minute during normal activity, reduced to ~10,000 when gowned correctly.

### SEMI S2 — Safety Guidelines for Semiconductor Equipment

**What it covers:** A comprehensive safety specification that equipment suppliers must satisfy for their tools to be acceptable on a semiconductor fab floor. Covers electrical safety, chemical hazards, fire suppression, ergonomics, and emergency shutoff design.

**Why it matters:** Every major equipment purchase in a semiconductor fab is evaluated for SEMI S2 compliance. Tools that do not comply cannot be installed. Insurance and regulatory audits reference SEMI S2 extensively.

### SEMI S8 — Safety Guidelines for Ergonomics

Supplements S2 with detailed ergonomic requirements for equipment design — accessible maintenance points, safe lift weights, and viewing windows at appropriate heights. Repetitive-strain injuries from poorly designed maintenance access are an occupational health cost that S8 seeks to reduce.

### SEMI C1 — Standard for Reagent Chemicals

Defines purity grades for chemicals used in semiconductor processing (acids, solvents, developers). Semiconductor-grade chemicals must meet far higher purity specifications than laboratory-grade materials. A trace ppb-level metal contamination in HF etch solution can introduce deep-level traps in silicon that degrade minority carrier lifetime.

### SEMI C7.1 — Guide for Ultrapure Water

Ultrapure water (UPW) used in wafer cleaning and CMP must meet extremely stringent specifications: resistivity >18 MΩ·cm, total organic carbon <1 ppb, particle counts <100 per litre at ≥0.05 µm, and bacteria <1 CFU/100 mL. SEMI C7.1 provides a framework for UPW system qualification and ongoing monitoring.

---

## 4. Process Equipment and Interface Standards

Modern fabs run dozens of different tools from multiple vendors. Standards for how those tools communicate, handle wafers, and report data are what make automated 300 mm fabs possible.

### SEMI E5 — SECS-II Communication Standard

**What it covers:** The message format and data item definitions for communication between semiconductor equipment and factory host systems.

**Why it matters:** SECS-II (SEMI Equipment Communication Standard) is the foundation of fab automation. Equipment sends events (process completed, alarm triggered) and receives commands (run recipe, load wafer) using SECS-II messages. Without it, each vendor would need custom integration software.

### SEMI E30 — GEM (Generic Equipment Model)

Defines the behavioural model that compliant equipment must implement — what states it can be in (online, offline, remote), what events it must report, and what commands it must accept. GEM specifies the *behaviour*; SECS-II specifies the *message format*. Together they allow a factory information system to integrate any compliant tool.

### SEMI E37 — HSMS (High-Speed Message Services)

An evolution of the original SECS-I serial interface, HSMS runs the same SECS-II message protocol over TCP/IP networks rather than serial cables. All modern fab tools use HSMS.

### SEMI E40 — Standard for Processing Management

Defines how equipment manages process jobs, control jobs, and recipes. Standardises how a fab MES (Manufacturing Execution System) instructs equipment to process a lot, monitor it, and report results.

### SEMI E84 — Enhanced Parallel I/O Interface for Interbay/Intrabay Automated Material Handling

Specifies the electrical and logical interface between material-handling robots (overhead transport, track systems) and equipment load ports. Without E84, a robot from vendor A cannot reliably hand off a carrier to a tool from vendor B.

### SEMI E47.1 — Mechanical Specification for FOUP

The **Front Opening Unified Pod (FOUP)** is the sealed carrier that holds 300 mm wafers during transport between tools. SEMI E47.1 defines its dimensions, latching mechanism, door interface, and material requirements (particle generation, outgassing). Every 300 mm fab in the world uses FOUPs conforming to this specification.

### SEMI E57 — Mechanical Specification for 200 mm FOSBs

The **Front Opening Shipping Box (FOSB)** is used for 200 mm wafer transport. Both FOUP and FOSB specifications are necessary to allow universal robot and equipment compatibility.

### SEMI E10 — Equipment Reliability, Availability, Maintainability (RAM)

Defines how to measure and report OEE (Overall Equipment Effectiveness), uptime, mean time between failures (MTBF), and mean time to repair (MTTR) for semiconductor equipment. Provides common definitions so that fab engineers can compare tools from different vendors on equal terms. A 300 mm lithography scanner costs >$100 M; knowing its real availability is financially critical.

### SEMI E158 — Interface Standard for 450 mm Equipment

Defines the load port, carrier, and material-handling interfaces for the next-generation 450 mm wafer size, analogous to E47.1 and E84 for 300 mm.

---

## 5. Lithography Standards

Lithography is the patterning step that defines feature sizes and drives the technology node. Its standards cover both the equipment interface and the mask (reticle) specifications.

### SEMI P1 — Specification for Hard Surface Photomasks

Defines the mechanical, dimensional, and defect requirements for chrome-on-glass photomasks used in optical lithography. Specifies plate size (most commonly 6 inch × 6 inch × 0.25 inch for 4× reduction steppers), flatness, and chrome film uniformity.

### SEMI P37 — Specification for Reticle Carriers

Defines the carrier used to transport reticles (the 4× or 5× reduction mask used in steppers and scanners) between the mask shop, inspection tools, and exposure tools. Standardised carriers allow automated reticle handling in mask libraries.

### SEMI P40 — Standard for Mask Defect Terminology

Establishes agreed-upon vocabulary for mask defects (pinholes, chrome spots, phase errors) to allow unambiguous communication between mask fabs, inspection vendors, and device manufacturers.

### SEMI P44 — Specification for 193 nm Immersion Reticles

Addresses the additional requirements for reticles used in immersion lithography (which uses water between lens and wafer to extend resolution). Covers pellicle-related contamination, hydrophobicity requirements, and defect printability criteria at 193 nm.

### ITRS Lithography Roadmap (now IRDS)

Not a formal standard but an industry consensus document that maps out required feature sizes, overlay tolerances, and resolution enhancements (multiple patterning, EUV) by year. Equipment suppliers, resist manufacturers, and device designers all use the IRDS roadmap as a coordinating document.

---

## 6. Electrical Test and Parametric Standards

Electrical test ensures that devices meet their specifications. Standards define test methods, parameter definitions, and data formats so that results are comparable and traceable.

### SEMI M30 — Test Patterns for Sheet Resistance Measurement

Defines standardised test structures (van der Pauw, bridge resistor, Kelvin contact) to be included on wafers for measuring sheet resistance of doped layers, implants, and deposited films. Enables across-wafer uniformity monitoring and process control.

### SEMI M35 — Guide for Determining Carrier Lifetime in Silicon

Specifies measurement methods for minority carrier lifetime — a critical indicator of silicon material quality and process cleanliness. Long lifetime (>1 ms) correlates with low recombination center density and is essential for bipolar and solar cell applications.

### SEMI MF1048 — Test Method for Measuring the Diameter of Silicon Wafers

Traceable dimensional measurement of wafer diameter using a scanning edge sensor. Necessary for verifying incoming wafer lot conformance.

### JEDEC JESD22 — Reliability Test Methods

**What it covers:** A large family of individual test methods (JESD22-Axxx, JESD22-Bxxx) covering environmental stress screening, burn-in, ESD, latch-up, and failure analysis. This is arguably the most widely cited qualification framework in the industry.

**Key individual standards:**

| Test | Standard | What It Measures |
|------|----------|-----------------|
| High Temperature Operating Life (HTOL) | JESD22-A108 | Time-dependent dielectric breakdown, hot carrier injection at elevated temperature |
| Temperature Cycling | JESD22-A104 | Solder joint and package fatigue under thermal cycling |
| Moisture/Reflow Sensitivity | J-STD-020 | Package cracking during solder reflow ("popcorn effect") |
| ESD (Human Body Model) | JESD22-A114 | Device damage from human body electrostatic discharge |
| ESD (Charged Device Model) | JESD22-C101 | Device damage from charged device discharge at pick-and-place |
| Latch-up | JESD22-A108 | Parasitic PNPN triggering in CMOS |
| Electromigration | JESD22-A109 | Metal line failure under high current density |

### JEDEC JESD47 — Stress-Test-Driven Qualification of Integrated Circuits

The master qualification flow document. Specifies which tests from JESD22 must be run, in what sequence, with what sample sizes, and what acceptance criteria apply for a new IC to be released for production. A product is "JEDEC-qualified" when it passes the matrix defined in JESD47.

### IEC 60747 — Discrete Semiconductor Devices and ICs

The IEC international standard for characterising discrete devices (diodes, transistors). Defines how parameters like breakdown voltage, leakage current, and capacitance are measured and reported. Referenced in product datasheets and purchasing specifications worldwide.

### SEMI M11 — Test Method for Measuring Resistivity of Silicon Slices Using a Collinear Four-Point Probe

Four-point probe measurement is the standard incoming QC check for silicon wafer resistivity. M11 specifies probe geometry (tip spacing, tip radius, tip force), correction factors for sample geometry, and measurement uncertainty. Resistivity maps from incoming wafer inspection use this method.

---

## 7. Reliability and Qualification Standards

Reliability standards ensure that devices will function over their intended lifetime under real-world conditions. Semiconductor devices must survive years of operation in environments ranging from consumer electronics (5-10 years, room temperature) to automotive powertrain (15+ years, 150°C junction temperature).

### AEC-Q100 — Failure Mechanism Based Stress Test Qualification for Integrated Circuits

**What it covers:** The automotive electronics qualification standard for integrated circuits. Defines a comprehensive stress test matrix that ICs must pass before they can be used in automotive applications.

**Why it matters:** Automotive applications demand much higher reliability than consumer electronics — a failure in a car's braking system has catastrophic consequences. AEC-Q100 specifies:
- High Temperature Operating Life (HTOL): 1,000 hours at 125°C or 150°C
- Temperature Cycling: -55°C to +150°C, 1,000 cycles
- Highly Accelerated Stress Test (HAST): 96 hours at 130°C, 85% RH
- ESD and latch-up to automotive voltage levels (±4 kV HBM)

Qualification data must be submitted to the PPAP (Production Part Approval Process) for automotive customers.

### AEC-Q101 — Failure Mechanism Based Stress Test Qualification for Discrete Semiconductors

The automotive equivalent of Q100 for discrete devices (diodes, transistors, thyristors). Follows the same philosophy but with test conditions appropriate for discrete components.

### AEC-Q200 — Stress Test Qualification for Passive Components

Covers resistors, capacitors, inductors, and other passive components used in automotive electronics. Relevant to MEMS packages which often include passive components.

### JEDEC JEP122 — Failure Mechanisms and Models for Semiconductor Devices

Not a test specification but a reference guide explaining the physics behind the failure modes that qualification tests probe. Covers electromigration, TDDB (time-dependent dielectric breakdown), hot carrier injection, NBTI (negative bias temperature instability), and stress migration. Understanding this document is essential for interpreting qualification test results.

### JEDEC JESD91 — Method for Developing Acceleration Models for Electronic Component Reliability

Provides statistical methods for extrapolating from accelerated test conditions (high temperature, high voltage) to use conditions. The Arrhenius model, Black's equation for electromigration, and Eyring models are all covered. This underpins the calculation of "10-year MTTF at 85°C" from a HTOL test run at 150°C.

### MIL-STD-883 — Test Methods for Microelectronics (Military)

The US military standard for semiconductor device testing. More stringent than commercial qualifications — higher temperature ranges, more thermal cycles, longer burn-in times. Used for aerospace, defence, and space applications. MIL-PRF-38535 is the companion qualification specification for integrated circuits.

### IEC 60068 — Environmental Testing

A broad IEC series covering standard environmental stress tests (temperature shock, vibration, humidity, salt fog, UV exposure). Referenced by automotive and industrial qualification flows. IEC 60068-2-14 covers thermal shock; IEC 60068-2-78 covers damp heat.

---

## 8. MEMS-Specific Standards

MEMS (Micro-Electro-Mechanical Systems) devices present unique challenges: they have moving parts, they interact with their environment (pressure, acceleration, light), and their failure modes differ substantially from purely electronic devices. Standards development for MEMS has lagged behind CMOS, but a core set of documents now exists.

### SEMI MS1 — Terminology for MEMS Technology

Establishes controlled vocabulary for MEMS fabrication and device description — essential because MEMS technology spans multiple disciplines (mechanical engineering, chemistry, electrical engineering) that previously used different terms for the same concepts.

### SEMI MS2 — Test Methods for MEMS Structural Film Properties

Defines mechanical property measurement methods for thin films used in MEMS structures:
- **Young's modulus** measurement via beam resonance or nanoindentation
- **Residual stress** measurement via substrate curvature (Stoney equation)
- **Fracture strength** via ring-on-ring or tensile tests
- **Fatigue behaviour** under cyclic loading

These properties determine resonant frequency, pull-in voltage, and long-term stability. Without standardised measurement, results from different labs cannot be compared.

### SEMI MS3 — Test Methods for MEMS Fabrication

Covers process-level characterisation for MEMS:
- Etch rate and selectivity measurements
- Sidewall angle characterisation
- Surface roughness measurement
- Release etch uniformity

### ASTM E2546 — Standard Practice for Instrumented Indentation Testing

Nanoindentation is the primary method for measuring Young's modulus and hardness of thin films and MEMS structural layers (polysilicon, silicon nitride, SiO₂). ASTM E2546 standardises the Oliver-Pharr analysis method used to extract modulus and hardness from load-displacement curves.

### IEEE 1451 — Smart Transducer Interface Standard

**What it covers:** Defines a standard interface between a smart transducer (MEMS sensor or actuator with onboard electronics) and a network or controller. The Transducer Electronic Data Sheet (TEDS) embedded in each device contains calibration and identification data.

**Why it matters:** Enables plug-and-play sensor systems where calibration data travels with the sensor rather than being managed separately. Used in industrial automation, aerospace, and emerging IoT sensor networks.

### IEC 62047 — Semiconductor Devices — MEMS

A series of IEC standards specifically for MEMS covering:
- **IEC 62047-1**: Vocabulary
- **IEC 62047-2**: Test methods for thin film materials
- **IEC 62047-6**: Resonant MEMS — measurement of resonant frequency and Q-factor
- **IEC 62047-8**: Measurement of fracture strength

These standards harmonise with SEMI MS documents and are referenced by automotive and medical device qualification flows that require IEC rather than SEMI standards.

### JEDEC JESD22-B117 — Solder Ball Shear

For MEMS devices in BGA packages, solder ball shear testing verifies solder joint integrity. Mechanical shock and vibration during shipping and use can fatigue solder joints, and MEMS devices with moving parts transmit forces differently than purely electronic ICs.

### ISO 13485 — Medical Devices Quality Management System

Medical MEMS devices (pressure sensors in catheters, accelerometers in hearing aids, lab-on-chip diagnostics) must comply with ISO 13485, which requires documented design controls, risk management (ISO 14971), and clinical evidence. The quality management requirements are more stringent than ISO 9001.

---

## 9. Packaging and Assembly Standards

After wafer fabrication, devices are diced, assembled into packages, and tested. Packaging standards govern materials, dimensions, assembly processes, and test requirements.

### JEDEC JESD22-B106 — Resistance to Soldering Temperature for Through-Hole Mounted Devices

Verifies that through-hole packages can withstand wave solder temperatures without delamination or failure.

### JEDEC J-STD-020 — Moisture/Reflow Sensitivity Classification for Non-Hermetic SMD Packages

**What it covers:** IC packages absorb moisture during storage. When reflowed over solder paste, the moisture rapidly vaporises and can crack the package — the "popcorn effect." J-STD-020 defines moisture sensitivity levels (MSL 1 through 6) and the baking and handling requirements for each level.

**Moisture Sensitivity Levels:**

| MSL | Floor Life at 30°C / 60% RH |
|-----|----------------------------|
| 1 | Unlimited |
| 2 | 1 year |
| 2a | 4 weeks |
| 3 | 168 hours |
| 4 | 72 hours |
| 5 | 48 hours |
| 5a | 24 hours |
| 6 | Must be baked and used within 6 hours |

**Why it matters:** Board assembly operations must track MSL for every component. Using an MSL-3 device that has been left on the bench for a week without baking it first can cause immediate field failures after reflow.

### IPC-A-610 — Acceptability of Electronic Assemblies

The dominant standard for PCB assembly quality. Defines three classes:
- **Class 1**: General electronics, lowest reliability requirements
- **Class 2**: Dedicated service electronics (most consumer and industrial)
- **Class 3**: High performance / harsh environment (aerospace, medical, military)

Inspection criteria cover solder joint geometry, component placement, cleanliness, and workmanship defects. Referenced in contracts between OEMs and contract manufacturers worldwide.

### SEMI G80 — Specification for Chip-on-Board (COB) Wire Bonding

Covers the mechanical and quality requirements for bare die wire bonding directly to PCBs or substrates — common in MEMS sensor modules and automotive ICs where package height is a constraint.

### MIL-STD-883 Method 2019 — Die Shear Strength

A standard test for the adhesion of die to substrate (die attach). The die attach material (epoxy, solder, eutectic alloy) must withstand mechanical stress during handling and thermal cycling. Failure of die attach can cause electrical opens or device drift in precision MEMS sensors.

---

## 10. Quality Management Standards

Quality management standards define how organisations build and document the systems that ensure consistent, defect-free production.

### ISO 9001 — Quality Management Systems

**What it covers:** The foundational QMS standard, applicable to any industry. Requires documented processes for design control, supplier management, corrective action, management review, and internal audit.

**Why it matters:** ISO 9001 certification is effectively a minimum entry requirement for semiconductor suppliers. Without it, major customers will not consider sourcing from you. The standard is maintained by the manufacturer's own auditors plus periodic third-party certification audits.

### IATF 16949 — Quality Management System for Automotive Production

The automotive-specific extension of ISO 9001. Required by all major OEMs (GM, Ford, Stellantis, Toyota, BMW, VW) for Tier 1 and Tier 2 suppliers. Adds requirements for:
- Advanced Product Quality Planning (APQP)
- Failure Mode and Effects Analysis (FMEA)
- Statistical Process Control (SPC)
- Production Part Approval Process (PPAP)
- Control Plan requirements

Semiconductor fabs supplying automotive IC customers must be IATF 16949 certified.

### AS9100 — Quality Management System for Aviation, Space, and Defense

The aerospace equivalent of IATF 16949. Adds configuration management, risk management, and first-article inspection requirements beyond ISO 9001. Required for suppliers to Boeing, Airbus, Lockheed Martin, and defence contractors.

### SEMI E10 / SEMI E79 — Equipment Performance Metrics

Provides standardised definitions and calculation methods for OEE (Overall Equipment Effectiveness), availability, utilisation, and capability metrics. Consistent metrics allow a fab to benchmark its equipment performance against industry norms and track improvement over time.

### Six Sigma and SPC in Semiconductor Manufacturing

While not a formal standard, Six Sigma methodology and Statistical Process Control are universally expected. Key control chart types used in semiconductor fabs:

| Chart Type | Application |
|------------|-------------|
| X-bar / R chart | Continuous variables (film thickness, CD uniformity) |
| p-chart | Fraction defective (particle adder rate, yield per lot) |
| c-chart | Count of defects per unit (particles on wafer surface) |
| CUSUM chart | Detecting small mean shifts (process drift) |
| EWMA chart | Adaptive run-to-run process control |

Control limits are typically set at ±3σ. Process capability index Cpk > 1.33 is a common minimum requirement; automotive applications often require Cpk > 1.67.

---

## 11. Safety and Environmental Standards

Semiconductor fabrication involves hazardous chemicals, high-voltage equipment, and high-power radiation sources. Safety and environmental standards are both legally required and ethically essential.

### SEMI S2 (revisited) — Safety Guidelines for Semiconductor Manufacturing Equipment

The most comprehensive safety standard for fab equipment. Sections cover:
- **Electrical safety**: Interlocks, grounding, arc flash protection
- **Chemical safety**: Secondary containment, exhaust design, material compatibility
- **Radiation safety**: UV, RF, laser, and X-ray hazard controls
- **Fire**: Sprinkler requirements, material flammability ratings
- **Ergonomics**: Maintenance access, weight limits, visual indicators

### SEMI S6 — Environmental, Health and Safety Guideline for the Exhaust Ventilation of Semiconductor Manufacturing Equipment

Defines minimum exhaust rates and abatement requirements for process equipment. All process gases (silane, chlorine, HF, TEOS, etc.) must be routed through appropriate exhaust systems and abatement before release to atmosphere.

### SEMI S23 — Guide for Conservation of Energy, Utilities, and Materials Used by Semiconductor Manufacturing Equipment

Addresses sustainability in equipment design — minimising chemical consumption, reducing standby energy use, and recovering or recycling process materials. Increasingly important as fab utility costs and environmental reporting requirements grow.

### IEC 62133 — Safety Requirements for Portable Sealed Secondary Lithium Cells

Relevant for MEMS-based consumer products (wearables, IoT sensors) that include lithium batteries. Covers overcharge, overdischarge, short circuit, and vibration tests.

### RoHS (Directive 2011/65/EU) and REACH

**RoHS (Restriction of Hazardous Substances)**: Restricts lead, mercury, cadmium, hexavalent chromium, PBB, and PBDE in electronic equipment sold in the EU. Affects solder alloys, package materials, and certain process chemicals.

**REACH (Registration, Evaluation, Authorisation and Restriction of Chemicals)**: EU chemical regulation requiring manufacturers to register hazardous chemical substances and demonstrate safe use. Impacts semiconductor fabs operating in or supplying to Europe.

### OSHA 29 CFR 1910 (US) / IEC 60079 (International)

Occupational safety regulations for chemical handling, electrical safety, and confined space entry. US fabs must comply with OSHA regulations; international equivalents apply in other jurisdictions.

---

## 12. Quick-Reference Tables

### 12.1 Standards by Application Domain

| Domain | Key Standards |
|--------|--------------|
| Wafer geometry and material | SEMI M1, M6, M57, ASTM F723, F1239 |
| Cleanroom environment | ISO 14644-1/-2/-5, SEMI S2 |
| Equipment automation | SEMI E5, E30, E37, E40, E84 |
| Wafer transport (300 mm) | SEMI E47.1 |
| Process qualification (CMOS) | JEDEC JESD47, JESD22 series |
| Automotive qualification | AEC-Q100, AEC-Q101, IATF 16949 |
| MEMS materials | SEMI MS1, MS2, MS3, IEC 62047 |
| MEMS sensors (interface) | IEEE 1451 |
| Packaging moisture sensitivity | JEDEC J-STD-020 |
| PCB assembly quality | IPC-A-610 |
| Quality management | ISO 9001, IATF 16949, AS9100 |
| Environmental/safety | SEMI S2, S6, RoHS, REACH |

### 12.2 Wafer Size and Key Specifications

| Diameter | Generation | Key Standard | TTV Spec | SFQR Spec |
|----------|-----------|--------------|---------|----------|
| 100 mm | 1970s–80s | SEMI M1 | <5 µm | N/A |
| 150 mm | 1980s–90s | SEMI M6 | <5 µm | N/A |
| 200 mm | 1990s–2000s | SEMI M1 | <3 µm | <130 nm |
| 300 mm | 2000s–present | SEMI M1 | <1 µm | <65 nm (28 nm node) |
| 450 mm | Future | SEMI M78 | TBD | TBD |

### 12.3 JEDEC Reliability Test Quick Reference

| Stress | Test ID | Condition | Duration |
|--------|---------|-----------|----------|
| High temperature operating life | JESD22-A108 | 125°C or 150°C, rated voltage | 1,000 h |
| Temperature cycling | JESD22-A104 | -55°C to +125°C | 1,000 cycles |
| HAST (accelerated humidity) | JESD22-A110 | 130°C, 85% RH | 96 h |
| ESD (HBM) | JESD22-A114 | ±2 kV, ±4 kV (automotive) | — |
| ESD (CDM) | JESD22-C101 | ±500 V | — |
| Latch-up | JESD22-A108 | T_amb = 125°C | — |
| Electromigration | JESD22-A109 | High current density, 200°C | Time to fail |
| Die shear | MIL-STD-883/2019 | Shear force applied to die | Pass/fail |

### 12.4 Cleanroom Classification Comparison

| ISO Class | Particles ≥ 0.1 µm /m³ | Particles ≥ 0.5 µm /m³ | Typical Application |
|-----------|-------------------------|------------------------|---------------------|
| ISO 1 | 10 | — | EUV exposure station |
| ISO 2 | 100 | — | Advanced litho tooling |
| ISO 3 | 1,000 | — | 193i scanner environments |
| ISO 4 | 10,000 | — | Deposition, etch |
| ISO 5 | 100,000 | 3,520 | General fab processing |
| ISO 6 | 1,000,000 | 35,200 | Wafer storage, prep |

### 12.5 Technology Node vs. Overlay and Defect Requirements

| Node | Gate CD (approx.) | Overlay Budget | Killer Defect Size | Lithography |
|------|------------------|----------------|-------------------|-------------|
| 180 nm | 180 nm | ±60 nm | >90 nm | KrF 248 nm |
| 90 nm | 90 nm | ±30 nm | >45 nm | ArF 193 nm (dry) |
| 45 nm | 45 nm | ±15 nm | >22 nm | 193 nm immersion |
| 22 nm | 22 nm | ±8 nm | >11 nm | 193i + double patterning |
| 7 nm | 7 nm | ±3 nm | >3.5 nm | EUV 13.5 nm |
| 3 nm | 3 nm | ±1.5 nm | >1.5 nm | EUV + high-NA |

---

## Further Reading

- **SEMI Standards**: [www.semi.org/standards](https://www.semi.org/en/products-services/standards)
- **JEDEC Standards**: [www.jedec.org/standards-documents](https://www.jedec.org/standards-documents)
- **IPC Standards**: [www.ipc.org/standards](https://www.ipc.org)
- **ISO 14644**: [www.iso.org/standard/53394.html](https://www.iso.org/standard/53394.html)
- **AEC Standards**: [www.aecouncil.com](http://www.aecouncil.com)
- *The International Technology Roadmap for Semiconductors (ITRS)* — archived at [www.itrs2.net](http://www.itrs2.net)
- *IRDS (successor to ITRS)* — [irds.ieee.org](https://irds.ieee.org)
- Wolf & Tauber, *Silicon Processing for the VLSI Era* — comprehensive process reference
- Madou, *Fundamentals of Microfabrication* — covers MEMS-specific standards context

---

*Part of the Silicon Fabrication Handbook — [github.com/Zeyad-Mustafa/silicon-fabrication-handbook](https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook)*  
*Last updated: February 2026*