%% COMSOL Membrane Deflection Model Builder
% =========================================
%
% This MATLAB script creates a complete membrane deflection simulation 
% model using COMSOL Multiphysics LiveLink for MATLAB.
%
% Requirements:
%   - COMSOL Multiphysics with valid license
%   - COMSOL LiveLink for MATLAB
%
% Usage:
%   Run this script in MATLAB with COMSOL LiveLink installed
%
% Author: Silicon Fabrication Handbook Project
% Date: January 2026

%% Initialize
clear all;
close all;
clc;

fprintf('===============================================\n');
fprintf('COMSOL Membrane Deflection Model Builder\n');
fprintf('===============================================\n\n');

%% Parameters
% Geometric parameters
r_mem = 500;           % Membrane radius [um]
t_mem = 2;             % Membrane thickness [um]
h_cavity = 10;         % Cavity depth [um]
w_support = 50;        % Support width [um]

% Material parameters
E_si = 170e9;          % Young's modulus [Pa]
nu_si = 0.28;          % Poisson's ratio
rho_si = 2329;         % Density [kg/m^3]

% Loading parameters
p_applied = 1e3;       % Applied pressure [Pa] (1 kPa)
sigma_residual = 50e6; % Residual stress [Pa] (50 MPa)

% Analysis parameters
dimension_type = '2D_axisym';  % '2D_axisym' or '3D'
study_type = 'stationary';      % 'stationary', 'parametric', or 'eigenfrequency'

%% Import COMSOL Model Object
import com.comsol.model.*
import com.comsol.model.util.*

%% Create Model
fprintf('Creating model...\n');
model = ModelUtil.create('MembraneDeflection');

%% Set Model Name and Description
model.name('membrane_deflection.mph');
model.label('Membrane Deflection Analysis');
model.comments(['MEMS membrane deflection simulation\n' ...
                'Created: ' datestr(now)]);

%% Define Parameters
fprintf('Setting up parameters...\n');
model.param.set('r_mem', [num2str(r_mem) '[um]'], 'Membrane radius');
model.param.set('t_mem', [num2str(t_mem) '[um]'], 'Membrane thickness');
model.param.set('h_cavity', [num2str(h_cavity) '[um]'], 'Cavity depth');
model.param.set('w_support', [num2str(w_support) '[um]'], 'Support width');
model.param.set('E_si', [num2str(E_si) '[Pa]'], 'Young''s modulus');
model.param.set('nu_si', num2str(nu_si), 'Poisson''s ratio');
model.param.set('rho_si', [num2str(rho_si) '[kg/m^3]'], 'Density');
model.param.set('p_applied', [num2str(p_applied) '[Pa]'], 'Applied pressure');
model.param.set('sigma_residual', [num2str(sigma_residual) '[Pa]'], 'Residual stress');

%% Create Component
fprintf('Creating component...\n');
if strcmp(dimension_type, '2D_axisym')
    model.component.create('comp1', true);
    model.component('comp1').geom.create('geom1', 2);
    model.component('comp1').geom('geom1').axisymmetric(true);
else
    model.component.create('comp1', true);
    model.component('comp1').geom.create('geom1', 3);
end

model.component('comp1').geom('geom1').lengthUnit('um');

%% Create Geometry
fprintf('Creating geometry...\n');
geom = model.component('comp1').geom('geom1');

if strcmp(dimension_type, '2D_axisym')
    % Create membrane rectangle
    geom.create('r1', 'Rectangle');
    geom.feature('r1').set('size', {'r_mem', 't_mem'});
    geom.feature('r1').set('pos', {'0', '0'});
    geom.feature('r1').label('Membrane');
    
    % Create support ring rectangle
    geom.create('r2', 'Rectangle');
    geom.feature('r2').set('size', {'w_support', 't_mem'});
    geom.feature('r2').set('pos', {'r_mem', '0'});
    geom.feature('r2').label('Support Ring');
    
    % Form union
    geom.create('uni1', 'Union');
    geom.feature('uni1').selection('input').set({'r1' 'r2'});
    
