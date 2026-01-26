%% MEMS Spring Design & Comprehensive Analysis Tool
% Complete design suite for folded beam, serpentine, and crab-leg springs
% Includes mechanical, dynamic, thermal, and reliability analysis
% Perfect for MEMS accelerometers, gyroscopes, and resonators

clear; close all; clc;

%% ============================================================
%  SECTION 1: MATERIAL PROPERTIES
%% ============================================================

fprintf('=== MEMS Spring Design Tool ===\n\n');

% Silicon Material Properties
mat.E = 169e9;              % Young's modulus [Pa] (Si <110>)
mat.rho = 2329;             % Density [kg/m³]
mat.nu = 0.064;             % Poisson's ratio
mat.sigma_yield = 7e9;      % Yield strength [Pa]
mat.alpha = 2.6e-6;         % Thermal expansion coefficient [1/K]
mat.k_thermal = 148;        % Thermal conductivity [W/m·K]

% Design Parameters (all in micrometers initially)
design.L = 200;             % Beam length [μm]
design.w = 4;               % Beam width [μm]
design.t = 10;              % Beam thickness [μm]
design.N_beams = 4;         % Number of beams (for folded spring)
design.mass = 1e-9;         % Proof mass [kg] (1 μg typical)

% Convert to SI units
L = design.L * 1e-6;        % [m]
w = design.w * 1e-6;        % [m]
t = design.t * 1e-6;        % [m]
m_proof = design.mass;      % [kg]

%% ============================================================
%  SECTION 2: SPRING TYPE SELECTION & GEOMETRY
%% ============================================================

fprintf('Available Spring Geometries:\n');
fprintf('1. Folded Beam (symmetric, high linearity)\n');
fprintf('2. Serpentine (compact, moderate stiffness)\n');
fprintf('3. Crab-leg (angled, lateral compliance)\n\n');

spring_type = 1;  % Default: Folded beam

switch spring_type
    case 1  % Folded Beam
        fprintf('Selected: FOLDED BEAM SPRING\n\n');
        % Each beam is a cantilever with end load
        % Total spring has N parallel beam pairs
        I = (w * t^3) / 12;     % Moment of inertia [m⁴]
        
        % Single beam stiffness (fixed-guided)
        k_single = (2 * mat.E * I) / (L^3);
        
        % Total stiffness (N beams in parallel)
        k_total = design.N_beams * k_single;
        
        % Effective length for stress analysis
        L_eff = L;
        geometry = 'Folded Beam';
        
    case 2  % Serpentine
        fprintf('Selected: SERPENTINE SPRING\n\n');
        % Multiple U-shaped segments
        N_segments = 3;
        L_segment = L / N_segments;
        I = (w * t^3) / 12;
        
        % Serpentine stiffness (series combination)
        k_segment = (mat.E * I) / (L_segment^3);
        k_total = k_segment / (2 * N_segments);
        
        L_eff = L;
        geometry = 'Serpentine';
        
    case 3  % Crab-leg
        fprintf('Selected: CRAB-LEG SPRING\n\n');
        % Angled beams for lateral compliance
        theta = 45 * pi/180;    % Angle [rad]
        L_angled = L / cos(theta);
        I = (w * t^3) / 12;
        
        % Effective stiffness with angle
        k_axial = (mat.E * w * t) / L_angled;
        k_total = design.N_beams * k_axial * sin(theta)^2;
        
        L_eff = L_angled;
        geometry = 'Crab-leg';
end

%% ============================================================
%  SECTION 3: MECHANICAL ANALYSIS
%% ============================================================

fprintf('--- Mechanical Characteristics ---\n');

% Spring constant
fprintf('Spring constant k: %.3f N/m\n', k_total);
fprintf('Compliance: %.3e m/N\n', 1/k_total);

% Displacement under load
F_test = [1e-6, 10e-6, 100e-6];  % Test forces [N]
delta = F_test / k_total * 1e6;   % Displacement [μm]

fprintf('\nDisplacement vs Force:\n');
for i = 1:length(F_test)
    fprintf('  F = %.1f μN → δ = %.3f μm\n', F_test(i)*1e6, delta(i));
end

% Maximum stress (at beam root)
delta_max = 10e-6;  % Max displacement [m]
F_max = k_total * delta_max;

% Bending stress: σ = M*c/I where M = F*L, c = t/2
M_max = F_max * L_eff;
c = t / 2;
sigma_max = (M_max * c) / I;

