%% Ion Implantation Profile Analysis
% ====================================
%
% Simulates dopant concentration profiles from ion implantation
% using Gaussian and Pearson-IV distributions. Includes:
% - Range and straggle calculations
% - Gaussian and dual-Pearson profiles
% - Multi-energy implants
% - Annealing effects (diffusion)
% - Junction depth calculation
%
% Author: Silicon Fabrication Handbook
% License: MIT
% Date: January 2026

clear; close all; clc;

fprintf('==============================================================\n');
fprintf('Ion Implantation Profile Analysis\n');
fprintf('==============================================================\n\n');

%% Physical Constants
q = 1.602e-19;          % Elementary charge [C]
k_B = 1.381e-23;        % Boltzmann constant [J/K]

%% Implantation Parameters

% Dopant species (Boron for p-type)
dopant = 'Boron';
M_dopant = 11;          % Atomic mass [amu]
Z_dopant = 5;           % Atomic number

% Target (Silicon)
M_target = 28;          % Si atomic mass [amu]

% Implant conditions
E_implant = 50;         % Implant energy [keV]
dose = 1e14;            % Dose [ions/cm²]
tilt_angle = 7;         % Wafer tilt [degrees] (prevents channeling)

% Substrate
N_substrate = 1e15;     % Background doping [cm⁻³]

fprintf('Implantation Parameters:\n');
fprintf('  Dopant: %s (M=%d amu, Z=%d)\n', dopant, M_dopant, Z_dopant);
fprintf('  Energy: %d keV\n', E_implant);
fprintf('  Dose: %.1e ions/cm²\n', dose);
fprintf('  Tilt angle: %d°\n', tilt_angle);
fprintf('  Substrate doping: %.1e cm⁻³\n\n', N_substrate);

%% Range and Straggle Calculation (LSS Theory)

% Projected range R_p and straggle ΔR_p (empirical for B in Si)
% Based on SRIM/TRIM data

if strcmp(dopant, 'Boron')
    % Empirical fit for Boron in Silicon
    R_p = 3.66e-6 * E_implant^1.24;      % [cm]
    Delta_Rp = 0.52 * R_p;               % [cm]
elseif strcmp(dopant, 'Phosphorus')
    R_p = 2.5e-6 * E_implant^1.2;
    Delta_Rp = 0.45 * R_p;
elseif strcmp(dopant, 'Arsenic')
    R_p = 1.8e-6 * E_implant^1.1;
    Delta_Rp = 0.35 * R_p;
else
    % Generic formula
    R_p = 3e-6 * E_implant^1.2;
    Delta_Rp = 0.5 * R_p;
end

fprintf('LSS Theory Results:\n');
fprintf('  Projected range R_p: %.2f nm\n', R_p*1e7);
fprintf('  Straggle ΔR_p: %.2f nm\n', Delta_Rp*1e7);
fprintf('  Peak concentration: %.2e cm⁻³\n\n', dose/(sqrt(2*pi)*Delta_Rp));

%% Depth Profile (Gaussian Distribution)

% Depth array
x = linspace(0, 5*R_p, 1000);  % Depth [cm]

% Gaussian profile
N_gaussian = (dose / (sqrt(2*pi) * Delta_Rp)) * ...
             exp(-0.5 * ((x - R_p) / Delta_Rp).^2);

% Peak concentration
N_peak = dose / (sqrt(2*pi) * Delta_Rp);

%% Multi-Energy Implant (for uniform profiles)

% Multiple energies to create box-like profile
energies = [20, 40, 60, 80, 100];  % [keV]
doses_multi = [2e13, 2e13, 2e13, 2e13, 2e13];  % [ions/cm²]

N_multi = zeros(size(x));

for i = 1:length(energies)
    E_i = energies(i);
    dose_i = doses_multi(i);
    
    % Calculate range and straggle for each energy
    R_p_i = 3.66e-6 * E_i^1.24;
    Delta_Rp_i = 0.52 * R_p_i;
    
    % Add Gaussian profile
    N_multi = N_multi + (dose_i / (sqrt(2*pi) * Delta_Rp_i)) * ...
              exp(-0.5 * ((x - R_p_i) / Delta_Rp_i).^2);
