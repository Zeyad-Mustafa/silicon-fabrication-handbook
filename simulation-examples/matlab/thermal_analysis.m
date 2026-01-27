%% MEMS Thermal Analysis & Optimization Tool
% Comprehensive thermal modeling for MEMS devices
% Includes: heat transfer, thermal stress, TCE compensation, and package effects
% Applications: thermal actuators, IR sensors, resonators, and reliability

clear; close all; clc;

%% ============================================================
%  SECTION 1: MATERIAL LIBRARY
%% ============================================================

fprintf('=== MEMS Thermal Analysis Tool ===\n\n');

% Silicon (substrate)
mat_Si.k = 148;                 % Thermal conductivity [W/m·K]
mat_Si.rho = 2329;              % Density [kg/m³]
mat_Si.Cp = 700;                % Specific heat [J/kg·K]
mat_Si.alpha = 2.6e-6;          % Thermal expansion coeff [1/K]
mat_Si.E = 169e9;               % Young's modulus [Pa]
mat_Si.name = 'Silicon';

% Silicon Dioxide (isolation/passivation)
mat_SiO2.k = 1.4;
mat_SiO2.rho = 2200;
mat_SiO2.Cp = 730;
mat_SiO2.alpha = 0.5e-6;
mat_SiO2.E = 70e9;
mat_SiO2.name = 'SiO2';

% Silicon Nitride (structural layer)
mat_Si3N4.k = 20;
mat_Si3N4.rho = 3100;
mat_Si3N4.Cp = 700;
mat_Si3N4.alpha = 3.2e-6;
mat_Si3N4.E = 250e9;
mat_Si3N4.name = 'Si3N4';

% Aluminum (metal interconnect)
mat_Al.k = 237;
mat_Al.rho = 2700;
mat_Al.Cp = 900;
mat_Al.alpha = 23.1e-6;
mat_Al.E = 70e9;
mat_Al.name = 'Aluminum';

% Polysilicon (structural/heater)
mat_PolySi.k = 35;
mat_PolySi.rho = 2320;
mat_PolySi.Cp = 700;
mat_PolySi.alpha = 2.6e-6;
mat_PolySi.E = 160e9;
mat_PolySi.name = 'Polysilicon';

fprintf('Material library loaded: Si, SiO2, Si3N4, Al, PolySi\n\n');

%% ============================================================
%  SECTION 2: DEVICE GEOMETRY DEFINITION
%% ============================================================

fprintf('--- Device Configuration ---\n');

% Choose device type
device_type = 1;  % 1=Cantilever, 2=Bridge, 3=Membrane

switch device_type
    case 1
        fprintf('Device Type: CANTILEVER BEAM\n');
        geom.L = 200e-6;        % Length [m]
        geom.w = 50e-6;         % Width [m]
        geom.t = 2e-6;          % Thickness [m]
        geom.area = geom.L * geom.w;
        geom.volume = geom.area * geom.t;
        geom_type = 'Cantilever';
        
    case 2
        fprintf('Device Type: DOUBLY-CLAMPED BRIDGE\n');
        geom.L = 300e-6;
        geom.w = 40e-6;
        geom.t = 1.5e-6;
        geom.area = geom.L * geom.w;
        geom.volume = geom.area * geom.t;
        geom_type = 'Bridge';
        
    case 3
        fprintf('Device Type: CIRCULAR MEMBRANE\n');
        geom.r = 100e-6;        % Radius [m]
        geom.t = 1e-6;          % Thickness [m]
        geom.area = pi * geom.r^2;
        geom.volume = geom.area * geom.t;
        geom_type = 'Membrane';
end

% Select structural material
struct_mat = mat_PolySi;  % Default: polysilicon
fprintf('Structural Material: %s\n', struct_mat.name);
fprintf('Dimensions: L=%.0f μm, w=%.0f μm, t=%.2f μm\n\n', ...
    geom.L*1e6, geom.w*1e6, geom.t*1e6);

%% ============================================================
%  SECTION 3: THERMAL RESISTANCE NETWORK
%% ============================================================

fprintf('--- Thermal Resistance Analysis ---\n');

% Conduction through structure
R_cond_struct = geom.L / (struct_mat.k * geom.w * geom.t);