fprintf('\nStress Analysis (δ_max = %.1f μm):\n', delta_max*1e6);
fprintf('  Maximum force: %.2f μN\n', F_max*1e6);
fprintf('  Maximum stress: %.2f MPa\n', sigma_max/1e6);
fprintf('  Safety factor: %.1f\n', mat.sigma_yield/sigma_max);

% Check for yielding
if sigma_max > mat.sigma_yield
    warning('YIELDING DETECTED! Reduce displacement or redesign.');
else
    fprintf('  Status: SAFE (below yield strength)\n');
end

%% ============================================================
%  SECTION 4: DYNAMIC ANALYSIS
%% ============================================================

fprintf('\n--- Dynamic Characteristics ---\n');

% Natural frequency (spring-mass system)
f_natural = (1/(2*pi)) * sqrt(k_total / m_proof);
omega_natural = 2 * pi * f_natural;

fprintf('Natural frequency: %.2f kHz\n', f_natural/1000);
fprintf('Angular frequency: %.2f krad/s\n', omega_natural/1000);

% Quality factor (typical for silicon in air and vacuum)
Q_air = 10;         % In atmospheric pressure
Q_vacuum = 10000;   % In high vacuum

fprintf('Q-factor (air): %d\n', Q_air);
fprintf('Q-factor (vacuum): %d\n', Q_vacuum);

% Damping coefficient
c_air = sqrt(k_total * m_proof) / Q_air;
c_vacuum = sqrt(k_total * m_proof) / Q_vacuum;

% Frequency response (air environment)
freq = logspace(log10(f_natural/10), log10(f_natural*10), 500);
omega = 2*pi*freq;

% Transfer function: H(ω) = 1 / (1 - (ω/ω₀)² + j(ω/ω₀)/Q)
zeta_air = 1/(2*Q_air);  % Damping ratio
H = 1 ./ sqrt((1 - (omega/omega_natural).^2).^2 + ...
    (2*zeta_air*omega/omega_natural).^2);

% Bandwidth (3dB points)
BW_air = f_natural / Q_air;
fprintf('Bandwidth (air): %.2f Hz\n', BW_air);

%% ============================================================
%  SECTION 5: PARAMETRIC DESIGN SWEEP
%% ============================================================

fprintf('\n--- Design Space Exploration ---\n');

% Sweep beam width
w_range = linspace(2e-6, 10e-6, 50);
k_vs_w = zeros(size(w_range));
f_vs_w = zeros(size(w_range));
sigma_vs_w = zeros(size(w_range));

for i = 1:length(w_range)
    I_temp = (w_range(i) * t^3) / 12;
    k_temp = design.N_beams * (2 * mat.E * I_temp) / (L^3);
    k_vs_w(i) = k_temp;
    f_vs_w(i) = (1/(2*pi)) * sqrt(k_temp / m_proof);
    
    F_temp = k_temp * delta_max;
    M_temp = F_temp * L_eff;
    sigma_vs_w(i) = (M_temp * (t/2)) / I_temp;
end

% Sweep beam length
L_range = linspace(100e-6, 500e-6, 50);
k_vs_L = zeros(size(L_range));
f_vs_L = zeros(size(L_range));

for i = 1:length(L_range)
    k_temp = design.N_beams * (2 * mat.E * I) / (L_range(i)^3);
    k_vs_L(i) = k_temp;
    f_vs_L(i) = (1/(2*pi)) * sqrt(k_temp / m_proof);
end

fprintf('Design space sweep complete.\n');
fprintf('Width range: %.1f - %.1f μm\n', w_range(1)*1e6, w_range(end)*1e6);
fprintf('Length range: %.1f - %.1f μm\n', L_range(1)*1e6, L_range(end)*1e6);

%% ============================================================
%  SECTION 6: THERMAL ANALYSIS
%% ============================================================

fprintf('\n--- Thermal Analysis ---\n');

% Temperature range
T_ref = 300;        % Reference temperature [K]
T_range = -40:80;   % Operating temperature [°C]

% Thermal stress (fixed-fixed beams)
% σ_thermal = E * α * ΔT
delta_T = T_range;
sigma_thermal = mat.E * mat.alpha * abs(delta_T);

% Thermal displacement (for free expansion)
delta_thermal = mat.alpha * L * delta_T * 1e6;  % [μm]

fprintf('Temperature coefficient: %.2f ppm/K\n', mat.alpha*1e6);
fprintf('Thermal stress at ΔT=100°C: %.2f MPa\n', ...
    mat.E * mat.alpha * 100 / 1e6);

