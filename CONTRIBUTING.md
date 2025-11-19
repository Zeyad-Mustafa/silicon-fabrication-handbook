# Contributing to Silicon Fabrication Handbook

Thank you for your interest in contributing to the Silicon Fabrication Handbook! This guide will help you get started.

## 📋 Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How Can I Contribute?](#how-can-i-contribute)
3. [Getting Started](#getting-started)
4. [Contribution Guidelines](#contribution-guidelines)
5. [Style Guidelines](#style-guidelines)
6. [Commit Messages](#commit-messages)
7. [Pull Request Process](#pull-request-process)

---

## Code of Conduct

This project follows a Code of Conduct to ensure a welcoming environment for all contributors:

- **Be respectful**: Treat everyone with respect and kindness
- **Be collaborative**: Work together toward common goals
- **Be professional**: Keep discussions technical and constructive
- **Be inclusive**: Welcome contributors of all backgrounds and experience levels

## How Can I Contribute?

### 🐛 Reporting Bugs

Found an error in the documentation or code? Please open an issue with:

- **Clear title**: Summarize the problem
- **Description**: Detailed explanation of the issue
- **Location**: File name and line number (if applicable)
- **Expected vs. Actual**: What should happen vs. what actually happens
- **Screenshots**: If relevant

**Example**:
```
Title: Incorrect oxide growth rate formula in Chapter 2

Description: The Deal-Grove equation in docs/02-cmos-feol/transistor-fabrication.md
has a typo in the linear rate constant formula.

Location: Line 234
Expected: B/A term
Actual: B*A term
```

### 💡 Suggesting Enhancements

Have an idea to improve the handbook? Open an issue with:

- **Feature description**: What you'd like to add or change
- **Motivation**: Why this would be valuable
- **Implementation ideas**: How it might be done (optional)

### 📝 Improving Documentation

Documentation improvements are always welcome! This includes:

- Fixing typos and grammatical errors
- Clarifying explanations
- Adding examples or illustrations
- Updating outdated information
- Translating content (future feature)

### 💻 Contributing Code

We welcome simulation code contributions:

- Python scripts for device modeling
- MATLAB functions for process simulation
- Jupyter notebooks with interactive examples
- Visualization tools

### 🎨 Creating Diagrams

Visual aids greatly enhance learning:

- Process flow diagrams (use Draw.io format)
- Cross-sectional illustrations
- 3D CAD models (STEP format preferred)
- Animations of fabrication processes

---

## Getting Started

### 1. Fork the Repository

Click the "Fork" button on GitHub to create your own copy.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/silicon-fabrication-handbook.git
cd silicon-fabrication-handbook
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Branch naming conventions:
- `feature/` - New content or functionality
- `fix/` - Bug fixes or corrections
- `docs/` - Documentation improvements
- `refactor/` - Code reorganization

### 4. Make Your Changes

Edit files using your preferred editor. Follow the style guidelines below.

### 5. Test Your Changes

**For documentation**:
- Check markdown rendering
- Verify all links work
- Ensure equations display correctly (LaTeX)

**For code**:
- Run the script/function to ensure it works
- Test with different parameters
- Verify plots are generated correctly

### 6. Commit Your Changes

```bash
git add .
git commit -m "Your descriptive commit message"
```

### 7. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 8. Open a Pull Request

Go to the original repository and click "New Pull Request."

---

## Contribution Guidelines

### Documentation

#### Markdown Style

- Use ATX-style headers (`#` syntax)
- One blank line before and after headers
- Use code fences for code blocks with language specified
- Use tables for structured data
- Include LaTeX equations where appropriate

**Example**:
```markdown
## Section Title

This is a paragraph with some **bold** and *italic* text.

### Subsection

The Deal-Grove equation is:

$$
x^2 + Ax = B(t + \tau)
$$

Where:
- $x$ = oxide thickness
- $t$ = oxidation time
- $A, B$ = rate constants
```

#### Technical Content

- **Accuracy**: Verify all technical information
- **Units**: Always include units (SI preferred)
- **Citations**: Reference sources for data
- **Clarity**: Explain concepts clearly for the target audience
- **Examples**: Include practical examples

#### Structure

Each documentation chapter should include:

1. **Overview**: Brief introduction
2. **Main content**: Detailed technical information
3. **Examples**: Practical applications
4. **Summary**: Key takeaways
5. **Further reading**: References

### Code Contributions

#### Python Style

Follow PEP 8 guidelines:

```python
#!/usr/bin/env python3
"""
Module docstring: Brief description.

Detailed explanation of what this module does.
"""

import numpy as np
import matplotlib.pyplot as plt

def calculate_mobility(temperature, doping_concentration):
    """
    Calculate carrier mobility in silicon.
    
    Args:
        temperature: Temperature in Kelvin
        doping_concentration: Doping in cm^-3
        
    Returns:
        mobility: Carrier mobility in cm²/V·s
    """
    # Implementation here
    pass

# Constants should be UPPERCASE
ELECTRON_CHARGE = 1.602e-19  # C

# Variables should be lowercase with underscores
oxide_thickness = 10e-9  # m
```

**Requirements**:
- Docstrings for all functions and classes
- Type hints encouraged
- Comments for complex logic
- Unit tests for critical functions

#### MATLAB Style

```matlab
function [output1, output2] = functionName(input1, input2)
% FUNCTIONNAME Brief description.
%
%   Detailed explanation of function.
%
%   Inputs:
%       input1 - Description [units]
%       input2 - Description [units]
%
%   Outputs:
%       output1 - Description [units]
%       output2 - Description [units]
%
%   Example:
%       [x, y] = functionName(1, 2);
%
%   Author: Your Name
%   Date: YYYY-MM-DD

% Input validation
validateattributes(input1, {'numeric'}, {'scalar', 'positive'});

% Implementation
output1 = input1 * 2;
output2 = input2 + 1;

end
```

#### Code Quality

- **Modularity**: Break code into reusable functions
- **Documentation**: Comprehensive docstrings and comments
- **Error handling**: Check inputs, provide meaningful errors
- **Plotting**: Clear labels, legends, and titles
- **Performance**: Optimize for readability first, then performance

### Diagrams and Figures

#### Format Requirements

- **Vector graphics** preferred (SVG, PDF for printing)
- **Editable format**: Include source files (.drawio for diagrams)
- **Resolution**: Minimum 300 DPI for raster images
- **File size**: Optimize images (<1MB per file when possible)

#### Content Guidelines

- **Labels**: All components should be clearly labeled
- **Scale bars**: Include scale references where appropriate
- **Color scheme**: Use colorblind-friendly palettes
- **Consistency**: Match style with existing figures

---

## Style Guidelines

### Writing Style

- **Clarity**: Write for understanding, not to impress
- **Conciseness**: Be thorough but avoid unnecessary verbosity
- **Active voice**: Prefer active over passive voice
- **Present tense**: Use present tense for general descriptions
- **Audience**: Write for advanced undergraduates and graduate students

**Good**:
> "The ion implanter accelerates dopant ions to energies of 10-200 keV."

**Avoid**:
> "Dopant ions are being accelerated by the ion implantation system to energy levels that typically range anywhere from approximately 10 keV up to potentially 200 keV or thereabouts."

### Technical Terminology

- **Consistency**: Use consistent terminology throughout
- **Abbreviations**: Define on first use: "Chemical Vapor Deposition (CVD)"
- **Units**: Use SI units with accepted semiconductor conventions
  - Distances: nm, μm for small; mm, cm for wafer-level
  - Doping: atoms/cm³
  - Resistivity: Ω·cm or Ω/square

### Mathematical Notation

Use LaTeX for equations:

**Inline**: `$E = mc^2$` → $E = mc^2$

**Display**:
```latex
$$
\frac{d^2x}{dt^2} + 2\zeta\omega_n\frac{dx}{dt} + \omega_n^2 x = \frac{F(t)}{m}
$$
```

---

## Commit Messages

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type

- `feat`: New feature or content
- `fix`: Bug fix or correction
- `docs`: Documentation improvements
- `style`: Formatting changes (no content change)
- `refactor`: Code restructuring
- `test`: Adding or modifying tests
- `chore`: Maintenance tasks

### Examples

**Good commit messages**:
```
feat(cmos): Add FinFET fabrication section

Adds comprehensive documentation on FinFET transistor fabrication
including sidewall image transfer lithography and fin patterning.

Closes #45
```

```
fix(python): Correct spring constant calculation

The formula was missing the factor of 4 for folded beams.
Updated mems_spring_mass.py line 67.

Fixes #78
```

**Avoid**:
```
Update files
Fixed stuff
Changes
```

---

## Pull Request Process

### Before Submitting

- [ ] Code runs without errors
- [ ] Documentation renders correctly
- [ ] All tests pass (if applicable)
- [ ] Commit messages follow guidelines
- [ ] Changes are focused and logical

### PR Description Template

```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] New content/feature
- [ ] Bug fix/correction
- [ ] Documentation improvement
- [ ] Code refactoring

## Motivation
Why is this change needed?

## Testing
How were these changes tested?

## Screenshots (if applicable)
Add screenshots for visual changes.

## Checklist
- [ ] Follows style guidelines
- [ ] Self-reviewed code/content
- [ ] Commented complex sections
- [ ] Updated documentation
- [ ] No new warnings or errors

## Related Issues
Closes #XX
```

### Review Process

1. **Automated checks**: CI runs basic validation
2. **Maintainer review**: A maintainer reviews your PR
3. **Feedback**: Address any requested changes
4. **Approval**: PR is approved and merged

**Timeline**: Most PRs reviewed within 1 week

### After Your PR is Merged

- Your contribution is live! 🎉
- Your name is added to contributors list
- Delete your feature branch
- Pull the latest changes from main

```bash
git checkout main
git pull upstream main
git branch -d feature/your-feature-name
```

---

## Recognition

All contributors are recognized in:

- **README.md**: Contributors section
- **AUTHORS.md**: Detailed contribution list
- **Commit history**: Permanent record

---

## Questions?

- **Documentation**: Open an issue with tag `question`
- **Email**: contact@yourproject.org
- **Discussions**: Use GitHub Discussions for general questions

---

## Resources for Contributors

### Learning Resources

- **Markdown**: [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/)
- **LaTeX Math**: [LaTeX Math Symbols](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)
- **Git**: [Git Documentation](https://git-scm.com/doc)
- **Python**: [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

### Tools

- **Markdown Editor**: VS Code, Typora, Mark Text
- **Diagram Creation**: Draw.io, Inkscape, Adobe Illustrator
- **LaTeX Rendering**: MathJax, KaTeX
- **Code Formatting**: Black (Python), MATLAB Editor

---

## License

By contributing, you agree that your contributions will be licensed under:
- **Code**: MIT License
- **Documentation**: CC BY 4.0

See [LICENSE](LICENSE) for details.

---

**Thank you for contributing to the Silicon Fabrication Handbook!**

Your contributions help educate and inspire the next generation of engineers and scientists.