end

%% Annealing and Diffusion

% Annealing conditions
T_anneal = 1000 + 273;  % Temperature [K] (1000°C)
t_anneal = 30 * 60;     % Time [s] (30 minutes)

% Diffusion coefficient (Arrhenius)
D_0 = 0.76;             % Pre-exponential factor [cm²/s] for B in Si
E_a = 3.46;             % Activation energy [eV]
D = D_0 * exp(-E_a / (k_B * T_anneal / q));  % [cm²/s]

% Diffusion length
L_diff = sqrt(2 * D * t_anneal);  % [cm]

% Annealed profile (convolution with Gaussian diffusion kernel)
Delta_total = sqrt(Delta_Rp^2 + L_diff^2);
N_annealed = (dose / (sqrt(2*pi) * Delta_total)) * ...
             exp(-0.5 * ((x - R_p) / Delta_total).^2);

fprintf('Annealing Parameters:\n');
fprintf('  Temperature: %.0f°C\n', T_anneal - 273);
fprintf('  Time: %.0f minutes\n', t_anneal/60);
fprintf('  Diffusion coefficient D: %.2e cm²/s\n', D);
fprintf('  Diffusion length: %.2f nm\n', L_diff*1e7);
fprintf('  Total straggle after anneal: %.2f nm\n\n', Delta_total*1e7);

%% Junction Depth Calculation

% Find junction depth (where N = N_substrate)
idx_junction = find(N_annealed >= N_substrate, 1, 'last');
if ~isempty(idx_junction)
    x_j = x(idx_junction);
    fprintf('Junction Depth:\n');
    fprintf('  x_j = %.3f µm\n\n', x_j*1e4);
else
    x_j = NaN;
    fprintf('Junction depth: Not found (dose too low)\n\n');
end

%% Sheet Resistance

% Sheet resistance calculation
R_sheet = 1 / (q * trapz(x, N_annealed * 400));  % Assume mobility = 400 cm²/V·s

fprintf('Electrical Properties:\n');
fprintf('  Sheet resistance R_s: %.1f Ω/sq\n\n', R_sheet);

%% Plotting

figure('Position', [100, 100, 1400, 900]);

% Plot 1: Single Energy Gaussian Profile
subplot(2, 3, 1);
semilogy(x*1e4, N_gaussian, 'b-', 'LineWidth', 2.5);
hold on;
semilogy(x*1e4, N_substrate*ones(size(x)), 'r--', 'LineWidth', 1.5);
semilogy([R_p*1e4, R_p*1e4], [1e12, 1e20], 'k--', 'LineWidth', 1);
xlabel('Depth [µm]', 'FontSize', 11);
ylabel('Concentration [cm^{-3}]', 'FontSize', 11);
title(sprintf('Gaussian Profile (%d keV)', E_implant), 'FontSize', 13, 'FontWeight', 'bold');
grid on;
legend('Implanted', 'Substrate', 'R_p', 'Location', 'northeast');
xlim([0, max(x)*1e4]);
ylim([1e13, 1e20]);

% Plot 2: As-Implanted vs Annealed
subplot(2, 3, 2);
semilogy(x*1e4, N_gaussian, 'b-', 'LineWidth', 2);
hold on;
semilogy(x*1e4, N_annealed, 'r-', 'LineWidth', 2);
semilogy(x*1e4, N_substrate*ones(size(x)), 'k--', 'LineWidth', 1.5);
if ~isnan(x_j)
    semilogy([x_j*1e4, x_j*1e4], [1e13, 1e20], 'g--', 'LineWidth', 1.5);
end
xlabel('Depth [µm]', 'FontSize', 11);
ylabel('Concentration [cm^{-3}]', 'FontSize', 11);
title('Effect of Annealing', 'FontSize', 13, 'FontWeight', 'bold');
grid on;
legend('As-implanted', sprintf('Annealed (%.0f°C, %.0fmin)', T_anneal-273, t_anneal/60), ...
       'Substrate', 'x_j', 'Location', 'northeast');