% Conduction through substrate (simplified)
t_substrate = 500e-6;  % Substrate thickness
R_cond_substrate = t_substrate / (mat_Si.k * geom.area);

% Convection to air (natural convection)
h_air = 10;  % Heat transfer coefficient [W/m²·K] (natural)
R_conv = 1 / (h_air * geom.area);

% Radiation (Stefan-Boltzmann)
epsilon = 0.6;  % Emissivity (typical for silicon)
sigma_sb = 5.67e-8;  % Stefan-Boltzmann constant [W/m²·K⁴]
T_ambient = 300;  % Ambient temperature [K]
T_device = 350;   % Device temperature [K]
h_rad = epsilon * sigma_sb * (T_device^2 + T_ambient^2) * ...
        (T_device + T_ambient);
R_rad = 1 / (h_rad * geom.area);

% Total thermal resistance (parallel paths)
R_parallel = 1 / (1/R_conv + 1/R_rad);
R_total = R_cond_struct + R_parallel;

fprintf('Thermal Resistances:\n');
fprintf('  R_conduction (structure): %.2e K/W\n', R_cond_struct);
fprintf('  R_convection: %.2e K/W\n', R_conv);
fprintf('  R_radiation: %.2e K/W\n', R_rad);
fprintf('  R_total: %.2e K/W\n\n', R_total);

%% ============================================================
%  SECTION 4: STEADY-STATE HEAT TRANSFER
%% ============================================================

fprintf('--- Steady-State Analysis ---\n');

% Power input scenarios
P_input = [1e-6, 10e-6, 100e-6, 1e-3];  % Power [W]
delta_T = P_input * R_total;

fprintf('Temperature Rise vs Input Power:\n');
for i = 1:length(P_input)
    fprintf('  P = %.2e W → ΔT = %.2f K\n', P_input(i), delta_T(i));
end

% Temperature distribution along cantilever (1D approximation)
if device_type == 1  % Cantilever only
    x = linspace(0, geom.L, 100);
    
    % Heat generation per unit length (uniform)
    q_gen = P_input(3) / geom.L;  % Use 100 μW case
    
    % Temperature profile: T(x) = T_base + (q*L²/2k)*(1-(x/L)²)
    T_base = T_ambient;
    T_profile = T_base + (q_gen * geom.L^2) / (2 * struct_mat.k * ...
                geom.w * geom.t) * (1 - (x/geom.L).^2);
    
    T_max = max(T_profile);
    fprintf('\nTemperature Distribution:\n');
    fprintf('  Base temperature: %.1f K\n', T_base);
    fprintf('  Maximum temperature: %.1f K\n', T_max);
    fprintf('  Temperature difference: %.1f K\n\n', T_max - T_base);
end

%% ============================================================
%  SECTION 5: TRANSIENT THERMAL RESPONSE
%% ============================================================

fprintf('--- Transient Analysis ---\n');

% Thermal mass (heat capacity)
C_thermal = struct_mat.rho * struct_mat.Cp * geom.volume;

% Thermal time constant
tau_thermal = R_total * C_thermal;

fprintf('Thermal Time Constant: %.2f ms\n', tau_thermal*1000);

% Step response simulation
t_span = linspace(0, 5*tau_thermal, 500);
P_step = 100e-6;  % Step power [W]

% First-order response: T(t) = ΔT_ss * (1 - exp(-t/τ))
delta_T_ss = P_step * R_total;
T_response = T_ambient + delta_T_ss * (1 - exp(-t_span/tau_thermal));

% 3dB bandwidth
f_3dB = 1 / (2 * pi * tau_thermal);
fprintf('Thermal Bandwidth (f_3dB): %.2f Hz\n\n', f_3dB);

%% ============================================================
%  SECTION 6: THERMAL STRESS ANALYSIS
%% ============================================================

fprintf('--- Thermal Stress Analysis ---\n');

% Temperature excursion
delta_T_range = -50:5:150;  % Temperature change [K]

% Bimorph effect (two materials with different α)
% Using Si substrate + SiO2 layer as example
t_SiO2 = 0.5e-6;  % Oxide thickness
t_Si = geom.t;

% Stoney's equation for curvature
delta_alpha = mat_SiO2.alpha - mat_Si.alpha;
kappa = 6 * delta_alpha * delta_T_range * t_SiO2 * ...
        (t_Si + t_SiO2) / (t_Si^2);

