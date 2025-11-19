%% MEMS Capacitive Sensor Model and Simulation
% ============================================
% This script models a MEMS capacitive sensor (e.g., accelerometer or pressure
% sensor) and simulates its electrical characteristics including:
% - Capacitance vs. displacement
% - Pull-in voltage
% - Electrostatic force
% - C-V characteristics
% - Sensitivity analysis
%
% Author: Silicon Fabrication Handbook Contributors
% License: MIT

clear; close all; clc;

%% Physical Constants
epsilon_0 = 8.854e-12;  % Vacuum permittivity [F/m]
epsilon_r_air = 1.0;    % Relative permittivity of air

%% Device Geometry Parameters
% Parallel plate capacitor structure
L = 200e-6;      % Plate length [m] (200 μm)
W = 50e-6;       % Plate width [m] (50 μm)
g0 = 2e-6;       % Initial gap [m] (2 μm)
t = 10e-6;       % Structural thickness [m] (10 μm)

% Calculate effective area
A = L * W;       % Overlap area [m²]

% Mechanical properties (Silicon)
E = 169e9;       % Young's modulus [Pa]
k_spring = 50;   % Spring constant [N/m] (from spring design)

%% Display Device Specifications
fprintf('\n=======================================================\n');
fprintf('MEMS CAPACITIVE SENSOR SPECIFICATIONS\n');
fprintf('=======================================================\n');
fprintf('Plate Dimensions:\n');
fprintf('  Length:          %0.1f μm\n', L*1e6);
fprintf('  Width:           %0.1f μm\n', W*1e6);
fprintf('  Thickness:       %0.1f μm\n', t*1e6);
fprintf('  Area:            %0.1f μm²\n', A*1e12);
fprintf('Initial Gap:       %0.2f μm\n', g0*1e6);
fprintf('Spring Constant:   %0.2f N/m\n', k_spring);
fprintf('=======================================================\n\n');

%% Function Definitions

% Capacitance as function of gap
capacitance = @(g) epsilon_0 * epsilon_r_air * A ./ g;

% Electrostatic force (attractive)
force_elec = @(V, g) 0.5 * epsilon_0 * A * V.^2 ./ g.^2;

% Spring restoring force
force_spring = @(x) k_spring * x;

% Pull-in voltage calculation
V_pullin = sqrt((8 * k_spring * g0^3) / (27 * epsilon_0 * A));

%% 1. C-V Characteristics at Different Displacements
fprintf('Calculating C-V characteristics...\n');

% Define displacement range (0 to 80% of gap to avoid pull-in)
x_range = linspace(0, 0.8*g0, 50);
V_range = linspace(0, 0.9*V_pullin, 100);

% Calculate capacitance matrix
C_matrix = zeros(length(x_range), length(V_range));
for i = 1:length(x_range)
    % Effective gap decreases as plate moves
    g_eff = g0 - x_range(i);
    
    % For each voltage, calculate equilibrium position
    for j = 1:length(V_range)
        % At equilibrium: F_elec = F_spring
        % This is simplified - actual device has voltage-dependent position
        C_matrix(i,j) = capacitance(g_eff);
    end
end

% Initial capacitance
C0 = capacitance(g0);

%% 2. Pull-in Analysis
fprintf('Analyzing pull-in instability...\n');

% At pull-in: V = V_pullin, x = g0/3
x_pullin = g0/3;
C_pullin = capacitance(g0 - x_pullin);

fprintf('\nPull-in Analysis:\n');
fprintf('  Pull-in Voltage:      %0.2f V\n', V_pullin);
fprintf('  Pull-in Distance:     %0.3f μm (1/3 of gap)\n', x_pullin*1e6);
fprintf('  Initial Capacitance:  %0.3f fF\n', C0*1e15);
fprintf('  Pull-in Capacitance:  %0.3f fF\n', C_pullin*1e15);
fprintf('  Capacitance Change:   %0.1f%%\n', (C_pullin/C0 - 1)*100);

