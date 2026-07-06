Below are the SRD‑46 measurements for the overall formation of the 1:1 Zn–EDTA complex (β11; β_def_812: [ML]/[M][L]) at 25 °C, spanning several ionic strengths, along with a simple Debye–Hückel–type extrapolation to I = 0.

Data used (25 °C, β_def_812):
| vlm_id | I (mol L⁻¹) | √I | logβ11 |
|--------|--------------|----|--------|
| vlm_108707 | 0.10 | 0.316 | 16.5 |
| vlm_108708 | 0.50 | 0.707 | 15.7 |
| vlm_108709 | 1.00 | 1.000 | 15.7 |
| vlm_108710 | 0.00 | 0.000 | 18.0 |

Extrapolation (from finite-I points only, I = 0.10, 0.50, 1.00):
- Model: logβ11 = a + b·√I
- Fit parameters: a = 16.79, b = −1.21
- Intercept uncertainty (SE[a], from linear fit): ±0.42
- Goodness of fit: R² ≈ 0.82

Comparison to SRD‑46 I = 0 measurement:
| Quantity | Value |
|----------|-------|
| Extrapolated logβ°11 (I → 0) | 16.79 ± 0.42 |
| Measured logβ11 at I = 0 (vlm_108710) | 18.00 |
| Difference (measured − extrapolated) | ≈ +1.21 |

Notes and interpretation
- The extrapolated I → 0 value (≈16.8) is lower than the SRD‑46 I = 0 measurement (18.0) by ~1.2 log units. This discrepancy is plausible if the finite‑I points are in media whose activity corrections differ from an idealized zero‑ionic‑strength reference; mixing media also biases simple linear extrapolation. The flattening between I = 0.5 and 1.0 (15.7 → 15.7) further suggests nonlinearity at higher ionic strength.
- A medium‑consistent SIT/Debye–Hückel treatment often yields a higher intercept; with only three finite‑I points and unknown medium, the simple √I fit underestimates logβ°11. For a tighter comparison, one would filter to a single electrolyte and inspect the vlm cards to confirm identical media and protocols.

Source: NIST SRD‑46 (ligand_id = ligand_6277, metal_id = metal_208; β_def_812; vlm_108707, vlm_108708, vlm_108709, vlm_108710).

---