% Maximum deflection (for cantilever)
if device_type == 1
    deflection_thermal = 0.5 * kappa * geom.L^2 * 1e6;  % [μm]
end

% Thermal stress (constrained expansion)
% σ = E * α * ΔT / (1 - ν)
nu = 0.28;  % Poisson's ratio (average)
sigma_thermal = struct_mat.E * struct_mat.alpha * abs(delta_T_range) / ...
                (1 - nu);

fprintf('Thermal Stress at ΔT = 100 K:\n');
idx_100 = find(abs(delta_T_range - 100) < 1, 1);
fprintf('  σ_thermal = %.2f MPa\n', sigma_thermal(idx_100)/1e6);
fprintf('  CTE mismatch strain: %.2e\n', ...
        struct_mat.alpha * 100);

if device_type == 1
    fprintf('  Tip deflection: %.2f μm\n\n', deflection_thermal(idx_100));
end

%% ============================================================
%  SECTION 7: TEMPERATURE COEFFICIENT COMPENSATION
%% ============================================================

fprintf('--- TCE Compensation Strategies ---\n');

% Frequency shift due to temperature
% Δf/f = (TCE/2) * ΔT where TCE = (1/E)(dE/dT) + α
TCE_Si = -64e-6;  % Temperature coefficient [ppm/K]
f_nominal = 10e3;  % Nominal frequency [Hz]

delta_f = f_nominal * TCE_Si * delta_T_range;

fprintf('Frequency shift (f = %.0f kHz):\n', f_nominal/1000);
fprintf('  ΔT = -50 K → Δf = %.2f Hz (%.1f ppm)\n', ...
    delta_f(1), delta_f(1)/f_nominal*1e6);
fprintf('  ΔT = +100 K → Δf = %.2f Hz (%.1f ppm)\n', ...
    delta_f(end), delta_f(end)/f_nominal*1e6);

% Compensation methods
fprintf('\nCompensation Techniques:\n');
fprintf('  1. Material selection (SiO2 has opposite TCE)\n');
fprintf('  2. Geometric compensation (bimorph structures)\n');
fprintf('  3. Active temperature control (heaters)\n');
fprintf('  4. Digital calibration (lookup tables)\n\n');

%% ============================================================
%  SECTION 8: PACKAGE-LEVEL THERMAL EFFECTS
%% ============================================================

fprintf('--- Package Thermal Analysis ---\n');

% Package thermal resistances
R_die_attach = 20;      % K/W (typical for die attach)
R_leadframe = 10;       % K/W (metal leadframe)
R_package = 50;         % K/W (plastic package to ambient)

R_total_package = R_total + R_die_attach + R_leadframe + R_package;

% Self-heating in package
P_dissipation = [10e-3, 50e-3, 100e-3];  % Package power [W]
T_rise_package = P_dissipation * R_total_package;

fprintf('Package Thermal Resistance: %.1f K/W\n', R_total_package);
fprintf('\nSelf-Heating in Package:\n');
for i = 1:length(P_dissipation)
    fprintf('  P = %.0f mW → ΔT = %.1f K\n', ...
        P_dissipation(i)*1000, T_rise_package(i));
end

% Thermal cycling (reliability test)
N_cycles = 1000;
T_high = 125 + 273;  % High temperature [K]
T_low = -40 + 273;   % Low temperature [K]
dwell_time = 15*60;  % Dwell time [s]

delta_T_cycle = T_high - T_low;
fprintf('\nThermal Cycling Test Conditions:\n');
fprintf('  Temperature range: %.0f to %.0f °C\n', T_low-273, T_high-273);
fprintf('  Cycles: %d\n', N_cycles);
fprintf('  Thermal stress range: ±%.1f MPa\n\n', ...
    struct_mat.E * struct_mat.alpha * delta_T_cycle/2 / (1-nu) / 1e6);

%% ============================================================
%  SECTION 9: SPECIFIC APPLICATIONS
%% ============================================================

fprintf('--- Application-Specific Analysis ---\n');