xlim([0, max(x)*1e4]);
ylim([1e13, 1e20]);

% Plot 3: Multi-Energy Implant
subplot(2, 3, 3);
semilogy(x*1e4, N_multi, 'g-', 'LineWidth', 2.5);
hold on;
semilogy(x*1e4, N_gaussian, 'b--', 'LineWidth', 1.5);
xlabel('Depth [µm]', 'FontSize', 11);
ylabel('Concentration [cm^{-3}]', 'FontSize', 11);
title('Multi-Energy Implant', 'FontSize', 13, 'FontWeight', 'bold');
grid on;
legend('Multi-energy', sprintf('Single (%dkeV)', E_implant), 'Location', 'northeast');
xlim([0, max(x)*1e4]);
ylim([1e15, 1e20]);

% Plot 4: Energy vs Range
subplot(2, 3, 4);
E_range = 10:10:200;  % Energy range [keV]
R_p_range = 3.66e-6 * E_range.^1.24;
Delta_Rp_range = 0.52 * R_p_range;

plot(E_range, R_p_range*1e7, 'b-', 'LineWidth', 2.5);
hold on;
plot(E_range, (R_p_range + Delta_Rp_range)*1e7, 'r--', 'LineWidth', 1.5);
plot(E_range, (R_p_range - Delta_Rp_range)*1e7, 'r--', 'LineWidth', 1.5);
plot([E_implant, E_implant], [0, max(R_p_range)*1e7*1.5], 'k--', 'LineWidth', 1);
xlabel('Energy [keV]', 'FontSize', 11);
ylabel('Depth [nm]', 'FontSize', 11);
title('Range vs. Energy (B in Si)', 'FontSize', 13, 'FontWeight', 'bold');
grid on;
legend('R_p', 'R_p±ΔR_p', '', 'Current', 'Location', 'northwest');

% Plot 5: Dose vs Peak Concentration
subplot(2, 3, 5);
dose_range = logspace(12, 16, 100);
N_peak_range = dose_range / (sqrt(2*pi) * Delta_Rp);

loglog(dose_range, N_peak_range, 'b-', 'LineWidth', 2.5);
hold on;
loglog([dose, dose], [1e14, 1e21], 'r--', 'LineWidth', 1.5);
loglog([1e12, 1e16], [N_substrate, N_substrate], 'k--', 'LineWidth', 1.5);
xlabel('Dose [ions/cm^2]', 'FontSize', 11);
ylabel('Peak Concentration [cm^{-3}]', 'FontSize', 11);
title('Peak Concentration vs. Dose', 'FontSize', 13, 'FontWeight', 'bold');
grid on;
legend('N_{peak}', 'Current dose', 'Substrate', 'Location', 'northwest');

% Plot 6: Diffusion Time vs Junction Depth
subplot(2, 3, 6);
t_range = logspace(1, 4, 100);  % 10s to 10000s
x_j_range = zeros(size(t_range));

for i = 1:length(t_range)
    L_diff_i = sqrt(2 * D * t_range(i));
    Delta_total_i = sqrt(Delta_Rp^2 + L_diff_i^2);
    N_temp = (dose / (sqrt(2*pi) * Delta_total_i)) * ...
             exp(-0.5 * ((x - R_p) / Delta_total_i).^2);
    idx = find(N_temp >= N_substrate, 1, 'last');
    if ~isempty(idx)
        x_j_range(i) = x(idx);
    else
        x_j_range(i) = NaN;
    end
end

semilogx(t_range/60, x_j_range*1e4, 'b-', 'LineWidth', 2.5);
hold on;
semilogx([t_anneal/60, t_anneal/60], [0, max(x_j_range)*1e4*1.2], 'r--', 'LineWidth', 1.5);
xlabel('Anneal Time [minutes]', 'FontSize', 11);
ylabel('Junction Depth [µm]', 'FontSize', 11);
title(sprintf('Junction Depth vs. Time (%.0f°C)', T_anneal-273), 'FontSize', 13, 'FontWeight', 'bold');
grid on;
legend('x_j(t)', 'Current time', 'Location', 'northwest');

