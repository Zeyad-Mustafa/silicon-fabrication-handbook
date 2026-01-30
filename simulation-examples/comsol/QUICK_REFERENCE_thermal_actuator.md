% COMSOL Multiphysics: Thermal Actuator Model
% ============================================
% 
% This script creates a complete thermal actuator model in COMSOL Multiphysics.
% The model couples electrical heating, heat transfer, thermal expansion, and
% mechanical deformation to simulate a V-beam thermal actuator commonly used in MEMS.
%
% DEVICE: V-Beam Thermal Actuator (Chevron/Bent-Beam design)
% PHYSICS: Joule Heating + Heat Transfer + Thermal Expansion + Structural Mechanics
% GEOMETRY: Two angled beams forming a V-shape, anchored at both ends
% APPLICATION: Micro-positioning, optical switches, RF switches, microgrippers
%
% File: thermal_actuator_build_script.m
% Author: Silicon Fabrication Handbook
% License: MIT
% Date: January 2026
% COMSOL Version: 6.0 or higher
%
% HOW TO USE:
% 1. Open COMSOL Multiphysics
% 2. File -> New -> Blank Model
% 3. Copy and paste this script into the COMSOL Script window (Developer -> Script)
% 4. Run the script (F5)
% 5. The model will be built automatically
% 6. Save as thermal_actuator.mph
%
% ALTERNATIVELY: Use COMSOL with MATLAB interface and run this as MATLAB script

%% ========================================================================
%  PART 1: MODEL INITIALIZATION
%% ========================================================================

fprintf('\n========================================\n');
fprintf('COMSOL Thermal Actuator Model Builder\n');
fprintf('========================================\n\n');

% Create new model
import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('ThermalActuator');
model.label('V-Beam Thermal Actuator');
model.comments(['Multiphysics MEMS thermal actuator model\n' ...
                'Couples Joule heating, heat transfer, thermal expansion, and mechanics\n' ...
                'Created by Silicon Fabrication Handbook']);

fprintf('✓ Model created: V-Beam Thermal Actuator\n');

%% ========================================================================
%  PART 2: PARAMETERS AND CONSTANTS
%% ========================================================================

fprintf('\n--- Setting Parameters ---\n');

% Create parameter group
model.param.group.create('par1');
model.param('par1').label('Geometric Parameters');

% Geometric parameters (all in micrometers)
model.param('par1').set('L_beam', '200[um]', 'Beam length');
model.param('par1').set('w_beam', '4[um]', 'Beam width');
model.param('par1').set('t_beam', '2[um]', 'Beam thickness');
model.param('par1').set('theta', '2[deg]', 'V-beam angle (half angle)');
model.param('par1').set('gap', '2[um]', 'Gap between beams');
model.param('par1').set('L_shuttle', '50[um]', 'Shuttle length');
model.param('par1').set('w_shuttle', '20[um]', 'Shuttle width');

% Electrical parameters
model.param.group.create('par2');
model.param('par2').label('Electrical Parameters');
model.param('par2').set('V_applied', '3[V]', 'Applied voltage');
model.param('par2').set('rho_Si', '2e-5[ohm*m]', 'Silicon resistivity (doped poly-Si)');

% Material parameters (Polysilicon)
model.param.group.create('par3');
model.param('par3').label('Material Properties');
model.param('par3').set('E_Si', '169[GPa]', 'Young\'s modulus');
model.param('par3').set('nu_Si', '0.22', 'Poisson ratio');
model.param('par3').set('rho_mass', '2329[kg/m^3]', 'Density');
model.param('par3').set('alpha_Si', '2.6e-6[1/K]', 'Coefficient of thermal expansion');
model.param('par3').set('k_Si', '34[W/(m*K)]', 'Thermal conductivity (poly-Si)');
model.param('par3').set('C_p', '712[J/(kg*K)]', 'Specific heat capacity');

% Operating conditions
model.param.group.create('par4');
model.param('par4').label('Operating Conditions');
model.param('par4').set('T_amb', '293.15[K]', 'Ambient temperature (20°C)');
model.param('par4').set('h_conv', '10[W/(m^2*K)]', 'Convection coefficient');

