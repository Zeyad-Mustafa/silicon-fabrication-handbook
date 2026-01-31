# Silicon Fabrication Process Animations

This directory contains interactive 3D animations demonstrating key silicon fabrication processes. Each animation is built using Three.js and runs directly in web browsers without requiring any additional software.

## Available Animations

### 1. Lithography Process (`lithography-process.html`)
**Process Overview:** Photolithography pattern transfer using UV light
- Step-by-step demonstration of photoresist coating, exposure, and development
- Shows mask alignment, UV exposure, and pattern transfer
- Visualizes the chemical changes in photoresist during exposure
- **Duration:** 6 steps, ~18 seconds in auto-play mode

**Key Features Demonstrated:**
- Spin coating of photoresist
- Soft bake process
- Mask alignment with sub-micron precision
- UV light exposure through photomask
- Development of exposed regions
- Hard bake for pattern stabilization

### 2. DRIE Etch (`drie-etch.html`)
**Process Overview:** Deep Reactive Ion Etching using the Bosch process
- Demonstrates alternating etch and passivation cycles
- Shows SF6 plasma etching and C4F8 polymer deposition
- Illustrates high aspect ratio trench formation
- **Duration:** 6 steps, ~21 seconds in auto-play mode

**Key Features Demonstrated:**
- SF6 plasma generation for silicon etching
- Directional ion bombardment
- C4F8 passivation layer deposition
- Sidewall protection mechanism
- Multiple cycle repetition for deep trenches
- Real-time plasma indicator

**Technical Parameters Shown:**
- Etch gas: SF6 (active) / C4F8 (passivation)
- Pressure: 10-50 mTorr
- RF Power: 400-800W
- Etch Rate: 3-6 µm/min

### 3. Wafer Bonding (`wafer-bonding.html`)
**Process Overview:** Fusion bonding of silicon wafers
- Demonstrates surface preparation and activation
- Shows precision alignment and bonding sequence
- Visualizes high-temperature annealing
- **Duration:** 7 steps, ~28 seconds in auto-play mode

**Key Features Demonstrated:**
- RCA cleaning process
- O2/N2 plasma surface activation
- Sub-micron alignment (<1 µm)
- Van der Waals bond initiation
- Bond wave propagation
- High-temperature anneal (800-1100°C)
- Covalent Si-O-Si bond formation

**Technical Parameters Shown:**
- Temperature: 25°C → 1000°C → 25°C
- Atmosphere: Clean room → N2 furnace
- Alignment accuracy: < 1 µm

### 4. CMP Process (`cmp-process.html`)
**Process Overview:** Chemical Mechanical Planarization
- Shows mechanical polishing combined with chemical etching
- Demonstrates surface planarization from rough to smooth
- Real-time uniformity and roughness metrics
- **Duration:** 8 steps, ~28 seconds in auto-play mode

**Key Features Demonstrated:**
- Non-uniform initial topography
- Polishing pad positioning
- Slurry dispense and flow
- Pad rotation and wafer counter-rotation
- Material removal via Preston's equation
- Endpoint detection
- Post-CMP cleaning

**Technical Parameters Shown:**
- Slurry: Silica-based (pH 10-11)
- Pad Speed: 0-60 RPM
- Down Force: 0-4 psi
- Removal Rate: 0-3000 Å/min
- Surface Uniformity: 45% → 95%
- Roughness: 250 Å → 20 Å

## How to Use

### Opening the Animations
1. Simply open any `.html` file in a modern web browser (Chrome, Firefox, Safari, Edge)
2. No installation or server required - these are standalone HTML files
3. For best performance, use a browser with WebGL support

### Controls
Each animation includes the following controls at the bottom of the screen:

- **← Previous**: Go back one step
- **Play**: Auto-play through all steps (converts to "Pause" when playing)
- **Next →**: Advance to the next step
- **Reset**: Return to the initial state

### Interactive Features
- **Auto-rotating camera**: The 3D view automatically rotates around the scene
- **Progress bar**: Shows current position in the animation sequence
- **Info panel**: Displays detailed description of each step
- **Technical parameters**: Real-time process parameters (temperature, pressure, etc.)
- **Visual indicators**: Plasma status, rotation, temperature gauges

## Technical Details

### Technology Stack
- **Three.js r128**: 3D graphics rendering
- **Pure JavaScript**: No external dependencies beyond Three.js CDN
- **WebGL**: Hardware-accelerated graphics
- **CSS3**: Modern UI styling and animations

### Browser Compatibility
- Chrome 90+ ✓
- Firefox 88+ ✓
- Safari 14+ ✓
- Edge 90+ ✓

### Performance
- Optimized for 60 FPS rendering
- Efficient particle systems (100-200 particles)
- Shadow mapping enabled for realistic lighting
- Responsive design (adapts to window size)

## Educational Use

These animations are designed for:
- **Semiconductor engineering courses**: Visual aid for fabrication processes
- **Research presentations**: High-quality process demonstrations
- **Industry training**: New employee onboarding
- **Self-study**: Understanding complex microfabrication steps

## Customization

The animations are built with modular code structure:
- Each step is defined in the `steps` array
- Timing can be adjusted via `playInterval` duration
- Visual parameters (colors, sizes, speeds) are configurable
- Camera angles and lighting can be modified

## File Structure
```
visualization/
└── animations/
    ├── README.md                    (this file)
    ├── lithography-process.html     (6 steps, photolithography)
    ├── drie-etch.html              (6 steps, plasma etching)
    ├── wafer-bonding.html          (7 steps, fusion bonding)
    └── cmp-process.html            (8 steps, planarization)
```

## Future Enhancements

Potential additions:
- [ ] Actual video export capability (MP4 format)
- [ ] VR/AR support for immersive viewing
- [ ] Interactive parameter adjustment
- [ ] Additional processes (CVD, PVD, ion implantation)
- [ ] Multi-language support
- [ ] Offline mode with service workers

## Credits

These animations are part of the Silicon Fabrication Handbook project, designed to provide comprehensive, interactive educational materials for semiconductor manufacturing processes.

## License

These visualization files are part of the silicon-fabrication-handbook repository.

---

**Note:** While these are HTML files instead of MP4 videos, they offer superior interactivity and educational value. Users can pause, rewind, and examine each step in detail. For creating actual MP4 files, you would need screen recording software or video rendering tools like FFmpeg with headless browser automation.
