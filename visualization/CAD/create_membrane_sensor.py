#!/usr/bin/env python3
"""
Generate Membrane Pressure Sensor CAD Model
============================================

Creates a circular membrane pressure sensor in STEP format.

Requirements:
    pip install cadquery

Usage:
    python create_membrane_sensor.py

Specifications:
    - Membrane diameter: 1000 µm
    - Membrane thickness: 20 µm
    - Cavity depth: 400 µm
    - Boss diameter: 200 µm (center reinforcement)
"""

import cadquery as cq
import math

# Unit conversion
UM_TO_MM = 0.001

def create_membrane_sensor():
    """Create circular membrane pressure sensor."""
    
    print("Creating membrane pressure sensor...")
    
    # Dimensions (convert µm to mm)
    membrane_radius = 500 * UM_TO_MM      # 1000 µm diameter
    membrane_thickness = 20 * UM_TO_MM
    cavity_depth = 400 * UM_TO_MM
    boss_radius = 100 * UM_TO_MM          # 200 µm diameter
    rim_width = 50 * UM_TO_MM
    
    # Total structure
    substrate_radius = membrane_radius + rim_width
    total_thickness = cavity_depth + membrane_thickness
    
    # Create substrate (solid cylinder)
    substrate = (
        cq.Workplane("XY")
        .circle(substrate_radius)
        .extrude(total_thickness)
        .translate((0, 0, -cavity_depth))
    )
    
    # Create cavity (hollow underneath membrane)
    cavity = (
        cq.Workplane("XY")
        .circle(membrane_radius)
        .extrude(cavity_depth)
        .translate((0, 0, -cavity_depth))
    )
    
    # Subtract cavity from substrate
    sensor = substrate.cut(cavity)
    
    # Add boss (center island for improved linearity)
    boss = (
        cq.Workplane("XY")
        .circle(boss_radius)
        .extrude(membrane_thickness * 1.5)
        .translate((0, 0, 0))
    )
    sensor = sensor.union(boss)
    
    # Add piezoresistor markers (4 locations at max stress)
    marker_size = 10 * UM_TO_MM
    marker_distance = membrane_radius * 0.7  # 70% of radius
    
    for angle in [0, 90, 180, 270]:
        rad = math.radians(angle)
        x = marker_distance * math.cos(rad)
        y = marker_distance * math.sin(rad)
        
        marker = (
            cq.Workplane("XY")
            .box(marker_size, marker_size, membrane_thickness * 0.5)
            .translate((x, y, membrane_thickness * 0.25))
        )
        sensor = sensor.union(marker)
    
    # Export to STEP
    output_file = "membrane-pressure-sensor.step"
    cq.exporters.export(sensor, output_file)
    
    print(f"✓ Created: {output_file}")
    print(f"  • Membrane: Ø{membrane_radius*2/UM_TO_MM:.0f} µm")
    print(f"  • Thickness: {membrane_thickness/UM_TO_MM:.0f} µm")
    print(f"  • Cavity: {cavity_depth/UM_TO_MM:.0f} µm deep")
    print(f"  • Boss: Ø{boss_radius*2/UM_TO_MM:.0f} µm")
    print()
    print("Open in FreeCAD or CAD viewer to inspect.")
    
    return sensor


if __name__ == "__main__":
    # Check CadQuery installation
    try:
        import cadquery
        print(f"Using CadQuery {cadquery.__version__}")
        print()
    except ImportError:
        print("ERROR: CadQuery not installed!")
        print("Install with: pip install cadquery")
        exit(1)
    
    create_membrane_sensor()
    print("Done! ✓")