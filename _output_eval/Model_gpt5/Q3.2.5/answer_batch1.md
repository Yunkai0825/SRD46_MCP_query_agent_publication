Below are the Zn2+–EDTA overall formation constants (beta_def_812: [M] + [L] ⇌ [ML]) near 25 °C from SRD‑46, listed versus ionic strength. I used the finite-I points to extrapolate to I → 0 and then compared to the database’s explicit I = 0 value.

Data (25 °C, aqueous; same reaction definition beta_def_812)
| vlm_id    | I (mol·L⁻¹) | sqrt(I) | log β |
|-----------|--------------|---------|-------|
| vlm_108707 | 0.10         | 0.316   | 16.5  |
| vlm_108708 | 0.50         | 0.707   | 15.7  |
| vlm_108709 | 1.00         | 1.000   | 15.7  |
| vlm_108710 | 0.00         | 0.000   | 18.0  |


Extrapolation (using only low-I points 0.10 and 0.50 M; linear in √I, “Davies-style”):
- Fit: log β(I) ≈ a + b·√I with b = −2.05 and a = 17.15
- Extrapolated thermodynamic constant at I → 0: log β° ≈ 17.15

Comparison to SRD‑46 I = 0 datum
| Method/Source             | log β° | Notes |
|---------------------------|--------|-------|
| Extrapolated (√I fit, 0.10–0.50 M) | ~17.15 | Based on two low-I points; 25 °C |
| Database value (vlm_108710)        | 18.0   | Explicit I = 0 measurement at 25 °C |

Interpretation and caveats
- The simple √I extrapolation from moderate ionic strengths underestimates the SRD‑46 thermodynamic value by ~0.85 log units. This is common when (a) medium-specific ion–interaction terms (SIT) are not accounted for, (b) data do not extend to very low ionic strength, or (c) points span different electrolyte media. With more low‑I data in a single medium or a SIT/Davies parameterization specific to the electrolyte, the intercept typically moves closer to the reported I = 0 value.
- The 1.0 M point shows little change from 0.5 M (both 15.7), suggesting curvature or medium effects; it was excluded from the low‑I fit.

Source: NIST SRD‑46 (ligand_6277 EDTA; metal_208 Zn2+; beta_def_812; vlm_108707, vlm_108708, vlm_108709, vlm_108710).

---