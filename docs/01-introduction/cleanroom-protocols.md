# Cleanroom Protocols and Best Practices

## Table of Contents
- [Introduction](#introduction)
- [Understanding Cleanroom Classification](#understanding-cleanroom-classification)
  - [ISO 14644-1 Standards](#iso-14644-1-standards)
  - [Particle Size Impact](#particle-size-impact)
- [Cleanroom Design and Airflow](#cleanroom-design-and-airflow)
  - [HEPA and ULPA Filtration](#hepa-and-ulpa-filtration)
  - [Airflow Patterns](#airflow-patterns)
  - [Pressure Cascade](#pressure-cascade)
  - [Air Changes Per Hour (ACH)](#air-changes-per-hour-ach)
- [Gowning Procedures](#gowning-procedures)
  - [Personal Preparation (Before Gowning)](#personal-preparation-before-gowning)
  - [Step-by-Step Gowning (ISO 5 Protocol)](#step-by-step-gowning-iso-5-protocol)
  - [Gown Integrity Checks](#gown-integrity-checks)
- [Cleanroom Behavior and Movement](#cleanroom-behavior-and-movement)
  - [The Golden Rules](#the-golden-rules)
  - [Movement Guidelines](#movement-guidelines)
  - [Communication](#communication)
  - [Material Handling](#material-handling)
  - [Wafer Handling Protocol](#wafer-handling-protocol)
- [Contamination Control](#contamination-control)
  - [Sources of Contamination](#sources-of-contamination)
  - [Monitoring and Control](#monitoring-and-control)
  - [Cleaning Protocols](#cleaning-protocols)
  - [Sticky Mats](#sticky-mats)
- [Electrostatic Discharge (ESD) Control](#electrostatic-discharge-esd-control)
  - [Why ESD Matters](#why-esd-matters)
  - [ESD Protection Measures](#esd-protection-measures)
- [Emergency Procedures](#emergency-procedures)
  - [Contamination Events](#contamination-events)
  - [Equipment Failures](#equipment-failures)
- [Quality Assurance and Audits](#quality-assurance-and-audits)
  - [Self-Monitoring](#self-monitoring)
  - [External Audits](#external-audits)
  - [Continuous Improvement](#continuous-improvement)
- [Training and Certification](#training-and-certification)
  - [Initial Training](#initial-training)
  - [Ongoing Training](#ongoing-training)
- [Best Practices Summary](#best-practices-summary)
  - [DO's](#dos)
  - [DON'Ts](#donts)
- [Conclusion](#conclusion)
- [Further Reading](#further-reading)

## Introduction

Cleanroom protocols are critical for maintaining the contamination-free environment necessary for semiconductor and MEMS fabrication. A single particle or contaminant can destroy an entire wafer batch worth millions of dollars. This chapter covers essential cleanroom procedures, gowning protocols, behavior guidelines, and contamination control strategies.

## Understanding Cleanroom Classification

### ISO 14644-1 Standards

Cleanrooms are classified by the number of particles per cubic meter of air:

| ISO Class | Particles/m³ (≥0.5μm) | Particles/ft³ (≥0.5μm) | Typical Application |
|-----------|----------------------|----------------------|---------------------|
| ISO 1 | 10 | 0.283 | Extreme precision (theoretical) |
| ISO 2 | 100 | 2.83 | Advanced photolithography |
| ISO 3 | 1,000 | 28.3 | Critical lithography steps |
| ISO 4 | 10,000 | 283 | Advanced IC fabrication |
| ISO 5 | 100,000 | 2,830 | Standard IC production |
| ISO 6 | 1,000,000 | 28,300 | Packaging, assembly |
| ISO 7 | 10,000,000 | 283,000 | Pre-cleanroom gowning area |
| ISO 8 | 100,000,000 | 2,830,000 | Gowning room entry |

**Context**: Normal outdoor air is approximately **35,000,000,000 particles/m³** (ISO 9 or worse)

### Particle Size Impact

Different features require different cleanliness levels:

| Technology Node | Critical Dimension | Max Particle Size | Required ISO Class |
|-----------------|-------------------|-------------------|-------------------|
| 7nm | 7nm | <50nm | ISO 1-2 (litho) |
| 28nm | 28nm | <140nm | ISO 2-3 |
| 90nm | 90nm | <450nm | ISO 3-4 |
| 180nm | 180nm | <900nm | ISO 4-5 |
| MEMS (10μm) | 10μm | <5μm | ISO 5-6 |

**Rule of Thumb**: Kill particle size should be less than **1/10th** of the critical dimension

## Cleanroom Design and Airflow

### HEPA and ULPA Filtration

**HEPA Filters** (High Efficiency Particulate Air):
- Removes ≥99.97% of particles ≥0.3μm
- Standard for ISO 5-7 cleanrooms
- Flow rate: 0.3-0.5 m/s (90 fpm)

**ULPA Filters** (Ultra-Low Penetration Air):
- Removes ≥99.999% of particles ≥0.12μm
- Required for ISO 3-4 cleanrooms
- Critical for advanced nodes (<28nm)

### Airflow Patterns

**Laminar Flow** (Unidirectional):
```
         ╔═══════════════════════╗
         ║   HEPA Filter Array   ║
         ╚═══════════════════════╝
              ↓↓↓↓↓↓↓↓↓↓↓
         ┌───────────────────────┐
         │                       │
         │   Clean Work Zone     │
         │   (ISO 3-5)           │
         │                       │
         └───────────────────────┘
              ↓↓↓↓↓↓↓↓↓↓↓
         ┌───────────────────────┐
         │   Perforated Floor    │
         │   Return Air Plenum   │
         └───────────────────────┘
```

- **Velocity**: 0.3-0.5 m/s vertically downward
- **Coverage**: 100% ceiling HEPA filters
- **Application**: Critical process tools, lithography bays

**Turbulent Flow** (Non-Unidirectional):
- Mixed air circulation
- Lower cost than laminar
- Suitable for ISO 6-8 areas
- Common in gowning rooms, corridors

### Pressure Cascade

Cleanrooms maintain **positive pressure** relative to less clean areas:

```
Critical Fab Area (ISO 4):  +20 Pa
    ↓ (pressure gradient)
Sub-Fab / Equipment Area:   +15 Pa
    ↓
General Cleanroom (ISO 5):  +10 Pa
    ↓
Gowning Room (ISO 7):       +5 Pa
    ↓
Entrance / Corridor:        0 Pa (ambient)
```

**Purpose**: Prevents contaminated air from entering cleaner areas

### Air Changes Per Hour (ACH)

| ISO Class | Minimum ACH | Typical ACH |
|-----------|-------------|-------------|
| ISO 3-4 | 500-600 | 600-800 |
| ISO 5 | 300-400 | 400-600 |
| ISO 6 | 100-150 | 150-250 |
| ISO 7 | 60-90 | 80-120 |

**Calculation**: 
```
ACH = (Air Volume Supplied per Hour) / (Room Volume)
```

## Gowning Procedures

### Personal Preparation (Before Gowning)

**Prohibited Items**:
-   Cosmetics, perfumes, colognes (particle sources)
-   Jewelry (except plain wedding bands)
-   Watches (unless approved for cleanroom)
-   Hair products, gels, sprays
-   Contact lens solution (use before entry)
-   Loose paper, cardboard
-   Food, drinks, gum, candy
-   Pencils (use cleanroom pens only)

**Personal Hygiene**:
- Wash hands thoroughly with soap
- Dry hands completely
- Tie back long hair
- Remove or secure loose clothing items

### Step-by-Step Gowning (ISO 5 Protocol)

**Location**: Gowning Room (ISO 7-8 area)

#### 1. Footwear

**Option A: Cleanroom Shoes**
```
1. Step on sticky mat at entrance
2. Put on dedicated cleanroom shoes
3. Never wear outside shoes in gowning area
```

**Option B: Shoe Covers**
```
1. Step on sticky mat
2. Sit on bench with legs not touching cleanroom side
3. Put shoe cover on one foot
4. Place covered foot on cleanroom side of bench
5. Repeat for second foot
6. Stand up fully on cleanroom side
```

#### 2. Hair Cover (Bouffant Cap or Hood)

```
1. Put on bouffant cap covering all hair
2. Ensure no hair is exposed
3. Tuck in completely around ears
4. For beards: Use beard cover (snood)
```

**Critical**: Hair is a major contamination source (sheds 50-100 hairs/day, each releasing particles)

#### 3. Cleanroom Suit (Bunny Suit)

**Types**:
- **One-piece coverall**: Most common, best protection
- **Two-piece**: Smock + pants, easier to don
- **Material**: Polyester, Tyvek, or specialized fabrics

**Donning Procedure**:
```
1. Remove cleanroom suit from dispenser/hook
2. Inspect for tears or damage
3. Step into suit one leg at a time
4. Pull up over body
5. Insert arms into sleeves
6. Zip/snap front closure completely
7. Ensure suit covers all street clothing
```

**Fit Check**:
- No skin exposed at wrists or ankles
- Comfortable but not loose
- All closures secured

#### 4. Gloves (First Pair - Under Suit)

```
1. Select correct size nitrile gloves
2. Put on first pair
3. Tuck glove cuffs UNDER suit sleeves
4. Ensure no skin gap between glove and sleeve
```

#### 5. Face Mask

```
1. Position mask over nose and mouth
2. Secure elastic straps (or ties) around head
3. Mold nose clip to face
4. Ensure no gaps around edges
5. Breathe normally to check seal
```

**Types**:
- **Surgical mask**: General use, ISO 6-7
- **N95/FFP2**: Better filtration, ISO 4-5
- **Full-face hood**: Integrated with suit for ISO 3-4

#### 6. Safety Glasses / Goggles (If Required)

```
1. Put on safety glasses
2. Ensure comfortable fit
3. Check for fogging (anti-fog coating)
4. Adjust over mask if worn
```

#### 7. Second Gloves (Over Suit)

```
1. Put on second pair of gloves
2. Pull glove cuffs OVER suit sleeves
3. This creates double-barrier protection
4. Secure with tape if protocol requires
```

#### 8. Final Inspection

```
□ All hair covered
□ Face mask secure with no gaps
□ Suit fully zipped/closed
□ Gloves cover all wrist areas
□ No skin visible except face (if mask only)
□ No street clothing visible
□ Badge visible (if required)
```

### Gown Integrity Checks

**Before Each Entry**:
- Visual inspection for tears or holes
- Check zipper/snap closures
- Verify glove integrity (stretch test)
- Ensure proper coverage at wrists and ankles

**Gown Lifetime**:
- **Disposable suits**: Single use or single shift
- **Reusable suits**: 20-50 washes (depends on material)
- **Contamination event**: Immediate replacement

## Cleanroom Behavior and Movement

### The Golden Rules

1. **Minimize Movement**: Every movement generates particles
2. **Slow and Deliberate**: Fast movements create turbulence
3. **Minimize Talking**: Speech generates particles
4. **No Touching Face**: Breaks contamination barrier
5. **Stay Away from Wafers**: Maintain minimum 12" distance

### Movement Guidelines

**Walking**:
- Walk slowly and smoothly (no running)
- Avoid sudden stops or direction changes
- Typical speed: 0.5 m/s (1 mph)
- Use designated walkways

**Reaching**:
- Avoid reaching over open wafers or equipment
- Keep arms below shoulder level when possible
- Use tools/handlers to manipulate wafers

**Particle Generation by Activity**:

| Activity | Particles Generated (particles/min) |
|----------|-------------------------------------|
| Standing still | ~100,000 |
| Sitting | ~500,000 |
| Slow walking | ~5,000,000 |
| Fast walking | ~10,000,000 |
| Arm movement | ~2,000,000 per movement |

### Communication

**Talking**:
- Minimize verbal communication
- Speak quietly and briefly
- Face AWAY from wafers/equipment
- Use electronic communication when possible

**Particle Release from Speech**:
- Normal speech: 100-1,000 particles per second
- Loud speech: 10,000+ particles per second
- Distance: Particles can travel 1-2 meters

**Best Practice**: Use intercom systems, chat, or email instead of talking

### Material Handling

**Approved Materials**:
-   Cleanroom paper (polyester-based)
-   Cleanroom pens (sealed, non-shedding)
-   Cleanroom wipes (polyester)
-   Stainless steel tools
-   PTFE/Teflon containers
-   Sealed electronic devices

**Prohibited Materials**:
-   Wood (sheds fibers)
-   Cardboard (particle source)
-   Regular paper (generates dust)
-   Pencils (graphite particles)
-   Latex (contains powder)
-   Natural fabrics (cotton, wool)

### Wafer Handling Protocol

**Basic Rules**:
1. **Never touch wafer surface**: Handle by edges only
2. **Use tweezers/vacuum wands**: Proper handling tools
3. **Transport in carriers**: SMIF pods, FOUP containers
4. **Minimize exposure**: Open carriers only when necessary

**Handling Technique**:
```
Correct Edge Grip:
        ___________________
       /                   \
      |                     |
   →  |  [Handle at edge]   |  ←
      |     [notch]         |
       \___________________/
       
Contact points: Edge only, away from device area
Angle: 5-10° tilt maximum
Duration: Minimal exposure time
```

## Contamination Control

### Sources of Contamination

#### 1. Personnel (80% of contamination)

**Skin**:
- Sheds 30,000-40,000 dead skin cells per minute
- Each cell can carry bacteria and particles
- Mitigation: Complete gowning coverage

**Hair**:
- Sheds 50-100 hairs per day
- Each hair releases thousands of particles
- Mitigation: Hair covers, hoods

**Breath/Saliva**:
- Droplets contain bacteria, salts, proteins
- Size: 0.5-100μm
- Mitigation: Face masks, minimize talking

#### 2. Equipment (10% of contamination)

**Mechanical Parts**:
- Bearings, motors generate particles
- Wear debris from moving components
- Mitigation: Sealed systems, HEPA filters at tools

**Vacuum Pumps**:
- Oil backstreaming
- Mitigation: Traps, isolation valves

#### 3. Process Materials (5% of contamination)

**Chemicals**:
- Impurities in precursors
- Residues from previous processes
- Mitigation: High-purity chemicals, cleaning protocols

**Gases**:
- Particulates in supply lines
- Mitigation: Point-of-use filters (0.003μm)

#### 4. Ambient Environment (5% of contamination)

**External Air**:
- Infiltration through doors, gaps
- Mitigation: Positive pressure, airlocks

### Monitoring and Control

#### Particle Counters

**Locations**:
- Process tool exhaust
- Critical work areas
- Return air plenums
- Gowning room

**Measurement**:
- Real-time monitoring: 1 minute intervals
- Alarm thresholds: 150% of baseline
- Data logging: Continuous recording

**Typical Setup**:
```
Laser Particle Counter
    ↓ (samples air at 28.3 L/min)
Channels:
  - 0.3 μm
  - 0.5 μm  ← ISO classification
  - 1.0 μm
  - 5.0 μm
    ↓
Computer logging system
    ↓
Alert if threshold exceeded
```

#### Environmental Monitoring

**Parameters**:

| Parameter | Typical Range | Tolerance | Monitoring Frequency |
|-----------|--------------|-----------|---------------------|
| Temperature | 20-22°C | ±0.5°C | Continuous |
| Humidity | 40-45% RH | ±2% | Continuous |
| Pressure | +10 to +20 Pa | ±2 Pa | Continuous |
| Air velocity | 0.3-0.5 m/s | ±10% | Weekly |

**Temperature Control Importance**:
- Photoresist coating uniformity
- Lithography overlay accuracy
- Equipment thermal stability

**Humidity Control Importance**:
- Static charge control (ESD)
- Photoresist adhesion
- Oxide growth rates

### Cleaning Protocols

#### Daily Cleaning

**Floors**:
```
1. Vacuum with HEPA-filtered vacuum
2. Wet mop with cleanroom-grade mop
3. Use approved cleaning solution (IPA/DI water)
4. Allow to air dry
```

**Surfaces**:
```
1. Wipe down with cleanroom wipes
2. Use 70% IPA solution
3. Wipe in one direction only
4. Replace wipes frequently
```

**Equipment Exteriors**:
```
1. Daily wipe-down of tool surfaces
2. Check for leaks or damage
3. Clean viewing windows
4. Vacuum around tool base
```

#### Weekly Cleaning

- Detailed equipment cleaning
- Wall and ceiling inspection
- HEPA filter check (pressure drop)
- Sticky mat replacement
- Tool maintenance areas

#### Monthly Cleaning

- Deep cleaning of all surfaces
- Filter replacement if needed
- Ceiling tile inspection
- Lighting fixture cleaning
- Gowning room deep clean

### Sticky Mats

**Purpose**: Remove particles from shoe bottoms

**Placement**:
- Cleanroom entrances
- Between ISO class transitions
- Equipment entry points

**Maintenance**:
- Peel off top layer when contaminated
- Replace mat when down to last few layers
- Typical life: 30-60 layers, 1-2 weeks

## Electrostatic Discharge (ESD) Control

### Why ESD Matters

**Damage Mechanisms**:
- Gate oxide rupture: <100V can damage
- Junction shorting: Melts silicon
- Latent damage: Devices fail later

**Sensitivity Levels**:
- **Class 0**: <50V (highly sensitive)
- **Class 1**: 50-250V (sensitive)
- **Class 2**: 250-1000V (moderately sensitive)
- **Class 3**: >1000V (less sensitive)

Modern CMOS: Typically Class 1 (HBM = 100-250V)

### ESD Protection Measures

#### 1. Grounding

**Personnel Grounding**:
```
Person → Wrist strap (1 MΩ resistor) → Ground point
        OR
Person → ESD shoes + Conductive floor → Ground
```

**Wrist Strap Testing**:
- Test before each shift
- Acceptable range: 0.75-1.25 MΩ to ground
- Test stations at cleanroom entrance

#### 2. Conductive/Dissipative Materials

**Floor**:
- Conductive vinyl tile (10⁴-10⁶ Ω)
- Epoxy coating with conductive additive
- Resistance to ground: <1 MΩ

**Work Surfaces**:
- Dissipative mats (10⁶-10⁹ Ω surface resistivity)
- Grounded through 1 MΩ resistor

**Containers**:
- Conductive or dissipative plastics
- Black color indicates carbon-doped material

#### 3. Ionization

**Air Ionizers**:
- Neutralize static charge in air
- Balanced ion output (positive and negative)
- Typical range: 30-50 cm from source
  
**Locations**:
- Near wafer handling stations
- Critical assembly areas
- Tool load ports

#### 4. Humidity Control

**Optimal Range**: 40-50% RH
- Below 30%: Static buildup increases
- Above 60%: Moisture issues (corrosion, contamination)

**Mechanism**: Higher humidity allows charge dissipation through air

## Emergency Procedures

### Contamination Events

#### Major Particle Release

**Symptoms**:
- Visible particles in air
- Particle counter alarm
- Process tool malfunction

**Response**:
```
1. Stop all wafer processing immediately
2. Close tool loading doors
3. Alert facility management
4. Evacuate affected area if severe
5. Allow air filtration system to run (30+ minutes)
6. Re-verify particle counts before resuming
7. Inspect/quarantine affected wafers
```

#### Chemical Spill

**Minor Spill** (<1 liter):
```
1. Alert nearby personnel
2. Ventilate area (increase exhaust)
3. Use spill kit (absorbent pads)
4. Dispose in proper waste container
5. Document incident
```

**Major Spill** (>1 liter):
```
1. Activate emergency alarm
2. Evacuate immediate area
3. Call emergency response team
4. Shut down equipment if safe to do so
5. Do not attempt cleanup without training
```

### Equipment Failures

#### HVAC System Failure

**Immediate Actions**:
```
1. Particle counters will alarm
2. Stop critical processes (litho, thin film)
3. Close tool load locks
4. Notify facility engineering
5. Do not open cleanroom doors (pressure loss)
```

**Recovery**:
- Verify particle counts return to normal
- Check temperature and humidity stability
- Resume operations after 30-minute stable period

#### Fire

**Response**:
```
1. Activate fire alarm
2. Evacuate using designated routes
3. Close cleanroom doors
4. Do not use elevators
5. Assemble at muster point
6. Account for all personnel
```

**Cleanroom Considerations**:
- Halon/FM-200 suppression systems in some fabs
- Know location of fire extinguishers
- Never fight chemical fires without training

## Quality Assurance and Audits

### Self-Monitoring

**Daily Checks**:
- [ ] Gowning inspection in mirror
- [ ] Wrist strap test
- [ ] Work area cleanliness
- [ ] Particle counter readings
- [ ] Chemical waste levels

**Weekly Tasks**:
- Review training on protocols
- Report any equipment issues
- Suggest process improvements

### External Audits

**Internal Audits** (Monthly):
- Facility management inspection
- Protocol compliance review
- Training verification
- Documentation check

**Certification Audits** (Yearly):
- ISO 14644 compliance testing
- HEPA filter integrity tests
- Airflow velocity measurements
- Particle count verification

### Continuous Improvement

**Kaizen Events**:
- Regular team meetings
- Identify contamination sources
- Implement corrective actions
- Track metrics over time

**Metrics to Track**:
- Particle counts (trend analysis)
- Yield correlation with contamination
- Gowning violation rates
- Training compliance

## Training and Certification

### Initial Training

**Topics**:
1. Cleanroom theory and classification
2. Contamination sources and control
3. Gowning procedures (hands-on)
4. Behavior and movement guidelines
5. ESD awareness and practices
6. Emergency procedures
7. Chemical safety basics

**Duration**: Typically 2-4 hours classroom + practical

**Certification**:
- Written test (80% passing score)
- Practical gowning demonstration
- Valid for 1 year (recertification required)

### Ongoing Training

**Quarterly Refreshers**:
- Protocol updates
- Incident reviews
- Best practices sharing
- New equipment training

**Annual Recertification**:
- Full protocol review
- Updated test
- Practical demonstration

## Best Practices Summary

### DO's  

-   Always follow gowning procedures completely
-   Move slowly and deliberately
-   Keep hands below shoulder level
-   Use proper wafer handling tools
-   Report all contamination events immediately
-   Maintain situational awareness
-   Follow traffic patterns and designated paths
-   Test wrist strap before starting work
-   Clean work areas before and after use
-   Ask questions if unsure about procedures

### DON'Ts  

-   Never run in the cleanroom
-   Never touch your face or adjust gown
-   Never lean or reach over open wafers
-   Never wear jewelry (except plain bands)
-   Never bring unauthorized materials inside
-   Never eat, drink, or chew gum
-   Never wear cosmetics or fragrances
-   Never skip gowning steps
-   Never use unapproved cleaning materials
-   Never ignore alarms or warnings

## Conclusion

Cleanroom protocols are not arbitrary rules—they are essential practices that ensure product quality, process reliability, and personnel safety. Mastery of these protocols distinguishes professional fabrication engineers from novices. Remember:

> **"In the cleanroom, discipline equals yield, and yield equals success."**

By consistently following these protocols, you contribute to the success of the entire fabrication team and the quality of the products manufactured.

## Further Reading

1. **ISO 14644-1:2015** - Classification of air cleanliness by particle concentration
2. **ISO 14644-2:2015** - Monitoring to provide evidence of cleanroom performance
3. **IEST-RP-CC001.6** - Cleanroom testing and monitoring
4. **SEMI S2** - Safety guidelines for semiconductor manufacturing equipment

---

**Next Chapter**: [Wafer Fundamentals](wafer-fundamentals.md) - Deep dive into silicon wafer properties and specifications
