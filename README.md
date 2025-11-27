# Silicon Fabrication Handbook

> Your friendly guide to making computer chips and tiny sensors!

## What's This About?

This is a complete guide that shows you how computer chips (CMOS) and tiny mechanical sensors (MEMS) are made. I started this as my personal study notes while learning at **BTU (Brandenburg University of Technology)** and attending industry events, and I've turned it into something that can help anyone learning about semiconductors.

Whether you're a student just starting out, a researcher, or working in the industry, you'll find everything explained step-by-step.

### Where These Notes Come From

**University Courses at BTU:**
- Semiconductor Technology - *Prof. Dr.-Ing. Gerhard Kahmen*
- Seminar on Experimental Physics - *Prof. Dr. rer. nat. habil. Jan Ingo Flege*
- Microsystems - *Prof. Dr.-Ing. Dr. rer. nat. habil. Harald Schenk*
- Advanced Microsystems, Focus on Microsensors - *Prof. Dr.-Ing. Dr. rer. nat. habil. Harald Schenk*
- Principles of Superconductivity - *Prof. Dr. rer. nat. habil. Götz Seibold*
- Nanoelectronics - *PD Dr. rer. nat. habil. Ulrich Wulf*

**Industry Events & Workshops:**
- **iCampµs (ICCC 2024)** - International Conference on Compound Semiconductors
- **Forschungsfabrik Mikroelektronik Deutschland (FMD)** - Green ICT Camp 2025

These notes combine academic knowledge with real-world industry insights!

---

## What's Inside?

### Main Chapters

**Completed:**
1. **[Introduction](docs/01-introduction)** - Start here! Learn about silicon wafers, cleanrooms, and how a chip factory works
2. **[CMOS FEOL](docs/02-cmos-feol)** - The first steps: doping, oxidation, making transistor gates
3. **[CMOS BEOL](docs/03-cmos-beol)** - The final steps: metal wiring, connecting everything together

**Work in Progress:**
4. **[MEMS Surface Micromachining](docs/04-mems-surface-micromachining)** - Making tiny structures on the surface using sacrificial layers *(currently being written)*
5. **[MEMS Bulk Micromachining](docs/05-mems-bulk-micromachining)** - Cutting deep into silicon to make sensors *(coming soon)*
6. **[Packaging](docs/06-packaging)** - Protecting your chip: wire bonding, flip-chip, and more *(coming soon)*
7. **[Testing & Yield](docs/07-testing-yield)** - Making sure chips work and tracking defects *(coming soon)*
8. **[Integrated MEMS-CMOS](docs/08-integrated-mems-cmos)** - Combining sensors and electronics together *(coming soon)*

### Extra Goodies

- **[Simulation Examples](simulation-examples)** - Working code (MATLAB & Python) to model devices
- **[Diagrams & Visualizations](diagrams)** - Pictures of processes, cross-sections, 3D models
- **[Animations](visualization/animations)** - Watch fabrication processes step-by-step
- **[Research Papers Database](resources/research-papers.md)** - Collection of important papers
- **[Equipment Reference](resources/fab-equipment-list.md)** - List of common tools and what they do
- **[Design Rules](resources/design-rules-examples.md)** - Rules for designing chips that actually work

For a detailed breakdown of how everything is organized, check out [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md).

---

## How to Use This

### Quick Start

```bash
# Download everything
git clone https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook.git
cd silicon-fabrication-handbook

# Start reading
cd docs/01-introduction
cat overview.md

# Try the simulations
cd simulation-examples/python
pip install -r requirements.txt
jupyter notebook mems_spring_mass.ipynb
```

---

## Real Examples

### Making a Basic Chip (CMOS)
```
Silicon Wafer → Grow Oxide Layer → Print Pattern (Lithography) → 
Add Dopants (Ion Implant) → Heat Treatment → Make Gates → 
Add Metal Wiring → Protective Layer → Test It
```

### Making an Accelerometer (Surface MEMS)
```
Silicon → Grow Oxide → Deposit Polysilicon → Pattern It → 
Remove Sacrificial Layer → Dry It Carefully → Package It
```

### Making a Pressure Sensor (Bulk MEMS)
```
SOI Wafer → Etch from Back → Create Cavity → Make Thin Diaphragm → 
Add Piezoresistors → Bond Glass → Wire Bond
```

---

## Simulations & Analysis

We include real working simulations that you can run:

- **Frequency response** of silicon sensors
- **Step response** analysis 
- **Shock response** for packaging design

All with code you can modify and learn from!

---

## What You Need

- **Documentation**: Just a browser to read the Markdown files
- **Simulations**: MATLAB R2020+ or Python 3.8+
- **Diagrams**: Draw.io or Inkscape (all diagrams are editable!)


---

## Want to Help?

I'd love your contributions! Check out [CONTRIBUTING.md](CONTRIBUTING.md) for details.

**You can help by:**
- Adding new process documentation (the same UNi or others as well )
- Fixing mistakes or suggesting improvements
- Sharing simulation examples
- Creating diagrams or animations
- Recommending research papers

---

## Use This in Your Work?

If you use this handbook for research or teaching, here's how to cite it:

```bibtex
@misc{silicon_fab_handbook_2025,
  title={Silicon Fabrication Handbook: A Comprehensive Guide to CMOS and MEMS Processing},
  author={Contributors},
  year={2025},
  publisher={GitHub},
  url={https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook}
}
```

---

## License

Everything is open and free to use:
- Code: MIT License (use it however you want!)
- Diagrams: CC BY 4.0 (share and remix with credit)
- Papers: Linked to original sources

See [LICENSE](LICENSE) for full details.

---

## Thank You To

- **BTU Cottbus-Senftenberg**: Special thanks to all professors who shared their knowledge
- **iCampµs (ICCC 2024)**: For insights into compound semiconductors
- **Forschungsfabrik Mikroelektronik Deutschland (FMD)**: For the Green ICT Camp 2025 experience
- **Companies**: IHP, TSMC, Intel, Samsung for their public documentation
- **Universities**: MIT, Stanford, Berkeley for MEMS research
- **Open Source Community**: Everyone who makes Python and MATLAB tools

---

## Get in Touch

- **Questions or Issues?** [GitHub Issues](https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook/discussions)
- **Email**: [zeyad.uni@gmail.com](mailto:zeyad.uni@gmail.com)

---

## Coming Next

- Advanced FinFET documentation
- GaN and SiC processes
- Interactive 3D wafer visualizer
- Video lecture series (if possible )
- Translations in other languages (Kurdish as well after finishing the project completly)

---

## Like This?

Star this repository if you find it helpful! It helps others discover it too.

---

**Last Updated**: November 2025

Made with ❤️ for everyone learning about semiconductors .