% Application 1: Thermal Actuator
fprintf('\n1. THERMAL ACTUATOR DESIGN:\n');
P_actuator = 10e-3;  % Power [W]
displacement_per_K = 0.1e-6;  % Displacement sensitivity [m/K]

delta_T_actuator = P_actuator * R_total;
displacement_actuator = displacement_per_K * delta_T_actuator * 1e6;

fprintf('   Power: %.0f mW\n', P_actuator*1000);
fprintf('   Temperature rise: %.1f K\n', delta_T_actuator);
fprintf('   Displacement: %.2f μm\n', displacement_actuator);
fprintf('   Response time: %.2f ms\n', tau_thermal*1000);

% Application 2: IR Bolometer
fprintf('\n2. IR BOLOMETER PERFORMANCE:\n');
TCR = 0.002;  % Temperature coefficient of resistance [1/K]
R_sensor = 1000;  % Sensor resistance [Ω]
P_IR = 1e-9;  % Incident IR power [W]

delta_T_IR = P_IR * R_total;
delta_R = R_sensor * TCR * delta_T_IR;
NEP = P_IR / (delta_R / sqrt(4 * 1.38e-23 * T_ambient * 1));  % Noise equiv power

fprintf('   IR power: %.0f nW\n', P_IR*1e9);
fprintf('   Temperature rise: %.2e K\n', delta_T_IR);
fprintf('   Resistance change: %.2e Ω\n', delta_R);
fprintf('   Thermal time constant: %.2f ms\n', tau_thermal*1000);

% Application 3: Resonator Stability
fprintf('\n3. RESONATOR TEMPERATURE STABILITY:\n');
f_res = 32e3;  % Resonance frequency [Hz]
Q = 10000;    % Quality factor

% Allan deviation due to temperature fluctuations
delta_T_rms = 0.1;  % Temperature noise [K]
delta_f_rms = abs(TCE_Si) * f_res * delta_T_rms;
allan_dev = delta_f_rms / f_res;

fprintf('   Resonance frequency: %.1f kHz\n', f_res/1000);
fprintf('   Q-factor: %d\n', Q);
fprintf('   Temp. noise (RMS): %.2f K\n', delta_T_rms);
fprintf('   Frequency stability: %.2f ppb\n', allan_dev*1e9);

%% ============================================================
%  SECTION 10: COMPREHENSIVE VISUALIZATION
%% ============================================================

figure('Position', [50, 50, 1500, 1000], 'Color', 'w');

% Plot 1: Temperature vs Power
subplot(3, 4, 1);
plot(P_input*1e6, delta_T, 'b-o', 'LineWidth', 2, 'MarkerSize', 8);
grid on;
xlabel('Input Power [μW]', 'FontSize', 10);
ylabel('Temperature Rise [K]', 'FontSize', 10);
title('Steady-State: ΔT vs Power', 'FontWeight', 'bold');
set(gca, 'XScale', 'log');

% Plot 2: Temperature Profile (if cantilever)
subplot(3, 4, 2);
if device_type == 1
    plot(x*1e6, T_profile-273, 'b-', 'LineWidth', 2);
    grid on;
    xlabel('Position [μm]', 'FontSize', 10);
    ylabel('Temperature [°C]', 'FontSize', 10);
    title('Temperature Distribution', 'FontWeight', 'bold');
else
    text(0.5, 0.5, 'N/A for this geometry', 'HorizontalAlignment', 'center');
    axis off;
end

% Plot 3: Transient Response
subplot(3, 4, 3);
plot(t_span*1000, T_response-273, 'b-', 'LineWidth', 2);
hold on;
plot([tau_thermal tau_thermal]*1000, [T_ambient-273 max(T_response)-273], ...
     'r--', 'LineWidth', 1.5);
grid on;
xlabel('Time [ms]', 'FontSize', 10);
ylabel('Temperature [°C]', 'FontSize', 10);
title('Step Response', 'FontWeight', 'bold');
legend('T(t)', '\tau', 'Location', 'southeast');

% Plot 4: Thermal Resistance Network
subplot(3, 4, 4);
axis off;
text(0.5, 0.9, '\bfThermal Network:', 'FontSize', 11, ...
     'HorizontalAlignment', 'center');
