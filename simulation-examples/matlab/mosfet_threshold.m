%% MOSFET Threshold Voltage Analysis
% ===================================
%
% Calculates and analyzes MOSFET threshold voltage (V_th) including:
% - Body effect (substrate bias)
% - Temperature dependence
% - Channel length modulation
% - Short channel effects
%
% Author: Silicon Fabrication Handbook
% License: MIT
% Date: January 2026

clear; close all; clc;

fprintf('==============================================================\n');
fprintf('MOSFET Threshold Voltage Analysis\n');
fprintf('==============================================================\n\n');

%% Physical Constants
q = 1.602e-19;          % Elementary charge [C]
k = 1.381e-23;          % Boltzmann constant [J/K]
epsilon_0 = 8.854e-12;  % Permittivity of free space [F/m]
epsilon_si = 11.7;      % Relative permittivity of Si
epsilon_ox = 3.9;       % Relative permittivity of SiO2

%% Device Parameters (nMOS transistor)
% Technology node
tech_node = 180;        % Technology node [nm]
L = tech_node * 1e-9;   % Channel length [m]
W = 10 * L;             % Channel width [m]

% Oxide parameters
t_ox = 4e-9;            % Gate oxide thickness [m] (4 nm)
C_ox = epsilon_0 * epsilon_ox / t_ox;  % Oxide capacitance per unit area [F/m²]

% Substrate doping
N_A = 5e17;             % Acceptor concentration [cm⁻³] for nMOS
N_A_si = N_A * 1e6;     % Convert to [m⁻³]

% Material parameters
n_i = 1.45e10;          % Intrinsic carrier concentration [cm⁻³] at 300K
T = 300;                % Temperature [K]
V_T = k*T/q;            % Thermal voltage [V]

% Work function difference
phi_ms = -0.95;         % Work function difference (n+ poly on p-substrate) [V]

% Oxide charge
Q_ox = 1e10 * q;        % Fixed oxide charge density [C/cm²]

fprintf('Device Parameters:\n');
fprintf('  Technology: %d nm\n', tech_node);
fprintf('  Channel L × W: %.0f × %.0f nm\n', L*1e9, W*1e9);
fprintf('  Oxide thickness: %.1f nm\n', t_ox*1e9);
fprintf('  Substrate doping: %.1e cm⁻³\n', N_A);
fprintf('  Temperature: %.0f K (%.0f°C)\n\n', T, T-273);

%% Threshold Voltage Calculation (Long Channel)

% Fermi potential
phi_F = V_T * log(N_A/n_i);  % [V]

% Body effect coefficient (gamma)
gamma = sqrt(2*q*epsilon_0*epsilon_si*N_A_si) / C_ox;  % [V^0.5]

% Zero-bias threshold voltage
V_th0 = phi_ms + 2*phi_F + gamma*sqrt(2*phi_F) - Q_ox/C_ox;

% Substrate bias (body effect)
V_SB_range = 0:0.1:3;  % Substrate bias [V]
V_th_body = zeros(size(V_SB_range));

for i = 1:length(V_SB_range)
    V_SB = V_SB_range(i);
    V_th_body(i) = V_th0 + gamma*(sqrt(2*phi_F + V_SB) - sqrt(2*phi_F));
end

fprintf('Threshold Voltage Components:\n');
fprintf('  Work function difference φ_ms: %.3f V\n', phi_ms);
fprintf('  Fermi potential φ_F: %.3f V\n', phi_F);
fprintf('  Body effect coefficient γ: %.3f V^0.5\n', gamma);
fprintf('  Fixed oxide charge term: %.3f V\n', -Q_ox/C_ox);
fprintf('  V_th0 (V_SB=0): %.3f V\n\n', V_th0);

%% Temperature Dependence

T_range = 233:10:423;  % Temperature range: -40°C to 150°C
V_th_temp = zeros(size(T_range));

for i = 1:length(T_range)
    T_i = T_range(i);
    V_T_i = k*T_i/q;
    
    % Intrinsic carrier concentration temperature dependence
    n_i_T = 1.45e10 * (T_i/300)^1.5 * exp(-q*1.12/(2*k) * (1/T_i - 1/300));
    
    % Fermi potential at temperature T
    phi_F_T = V_T_i * log(N_A/n_i_T);
    
    % Threshold voltage (simplified - ignores other temp effects)
    V_th_temp(i) = phi_ms + 2*phi_F_T + gamma*sqrt(2*phi_F_T) - Q_ox/C_ox;
end

% Temperature coefficient
dVth_dT = (V_th_temp(end) - V_th_temp(1))/(T_range(end) - T_range(1));

fprintf('Temperature Effects:\n');
fprintf('  Temperature coefficient: %.2f mV/°C\n', dVth_dT*1e3);
fprintf('  V_th at -40°C: %.3f V\n', V_th_temp(1));
fprintf('  V_th at 150°C: %.3f V\n\n', V_th_temp(end));

%% Channel Length Dependence (Short Channel Effects)

L_range = logspace(-8, -6, 50);  % 10 nm to 1 µm
V_th_SCE = zeros(size(L_range));

