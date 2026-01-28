%% Squeeze-Film Damping Analysis for MEMS Devices
% ================================================
%
% Calculates squeeze-film damping coefficient and quality factor
% for MEMS structures oscillating parallel to a substrate.
%
% Author: Silicon Fabrication Handbook
% License: MIT
% Date: January 2026

clear; close all; clc;

fprintf('==============================================================\n');
fprintf('Squeeze-Film Damping Analysis for MEMS\n');
fprintf('==============================================================\n\n');

%% Device Parameters
% Geometry
L = 100e-6;         % Plate length [m] (100 µm)
W = 100e-6;         % Plate width [m] (100 µm)
h = 2e-6;           % Gap height [m] (2 µm)
t = 2e-6;           % Plate thickness [m] (2 µm)

% Material properties (Silicon)
rho = 2330;         % Density [kg/m³]
E = 170e9;          % Young's modulus [Pa]

% Air properties (at 1 atm, 20°C)
mu_air = 1.81e-5;   % Dynamic viscosity [Pa·s]
P_atm = 101325;     % Atmospheric pressure [Pa]
lambda_mfp = 65e-9; % Mean free path [m] (65 nm)

% Calculated parameters
m = rho * L * W * t;        % Mass [kg]
A = L * W;                  % Plate area [m²]
Kn = lambda_mfp / h;        % Knudsen number

fprintf('Device Geometry:\n');
fprintf('  Plate: %.0f × %.0f × %.0f µm³\n', L*1e6, W*1e6, t*1e6);
fprintf('  Gap: %.1f µm\n', h*1e6);
fprintf('  Area: %.1f × 10⁻⁸ m²\n', A*1e8);
fprintf('  Mass: %.2f ng\n', m*1e9);
fprintf('  Knudsen number: %.3f\n\n', Kn);

%% Damping Coefficient Calculation

% Pressure number (for compressibility effects)
omega = 2*pi*10e3;  % Assumed frequency [rad/s] (10 kHz)
sigma = (12*mu_air*omega*L^2)/(P_atm*h^2);  % Squeeze number

% Effective viscosity (rarefaction correction)
Q_eff = 1/(1 + 2*Kn);  % Effective quality factor correction

% Damping coefficient (parallel plate, no holes)
b_squeeze = (mu_air * L^4 * W)/(h^3) * Q_eff;  % Simplified

% More accurate formula (border effects)
b_border = 0.42 * (mu_air * (L^3 * W + L * W^3)) / h^3 * Q_eff;

% Total damping
b_total = b_squeeze + b_border;

fprintf('Damping Analysis:\n');
fprintf('  Squeeze damping: %.3e N·s/m\n', b_squeeze);
fprintf('  Border damping: %.3e N·s/m\n', b_border);
fprintf('  Total damping: %.3e N·s/m\n', b_total);
fprintf('  Rarefaction correction Q_eff: %.3f\n\n', Q_eff);

%% Quality Factor vs. Pressure

% Pressure range (from vacuum to atmospheric)
P_range = logspace(0, 5, 100);  % 1 Pa to 100 kPa

% Spring constant (assumed)
k = 10;  % N/m (typical for MEMS)
omega_n = sqrt(k/m);
f_n = omega_n/(2*pi);

% Quality factor vs pressure
Q_factor = zeros(size(P_range));

for i = 1:length(P_range)
    % Update mean free path with pressure
    lambda_p = lambda_mfp * P_atm / P_range(i);
    Kn_p = lambda_p / h;
    Q_eff_p = 1/(1 + 2*Kn_p);
    
    % Damping coefficient
    b_p = (mu_air * L^4 * W)/(h^3) * Q_eff_p;
    
    % Quality factor
    Q_factor(i) = m * omega_n / b_p;
end

% Plot Q vs Pressure
figure('Position', [100, 100, 1000, 600]);

subplot(2, 2, 1);
loglog(P_range/1e3, Q_factor, 'b-', 'LineWidth', 2);
hold on;
loglog([P_atm/1e3, P_atm/1e3], [min(Q_factor), max(Q_factor)], 'r--', 'LineWidth', 1.5);
xlabel('Pressure [kPa]', 'FontSize', 11);
ylabel('Quality Factor Q', 'FontSize', 11);
title('Quality Factor vs. Pressure', 'FontSize', 13, 'FontWeight', 'bold');
grid on;
legend('Q-factor', '1 atm', 'Location', 'northwest');
text(P_atm/1e3*1.5, max(Q_factor)*0.8, sprintf('Q_{atm} = %.0f', Q_factor(end)), ...
     'FontSize', 10, 'Color', 'red');

%% Damping vs. Gap Height

h_range = logspace(-7, -5, 100);  % 0.1 to 10 µm
b_vs_h = zeros(size(h_range));
Q_vs_h = zeros(size(h_range));

for i = 1:length(h_range)
    Kn_h = lambda_mfp / h_range(i);
    Q_eff_h = 1/(1 + 2*Kn_h);
    b_vs_h(i) = (mu_air * L^4 * W)/(h_range(i)^3) * Q_eff_h;
    Q_vs_h(i) = m * omega_n / b_vs_h(i);
end

subplot(2, 2, 2);
loglog(h_range*1e6, b_vs_h, 'r-', 'LineWidth', 2);
hold on;
loglog([h*1e6, h*1e6], [min(b_vs_h), max(b_vs_h)], 'k--', 'LineWidth', 1.5);
xlabel('Gap Height [µm]', 'FontSize', 11);
ylabel('Damping Coefficient [N·s/m]', 'FontSize', 11);
title('Damping vs. Gap Height (b ∝ 1/h³)', 'FontSize', 13, 'FontWeight', 'bold');
grid on;
legend('b(h)', 'Current gap', 'Location', 'northeast');