%% 3. Voltage-Displacement Equilibrium
% Solve for equilibrium position at each voltage
V_eq = linspace(0, 0.95*V_pullin, 200);
x_eq = zeros(size(V_eq));

for i = 1:length(V_eq)
    % Solve equilibrium equation: k*x = 0.5*ε*A*V²/(g0-x)²
    % Rearrange: k*x*(g0-x)² = 0.5*ε*A*V²
    
    % Use fzero to find equilibrium
    eq_func = @(x) force_spring(x) - force_elec(V_eq(i), g0-x);
    
    if V_eq(i) < V_pullin
        x_eq(i) = fzero(eq_func, [0, g0/3]);
    else
        x_eq(i) = NaN;  % Beyond pull-in
    end
end

% Calculate corresponding capacitance
C_eq = capacitance(g0 - x_eq);

%% 4. Sensitivity Analysis
fprintf('\nSensitivity Analysis:\n');

% Small-signal sensitivity: dC/dx at zero bias
dC_dx = epsilon_0 * A / g0^2;
sensitivity_mechanical = dC_dx;  % [F/m]

fprintf('  Mechanical Sensitivity (dC/dx): %0.3f fF/μm\n', dC_dx*1e15*1e6);

% For 1 fF capacitance change, required displacement:
delta_C_target = 1e-15;  % 1 fF
delta_x_for_1fF = delta_C_target / dC_dx;
fprintf('  Displacement for 1 fF change:   %0.3f nm\n', delta_x_for_1fF*1e9);

% Electromechanical sensitivity: dx/dV at operating point
V_op = 0.5 * V_pullin;  % Typical operating voltage
x_op = fzero(@(x) force_spring(x) - force_elec(V_op, g0-x), [0, g0/3]);
dFelec_dx = epsilon_0 * A * V_op^2 / (g0-x_op)^3;
dx_dV = (epsilon_0 * A * V_op) / ((g0-x_op)^2 * (k_spring + dFelec_dx));
fprintf('  Electromechanical (dx/dV):      %0.3f nm/V\n', dx_dV*1e9);

%% 5. Frequency Response (Resonant Behavior)
fprintf('\nCalculating frequency response...\n');

% Assuming proof mass m and damping b
m = 5e-9;        % Mass [kg] (5 nanograms - typical)
Q = 100;         % Quality factor (vacuum packaged)

omega_n = sqrt(k_spring / m);
f_n = omega_n / (2*pi);
b = k_spring / (Q * omega_n);

fprintf('  Resonant Frequency:   %0.2f kHz\n', f_n/1e3);
fprintf('  Quality Factor:       %0.1f\n', Q);
fprintf('  Damping Coefficient:  %0.2e N·s/m\n', b);

%% Plotting Results

%% Figure 1: Capacitance vs Gap
figure('Position', [100, 100, 1200, 800], 'Name', 'MEMS Capacitor Analysis');

subplot(2,3,1)
g_plot = linspace(0.2*g0, 1.5*g0, 200);
C_plot = capacitance(g_plot) * 1e15;  % Convert to fF
plot(g_plot*1e6, C_plot, 'b-', 'LineWidth', 2);
hold on;
plot(g0*1e6, C0*1e15, 'ro', 'MarkerSize', 10, 'MarkerFaceColor', 'r');
grid on;
xlabel('Gap Distance (μm)', 'FontSize', 11);
ylabel('Capacitance (fF)', 'FontSize', 11);
title('Capacitance vs. Gap', 'FontSize', 12, 'FontWeight', 'bold');
legend('C(g)', sprintf('Initial: %.2f fF', C0*1e15), 'Location', 'northeast');
set(gca, 'FontSize', 10);