text(0.1, 0.7, sprintf('R_{cond} = %.1e K/W', R_cond_struct), 'FontSize', 9);
text(0.1, 0.55, sprintf('R_{conv} = %.1e K/W', R_conv), 'FontSize', 9);
text(0.1, 0.4, sprintf('R_{rad} = %.1e K/W', R_rad), 'FontSize', 9);
text(0.1, 0.25, sprintf('R_{total} = %.1e K/W', R_total), 'FontSize', 9);
text(0.1, 0.1, sprintf('τ_{th} = %.2f ms', tau_thermal*1000), 'FontSize', 9);

% Plot 5: Thermal Stress vs Temperature
subplot(3, 4, 5);
plot(delta_T_range, sigma_thermal/1e6, 'b-', 'LineWidth', 2);
grid on;
xlabel('ΔT [K]', 'FontSize', 10);
ylabel('Thermal Stress [MPa]', 'FontSize', 10);
title('Thermal Stress', 'FontWeight', 'bold');

% Plot 6: Thermal Deflection (if cantilever)
subplot(3, 4, 6);
if device_type == 1
    plot(delta_T_range, deflection_thermal, 'b-', 'LineWidth', 2);
    grid on;
    xlabel('ΔT [K]', 'FontSize', 10);
    ylabel('Tip Deflection [μm]', 'FontSize', 10);
    title('Bimorph Deflection', 'FontWeight', 'bold');
else
    text(0.5, 0.5, 'N/A for this geometry', 'HorizontalAlignment', 'center');
    axis off;
end

% Plot 7: Frequency Shift
subplot(3, 4, 7);
plot(delta_T_range, delta_f, 'b-', 'LineWidth', 2);
grid on;
xlabel('ΔT [K]', 'FontSize', 10);
ylabel('Frequency Shift [Hz]', 'FontSize', 10);
title('TCE Effect on Frequency', 'FontWeight', 'bold');

% Plot 8: Material Comparison
subplot(3, 4, 8);
materials = {'Si', 'SiO_2', 'Si_3N_4', 'Al', 'PolySi'};
k_values = [mat_Si.k, mat_SiO2.k, mat_Si3N4.k, mat_Al.k, mat_PolySi.k];
alpha_values = [mat_Si.alpha, mat_SiO2.alpha, mat_Si3N4.alpha, ...
                mat_Al.alpha, mat_PolySi.alpha] * 1e6;

yyaxis left;
bar(1:5, k_values);
ylabel('Thermal Conductivity [W/m·K]', 'FontSize', 10);
yyaxis right;
plot(1:5, alpha_values, 'ro-', 'LineWidth', 2, 'MarkerSize', 8);
ylabel('CTE [ppm/K]', 'FontSize', 10);
set(gca, 'XTick', 1:5, 'XTickLabel', materials);
title('Material Properties', 'FontWeight', 'bold');
grid on;

% Plot 9: Package Self-Heating
subplot(3, 4, 9);
plot(P_dissipation*1000, T_rise_package, 'ro-', 'LineWidth', 2, 'MarkerSize', 8);
grid on;
xlabel('Package Power [mW]', 'FontSize', 10);
ylabel('Temperature Rise [K]', 'FontSize', 10);
title('Package Self-Heating', 'FontWeight', 'bold');

% Plot 10: Thermal Cycling Profile
subplot(3, 4, 10);
t_cycle = [0, dwell_time, dwell_time+60, 2*dwell_time+60];
T_cycle = [T_low, T_low, T_high, T_high] - 273;
t_total = linspace(0, 3*max(t_cycle), 300);
T_cycling = T_low - 273 + (T_high-T_low)/2 * ...
            (1 + square(2*pi*t_total/(2*(dwell_time+60))));

plot(t_total/60, T_cycling, 'b-', 'LineWidth', 2);
grid on;
xlabel('Time [min]', 'FontSize', 10);
ylabel('Temperature [°C]', 'FontSize', 10);
title('Thermal Cycling Test', 'FontWeight', 'bold');
ylim([T_low-273-10, T_high-273+10]);