% Derived parameters
model.param.group.create('par5');
model.param('par5').label('Derived Parameters');
model.param('par5').set('A_beam', 'w_beam*t_beam', 'Beam cross-sectional area');
model.param('par5').set('I_beam', 'w_beam*t_beam^3/12', 'Moment of inertia');
model.param('par5').set('L_horiz', 'L_beam*cos(theta)', 'Horizontal beam projection');
model.param('par5').set('L_vert', 'L_beam*sin(theta)', 'Vertical beam offset');

fprintf('✓ Parameters defined\n');

%% ========================================================================
%  PART 3: GEOMETRY CREATION
%% ========================================================================

fprintf('\n--- Building Geometry ---\n');

% Create geometry
model.component.create('comp1', true);
model.component('comp1').geom.create('geom1', 3);
model.component('comp1').geom('geom1').lengthUnit('um');
model.component('comp1').geom('geom1').label('3D Geometry');

% Work plane for 2D sketch
model.component('comp1').geom('geom1').create('wp1', 'WorkPlane');
model.component('comp1').geom('geom1').feature('wp1').set('quickplane', 'xy');
model.component('comp1').geom('geom1').feature('wp1').label('XY Plane');

% Create left V-beam
model.component('comp1').geom('geom1').feature('wp1').geom.create('r1', 'Rectangle');
model.component('comp1').geom('geom1').feature('wp1').geom.feature('r1').label('Left Beam Base');
model.component('comp1').geom('geom1').feature('wp1').geom.feature('r1').set('size', {'L_beam' 'w_beam'});
model.component('comp1').geom('geom1').feature('wp1').geom.feature('r1').set('pos', {0 'L_vert'});

% Rotate left beam
model.component('comp1').geom('geom1').feature('wp1').geom.create('rot1', 'Rotate');
model.component('comp1').geom('geom1').feature('wp1').geom.feature('rot1').set('rot', '-theta');
model.component('comp1').geom('geom1').feature('wp1').geom.feature('rot1').selection('input').set({'r1'});

% Create right V-beam
model.component('comp1').geom('geom1').feature('wp1').geom.create('r2', 'Rectangle');
model.component('comp1').geom('geom1').feature('wp1').geom.feature('r2').label('Right Beam Base');
model.component('comp1').geom('geom1').feature('wp1').geom.feature('r2').set('size', {'L_beam' 'w_beam'});
model.component('comp1').geom('geom1').feature('wp1').geom.feature('r2').set('pos', {0 '-L_vert-w_beam'});

% Rotate right beam
model.component('comp1').geom('geom1').feature('wp1').geom.create('rot2', 'Rotate');
model.component('comp1').geom('geom1').feature('wp1').geom.feature('rot2').set('rot', 'theta');
model.component('comp1').geom('geom1').feature('wp1').geom.feature('rot2').selection('input').set({'r2'});

% Create shuttle (central moving part)
model.component('comp1').geom('geom1').feature('wp1').geom.create('r3', 'Rectangle');
model.component('comp1').geom('geom1').feature('wp1').geom.feature('r3').label('Shuttle');
model.component('comp1').geom('geom1').feature('wp1').geom.feature('r3').set('size', {'L_shuttle' 'w_shuttle'});
model.component('comp1').geom('geom1').feature('wp1').geom.feature('r3').set('pos', {'L_horiz' '-w_shuttle/2'});

% Union all 2D features
model.component('comp1').geom('geom1').feature('wp1').geom.create('uni1', 'Union');
model.component('comp1').geom('geom1').feature('wp1').geom.feature('uni1').set('intbnd', false);
model.component('comp1').geom('geom1').feature('wp1').geom.feature('uni1').selection('input').set({'rot1' 'rot2' 'r3'});

% Extrude to 3D
model.component('comp1').geom('geom1').create('ext1', 'Extrude');
model.component('comp1').geom('geom1').feature('ext1').label('Extrude to 3D');
model.component('comp1').geom('geom1').feature('ext1').setIndex('distance', 't_beam', 0);
model.component('comp1').geom('geom1').feature('ext1').selection('input').set({'wp1'});

% Build geometry
model.component('comp1').geom('geom1').run;

fprintf('✓ Geometry created: V-beam with shuttle\n');

%% ========================================================================
%  PART 4: MATERIAL DEFINITION
%% ========================================================================

fprintf('\n--- Defining Materials ---\n');