%% Figure 2: C-V Curve at Zero Displacement
subplot(2,3,2)
V_cv = linspace(0, 0.95*V_pullin, 100);
C_cv = capacitance(g0) * ones(size(V_cv)) * 1e15;
plot(V_cv, C_cv, 'g-', 'LineWidth', 2);
hold on;
xline(V_pullin, 'r--', 'LineWidth', 2, 'Label', sprintf('V_{pull-in} = %.2fV', V_pullin));
grid on;
xlabel('Applied Voltage (V)', 'FontSize', 11);
ylabel('Capacitance (fF)', 'FontSize', 11);
title('C-V at Zero Bias (Rigid Plate)', 'FontSize', 12, 'FontWeight', 'bold');
xlim([0, V_pullin*1.1]);
set(gca, 'FontSize', 10);

%% Figure 3: Electrostatic Force vs Displacement
subplot(2,3,3)
x_force = linspace(0, 0.9*g0, 200);
V_forces = [5, 10, 15, 20];  % Different voltages
colors = {'b', 'g', 'r', 'm'};

for i = 1:length(V_forces)
    F_elec_plot = force_elec(V_forces(i), g0 - x_force) * 1e9;  % Convert to nN
    plot(x_force*1e6, F_elec_plot, colors{i}, 'LineWidth', 2, ...
         'DisplayName', sprintf('V = %d V', V_forces(i)));
    hold on;
end

% Add spring force
F_spring_plot = force_spring(x_force) * 1e9;
plot(x_force*1e6, F_spring_plot, 'k--', 'LineWidth', 2, 'DisplayName', 'Spring Force');

grid on;
xlabel('Displacement (μm)', 'FontSize', 11);
ylabel('Force (nN)', 'FontSize', 11);
title('Electrostatic vs. Spring Force', 'FontSize', 12, 'FontWeight', 'bold');
legend('Location', 'northwest', 'FontSize', 9);
set(gca, 'FontSize', 10);

%% Figure 4: Equilibrium Displacement vs Voltage
subplot(2,3,4)
plot(V_eq, x_eq*1e6, 'b-', 'LineWidth', 2);
hold on;
plot(V_pullin, x_pullin*1e6, 'ro', 'MarkerSize', 10, 'MarkerFaceColor', 'r');
xline(V_pullin, 'r--', 'LineWidth', 1.5);
yline(g0*1e6/3, 'r--', 'LineWidth', 1.5);
grid on;
xlabel('Applied Voltage (V)', 'FontSize', 11);
ylabel('Displacement (μm)', 'FontSize', 11);
title('Voltage-Displacement Curve', 'FontSize', 12, 'FontWeight', 'bold');
legend('Equilibrium', 'Pull-in Point', 'Location', 'northwest');
xlim([0, V_pullin*1.1]);
ylim([0, g0*1e6]);
set(gca, 'FontSize', 10);

%% Figure 5: Capacitance vs Voltage (with displacement)
subplot(2,3,5)
plot(V_eq, C_eq*1e15, 'b-', 'LineWidth', 2);
hold on;
plot(V_pullin, C_pullin*1e15, 'ro', 'MarkerSize', 10, 'MarkerFaceColor', 'r');
xline(V_pullin, 'r--', 'LineWidth', 1.5, 'Label', 'Pull-in');
grid on;
xlabel('Applied Voltage (V)', 'FontSize', 11);
ylabel('Capacitance (fF)', 'FontSize', 11);
title('C-V Characteristic (Compliant)', 'FontSize', 12, 'FontWeight', 'bold');
legend('C(V) with displacement', 'Pull-in', 'Location', 'northwest');
xlim([0, V_pullin*1.1]);
set(gca, 'FontSize', 10);

%% Figure 6: Sensitivity Map
subplot(2,3,6)
V_sens = linspace(0, 0.9*V_pullin, 50);
x_sens = linspace(0, 0.8*g0, 50);
[V_mesh, X_mesh] = meshgrid(V_sens, x_sens);

