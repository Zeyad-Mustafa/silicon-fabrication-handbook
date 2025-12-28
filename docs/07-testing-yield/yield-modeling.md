# Yield Modeling for MEMS

## Table of Contents
- [Introduction](#introduction)
- [Defect-Based Models](#defect-based-models)
- [Parametric Yield Models](#parametric-yield-models)
- [Spatial Analysis](#spatial-analysis)
- [Yield Prediction](#yield-prediction)
- [Yield Improvement](#yield-improvement)
- [References](#references)

## Introduction

Yield modeling quantifies the relationship between defects, process variations, and manufacturing yield. It enables yield prediction, process optimization, and cost estimation.

### Yield Definitions

**Types of Yield:**

```
Fab Yield (Y_fab):
- Dies passing electrical test at wafer level
- Y_fab = Good die / Total die on wafer

Probe Yield:
- Dies passing parametric test
- Often same as fab yield

Package Yield (Y_pkg):
- Devices passing after assembly
- Y_pkg = Good packages / Packaged units

Final Yield (Y_final):
- Devices passing final test after burn-in
- Y_final = Shipped units / Started units

Cumulative Yield:
Y_total = Y_fab × Y_pkg × Y_final

Example:
Y_fab = 90%, Y_pkg = 98%, Y_final = 99%
Y_total = 0.90 × 0.98 × 0.99 = 87.3%
```

### Yield Loss Mechanisms

**Categories:**

| Category | Examples | Typical Impact | Detection |
|----------|----------|----------------|-----------|
| Random defects | Particles, scratches | 5-20% loss | Wafer inspection |
| Systematic defects | Edge effects, pattern | 2-10% loss | Spatial analysis |
| Parametric | Out-of-spec values | 5-15% loss | Electrical test |
| Latent defects | Early failures | 1-5% loss | Burn-in, reliability |

## Defect-Based Models

### Poisson Yield Model (Murphy)

**Assumption:** Random defects follow Poisson distribution

```
Y = exp(-D₀ × A)

Where:
Y = yield (fraction)
D₀ = defect density (defects/cm²)
A = die area (cm²)

Interpretation:
- Assumes fatal defect if any defect in die
- Exponential decrease with die size
- Simple but pessimistic
```

**Example Calculation:**

```
Given:
Defect density: D₀ = 0.5 defects/cm²
Die size: 5 × 5 mm = 0.25 cm²

Y = exp(-0.5 × 0.25)
Y = exp(-0.125)
Y = 0.882 = 88.2%

For different die sizes:
Die (mm²) | Area (cm²) | Yield
----------|------------|------
2×2       | 0.04       | 98.0%
5×5       | 0.25       | 88.2%
10×10     | 1.00       | 60.7%
15×15     | 2.25       | 32.5%

Observation: Yield decreases exponentially with area
```

### Negative Binomial Model (Seeds)

**More Realistic:** Accounts for defect clustering

```
Y = [1 + (D₀ × A)/α]^(-α)

Where:
α = clustering parameter
α → ∞: Random (approaches Poisson)
α ≈ 2-5: Moderate clustering (typical)
α ≈ 0.5-1: Strong clustering

Higher α = less clustering
Lower α = more clustering
```

**Comparison:**

```
Given: D₀ = 0.5, A = 0.25 cm²

Model            | α    | Yield
-----------------|------|------
Poisson          | ∞    | 88.2%
Neg. Binomial    | 5    | 89.5%
Neg. Binomial    | 2    | 92.3%
Neg. Binomial    | 1    | 94.1%

Clustering improves yield prediction accuracy
Typical for MEMS: α = 2-3
```

### Bose-Einstein Model

**For Systematic Defects:**

```
Y = (1 - Φ)^(A/A_crit)

Where:
Φ = critical area fraction
A_crit = critical area size

Use when:
- Lithography issues
- Pattern-dependent effects
- Edge exclusion
```

### Defect Density Calculation

**From Yield Data:**

```
Given yield and die area, solve for D₀:

Poisson:
D₀ = -ln(Y) / A

Negative Binomial:
D₀ = α/A × [(1/Y)^(1/α) - 1]

Example:
Measured yield: 88%
Die area: 0.25 cm²

Poisson:
D₀ = -ln(0.88) / 0.25
D₀ = 0.128 / 0.25
D₀ = 0.51 defects/cm²

Verification:
Y = exp(-0.51 × 0.25) = 88% ✓
```

### Critical Area Analysis

**Refined Defect Model:**

```
Not all defects are fatal:
- Small defects may not bridge features
- Location matters (active vs non-active)

Critical area (A_crit):
Area where defect of size x causes failure

Y = exp(-Σ D(x) × A_crit(x) × Δx)

Where:
D(x) = defect density for size x
A_crit(x) = critical area for size x

Typical: A_crit << physical area
```

**Example:**

```
Physical die area: 25 mm² = 0.25 cm²
Critical area (shorts): 2 mm² = 0.02 cm²
Critical area (opens): 1 mm² = 0.01 cm²
Defect density: 0.5 defects/cm²

Y_shorts = exp(-0.5 × 0.02) = 99.0%
Y_opens = exp(-0.5 × 0.01) = 99.5%
Y_total = 0.990 × 0.995 = 98.5%

vs Poisson (full area):
Y = exp(-0.5 × 0.25) = 88.2%

Critical area analysis more accurate!
```

## Parametric Yield Models

### Normal Distribution Model

**For Continuous Parameters:**

```
Parameter with normal distribution:
μ = mean
σ = standard deviation

Spec limits: [LSL, USL]

Y = Φ((USL - μ)/σ) - Φ((LSL - μ)/σ)

Where Φ = cumulative normal distribution

Relation to Cpk:
Y ≈ 1 - 2 × Φ(-3 × Cpk)

For Cpk = 1.33:
Y = 1 - 2 × Φ(-4) = 99.9937% (63 ppm)
```

**Example:**

```
Resist thickness:
μ = 500 nm
σ = 5 nm
LSL = 480 nm
USL = 520 nm

Z_USL = (520 - 500) / 5 = 4.0
Z_LSL = (480 - 500) / 5 = -4.0

Y = Φ(4.0) - Φ(-4.0)
Y = 0.99997 - 0.00003
Y = 0.99994 = 99.994%

Defect rate: 60 ppm (30 ppm each tail)
```

### Monte Carlo Simulation

**For Complex Interactions:**

```
When:
- Multiple correlated parameters
- Non-normal distributions
- Complex pass/fail criteria

Method:
1. Generate random parameter values
2. Check against specifications
3. Count passes and failures
4. Repeat N times (10,000-1,000,000)
5. Yield = Passes / N

Advantages:
- Handles complexity
- No analytical solution needed
- Accounts for correlations

Disadvantages:
- Computationally intensive
- Requires parameter models
```

**Example Pseudo-code:**

```python
def monte_carlo_yield(n_samples=100000):
    passes = 0
    
    for i in range(n_samples):
        # Generate parameters (correlated)
        thickness = normal(500, 5)
        etch_rate = normal(100, 3)
        
        # Calculate derived parameter
        final_depth = thickness * etch_rate / 100
        
        # Check specifications
        if 480 < thickness < 520 and \
           95 < etch_rate < 105 and \
           470 < final_depth < 530:
            passes += 1
    
    yield_fraction = passes / n_samples
    return yield_fraction

# Result: 98.5% (accounts for correlation)
```

### RSS (Root Sum Square) Model

**For Independent Parameters:**

```
Multiple independent parameters:
σ_total = √(σ₁² + σ₂² + ... + σₙ²)

Then use normal distribution:
Y = Φ((USL - μ)/σ_total) - Φ((LSL - μ)/σ_total)

Example:
Final dimension = A + B - C
σ_A = 2 nm, σ_B = 3 nm, σ_C = 1.5 nm

σ_total = √(2² + 3² + 1.5²)
σ_total = √(4 + 9 + 2.25)
σ_total = √15.25
σ_total = 3.9 nm
```

## Spatial Analysis

### Wafer Maps

**Yield vs Position:**

```
Wafer divided into regions:
- Center
- Mid-radius
- Edge
- Quadrants

Pattern types:
1. Center-high: Process uniformity issue
2. Edge-low: Edge exclusion, uniformity
3. Quadrant: Equipment asymmetry
4. Random: Defect-limited
5. Bulls-eye: Radial gradient (temp, flow)
```

**Edge Exclusion:**

```
Unusable area at wafer edge

Typical exclusion: 2-5 mm

For 200 mm wafer:
Total area: π × 10² = 314 cm²
Exclusion (3 mm): π × (10² - 9.7²) = 19.4 cm²
Loss: 6.2% of area

For 300 mm wafer:
Total area: 707 cm²
Exclusion (3 mm): 28.8 cm²
Loss: 4.1% of area

Advantage of larger wafers!
```

### Bin Analysis

**Spatial Patterns:**

```
Bin Pareto:
Rank failure bins by frequency

Example:
Bin | Description        | Count | %   | Cumulative
----|-------------------|-------|-----|------------
1   | Pass              | 8500  | 85% | 85%
4   | High leakage      | 600   | 6%  | 91%
7   | Low sensitivity   | 400   | 4%  | 95%
5   | Shorts            | 300   | 3%  | 98%
8   | Open circuit      | 100   | 1%  | 99%
X   | Other             | 100   | 1%  | 100%

Focus: Top 3 bins (80/20 rule)
```

**Cluster Detection:**

```
Statistical tests:
- Random vs clustered
- Z-score for each die location
- Neighboring die correlation

If clustered:
- Tool issue (chamber region)
- Reticle defect (repeating pattern)
- Process gradient (temperature)

If random:
- Particles
- Handling damage
- Material defects
```

### Learning Curves

**Yield Improvement Over Time:**

```
Wright's Law:
Y_n = Y_1 × n^b

Where:
Y_n = yield at unit n
Y_1 = first unit yield
n = cumulative units
b = learning rate exponent

Learning rate (LR):
LR = 2^b (yield doubles every LR units)

Typical: LR = 70-85%
(30-15% yield gain per doubling)
```

**Example:**

```
First lot: Y = 60%
Learning rate: 80%

After 10 lots (log₂(10) = 3.32 doublings):
Y = 60% × 10^(log₂(0.8))
Y = 60% × 10^(-0.322)
Y = 60% × 0.476 = 28.6%... wait, that's wrong!

Correct:
b = log₂(0.8) = -0.322
Y_10 = 60% × 10^(-0.322)
Y_10 = 60% × 0.476

Actually, use:
Y_n = Y_1 × (1 + (n-1) × r)

Where r = learning rate per unit

More practical model:
Y_n = Y_∞ - (Y_∞ - Y_1) × exp(-k × n)

Where:
Y_∞ = ultimate yield (asymptote)
k = learning rate constant

Example:
Y_1 = 60%, Y_∞ = 95%, k = 0.1

Y_10 = 95% - (95% - 60%) × exp(-0.1 × 10)
Y_10 = 95% - 35% × 0.368
Y_10 = 82.1%
```

## Yield Prediction

### Yield Forecasting

**Based on Historical Data:**

```
Methods:
1. Trend analysis (linear, exponential)
2. Moving average
3. Time series (ARIMA)
4. Machine learning (if sufficient data)

Simple exponential smoothing:
F_t+1 = α × Y_t + (1 - α) × F_t

Where:
F_t+1 = forecast for next period
Y_t = actual yield in period t
F_t = forecast for period t
α = smoothing constant (0.1-0.3 typical)
```

**Example:**

```
Month | Actual | Forecast (α=0.2)
------|--------|------------------
Jan   | 82%    | 80% (given)
Feb   | 85%    | 80.4% = 0.2×82 + 0.8×80
Mar   | 84%    | 81.3% = 0.2×85 + 0.8×80.4
Apr   | 87%    | 81.8% = 0.2×84 + 0.8×81.3
May   | ?      | 82.8% = 0.2×87 + 0.8×81.8

Prediction: May yield ≈ 83%
```

### Die Per Wafer (DPW)

**Wafer Utilization:**

```
Gross DPW (rectangular approximation):
DPW = (Wafer_area - Edge_exclusion) / Die_area

More accurate (accounting for die positioning):
DPW = π × [(D/2 - E)² - (D/2 - E) × √2 × d] / A

Where:
D = wafer diameter
E = edge exclusion
d = die edge length
A = die area

For 200 mm wafer, 5×5 mm die, 3 mm exclusion:
Area available: π × 9.7² = 296 cm²
Die area: 0.25 cm²
Gross: 296 / 0.25 = 1184 die

Actual (accounting for packing): ~1050 die
Packing efficiency: 89%
```

**Good Die Per Wafer (GDPW):**

```
GDPW = DPW × Y_fab

Example:
DPW = 1050
Y_fab = 85%

GDPW = 1050 × 0.85 = 893 die

For cost calculation:
Wafer cost = $500
Die cost = $500 / 893 = $0.56 per die

If yield improves to 90%:
GDPW = 945 die
Die cost = $0.53 (6% reduction)
```

### Yield Sensitivity Analysis

**Impact of Variables:**

```
Sensitivity = ∂Y / ∂x

For Poisson model:
Y = exp(-D₀ × A)

∂Y/∂D₀ = -A × exp(-D₀ × A) = -A × Y
∂Y/∂A = -D₀ × exp(-D₀ × A) = -D₀ × Y

Relative sensitivity:
(∂Y/Y) / (∂D₀/D₀) = -D₀ × A

Example:
D₀ = 0.5, A = 0.25
Relative sensitivity = -0.5 × 0.25 = -0.125

Interpretation:
10% reduction in D₀ → 1.25% increase in Y
10% reduction in A → 1.25% increase in Y
```

## Yield Improvement

### Pareto Analysis

**80/20 Rule:**

```
Identify top loss mechanisms:

Loss Mode         | DPPM  | % of Total
-----------------|-------|------------
Particles        | 5000  | 50%
Lithography CD   | 2000  | 20%
Etch uniformity  | 1500  | 15%
Wire bond        | 800   | 8%
Other            | 700   | 7%
-----------------|-------|------------
Total            | 10000 | 100%

Focus on top 3 (85% of losses)
Potential: 85% reduction in defects

Action priority:
1. Particle reduction program
2. CD control improvement
3. Etch uniformity optimization
```

### Defect Reduction Strategies

**Systematic Approach:**

```
1. Measure baseline
   - Defect density by type
   - Pareto by source
   - Spatial distribution

2. Root cause analysis
   - Top defect types
   - 5-Why, fishbone
   - Equipment correlation

3. Implement countermeasures
   - Process optimization
   - Equipment PM
   - Handling improvements

4. Verify effectiveness
   - Monitor D₀ reduction
   - Track yield improvement
   - Cost-benefit analysis

5. Sustain improvements
   - SPC on critical parameters
   - Standard procedures
   - Training and audits
```

**Typical Improvement Trajectory:**

```
Starting point: Y = 60%, D₀ = 2.0

Quarter 1 (low-hanging fruit):
- Improve handling: D₀ → 1.5
- Y = exp(-1.5 × 0.25) = 69%
- 9% absolute improvement

Quarter 2 (process optimization):
- Chamber cleaning: D₀ → 1.0
- Y = exp(-1.0 × 0.25) = 78%
- 18% total improvement

Quarter 3 (advanced process):
- Recipe refinement: D₀ → 0.7
- Y = exp(-0.7 × 0.25) = 84%
- 24% total improvement

Quarter 4 (continuous improvement):
- Automated inspection: D₀ → 0.5
- Y = exp(-0.5 × 0.25) = 88%
- 28% total improvement

Diminishing returns observed
Cost-benefit analysis critical
```

### Cost-Yield Optimization

**Economic Model:**

```
Total cost per good die:

C_die = (C_wafer + C_process) / (DPW × Y)

Where:
C_wafer = wafer material cost
C_process = processing cost per wafer
DPW = die per wafer
Y = yield

Example:
C_wafer = $100
C_process = $400
DPW = 1000
Y = 80%

C_die = ($100 + $400) / (1000 × 0.8)
C_die = $500 / 800 = $0.625

If yield improvement project:
Investment: $50K
Expected Y: 80% → 85%

New cost: $500 / 850 = $0.588
Savings: $0.037 per die

Break-even: $50K / $0.037 = 1.35M die
At 10K die/month: ROI in 11.3 months
```

### Benchmark Comparison

**Industry Standards:**

| Product Type | Die Size | Typical Yield | Best-in-Class |
|--------------|----------|---------------|---------------|
| MEMS sensor (consumer) | 2-5 mm² | 85-90% | >95% |
| MEMS sensor (automotive) | 3-8 mm² | 90-95% | >98% |
| MEMS actuator | 5-15 mm² | 75-85% | >90% |
| Analog IC | 5-20 mm² | 85-92% | >95% |
| Digital logic | 100-500 mm² | 60-80% | >85% |

**Yield Maturity:**

```
Development phase:
- Year 0-1: 30-50% (learning)
- Year 1-2: 50-70% (optimization)
- Year 2-3: 70-85% (mature)
- Year 3+: 85-95% (best-in-class)

Factors:
- Process complexity
- Design maturity
- Equipment capability
- Fab experience
```

## Advanced Topics

### Inline Yield Prediction

**Early Warning:**

```
Predict final yield from:
- Inline inspection (defects)
- Parametric measurements
- Equipment sensors

Model:
Y_predicted = f(defect_count, CD, thickness, ...)

Machine learning approach:
1. Collect historical data
   - Inline measurements
   - Final yield results

2. Train model
   - Random forest
   - Neural network
   - Gradient boosting

3. Deploy for prediction
   - Real-time inline data
   - Predict final yield
   - Alert if low yield exp