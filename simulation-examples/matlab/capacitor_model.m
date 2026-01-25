%% MOS Capacitor C-V Characteristics Simulation
% Demonstrates accumulation, depletion, and inversion regions
% Perfect for understanding CMOS capacitance behavior

%% Physical Constants
q = 1.602e-19;          % Elementary charge [C]
eps0 = 8.854e-14;       % Vacuum permittivity [F/cm]
k = 1.381e-23;          % Boltzmann constant [J/K]
T = 300;                % Temperature [K]
kT = k * T / q;         % Thermal voltage [V]

%% Material Parameters
% Silicon substrate (p-type)
Na = 1e16;              % Acceptor concentration [cm^-3]
eps_si = 11.7;          % Si relative permittivity
ni = 1.45e10;           % Intrinsic carrier concentration [cm^-3]

% Gate oxide (SiO2)
tox = 10e-7;            % Oxide thickness [cm] (10 nm)
eps_ox = 3.9;           % SiO2 relative permittivity

% Metal gate
phi_m = 4.1;            % Work function [eV]
chi_si = 4.05;          % Si electron affinity [eV]
Eg = 1.12;              % Si bandgap [eV]

%% Derived Parameters
Cox = eps0 * eps_ox / tox;              % Oxide capacitance [F/cm^2]
phi_f = kT * log(Na / ni);              % Fermi potential [V]
Ld = sqrt(eps0 * eps_si * kT / (q * Na)); % Debye length [cm]

% Flat-band voltage
phi_si = chi_si + Eg/2 + phi_f;         % Si work function
Vfb = phi_m - phi_si;                   % Flat-band voltage [V]

%% Voltage Sweep
Vg = linspace(-2, 2, 500);              % Gate voltage [V]
C = zeros(size(Vg));                    % Total capacitance

%% Calculate C-V Characteristics
for i = 1:length(Vg)
    Vs = Vg(i) - Vfb;  % Surface potential shift
    
    if Vs < -3*kT
        % Accumulation: holes accumulate at surface
        Cd = Cox * 100;  % Effectively infinite
    elseif Vs < 2*phi_f
        % Depletion: depletion region grows
        W = sqrt(2 * eps0 * eps_si * abs(Vs) / (q * Na));
        Cd = eps0 * eps_si / W;
    else
        % Inversion: electron layer forms
        W = sqrt(2 * eps0 * eps_si * 2*phi_f / (q * Na));
        Cd = eps0 * eps_si / W;
    end
    
    % Series combination: 1/C_total = 1/C_ox + 1/C_d
    C(i) = (Cox * Cd) / (Cox + Cd);
end

% Normalize to Cox
C_norm = C / Cox;

%% Plotting
figure('Position', [100, 100, 800, 600]);

% C-V curve
subplot(2,1,1);
plot(Vg, C_norm, 'b-', 'LineWidth', 2);
hold on;
plot([Vfb Vfb], [0 1], 'r--', 'LineWidth', 1.5);
plot([2*phi_f 2*phi_f], [0 1], 'g--', 'LineWidth', 1.5);
grid on;
xlabel('Gate Voltage V_G [V]', 'FontSize', 12);
ylabel('C/C_{ox}', 'FontSize', 12);
title('MOS Capacitor C-V Characteristics', 'FontSize', 14, 'FontWeight', 'bold');
legend('C-V Curve', 'V_{fb}', 'V_T (threshold)', 'Location', 'best');
ylim([0 1.1]);

% Add region labels
text(-1.2, 0.95, 'Accumulation', 'FontSize', 11, 'Color', 'blue');
text(0, 0.65, 'Depletion', 'FontSize', 11, 'Color', 'blue');
text(1, 0.4, 'Inversion', 'FontSize', 11, 'Color', 'blue');

% Capacitance components
subplot(2,1,2);
plot(Vg, C*1e6, 'b-', 'LineWidth', 2);
hold on;
plot(Vg, ones(size(Vg))*Cox*1e6, 'r--', 'LineWidth', 1.5);
grid on;
xlabel('Gate Voltage V_G [V]', 'FontSize', 12);
ylabel('Capacitance [μF/cm²]', 'FontSize', 12);
title('Absolute Capacitance vs Gate Voltage', 'FontSize', 14, 'FontWeight', 'bold');
legend('C_{total}', 'C_{ox}', 'Location', 'best');

%% Results Summary
fprintf('\n=== MOS Capacitor Simulation Results ===\n');
fprintf('Oxide thickness: %.1f nm\n', tox*1e7);
fprintf('Oxide capacitance: %.2f μF/cm²\n', Cox*1e6);
fprintf('Substrate doping: %.2e cm⁻³\n', Na);
fprintf('Fermi potential: %.3f V\n', phi_f);
fprintf('Flat-band voltage: %.3f V\n', Vfb);
fprintf('Threshold voltage: %.3f V\n', 2*phi_f);
fprintf('Debye length: %.2f nm\n', Ld*1e7);
fprintf('Max depletion width: %.2f nm\n', ...
    sqrt(2*eps0*eps_si*2*phi_f/(q*Na))*1e7);
fprintf('========================================\n\n');