% Drain-induced barrier lowering (DIBL) coefficient
V_DS = 1.8;  % Drain voltage [V]
eta_DIBL = 0.1;  % DIBL coefficient [V/V]

for i = 1:length(L_range)
    L_i = L_range(i);
    
    % Short channel effect (empirical model)
    if L_i < 0.5e-6
        % Threshold voltage rolloff
        delta_Vth = -0.1 * (1 - L_i/0.5e-6);
        
        % DIBL effect
        delta_DIBL = -eta_DIBL * V_DS * (1 - L_i/0.5e-6);
    else
        delta_Vth = 0;
        delta_DIBL = 0;
    end
    
    V_th_SCE(i) = V_th0 + delta_Vth + delta_DIBL;
end

fprintf('Short Channel Effects:\n');
fprintf('  V_th at L=180nm: %.3f V\n', V_th_SCE(find(L_range>=180e-9, 1)));
fprintf('  V_th at L=50nm: %.3f V (rolloff: %.0f mV)\n', ...
    V_th_SCE(find(L_range>=50e-9, 1)), ...
    (V_th0 - V_th_SCE(find(L_range>=50e-9, 1)))*1e3);

%% Plotting

figure('Position', [100, 100, 1200, 800]);

% Plot 1: Body Effect
subplot(2, 3, 1);
plot(V_SB_range, V_th_body, 'b-', 'LineWidth', 2.5);
hold on;
plot([0, 0], [min(V_th_body), max(V_th_body)], 'r--', 'LineWidth', 1.5);
xlabel('Substrate Bias V_{SB} [V]', 'FontSize', 11);
ylabel('Threshold Voltage V_{th} [V]', 'FontSize', 11);
title('Body Effect', 'FontSize', 13, 'FontWeight', 'bold');
grid on;
legend('V_{th}(V_{SB})', 'V_{SB}=0', 'Location', 'northwest');
text(1.5, V_th0+0.1, sprintf('γ = %.3f V^{0.5}', gamma), 'FontSize', 10);

% Plot 2: Temperature Dependence
subplot(2, 3, 2);
plot(T_range-273, V_th_temp, 'r-', 'LineWidth', 2.5);
hold on;
plot([27, 27], [min(V_th_temp), max(V_th_temp)], 'k--', 'LineWidth', 1.5);
xlabel('Temperature [°C]', 'FontSize', 11);
ylabel('Threshold Voltage V_{th} [V]', 'FontSize', 11);
title('Temperature Dependence', 'FontSize', 13, 'FontWeight', 'bold');
grid on;
legend('V_{th}(T)', '27°C', 'Location', 'northeast');
text(50, max(V_th_temp)-0.05, sprintf('dV_{th}/dT = %.2f mV/°C', dVth_dT*1e3), ...
     'FontSize', 10);

% Plot 3: Channel Length Dependence
subplot(2, 3, 3);
semilogx(L_range*1e9, V_th_SCE, 'g-', 'LineWidth', 2.5);
hold on;
semilogx([tech_node, tech_node], [min(V_th_SCE), max(V_th_SCE)], 'k--', 'LineWidth', 1.5);
xlabel('Channel Length L [nm]', 'FontSize', 11);
ylabel('Threshold Voltage V_{th} [V]', 'FontSize', 11);
title('Short Channel Effects', 'FontSize', 13, 'FontWeight', 'bold');
grid on;
legend('V_{th}(L)', sprintf('%d nm node', tech_node), 'Location', 'southeast');

% Plot 4: I-V Characteristics
subplot(2, 3, 4);
V_GS_range = 0:0.01:2;
V_DS_val = 1.8;
mu_n = 400e-4;  % Electron mobility [m²/V·s]
I_D = zeros(size(V_GS_range));

for i = 1:length(V_GS_range)
    V_GS = V_GS_range(i);
    if V_GS > V_th0
        % Saturation region
        I_D(i) = 0.5 * mu_n * C_ox * (W/L) * (V_GS - V_th0)^2;
    end
end

semilogy(V_GS_range, I_D*1e6, 'b-', 'LineWidth', 2.5);
hold on;
semilogy([V_th0, V_th0], [1e-6, max(I_D)*1e6], 'r--', 'LineWidth', 1.5);
xlabel('Gate Voltage V_{GS} [V]', 'FontSize', 11);
ylabel('Drain Current I_D [µA]', 'FontSize', 11);
title(sprintf('I_D vs V_{GS} (V_{DS}=%.1fV)', V_DS_val), 'FontSize', 13, 'FontWeight', 'bold');
grid on;
legend('I_D', sprintf('V_{th}=%.2fV', V_th0), 'Location', 'northwest');
ylim([1e-3, max(I_D)*1e6*2]);

% Plot 5: Subthreshold Slope
subplot(2, 3, 5);
V_GS_sub = 0:0.01:V_th0+0.5;
I_D_sub = zeros(size(V_GS_sub));
n_sub = 1.5;  % Subthreshold slope factor