% Plot 11: Frequency Response (thermal)
subplot(3, 4, 11);
f = logspace(-2, 3, 500);
H_thermal = 1 ./ sqrt(1 + (2*pi*f*tau_thermal).^2);
semilogx(f, 20*log10(H_thermal), 'b-', 'LineWidth', 2);
hold on;
plot([f_3dB f_3dB], [-40 0], 'r--', 'LineWidth', 1.5);
grid on;
xlabel('Frequency [Hz]', 'FontSize', 10);
ylabel('Magnitude [dB]', 'FontSize', 10);
title('Thermal Frequency Response', 'FontWeight', 'bold');
legend('|H(f)|', 'f_{3dB}', 'Location', 'southwest');

% Plot 12: Application Summary
subplot(3, 4, 12);
axis off;
text(0.5, 0.95, ['\bf' geom_type ' Summary:'], 'FontSize', 11, ...
     'HorizontalAlignment', 'center');
text(0.05, 0.8, sprintf('Material: %s', struct_mat.name), 'FontSize', 9);
text(0.05, 0.7, sprintf('R_{th} = %.1e K/W', R_total), 'FontSize', 9);
text(0.05, 0.6, sprintf('τ_{th} = %.2f ms', tau_thermal*1000), 'FontSize', 9);
text(0.05, 0.5, sprintf('f_{3dB} = %.1f Hz', f_3dB), 'FontSize', 9);
text(0.05, 0.4, sprintf('TCE = %.0f ppm/K', TCE_Si*1e6), 'FontSize', 9);
text(0.05, 0.3, sprintf('σ_{th}(100K) = %.0f MPa', ...
     sigma_thermal(idx_100)/1e6), 'FontSize', 9);
text(0.05, 0.2, sprintf('R_{pkg} = %.0f K/W', R_total_package), 'FontSize', 9);
text(0.05, 0.1, sprintf('Area = %.1e m²', geom.area), 'FontSize', 9);

sgtitle('MEMS Comprehensive Thermal Analysis', 'FontSize', 14, 'FontWeight', 'bold');

%% ============================================================
%  SECTION 11: OPTIMIZATION RECOMMENDATIONS
%% ============================================================

fprintf('\n=== Thermal Design Optimization ===\n');

% Check thermal bandwidth
if f_3dB < 1
    fprintf('⚠ Low thermal bandwidth (< 1 Hz): Reduce thermal mass\n');
elseif f_3dB > 1000
    fprintf('✓ Fast thermal response (> 1 kHz)\n');
else
    fprintf('✓ Moderate thermal bandwidth (1-1000 Hz)\n');
end

% Check self-heating
max_self_heating = max(delta_T);
if max_self_heating > 50
    fprintf('⚠ Significant self-heating (> 50 K): Improve heat sinking\n');
else
    fprintf('✓ Acceptable self-heating levels\n');
end

% Check thermal stress
if max(sigma_thermal)/1e6 > 100
    fprintf('⚠ High thermal stress (> 100 MPa): Consider:\n');
    fprintf('  - Material with lower CTE\n');
    fprintf('  - Stress relief structures\n');
    fprintf('  - Temperature-stable design\n');
else
    fprintf('✓ Manageable thermal stress levels\n');
end

fprintf('\nOptimization strategies:\n');
fprintf('  1. Minimize thermal mass → faster response\n');
fprintf('  2. Increase thermal conductivity → lower ΔT\n');
fprintf('  3. Use CTE-matched materials → reduce stress\n');
fprintf('  4. Add thermal isolation → improve efficiency\n');
fprintf('  5. Package selection → manage self-heating\n');

fprintf('\nRecommended material combinations:\n');
fprintf('  • Low stress: Si substrate + thin SiO2\n');
fprintf('  • High speed: Thin membranes, small area\n');
fprintf('  • High stability: Si3N4 for TCE compensation\n');
fprintf('=====================================\n\n');

%% ============================================================
%  SECTION 12: EXPORT RESULTS
%% ============================================================

% Create comprehensive results structure
results.geometry = geom;
results.material = struct_mat.name;
results.thermal_resistance = R_total;
results.thermal_time_constant = tau_thermal;
results.thermal_bandwidth = f_3dB;
results.max_temperature_rise = max(delta_T);
results.thermal_stress_100K = sigma_thermal(idx_100);
results.TCE = TCE_Si;
results.package_resistance = R_total_package;

fprintf('Thermal analysis complete!\n');
fprintf('All results stored in ''results'' structure.\n');
fprintf('Comprehensive visualization generated.\n\n');