% Calculate capacitance sensitivity at each point
Sens_map = epsilon_0 * A ./ (g0 - X_mesh).^2 * 1e15 * 1e6;  % fF/μm

contourf(V_mesh, X_mesh*1e6, Sens_map, 20);
colorbar;
xlabel('Voltage (V)', 'FontSize', 11);
ylabel('Displacement (μm)', 'FontSize', 11);
title('Sensitivity Map (dC/dx in fF/μm)', 'FontSize', 12, 'FontWeight', 'bold');
set(gca, 'FontSize', 10);

%% Save Results
fprintf('\nSaving plots...\n');
saveas(gcf, 'capacitive_sensor_analysis.png');

%% Additional Analysis: Noise Floor
fprintf('\n=======================================================\n');
fprintf('NOISE ANALYSIS\n');
fprintf('=======================================================\n');

k_B = 1.38e-23;  % Boltzmann constant [J/K]
T = 300;         % Temperature [K]

% Thermomechanical noise
x_thermal = sqrt(k_B * T / k_spring) * 1e9;  % [nm]
C_noise = sensitivity_mechanical * x_thermal * 1e-9 * 1e15;  % [fF]

fprintf('Thermomechanical Noise:\n');
fprintf('  Position noise:       %0.3f pm RMS\n', x_thermal*1e3);
fprintf('  Capacitance noise:    %0.3f aF RMS\n', C_noise*1e3);

% Electronic noise (assuming readout circuit)
% Typical capacitance readout: 10 aF/√Hz @ 1 kHz
C_elec_noise = 10e-18;  % [F/√Hz]
BW = f_n;               % Measurement bandwidth [Hz]
C_total_noise = sqrt(C_noise^2 + (C_elec_noise * sqrt(BW))^2);

fprintf('  Total capacitance noise (@ %0.1f kHz BW): %0.3f fF RMS\n', ...
        BW/1e3, C_total_noise);

% Minimum detectable displacement
x_min = C_total_noise / (sensitivity_mechanical * 1e15) * 1e9;
fprintf('  Minimum detectable displacement: %0.3f nm\n', x_min);

fprintf('=======================================================\n\n');

%% Design Space Exploration
fprintf('Design Space Exploration:\n');
fprintf('Effect of varying key parameters:\n\n');

% Vary gap
gaps = [1e-6, 2e-6, 3e-6, 5e-6];
fprintf('Gap Variation (fixed A = %0.1f μm²):\n', A*1e12);
for i = 1:length(gaps)
    C_temp = capacitance(gaps(i));
    V_pi_temp = sqrt((8 * k_spring * gaps(i)^3) / (27 * epsilon_0 * A));
    fprintf('  g = %0.1f μm: C0 = %0.2f fF, V_pullin = %0.2f V\n', ...
            gaps(i)*1e6, C_temp*1e15, V_pi_temp);
end

% Vary area
fprintf('\nArea Variation (fixed g = %0.1f μm):\n', g0*1e6);
areas = [50e-6*50e-6, 100e-6*100e-6, 200e-6*100e-6, 200e-6*200e-6];
for i = 1:length(areas)
    C_temp = epsilon_0 * areas(i) / g0;
    V_pi_temp = sqrt((8 * k_spring * g0^3) / (27 * epsilon_0 * areas(i)));
    fprintf('  A = %0.1f μm²: C0 = %0.2f fF, V_pullin = %0.2f V\n', ...
            areas(i)*1e12, C_temp*1e15, V_pi_temp);
end

fprintf('\n=======================================================\n');
fprintf('Analysis Complete!\n');
fprintf('=======================================================\n\n');

%% Export Data
% Save key results to CSV for further analysis
results_table = table(V_eq', x_eq'*1e6, C_eq'*1e15, ...
    'VariableNames', {'Voltage_V', 'Displacement_um', 'Capacitance_fF'});
writetable(results_table, 'capacitor_cv_data.csv');
fprintf('Data exported to: capacitor_cv_data.csv\n\n');