else
    % Create 3D geometry
    geom.create('wp1', 'WorkPlane');
    geom.feature('wp1').set('quickplane', 'xy');
    
    % Create square on work plane
    geom.feature('wp1').geom.create('sq1', 'Square');
    geom.feature('wp1').geom.feature('sq1').set('size', '2*r_mem');
    geom.feature('wp1').geom.feature('sq1').set('pos', {'-r_mem', '-r_mem'});
    
    % Extrude
    geom.create('ext1', 'Extrude');
    geom.feature('ext1').selection('input').set({'wp1'});
    geom.feature('ext1').setIndex('distance', 't_mem', 0);
end

% Build geometry
geom.run;
fprintf('  Geometry created successfully\n');

%% Create Material
fprintf('Adding material (Silicon)...\n');
model.component('comp1').material.create('mat1', 'Common');
model.component('comp1').material('mat1').label('Silicon');

% Set material properties
model.component('comp1').material('mat1').propertyGroup('def'). ...
    set('density', 'rho_si');
model.component('comp1').material('mat1').propertyGroup('def'). ...
    set('youngsmodulus', 'E_si');
model.component('comp1').material('mat1').propertyGroup('def'). ...
    set('poissonsratio', 'nu_si');

% Assign to all domains
model.component('comp1').material('mat1').selection.all;

fprintf('  Silicon material added\n');

%% Add Physics - Solid Mechanics
fprintf('Setting up physics (Solid Mechanics)...\n');
model.component('comp1').physics.create('solid', 'SolidMechanics', 'geom1');
model.component('comp1').physics('solid').label('Solid Mechanics');

% Initial stress (residual stress)
model.component('comp1').physics('solid').feature('lemm1'). ...
    create('inits1', 'InitialStressandStrain', 2);
model.component('comp1').physics('solid').feature('lemm1'). ...
    feature('inits1').selection.all;
model.component('comp1').physics('solid').feature('lemm1'). ...
    feature('inits1').set('Sil', {'sigma_residual'; '0'; '0'; ...
                                   '0'; 'sigma_residual'; '0'; ...
                                   '0'; '0'; '0'});
model.component('comp1').physics('solid').feature('lemm1'). ...
    feature('inits1').label('Residual Stress');

% Fixed constraint (support boundary)
model.component('comp1').physics('solid').create('fix1', 'Fixed', 1);
model.component('comp1').physics('solid').feature('fix1'). ...
    label('Fixed Support');

if strcmp(dimension_type, '2D_axisym')
    % Select right boundary (outer edge)
    model.component('comp1').physics('solid').feature('fix1'). ...
        selection.set([4]);  % Adjust based on actual boundary number
else
    % For 3D, select outer edges manually in GUI
end

% Boundary load (pressure)
model.component('comp1').physics('solid').create('bndl1', 'BoundaryLoad', 1);
model.component('comp1').physics('solid').feature('bndl1'). ...
    set('LoadType', 'Pressure');
model.component('comp1').physics('solid').feature('bndl1'). ...
    set('Pressure', 'p_applied');
model.component('comp1').physics('solid').feature('bndl1'). ...
    label('Applied Pressure');

if strcmp(dimension_type, '2D_axisym')
    % Select bottom boundary
    model.component('comp1').physics('solid').feature('bndl1'). ...
        selection.set([1]);  % Adjust based on actual boundary number
end

fprintf('  Solid mechanics physics configured\n');

%% Create Mesh
fprintf('Creating mesh...\n');
model.component('comp1').mesh.create('mesh1');

% Set size
model.component('comp1').mesh('mesh1').create('size1', 'Size');
model.component('comp1').mesh('mesh1').feature('size1').selection. ...
    geom('geom1', 2);
model.component('comp1').mesh('mesh1').feature('size1').selection.all;
model.component('comp1').mesh('mesh1').feature('size1'). ...
    set('hauto', 1);  % Extra fine
model.component('comp1').mesh('mesh1').feature('size1'). ...
    set('custom', 'on');
model.component('comp1').mesh('mesh1').feature('size1'). ...
    set('hmax', 't_mem/4');
model.component('comp1').mesh('mesh1').feature('size1'). ...
    set('hmin', 't_mem/10');

% Build mesh
model.component('comp1').mesh('mesh1').run;
fprintf('  Mesh created successfully\n');

