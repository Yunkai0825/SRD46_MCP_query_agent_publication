Excellent — I have all the data I need. Let me now perform the extrapolation and deliver the final answer.

---

## Zn²⁺–EDTA Stability Constants: Ionic-Strength Trend & Extrapolation to I = 0

**Reaction:** Zn²⁺ + EDTA⁴⁻ ⇌ [ZnEDTA]²⁻ &nbsp;(`beta_def_812`, all at **25 °C**)

### Raw SRD-46 Data

| vlm_id | log K | I (mol/L) | √I |
|---|---|---|---|
| vlm_108707 | 16.50 | 0.10 | 0.316 |
| vlm_108708 | 15.70 | 0.50 | 0.707 |
| vlm_108709 | 15.70 | 1.00 | 1.000 |
| **vlm_108710** | **18.00** | **0.00** | **0.000** |

*(vlm_108711 and vlm_108712 are ΔH and ΔS entries at I = 0.1 M, not log K — excluded from the fit.)*

---

### Linear Extrapolation: log K vs √I

Using the three finite-ionic-strength log K points (I = 0.1, 0.5, 1.0 M), a linear regression of log K on √I gives:

| Point | √I | log K |
|---|---|---|
| 1 | 0.316 | 16.50 |
| 2 | 0.707 | 15.70 |
| 3 | 1.000 | 15.70 |

**Slope** (Δ log K / Δ√I):

Using points 1 and 3:  
Δ log K = 15.70 − 16.50 = −0.80  
Δ√I = 1.000 − 0.316 = 0.684  
**slope ≈ −1.17 per (mol/L)^½**

**Intercept** (extrapolated log K at I = 0):  
log K(I→0) = 16.50 − (−1.17)(0.316) = 16.50 + 0.37 ≈ **16.87**

A simple least-squares fit of all three points gives a consistent result of approximately **log K(I→0) ≈ 16.8–17.0**.

---

### Comparison with the SRD-46 Thermodynamic Value

| Source | log K | I (mol/L) | T (°C) | vlm_id |
|---|---|---|---|---|
| Extrapolated (linear fit, √I) | **≈ 16.9** | 0 (calc.) | 25 | — |
| SRD-46 direct measurement | **18.00** | 0 | 25 | vlm_108710 |
| **Difference** | **≈ +1.1 log units** | — | — | — |

---

### Chemistry Insight

The extrapolated value (~16.9) falls **~1.1 log units below** the directly measured thermodynamic constant (log K = 18.00 at I = 0). This discrepancy is chemically meaningful and expected:

1. **Non-linearity at low I:** The Davies or extended Debye–Hückel equations predict that activity coefficients for highly charged species (Zn²⁺ is +2, EDTA⁴⁻ is −4, product is −2) change most steeply near I → 0. A simple linear fit in √I underestimates the upward curvature as I → 0, so the true thermodynamic constant is higher than the linear extrapolation suggests.

2. **Charge product effect:** The reaction involves a net charge change of Δz² = z²(Zn²⁺) + z²(EDTA⁴⁻) − z²(ZnEDTA²⁻) = 4 + 16 − 4 = **+16**, which is large. The Debye–Hückel slope for log K vs √I scales with this Δz², making the ionic-strength dependence steep and non-linear — exactly what we observe.

3. **Practical implication:** The commonly cited "log K = 16.5" (at I = 0.1 M, e.g. KNO₃ background) is the value most relevant to physiological or environmental conditions, while the thermodynamic log K = 18.0 reflects the true intrinsic metal–ligand affinity in the absence of ionic screening.

> **Source:** NIST SRD-46 (Standard Reference Database 46), `beta_def_812`, `metal_208` (Zn²⁺), `ligand_6277` (EDTA), all at 25 °C.

---