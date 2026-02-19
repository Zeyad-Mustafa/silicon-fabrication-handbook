# Foundry Comparison for Semiconductor Manufacturing

**A practical guide to selecting the right foundry partner for your silicon fabrication project — from leading-edge logic to specialty MEMS.**

Choosing a foundry is one of the most consequential decisions in bringing a semiconductor device to market. The foundry determines not just whether your design can be manufactured, but at what cost, with what yield, at what volume, and with what degree of support. A fabless design house might have a brilliant chip architecture, but if the foundry cannot deliver it at the target price point and volume, the product fails.

This document surveys the global foundry landscape: the technology offerings, business models, minimum order quantities, NRE (non-recurring engineering) costs, typical lead times, and strategic trade-offs involved in foundry selection. It covers both the advanced-node pure-play foundries (TSMC, Samsung, Intel Foundry Services) that compete for leading-edge logic, and the mature-node and specialty foundries (GlobalFoundries, UMC, Tower, X-FAB, SkyWater) that serve analog, power, MEMS, and automotive markets.

All information reflects the state of the industry as of early 2026. Foundry pricing and capacity allocations change quarterly; treat all figures as representative rather than contractual.

---

## Table of Contents

1. [Foundry Business Models](#1-foundry-business-models)
2. [Leading-Edge Logic Foundries (≤7 nm)](#2-leading-edge-logic-foundries-7-nm)
3. [Mature-Node Foundries (≥28 nm)](#3-mature-node-foundries-28-nm)
4. [Specialty Foundries — Analog, RF, Power](#4-specialty-foundries--analog-rf-power)
5. [MEMS and Sensor Foundries](#5-mems-and-sensor-foundries)
6. [Compound Semiconductor Foundries (GaAs, GaN, SiC)](#6-compound-semiconductor-foundries-gaas-gan-sic)
7. [Packaging and Heterogeneous Integration](#7-packaging-and-heterogeneous-integration)
8. [Academic and Research Foundries](#8-academic-and-research-foundries)
9. [Selection Criteria and Trade-offs](#9-selection-criteria-and-trade-offs)
10. [Cost Structure and Economics](#10-cost-structure-and-economics)
11. [Quick-Reference Foundry Tables](#11-quick-reference-foundry-tables)

---

## 1. Foundry Business Models

### Pure-Play Foundry

A pure-play foundry manufactures ICs exclusively for third-party customers — it designs no chips of its own. This eliminates the conflict of interest that arises when a foundry competes with its own customers. TSMC invented the pure-play model in 1987 and remains its most successful practitioner.

**Advantages:**
- No design IP competition with customers
- Technology development roadmap aligned with customer needs
- Predictable pricing and capacity allocation
- Mature design ecosystems (PDKs, design rules, IP libraries)

**Examples:** TSMC, GlobalFoundries, UMC, Tower Semiconductor, X-FAB

---

### IDM with Foundry Services

An integrated device manufacturer (IDM) that also offers foundry services manufactures both its own products and those of external customers. The foundry division competes for wafer capacity with the company's internal product groups.

**Advantages:**
- May offer unique process technology (e.g., Intel's 18A with backside power)
- Often lower cost for captive-design compatibility (e.g., using same libraries as IDM products)

**Disadvantages:**
- Potential capacity conflict during high internal demand
- Customer concerns about IP security and competitive information
- Less predictable pricing and lead times
- Smaller third-party ecosystem

**Examples:** Intel Foundry Services (IFS), Samsung Foundry, TowerJazz (acquired by Intel), ON Semiconductor foundry services

---

### University and Research Foundries

Provide subsidised or cost-recovery fabrication for academic research, prototyping, and workforce training. Not suitable for volume production but essential for research community access to state-of-the-art processes.

**Examples:** SkyWater (open-source 130 nm via Google/CHIPS Act), IMEC (process R&D testbeds), MIT Lincoln Labs (GaN), SUNY Polytechnic Institute (300 mm CMOS testbed)

---

## 2. Leading-Edge Logic Foundries (≤7 nm)

Leading-edge nodes — currently defined as 7 nm, 5 nm, 3 nm, and future 2 nm and below — are characterised by FinFET or gate-all-around (GAA) transistor structures, EUV lithography, and extremely tight design rules. Only three companies currently offer these nodes at volume: TSMC, Samsung, and Intel (via IFS).

### TSMC (Taiwan Semiconductor Manufacturing Company)

**Headquarters:** Hsinchu, Taiwan  
**Founded:** 1987  
**Revenue (2025):** ~$90 billion USD  
**Market share (advanced logic):** ~60%

#### Technology Nodes Offered

| Node | Transistor Type | Lithography | Metal Layers | Typical Applications | Volume Production |
|------|----------------|-------------|--------------|---------------------|------------------|
| N3E / N3P / N3X | FinFET (enhanced) | EUV | 15–20 | Smartphone SoC, AI inference | 2023–present |
| N4 / N4P / N4X | FinFET | EUV | 15–18 | Mid-range mobile, automotive | 2023–present |
| N5 / N5P | FinFET | EUV | 15–17 | High-end mobile, HPC | 2020–present |
| N6 | FinFET | EUV | 13–15 | Cost-optimised mobile | 2020–present |
| N7 / N7+ | FinFET | DUV / EUV | 12–16 | Mainstream logic, GPU | 2018–present |
| N12 / N16 | FinFET | DUV | 10–13 | IoT, mid-tier mobile | 2015–present |

**N2 (2 nm class):** Gate-all-around (GAA) nanosheet transistors. Volume production planned for 2025–2026. First customer tape-outs in 2024. Represents the most significant transistor architecture change since FinFET introduction in 2011.

#### Business Terms (Representative)

| Metric | Value | Notes |
|--------|-------|-------|
| Minimum order (N3/N5) | 1,000–3,000 wafers | Per quarter, negotiable for strategic customers |
| NRE (N3/N5 new design) | $30–80 M | Includes mask set (~$15 M for N3), IP license, design verification |
| Wafer cost (N5, 300 mm) | $16,000–18,000 | Volume pricing; spot pricing higher |
| Wafer cost (N3) | $18,000–20,000 | — |
| Lead time (first silicon) | 12–16 weeks | From tape-out; assumes allocated capacity |
| Lead time (volume ramp) | 6–12 months | From first silicon to 10k wpm |
| Yield (N5, mature product) | 80–95% | Electrical yield; heavily design-dependent |

**Why TSMC leads:** Relentless execution on Moore's Law roadmap, unmatched capital investment (~$40 B/year), deepest ecosystem of EDA tool support and IP vendors, and track record of on-time delivery. Apple's A-series and M-series chips, NVIDIA's GPUs, AMD's Ryzen and EPYC processors, and Qualcomm's Snapdragon SoCs all use TSMC.

**Customer support model:** Dedicated Design Technology Co-Optimization (DTCO) teams work with lead customers on yield ramp. TSMC Open Innovation Platform (OIP) pre-qualifies IP cores and design flows for each node. Design rule manuals (DRM) are comprehensive (~5,000 pages for N5) but require deep expertise to navigate.

---

### Samsung Foundry

**Headquarters:** Hwaseong and Pyeongtaek, South Korea  
**Founded (foundry division):** 2017 (spun out from Samsung Electronics)  
**Revenue (foundry):** ~$8 billion USD (2025 est.)  
**Market share (advanced logic):** ~15%

#### Technology Nodes Offered

| Node | Transistor Type | Lithography | Typical Applications | Volume Production |
|------|----------------|-------------|---------------------|------------------|
| SF3 (3 nm) | GAA (MBCFET™) | EUV | Flagship mobile, HPC | 2024–present |
| SF4 / SF4P / SF4X (4 nm) | FinFET | EUV | Mobile, networking | 2022–present |
| SF5 / SF5LPE (5 nm) | FinFET | EUV | Mobile SoC, crypto ASIC | 2021–present |
| 7LPP / 7LPE (7 nm+) | FinFET | EUV | GPU, automotive compute | 2019–present |
| 8LPP (8 nm) | FinFET | DUV | Mid-range mobile | 2019–present |

**SF2 (2 nm):** Second-generation GAA, planned 2026–2027.

**Why Samsung competes:** Samsung was first to introduce GAA transistors (SF3, 2024), beating TSMC's N2 by 12–18 months. Samsung offers aggressive pricing to win market share — typically 10–15% below TSMC for equivalent nodes. Vertical integration (Samsung manufactures its own smartphones, memory, displays) provides internal test vehicle for new processes.

**Customer concerns:** Yield learning curve has historically lagged TSMC by 6–12 months. Qualcomm returned Snapdragon flagship production from Samsung 4LPE back to TSMC N4 in 2023 due to yield and power issues. However, Samsung SF3 (3 nm GAA) appears more competitive — securing Qualcomm's Snapdragon 8 Gen 4 and Samsung's own Exynos flagship.

#### Business Terms

| Metric | Value | Notes |
|--------|-------|-------|
| Minimum order (SF3/SF5) | 500–2,000 wafers | More flexible than TSMC for new customers |
| NRE (SF3/SF5) | $25–70 M | Lower than TSMC; includes aggressive discounts for strategic designs |
| Wafer cost (SF5) | $15,000–16,500 | ~10% below TSMC N5 |
| Wafer cost (SF3) | $17,000–19,000 | — |
| Lead time (first silicon) | 12–16 weeks | — |
| Yield (SF5, mature) | 70–85% | Improving but still trails TSMC |

---

### Intel Foundry Services (IFS)

**Headquarters:** Santa Clara, California, USA  
**Founded (foundry division):** 2021  
**Revenue (foundry):** ~$1 billion USD (2025 est.)  
**Market share:** <5%

Intel Foundry Services represents Intel's attempt to enter the pure-play foundry market after decades as a vertically-integrated IDM. IFS offers Intel's advanced process nodes to external customers while Intel Products (the design division) remains a large internal customer.

#### Technology Nodes Offered

| Node | Transistor Type | Lithography | Typical Applications | Status |
|------|----------------|-------------|---------------------|--------|
| Intel 18A (1.8 nm) | RibbonFET (GAA) + PowerVia (backside power) | High-NA EUV | HPC, AI accelerators | Pilot production 2024–2025 |
| Intel 20A (2.0 nm) | RibbonFET + PowerVia | EUV | Lead vehicle for 18A | Development vehicle only |
| Intel 3 | FinFET (enhanced) | EUV | Server CPU (internal), potential foundry | 2023 (Intel products) |
| Intel 4 | FinFET | EUV | Meteor Lake (internal) | 2023 (Intel products) |
| Intel 16 (≈7 nm external) | FinFET | DUV | FPGA, embedded | Available via legacy nodes |

**Why Intel 18A matters:** Intel 18A offers two architectural innovations not available elsewhere:
1. **RibbonFET:** Intel's GAA transistor implementation, roughly equivalent to TSMC N2 and Samsung SF2
2. **PowerVia:** Backside power delivery network (buried power rails under the transistors), reducing IR drop and allowing denser logic. Unique among production foundries as of 2025.

**Customer concerns:** 
- Unproven track record — IFS has no mature volume foundry customer wins as of early 2025
- Capacity uncertainty — Intel Products consumes most advanced node capacity
- IP security concerns — Intel competes directly with many potential foundry customers in CPUs, GPUs, AI accelerators
- Design ecosystem immaturity — PDK completeness lags TSMC by 12–24 months

**Strategic customers:** US Department of Defense (Rapid Assured Microelectronics Prototypes – RAMP program), Synopsys (EDA tool co-development), Arm (IP optimisation), potentially Amazon (AI accelerator).

**CHIPS Act support:** Intel received $8.5 billion in direct funding + $11 billion in loans from the US CHIPS and Science Act to expand US foundry capacity. This subsidises Arizona, Ohio, and New Mexico fab construction, potentially enabling lower foundry pricing for strategic customers.

#### Business Terms

| Metric | Value | Notes |
|--------|-------|-------|
| Minimum order (18A) | Negotiable | Seeking early adopters; flexible minimums |
| NRE (18A) | $40–100 M (estimated) | High due to immature ecosystem; subsidised for strategic wins |
| Wafer cost (18A) | Not disclosed | Likely comparable to or higher than TSMC N2 initially |
| Lead time | 16–24 weeks (estimated) | Longer due to new process |
| Yield | Unknown | 18A in pilot; production yield unclear |

---

## 3. Mature-Node Foundries (≥28 nm)

Mature nodes — 180 nm, 130 nm, 90 nm, 65 nm, 40 nm, 28 nm — no longer shrink in feature size but remain critical for analog, mixed-signal, power management, automotive, IoT, and cost-sensitive logic. These nodes offer superior reliability, higher voltage capability, and dramatically lower NRE costs than leading-edge processes.

### GlobalFoundries

**Headquarters:** Malta, New York, USA (fab operations global)  
**Founded:** 2009 (spun out from AMD)  
**Revenue:** ~$8 billion USD (2025)  
**Market share (mature nodes):** ~10%

GlobalFoundries exited leading-edge logic in 2018 (cancelled 7 nm development) and repositioned as a specialty foundry focused on RF, automotive, and IoT. This strategic pivot eliminated the unsustainable capital expenditure race with TSMC.

#### Technology Offerings

| Node / Process | Description | Typical Applications |
|---------------|-------------|---------------------|
| 12LP / 14LPP | 12/14 nm FinFET (legacy) | Networking, FPGA (legacy designs) |
| 22FDX | 22 nm FD-SOI, back-bias capability | RF-SOI, IoT, automotive radar |
| 40LP / 40LPe | 40 nm low-power CMOS | Mainstream logic, MCU |
| 55LPe / 55LPx | 55 nm low-power, extended voltage | Automotive, industrial control |
| 90SLVT | 90 nm super-low-Vth analog | Precision analog, sensor AFE |
| 130BCD | 130 nm bipolar-CMOS-DMOS | Power management, motor control |
| 180MCU | 180 nm mixed-signal | MCU, automotive body electronics |
| SiGe / SiGeBiCMOS | 130–180 nm BiCMOS + SiGe HBT | mmWave RF (28/39 GHz 5G, 77 GHz radar) |

**Why GlobalFoundries for specialty:** 
- **22FDX advantage:** FD-SOI with back-bias offers dynamic V_th tuning — enabling ultra-low-power operation (IoT sensors at 0.4 V) or high-performance mode (RF PA at 77 GHz). No other foundry offers volume FD-SOI at 22 nm.
- **Automotive qualification:** IATF 16949 certified, AEC-Q100 Grade 1 (−40 to +125 °C) processes widely available, extensive automotive customer base (NXP, Qualcomm automotive, Renesas)
- **US/EU capacity:** Fabs in Malta NY, Vermont, Dresden Germany, Singapore — valuable for supply chain diversification away from Taiwan dependence

#### Business Terms

| Metric | 22FDX | 55 nm / 40 nm | 130 nm BCD |
|--------|-------|---------------|-----------|
| Min order | 500–1,000 wafers | 200–500 wafers | 100–300 wafers |
| NRE | $3–8 M | $1–3 M | $0.5–1.5 M |
| Wafer cost | $5,000–6,000 | $2,000–3,000 | $1,200–1,800 |
| Lead time | 10–14 weeks | 8–12 weeks | 6–10 weeks |

---

### UMC (United Microelectronics Corporation)

**Headquarters:** Hsinchu, Taiwan  
**Founded:** 1980  
**Revenue:** ~$7 billion USD (2025)  
**Market share (mature):** ~8%

UMC is the world's third-largest foundry by revenue (after TSMC and Samsung). Like GlobalFoundries, UMC exited advanced nodes (stopped at 14 nm) to focus on mature-node profitability.

#### Technology Offerings

| Node | Process | Applications |
|------|---------|--------------|
| 14 nm | FinFET (limited volume) | Networking, FPGA |
| 22/28 nm | LL (low-leakage), HPC | RF transceiver, FPGA fabric |
| 40 nm | LLP, LP, HV | Display driver IC, MCU |
| 55/65 nm | LP, ULP | IoT, wearables, OLED driver |
| 80/90 nm | LL, LP, SPLL | Automotive MCU, smart card |
| 110/130 nm | HS (high-speed), MS (mixed-signal) | Automotive sensor, PMIC |
| 180/250 nm | MM/RF, HV, BCD | Power discrete, IGBT driver |

**Why UMC competes:** Lower wafer pricing than TSMC for equivalent mature nodes. Faster cycle time (8–10 weeks) for established processes. Strong presence in China (fabs in Suzhou, Xiamen, Fujian) — appeals to mainland China customers. Extensive automotive and industrial certification portfolio.

#### Business Terms (Representative)

| Node | Wafer Cost (300 mm) | Min Order (wafers/qtr) | NRE (new design) |
|------|-------------------|----------------------|-----------------|
| 28 nm | $2,500–3,500 | 500–1,000 | $2–5 M |
| 40 nm | $1,800–2,500 | 300–800 | $1–3 M |
| 110/130 nm | $1,000–1,500 | 100–300 | $0.3–1 M |
| 180 nm | $800–1,200 | 50–200 | $0.2–0.8 M |

---

### SMIC (Semiconductor Manufacturing International Corporation)

**Headquarters:** Shanghai, China  
**Founded:** 2000  
**Revenue:** ~$6 billion USD (2025 est.)  
**Market share:** ~6%

SMIC is China's largest and most advanced foundry. US export controls have restricted SMIC's access to EUV lithography equipment, limiting it to nodes ≥7 nm using DUV multi-patterning.

#### Technology and Geopolitical Context

| Node | Status | Notes |
|------|--------|-------|
| 7 nm (DUV) | Limited volume (2023–present) | DUV-only; no EUV access; yield ~50%; used in Huawei Kirin 9000S |
| 14 nm | Volume production | FinFET; mainstream for China domestic market |
| 28 nm | High volume | HKC, HPC variants; large automotive base |
| 40/55 nm | Mature | — |
| 110/130/180 nm | High volume | IoT, MCU, power management |

**US export restrictions (2020–present):** SMIC is on the US Entity List, restricting sales of advanced semiconductor equipment including EUV lithography and advanced etch/deposition tools. This caps SMIC at ~7 nm achievable through DUV multi-patterning — a technology dead-end beyond 7 nm due to cost and complexity.

**Strategic significance:** SMIC is central to China's semiconductor self-sufficiency goals. Chinese government subsidies (~$10 B cumulative) support capacity expansion despite technology lag. For non-US customers with mature-node requirements and China manufacturing preference, SMIC offers competitive pricing.

**Customer base:** Primarily Chinese fabless companies (HiSilicon, Spreadtrum), automotive (mainland China OEMs), and IoT. International customers limited due to geopolitical risk and IP security concerns.

---

## 4. Specialty Foundries — Analog, RF, Power

Specialty foundries focus on process technologies optimised for non-digital applications: high-voltage power devices, RF transceivers, precision analog, MEMS, and optoelectronics. These processes sacrifice transistor density for other metrics: breakdown voltage, noise performance, linearity, or mechanical functionality.

### Tower Semiconductor (acquired by Intel 2022–2023)

**Headquarters:** Migdal Haemek, Israel  
**Ownership:** Intel Corporation (acquisition completed February 2023 for $5.4 B)  
**Revenue (pre-acquisition):** ~$1.5 billion USD  

Tower specialised in analog-intensive mixed-signal processes. Post-acquisition, it operates as Intel Foundry Services — Specialty Technology division.

#### Process Portfolio

| Technology | Node | Applications |
|-----------|------|--------------|
| SiGe BiCMOS | 180/130 nm | mmWave RF, radar, satellite communication |
| RF-SOI | 130/180 nm | RF switch, antenna tuner, 5G front-end |
| High-voltage BCD | 180/350 nm | PMIC, motor driver, IGBT gate driver |
| CMOS Image Sensor (CIS) | 110/130 nm | Mobile camera, automotive, security |
| Power Discrete | 600 V–1200 V | IGBT, power MOSFET, Schottky diode |
| MEMS (via acquisition) | 180/350 nm | Pressure sensor, accelerometer, microphone |

**Intel's strategy:** Tower acquisition gives Intel a mature-node specialty capability that complements its leading-edge logic push. Tower's automotive and industrial customer base (TI, Broadcom, ON Semi as licensees) provides foundry services revenue diversification.

---

### X-FAB

**Headquarters:** Tessenderlo, Belgium  
**Founded:** 1992  
**Revenue:** ~$800 million USD (2025)  

X-FAB operates six fabs across Germany, France, and Malaysia, focused exclusively on specialty analog and mixed-signal. It does not compete in digital logic.

#### Differentiated Technologies

| Process | Description | Applications |
|---------|-------------|--------------|
| XM018 (Modular) | 180 nm mixed-signal platform | Analog front-end, sensor interface, data converter |
| XT018 | 180 nm high-voltage (50 V) | Display driver, LED driver, industrial control |
| XP018 | 180 nm LDMOS power (120 V) | Class-D audio amplifier, motor control |
| XH018 | 180 nm high-voltage (650 V) | Offline AC-DC converter, PFC controller |
| XI010 (SiGe) | 130 nm SiGe BiCMOS | 77 GHz radar, 60 GHz WLAN, LiDAR |
| Silicon Carbide (SiC) | 150 mm SiC MOSFET/Schottky | EV inverter, solar inverter, HV switching |

**Why X-FAB for automotive:** IATF 16949, AEC-Q100 Grade 0 (−40 to +150 °C), ISO 26262 ASIL-D certified processes. X-FAB has the broadest automotive-qualified analog portfolio of any pure-play foundry. Customers include Melexis (automotive sensor IC), ams OSRAM (automotive lighting), and NXP (automotive power management).

**SiC differentiator:** X-FAB is one of few pure-play foundries offering SiC MOSFET fabrication — most SiC is produced by vertically-integrated power semiconductor companies (Wolfspeed, ON Semi, Infineon, STMicro). X-FAB provides SiC foundry access for fabless power IC designers.

#### Business Terms

| Process | Wafer Size | Wafer Cost | NRE | Min Order |
|---------|-----------|-----------|-----|-----------|
| XM018 modular | 200 mm | $1,500–2,500 | $0.5–2 M | 100–500 wafers |
| XH018 (650 V) | 200 mm | $2,000–3,000 | $0.8–2.5 M | 200–600 wafers |
| XI010 SiGe | 200 mm | $3,000–4,500 | $2–5 M | 300–800 wafers |
| SiC 650 V MOSFET | 150 mm | $3,500–5,000 | $1–3 M | 100–300 wafers |

---

### Vanguard International Semiconductor (VIS)

**Headquarters:** Hsinchu, Taiwan  
**Ownership:** TSMC (28%), Powerchip (24%)  
**Revenue:** ~$1 billion USD  

Specialty foundry focused on power discrete and high-voltage analog. Strong presence in power management IC (PMIC) for consumer and computing markets.

**Process strength:** 0.25 µm–0.15 µm high-voltage BCD (Bipolar-CMOS-DMOS) with 40–90 V capability. Cost-competitive alternative to TSMC for non-leading-edge PMIC.

---

## 5. MEMS and Sensor Foundries

MEMS (micro-electro-mechanical systems) foundries combine semiconductor fabrication with mechanical structure release, packaging, and often wafer-level assembly. MEMS processes are highly application-specific — an accelerometer process is completely incompatible with a microphone process — so MEMS foundries typically offer multiple isolated process flows.

### Teledyne DALSA Semiconductor

**Headquarters:** Bromont, Quebec, Canada  
**Fab Size:** 200 mm  

Specialises in MEMS inertial sensors (accelerometers, gyroscopes), pressure sensors, and CMOS image sensors. Strong automotive qualification portfolio.

**Process offerings:**
- Bulk micromachining (capacitive pressure sensor)
- Surface micromachining (gyroscope, accelerometer)
- Bonded SOI (inertial sensor with vacuum packaging)

**Target customers:** Automotive Tier 1 suppliers, industrial sensor companies, medical diagnostics. Minimum order ~50–100 wafers. NRE $0.5–2 M depending on custom process requirements.

---

### Silex Microsystems

**Headquarters:** Järfälla, Sweden  
**Fabs:** Sweden (200 mm), USA (200 mm)  

Pure-play MEMS foundry with no IC capability. Offers custom and semi-custom MEMS fabrication across multiple process platforms:

| Platform | Description | Applications |
|---------|-------------|--------------|
| MEMS capacitive | Polysilicon surface micromachining | Accelerometer, gyroscope, pressure sensor |
| MEMS resonator | High-Q MEMS oscillator, <100 ppm stability | Timing reference, clock replacement |
| MEMS optical | Micromirror array, tunable filter | LiDAR, optical switching |
| MEMS fluidic | Microfluidic channel, valve, pump | Lab-on-chip, drug delivery |
| Through-silicon via (TSV) | DRIE + metallisation for 3D integration | 3D-stacked image sensor, interposer |

**Business model:** Silex operates on a semi-custom basis — customers submit designs that are adapted to one of Silex's pre-qualified process flows. Lower NRE than full-custom MEMS ($0.3–1.5 M typical) at the cost of design constraint. Minimum order 25–100 wafers.

---

### Innovative Micro Technology (IMT)

**Headquarters:** Santa Barbara, California, USA  
**Fab Size:** 150 mm  

Specialises in electrostatically-actuated MEMS: micromirrors for optical switching, RF MEMS switches, and tunable capacitors. Process portfolio based on polysilicon surface micromachining with sacrificial oxide release.

**Typical customers:** Aerospace (optical crossconnect), telecommunications (RF switching matrix), medical (endoscopic imaging), and consumer (pico-projector). Custom design services included — IMT's business model bundles design, fabrication, and packaging as a turnkey service. Minimum order 25 wafers. NRE $0.5–3 M.

---

### TSMC MEMS/Sensor

**Location:** Fab 5 (Hsinchu), Fab 3 (specialty)  
**Fab Size:** 200 mm  

TSMC entered MEMS in 2011 to capture the growing smartphone sensor market. Offers integrated MEMS+CMOS processes where sensor and ASIC are co-fabricated on the same die or bonded at wafer level.

**Process offerings:**
- CMOS MEMS (monolithic integration — sensor and logic on same die)
- Backside illumination (BSI) CMOS image sensor
- Wafer-level packaging (WLP) for MEMS
- Through-silicon via (TSV) for 3D stacking

**Target customers:** Tier-1 smartphone OEMs (Apple, Samsung), automotive imaging (Sony, OmniVision), industrial sensors. Minimum order ~1,000 wafers — much higher than specialty MEMS foundries because TSMC optimises for volume. NRE $3–10 M depending on integration complexity.

---

## 6. Compound Semiconductor Foundries (GaAs, GaN, SiC)

Compound semiconductors — materials other than silicon — enable applications that silicon cannot address: high-frequency RF (GaAs), high-power switching (SiC), high-efficiency power amplifiers (GaN). These foundries operate on substrates ranging from 100 mm (SiC) to 200 mm (GaN-on-Si).

### WIN Semiconductors (GaAs)

**Headquarters:** Taoyuan, Taiwan  
**Founded:** 1999  
**Revenue:** ~$800 million USD  

World's largest pure-play GaAs foundry. Specialises in RF front-end ICs for mobile handsets (power amplifiers, switches, LNAs) and wireless infrastructure.

| Process | Technology | fT / fmax | Applications |
|---------|-----------|-----------|--------------|
| pHEMT | Pseudomorphic high-electron-mobility transistor | 60 GHz / 120 GHz | 2G/3G/4G PA, WiFi |
| HBT | Heterojunction bipolar transistor | 80 GHz / 150 GHz | 5G sub-6 GHz PA, mmWave PA |
| GaAs MMIC | Monolithic microwave IC | — | Radar front-end, satellite communication |

**Wafer cost:** $2,000–4,000 per 150 mm wafer (GaAs substrate + epitaxy). NRE $0.5–2 M. Lead time 8–12 weeks.

**Competition:** Qorvo and Skyworks (both IDMs) dominate the smartphone PA market but use foundries including WIN Semi for capacity expansion and legacy products.

---

### Qromis (GaN-on-Si)

**Headquarters:** Santa Clara, California, USA  
**Founded:** 2006  
**Fab:** Fremont, CA (200 mm)  

Pure-play GaN power foundry. Focuses on GaN-on-Si for cost-competitive power conversion (USB-PD chargers, server PSU, EV onboard chargers).

| Process | Breakdown Voltage | RDS(on) | Applications |
|---------|------------------|---------|--------------|
| 150 V GaN | 150 V | 5–10 mΩ·mm² | USB-C PD, laptop adapter |
| 650 V GaN | 650 V | 15–30 mΩ·mm² | AC-DC converter, motor drive, solar inverter |
| 1200 V GaN (development) | 1200 V | 40–80 mΩ·mm² | EV traction inverter, HV DC-DC |

**Why GaN-on-Si matters:** GaN power devices switch 5–10× faster than silicon MOSFETs or IGBTs at the same voltage rating, enabling dramatic size and weight reduction in power supplies. The GaN-on-Si approach (GaN epitaxy on 200 mm silicon wafers) enables mainstream CMOS fab processing and cost scalability — in contrast to GaN-on-SiC (higher performance but 3–5× cost due to expensive SiC substrates).

**Wafer cost:** $3,000–5,000 per 200 mm wafer. NRE $1–3 M. Lead time 10–14 weeks.

---

### Wolfspeed (SiC)

**Headquarters:** Durham, North Carolina, USA  
**Founded:** 1987 (as Cree; renamed Wolfspeed 2021)  
**Revenue:** ~$700 million USD  

Vertically integrated SiC company — grows SiC substrates, epitaxy, device fabrication, and module assembly. Also offers foundry services for third-party SiC power device designers.

| Process | Substrate | Voltage Class | Applications |
|---------|-----------|---------------|--------------|
| SiC MOSFET | 150 mm SiC | 650 V, 900 V, 1200 V, 1700 V | EV inverter, solar PV, industrial motor drive |
| SiC Schottky diode | 150 mm SiC | 600 V, 1200 V, 1700 V | PFC rectifier, boost converter |
| SiC JFET (niche) | 150 mm SiC | 1200 V | High-temperature applications |

**Why SiC for power:** 10× higher breakdown field than silicon enables 10× thinner drift layer → 100× lower on-resistance at same voltage rating → dramatically lower conduction loss in high-power converters. SiC 1200 V MOSFETs compete directly with silicon 1200 V IGBTs and are winning in EV traction inverters (Tesla Model 3/Y, GM Ultium, Ford Mach-E all use SiC).

**SiC substrate bottleneck:** SiC wafers are expensive ($1,500–2,000 per 150 mm blank) and difficult to manufacture — crystal growth is 100× slower than silicon. Wolfspeed, II-VI, STMicro, and Rohm are the primary substrate suppliers. Wafer supply shortage constrains the entire SiC industry through 2025.

**Foundry model:** Wolfspeed offers SiC foundry services primarily to automotive OEMs developing custom power modules (GM, Mercedes). Wafer cost $5,000–8,000 per 150 mm (substrate + process). NRE $2–5 M. Minimum order 100–300 wafers.

---

## 7. Packaging and Heterogeneous Integration

Advanced packaging is increasingly critical as Moore's Law slows. Chiplets — smaller dies assembled into a system-in-package — allow cost-effective heterogeneous integration: logic at 5 nm, I/O at 16 nm, memory at 10 nm DRAM, all on a silicon interposer or organic substrate.

### TSMC SoIC (System-on-Integrated-Chips)

**Technology:** Wafer-on-wafer (WoW) and chip-on-wafer (CoW) bonding with <1 µm pitch micro-bumps.

**Applications:** High-bandwidth memory (HBM) stacks, 3D-stacked logic, chiplet integration (Apple M-series Ultra variants use UltraFusion — two SoCs bonded face-to-face with >10,000 interconnects).

**Cost adder:** 20–40% over standard flip-chip packaging. Lead time +6–10 weeks.

---

### Intel EMIB (Embedded Multi-Die Interconnect Bridge)

**Technology:** Silicon bridge embedded in organic substrate — allows 2.5D chiplet connection with <50 µm pitch without expensive silicon interposer.

**Applications:** Intel Sapphire Rapids Xeon (compute + HBM), Ponte Vecchio GPU (47 tiles). Available via IFS for external customers.

**Cost:** Lower than CoWoS (TSMC's competing technology) for <4 dies; higher for larger assemblies.

---

### Amkor, ASE, JCET (OSAT — Outsourced Assembly and Test)

Provide packaging services for fabless companies and IDMs. Offerings include flip-chip, wire-bond, fan-out wafer-level packaging (FOWLP), system-in-package (SiP), and 3D stacking.

**Typical flow:** Foundry ships good-die wafers to OSAT → OSAT dices, assembles, encapsulates, tests, and ships finished packaged ICs to customer.

**Cost structure:** Packaging adds $0.50–$5.00 per die depending on complexity. Flip-chip BGA (high I/O count, thermal management) costs $2–4/die. Simple wire-bond QFP costs $0.20–0.50/die.

---

## 8. Academic and Research Foundries

Provide subsidised or cost-recovery access to semiconductor fabrication for university research groups, startups, and government-funded R&D programs. Not suitable for volume production but critical for workforce training and technology prototyping.

### SkyWater Technology (130 nm Open-Source PDK)

**Location:** Bloomington, Minnesota, USA  
**Fab Size:** 200 mm  
**Ownership:** Private (acquired from Cypress 2017)  

SkyWater operates a DoD-trusted foundry (secure supply chain for defence ICs) and participates in Google's open-source PDK initiative.

**130 nm Open-Source Access:** Funded by Google and the CHIPS Act, SkyWater released a fully open-source 130 nm process design kit (PDK) in 2020 — the first time a commercial foundry has published complete design rules, device models, and verification decks publicly. This enables:
- University courses teaching full IC design → fabrication (previously prohibitive due to $10k–50k PDK license fees)
- Startups prototyping custom ICs risk-free
- Open-source hardware community developing reusable IP cores

**Cost model:** Fabrication runs organised as multi-project wafers (MPW) — dozens of designs share a wafer. Cost per mm² ~$10–20 (subsidised by Google/CHIPS Act funding initially). Schedule: quarterly MPW shuttles.

---

### MOSIS (USC Information Sciences Institute)

**Location:** Los Angeles, California, USA  
**Founded:** 1981  

MOSIS pioneered the multi-project wafer (MPW) concept — aggregating small-volume IC designs from academic and government researchers onto shared wafer runs at commercial foundries.

**Business model:** MOSIS negotiates discounted capacity from TSMC, GlobalFoundries, and other foundries, then resells in small quantities (as few as 5 mm² of silicon) at heavily subsidised prices for research and education.

**Available processes:** 180 nm, 130 nm, 90 nm, 65 nm, and specialty processes (SiGe, SOI). Runs scheduled quarterly. Typical cost for university research: $5,000–15,000 for 40 packaged dies (5 mm² each).

---

### EUROPRACTICE

**Location:** Interuniversity Microelectronics Centre (IMEC), Leuven, Belgium  

European equivalent of MOSIS. Provides multi-project wafer access to university and SME customers across Europe. Affiliated with 20+ universities. Fabrication through agreements with X-FAB, IHP, and other European foundries.

---

### MIT Lincoln Laboratory

**Location:** Lexington, Massachusetts, USA  
**Fab Size:** 150 mm / 200 mm  
**Affiliation:** US Department of Defense  

Government-funded research fab focused on advanced materials (GaN, InP, superconducting electronics) and rad-hard ICs for space and defence. Not open to commercial customers but collaborates with DoD contractors and DARPA programs.

---

## 9. Selection Criteria and Trade-offs

Choosing the right foundry involves balancing multiple competing objectives. No single foundry optimises for all criteria simultaneously.

### Performance vs. Cost

**Leading-edge nodes (TSMC N3, Samsung SF3, Intel 18A):**
- **Advantages:** Highest transistor density, lowest power per transistor, fastest digital logic
- **Disadvantages:** $30–80 M NRE, $16k–20k per wafer, 70–85% yield initially, 12–24 month development cycle, requires EDA tools and IP optimised for node

**Mature nodes (28 nm, 40 nm, 65 nm):**
- **Advantages:** $1–5 M NRE, $2k–4k per wafer, >95% mature yield, proven IP libraries, 6–10 week cycle time
- **Disadvantages:** ~3× larger die area for same logic function, ~2–5× higher power consumption

**Decision heuristic:** Use leading-edge only if product economics justify it — typically high-volume consumer (smartphone, PC, cloud server) where die cost amortises over >10M units/year, or where power/performance at any cost is the requirement (AI training accelerator, HPC). For industrial, automotive, IoT, or <1M units/year, mature nodes nearly always win.

---

### Geopolitical Risk and Supply Chain

**Taiwan concentration risk:** TSMC controls 60% of global foundry capacity and >90% of advanced logic capacity. Nearly all leading-edge chips — smartphone SoCs, datacenter CPUs/GPUs, AI accelerators — are fabricated in Taiwan. This creates systemic risk:
- Natural disaster (earthquake, typhoon)
- Cross-strait military conflict
- Export restrictions or sanctions

**Mitigation strategies:**
1. **Dual-source:** Qualify designs at both TSMC and Samsung (expensive: 2× NRE)
2. **Geographic diversification:** TSMC Arizona (N4/N3, 2025+), Samsung Texas (SF4, 2024+), Intel Ohio (18A, 2026+)
3. **Node derating:** Design at mature node available from multiple foundries (28 nm available from TSMC, Samsung, GlobalFoundries, UMC, SMIC)

**US/EU policy response:** CHIPS Act ($52 B USA, 2022), EU Chips Act (€43 B, 2023) subsidise domestic foundry capacity. However, most subsidised fabs produce trailing-edge or mature-node chips (Intel Ohio 18A is exception). Leading-edge still concentrated in Taiwan and South Korea through 2027.

---

### Automotive Qualification

Automotive IC foundries must demonstrate:
- IATF 16949 QMS certification
- AEC-Q100 qualification (1,000 h @ 150 °C HTOL, 1,000 thermal cycles)
- Zero-defect mentality (automotive target: <0.1 defective PPM)
- Long-term supply commitment (automotive production lifetime 10–15 years; semiconductor node lifetime often <5 years)

**Qualified foundries:** GlobalFoundries, UMC, TSMC (automotive BU), Tower/Intel, X-FAB, Vanguard, Samsung (automotive-qualified nodes limited to 28 nm and above).

**Automotive foundry premium:** Wafers cost 10–30% more for automotive-qualified lots due to tighter process control, extended burn-in, and traceability requirements.

---

### IP Security

**Concern:** Fabless companies must share complete design databases (GDS-II layout files) with the foundry. This database represents years of engineering investment and embodies proprietary circuit architectures.

**Risk scenarios:**
1. **Rogue employee exfiltration:** Employee at foundry copies customer design for sale to competitor
2. **State-sponsored IP theft:** Government intelligence services access foundry systems
3. **Overproduction and grey market:** Foundry runs extra wafers beyond contract and sells to grey market

**Mitigation — technical:**
- Design obfuscation (encrypt sensitive blocks)
- Split fabrication (critical IP on trusted foundry, commodity logic on lower-cost foundry)
- Hardware security modules (HSM) for mask data encryption

**Mitigation — contractual:**
- NDA with liquidated damages clause
- Right-to-audit foundry security practices
- Indemnification for IP breach

**Trusted foundries:** US DoD maintains "trusted foundry" program — foundries with security clearances, US-citizen-only clean rooms, and regular security audits. Examples: SkyWater, IBM (Albany), Intel (Oregon), BAE Systems. Required for ICs containing classified information or weapon system critical functions.

---

## 10. Cost Structure and Economics

Understanding the cost structure of IC fabrication informs foundry selection and business case development.

### NRE (Non-Recurring Engineering) Breakdown

NRE is the one-time cost to bring a new IC design to production. It does not recur with each wafer lot.

| Component | Leading-Edge (5 nm) | Mature (40 nm) | Mature (180 nm) |
|-----------|-------------------|----------------|-----------------|
| **Mask set** | $12–18 M | $0.8–2 M | $0.05–0.15 M |
| **Design IP license** | $5–20 M | $0.5–2 M | $0.1–0.5 M |
| **EDA tool time** | $2–5 M | $0.2–0.8 M | $0.05–0.2 M |
| **Foundry engineering** | $5–15 M | $0.5–2 M | $0.1–0.5 M |
| **First silicon / debug** | $3–10 M | $0.3–1 M | $0.05–0.3 M |
| **Test program development** | $1–3 M | $0.2–0.6 M | $0.05–0.2 M |
| **Packaging NRE** | $1–5 M | $0.2–0.8 M | $0.05–0.3 M |
| **Total NRE** | **$30–80 M** | **$2.5–8 M** | **$0.4–2 M** |

**Mask cost dominance:** At 5 nm, a full reticle set with EUV layers costs $12–18 M — more than half the total NRE. Each EUV mask costs ~$200k–300k vs. ~$10k–20k for DUV masks. There are 40–50 mask layers in a modern logic process, with 10–15 of those being EUV at 5 nm / 3 nm.

---

### Wafer Cost and Die Cost

**Wafer cost drivers:**
- Node (smaller → more expensive due to equipment depreciation)
- Wafer size (300 mm standard for advanced nodes; 200 mm for mature/specialty)
- Metal layer count (each additional metal layer adds $200–500 per wafer)
- Special features (embedded memory, analog, RF)

**Representative wafer costs (300 mm):**
| Node | Wafer Cost | Notes |
|------|-----------|-------|
| 3 nm | $18,000–20,000 | EUV-heavy |
| 5 nm | $16,000–18,000 | EUV |
| 7 nm | $12,000–15,000 | DUV + limited EUV |
| 16 nm | $6,000–8,000 | FinFET, DUV |
| 28 nm | $2,500–4,000 | Planar or FinFET |
| 40 nm | $1,800–2,800 | Planar |
| 130 nm | $1,000–1,800 | — |
| 180 nm | $800–1,400 | — |

**Die cost calculation:**
$$
\text{Die Cost} = \frac{\text{Wafer Cost}}{\text{Gross Dies per Wafer} \times \text{Yield}}
$$

**Example (100 mm² die on 300 mm wafer):**
- Gross dies per wafer: ~650 (accounting for edge loss)
- Yield (mature design, 5 nm): 80%
- Wafer cost: $17,000
- Die cost: $17,000 / (650 × 0.80) = **$32.70 per die**

**Packaging and test add-on:**
- Advanced flip-chip packaging: $2–5 per die
- Standard QFN/QFP: $0.20–0.80 per die
- Final test: $0.10–1.00 per die (depending on test time)

**Total IC cost:** $35–40 per die for this example.

---

### Break-Even Volume

NRE must be amortised over production volume. The break-even volume is the production quantity where NRE + production cost equals the revenue.

**Simplified model:**
$$
\text{Break-even units} = \frac{\text{NRE}}{\text{ASP} - \text{Variable Cost per Unit}}
$$

**Example:**
- NRE: $40 M (5 nm logic SoC)
- Die cost: $40
- Packaging: $3
- Test: $1
- Variable cost: $44
- Target ASP: $100
- Contribution margin: $56

$$
\text{Break-even} = \frac{40,000,000}{56} = 714,000 \text{ units}
$$

If production ramps to 2M units/year, NRE is recovered in ~4 months. If production is only 100k units/year, NRE never recovers. This is why leading-edge nodes are only viable for very high volume products.

---

### Foundry Business Model — Allocation and Pricing

**Capacity allocation mechanisms:**
1. **Long-term agreement (LTA):** Customer commits to minimum quarterly wafer volumes (e.g., 10,000 wafers/quarter for 3 years) in exchange for guaranteed capacity and fixed pricing. Typical for strategic customers (Apple, AMD, NVIDIA at TSMC).
2. **Spot market:** Customer orders wafers quarter-by-quarter with no commitment. Pricing fluctuates with supply-demand; lead times extend during shortages. Typical for smaller customers.
3. **Prepayment:** During capacity shortages, foundries require prepayment (3–6 months in advance) to secure slot allocation.

**Pricing dynamics (2020–2025):** Pandemic-driven demand surge + fab capex lag → multi-year undersupply → spot prices increased 15–30% above LTA pricing (2021–2022). Supply-demand rebalanced by 2024; spot premiums compressed to 0–10%.

---

## 11. Quick-Reference Foundry Tables

### 11.1 Leading-Edge Logic Foundries (≤7 nm)

| Foundry | Best Node | Transistor Type | Wafer Cost (best node) | NRE | Market Position |
|---------|----------|----------------|----------------------|-----|-----------------|
| TSMC | N3E / N3P | FinFET | $18k–20k | $30–80 M | Market leader, 60% advanced share |
| Samsung | SF3 | GAA (MBCFET) | $17k–19k | $25–70 M | Second place, aggressive pricing |
| Intel IFS | 18A | RibbonFET (GAA) + PowerVia | TBD (est. $18k–22k) | $40–100 M | New entrant, unproven yield |

### 11.2 Mature-Node Foundries

| Foundry | Headquarters | Nodes Offered | Specialty | Wafer Cost (28 nm) | Market Share |
|---------|-------------|--------------|-----------|-------------------|--------------|
| GlobalFoundries | USA (NY) | 12–180 nm | 22FDX, automotive, RF-SOI | $2.5k–4k | 10% |
| UMC | Taiwan | 14–350 nm | Automotive, display driver, IoT | $2.5k–3.5k | 8% |
| SMIC | China | 7–180 nm (DUV) | China domestic, price-competitive | $2k–3k | 6% |
| Tower/Intel | Israel | 65–350 nm | Analog, CIS, power, MEMS | $1.5k–3k | 3% |

### 11.3 Specialty and MEMS Foundries

| Foundry | Specialty | Wafer Size | Target Applications | Representative Wafer Cost |
|---------|-----------|-----------|---------------------|-------------------------|
| X-FAB | High-voltage analog, SiC | 150–200 mm | Automotive PMIC, motor control, EV inverter | $1.5k–5k |
| Vanguard | Power discrete, BCD | 200 mm | Consumer PMIC, display driver | $1k–2.5k |
| Silex Micro | Pure-play MEMS | 200 mm | Accelerometer, gyroscope, pressure sensor | $1.5k–4k |
| Teledyne DALSA | MEMS, CIS | 200 mm | Automotive sensor, medical imaging | $2k–4k |

### 11.4 Compound Semiconductor Foundries

| Foundry | Material | Substrate Size | Voltage / Frequency | Wafer Cost | Applications |
|---------|---------|---------------|-------------------|-----------|--------------|
| WIN Semi | GaAs | 150 mm | fT ~80 GHz | $2k–4k | 5G PA, radar front-end |
| Qromis | GaN-on-Si | 200 mm | 150–1200 V | $3k–5k | USB-C PD, server PSU, EV charger |
| Wolfspeed | SiC | 150 mm | 650–1700 V | $5k–8k | EV traction inverter, solar PV |
| IQE | InP, GaN | 100–150 mm | fmax ~300 GHz | $4k–8k | mmWave satellite, photonics |

### 11.5 Typical Lead Times by Node

| Node / Complexity | Engineering Samples (first Si) | Qual Lots | Production Ramp (10k wpm) |
|------------------|------------------------------|----------|--------------------------|
| 3–5 nm (TSMC, Samsung) | 14–18 weeks | 6–10 weeks | 6–12 months |
| 7–16 nm | 12–16 weeks | 4–8 weeks | 4–8 months |
| 28–40 nm | 10–14 weeks | 4–6 weeks | 3–6 months |
| 90–180 nm | 8–12 weeks | 3–5 weeks | 2–4 months |
| MEMS (custom) | 14–20 weeks | 6–10 weeks | 6–12 months |
| Compound (GaAs, SiC) | 10–16 weeks | 4–8 weeks | 4–8 months |

---

## Further Reading

- *IC Insights* — quarterly foundry market share and pricing reports
- *Semiconductor Engineering* — foundry technology and business analysis
- *EE Times* — foundry announcements and customer wins
- *SEMI Equipment Market Report* — capital equipment spending by foundry
- TSMC Technology Symposia presentations (annual) — foundry roadmap updates
- Gartner / IDC semiconductor manufacturing reports
- *The Chip War* by Chris Miller — geopolitical context of foundry industry

---

*Part of the Silicon Fabrication Handbook — [github.com/Zeyad-Mustafa/silicon-fabrication-handbook](https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook)*  
*Last updated: February 2026*. 