#!/usr/bin/env python3
"""
3D Capacitive MEMS Sensor Visualization
========================================

Creates interactive 3D visualization of a capacitive accelerometer
showing movable proof mass, fixed electrodes, and capacitive sensing.

Author: Silicon Fabrication Handbook
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from pathlib import Path

# Output directory
OUTPUT_DIR = Path("images")
OUTPUT_DIR.mkdir(exist_ok=True)

# Colors
COLORS = {
    'proof_mass': '#ce93d8',      # Purple (movable)
    'fixed_electrode': '#90caf9',  # Blue (fixed)
    'spring': '#ffd54f',           # Gold
    'anchor': '#8b7355',           # Brown (substrate)
    'substrate': '#e0e0e0',        # Gray
}


def create_box(x_range, y_range, z_range, color, alpha=0.8):
    """Create a 3D box."""
    x0, x1 = x_range
    y0, y1 = y_range
    z0, z1 = z_range
    
    vertices = [
        [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)],  # Bottom
        [(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)],  # Top
        [(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)],  # Front
        [(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)],  # Back
        [(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)],  # Left
        [(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)],  # Right
    ]
    
    return Poly3DCollection(vertices, facecolors=color, linewidths=0.5,
                           edgecolors='black', alpha=alpha)


def create_capacitive_accelerometer_3d():
    """Create 3D model of capacitive accelerometer."""
    print("Creating 3D capacitive accelerometer...")
    
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Dimensions (in micrometers, scaled for visualization)
    proof_mass_size = 50  # 50 µm
    electrode_width = 40
    electrode_thickness = 10
    gap = 2  # 2 µm capacitive gap
    spring_length = 30
    spring_width = 3
    
    # Substrate base
    substrate = create_box([-80, 80], [-80, 80], [-5, 0], 
                          COLORS['substrate'], alpha=0.2)
    ax.add_collection3d(substrate)
    
    # Anchor points (4 corners)
    anchors = [
        create_box([-70, -60], [-70, -60], [0, 5], COLORS['anchor']),
        create_box([60, 70], [-70, -60], [0, 5], COLORS['anchor']),
        create_box([-70, -60], [60, 70], [0, 5], COLORS['anchor']),
        create_box([60, 70], [60, 70], [0, 5], COLORS['anchor']),
    ]
    for anchor in anchors:
        ax.add_collection3d(anchor)
    
    # Folded springs (4 corners connecting to proof mass)
    springs = [
        # Top-left spring
        create_box([-65, -62], [-50, -50+spring_length], [0, 2], COLORS['spring']),
        create_box([-62, -50-spring_width], [-50+spring_length, -50+spring_length+3], [0, 2], COLORS['spring']),
        # Top-right spring
        create_box([62, 65], [-50, -50+spring_length], [0, 2], COLORS['spring']),
        create_box([50+spring_width, 62], [-50+spring_length, -50+spring_length+3], [0, 2], COLORS['spring']),
        # Bottom-left spring
        create_box([-65, -62], [50-spring_length, 50], [0, 2], COLORS['spring']),
        create_box([-62, -50-spring_width], [50-spring_length-3, 50-spring_length], [0, 2], COLORS['spring']),
        # Bottom-right spring
        create_box([62, 65], [50-spring_length, 50], [0, 2], COLORS['spring']),
        create_box([50+spring_width, 62], [50-spring_length-3, 50-spring_length], [0, 2], COLORS['spring']),
    ]
    for spring in springs:
        ax.add_collection3d(spring)
    
    # Central proof mass (movable)
    proof_mass = create_box([-proof_mass_size/2, proof_mass_size/2],
                           [-proof_mass_size/2, proof_mass_size/2],
                           [0, electrode_thickness],
                           COLORS['proof_mass'], alpha=0.9)
    ax.add_collection3d(proof_mass)
    
    # Fixed electrodes (4 sides with capacitive gaps)
    # Left electrode
    left_electrode = create_box([-proof_mass_size/2 - gap - electrode_width,
                                 -proof_mass_size/2 - gap],
                                [-electrode_width, electrode_width],
                                [0, electrode_thickness],
                                COLORS['fixed_electrode'], alpha=0.8)
    ax.add_collection3d(left_electrode)
    
    # Right electrode
    right_electrode = create_box([proof_mass_size/2 + gap,
                                  proof_mass_size/2 + gap + electrode_width],
                                 [-electrode_width, electrode_width],
                                 [0, electrode_thickness],
                                 COLORS['fixed_electrode'], alpha=0.8)
    ax.add_collection3d(right_electrode)
    
    # Top electrode
    top_electrode = create_box([-electrode_width, electrode_width],
                               [proof_mass_size/2 + gap,
                                proof_mass_size/2 + gap + electrode_width],
                               [0, electrode_thickness],
                               COLORS['fixed_electrode'], alpha=0.8)
    ax.add_collection3d(top_electrode)
    
    # Bottom electrode
    bottom_electrode = create_box([-electrode_width, electrode_width],
                                  [-proof_mass_size/2 - gap - electrode_width,
                                   -proof_mass_size/2 - gap],
                                  [0, electrode_thickness],
                                  COLORS['fixed_electrode'], alpha=0.8)
    ax.add_collection3d(bottom_electrode)
    
    # Capacitive gap indicators (thin lines showing gap)
    gap_lines = [
        ([[-proof_mass_size/2, -proof_mass_size/2 - gap]], [[0, 0]], [[5, 5]]),
        ([[proof_mass_size/2, proof_mass_size/2 + gap]], [[0, 0]], [[5, 5]]),
        ([[0, 0]], [[proof_mass_size/2, proof_mass_size/2 + gap]], [[5, 5]]),
        ([[0, 0]], [[-proof_mass_size/2, -proof_mass_size/2 - gap]], [[5, 5]]),
    ]
    
    # Labels
    ax.text(0, 0, 20, 'Proof Mass\n(Movable)', fontsize=11, 
            ha='center', weight='bold', color=COLORS['proof_mass'])
    ax.text(-50, 0, 20, 'Fixed\nElectrode', fontsize=9, 
            ha='center', color=COLORS['fixed_electrode'])
    ax.text(0, -70, 8, 'Spring\nSuspension', fontsize=9, 
            ha='center', color=COLORS['spring'])
    ax.text(65, -65, 8, 'Anchor', fontsize=8, 
            ha='center', color=COLORS['anchor'])
    
    # Gap annotation
    ax.text(-proof_mass_size/2 - gap/2, 0, 15, f'{gap}µm\ngap', 
            fontsize=8, ha='center', color='red', weight='bold')
    
    # Axis settings
    ax.set_xlabel('X [µm]', fontsize=11)
    ax.set_ylabel('Y [µm]', fontsize=11)
    ax.set_zlabel('Z [µm]', fontsize=11)
    ax.set_xlim([-80, 80])
    ax.set_ylim([-80, 80])
    ax.set_zlim([-5, 25])
    ax.view_init(elev=20, azim=45)
    ax.set_title('Capacitive MEMS Accelerometer (3D View)', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=COLORS['proof_mass'], label='Proof Mass (movable)'),
        Patch(facecolor=COLORS['fixed_electrode'], label='Fixed Electrodes'),
        Patch(facecolor=COLORS['spring'], label='Spring Beams'),
        Patch(facecolor=COLORS['anchor'], label='Anchors'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=9)
    
    plt.tight_layout()
    output_file = OUTPUT_DIR / "capacitive_sensor_3d.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_file}")
    plt.show()
    
    print()
    print("Device specifications:")
    print(f"  • Proof mass: {proof_mass_size}×{proof_mass_size}×{electrode_thickness} µm³")
    print(f"  • Capacitive gap: {gap} µm")
    print(f"  • Electrode size: {electrode_width}×{electrode_width}×{electrode_thickness} µm³")
    print(f"  • Spring dimensions: {spring_length}×{spring_width}×2 µm³")
    print()


def create_operating_principle():
    """Show operating principle with displacement."""
    print("Creating operating principle visualization...")
    
    fig = plt.figure(figsize=(16, 5))
    
    # Three states: Rest, +Acceleration, -Acceleration
    states = [
        {'title': 'Rest (No Acceleration)', 'offset': 0, 'ax_idx': 0},
        {'title': 'Acceleration →', 'offset': 5, 'ax_idx': 1},
        {'title': 'Acceleration ←', 'offset': -5, 'ax_idx': 2},
    ]
    
    for state in states:
        ax = fig.add_subplot(1, 3, state['ax_idx'] + 1, projection='3d')
        offset = state['offset']
        
        # Proof mass (displaced)
        proof_mass = create_box([offset-25, offset+25], [-25, 25], [0, 10],
                               COLORS['proof_mass'], alpha=0.9)
        ax.add_collection3d(proof_mass)
        
        # Fixed electrodes
        left_electrode = create_box([-50, -30], [-20, 20], [0, 10],
                                   COLORS['fixed_electrode'], alpha=0.7)
        right_electrode = create_box([30, 50], [-20, 20], [0, 10],
                                    COLORS['fixed_electrode'], alpha=0.7)
        ax.add_collection3d(left_electrode)
        ax.add_collection3d(right_electrode)
        
        # Calculate capacitances
        d_left = abs(-30 - (offset - 25))
        d_right = abs(30 - (offset + 25))
        
        # Gap annotations
        ax.text(-30 + d_left/2, 0, 15, f'd={d_left:.0f}µm', 
                fontsize=9, ha='center', color='red')
        ax.text(30 + d_right/2, 0, 15, f'd={d_right:.0f}µm', 
                fontsize=9, ha='center', color='red')
        
        # Capacitance indicators
        C_left_ratio = 5 / d_left
        C_right_ratio = 5 / d_right
        ax.text(-40, 30, 5, f'C₁∝1/{d_left:.0f}', fontsize=9, color='blue')
        ax.text(40, 30, 5, f'C₂∝1/{d_right:.0f}', fontsize=9, color='blue')
        
        # Differential output
        delta_C = C_left_ratio - C_right_ratio
        ax.text(0, -35, 5, f'ΔC = C₁-C₂', fontsize=10, 
                ha='center', weight='bold', color='purple')
        
        ax.set_xlim([-60, 60])
        ax.set_ylim([-40, 40])
        ax.set_zlim([0, 20])
        ax.set_xlabel('X [µm]', fontsize=9)
        ax.set_ylabel('Y [µm]', fontsize=9)
        ax.set_zlabel('Z [µm]', fontsize=9)
        ax.view_init(elev=15, azim=45)
        ax.set_title(state['title'], fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    output_file = OUTPUT_DIR / "capacitive_operating_principle.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_file}")
    plt.show()
    
    print()
    print("Operating principle:")
    print("  • Acceleration → Proof mass displacement")
    print("  • Displacement → Capacitance change (C = ε₀A/d)")
    print("  • Differential sensing: ΔC = C₁ - C₂")
    print("  • Output voltage: V_out ∝ ΔC")
    print()


def main():
    """Run 3D capacitive sensor visualization."""
    print("=" * 60)
    print("3D Capacitive MEMS Sensor Visualization")
    print("=" * 60)
    print()
    
    create_capacitive_accelerometer_3d()
    create_operating_principle()
    
    print("=" * 60)
    print("Visualization complete!")
    print(f"Images saved to: {OUTPUT_DIR}/")
    print("=" * 60)


if __name__ == "__main__":
    main()