for i = 1:length(V_GS_sub)
    I_D_sub(i) = 1e-12 * exp((V_GS_sub(i) - V_th0)/(n_sub*V_T));  % [A]
end

semilogy(V_GS_sub, I_D_sub*1e9, 'b-', 'LineWidth', 2.5);
xlabel('Gate Voltage V_{GS} [V]', 'FontSize', 11);
ylabel('Drain Current I_D [nA]', 'FontSize', 11);
title('Subthreshold Characteristics', 'FontSize', 13, 'FontWeight', 'bold');
grid on;

% Subthreshold swing
S = n_sub * V_T * log(10);  % [V/decade]
text(0.3, 1e-2, sprintf('S = %.0f mV/dec', S*1e3), 'FontSize', 10);

% Plot 6: Threshold Voltage Components
subplot(2, 3, 6);
components = [phi_ms, 2*phi_F, gamma*sqrt(2*phi_F), -Q_ox/C_ox];
component_names = {'φ_{ms}', '2φ_F', 'γ√{2φ_F}', '-Q_{ox}/C_{ox}'};
colors_bar = [0.2 0.4 0.8; 0.8 0.4 0.2; 0.4 0.8 0.4; 0.8 0.2 0.4];

b = bar(components, 'FaceColor', 'flat');
b.CData = colors_bar;
set(gca, 'XTickLabel', component_names);
ylabel('Voltage [V]', 'FontSize', 11);
title('V_{th} Components', 'FontSize', 13, 'FontWeight', 'bold');
grid on;
hold on;
yline(V_th0, 'r--', 'LineWidth', 2, 'Label', sprintf('V_{th0}=%.3fV', V_th0));

sgtitle('MOSFET Threshold Voltage Analysis', 'FontSize', 15, 'FontWeight', 'bold');

%% Save Figure
if ~exist('images', 'dir')
    mkdir('images');
end
saveas(gcf, 'images/mosfet_threshold.png');
fprintf('\n✓ Saved: images/mosfet_threshold.png\n\n');

%% Summary Table

fprintf('==============================================================\n');
fprintf('Summary: Threshold Voltage Characteristics\n');
fprintf('==============================================================\n\n');

fprintf('Nominal Threshold Voltage:\n');
fprintf('  V_th0 = %.3f V\n\n', V_th0);

fprintf('Body Effect:\n');
fprintf('  γ = %.3f V^{0.5}\n', gamma);
fprintf('  V_th at V_SB=2V: %.3f V (increase: %.0f mV)\n', ...
    V_th_body(find(V_SB_range>=2, 1)), ...
    (V_th_body(find(V_SB_range>=2, 1)) - V_th0)*1e3);

fprintf('\nTemperature Sensitivity:\n');
fprintf('  dV_th/dT = %.2f mV/°C\n', dVth_dT*1e3);
fprintf('  ΔV_th (-40°C to 150°C) = %.0f mV\n', ...
    (V_th_temp(end) - V_th_temp(1))*1e3);

fprintf('\nShort Channel Effects:\n');
fprintf('  V_th rolloff at L=50nm: %.0f mV\n', ...
    (V_th0 - V_th_SCE(find(L_range>=50e-9, 1)))*1e3);
fprintf('  DIBL coefficient: %.2f V/V\n', eta_DIBL);

fprintf('\nDevice Performance:\n');
fprintf('  C_ox = %.2f fF/µm²\n', C_ox*1e9);
fprintf('  Subthreshold swing S = %.0f mV/decade\n', S*1e3);
fprintf('  I_on/I_off ratio: ~10^6\n');

fprintf('\n==============================================================\n');
fprintf('Analysis complete!\n');
fprintf('==============================================================\n');

%% Design Guidelines

fprintf('\nDesign Guidelines:\n');
fprintf('──────────────────────────────────────────────────────────────\n');
fprintf('To increase V_th:\n');
fprintf('  • Increase substrate doping N_A\n');
fprintf('  • Use thicker gate oxide t_ox\n');
fprintf('  • Apply substrate bias V_SB\n');
fprintf('  • Choose appropriate gate material (higher work function)\n\n');

fprintf('To decrease V_th:\n');
fprintf('  • Decrease substrate doping N_A\n');
fprintf('  • Use thinner gate oxide t_ox\n');
fprintf('  • Choose appropriate gate material (lower work function)\n');
fprintf('  • Minimize fixed oxide charge Q_ox\n\n');

fprintf('Short Channel Effects Mitigation:\n');
fprintf('  • Use retrograde doping profiles\n');
fprintf('  • Implement halo/pocket implants\n');
fprintf('  • Reduce oxide thickness (scaled)\n');
fprintf('  • Use high-k dielectrics for modern nodes\n\n');

fprintf('Typical Values:\n');
fprintf('  Low-V_th (LVT): 0.2-0.3 V (high performance)\n');
fprintf('  Regular-V_th (RVT): 0.4-0.5 V (balanced)\n');
fprintf('  High-V_th (HVT): 0.6-0.8 V (low leakage)\n');
fprintf('──────────────────────────────────────────────────────────────\n');