%% Create Study
fprintf('Creating study (%s)...\n', study_type);

switch study_type
    case 'stationary'
        model.study.create('std1');
        model.study('std1').create('stat', 'Stationary');
        model.study('std1').label('Stationary Study');
        
    case 'parametric'
        model.study.create('std1');
        model.study('std1').create('stat', 'Stationary');
        model.study('std1').create('param', 'Parametric');
        model.study('std1').feature('param').setIndex('pname', 'p_applied', 0);
        model.study('std1').feature('param').setIndex('plistarr', ...
            'range(0,1[kPa],10[kPa])', 0);
        model.study('std1').label('Parametric Study');
        
    case 'eigenfrequency'
        model.study.create('std1');
        model.study('std1').create('eig', 'Eigenfrequency');
        model.study('std1').feature('eig').set('neigs', 6);
        model.study('std1').feature('eig').set('shift', '10[kHz]');
        model.study('std1').label('Eigenfrequency Study');
end

fprintf('  Study created\n');

%% Create Results
fprintf('Creating result plots...\n');

% Displacement plot
model.result.create('pg1', 'PlotGroup3D');
model.result('pg1').label('Displacement');
model.result('pg1').set('data', 'dset1');
model.result('pg1').create('surf1', 'Surface');
model.result('pg1').feature('surf1').set('expr', 'solid.disp');
model.result('pg1').feature('surf1').set('unit', 'um');
model.result('pg1').feature('surf1').set('descr', 'Total displacement');

% von Mises stress plot
model.result.create('pg2', 'PlotGroup3D');
model.result('pg2').label('von Mises Stress');
model.result('pg2').create('surf1', 'Surface');
model.result('pg2').feature('surf1').set('expr', 'solid.mises');
model.result('pg2').feature('surf1').set('unit', 'MPa');
model.result('pg2').feature('surf1').set('descr', 'von Mises stress');

fprintf('  Result plots configured\n');

%% Solve (Optional - comment out if you want to solve manually)
% fprintf('\nSolving model...\n');
% model.study('std1').run;
% fprintf('  Solution completed\n');

%% Save Model
output_filename = 'membrane_deflection.mph';
fprintf('\nSaving model to %s...\n', output_filename);
model.save(output_filename);
fprintf('  Model saved successfully\n');

%% Summary
fprintf('\n===============================================\n');
fprintf('Model Building Complete!\n');
fprintf('===============================================\n\n');
fprintf('Model Details:\n');
fprintf('  Dimension: %s\n', dimension_type);
fprintf('  Study type: %s\n', study_type);
fprintf('  Membrane radius: %.0f um\n', r_mem);
fprintf('  Membrane thickness: %.1f um\n', t_mem);
fprintf('  Applied pressure: %.1f kPa\n', p_applied/1000);
fprintf('  Output file: %s\n', output_filename);
fprintf('\nNext Steps:\n');
fprintf('  1. Open %s in COMSOL GUI\n', output_filename);
fprintf('  2. Verify boundary selections\n');
fprintf('  3. Run the study\n');
fprintf('  4. Analyze results\n\n');

%% Post-Processing Functions (Optional)

% Uncomment to evaluate maximum deflection after solving:
% if exist('model', 'var')
%     fprintf('Post-processing results...\n');
%     
%     % Get maximum deflection
%     max_disp = mphglobal(model, 'minop1(solid.disp)', 'dataset', 'dset1');
%     fprintf('  Maximum deflection: %.3f um\n', max_disp*1e6);
%     
%     % Get maximum stress
%     max_stress = mphglobal(model, 'maxop1(solid.mises)', 'dataset', 'dset1');
%     fprintf('  Maximum von Mises stress: %.2f MPa\n', max_stress/1e6);
%     
%     % Calculate analytical solution for comparison
%     w_analytical = (3*(1-nu_si^2)*p_applied*(r_mem*1e-6)^4) / ...
%                    (16*E_si*(t_mem*1e-6)^3);
%     fprintf('  Analytical deflection: %.3f um\n', w_analytical*1e6);
%     fprintf('  Difference: %.2f%%\n', abs(max_disp-w_analytical)/w_analytical*100);
% end

fprintf('Script execution completed.\n');