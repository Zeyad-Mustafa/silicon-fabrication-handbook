#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Physical constants
q = 1.602e-19
k_B = 1.381e-23

# Implantation parameters
E_implant = 50  # keV
dose = 1e14  # ions/cm²
N_substrate = 1e15  # cm⁻³

# Range and straggle (Boron in Si)
R_p = 3.66e-6 * E_implant**1.24  # cm
Delta_Rp = 0.52 * R_p

# Depth array
x = np.linspace(0, 5*R_p, 1000)

# Gaussian profile
N_gaussian = (dose / (np.sqrt(2*np.pi) * Delta_Rp)) * \
             np.exp(-0.5 * ((x - R_p) / Delta_Rp)**2)

# Multi-energy implant
energies = [20, 40, 60, 80, 100]
doses_multi = [2e13]*5
N_multi = np.zeros_like(x)

for E_i, dose_i in zip(energies, doses_multi):
    R_p_i = 3.66e-6 * E_i**1.24
    Delta_Rp_i = 0.52 * R_p_i
    N_multi += (dose_i / (np.sqrt(2*np.pi) * Delta_Rp_i)) * \
               np.exp(-0.5 * ((x - R_p_i) / Delta_Rp_i)**2)

# Annealing
T_anneal = 1000 + 273
t_anneal = 30 * 60
D_0 = 0.76
E_a = 3.46
D = D_0 * np.exp(-E_a / (k_B * T_anneal / q))
L_diff = np.sqrt(2 * D * t_anneal)
Delta_total = np.sqrt(Delta_Rp**2 + L_diff**2)
N_annealed = (dose / (np.sqrt(2*np.pi) * Delta_total)) * \
             np.exp(-0.5 * ((x - R_p) / Delta_total)**2)

# Junction depth
idx = np.where(N_annealed >= N_substrate)[0]
x_j = x[idx[-1]] if len(idx) > 0 else None

# Energy vs Range
E_range = np.arange(10, 201, 10)
R_p_range = 3.66e-6 * E_range**1.24
Delta_Rp_range = 0.52 * R_p_range

# Dose vs Peak
dose_range = np.logspace(12, 16, 100)
N_peak_range = dose_range / (np.sqrt(2*np.pi) * Delta_Rp)

# Junction depth vs time
t_range = np.logspace(1, 4, 100)
x_j_range = np.zeros_like(t_range)

for i, t_i in enumerate(t_range):
    L_diff_i = np.sqrt(2 * D * t_i)
    Delta_total_i = np.sqrt(Delta_Rp**2 + L_diff_i**2)
    N_temp = (dose / (np.sqrt(2*np.pi) * Delta_total_i)) * \
             np.exp(-0.5 * ((x - R_p) / Delta_total_i)**2)
    idx = np.where(N_temp >= N_substrate)[0]
    x_j_range[i] = x[idx[-1]] if len(idx) > 0 else np.nan

# Create figure
fig = plt.figure(figsize=(14, 9))
gs = GridSpec(2, 3, figure=fig, hspace=0.3, wspace=0.3)

