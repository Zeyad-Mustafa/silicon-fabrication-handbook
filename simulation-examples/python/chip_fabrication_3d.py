#!/usr/bin/env python3
"""
3D Chip Fabrication Process Visualization
==========================================

Visualizes MOSFET fabrication steps in 3D using matplotlib.
Shows layer-by-layer process for CMOS transistor formation.

Author: Silicon Fabrication Handbook
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from pathlib import Path
import argparse

# Output directory
DEFAULT_OUTPUT_DIR = Path("images")

# Colors for different materials
COLORS = {
    'silicon': '#8b7355',
    'oxide': '#4fc3f7',
    'poly': '#b0bec5',
    'n_plus': '#ff5252',
    'p_plus': '#9c27b0',
    'metal': '#ffd54f',
    'photoresist': '#ec407a',
    'n_well': '#ffb74d',
}


def create_box(x_range, y_range, z_range, color, alpha=0.8):
    """Create a 3D box as a collection of polygons."""
    x0, x1 = x_range
    y0, y1 = y_range
    z0, z1 = z_range
    
    # Define the 6 faces of the box
    vertices = [
        # Bottom (z=z0)
        [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)],
        # Top (z=z1)
        [(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)],
        # Front (y=y0)
        [(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)],
        # Back (y=y1)
        [(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)],
        # Left (x=x0)
        [(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)],
        # Right (x=x1)
        [(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)],
    ]
    
    return Poly3DCollection(vertices, facecolors=color, linewidths=0.5, 
                           edgecolors='black', alpha=alpha)


def step1_substrate(ax):
    """Step 1: Silicon substrate."""
    substrate = create_box([0, 10], [0, 5], [0, 2], COLORS['silicon'])
    ax.add_collection3d(substrate)
    ax.set_title('Step 1: Silicon Substrate', fontsize=14, fontweight='bold')


def step2_oxidation(ax):
    """Step 2: Thermal oxidation."""
    substrate = create_box([0, 10], [0, 5], [0, 2], COLORS['silicon'])
    oxide = create_box([0, 10], [0, 5], [2, 2.2], COLORS['oxide'])
    ax.add_collection3d(substrate)
    ax.add_collection3d(oxide)
    ax.set_title('Step 2: Thermal Oxidation (SiO₂)', fontsize=14, fontweight='bold')


def step3_photoresist(ax):
    """Step 3: Photoresist coating."""
    substrate = create_box([0, 10], [0, 5], [0, 2], COLORS['silicon'])
    oxide = create_box([0, 10], [0, 5], [2, 2.2], COLORS['oxide'])
    pr = create_box([0, 10], [0, 5], [2.2, 2.6], COLORS['photoresist'], alpha=0.6)
    ax.add_collection3d(substrate)
    ax.add_collection3d(oxide)
    ax.add_collection3d(pr)
    ax.set_title('Step 3: Photoresist Coating', fontsize=14, fontweight='bold')


def step4_lithography(ax):
    """Step 4: Lithography (after exposure and develop)."""
    substrate = create_box([0, 10], [0, 5], [0, 2], COLORS['silicon'])
    oxide = create_box([0, 10], [0, 5], [2, 2.2], COLORS['oxide'])
    # Patterned photoresist
    pr1 = create_box([0, 3], [0, 5], [2.2, 2.6], COLORS['photoresist'], alpha=0.6)
    pr2 = create_box([7, 10], [0, 5], [2.2, 2.6], COLORS['photoresist'], alpha=0.6)
    ax.add_collection3d(substrate)
    ax.add_collection3d(oxide)
    ax.add_collection3d(pr1)
    ax.add_collection3d(pr2)
    ax.set_title('Step 4: Lithography (Pattern)', fontsize=14, fontweight='bold')


def step5_etching(ax):
    """Step 5: Oxide etching."""
    substrate = create_box([0, 10], [0, 5], [0, 2], COLORS['silicon'])
    # Etched oxide
    oxide1 = create_box([0, 3], [0, 5], [2, 2.2], COLORS['oxide'])
    oxide2 = create_box([7, 10], [0, 5], [2, 2.2], COLORS['oxide'])
    pr1 = create_box([0, 3], [0, 5], [2.2, 2.6], COLORS['photoresist'], alpha=0.6)
    pr2 = create_box([7, 10], [0, 5], [2.2, 2.6], COLORS['photoresist'], alpha=0.6)
    ax.add_collection3d(substrate)
    ax.add_collection3d(oxide1)
    ax.add_collection3d(oxide2)
    ax.add_collection3d(pr1)
    ax.add_collection3d(pr2)
    ax.set_title('Step 5: Oxide Etching', fontsize=14, fontweight='bold')


def step6_ion_implant(ax):
    """Step 6: Ion implantation (n+ doping)."""
    substrate = create_box([0, 10], [0, 5], [0, 2], COLORS['silicon'])
    # n+ implanted regions
    n_plus1 = create_box([3, 4.5], [0, 5], [1.7, 2], COLORS['n_plus'], alpha=0.7)
    n_plus2 = create_box([5.5, 7], [0, 5], [1.7, 2], COLORS['n_plus'], alpha=0.7)
    oxide1 = create_box([0, 3], [0, 5], [2, 2.2], COLORS['oxide'])
    oxide2 = create_box([7, 10], [0, 5], [2, 2.2], COLORS['oxide'])
    ax.add_collection3d(substrate)
    ax.add_collection3d(n_plus1)
    ax.add_collection3d(n_plus2)
    ax.add_collection3d(oxide1)
    ax.add_collection3d(oxide2)
    ax.set_title('Step 6: Ion Implantation (n⁺)', fontsize=14, fontweight='bold')


def step7_poly_gate(ax):
    """Step 7: Polysilicon gate deposition."""
    substrate = create_box([0, 10], [0, 5], [0, 2], COLORS['silicon'])
    n_plus1 = create_box([3, 4.5], [0, 5], [1.7, 2], COLORS['n_plus'], alpha=0.7)
    n_plus2 = create_box([5.5, 7], [0, 5], [1.7, 2], COLORS['n_plus'], alpha=0.7)
    oxide1 = create_box([0, 3], [0, 5], [2, 2.2], COLORS['oxide'])
    oxide2 = create_box([7, 10], [0, 5], [2, 2.2], COLORS['oxide'])
    # Poly gate
    gate_oxide = create_box([4.5, 5.5], [0, 5], [2, 2.05], COLORS['oxide'])
    poly = create_box([4.5, 5.5], [0, 5], [2.05, 2.35], COLORS['poly'])
    ax.add_collection3d(substrate)
    ax.add_collection3d(n_plus1)
    ax.add_collection3d(n_plus2)
    ax.add_collection3d(oxide1)
    ax.add_collection3d(oxide2)
    ax.add_collection3d(gate_oxide)
    ax.add_collection3d(poly)
    ax.set_title('Step 7: Polysilicon Gate', fontsize=14, fontweight='bold')


def step8_metallization(ax):
    """Step 8: Metallization (contacts and interconnects)."""
    substrate = create_box([0, 10], [0, 5], [0, 2], COLORS['silicon'])
    n_plus1 = create_box([3, 4.5], [0, 5], [1.7, 2], COLORS['n_plus'], alpha=0.7)
    n_plus2 = create_box([5.5, 7], [0, 5], [1.7, 2], COLORS['n_plus'], alpha=0.7)
    oxide1 = create_box([0, 3], [0, 5], [2, 2.2], COLORS['oxide'])
    oxide2 = create_box([7, 10], [0, 5], [2, 2.2], COLORS['oxide'])
    gate_oxide = create_box([4.5, 5.5], [0, 5], [2, 2.05], COLORS['oxide'])
    poly = create_box([4.5, 5.5], [0, 5], [2.05, 2.35], COLORS['poly'])
    # ILD (interlayer dielectric)
    ild = create_box([0, 10], [0, 5], [2.35, 2.7], COLORS['oxide'], alpha=0.3)
    # Metal contacts
    metal1 = create_box([3.5, 4], [0, 5], [2.7, 3.1], COLORS['metal'])
    metal2 = create_box([4.75, 5.25], [0, 5], [2.7, 3.1], COLORS['metal'])
    metal3 = create_box([6, 6.5], [0, 5], [2.7, 3.1], COLORS['metal'])
    ax.add_collection3d(substrate)
    ax.add_collection3d(n_plus1)
    ax.add_collection3d(n_plus2)
    ax.add_collection3d(oxide1)
    ax.add_collection3d(oxide2)
    ax.add_collection3d(gate_oxide)
    ax.add_collection3d(poly)
    ax.add_collection3d(ild)
    ax.add_collection3d(metal1)
    ax.add_collection3d(metal2)
    ax.add_collection3d(metal3)
    ax.set_title('Step 8: Metallization (Al/Cu)', fontsize=14, fontweight='bold')


def setup_axis(ax, elev=25, azim=45):
    """Configure 3D axis appearance."""
    ax.set_xlabel('X [µm]', fontsize=10)
    ax.set_ylabel('Y [µm]', fontsize=10)
    ax.set_zlabel('Z [µm]', fontsize=10)
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 5])
    ax.set_zlim([0, 4])
    ax.view_init(elev=elev, azim=azim)
    ax.grid(True, alpha=0.3)


def create_fabrication_animation(output_dir, save_plots=True, dpi=300, elev=25, azim=45, show=True):
    """Create step-by-step fabrication visualization."""
    print("Creating 3D chip fabrication visualization...")
    
    steps = [
        step1_substrate,
        step2_oxidation,
        step3_photoresist,
        step4_lithography,
        step5_etching,
        step6_ion_implant,
        step7_poly_gate,
        step8_metallization,
    ]
    
    fig = plt.figure(figsize=(16, 10))
    
    for i, step_func in enumerate(steps, 1):
        ax = fig.add_subplot(2, 4, i, projection='3d')
        step_func(ax)
        setup_axis(ax, elev=elev, azim=azim)
    
    plt.tight_layout()
    
    if save_plots:
        output_file = output_dir / "chip_fabrication_3d.png"
        plt.savefig(output_file, dpi=dpi, bbox_inches='tight')
        print(f"✓ Saved: {output_file}")
    
    if show:
        plt.show()
    print()


def create_final_structure_detail(output_dir, save_plots=True, dpi=300, elev=25, azim=45, show=True):
    """Create detailed view of final MOSFET structure."""
    print("Creating detailed final structure...")
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Build complete nMOS structure
    substrate = create_box([0, 10], [0, 5], [0, 2], COLORS['silicon'])
    n_plus_source = create_box([2.5, 4.2], [0, 5], [1.6, 2], COLORS['n_plus'], alpha=0.8)
    n_plus_drain = create_box([5.8, 7.5], [0, 5], [1.6, 2], COLORS['n_plus'], alpha=0.8)
    
    # STI (Shallow Trench Isolation)
    sti_left = create_box([0, 2.5], [0, 5], [1.5, 2.2], COLORS['oxide'])
    sti_right = create_box([7.5, 10], [0, 5], [1.5, 2.2], COLORS['oxide'])
    
    # Gate stack
    gate_oxide = create_box([4.2, 5.8], [0, 5], [2, 2.05], COLORS['oxide'])
    poly_gate = create_box([4.2, 5.8], [0, 5], [2.05, 2.45], COLORS['poly'])
    
    # Spacers
    spacer_l = create_box([4.0, 4.2], [0, 5], [2, 2.3], COLORS['oxide'], alpha=0.6)
    spacer_r = create_box([5.8, 6.0], [0, 5], [2, 2.3], COLORS['oxide'], alpha=0.6)
    
    # ILD
    ild = create_box([0, 10], [0, 5], [2.45, 2.8], COLORS['oxide'], alpha=0.3)
    
    # Metal contacts
    contact_source = create_box([3.0, 3.8], [0, 5], [2.8, 3.3], COLORS['metal'])
    contact_gate = create_box([4.7, 5.3], [0, 5], [2.8, 3.3], COLORS['metal'])
    contact_drain = create_box([6.2, 7.0], [0, 5], [2.8, 3.3], COLORS['metal'])
    
    # Add all components
    ax.add_collection3d(substrate)
    ax.add_collection3d(n_plus_source)
    ax.add_collection3d(n_plus_drain)
    ax.add_collection3d(sti_left)
    ax.add_collection3d(sti_right)
    ax.add_collection3d(gate_oxide)
    ax.add_collection3d(poly_gate)
    ax.add_collection3d(spacer_l)
    ax.add_collection3d(spacer_r)
    ax.add_collection3d(ild)
    ax.add_collection3d(contact_source)
    ax.add_collection3d(contact_gate)
    ax.add_collection3d(contact_drain)
    
    # Labels
    ax.text(3.4, 5.5, 3.5, 'Source', fontsize=10, color='black', weight='bold')
    ax.text(5.0, 5.5, 3.5, 'Gate', fontsize=10, color='black', weight='bold')
    ax.text(6.6, 5.5, 3.5, 'Drain', fontsize=10, color='black', weight='bold')
    
    setup_axis(ax, elev=elev, azim=azim)
    ax.set_title('Complete nMOS Transistor Structure', fontsize=16, fontweight='bold', pad=20)
    
    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=COLORS['silicon'], label='Silicon'),
        Patch(facecolor=COLORS['oxide'], label='SiO₂'),
        Patch(facecolor=COLORS['poly'], label='Poly-Si'),
        Patch(facecolor=COLORS['n_plus'], label='n⁺'),
        Patch(facecolor=COLORS['metal'], label='Metal'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=10)
    
    plt.tight_layout()
    
    if save_plots:
        output_file = output_dir / "final_mosfet_structure.png"
        plt.savefig(output_file, dpi=dpi, bbox_inches='tight')
        print(f"✓ Saved: {output_file}")
    
    if show:
        plt.show()
    print()


def build_parser():
    parser = argparse.ArgumentParser(
        description="Generate 3D MOSFET fabrication visuals."
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Output directory for generated images.",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=300,
        help="DPI for saved images.",
    )
    parser.add_argument(
        "--no-show",
        action="store_true",
        help="Do not open interactive windows (useful for headless runs).",
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Render figures without saving images.",
    )
    parser.add_argument(
        "--elev",
        type=float,
        default=25,
        help="Camera elevation angle.",
    )
    parser.add_argument(
        "--azim",
        type=float,
        default=45,
        help="Camera azimuth angle.",
    )
    return parser


def main():
    """Run 3D fabrication visualization."""
    parser = build_parser()
    args = parser.parse_args()
    output_dir = args.outdir
    output_dir.mkdir(parents=True, exist_ok=True)
    save_plots = not args.no_save
    show = not args.no_show

    print("=" * 60)
    print("3D Chip Fabrication Process Visualization")
    print("=" * 60)
    print()
    
    create_fabrication_animation(
        output_dir=output_dir,
        save_plots=save_plots,
        dpi=args.dpi,
        elev=args.elev,
        azim=args.azim,
        show=show,
    )
    create_final_structure_detail(
        output_dir=output_dir,
        save_plots=save_plots,
        dpi=args.dpi,
        elev=args.elev,
        azim=args.azim,
        show=show,
    )
    
    print("=" * 60)
    print("Visualization complete!")
    if save_plots:
        print(f"Images saved to: {output_dir}/")
    else:
        print("Images were not saved (--no-save).")
    print("=" * 60)


if __name__ == "__main__":
    main()