%% Frequency Response with Damping

freq = logspace(2, 5, 1000);  % 100 Hz to 100 kHz
omega_freq = 2*pi*freq;

% Transfer function magnitude
H = zeros(size(omega_freq));
zeta = b_total/(2*sqrt(m*k));  % Damping ratio

for i = 1:length(omega_freq)
    w = omega_freq(i);
    H(i) = 1/sqrt((omega_n^2 - w^2)^2 + (2*zeta*omega_n*w)^2);
end

H_dB = 20*log10(H);

subplot(2, 2, 3);
semilogx(freq/1e3, H_dB, 'b-', 'LineWidth', 2);
hold on;
semilogx([f_n/1e3, f_n/1e3], [min(H_dB), max(H_dB)], 'r--', 'LineWidth', 1.5);
xlabel('Frequency [kHz]', 'FontSize', 11);
ylabel('Magnitude [dB]', 'FontSize', 11);
title(sprintf('Frequency Response (ζ = %.3f, Q = %.1f)', zeta, 1/(2*zeta)), ...
      'FontSize', 13, 'FontWeight', 'bold');
grid on;
legend('|H(f)|', 'f_n', 'Location', 'southwest');

%% Effect of Perforation Holes

% Hole parameters
d_hole = 5e-6;      % Hole diameter [m] (5 µm)
N_holes_range = [0, 10, 50, 100, 500];  % Number of holes
colors = lines(length(N_holes_range));

subplot(2, 2, 4);
hold on;

for j = 1:length(N_holes_range)
    N_holes = N_holes_range(j);
    
    % Effective area reduction
    A_holes = N_holes * pi * (d_hole/2)^2;
    phi = A_holes / A;  % Perforation ratio
    
    % Damping reduction factor (empirical)
    if N_holes > 0
        b_reduction = 1/(1 + phi*10);  % Simplified model
    else
        b_reduction = 1;
    end
    
    % Calculate Q vs pressure with holes
    Q_holes = zeros(size(P_range));
    for i = 1:length(P_range)
        lambda_p = lambda_mfp * P_atm / P_range(i);
        Kn_p = lambda_p / h;
        Q_eff_p = 1/(1 + 2*Kn_p);
        b_p = (mu_air * L^4 * W)/(h^3) * Q_eff_p * b_reduction;
        Q_holes(i) = m * omega_n / b_p;
    end
    
    loglog(P_range/1e3, Q_holes, 'LineWidth', 2, 'Color', colors(j,:), ...
           'DisplayName', sprintf('%d holes', N_holes));
end

xlabel('Pressure [kPa]', 'FontSize', 11);
ylabel('Quality Factor Q', 'FontSize', 11);
title('Effect of Perforation Holes', 'FontSize', 13, 'FontWeight', 'bold');
grid on;
legend('show', 'Location', 'northwest');
hold off;

sgtitle('Squeeze-Film Damping Analysis', 'FontSize', 15, 'FontWeight', 'bold');

%% Save Figure
if ~exist('images', 'dir')
    mkdir('images');
end
saveas(gcf, 'images/squeeze_film_damping.png');
fprintf('✓ Saved: images/squeeze_film_damping.png\n\n');

%% Summary Report

fprintf('==============================================================\n');
fprintf('Summary Report\n');
fprintf('==============================================================\n\n');

fprintf('Natural Frequency:\n');
fprintf('  f_n = %.2f kHz\n', f_n/1e3);
fprintf('  ω_n = %.2e rad/s\n\n', omega_n);

fprintf('Damping Characteristics (at 1 atm):\n');
fprintf('  Damping coefficient: %.3e N·s/m\n', b_total);
fprintf('  Damping ratio ζ: %.4f\n', zeta);
fprintf('  Quality factor Q: %.1f\n', 1/(2*zeta));
fprintf('  Viscous damping time τ: %.2f ms\n\n', m/b_total*1e3);

fprintf('Regime Classification:\n');
if Kn < 0.01
    fprintf('  Continuum regime (Kn < 0.01)\n');
    fprintf('  Navier-Stokes equations valid\n');
elseif Kn < 0.1
    fprintf('  Slip flow regime (0.01 < Kn < 0.1)\n');
    fprintf('  Velocity slip at boundaries\n');
else
    fprintf('  Transition/Free molecular regime (Kn > 0.1)\n');
    fprintf('  Rarefied gas effects significant\n');
end
fprintf('\n');

fprintf('Design Recommendations:\n');
fprintf('  1. To reduce damping (increase Q):\n');
fprintf('     • Increase gap height h (Q ∝ h³)\n');
fprintf('     • Add perforation holes (venting)\n');
fprintf('     • Operate in vacuum (P < 1 kPa)\n');
fprintf('  2. To increase damping (decrease Q):\n');
fprintf('     • Decrease gap height h\n');
fprintf('     • Remove perforation holes\n');
fprintf('     • Operate at atmospheric pressure\n\n');

fprintf('Typical MEMS Values:\n');
fprintf('  Consumer accelerometer: Q = 10-100 (air damped)\n');
fprintf('  Gyroscope: Q = 1,000-10,000 (vacuum packaged)\n');
fprintf('  Resonator: Q = 10,000-100,000 (high vacuum)\n\n');

fprintf('==============================================================\n');
fprintf('Analysis complete!\n');
fprintf('==============================================================\n');