sgtitle('Ion Implantation Profile Analysis', 'FontSize', 15, 'FontWeight', 'bold');

%% Save Figure
if ~exist('images', 'dir')
    mkdir('images');
end
saveas(gcf, 'images/ion_implant_profile.png');
fprintf('✓ Saved: images/ion_implant_profile.png\n\n');

%% Summary Report

fprintf('==============================================================\n');
fprintf('Summary Report\n');
fprintf('==============================================================\n\n');

fprintf('Implantation Results:\n');
fprintf('  Projected range R_p: %.2f nm\n', R_p*1e7);
fprintf('  Straggle ΔR_p: %.2f nm\n', Delta_Rp*1e7);
fprintf('  Peak concentration: %.2e cm⁻³\n', N_peak);
fprintf('  Surface concentration: %.2e cm⁻³\n', N_gaussian(1));

fprintf('\nPost-Annealing Results:\n');
fprintf('  Diffusion coefficient: %.2e cm²/s\n', D);
fprintf('  Diffusion length: %.2f nm\n', L_diff*1e7);
fprintf('  Total straggle: %.2f nm\n', Delta_total*1e7);
if ~isnan(x_j)
    fprintf('  Junction depth x_j: %.3f µm\n', x_j*1e4);
end
fprintf('  Sheet resistance: %.1f Ω/sq\n', R_sheet);

fprintf('\nDose Distribution:\n');
fprintf('  Total implanted dose: %.2e ions/cm²\n', dose);
dose_integrated = trapz(x, N_annealed);
fprintf('  Integrated dose (after anneal): %.2e ions/cm²\n', dose_integrated);
fprintf('  Dose retention: %.1f%%\n', dose_integrated/dose*100);

fprintf('\n==============================================================\n');

%% Design Guidelines

fprintf('\nDesign Guidelines:\n');
fprintf('──────────────────────────────────────────────────────────────\n');
fprintf('Energy Selection:\n');
fprintf('  • Low energy (5-20 keV): Shallow junctions (<50 nm)\n');
fprintf('  • Medium energy (20-80 keV): Source/drain extensions\n');
fprintf('  • High energy (80-200 keV): Deep wells, buried layers\n\n');

fprintf('Dose Selection:\n');
fprintf('  • Low dose (1e12-1e13 cm⁻²): Threshold adjust, lightly doped\n');
fprintf('  • Medium dose (1e13-1e14 cm⁻²): LDD, moderate doping\n');
fprintf('  • High dose (1e15-1e16 cm⁻²): Source/drain, heavily doped\n\n');

fprintf('Annealing Considerations:\n');
fprintf('  • RTA (Rapid Thermal Anneal): 1000-1100°C, 1-30 seconds\n');
fprintf('  • Spike anneal: >1100°C, <1 second (minimal diffusion)\n');
fprintf('  • Furnace anneal: 800-1000°C, 10-60 minutes (more diffusion)\n\n');

fprintf('Tilt Angle:\n');
fprintf('  • 0°: Maximum channeling (avoid!)\n');
fprintf('  • 7°: Standard tilt (compromise)\n');
fprintf('  • Quad implant (4×7°): Minimize channeling completely\n\n');

fprintf('Typical Junction Depths:\n');
fprintf('  • Ultra-shallow (14nm node): 5-15 nm\n');
fprintf('  • Shallow (65nm node): 30-60 nm\n');
fprintf('  • Moderate (180nm node): 100-200 nm\n');
fprintf('  • Deep wells: 1-3 µm\n');
fprintf('──────────────────────────────────────────────────────────────\n');

fprintf('\n==============================================================\n');
fprintf('Analysis complete!\n');
fprintf('==============================================================\n');