# Plot 1: Gaussian Profile
ax1 = fig.add_subplot(gs[0, 0])
ax1.semilogy(x*1e4, N_gaussian, 'b-', linewidth=2.5, label='Implanted')
ax1.semilogy(x*1e4, N_substrate*np.ones_like(x), 'r--', linewidth=1.5, label='Substrate')
ax1.axvline(R_p*1e4, color='k', linestyle='--', linewidth=1, label='$R_p$')
ax1.set_xlabel('Depth [μm]', fontsize=11)
ax1.set_ylabel('Concentration [cm⁻³]', fontsize=11)
ax1.set_title(f'Gaussian Profile ({E_implant} keV)', fontsize=13, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend(loc='upper right', fontsize=9)
ax1.set_xlim([0, max(x)*1e4])
ax1.set_ylim([1e13, 1e20])

# Plot 2: As-Implanted vs Annealed
ax2 = fig.add_subplot(gs[0, 1])
ax2.semilogy(x*1e4, N_gaussian, 'b-', linewidth=2, label='As-implanted')
ax2.semilogy(x*1e4, N_annealed, 'r-', linewidth=2, label=f'Annealed ({T_anneal-273:.0f}°C)')
ax2.semilogy(x*1e4, N_substrate*np.ones_like(x), 'k--', linewidth=1.5, label='Substrate')
if x_j is not None:
    ax2.axvline(x_j*1e4, color='g', linestyle='--', linewidth=1.5, label='$x_j$')
ax2.set_xlabel('Depth [μm]', fontsize=11)
ax2.set_ylabel('Concentration [cm⁻³]', fontsize=11)
ax2.set_title('Effect of Annealing', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend(loc='upper right', fontsize=9)
ax2.set_xlim([0, max(x)*1e4])
ax2.set_ylim([1e13, 1e20])

# Plot 3: Multi-Energy
ax3 = fig.add_subplot(gs[0, 2])
ax3.semilogy(x*1e4, N_multi, 'g-', linewidth=2.5, label='Multi-energy')
ax3.semilogy(x*1e4, N_gaussian, 'b--', linewidth=1.5, label=f'Single ({E_implant}keV)')
ax3.set_xlabel('Depth [μm]', fontsize=11)
ax3.set_ylabel('Concentration [cm⁻³]', fontsize=11)
ax3.set_title('Multi-Energy Implant', fontsize=13, fontweight='bold')
ax3.grid(True, alpha=0.3)
ax3.legend(loc='upper right', fontsize=9)
ax3.set_xlim([0, max(x)*1e4])
ax3.set_ylim([1e15, 1e20])

# Plot 4: Energy vs Range
ax4 = fig.add_subplot(gs[1, 0])
ax4.plot(E_range, R_p_range*1e7, 'b-', linewidth=2.5, label='$R_p$')
ax4.plot(E_range, (R_p_range + Delta_Rp_range)*1e7, 'r--', linewidth=1.5, label='$R_p±ΔR_p$')
ax4.plot(E_range, (R_p_range - Delta_Rp_range)*1e7, 'r--', linewidth=1.5)
ax4.axvline(E_implant, color='k', linestyle='--', linewidth=1, label='Current')
ax4.set_xlabel('Energy [keV]', fontsize=11)
ax4.set_ylabel('Depth [nm]', fontsize=11)
ax4.set_title('Range vs. Energy (B in Si)', fontsize=13, fontweight='bold')
ax4.grid(True, alpha=0.3)
ax4.legend(loc='upper left', fontsize=9)

# Plot 5: Dose vs Peak
ax5 = fig.add_subplot(gs[1, 1])
ax5.loglog(dose_range, N_peak_range, 'b-', linewidth=2.5, label='$N_{peak}$')
ax5.axvline(dose, color='r', linestyle='--', linewidth=1.5, label='Current dose')
ax5.axhline(N_substrate, color='k', linestyle='--', linewidth=1.5, label='Substrate')
ax5.set_xlabel('Dose [ions/cm²]', fontsize=11)
ax5.set_ylabel('Peak Concentration [cm⁻³]', fontsize=11)
ax5.set_title('Peak Concentration vs. Dose', fontsize=13, fontweight='bold')
ax5.grid(True, alpha=0.3)
ax5.legend(loc='upper left', fontsize=9)

# Plot 6: Junction Depth vs Time
ax6 = fig.add_subplot(gs[1, 2])
ax6.semilogx(t_range/60, x_j_range*1e4, 'b-', linewidth=2.5, label='$x_j(t)$')
ax6.axvline(t_anneal/60, color='r', linestyle='--', linewidth=1.5, label='Current time')
ax6.set_xlabel('Anneal Time [minutes]', fontsize=11)
ax6.set_ylabel('Junction Depth [μm]', fontsize=11)
ax6.set_title(f'Junction Depth vs. Time ({T_anneal-273:.0f}°C)', fontsize=13, fontweight='bold')
ax6.grid(True, alpha=0.3)
ax6.legend(loc='upper left', fontsize=9)

fig.suptitle('Ion Implantation Profile Analysis', fontsize=15, fontweight='bold', y=0.995)
plt.savefig('/home/claude/images/ion_implant_profile.png', dpi=150, bbox_inches='tight')
print("✓ Saved: images/ion_implant_profile.png")