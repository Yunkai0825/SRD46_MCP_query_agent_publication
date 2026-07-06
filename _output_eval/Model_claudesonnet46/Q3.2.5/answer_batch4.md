I now have everything needed for a thorough analysis. Let me compile the results.

---

## Zn²⁺–EDTA Stability Constants vs. Ionic Strength

### Raw Data from SRD-46 (β-def 812: Zn²⁺ + L⁴⁻ ⇌ ZnL²⁻, 25 °C)

| vlm_id | log K | I (mol/L) | √I | T (°C) |
|---|---|---|---|---|
| vlm_108710 | **18.00** | 0.00 | 0.000 | 25 |
| vlm_108707 | 16.50 | 0.10 | 0.316 | 25 |
| vlm_108708 | 15.70 | 0.50 | 0.707 | 25 |
| vlm_108709 | 15.70 | 1.00 | 1.000 | 25 |

*(ΔH = −19.7 kJ/mol, ΔS = +250.2 J/mol·K at I = 0.1 M are also recorded — vlm_108711/12)*

---

### Ionic-Strength Trend & Extrapolation to I = 0

The four log K values at 25 °C span I = 0 → 1 M. A linear regression of **log K vs. √I** through the three non-zero points gives:

| Point | √I | log K |
|---|---|---|
| I = 0.10 | 0.316 | 16.50 |
| I = 0.50 | 0.707 | 15.70 |
| I = 1.00 | 1.000 | 15.70 |

Fitting log K = a − b·√I through these three points:

- Slope b ≈ **−1.14** (log K drops ~1.1 units per unit of √I)
- Intercept (extrapolated I = 0): **log K⁰ ≈ 16.86**

| Method | log K at I = 0 |
|---|---|
| Linear extrapolation (√I → 0) | **≈ 16.86** |
| **SRD-46 measured value (vlm_108710)** | **18.00** |
| Difference | **~1.1 log units** |

---

### Comparison & Chemistry Insight

The extrapolated value (~16.9) is **~1.1 log units lower** than the directly measured I = 0 value of **log K = 18.00**. This discrepancy is physically meaningful and expected:

1. **Non-linearity at low I**: The Debye–Hückel / Davies equation predicts that activity corrections are *largest and most curved* near I = 0. A simple linear fit in √I underestimates the true intercept because the real log K vs. √I curve is concave — it rises steeply as I → 0 for a highly charged reaction (Zn²⁺ + L⁴⁻ → ZnL²⁻, net charge change Δz² = 4² + 2² − 2² = 16).

2. **Large charge product**: The Debye–Hückel term scales as Δz² = |z_M·z_L| = 2×4 = 8, making Zn²⁺–EDTA one of the most ionic-strength-sensitive systems in the database. The ~2.3 log-unit drop from I = 0 to I = 1 M is entirely consistent with theory.

3. **The SRD-46 I = 0 value (log K = 18.00)** is backed by **34 independent literature citations** spanning 1949–1990 (Schwarzenbach, Anderegg, Martell, and many others), making it one of the most thoroughly cross-validated constants in the database. It is the recommended thermodynamic stability constant for Zn²⁺–EDTA.

> **Bottom line**: The thermodynamic stability constant for Zn²⁺–EDTA is **log K° = 18.00** at 25 °C, I = 0 (SRD-46, vlm_108710, 34 citations). A naïve linear extrapolation from the I = 0.1–1.0 M data yields ~16.9, underestimating by ~1.1 units due to the strong curvature of activity corrections for this highly charged system. For rigorous extrapolation, a SIT or extended Debye–Hückel model is required.

*Source: NIST SRD-46, metal_208 (Zn²⁺), ligand_6277 (EDTA), beta_def_812.*

---