% Create material (Polysilicon)
model.component('comp1').material.create('mat1', 'Common');
model.component('comp1').material('mat1').label('Doped Polysilicon');
model.component('comp1').material('mat1').propertyGroup.create('Enu', 'Young\'s modulus and Poisson\'s ratio');
model.component('comp1').material('mat1').propertyGroup.create('Murnaghan', 'Murnaghan');
model.component('comp1').material('mat1').propertyGroup.create('Lame', 'Lamé parameters');

% Set material properties
model.component('comp1').material('mat1').propertyGroup('def').set('density', 'rho_mass');
model.component('comp1').material('mat1').propertyGroup('def').set('heatcapacity', 'C_p');
model.component('comp1').material('mat1').propertyGroup('def').set('thermalconductivity', {'k_Si' '0' '0' '0' 'k_Si' '0' '0' '0' 'k_Si'});
model.component('comp1').material('mat1').propertyGroup('def').set('electricconductivity', {'1/rho_Si' '0' '0' '0' '1/rho_Si' '0' '0' '0' '1/rho_Si'});
model.component('comp1').material('mat1').propertyGroup('def').set('thermalexpansioncoefficient', {'alpha_Si' '0' '0' '0' 'alpha_Si' '0' '0' '0' 'alpha_Si'});
model.component('comp1').material('mat1').propertyGroup('Enu').set('E', 'E_Si');
model.component('comp1').material('mat1').propertyGroup('Enu').set('nu', 'nu_Si');

% Apply material to geometry
model.component('comp1').material('mat1').selection.all;

fprintf('✓ Material defined: Doped Polysilicon\n');

%% ========================================================================
%  PART 5: PHYSICS - ELECTRIC CURRENTS (Joule Heating)
%% ========================================================================

fprintf('\n--- Setting up Physics ---\n');

% Create Electric Currents physics
model.component('comp1').physics.create('ec', 'ConductiveMedia', 'geom1');
model.component('comp1').physics('ec').label('Electric Currents (Joule Heating)');
model.component('comp1').physics('ec').prop('ShapeProperty').set('order_electricpotential', 2);

% Ground (left anchor)
model.component('comp1').physics('ec').create('gnd1', 'Ground', 2);
model.component('comp1').physics('ec').feature('gnd1').label('Ground - Left Anchor');
model.component('comp1').physics('ec').feature('gnd1').selection.set([1]); % Boundary selection

% Electric potential (right anchor)
model.component('comp1').physics('ec').create('pot1', 'ElectricPotential', 2);
model.component('comp1').physics('ec').feature('pot1').label('Applied Voltage - Right Anchor');
model.component('comp1').physics('ec').feature('pot1').set('V0', 'V_applied');
model.component('comp1').physics('ec').feature('pot1').selection.set([2]); % Boundary selection

fprintf('  ✓ Electric Currents physics configured\n');

%% ========================================================================
%  PART 6: PHYSICS - HEAT TRANSFER
%% ========================================================================

% Create Heat Transfer physics
model.component('comp1').physics.create('ht', 'HeatTransfer', 'geom1');
model.component('comp1').physics('ht').label('Heat Transfer');
model.component('comp1').physics('ht').prop('ShapeProperty').set('order_temperature', 2);

% Heat source from Joule heating
model.component('comp1').physics('ht').create('hs1', 'HeatSource', 3);
model.component('comp1').physics('ht').feature('hs1').label('Joule Heating Source');
model.component('comp1').physics('ht').feature('hs1').set('Q0', 'ec.Qh'); % Coupling from Electric Currents
model.component('comp1').physics('ht').feature('hs1').selection.all;

% Temperature boundary condition (anchors)
model.component('comp1').physics('ht').create('temp1', 'Temperature', 2);
model.component('comp1').physics('ht').feature('temp1').label('Fixed Temperature - Anchors');
model.component('comp1').physics('ht').feature('temp1').set('T0', 'T_amb');
model.component('comp1').physics('ht').feature('temp1').selection.set([1 2]); % Both anchor boundaries

% Convective cooling (all external surfaces)
model.component('comp1').physics('ht').create('hf1', 'HeatFluxBoundary', 2);
model.component('comp1').physics('ht').feature('hf1').label('Convective Cooling');
model.component('comp1').physics('ht').feature('hf1').set('HeatFluxType', 'ConvectiveHeatFlux');
model.component('comp1').physics('ht').feature('hf1').set('h', 'h_conv');
model.component('comp1').physics('ht').feature('hf1').set('Text', 'T_amb');
model.component('comp1').physics('ht').feature('hf1').selection.all;

