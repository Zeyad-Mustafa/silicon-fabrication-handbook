# Safety Guidelines for Semiconductor Fabrication

## Table of Contents
- [Introduction](#introduction)
- [Hierarchy of Safety Controls](#hierarchy-of-safety-controls)
- [Chemical Safety](#chemical-safety)
  - [Hazard Classification](#hazard-classification)
  - [Chemical Storage](#chemical-storage)
  - [Personal Protective Equipment (PPE)](#personal-protective-equipment-ppe)
  - [Emergency Response](#emergency-response)
  - [Safety Showers and Eyewash Stations](#safety-showers-and-eyewash-stations)
- [Electrical Safety](#electrical-safety)
  - [High-Voltage Hazards](#high-voltage-hazards)
  - [Lockout/Tagout (LOTO)](#lockouttagout-loto)
  - [Electrical PPE](#electrical-ppe)
- [Laser Safety](#laser-safety)
  - [Laser Classifications](#laser-classifications)
  - [Laser Safety Measures](#laser-safety-measures)
- [Radiation Safety](#radiation-safety)
  - [Ionizing Radiation](#ionizing-radiation)
  - [Non-Ionizing Radiation](#non-ionizing-radiation)
- [Cryogenic Safety](#cryogenic-safety)
  - [Liquid Nitrogen (LN₂)](#liquid-nitrogen-ln₂)
- [Mechanical Hazards](#mechanical-hazards)
  - [Rotating Equipment](#rotating-equipment)
  - [Compressed Gases](#compressed-gases)
- [Confined Space Entry](#confined-space-entry)
- [Ergonomics and Repetitive Strain](#ergonomics-and-repetitive-strain)
  - [Wafer Handling](#wafer-handling)
  - [Cleanroom Ergonomics](#cleanroom-ergonomics)
- [Noise Exposure](#noise-exposure)
- [Environmental Safety](#environmental-safety)
  - [Waste Management](#waste-management)
  - [Sustainability](#sustainability)
- [Emergency Preparedness](#emergency-preparedness)
  - [Fire Safety](#fire-safety)
  - [Earthquake Preparedness (Seismic Zones)](#earthquake-preparedness-seismic-zones)
  - [Medical Emergencies](#medical-emergencies)
- [Training and Certification](#training-and-certification)
  - [Required Training](#required-training)
  - [Safety Data Sheets (SDS)](#safety-data-sheets-sds)
- [Regulatory Compliance](#regulatory-compliance)
  - [Key Regulations (US)](#key-regulations-us)
- [Safety Culture](#safety-culture)
  - [Personal Responsibility](#personal-responsibility)
- [Conclusion](#conclusion)
- [Emergency Contact Information](#emergency-contact-information)
- [Further Resources](#further-resources)

## Introduction

Semiconductor fabrication facilities use some of the most hazardous materials and processes in any industrial setting. Toxic gases, corrosive acids, high-voltage equipment, and cleanroom environments all require strict safety protocols. This chapter covers comprehensive safety guidelines to protect personnel, equipment, and the environment.

> ** CRITICAL**: Safety is never optional. A single safety violation can result in injury, death, equipment damage, or environmental harm. When in doubt, STOP and ask.

## Hierarchy of Safety Controls

Follow this hierarchy (most to least effective):

1. **Elimination**: Remove the hazard entirely
2. **Substitution**: Replace with a safer alternative
3. **Engineering Controls**: Ventilation, interlocks, barriers
4. **Administrative Controls**: Procedures, training, signage
5. **Personal Protective Equipment (PPE)**: Last line of defense

## Chemical Safety

### Hazard Classification

#### Corrosives (Acids and Bases)

**Hydrofluoric Acid (HF)** - ⚠️ EXTREME HAZARD
- **Concentration**: 1-49%
- **Use**: Oxide etching, cleaning
- **Hazards**:
  - Penetrates skin rapidly without immediate pain
  - Dissolves tissue and leaches calcium from bones
  - Can cause cardiac arrest (Ca²⁺ binding)
  - Fatal dose: 2% body surface area (50% HF)
- **First Aid**:
  - Flush with water immediately (15+ minutes)
  - Apply calcium gluconate gel
  - Seek medical attention IMMEDIATELY
  - Monitor for 24 hours (delayed symptoms)

**Sulfuric Acid (H₂SO₄)**
- **Concentration**: 95-98%
- **Use**: Piranha clean, resist stripping
- **Hazards**:
  - Severe burns on contact
  - Generates heat when mixed with water
  - Destroys organic materials
- **First Aid**:
  - Flush with copious water (20 minutes)
  - Remove contaminated clothing
  - Seek medical attention

**Nitric Acid (HNO₃)**
- **Concentration**: 65-70%
- **Use**: Metal etching, cleaning
- **Hazards**:
  - Oxidizing agent (fire risk)
  - Produces toxic NO₂ fumes
  - Causes yellow staining of skin
- **First Aid**: Flush with water, medical attention

**Phosphoric Acid (H₃PO₄)**
- **Concentration**: 85%, used hot (160-180°C)
- **Use**: Silicon nitride etching
- **Hazards**:
  - Burns (thermal + chemical)
  - Splash hazard when hot
- **Safety**: Heat-resistant face shield, long gloves

**Sodium Hydroxide (NaOH) / Potassium Hydroxide (KOH)**
- **Concentration**: 20-45%
- **Use**: Wet etching, cleaning
- **Hazards**:
  - Severe caustic burns
  - Eye damage (blindness risk)
  - Dissolves fats, proteins
- **First Aid**: Flush with water (20 minutes), medical attention

**Ammonium Hydroxide (NH₄OH)**
- **Concentration**: 29%
- **Use**: RCA SC-1 clean
- **Hazards**:
  - Corrosive vapor
  - Eye and respiratory irritant

**Hydrogen Peroxide (H₂O₂)**
- **Concentration**: 30-50%
- **Use**: Piranha, RCA cleans, oxidizer
- **Hazards**:
  - Strong oxidizer
  - Skin bleaching/burns
  - Can decompose explosively if contaminated
- **Storage**: Cool, dark, vented

#### Toxic Gases - ☠️ EXTREME HAZARD

**Arsine (AsH₃)**
- **Use**: Arsenic doping
- **Hazards**:
  - Extremely toxic (TLV: 0.05 ppm)
  - Hemolytic (destroys red blood cells)
  - Colorless, garlic-like odor
  - Fatal at 25-50 ppm for 30 minutes
- **Detection**: Continuous monitors, <0.01 ppm alarm
- **Controls**: Double-wall piping, gas cabinets, scrubbers

**Phosphine (PH₃)**
- **Use**: Phosphorus doping
- **Hazards**:
  - Highly toxic (TLV: 0.3 ppm)
  - Pulmonary edema, cardiovascular effects
  - Spontaneously flammable in air (>100°C)
- **Detection**: Continuous monitoring
- **Controls**: Inert purge, flame arrestors

**Diborane (B₂H₆)**
- **Use**: Boron doping
- **Hazards**:
  - Highly toxic (TLV: 0.1 ppm)
  - Spontaneously flammable in moist air
  - Pulmonary irritant
- **Controls**: Scrubbers, leak detection

**Silane (SiH₄)**
- **Use**: Silicon deposition
- **Hazards**:
  - Pyrophoric (spontaneously ignites)
  - Explosive with air (1.5-98%)
  - Moderate toxicity
- **Controls**: Inert gas dilution, flame detectors

**Chlorine (Cl₂)**
- **Use**: Plasma etching
- **Hazards**:
  - Severe respiratory irritant (TLV: 0.5 ppm)
  - Pulmonary edema
  - Greenish-yellow gas
- **First Aid**: Fresh air, oxygen, medical attention

**Ammonia (NH₃)**
- **Use**: Nitride deposition, cleaning
- **Hazards**:
  - Corrosive to respiratory system (TLV: 25 ppm)
  - Eye irritant (0.5 ppm)
  - Pungent odor
- **Detection**: Odor threshold 5-50 ppm

#### Flammable Solvents

**Acetone (CH₃COCH₃)**
- **Use**: Photoresist removal, cleaning
- **Flash Point**: -20°C
- **Hazards**: Extremely flammable, narcotic at high conc.
- **Storage**: Flammable cabinet, grounded containers

**Isopropanol (IPA, C₃H₇OH)**
- **Use**: Cleaning, drying
- **Flash Point**: 12°C
- **Hazards**: Flammable, skin drying
- **Storage**: Flammable cabinet

**Methanol (CH₃OH)**
- **Use**: Cleaning, etchant
- **Hazards**: Toxic, can cause blindness
- **TLV**: 200 ppm

**N-Methyl-2-Pyrrolidone (NMP)**
- **Use**: Photoresist stripping
- **Hazards**: Reproductive toxin, skin absorption
- **PPE**: Nitrile gloves, good ventilation

### Chemical Storage

#### Segregation Requirements

**Incompatible Groups** (NEVER store together):

1. **Acids**: HF, H₂SO₄, HNO₃, H₃PO₄
2. **Bases**: NaOH, KOH, NH₄OH
3. **Oxidizers**: H₂O₂, HNO₃, Cl₂
4. **Flammables**: Acetone, IPA, methanol
5. **Toxics**: Separate from all

**Example Reaction** (if mixed):
```
H₂SO₄ + H₂O₂ → Piranha solution (violently exothermic)
Acids + Bases → Heat + splashing
Oxidizers + Organics → Fire/explosion
```

#### Storage Requirements

**Acid Cabinet**:
- Corrosion-resistant (polyethylene or coated steel)
- Bottom containment tray (120% volume)
- Ventilation: 0.5 m/s face velocity
- Segregate by type (organic/inorganic, oxidizing/non-oxidizing)

**Flammable Cabinet**:
- UL/FM approved, self-closing doors
- Grounding strap for static discharge
- Limit: 60 gallons per cabinet
- Signage: "FLAMMABLE - KEEP FIRE AWAY"

**Gas Cabinet**:
- Ventilated enclosure (150+ fpm face velocity)
- Explosion-proof electrical
- Gas detection with auto-shutoff
- Seismic restraints (earthquake zones)

### Personal Protective Equipment (PPE)

#### Minimum PPE for Chemical Work

**Base Layer**:
- [ ] Safety glasses with side shields
- [ ] Cleanroom garment (chemical-resistant if handling directly)
- [ ] Nitrile gloves (double-glove for acids)
- [ ] Closed-toe shoes (chemical-resistant preferred)

**Enhanced PPE for Concentrated Acids/Bases**:
- [ ] Face shield (over safety glasses)
- [ ] Acid-resistant apron or coat
- [ ] Neoprene or butyl rubber gloves (over nitrile)
- [ ] Sleeve protectors
- [ ] Chemical-resistant boots (for large volumes)

#### Glove Selection Chart

| Chemical | Compatible Gloves | Not Recommended |
|----------|------------------|-----------------|
| HF (dilute) | Neoprene (>0.7mm) | Latex, PVC |
| H₂SO₄ | Neoprene, butyl rubber | Nitrile alone |
| Solvents (acetone, IPA) | Nitrile | Latex |
| NaOH/KOH | Neoprene, nitrile | Natural rubber |
| Photoresist | Nitrile | PVC |

**Breakthrough Time**: Replace gloves per manufacturer specs (typically 15-60 min for acids)

### Emergency Response

#### Chemical Spill Response

**Minor Spill** (<100 mL):
```
1. Alert nearby personnel
2. Don appropriate PPE
3. Neutralize if applicable:
   - Acid spills → Sodium bicarbonate
   - Base spills → Citric acid or weak acid
4. Absorb with spill pads
5. Dispose in proper waste container
6. Document incident
```

**Major Spill** (>100 mL or toxic gas):
```
1. Evacuate area immediately
2. Activate emergency alarm
3. Call emergency response team (dial XXX)
4. Close doors to contain (if safe)
5. Do NOT attempt cleanup
6. Provide MSDS to responders
7. Account for all personnel
```

#### Personal Contamination

**Chemical Splash on Skin/Eyes**:
```
1. IMMEDIATELY go to nearest safety shower/eyewash
2. Activate shower/eyewash
3. Remove contaminated clothing (while rinsing)
4. Flush for 15 minutes minimum (eyes: 20 minutes)
5. Call for medical assistance
6. Continue rinsing until help arrives
7. For HF: Apply calcium gluconate gel after rinsing
```

**Do NOT**:
- Attempt to neutralize acids/bases on skin (generates heat)
- Rub eyes
- Use chemical neutralizers without training

#### Gas Leak Response

**Toxic Gas Alarm**:
```
1. Evacuate immediately (no delays)
2. Exit upwind if outdoors
3. Help others evacuate
4. Close doors behind you (if safe)
5. Assemble at muster point
6. Account for all personnel
7. Wait for all-clear from safety team
```

**Gas Cylinder Leak**:
```
If SMALL leak and you're trained:
  1. Close cylinder valve (if accessible)
  2. Ventilate area
  3. Notify supervisor

If LARGE leak or pyrophoric gas:
  1. Evacuate immediately
  2. Activate alarm
  3. Call fire department
  4. Do NOT re-enter
```

### Safety Showers and Eyewash Stations

**Requirements**:
- Location: Within 10 seconds (55 feet) of any chemical hazard
- Flow rate: 20 gallons/minute (shower), 0.4 gpm (eyewash)
- Temperature: 60-100°F (tepid)
- Testing: Weekly activation (flush 3 minutes)
- Signage: High-visibility green/yellow signs

**Usage**:
```
Safety Shower:
  - Pull handle (stays on, hands-free)
  - Step fully under water
  - Remove clothing while rinsing
  - Rinse for 15 minutes minimum

Eyewash:
  - Push paddles to activate
  - Hold eyes open with fingers
  - Roll eyes to rinse thoroughly
  - Rinse for 20 minutes minimum
  - Seek medical attention
```

## Electrical Safety

### High-Voltage Hazards

Semiconductor equipment often uses high voltage:
- Ion implanters: 1 kV - 3 MV
- Plasma tools: 1-13.56 MHz RF (1-5 kV)
- Lasers: Kilovolt capacitor banks
- Power supplies: 480V, 3-phase

**Hazards**:
- Electrocution (>50 mA can be fatal)
- Burns (arc flash, resistive heating)
- Arc blast (explosive pressure wave)

### Lockout/Tagout (LOTO)

**Purpose**: Prevent accidental equipment energization during maintenance

**Procedure**:
```
1. Notify affected personnel
2. Shut down equipment properly
3. Isolate energy sources:
   - Disconnect power
   - Close gas valves
   - Bleed pressurized lines
4. Apply lockout device (personal padlock)
5. Attach tagout tag with your name, date
6. Test equipment is de-energized
7. Perform maintenance
8. Remove LOTO only when safe (only person who applied it)
```

**Personal Locks**:
- One lock per person
- Never remove another person's lock
- Disciplinary action for violations

### Electrical PPE

**Voltage-Rated Gloves**:
- Class 00: Up to 500V AC
- Class 0: Up to 1,000V AC
- Inspect before each use (air test, visual)
- Leather protectors worn over rubber gloves

**Arc-Rated Clothing**:
- Required for energized work >50V
- ATPV rating ≥8 cal/cm²
- Face shields, arc-rated hoods

**Insulated Tools**:
- 1000V rated for high-voltage work
- Regular inspection

## Laser Safety

### Laser Classifications

| Class | Hazard | Examples |
|-------|--------|----------|
| Class 1 | Safe under normal use | Enclosed laser systems |
| Class 2 | Low power visible (<1mW) | Laser pointers |
| Class 3R | Medium power (1-5mW) | Alignment lasers |
| Class 3B | Hazardous (5-500mW) | Lab lasers, lithography alignment |
| Class 4 | Severe hazard (>500mW) | Industrial cutting, EUV lithography |

**Hazards**:
- **Eye damage**: Retinal burns (permanent blindness)
- **Skin burns**: High-power lasers
- **Fire**: Ignition of materials
- **Electrical**: High-voltage power supplies

### Laser Safety Measures

**Engineering Controls**:
- Enclosed beam path
- Interlocked enclosures (beam stops if opened)
- Beam shutters
- Remote operation

**Administrative**:
- Authorized personnel only
- Laser safety training required
- Controlled area signage
- Standard operating procedures (SOPs)

**PPE**:
- Laser safety glasses (OD 4+ at wavelength)
  - Example: 193nm (ArF) requires OD 7+ UV protection
- Never rely on PPE alone (engineering controls first)

**Emergency**: Eye injury → Immediate medical evaluation by ophthalmologist

## Radiation Safety

### Ionizing Radiation

**Sources in Fabs**:
- **X-ray systems**: Metrology, inspection
- **Ion implanters**: High-energy ions generate X-rays
- **Electron beams**: E-beam lithography, inspection

**Dose Limits** (Annual):
- Occupational: 50 mSv (5 rem)
- Public: 1 mSv (0.1 rem)
- As Low As Reasonably Achievable (ALARA principle)

**Protection**:
- Time: Minimize exposure time
- Distance: Inverse square law (2× distance = 1/4 dose)
- Shielding: Lead shielding on equipment
- Dosimetry: Badge monitoring for radiation workers

### Non-Ionizing Radiation

**RF/Microwave** (plasma tools):
- Frequency: 13.56 MHz, 2.45 GHz
- Hazard: Heating of tissues
- Protection: Shielded chambers, interlocks

**UV Radiation** (lithography):
- Wavelengths: 365nm (i-line), 248nm (KrF), 193nm (ArF)
- Hazards: Skin burns, eye damage
- Protection: Enclosed systems, UV-blocking windows

## Cryogenic Safety

### Liquid Nitrogen (LN₂)

**Properties**:
- Boiling point: -196°C (-321°F)
- Expansion ratio: 1:694 (liquid to gas)
- Inert, non-toxic

**Hazards**:
1. **Frostbite**: Severe cold burns
2. **Asphyxiation**: Displaces oxygen (19.5-23.5% O₂ required)
3. **Pressure**: Rapid vaporization can rupture containers
4. **Embrittlement**: Materials become brittle at cryogenic temps

**Safety Measures**:
- Insulated gloves and face shield
- Adequate ventilation (O₂ monitors required)
- Pressure relief valves on containers
- Never seal LN₂ containers completely

**Oxygen Deficiency**:
```
Oxygen Level | Symptoms
21%          | Normal
19%          | Impaired thinking
17%          | Impaired coordination
15%          | Fainting, unconsciousness
<12%         | Death within minutes
```

**O₂ Monitors**: Alarm at <19.5%, evacuation at <18%

## Mechanical Hazards

### Rotating Equipment

**Hazards**:
- Entanglement (clothing, hair, jewelry)
- Pinch points
- Projectiles (broken parts)

**Prevention**:
- Machine guards (never remove during operation)
- Emergency stop buttons (E-stops) within reach
- Lockout/tagout before maintenance
- No loose clothing or jewelry
- Hair tied back

### Compressed Gases

**Gas Cylinders**:
- Pressure: 2000-3000 psi (140-210 bar)
- Hazard: Projectile if valve breaks off

**Safe Handling**:
- Always secure with chain or strap
- Transport with valve cap installed
- Store upright in well-ventilated area
- Never drop or drag cylinders
- Regulators: Use correct type for gas

**Cylinder Color Codes** (US):
- Green: Oxygen
- Yellow: Chlorine, toxic gases
- Red: Flammable gases
- Gray: Carbon dioxide, inert gases

*Note*: Color codes vary by country (not universal)

## Confined Space Entry

**Definition**: Space that is:
1. Large enough to enter
2. Limited entry/exit
3. Not designed for continuous occupancy

**Examples in Fabs**:
- Sub-fab utility areas
- Chemical storage tanks
- Process tool chambers (large)

**Hazards**:
- Oxygen deficiency
- Toxic gases
- Engulfment
- Temperature extremes

**Entry Requirements**:
- Permit-required confined space program
- Atmospheric testing (O₂, LEL, toxics)
- Continuous air monitoring
- Attendant outside (communication maintained)
- Rescue equipment ready
- Training and authorization

**NEVER ENTER** alone or without authorization

## Ergonomics and Repetitive Strain

### Wafer Handling

**Risk**: Repetitive motion injuries (carpal tunnel, tendonitis)

**Prevention**:
- Automated wafer handling where possible
- Proper lifting technique (use wafer vacuum wand)
- Micro-breaks every 30 minutes
- Stretch exercises
- Job rotation

### Cleanroom Ergonomics

**Challenges**:
- Bulky gowning restricts movement
- Extended standing
- Awkward postures (reaching into tools)

**Solutions**:
- Anti-fatigue mats at workstations
- Adjustable-height benches
- Proper lifting techniques (bend knees, not back)
- Regular breaks

## Noise Exposure

**Sources**:
- Vacuum pumps: 75-85 dBA
- Exhaust blowers: 80-90 dBA
- Pneumatic systems: 85-95 dBA

**Limits**:
- 85 dBA: Hearing conservation program required
- 90 dBA: Hearing protection mandatory
- 115 dBA: Exposure limit (15 min/day)

**Protection**:
- Engineering: Enclose noisy equipment, silencers
- Administrative: Limit exposure time
- PPE: Earplugs (NRR 29-33 dB) or earmuffs (NRR 25-31 dB)

## Environmental Safety

### Waste Management

#### Chemical Waste

**Segregation**:
- Halogenated solvents (chlorinated)
- Non-halogenated solvents
- Acids (separate organic/inorganic)
- Bases
- Metals (heavy metal waste)

**Containers**:
- Compatible material (HDPE for acids)
- Labeled with contents, date, responsible person
- Secondary containment
- Close lids (no evaporation)

**Disposal**:
- Manifest system (track from cradle to grave)
- Licensed waste hauler
- Proper EPA waste codes

#### Wastewater

**Treatment**:
- Acid/base neutralization
- Heavy metal precipitation
- Fluoride precipitation (for HF waste)
- Discharge limits per permit

**Prohibited**:
- Pouring chemicals down drain (unless approved)
- Mixing incompatible wastes

#### Air Emissions

**Scrubbers**:
- Wet scrubbers: Remove acids, bases
- Dry scrubbers: Remove organics
- Burn boxes: Combust pyrophorics

**Monitoring**:
- Continuous emission monitoring systems (CEMS)
- Compliance with air quality permits

### Sustainability

**Water Conservation**:
- DI water recycling
- Cooling water recirculation
- Ultra-pure water (UPW) recovery

**Energy Efficiency**:
- HVAC optimization (major energy user)
- Heat recovery from chillers
- LED lighting conversion

## Emergency Preparedness

### Fire Safety

**Fire Triangle**:
```
      Heat
       /\
      /  \
     /____\
  Fuel    Oxygen
  
Remove any one element → Fire extinguishes
```

**Fire Classes**:
- **Class A**: Ordinary combustibles (wood, paper)
- **Class B**: Flammable liquids (solvents)
- **Class C**: Electrical fires
- **Class D**: Combustible metals (Na, Mg, Ti)

**Fire Extinguisher Selection**:
- ABC: Most common, multi-purpose
- BC: Flammable liquids, electrical
- D: Metal fires only (special powder)
- **Never use water on electrical or chemical fires**

**PASS Method**:
```
P - Pull pin
A - Aim at base of fire
S - Squeeze handle
S - Sweep side to side
```

**Evacuation**:
- Know two exit routes from your area
- Proceed to muster point
- Do NOT re-enter until all-clear given
- Assist others if safe to do so

### Earthquake Preparedness (Seismic Zones)

**During Earthquake**:
```
1. DROP to hands and knees
2. COVER under sturdy desk/table
3. HOLD ON until shaking stops
4. Stay away from glass, equipment
```

**After Earthquake**:
```
1. Check for injuries
2. Evacuate if building damaged
3. Check for gas leaks (smell, sound)
4. Inspect chemical storage for spills
5. Do NOT use elevators
6. Expect aftershocks
```

**Prevention**:
- Seismic restraints on gas cylinders
- Cabinet latches secure
- Heavy items stored low

### Medical Emergencies

**First Aid**:
- First aid kits accessible
- AED (Automated External Defibrillator) locations
- CPR-trained personnel on each shift

**Emergency Call**:
```
Dial XXX (internal) or 911
Provide:
  - Location (building, room)
  - Nature of emergency
  - Number of people affected
  - Your name and callback number
  
Stay on line until released
```

## Training and Certification

### Required Training

**Before Fab Entry**:
- [ ] General safety orientation
- [ ] Cleanroom protocols
- [ ] Chemical safety (Hazcom)
- [ ] Emergency procedures
- [ ] Electrical safety awareness

**Job-Specific**:
- [ ] Tool-specific safety training
- [ ] Chemical handling (for process engineers)
- [ ] Lockout/tagout (for maintenance)
- [ ] Confined space (if applicable)
- [ ] Radiation safety (if applicable)

**Refreshers**:
- Annual: General safety, chemical safety
- Every 3 years: First aid/CPR, tool-specific

### Safety Data Sheets (SDS)

**Formerly MSDS (Material Safety Data Sheets)**

**Required Information**:
1. Identification
2. Hazard(s) identification
3. Composition/ingredients
4. First-aid measures
5. Fire-fighting measures
6. Accidental release measures
7. Handling and storage
8. Exposure controls/PPE
9. Physical and chemical properties
10. Stability and reactivity
11. Toxicological information
12. Ecological information
13. Disposal considerations
14. Transport information
15. Regulatory information
16. Other information

**Accessibility**: Available at all chemical use locations

## Regulatory Compliance

### Key Regulations (US)

**OSHA** (Occupational Safety and Health Administration):
- Hazard Communication Standard (HazCom)
- PPE requirements (29 CFR 1910.132)
- Respiratory protection (29 CFR 1910.134)
- Electrical safety (29 CFR 1910 Subpart S)
- Confined space (29 CFR 1910.146)

**EPA** (Environmental Protection Agency):
- RCRA (Resource Conservation and Recovery Act) - waste
- Clean Air Act - emissions
- Clean Water Act - wastewater discharge
- EPCRA (Emergency Planning) - chemical reporting

**DOT** (Department of Transportation):
- Hazardous materials shipping regulations

**International**:
- Similar regulations in EU, Japan, China, etc.
- GHS (Globally Harmonized System) for labeling

## Safety Culture

### Personal Responsibility

**Stop Work Authority**:
- Anyone can stop work if unsafe condition observed
- No repercussions for good-faith safety stops
- Identify hazard, notify supervisor, resolve before continuing

**Near-Miss Reporting**:
- Report incidents that COULD have caused injury
- Learn from close calls
- Anonymous reporting options available

**5S Methodology**:
1. **Sort** - Remove unnecessary items
2. **Set in Order** - Organize workspace
3. **Shine** - Clean and inspect
4. **Standardize** - Create standards
5. **Sustain** - Maintain improvements

**Safety Mantras**:
- "Safety first, quality second, production third"
- "If you don't have time to do it safely, you don't have time to do it"
- "See something, say something"

## Conclusion

Safety in semiconductor fabrication is a shared responsibility. Every individual must:

1. **Know the hazards** of materials and equipment used
2. **Follow procedures** without shortcuts
3. **Use PPE correctly** every time
4. **Report hazards** immediately
5. **Participate in training** actively
6. **Look out for coworkers**

> "Safety isn't expensive, it's priceless. An accident is expensive in ways that can never be fully calculated."

Your most important job is to go home safe at the end of every shift.

## Emergency Contact Information

**Template** (Customize for your facility):

```
Emergency Services:        911 (external)
                          XXX (internal)

Facility Security:        XXX
Environmental Health:     XXX
Maintenance Emergency:    XXX

Poison Control:          1-800-222-1222
Chemical Spill Hotline:  XXX

Nearest Hospital:
  Name: _______________
  Address: _______________
  Phone: _______________
```

## Further Resources

1. **OSHA Website**: www.osha.gov
2. **NIOSH Safety Resources**: www.cdc.gov/niosh
3. **SEMI S2/S8 Standards**: Safety guidelines for semiconductor equipment
4. **Chemical Safety Board (CSB)**: Incident investigation reports
5. **Facility-Specific**: Safety manuals, SOPs, training materials

---

**End of Introduction Section**

**Next**: [Chapter 2 - CMOS FEOL](../02-cmos-feol/) - Front-End-Of-Line Fabrication Processes

---

**Document Revision**: November 2025  
**Review Frequency**: Annual or when procedures change  
**Acknowledgment**: All personnel must read and sign understanding of safety guidelines
