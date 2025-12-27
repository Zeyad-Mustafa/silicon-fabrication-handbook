# Statistical Process Control (SPC)

## Table of Contents
- [Introduction](#introduction)
- [Control Charts](#control-charts)
- [Process Capability](#process-capability)
- [Sampling Plans](#sampling-plans)
- [SPC Implementation](#spc-implementation)
- [Advanced Techniques](#advanced-techniques)
- [References](#references)

## Introduction

Statistical Process Control (SPC) uses statistical methods to monitor and control manufacturing processes, ensuring consistent quality and rapid detection of problems.

### SPC Objectives

```
Primary goals:
1. Detect process shifts early
2. Reduce variation
3. Improve yield
4. Prevent defects (not detect)
5. Enable data-driven decisions

Benefits:
- Early problem detection (hours vs days)
- Reduced scrap and rework
- Consistent product quality
- Lower cost of quality
- Improved customer satisfaction
```

### Key Concepts

**Common Cause vs Special Cause Variation:**

| Type | Description | Magnitude | Action |
|------|-------------|-----------|--------|
| Common cause | Natural process variation | Small, random | No action (stable) |
| | Inherent to process | Predictable | Process improvement |
| Special cause | Assignable causes | Large, unusual | Investigate immediately |
| | Tool drift, contamination | Not predictable | Correct root cause |

**Process States:**

```
In Control:
- Only common cause variation
- Predictable within limits
- Stable over time
- Continue monitoring

Out of Control:
- Special cause variation present
- Points beyond control limits
- Trends or patterns
- Immediate investigation required
```

## Control Charts

### X-bar and R Charts

**X-bar Chart (Average):**

Monitors process centering.

```
Control limits:
UCL = X̄̄ + A₂ × R̄
Center Line = X̄̄
LCL = X̄̄ - A₂ × R̄

Where:
X̄̄ = grand average (average of subgroup averages)
R̄ = average range
A₂ = constant based on subgroup size (n)

For n=5: A₂ = 0.577
```

**R Chart (Range):**

Monitors process variation.

```
Control limits:
UCL = D₄ × R̄
Center Line = R̄
LCL = D₃ × R̄

For n=5: D₃ = 0, D₄ = 2.114
```

**Example Calculation:**

```
Data: Resist thickness (nm)
Subgroup size: n = 5 wafers
Number of subgroups: k = 25

Sample data (first 5 subgroups):
Subgroup | Measurements (nm)           | X̄    | R
---------|----------------------------|------|----
1        | 502, 498, 505, 497, 503   | 501  | 8
2        | 499, 501, 497, 502, 496   | 499  | 6
3        | 503, 500, 498, 501, 499   | 500.2| 5
4        | 495, 502, 498, 500, 497   | 498.4| 7
5        | 501, 499, 503, 497, 500   | 500  | 6

Calculate:
X̄̄ = (501 + 499 + 500.2 + 498.4 + 500 + ...) / 25 = 500.0 nm
R̄ = (8 + 6 + 5 + 7 + 6 + ...) / 25 = 6.5 nm

X-bar chart:
UCL = 500.0 + 0.577 × 6.5 = 503.75 nm
CL = 500.0 nm
LCL = 500.0 - 0.577 × 6.5 = 496.25 nm

R chart:
UCL = 2.114 × 6.5 = 13.74 nm
CL = 6.5 nm
LCL = 0 × 6.5 = 0 nm (n=5, LCL is zero)
```

### Individuals and Moving Range (I-MR) Charts

**When to Use:**

```
Use I-MR when:
- Subgroup size = 1 (single measurement)
- Slow production rate
- Expensive or destructive testing
- Homogeneous batches

Common applications:
- Chemical concentration
- Wafer uniformity
- Daily averages
- Critical dimensions
```

**Control Limits:**

```
Individuals (I) Chart:
UCL = X̄ + 2.66 × MR̄
Center Line = X̄
LCL = X̄ - 2.66 × MR̄

Moving Range (MR) Chart:
UCL = 3.267 × MR̄
Center Line = MR̄
LCL = 0 (typically)

Where:
X̄ = average of individual values
MR̄ = average moving range
MR = |Xᵢ - Xᵢ₋₁|
```

**Example:**

```
Etch rate (nm/min) - daily average:
Day | Etch Rate | Moving Range
----|-----------|-------------
1   | 105.2     | -
2   | 106.1     | 0.9
3   | 104.8     | 1.3
4   | 105.5     | 0.7
5   | 106.3     | 0.8
6   | 105.0     | 1.3
7   | 105.8     | 0.8
8   | 104.9     | 0.9

X̄ = 105.45 nm/min
MR̄ = 0.96 nm/min

I Chart:
UCL = 105.45 + 2.66 × 0.96 = 108.00
LCL = 105.45 - 2.66 × 0.96 = 102.90

MR Chart:
UCL = 3.267 × 0.96 = 3.14
```

### Control Chart Rules (Western Electric Rules)

**Out-of-Control Conditions:**

```
Zone definitions:
Zone A: ±2σ to ±3σ (control limits)
Zone B: ±1σ to ±2σ
Zone C: 0 to ±1σ (center)

Rule 1: Single point beyond 3σ (Zone A+)
→ Special cause, investigate immediately

Rule 2: 2 out of 3 consecutive points in Zone A or beyond
→ Process shift

Rule 3: 4 out of 5 consecutive points in Zone B or beyond
→ Sustained shift

Rule 4: 8 consecutive points on one side of center
→ Process shift or trend

Rule 5: 6 consecutive points increasing or decreasing (trend)
→ Tool wear, drift

Rule 6: 15 consecutive points in Zone C
→ Reduced variation (sampling issue?)

Rule 7: 14 consecutive points alternating up/down
→ Oscillation (temperature cycling?)

Rule 8: 8 consecutive points outside Zone C
→ Mixture pattern (two populations?)
```

**Example - Process Shift:**

```
Subgroup | X̄    | Status
---------|------|--------
15       | 500.5| OK (Zone C)
16       | 501.2| OK (Zone C)
17       | 502.8| Warning (Zone B)
18       | 503.1| WARNING - Rule 2
19       | 502.5| (2 of 3 in Zone B+)

Action: Investigate process
Finding: Chamber temperature +5°C
Cause: Cooling system degradation
Fix: Service cooling system
```

### p-Chart (Proportion Defective)

**For Attribute Data:**

```
Use when:
- Count defectives (pass/fail)
- Variable sample size acceptable
- Binomial distribution

Control limits:
UCL = p̄ + 3√(p̄(1-p̄)/n)
Center Line = p̄
LCL = p̄ - 3√(p̄(1-p̄)/n)

Where:
p̄ = average proportion defective
n = sample size

If LCL < 0, set LCL = 0
```

**Example:**

```
Die yield monitoring:
Sample size: n = 100 die per wafer
25 wafers monitored

Wafer | Defective | p
------|-----------|------
1     | 5         | 0.05
2     | 7         | 0.07
3     | 4         | 0.04
...
25    | 6         | 0.06

p̄ = 0.058 (5.8% defective)

UCL = 0.058 + 3√(0.058 × 0.942/100)
    = 0.058 + 3 × 0.0234
    = 0.128 (12.8%)

LCL = 0.058 - 0.070 = -0.012 → 0 (set to zero)

Action limit: >12.8% defective → investigate
```

### c-Chart (Count of Defects)

**For Defect Counts:**

```
Use when:
- Count defects per unit
- Constant sample size
- Poisson distribution

Examples:
- Particles per wafer
- Scratches per die
- Solder defects per board

Control limits:
UCL = c̄ + 3√c̄
Center Line = c̄
LCL = c̄ - 3√c̄

Where:
c̄ = average count per unit
```

**Example:**

```
Particles per wafer (200 mm):
c̄ = 12 particles/wafer

UCL = 12 + 3√12 = 12 + 10.4 = 22.4
LCL = 12 - 10.4 = 1.6

If wafer has >22 particles → investigate
Typical causes:
- Chamber contamination
- Filter degradation
- Process upset
```

## Process Capability

### Capability Indices

**Cp (Process Capability):**

```
Cp = (USL - LSL) / (6σ)

Where:
USL = Upper Specification Limit
LSL = Lower Specification Limit
σ = process standard deviation

Interpretation:
Cp < 1.0: Process not capable (defects expected)
Cp = 1.0: Process just capable (99.73%)
Cp = 1.33: Process capable (63 ppm)
Cp = 1.67: Good process (0.6 ppm)
Cp = 2.0: Excellent process (0.002 ppm)

Note: Assumes process centered
```

**Cpk (Process Capability with Centering):**

```
Cpk = min[(USL - μ)/(3σ), (μ - LSL)/(3σ)]

Where:
μ = process mean

Cpk accounts for process centering
Cpk ≤ Cp always (equality when centered)

Target: Cpk ≥ 1.33 (4σ process)
        Cpk ≥ 1.67 (5σ process)
        Cpk ≥ 2.0 (6σ process)
```

**Example Calculation:**

```
Resist thickness specification:
LSL = 490 nm
USL = 510 nm
Target = 500 nm

Measured data (100 wafers):
μ = 502 nm (mean)
σ = 2.5 nm (std dev)

Cp = (510 - 490) / (6 × 2.5)
   = 20 / 15
   = 1.33

Cpk = min[(510 - 502)/(3 × 2.5), (502 - 490)/(3 × 2.5)]
    = min[8/7.5, 12/7.5]
    = min[1.07, 1.60]
    = 1.07

Interpretation:
- Cp = 1.33: Process variation acceptable
- Cpk = 1.07: Process off-center (high side)
- Action: Center process to 500 nm
- Potential Cpk if centered: 1.33
```

**Defect Rate from Cpk:**

```
Cpk | Sigma Level | DPMO (Defects Per Million)
----|-------------|---------------------------
0.33| 1σ          | 317,300
0.67| 2σ          | 45,500
1.00| 3σ          | 2,700
1.33| 4σ          | 63
1.67| 5σ          | 0.6
2.00| 6σ          | 0.002

Example:
Current Cpk = 1.07 → ~1,350 DPPM
Target Cpk = 1.33 → 63 DPPM
Improvement: 20× reduction in defects
```

### Pp and Ppk (Process Performance)

**Difference from Cp/Cpk:**

```
Cp/Cpk: Short-term capability
- Based on within-subgroup variation
- Estimates inherent process capability
- What process could achieve

Pp/Ppk: Long-term performance
- Based on total variation (all data)
- Includes shifts and drifts
- What process actually achieves

Formulas:
Pp = (USL - LSL) / (6s)
Ppk = min[(USL - X̄)/(3s), (X̄ - LSL)/(3s)]

Where:
s = overall standard deviation
X̄ = overall mean

Relationship:
Pp ≤ Cp (usually)
Ppk ≤ Cpk (usually)

Ratio:
Pp/Cp = measure of process stability
<1: Process drifts over time
=1: Process very stable
```

## Sampling Plans

### Acceptance Sampling

**MIL-STD-105E (ANSI/ASQ Z1.4):**

```
Definitions:
- Lot size (N): Number of units in batch
- Sample size (n): Number inspected
- Acceptance number (c): Maximum defects allowed
- AQL: Acceptable Quality Level (%)

Example:
Lot size: 1000 wafers
Inspection level: II (normal)
AQL: 1.0%

From tables:
Sample size: n = 80 wafers
Acceptance number: c = 2

Decision:
≤2 defects found → Accept lot
≥3 defects found → Reject lot
```

**Operating Characteristic (OC) Curve:**

```
Shows probability of accepting lot vs actual defect rate

For n=80, c=2:
True Defect Rate | P(Accept)
-----------------|----------
0.5%            | 95%
1.0% (AQL)      | 90%
2.0%            | 70%
4.0%            | 35%
6.0%            | 15%

Key points:
- Producer's risk (α): Reject good lot (5-10%)
- Consumer's risk (β): Accept bad lot (5-10%)
- Balance between cost and protection
```

### Sequential Sampling

**Reduced Testing:**

```
Instead of fixed sample size:
1. Take small initial sample
2. Make decision: Accept, Reject, or Continue
3. If Continue, take more samples
4. Repeat until decision

Advantages:
- Average sample size smaller (30-50% reduction)
- Quicker decisions for very good or very bad lots

Disadvantages:
- Variable inspection time
- More complex administration
```

## SPC Implementation

### Implementation Steps

**Phase 1: Planning (1-2 months):**

```
1. Identify critical parameters
   - Impact on yield
   - Impact on reliability
   - Customer specifications
   - High variation processes

2. Select control chart types
   - Variable data: X-bar/R, I-MR
   - Attribute data: p-chart, c-chart

3. Determine sampling strategy
   - Frequency (hourly, per lot, daily)
   - Sample size (statistical power)
   - Measurement method

4. Establish data collection
   - Automated (preferred)
   - Manual forms
   - Database design

5. Set up charting system
   - Software selection
   - Chart layout and distribution
   - Alert mechanisms
```

**Phase 2: Baseline (1-2 months):**

```
6. Collect baseline data
   - Minimum 20-25 subgroups
   - Process running normally
   - No adjustments

7. Calculate control limits
   - Use baseline data
   - Apply formulas
   - Verify stability

8. Train personnel
   - Chart interpretation
   - Response procedures
   - Data collection

9. Document procedures
   - SOPs for charting
   - Response plans
   - Escalation paths
```

**Phase 3: Operation (Ongoing):**

```
10. Monitor and respond
    - Real-time charting
    - Out-of-control investigation
    - Root cause analysis

11. Review and update
    - Recalculate limits (quarterly)
    - Modify sampling if needed
    - Continuous improvement

12. Measure effectiveness
    - Yield improvement
    - Defect reduction
    - Response time
```

### Critical Parameters for SPC

**MEMS Fabrication:**

| Process | Parameter | Chart Type | Frequency |
|---------|-----------|------------|-----------|
| Lithography | CD (Critical Dimension) | X-bar/R | Per lot |
| | Overlay accuracy | X-bar/R | Per lot |
| Deposition | Thickness | X-bar/R | Per run |
| | Uniformity | I-MR | Per run |
| Etch | Etch rate | X-bar/R | Per lot |
| | Selectivity | I-MR | Per lot |
| Implant | Dose | X-bar/R | Per run |
| | Sheet resistance | X-bar/R | Per lot |
| CMP | Post-CMP thickness | X-bar/R | Per lot |
| | Uniformity | I-MR | Per lot |
| Metrology | Defect count | c-chart | Per wafer |
| Final test | Yield | p-chart | Per lot |

### Data Collection Methods

**Automated vs Manual:**

```
Automated (preferred):
- Equipment sensors
- In-line metrology
- Test data download
- Real-time charting

Advantages:
- No transcription errors
- Real-time response
- 100% data capture
- Less labor

Disadvantages:
- Higher setup cost
- System maintenance
- IT infrastructure

Manual:
- Paper forms
- Periodic measurements
- Manual charting or entry

Use when:
- Low volume
- Lab measurements
- Pilot production
- Cost-sensitive
```

### Response Procedures

**Out-of-Control Response:**

```
Immediate actions (within 1 hour):
1. Stop process (if critical parameter)
2. Notify supervisor/engineer
3. Quarantine affected units
4. Document event

Investigation (within 8 hours):
5. Review recent changes
6. Check equipment status
7. Verify measurement system
8. Inspect materials

Root cause (within 24 hours):
9. Perform detailed analysis
10. Identify root cause
11. Implement corrective action
12. Verify effectiveness

Follow-up:
13. Update control limits if needed
14. Modify process if needed
15. Prevent recurrence
16. Document in database
```

## Advanced Techniques

### Multivariate SPC

**Monitoring Multiple Parameters:**

```
Traditional SPC: One parameter per chart
Problem: Many parameters, difficult to monitor all

Multivariate methods:
1. Hotelling's T² statistic
2. Principal Component Analysis (PCA)
3. Multivariate EWMA

Advantages:
- Single chart for multiple parameters
- Detects interactions
- More sensitive to shifts

Applications:
- Process with 10+ critical parameters
- Correlated variables
- Recipe optimization
```

**T² Control Chart:**

```
For p variables (parameters):

T² = n(X̄ - μ)' Σ⁻¹ (X̄ - μ)

Where:
X̄ = vector of sample means
μ = vector of target values
Σ = covariance matrix
n = sample size

UCL = χ²α,p (chi-squared distribution)

Example:
Monitor 5 lithography parameters simultaneously
If T² > UCL → at least one parameter out of spec
Determine which using contribution plot
```

### EWMA (Exponentially Weighted Moving Average)

**For Small Shifts:**

```
More sensitive to small sustained shifts than Shewhart charts

EWMA:
Zᵢ = λXᵢ + (1-λ)Zᵢ₋₁

Where:
λ = smoothing constant (0 < λ ≤ 1)
Typical λ = 0.2 (weight recent data more)

Control limits:
UCL = μ + Lσ√(λ/(2-λ) × [1-(1-λ)²ⁱ])
LCL = μ - Lσ√(λ/(2-λ) × [1-(1-λ)²ⁱ])

Typically L = 3

Detects:
- 0.5σ shift in ~8 samples
- vs Shewhart: ~14 samples
```

### CUSUM (Cumulative Sum)

**For Detecting Small Shifts:**

```
Accumulates deviations from target

Cᵢ⁺ = max[0, Xᵢ - (μ + K) + Cᵢ₋₁⁺]
Cᵢ⁻ = max[0, (μ - K) - Xᵢ + Cᵢ₋₁⁻]

Where:
K = reference value (typically 0.5σ)
H = decision interval (typically 5σ)

Out of control:
- If Cᵢ⁺ > H (upward shift)
- If Cᵢ⁻ > H (downward shift)

Advantages:
- Detects small shifts quickly
- Visual trend indication
- Good for continuous processes
```

### SPC Software

**Commercial Solutions:**

| Software | Capabilities | Cost | Best For |
|----------|--------------|------|----------|
| Minitab | Statistical analysis + SPC | $3K-5K | General purpose |
| JMP (SAS) | Advanced analytics + SPC | $5K-10K | Complex analysis |
| InfinityQS | Real-time SPC | $10K-50K | Manufacturing |
| Enact (InfinityQS) | Cloud-based SPC | $5K-20K | Multiple sites |
| StatSoft | Full statistical suite | $5K-15K | Engineering |

**Open Source:**

```
R packages:
- qcc: Quality control charts
- spc: Statistical process control
- MSQC: Multivariate SPC

Python packages:
- scipy.stats: Statistical functions
- matplotlib: Charting
- pandas: Data manipulation

Cost: Free
Flexibility: High
Support: Community
Learning curve: Steeper
```

## Case Study: SPC Implementation

### Etch Rate Control

**Problem:**

```
Process: DRIE silicon etch
Issue: High etch rate variation (±15%)
Impact: Yield loss (10%), rework
Target: Reduce variation to ±5%
```

**Implementation:**

```
Week 1-2: Planning
- Identified etch rate as critical
- Selected X-bar/R chart (n=3 per run)
- Sampling: Every run, 3 wafers
- Measurement: Profilometer

Week 3-6: Baseline
- Collected 25 runs (75 wafers)
- Mean: 3.2 μm/min
- Std dev: 0.22 μm/min
- Calculated control limits

Week 7+: Operation
- Real-time charting
- Out-of-control investigations
```

**Results:**

```
Month 1-2 (before SPC):
- Etch rate: 3.2 ± 0.48 μm/min (±15%)
- Cpk: 0.89 (not capable)
- Yield: 90%
- Investigations: Reactive (after failures)

Month 6 (after SPC):
- Etch rate: 3.2 ± 0.16 μm/min (±5%)
- Cpk: 1.67 (good)
- Yield: 98%
- Investigations: Proactive (prevent failures)

Improvements:
- 3× reduction in variation
- 8% yield improvement
- 70% reduction in rework
- Early problem detection (tool drift caught in 2 days vs 2 weeks)

ROI:
- Investment: $20K (software, training)
- Annual savings: $150K (yield improvement)
- Payback: 2 months
```

## Best Practices

### SPC Guidelines

```
✓ Start with critical parameters (not everything)
✓ Use appropriate chart type for data
✓ Collect sufficient baseline data (≥20 subgroups)
✓ Train all personnel thoroughly
✓ Automate data collection when possible
✓ Respond to out-of-control quickly (<1 hour)
✓ Perform root cause analysis (not just adjust)
✓ Review and update limits periodically
✓ Measure and communicate improvements
✓ Integrate with quality system (ISO, etc.)
```

### Common Mistakes ✗

```
✗ Too many charts (overwhelming)
✗ Wrong chart type for data
✗ Insufficient baseline data (<20)
✗ Ignoring out-of-control signals
✗ Adjusting process without investigation
✗ Not updating control limits
✗ Manual charting when automation possible
✗ No response procedures documented
✗ Treating SPC as one-time project
✗ Not engaging operators in process
```

### Success Factors

```
Critical elements:
1. Management commitment
   - Resources allocated
   - Support for changes
   - Long-term focus

2. Training
   - Statistical concepts
   - Chart interpretation
   - Response procedures

3. Integration
   - Part of daily workflow
   - Linked to manufacturing execution system
   - Automated where possible

4. Culture
   - Proactive vs reactive
   - Data-driven decisions
   - Continuous improvement mindset

5. Sustainability
   - Ongoing reviews
   - Regular updates
   - Recognition and rewards
```

## References

1. Montgomery, D. C. (2019). *Introduction to Statistical Quality Control* (8th ed.). Wiley.

2. Wheeler, D. J., & Chambers, D. S. (1992). *Understanding Statistical Process Control* (2nd ed.). SPC Press.

3. Oakland, J. S. (2007). *Statistical Process Control* (6th ed.). Butterworth-Heinemann.

4. American Society for Quality (ASQ). (2020). *Quality Control and Improvement Standards*.

5. SEMI E10. (2019). *Specification for Definition and Measurement of Equipment Reliability, Availability, and Maintainability (RAM)*.

---

**Document Information:**
- **Created:** December 23, 2025
- **Version:** 1.0
- **Status:** Complete
- **Part of:** Silicon Fabrication Handbook
- **Next Chapter:** [Yield Modeling](yield-modeling.md)
- **Previous Chapter:** [Failure Analysis](failure-analysis.md)

**License:** CC BY 4.0 - Free to use with attribution

---

*For questions, corrections, or contributions, please visit:*
https://github.com/Zeyad-Mustafa/silicon-fabrication-handbook