fprintf('  ✓ Heat Transfer physics configured\n');

%% ========================================================================
%  PART 7: PHYSICS - SOLID MECHANICS
%% ========================================================================

% Create Solid Mechanics physics
model.component('comp1').physics.create('solid', 'SolidMechanics', 'geom1');
model.component('comp1').physics('solid').label('Solid Mechanics (Thermal Expansion)');
model.component('comp1').physics('solid').prop('ShapeProperty').set('order_displacement', 2);

% Fixed constraints (anchors)
model.component('comp1').physics('solid').create('fix1', 'Fixed', 2);
model.component('comp1').physics('solid').feature('fix1').label('Fixed - Left Anchor');
model.component('comp1').physics('solid').feature('fix1').selection.set([1]);

model.component('comp1').physics('solid').create('fix2', 'Fixed', 2);
model.component('comp1').physics('solid').feature('fix2').label('Fixed - Right Anchor');
model.component('comp1').physics('solid').feature('fix2').selection.set([2]);

% Thermal expansion (volume force)
model.component('comp1').physics('solid').feature('lemm1').label('Thermal Expansion');
model.component('comp1').physics('solid').feature('lemm1').set('Ts', 'T_amb'); % Reference temperature
model.component('comp1').physics('solid').feature('lemm1').set('dL', 'alpha_Si*(ht.T-T_amb)'); % Thermal strain coupling

fprintf('  ✓ Solid Mechanics physics configured\n');

%% ========================================================================
%  PART 8: MULTIPHYSICS COUPLINGS
%% ========================================================================

fprintf('\n--- Setting up Multiphysics Couplings ---\n');

% Create multiphysics node
model.component('comp1').multiphysics.create('te1', 'ThermalExpansion', -1);
model.component('comp1').multiphysics('te1').label('Thermal Expansion Coupling');
model.component('comp1').multiphysics('te1').selection.all;

fprintf('✓ Multiphysics coupling established\n');

%% ========================================================================
%  PART 9: MESH
%% ========================================================================

fprintf('\n--- Creating Mesh ---\n');

% Create mesh
model.component('comp1').mesh.create('mesh1');
model.component('comp1').mesh('mesh1').label('Thermal Actuator Mesh');

% Free tetrahedral mesh
model.component('comp1').mesh('mesh1').create('ftet1', 'FreeTet');
model.component('comp1').mesh('mesh1').feature('ftet1').label('Free Tetrahedral');
model.component('comp1').mesh('mesh1').feature('ftet1').create('size1', 'Size');

% Mesh sizing
model.component('comp1').mesh('mesh1').feature('ftet1').feature('size1').set('custom', 'on');
model.component('comp1').mesh('mesh1').feature('ftet1').feature('size1').set('hmax', '5[um]'); % Max element size
model.component('comp1').mesh('mesh1').feature('ftet1').feature('size1').set('hmin', '0.5[um]'); % Min element size
model.component('comp1').mesh('mesh1').feature('ftet1').feature('size1').set('hgrad', 1.3); % Growth rate

% Build mesh
model.component('comp1').mesh('mesh1').run;

fprintf('✓ Mesh created\n');

%% ========================================================================
%  PART 10: STUDY (Stationary Analysis)
%% ========================================================================

fprintf('\n--- Configuring Study ---\n');

% Create stationary study
model.study.create('std1');
model.study('std1').label('Stationary Thermal-Electric-Mechanical Analysis');
model.study('std1').create('stat', 'Stationary');
model.study('std1').feature('stat').label('Stationary Study');

% Set physics selection
model.study('std1').feature('stat').set('physselection', 'all');

% Solver configuration
model.sol.create('sol1');
model.sol('sol1').study('std1');
model.sol('sol1').attach('std1');
model.sol('sol1').create('st1', 'StudyStep');
model.sol('sol1').create('v1', 'Variables');
model.sol('sol1').create('s1', 'Stationary');

% Fully coupled solver
model.sol('sol1').feature('s1').create('fc1', 'FullyCoupled');
model.sol('sol1').feature('s1').create('i1', 'Iterative');
model.sol('sol1').feature('s1').feature('fc1').set('linsolver', 'i1');
model.sol('sol1').feature('s1').feature('i1').set('itrestart', 300);
model.sol('sol1').feature('s1').feature('i1').label('Suggested Iterative Solver (Electric Currents)');

