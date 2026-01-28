# MATLAB Simulation Examples - Quick Reference

## Summary of All Scripts

| Script | Purpose | Key Outputs | Auto-saves? |
|--------|---------|-------------|-------------|
| `ion_implant_profile.m` | Dopant concentration profiles | Range, straggle, junction depth, annealing effects | ✓ Yes |
| `mosfet_threshold.m` | Threshold voltage analysis | Vth components, body effect, temperature, SCE | ✓ Yes |
| `spring_design.m` | MEMS spring mechanics | Stiffness, frequency, stress, fatigue life | ✗ Manual |
| `squeeze_film_damping.m` | Air damping in MEMS | Q-factor vs pressure, gap effects | ✓ Yes |
| `thermal_analysis.m` | Thermal behavior | Heat transfer, stress, time constants | ✗ Manual |
| `capacitor_model.m` | MOS capacitor C-V | Accumulation/depletion/inversion regions | ✗ Manual |

## Key Parameters by Script

### Ion Implantation
- **Energy:** 5-200 keV (shallow to deep implants)
- **Dose:** 1e12-1e16 ions/cm² (light to heavy doping)
- **Anneal:** 800-1100°C, 1s-60min (RTA to furnace)
- **Output:** Concentration profiles, junction depth, sheet resistance

### MOSFET Threshold
- **Technology:** 14nm-1μm nodes
- **Vth range:** 0.2-0.8V (LVT to HVT)
- **Body effect:** γ = 0.3-0.8 V^0.5
- **Temp coefficient:** -2 to -4 mV/°C
- **Output:** Vth vs VSB/T/L, I-V curves, subthreshold swing

### MEMS Spring
- **Geometries:** Folded beam, serpentine, crab-leg
- **Length:** 100-500 μm
- **Width:** 2-10 μm
- **k range:** 0.1-10000 N/m
- **Frequency:** 100 Hz - 100 kHz
- **Output:** Stiffness, frequency, stress, Q-factor

### Squeeze Film Damping
- **Gap:** 0.1-10 μm
- **Pressure:** 1 Pa - 100 kPa
- **Q-factor:** 10 (air) to 10,000 (vacuum)
- **Output:** Damping coefficient, frequency response

### Thermal Analysis
- **Power:** 0-1 mW (device level)
- **ΔT range:** 0-100 K
- **Materials:** Si, SiO₂, SiN, Al
- **Output:** Thermal resistance, time constant, stress, deflection

### MOS Capacitor
- **Oxide:** 2-20 nm
- **Doping:** 1e14-1e18 cm⁻³
- **Voltage:** -2 to +2 V
- **Output:** C-V curves, Vfb, Vt, depletion width

## Typical Use Cases

### Device Design
1. **CMOS Process:** Use `ion_implant_profile.m` → `mosfet_threshold.m` → `capacitor_model.m`
2. **MEMS Sensor:** Use `spring_design.m` → `squeeze_film_damping.m` → `thermal_analysis.m`

### Optimization
- **Minimize Vth variation:** Adjust doping, oxide thickness in `mosfet_threshold.m`
- **Maximize Q-factor:** Optimize gap, add holes in `squeeze_film_damping.m`
- **Target frequency:** Tune beam dimensions in `spring_design.m`

### Troubleshooting
- **Junction too deep:** Reduce energy or anneal time in `ion_implant_profile.m`
- **High thermal stress:** Use materials with matched CTE in `thermal_analysis.m`
- **Over-damped:** Increase gap or add vacuum in `squeeze_film_damping.m`

## Running All Scripts

Quick batch execution:

```matlab
% Run all scripts
scripts = {'ion_implant_profile', 'mosfet_threshold', 'spring_design', ...
           'squeeze_film_damping', 'thermal_analysis', 'capacitor_model'};

for i = 1:length(scripts)
    fprintf('\n========== Running %s ==========\n', scripts{i});
    run([scripts{i} '.m']);
    fprintf('========== Completed %s ==========\n\n', scripts{i});
end
```

## Export All Figures

For scripts that don't auto-save:

```matlab
% After running spring_design.m
saveas(gcf, 'images/spring_design.png');

% After running thermal_analysis.m
saveas(gcf, 'images/thermal_analysis.png');

% After running capacitor_model.m
saveas(gcf, 'images/capacitor_model.png');
```

## Customization Examples

### Change Ion Implant Energy
```matlab
E_implant = 100;  % Change from 50 to 100 keV
```

### Adjust MOSFET Technology Node
```matlab
tech_node = 65;   % Change from 180nm to 65nm
t_ox = 2e-9;      % Scale oxide accordingly
```

### Design Stiffer Spring
```matlab
w = 8e-6;         % Increase width from 4μm to 8μm
L = 150e-6;       % Decrease length from 200μm to 150μm
```

### Simulate Vacuum Package
```matlab
P_atm = 100;      % Change from 101325 to 100 Pa
```

---

**Pro Tip:** Always check the console output for design guidelines and warnings!
