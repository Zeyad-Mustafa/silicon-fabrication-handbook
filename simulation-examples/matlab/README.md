# MATLAB Simulation Examples

This folder contains MATLAB scripts that model core silicon fabrication and MEMS concepts. Each script prints a short console report and generates figures that summarize the analysis. Some scripts save images into a local `images/` directory (created automatically when needed).

## Requirements
- MATLAB R2020a+ (tested) or GNU Octave (most scripts should work; plotting style may vary)
- No external toolboxes required

## How to Run
From MATLAB, set your current folder to `simulation-examples/matlab`, then run a script:

```matlab
run('ion_implant_profile.m')
```

You can also open a script and press **Run** in the editor.

Images are saved to a local `images/` directory if the script includes a save step.

## Scripts and Outputs

### `ion_implant_profile.m` — Ion Implantation Profile Analysis
Simulates dopant concentration profiles (Gaussian and multi-energy), annealing diffusion effects, and junction depth for implanted dopants in silicon.

Console output highlights:
- Projected range and straggle (LSS theory)
- Peak concentration and junction depth
- Diffusion length after anneal
- Sheet resistance estimate
- Summary report and design guidelines

Figures (saved to `images/ion_implant_profile.png`):
- Single-energy Gaussian profile vs substrate doping
- As-implanted vs annealed profile with junction depth
- Multi-energy implant profile (box-like)
- Range vs energy trend
- Dose vs peak concentration
- Junction depth vs anneal time

---

### `mosfet_threshold.m` — MOSFET Threshold Voltage Analysis
Calculates and visualizes MOSFET threshold voltage with body effect, temperature dependence, and short-channel rolloff. Also includes simple I-V and subthreshold models.

Console output highlights:
- Threshold voltage components (phi_ms, phi_F, gamma, Q_ox/C_ox)
- Temperature coefficient (dVth/dT)
- Short-channel rolloff and DIBL impact
- Subthreshold swing and I_on/I_off estimate
- Summary report and design guidelines

Figures (saved to `images/mosfet_threshold.png`):
- V_th vs substrate bias (body effect)
- V_th vs temperature
- V_th vs channel length (short-channel effects)
- I_D vs V_GS (saturation region)
- Subthreshold characteristics
- V_th component breakdown bar chart

---

### `spring_design.m` — MEMS Spring Design & Analysis
Comprehensive design tool for folded-beam (default), serpentine, or crab-leg MEMS springs. Computes stiffness, stress, dynamic response, thermal effects, reliability, and design sweeps.

Console output highlights:
- Spring constant, compliance, and displacement under load
- Stress and safety factor at max displacement
- Natural frequency, bandwidth, and Q-factor assumptions
- Width/length sweep ranges and design space notes
- Fatigue life and shock survivability

Figures:
- 3x3 dashboard including frequency response, stiffness/frequency vs geometry, stress trends, thermal expansion, fatigue, and a summary panel

Note: This script does **not** save images by default. Use MATLAB's save button or add `saveas` if you want to export figures.

---

### `squeeze_film_damping.m` — Squeeze-Film Damping in MEMS
Analyzes viscous damping for a micro-plate over a substrate, including rarefaction effects and pressure dependence. Useful for Q-factor prediction and packaging trade-offs.

Console output highlights:
- Damping coefficient (squeeze + border)
- Rarefaction correction
- Natural frequency and damping ratio
- Regime classification by Knudsen number
- Design recommendations and typical MEMS Q ranges

Figures (saved to `images/squeeze_film_damping.png`):
- Q vs pressure
- Damping vs gap height (b ~ 1/h^3)
- Frequency response with damping
- Q vs pressure for different perforation hole counts

---

### `thermal_analysis.m` — MEMS Thermal Analysis & Optimization
Thermal modeling for MEMS devices (cantilever/bridge/membrane). Includes steady-state, transient response, thermal stress, temperature coefficient effects, package heating, and application examples.

Console output highlights:
- Thermal resistances and time constant
- Temperature rise vs power
- Thermal stress at DeltaT=100 K
- Frequency shift due to TCE
- Package self-heating and cycling conditions
- Application-specific results (actuator, bolometer, resonator)

Figures:
- 3x4 dashboard with steady-state, transient, stress, deflection, material comparison, package heating, cycling profile, and summary panel

Note: This script does **not** save images by default. Use MATLAB's save button or add `saveas` if you want to export figures.

---

### `capacitor_model.m` — MOS Capacitor C-V Simulation
Simulates MOS capacitor C-V behavior across accumulation, depletion, and inversion regions.

Console output highlights:
- Oxide capacitance, Fermi potential, Vfb, Vt
- Debye length and depletion width estimates

Figures:
- Normalized C/Cox vs gate voltage (with region markers)
- Absolute capacitance vs gate voltage

Note: This script does **not** save images by default. Use MATLAB's save button or add `saveas` if you want to export figures.

## Output Folder
Scripts that save images will create `simulation-examples/matlab/images` if it does not exist:
- `ion_implant_profile.png`
- `mosfet_threshold.png`
- `squeeze_film_damping.png`

## Tips
- Parameters are declared near the top of each script for easy modification.
- For Octave users, minor plot styling differences are expected.
- To export figures from scripts that do not save, add a line like:

```matlab
saveas(gcf, 'images/my_figure.png')
```