fprintf('✓ Study configured\n');

%% ========================================================================
%  PART 11: RESULTS AND VISUALIZATION
%% ========================================================================

fprintf('\n--- Setting up Results ---\n');

% Create result datasets
model.result.dataset.create('dset1', 'Solution');
model.result.dataset('dset1').label('Solution Dataset');

% Temperature distribution plot
model.result.create('pg1', 'PlotGroup3D');
model.result('pg1').label('Temperature Distribution');
model.result('pg1').set('data', 'dset1');
model.result('pg1').create('surf1', 'Surface');
model.result('pg1').feature('surf1').set('expr', 'ht.T-T_amb');
model.result('pg1').feature('surf1').set('unit', 'K');
model.result('pg1').feature('surf1').set('descr', 'Temperature rise');
model.result('pg1').feature('surf1').create('def', 'Deform');
model.result('pg1').feature('surf1').feature('def').set('expr', {'u' 'v' 'w'});
model.result('pg1').feature('surf1').feature('def').set('scale', 1e6);
model.result('pg1').feature('surf1').feature('def').set('scaleactive', true);

% Displacement plot
model.result.create('pg2', 'PlotGroup3D');
model.result('pg2').label('Displacement Magnitude');
model.result('pg2').set('data', 'dset1');
model.result('pg2').create('surf2', 'Surface');
model.result('pg2').feature('surf2').set('expr', 'sqrt(u^2+v^2+w^2)');
model.result('pg2').feature('surf2').set('unit', 'um');
model.result('pg2').feature('surf2').set('descr', 'Displacement');
model.result('pg2').feature('surf2').create('def', 'Deform');
model.result('pg2').feature('surf2').feature('def').set('expr', {'u' 'v' 'w'});
model.result('pg2').feature('surf2').feature('def').set('scale', 1e6);
model.result('pg2').feature('surf2').feature('def').set('scaleactive', true);

% Von Mises stress plot
model.result.create('pg3', 'PlotGroup3D');
model.result('pg3').label('Von Mises Stress');
model.result('pg3').set('data', 'dset1');
model.result('pg3').create('surf3', 'Surface');
model.result('pg3').feature('surf3').set('expr', 'solid.mises');
model.result('pg3').feature('surf3').set('unit', 'MPa');
model.result('pg3').feature('surf3').set('descr', 'von Mises stress');

% Current density plot
model.result.create('pg4', 'PlotGroup3D');
model.result('pg4').label('Current Density');
model.result('pg4').set('data', 'dset1');
model.result('pg4').create('arws1', 'ArrowVolume');
model.result('pg4').feature('arws1').set('expr', {'ec.Jx' 'ec.Jy' 'ec.Jz'});
model.result('pg4').feature('arws1').set('descr', 'Current density');

fprintf('✓ Results visualization configured\n');

%% ========================================================================
%  PART 12: PARAMETRIC SWEEP (Optional - Voltage Sweep)
%% ========================================================================

fprintf('\n--- Setting up Parametric Sweep ---\n');

% Create parametric sweep study
model.study.create('std2');
model.study('std2').label('Voltage Sweep');
model.study('std2').create('param', 'Parametric');
model.study('std2').feature('param').set('pname', {'V_applied'});
model.study('std2').feature('param').set('plistarr', {'0 0.5 1 1.5 2 2.5 3 3.5 4'});
model.study('std2').feature('param').set('punit', {'V'});
model.study('std2').create('stat', 'Stationary');

fprintf('✓ Parametric sweep configured (0-4V)\n');

%% ========================================================================
%  PART 13: DERIVED VALUES
%% ========================================================================

fprintf('\n--- Setting up Derived Values ---\n');

% Create derived value for shuttle displacement
model.result.numerical.create('gev1', 'EvalGlobal');
model.result.numerical('gev1').label('Shuttle Displacement');
model.result.numerical('gev1').set('probetag', 'none');
model.result.numerical('gev1').set('expr', {'maxop1(u)'});
model.result.numerical('gev1').set('unit', {'um'});
model.result.numerical('gev1').set('descr', {'X-displacement at shuttle tip'});
model.result.numerical('gev1').set('table', 'tbl1');