%% ============================================================
%  SECTION 7: RELIABILITY & FATIGUE ANALYSIS
%% ============================================================

fprintf('\n--- Reliability Analysis ---\n');

% Fatigue life estimation (based on stress amplitude)
% Using Basquin's law: N_f = (σ_f'/σ_a)^b
sigma_f_prime = mat.sigma_yield * 0.9;  % Fatigue strength coefficient
b = -0.1;  % Fatigue exponent (silicon)

% Oscillation amplitude
delta_osc = [1e-6, 5e-6, 10e-6];  % [m]
N_cycles = zeros(size(delta_osc));

for i = 1:length(delta_osc)
    F_osc = k_total * delta_osc(i);
    M_osc = F_osc * L_eff;
    sigma_a = (M_osc * c) / I;
    
    N_cycles(i) = (sigma_f_prime / sigma_a)^(1/b);
    
    fprintf('Amplitude %.1f μm → Cycles to failure: %.2e\n', ...
        delta_osc(i)*1e6, N_cycles(i));
end

% Shock survivability
g_shock = 1000;  % Shock acceleration [g]
a_shock = g_shock * 9.81;  % [m/s²]
F_shock = m_proof * a_shock;
delta_shock = F_shock / k_total * 1e6;  % [μm]

M_shock = F_shock * L_eff;
sigma_shock = (M_shock * c) / I;

fprintf('\nShock Survivability (%.0fg):\n', g_shock);
fprintf('  Shock displacement: %.2f μm\n', delta_shock);
fprintf('  Shock stress: %.2f MPa\n', sigma_shock/1e6);
if sigma_shock < mat.sigma_yield
    fprintf('  Status: SURVIVES\n');
else
    fprintf('  Status: FAILURE RISK\n');
end

%% ============================================================
%  SECTION 8: COMPREHENSIVE VISUALIZATION
%% ============================================================

figure('Position', [50, 50, 1400, 900], 'Color', 'w');

% Plot 1: Frequency Response
subplot(3, 3, 1);
semilogx(freq/1000, 20*log10(H), 'b-', 'LineWidth', 2);
hold on;
plot([f_natural f_natural]/1000, [-40 20], 'r--', 'LineWidth', 1.5);
grid on;
xlabel('Frequency [kHz]', 'FontSize', 10);
ylabel('Magnitude [dB]', 'FontSize', 10);
title('Frequency Response (Air)', 'FontWeight', 'bold');
legend('H(\omega)', 'f_n', 'Location', 'southwest');

% Plot 2: Stiffness vs Width
subplot(3, 3, 2);
plot(w_range*1e6, k_vs_w, 'b-', 'LineWidth', 2);
hold on;
plot(design.w, k_total, 'ro', 'MarkerSize', 10, 'LineWidth', 2);
grid on;
xlabel('Beam Width [μm]', 'FontSize', 10);
ylabel('Stiffness [N/m]', 'FontSize', 10);
title('Stiffness vs Beam Width', 'FontWeight', 'bold');
legend('k(w)', 'Current design', 'Location', 'northwest');

% Plot 3: Frequency vs Width
subplot(3, 3, 3);
plot(w_range*1e6, f_vs_w/1000, 'b-', 'LineWidth', 2);
hold on;
plot(design.w, f_natural/1000, 'ro', 'MarkerSize', 10, 'LineWidth', 2);
grid on;
xlabel('Beam Width [μm]', 'FontSize', 10);
ylabel('Natural Frequency [kHz]', 'FontSize', 10);
title('Frequency vs Beam Width', 'FontWeight', 'bold');

% Plot 4: Stiffness vs Length
subplot(3, 3, 4);
semilogy(L_range*1e6, k_vs_L, 'b-', 'LineWidth', 2);
hold on;
plot(design.L, k_total, 'ro', 'MarkerSize', 10, 'LineWidth', 2);
grid on;
xlabel('Beam Length [μm]', 'FontSize', 10);
ylabel('Stiffness [N/m]', 'FontSize', 10);
title('Stiffness vs Beam Length (log)', 'FontWeight', 'bold');

% Plot 5: Stress vs Width
subplot(3, 3, 5);
plot(w_range*1e6, sigma_vs_w/1e6, 'b-', 'LineWidth', 2);
hold on;
plot(design.w, sigma_max/1e6, 'ro', 'MarkerSize', 10, 'LineWidth', 2);
yline(mat.sigma_yield/1e6, 'r--', 'Yield', 'LineWidth', 1.5);
grid on;
xlabel('Beam Width [μm]', 'FontSize', 10);
ylabel('Max Stress [MPa]', 'FontSize', 10);
title('Stress vs Beam Width', 'FontWeight', 'bold');

