# Useful Links and Resources

**A curated collection of online resources, databases, tools, and references for semiconductor and MEMS fabrication.**

Learning semiconductor fabrication requires access to diverse information sources: equipment vendor white papers, university courses, standards documents, simulation tools, and active research literature. This document organizes the most valuable online resources by category, with brief descriptions of what each offers and when to use it.

All links verified as of February 2026. Many resources are freely accessible; some require institutional access or paid subscriptions (noted where applicable).

---

## Table of Contents

1. [Educational Resources](#1-educational-resources)
2. [Standards and Specifications](#2-standards-and-specifications)
3. [Technical Databases](#3-technical-databases)
4. [Simulation and Design Tools](#4-simulation-and-design-tools)
5. [Industry News and Analysis](#5-industry-news-and-analysis)
6. [Conference Proceedings and Journals](#6-conference-proceedings-and-journals)
7. [Equipment Vendors and Datasheets](#7-equipment-vendors-and-datasheets)
8. [Open-Source Projects and Foundries](#8-open-source-projects-and-foundries)
9. [Professional Organizations](#9-professional-organizations)
10. [YouTube Channels and Video Resources](#10-youtube-channels-and-video-resources)
11. [Podcasts and Audio Resources](#11-podcasts-and-audio-resources)
12. [Books and Textbooks](#12-books-and-textbooks)

---

## 1. Educational Resources

### University Courses (Free Online)

#### MIT OpenCourseWare — Integrated Microelectronic Devices
**URL:** https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2009/  
**Description:** Complete course covering semiconductor physics, MOSFET operation, and device modeling. Lecture notes, problem sets, and exams available.  
**Best for:** Understanding device physics from first principles.

#### Stanford EE311 — Semiconductor Device Physics
**URL:** https://online.stanford.edu (search for EE311)  
**Description:** Graduate-level course on PN junctions, BJTs, MOSFETs, and device scaling. Requires Stanford Online enrollment (free audit available).  
**Best for:** Deep dive into carrier transport and quantum effects.

#### UC Berkeley EECS 143 — Microfabrication Technology
**URL:** https://inst.eecs.berkeley.edu/~ee143/  
**Description:** Lab-focused course covering cleanroom processes, lithography, thin films, etching, and device fabrication. Excellent lecture slides publicly available.  
**Best for:** Practical fabrication process understanding.

#### Purdue nanoHUB — Semiconductor Education Resources
**URL:** https://nanohub.org/  
**Description:** Free online platform with simulation tools (TCAD, SPICE), courses, and seminars on nanofabrication, devices, and materials. Over 10,000 resources.  
**Best for:** Interactive simulations and visual learning.

#### TU Delft — MEMS & Microsystems Technology
**URL:** https://online-learning.tudelft.nl/ (search for MEMS)  
**Description:** Online course covering MEMS design principles, fabrication techniques, and applications. Offered through edX.  
**Best for:** MEMS-specific process flows and design methodologies.

### Online Tutorials and Guides

#### Semiconductor Manufacturing Handbook (Online)
**URL:** https://www.lithoguru.com/  
**Description:** Extensive tutorial library by Chris Mack covering lithography optics, resolution limits, OPC (optical proximity correction), and photoresist chemistry.  
**Best for:** Deep understanding of lithography physics.

#### MEMS and Nanotechnology Exchange
**URL:** https://www.mems-exchange.org/  
**Description:** Community portal with design tutorials, fabrication protocols, and MEMS foundry comparison tools.  
**Best for:** MEMS designers seeking foundry services.

#### SemiWiki Educational Resources
**URL:** https://semiwiki.com/semiconductor-manufacturers/  
**Description:** Industry blog with detailed articles on semiconductor manufacturing, EDA tools, and foundry technology. Free registration required.  
**Best for:** Current industry trends and technology updates.

#### Cleanroom Training Videos
**URL:** https://www.youtube.com/@SNFStanford  
**Description:** Stanford Nanofabrication Facility's YouTube channel with equipment training videos, process demonstrations, and safety protocols.  
**Best for:** Visual learners and hands-on fab users.

---

## 2. Standards and Specifications

### SEMI Standards
**URL:** https://www.semi.org/en/products-services/standards  
**Access:** Paid subscription required ($2,000–$10,000/year for full access)  
**Description:** Complete collection of SEMI standards covering equipment automation (E-series), materials (M-series), safety (S-series), and processes. Free previews available.  
**Key standards:** SEMI M1 (wafer specs), SEMI E5 (SECS-II communication), SEMI S2 (equipment safety).  
**Note:** Many universities and companies maintain institutional subscriptions.

### JEDEC Standards
**URL:** https://www.jedec.org/standards-documents  
**Access:** Free download after registration  
**Description:** Semiconductor device and packaging standards. Includes complete reliability test methods (JESD22 series), memory specifications (DDR, LPDDR), and qualification flows (JESD47).  
**Best for:** Reliability engineering and qualification procedures.

### IEC Webstore
**URL:** https://webstore.iec.ch/  
**Access:** Pay-per-document ($50–$300 per standard)  
**Description:** International electrical standards including IEC 60068 (environmental testing), IEC 61010 (equipment safety), and IEC 62047 (MEMS standards).  
**Best for:** Safety compliance and international specifications.

### ASTM Standards
**URL:** https://www.astm.org/  
**Access:** Pay-per-document or subscription  
**Description:** Material characterization test methods including silicon resistivity (F723), oxygen content (F1239), and nanoindentation (E2546).  
**Best for:** Material property measurement procedures.

### ISO Standards Catalog
**URL:** https://www.iso.org/standards.html  
**Access:** Pay-per-document  
**Description:** Quality management (ISO 9001), cleanroom classification (ISO 14644), and environmental management (ISO 14001) standards.  
**Best for:** Quality systems and cleanroom design.

---

## 3. Technical Databases

### NIST Materials Database
**URL:** https://webbook.nist.gov/  
**Description:** Thermophysical and thermochemical data for thousands of materials. Includes vapor pressure, heat capacity, thermal conductivity, and reaction kinetics.  
**Access:** Free  
**Best for:** Process modeling and material property lookup.

### Ioffe Physical-Technical Institute Database
**URL:** http://www.ioffe.ru/SVA/NSM/Semicond/  
**Description:** Comprehensive semiconductor material properties (Si, Ge, GaAs, InP, SiC, GaN, etc.): bandgap, mobility, thermal conductivity, lattice constants, and temperature dependence.  
**Access:** Free  
**Best for:** Device physics and material selection.

### MatWeb Material Property Database
**URL:** https://www.matweb.com/  
**Description:** Searchable database of engineering material properties including metals, polymers, ceramics, and composites. Covers Young's modulus, CTE, density, thermal conductivity.  
**Access:** Free (basic), paid for advanced features  
**Best for:** MEMS structural material selection and thermal analysis.

### Refractive Index Database
**URL:** https://refractiveindex.info/  
**Description:** Optical constants (refractive index, extinction coefficient) for hundreds of materials across UV to IR wavelengths. Essential for lithography and optical MEMS design.  
**Access:** Free  
**Best for:** Optical thin film design and ellipsometry modeling.

### Crystallography Open Database (COD)
**URL:** http://www.crystallography.net/  
**Description:** Crystal structures of >400,000 compounds. Includes unit cell parameters, space groups, and atomic positions.  
**Access:** Free  
**Best for:** Epitaxy lattice matching and XRD pattern identification.

---

## 4. Simulation and Design Tools

### ngspice (Open-Source SPICE Simulator)
**URL:** http://ngspice.sourceforge.net/  
**Description:** Open-source circuit simulator compatible with commercial SPICE syntax. Supports transistor models (BSIM, EKV), subcircuits, and transient/AC/DC analysis.  
**Best for:** Circuit simulation without expensive commercial licenses.

### Magic VLSI Layout Tool
**URL:** http://opencircuitdesign.com/magic/  
**Description:** Open-source layout editor for IC design. Supports GDS-II export, DRC, and extraction. Works with SkyWater 130nm PDK.  
**Best for:** Open-source IC layout and learning VLSI design.

### KLayout
**URL:** https://www.klayout.de/  
**Description:** High-performance layout viewer and editor. Reads GDS-II, OASIS, and other formats. Scripting support (Ruby/Python). Free and cross-platform.  
**Best for:** Viewing and editing layout files, DRC/LVS scripting.

### COMSOL Multiphysics (Free Trial)
**URL:** https://www.comsol.com/  
**Description:** Finite-element simulation for coupled physics (thermal, structural, electrical, fluid). MEMS module includes squeeze-film damping, piezoelectric, and electrostatic solvers.  
**Access:** Commercial license ($5k–$50k) or 90-day trial  
**Best for:** MEMS device simulation and multiphysics coupling.

### Sentaurus TCAD (Synopsys)
**URL:** https://www.synopsys.com/silicon/tcad.html  
**Description:** Industry-standard process and device simulation. Models oxidation, diffusion, ion implantation, etching, and complete device electrical characteristics.  
**Access:** Commercial license (university discounts available)  
**Best for:** Advanced CMOS process development and device optimization.

### SILVACO TCAD
**URL:** https://silvaco.com/tcad/  
**Description:** Competitor to Sentaurus TCAD with similar capabilities. Athena (process simulator) and Atlas (device simulator) are flagship tools.  
**Access:** Commercial license  
**Best for:** Alternative to Synopsys for TCAD simulation.

### Python Scientific Stack (Free)
**Packages:** NumPy, SciPy, Matplotlib, pandas  
**URL:** https://scipy.org/  
**Description:** Open-source libraries for numerical computation, data analysis, and plotting. Ideal for custom process models and data analysis scripts.  
**Best for:** Building custom simulation tools and analyzing experimental data.

### FreeCAD + A2plus
**URL:** https://www.freecad.org/  
**Description:** Open-source 3D parametric CAD software. Useful for MEMS device visualization and mechanical assembly design.  
**Best for:** 3D visualization and mechanical design without expensive CAD licenses.

---

## 5. Industry News and Analysis

### Semiconductor Engineering
**URL:** https://semiengineering.com/  
**Description:** Daily news covering process technology, EDA tools, design trends, and industry analysis. Excellent technical depth on emerging nodes and packaging.  
**Best for:** Staying current on leading-edge technology developments.

### EE Times
**URL:** https://www.eetimes.com/  
**Description:** Electronics engineering news covering semiconductors, embedded systems, automotive, and IoT. Mix of news and technical articles.  
**Best for:** Broad industry coverage and design engineer perspective.

### Anandtech
**URL:** https://www.anandtech.com/  
**Description:** Deep-dive reviews and technical analysis of processors, GPUs, and memory products. Detailed architecture and manufacturing discussions.  
**Best for:** Understanding how process technology translates to product performance.

### WikiChip
**URL:** https://en.wikichip.org/  
**Description:** Comprehensive database of processor microarchitectures, process nodes, and die photos. Detailed technical specifications.  
**Best for:** Processor architecture research and die size analysis.

### SemiAnalysis
**URL:** https://www.semianalysis.com/  
**Description:** Industry analysis newsletter covering foundry economics, supply chain, geopolitics, and technology trends. Some content paywalled.  
**Best for:** Business-level semiconductor industry analysis.

### ASML Blog and Technology Papers
**URL:** https://www.asml.com/en/technology  
**Description:** Technical articles from the world's leading lithography equipment supplier. Deep dives on EUV, high-NA, and computational lithography.  
**Best for:** Understanding lithography technology from the equipment maker.

### Chips and Cheese (CPU Architecture)
**URL:** https://chipsandcheese.com/  
**Description:** Detailed microarchitecture analysis and performance testing. Reverse-engineers CPU designs through benchmarking and die shots.  
**Best for:** Understanding CPU architecture and performance bottlenecks.

---

## 6. Conference Proceedings and Journals

### IEEE Xplore Digital Library
**URL:** https://ieeexplore.ieee.org/  
**Access:** Institutional subscription or pay-per-article ($33)  
**Description:** Complete proceedings from IEDM, VLSI Technology, ISSCC, ISCAS, and hundreds of other conferences. Full-text search across millions of papers.  
**Key conferences:** IEDM (devices), VLSI Technology (process), ISSCC (circuits), TRANSDUCERS (MEMS).  
**Best for:** Research literature and state-of-art results.

### Journal of Microelectromechanical Systems (JMEMS)
**URL:** https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=84  
**Access:** IEEE subscription required  
**Description:** Top-tier journal for MEMS research. Covers fabrication, modeling, and applications.  
**Best for:** MEMS process development and device characterization.

### IEEE Electron Device Letters (EDL)
**URL:** https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=55  
**Access:** IEEE subscription  
**Description:** Rapid publication of breakthrough device results. Often first publication of new record performance.  
**Best for:** Tracking cutting-edge device research.

### Journal of Vacuum Science and Technology B
**URL:** https://avs.scitation.org/journal/jvb  
**Access:** Subscription required  
**Description:** Covers nanofabrication, lithography, thin films, and vacuum processes.  
**Best for:** Process-focused research and equipment studies.

### Nature Electronics
**URL:** https://www.nature.com/natelectron/  
**Access:** Subscription required  
**Description:** High-impact electronics journal covering emerging devices, 2D materials, neuromorphic computing, and flexible electronics.  
**Best for:** Beyond-CMOS and emerging technology research.

---

## 7. Equipment Vendors and Datasheets

### ASML (Lithography)
**URL:** https://www.asml.com/  
**Resources:** System specifications, technology white papers, and investor presentations (detailed technology roadmaps).  
**Key products:** NXT:2000i (ArF immersion scanner), NXE:3600D (EUV scanner).

### Applied Materials
**URL:** https://www.appliedmaterials.com/  
**Resources:** Process modules library, application notes, and technology briefs covering deposition (CVD, PVD, ALD), etch, and CMP.  
**Key products:** Endura (PVD), Centura (CVD), Producer (etch), Reflexion (CMP).

### Lam Research
**URL:** https://www.lamresearch.com/  
**Resources:** Process application notes for etch and deposition. Extensive library on plasma etch chemistry.  
**Key products:** Kiyo (conductor etch), Flex (dielectric etch), Vector (PECVD).

### Tokyo Electron Limited (TEL)
**URL:** https://www.tel.com/  
**Resources:** Equipment specifications and process capabilities for coater/developers (lithography), etch, and deposition tools.  
**Key products:** CLEAN TRACK (lithography track system), Trias (etch).

### KLA Corporation
**URL:** https://www.kla.com/  
**Resources:** Metrology and inspection technology white papers. Detailed explanations of defect detection and process control.  
**Key products:** Optical inspection, e-beam inspection, thin-film metrology.

### Onto Innovation (formerly Nanometrics + Rudolph)
**URL:** https://www.ontoinnovation.com/  
**Resources:** Metrology application notes covering optical CD, film thickness, and overlay measurement.

### Veeco (ALD/MBE/CMP)
**URL:** https://www.veeco.com/  
**Resources:** ALD process development guides and MBE system specifications.

---

## 8. Open-Source Projects and Foundries

### SkyWater Open-Source PDK (130nm)
**URL:** https://github.com/google/skywater-pdk  
**Description:** First fully open-source process design kit for a commercial foundry. Includes design rules, SPICE models, standard cells, and I/O libraries.  
**Foundry:** SkyWater Technology (Bloomington, MN)  
**Access:** Fully open on GitHub under Apache 2.0 license  
**Best for:** Learning IC design without expensive PDK licenses. Educational use and open-source hardware.

### Google + SkyWater — Open MPW Shuttle
**URL:** https://efabless.com/open_shuttle_program  
**Description:** Free IC fabrication for open-source designs. Submit designs via Efabless platform; Google funds fabrication at SkyWater.  
**Cost:** Free (funded by Google)  
**Best for:** Prototyping open-source ICs without NRE costs.

### Caravel Harness (Open-Source SoC)
**URL:** https://github.com/efabless/caravel  
**Description:** Open-source SoC template with RISC-V processor, GPIO, and user project area. Designed for SkyWater 130nm.  
**Best for:** Building custom SoCs on open-source infrastructure.

### OpenRAM
**URL:** https://openram.org/  
**Description:** Open-source SRAM compiler. Generates layout, netlists, and timing models for custom memory arrays.  
**Best for:** Integrating SRAM into open-source ICs.

### Magic VLSI + PDK Integration
**URL:** http://opencircuitdesign.com/magic/  
**Description:** Magic layout tool with full SkyWater PDK integration. DRC and extraction decks included.  
**Best for:** Complete open-source IC layout flow.

### OpenLane (Automated RTL-to-GDS Flow)
**URL:** https://github.com/The-OpenROAD-Project/OpenLane  
**Description:** Fully automated physical design flow from Verilog RTL to GDS-II layout. Integrates synthesis, placement, routing, and verification.  
**Best for:** Automated digital IC design without commercial EDA tools.

### MOSIS Multi-Project Wafer Service
**URL:** https://www.mosis.com/  
**Description:** Academic and research IC fabrication service. Aggregates small designs onto shared wafer runs at commercial foundries (TSMC, GlobalFoundries, X-FAB).  
**Cost:** $5k–$50k per project depending on node and quantity  
**Best for:** University research and low-volume IC prototyping.

### eFabless Platform
**URL:** https://efabless.com/  
**Description:** Online platform for submitting designs to open MPW shuttles. Provides design verification, submission management, and community support.  
**Best for:** Participating in open-source silicon initiatives.

---

## 9. Professional Organizations

### IEEE (Institute of Electrical and Electronics Engineers)
**URL:** https://www.ieee.org/  
**Membership:** ~$200/year (student discounts available)  
**Benefits:** Access to IEEE Xplore, conference discounts, technical societies (EDS, SSCS), and local chapter events.  
**Best for:** Networking and staying current with research literature.

### SEMI (Semiconductor Equipment and Materials International)
**URL:** https://www.semi.org/  
**Membership:** Varies by membership type  
**Benefits:** Standards access, industry statistics, and networking at SEMICON conferences.  
**Best for:** Equipment suppliers and process engineers.

### SPIE (Optics and Photonics Society)
**URL:** https://www.spie.org/  
**Membership:** ~$125/year  
**Benefits:** Conference proceedings, optical engineering journal access, and lithography conference discounts.  
**Best for:** Lithography and optical MEMS researchers.

### AVS (American Vacuum Society)
**URL:** https://avs.org/  
**Membership:** ~$150/year  
**Benefits:** Journal of Vacuum Science & Technology access, conference discounts, and vacuum technology resources.  
**Best for:** Thin-film deposition and etch researchers.

### MRS (Materials Research Society)
**URL:** https://www.mrs.org/  
**Membership:** ~$140/year  
**Benefits:** Conference access, MRS Bulletin, and materials science networking.  
**Best for:** Materials science and emerging device research.

### Electrochemical Society (ECS)
**URL:** https://www.electrochem.org/  
**Membership:** ~$110/year  
**Benefits:** Journal access, electrochemistry and solid-state science resources.  
**Best for:** Electrochemistry and materials processing.

---

## 10. YouTube Channels and Video Resources

### Asianometry
**URL:** https://www.youtube.com/@Asianometry  
**Description:** Deep-dive video essays on semiconductor history, geopolitics, and technology. Excellent storytelling and research.  
**Best videos:** TSMC history, lithography evolution, semiconductor supply chain.

### Breaking Taps (Machining and Microfabrication)
**URL:** https://www.youtube.com/@BreakingTaps  
**Description:** Hands-on microfabrication tutorials, equipment teardowns, and DIY cleanroom projects.  
**Best for:** Practical fabrication techniques and home experiments.

### Ben Eater (Digital Logic)
**URL:** https://www.youtube.com/@BenEater  
**Description:** Building computers from discrete logic ICs. Excellent for understanding digital fundamentals that underlie VLSI.  
**Best for:** Learning digital logic from first principles.

### Stanford Nanofabrication Facility
**URL:** https://www.youtube.com/@SNFStanford  
**Description:** Equipment training videos, cleanroom safety, and process demonstrations from SNF staff.  
**Best for:** Visual equipment operation tutorials.

### Applied Science
**URL:** https://www.youtube.com/@AppliedScience  
**Description:** DIY science and engineering projects including electron microscopes, ion milling, and microfabrication.  
**Best for:** Hands-on learners interested in building equipment.

### MIT OpenCourseWare
**URL:** https://www.youtube.com/@mitocw  
**Description:** Full lecture recordings of MIT courses including microelectronics, circuits, and device physics.  
**Best for:** Structured university-level courses.

### TechTechPotato (Dr. Ian Cutress)
**URL:** https://www.youtube.com/@TechTechPotato  
**Description:** Semiconductor industry analysis, CPU architecture discussions, and technology deep dives. Former AnandTech senior editor.  
**Best for:** Industry news and architectural analysis.

### High Yield (Semiconductor Podcaster + Video)
**URL:** https://www.youtube.com/@HighYieldYT  
**Description:** Discussions on semiconductor economics, technology trends, and supply chain. Video versions of podcast episodes.  
**Best for:** Business and industry perspective.

---

## 11. Podcasts and Audio Resources

### Acquired (Semiconductor Episodes)
**URL:** https://www.acquired.fm/  
**Description:** Business history podcast with excellent semiconductor company deep dives (TSMC, NVIDIA, Intel, ARM).  
**Best episodes:** TSMC founding story, NVIDIA's rise, Intel's history.  
**Best for:** Business strategy and industry context.

### High Yield
**URL:** https://www.highyieldpodcast.com/  
**Description:** Semiconductor-focused podcast covering foundries, equipment, EDA, and industry trends. Hosted by industry veterans.  
**Best for:** Industry insiders' perspective on technology and business.

### Waveform (ASML and Lithography)
**URL:** Various podcast platforms  
**Description:** Occasional semiconductor episodes covering lithography, EUV, and manufacturing. Part of MKBHD network.  
**Best for:** Accessible introduction to complex topics.

---

## 12. Books and Textbooks

### Fundamentals and Device Physics

**Semiconductor Devices: Physics and Technology** (3rd ed.)  
*S.M. Sze & M.K. Lee*  
ISBN: 978-0470537947  
The definitive textbook on semiconductor device operation. Covers PN junctions, bipolar transistors, MOSFETs, and optoelectronic devices.

**Physics of Semiconductor Devices** (3rd ed.)  
*S.M. Sze & Kwok K. Ng*  
ISBN: 978-0471143239  
Comprehensive 800-page reference covering device physics in exhaustive detail. Graduate-level.

**Modern Semiconductor Devices for Integrated Circuits**  
*Chenming Hu & Chenming Calvin Hu*  
ISBN: 978-0136085256  
Excellent undergraduate/early graduate textbook with clear explanations and problem sets.

### Process Technology

**Silicon Processing for the VLSI Era** (4 volumes)  
*Stanley Wolf & Richard N. Tauber*  
ISBN: Vol 1: 978-0961672140  
The most comprehensive process reference. Vol 1: Process Technology. Vol 2: Process Integration. Vol 3: The Submicron MOSFET. Vol 4: Deep-Submicron Process Technology.

**ULSI Technology**  
*C.Y. Chang & S.M. Sze (editors)*  
ISBN: 978-0071370219  
Advanced process technology textbook covering lithography, oxidation, diffusion, ion implantation, etching, deposition, and integration.

**Microchip Fabrication** (6th ed.)  
*Peter Van Zant*  
ISBN: 978-0071821018  
Accessible introduction to semiconductor manufacturing. Excellent for beginners.

### MEMS and Microfabrication

**Microsystem Design**  
*Stephen D. Senturia*  
ISBN: 978-0792372462  
The standard MEMS textbook. Covers coupled-domain modeling, fabrication, and transduction mechanisms.

**Fundamentals of Microfabrication and Nanotechnology** (3 volumes)  
*Marc J. Madou*  
ISBN: Vol 1: 978-1439895306  
Comprehensive MEMS fabrication reference covering both bulk and surface micromachining.

**Introduction to Microfabrication** (2nd ed.)  
*Sami Franssila*  
ISBN: 978-0470749838  
Excellent practical guide to microfabrication processes with clear diagrams.

### Lithography

**Fundamental Principles of Optical Lithography**  
*Chris A. Mack*  
ISBN: 978-0470018934  
Detailed treatment of lithography optics, resolution, OPC, and photoresist chemistry. Written by industry expert.

**Microlithography: Science and Technology** (2nd ed.)  
*J.R. Sheats & B.W. Smith (editors)*  
ISBN: 978-0824799991  
Multi-author reference covering all aspects of photolithography.

### Reliability and Testing

**Reliability Physics and Engineering**  
*J.W. McPherson*  
ISBN: 978-3319930305  
Comprehensive reliability reference covering TDDB, electromigration, NBTI, hot carrier injection, and acceleration models.

**Microelectronics Failure Analysis Desk Reference** (7th ed.)  
*ASM International (publisher)*  
ISBN: 978-1627082907  
Practical guide to failure analysis techniques, tools, and interpretation.

### History and Industry

**The Chip War**  
*Chris Miller*  
ISBN: 978-1982172008  
2022 book covering semiconductor geopolitics, supply chain, and strategic importance. Excellent industry context.

**The Innovators**  
*Walter Isaacson*  
ISBN: 978-1476708706  
History of computing from vacuum tubes to silicon Valley, covering transistor invention and IC development.

---

## Quick-Access Resource Index

| Need | Resource | Access |
|------|----------|--------|
| Learn device physics | MIT OCW + Sze textbook | Free + $50–100 |
| Process simulation | Sentaurus TCAD or ngspice | License or free |
| Material properties | NIST + Ioffe database | Free |
| Industry news | SemiEngineering + EE Times | Free |
| Standards | JEDEC (free) + SEMI (paid) | Mixed |
| Open-source IC design | SkyWater PDK + Magic + OpenLane | Free |
| MEMS foundry comparison | MEMS Exchange | Free |
| Research papers | IEEE Xplore | Institutional access |
| Equipment datasheets | Vendor websites (Applied, Lam, ASML) | Free registration |
| YouTube learning | Asianometry + Breaking Taps + Applied Science | Free |

---

## Contributing to This List

Found a broken link? Know of an excellent resource not listed here? This document is part of the open Silicon Fabrication Handbook project.

**How to contribute:**
1. Open an issue on the GitHub repository
2. Submit a pull request with additions/corrections
3. Include: URL, description, access requirements, and why it's useful

**Criteria for inclusion:**
- High-quality, authoritative content
- Actively maintained (for databases and tools)
- Free or widely accessible via institutional subscriptions
- Relevant to semiconductor or MEMS fabrication

---

*Part of the Silicon Fabrication Handbook — [github.com/Zeyad-Mustafa/silicon-fabrication-handbook](https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook)*  
*Last updated: February 2026*