% Create derived value for maximum temperature
model.result.numerical.create('gev2', 'EvalGlobal');
model.result.numerical('gev2').label('Maximum Temperature');
model.result.numerical('gev2').set('probetag', 'none');
model.result.numerical('gev2').set('expr', {'maxop1(ht.T-T_amb)'});
model.result.numerical('gev2').set('unit', {'K'});
model.result.numerical('gev2').set('descr', {'Maximum temperature rise'});
model.result.numerical('gev2').set('table', 'tbl1');

% Create derived value for total power
model.result.numerical.create('gev3', 'EvalGlobal');
model.result.numerical('gev3').label('Total Power Dissipation');
model.result.numerical('gev3').set('probetag', 'none');
model.result.numerical('gev3').set('expr', {'intop1(ec.Qh)'});
model.result.numerical('gev3').set('unit', {'mW'});
model.result.numerical('gev3').set('descr', {'Total Joule heating power'});
model.result.numerical('gev3').set('table', 'tbl1');

% Create derived value for maximum stress
model.result.numerical.create('gev4', 'EvalGlobal');
model.result.numerical('gev4').label('Maximum von Mises Stress');
model.result.numerical('gev4').set('probetag', 'none');
model.result.numerical('gev4').set('expr', {'maxop1(solid.mises)'});
model.result.numerical('gev4').set('unit', {'MPa'});
model.result.numerical('gev4').set('descr', {'Maximum stress'});
model.result.numerical('gev4').set('table', 'tbl1');

fprintf('✓ Derived values configured\n');

%% ========================================================================
%  PART 14: SAVE MODEL
%% ========================================================================

fprintf('\n--- Saving Model ---\n');

% Save the model
try
    mphsave(model, 'thermal_actuator.mph');
    fprintf('✓ Model saved: thermal_actuator.mph\n');
catch
    fprintf('! Note: Model created but not saved (requires COMSOL with MATLAB)\n');
    fprintf('  Save manually from COMSOL: File -> Save As -> thermal_actuator.mph\n');
end

%% ========================================================================
%  SUMMARY AND NEXT STEPS
%% ========================================================================

fprintf('\n========================================\n');
fprintf('MODEL BUILD COMPLETE!\n');
fprintf('========================================\n\n');

fprintf('Model Summary:\n');
fprintf('  Device: V-Beam Thermal Actuator\n');
fprintf('  Physics: Joule Heating + Heat Transfer + Thermal Expansion\n');
fprintf('  Beam Length: 200 μm\n');
fprintf('  Beam Width: 4 μm\n');
fprintf('  Beam Thickness: 2 μm\n');
fprintf('  V-angle: 2°\n');
fprintf('  Applied Voltage: 3 V\n');
fprintf('  Material: Doped Polysilicon\n\n');

fprintf('Configured Studies:\n');
fprintf('  1. Stationary Analysis (std1)\n');
fprintf('  2. Voltage Sweep 0-4V (std2)\n\n');

fprintf('Available Plots:\n');
fprintf('  1. Temperature Distribution (pg1)\n');
fprintf('  2. Displacement Magnitude (pg2)\n');
fprintf('  3. Von Mises Stress (pg3)\n');
fprintf('  4. Current Density (pg4)\n\n');

fprintf('Derived Values:\n');
fprintf('  - Shuttle displacement (μm)\n');
fprintf('  - Maximum temperature rise (K)\n');
fprintf('  - Total power dissipation (mW)\n');
fprintf('  - Maximum von Mises stress (MPa)\n\n');

fprintf('Next Steps:\n');
fprintf('  1. Run Study 1: Click Compute button or F5\n');
fprintf('  2. View results in plots pg1-pg4\n');
fprintf('  3. Check derived values table\n');
fprintf('  4. Run Study 2 for parametric sweep\n');
fprintf('  5. Export data: Results -> Export -> Data\n\n');

fprintf('Expected Results (at 3V):\n');
fprintf('  - Displacement: ~2-5 μm\n');
fprintf('  - Temperature rise: ~100-300 K\n');
fprintf('  - Power: ~10-50 mW\n');
fprintf('  - Max stress: <500 MPa (yield ~7 GPa)\n\n');

fprintf('Troubleshooting:\n');
fprintf('  - If convergence fails: Reduce voltage or refine mesh\n');
fprintf('  - For better accuracy: Decrease max mesh size to 2 μm\n');
fprintf('  - For faster solving: Use coarser mesh (10 μm)\n\n');

fprintf('========================================\n');
fprintf('Happy Simulating!\n');
fprintf('========================================\n\n');

% End of script