% Plot 6: Thermal Displacement
subplot(3, 3, 6);
plot(T_range, delta_thermal, 'b-', 'LineWidth', 2);
grid on;
xlabel('Temperature Change [°C]', 'FontSize', 10);
ylabel('Thermal Displacement [μm]', 'FontSize', 10);
title('Thermal Expansion', 'FontWeight', 'bold');

% Plot 7: Design Space Map (k vs f)
subplot(3, 3, 7);
scatter(k_vs_w, f_vs_w/1000, 50, w_range*1e6, 'filled');
hold on;
plot(k_total, f_natural/1000, 'rx', 'MarkerSize', 15, 'LineWidth', 3);
colormap(jet);
cb = colorbar;
cb.Label.String = 'Width [μm]';
grid on;
xlabel('Stiffness [N/m]', 'FontSize', 10);
ylabel('Frequency [kHz]', 'FontSize', 10);
title('Design Space Map', 'FontWeight', 'bold');

% Plot 8: Fatigue Life
subplot(3, 3, 8);
semilogy(delta_osc*1e6, N_cycles, 'bo-', 'MarkerSize', 8, 'LineWidth', 2);
grid on;
xlabel('Oscillation Amplitude [μm]', 'FontSize', 10);
ylabel('Cycles to Failure', 'FontSize', 10);
title('Fatigue Life Prediction', 'FontWeight', 'bold');

% Plot 9: Performance Summary
subplot(3, 3, 9);
axis off;
text(0.1, 0.9, ['\bf' geometry ' Spring Summary:'], 'FontSize', 11);
text(0.1, 0.75, sprintf('k = %.2f N/m', k_total), 'FontSize', 9);
text(0.1, 0.65, sprintf('f_n = %.2f kHz', f_natural/1000), 'FontSize', 9);
text(0.1, 0.55, sprintf('Q = %d (air)', Q_air), 'FontSize', 9);
text(0.1, 0.45, sprintf('σ_{max} = %.1f MPa', sigma_max/1e6), 'FontSize', 9);
text(0.1, 0.35, sprintf('SF = %.1f', mat.sigma_yield/sigma_max), 'FontSize', 9);
text(0.1, 0.25, sprintf('BW = %.1f Hz', BW_air), 'FontSize', 9);
text(0.1, 0.15, sprintf('L×w×t = %d×%d×%d μm', ...
    design.L, design.w, design.t), 'FontSize', 9);
text(0.1, 0.05, sprintf('N_{beams} = %d', design.N_beams), 'FontSize', 9);

sgtitle('MEMS Spring Comprehensive Analysis', 'FontSize', 14, 'FontWeight', 'bold');

%% ============================================================
%  SECTION 9: DESIGN RECOMMENDATIONS
%% ============================================================

fprintf('\n=== Design Recommendations ===\n');

% Check critical parameters
if f_natural < 1000
    fprintf('⚠ Low frequency (< 1 kHz): Consider shorter beams\n');
elseif f_natural > 100000
    fprintf('⚠ High frequency (> 100 kHz): Consider longer beams\n');
else
    fprintf('✓ Frequency in good range (1-100 kHz)\n');
end

if sigma_max/mat.sigma_yield > 0.5
    fprintf('⚠ High stress ratio: Reduce displacement or increase width\n');
else
    fprintf('✓ Safe stress levels (SF > 2)\n');
end

if delta_shock > 50
    fprintf('⚠ Large shock displacement: Increase stiffness\n');
else
    fprintf('✓ Shock-resistant design\n');
end

fprintf('\nOptimal design regions:\n');
fprintf('  Width: %.1f - %.1f μm\n', w_range(10)*1e6, w_range(30)*1e6);
fprintf('  Length: %.1f - %.1f μm\n', L_range(15)*1e6, L_range(35)*1e6);
fprintf('================================\n\n');

%% ============================================================
%  SECTION 10: EXPORT DATA
%% ============================================================

% Create results structure
results.geometry = geometry;
results.k_total = k_total;
results.f_natural = f_natural;
results.Q_air = Q_air;
results.sigma_max = sigma_max;
results.safety_factor = mat.sigma_yield/sigma_max;
results.shock_displacement = delta_shock;
results.design = design;

fprintf('Analysis complete! All results stored in ''results'' structure.\n');
fprintf('Figures generated for comprehensive visualization.\n\n');