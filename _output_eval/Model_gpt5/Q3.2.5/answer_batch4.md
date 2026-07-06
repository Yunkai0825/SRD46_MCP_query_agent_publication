Here’s what SRD‑46 reports for Zn2+ + EDTA ⇌ ZnEDTA (β definition: beta_def_812 = [ML]/[M][L]) at 25 °C, with ionic strength I noted. I used the non‑zero I points to extrapolate log β to I → 0 and then compared to the database’s I = 0 entry.

Data used for trend (25 °C)

| vlm_id   | I (mol L⁻¹) | √I     | log β |
|----------|--------------|--------|-------|
| vlm_108707 | 0.10         | 0.3162 | 16.5  |
| vlm_108708 | 0.50         | 0.7071 | 15.7  |
| vlm_108709 | 1.00         | 1.0000 | 15.7  |

Zero‑ionic‑strength entry (25 °C)

| vlm_id   | I (mol L⁻¹) | log β |
|----------|--------------|-------|
| vlm_108710 | 0            | 18.0  |

Extrapolation method and result
- Model: linear log β vs √I (Debye–Hückel style over moderate I) using the three non‑zero points above.
- Fit (least squares): log β(I) ≈ 16.79 − 1.22·√I.
- Extrapolated log β at I → 0: 16.79.

Comparison to SRD‑46 I = 0 value
- Extrapolated I → 0: 16.79
- Database I = 0 (vlm_108710): 18.0
- Difference: ≈ 1.2 log units (extrapolated is lower).

Notes and caveats
- The fit mixes points at different ionic strengths without electrolyte identifiers (not shown in these rows), and specific ion effects can change the slope; a fit restricted to the lower‑I pair (0.1 and 0.5 M) gives a slightly higher intercept (~17.1), but still below 18.0.
- Linear log β vs √I is a simple approximation; strong complexes like ZnEDTA2− show pronounced activity corrections, so I → 0 thermodynamic β can exceed conditional β at finite I by ~1 log unit or more.

Source: NIST SRD‑46 (vlm_108707, vlm_108708, vlm_108709, vlm_108710; beta_def_812).

---