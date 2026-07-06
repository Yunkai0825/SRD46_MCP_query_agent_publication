Here is what SRD‑46 reports for Zn2+ + EDTA4− ⇌ ZnEDTA2− (β definition: [ML]/[M][L], beta_def_812) at 25 °C, along with an I→0 extrapolation.

Data (25 °C)
| I (mol/L) | √I   | f(I)=√I/(1+√I) | log β (ML) | vlm_id     |
|-----------|------|-----------------|------------|------------|
| 0.00      | 0.000| 0.000           | 18.0       | vlm_108710 |
| 0.10      | 0.316| 0.240           | 16.5       | vlm_108707 |
| 0.50      | 0.707| 0.414           | 15.7       | vlm_108708 |
| 1.00      | 1.000| 0.500           | 15.7       | vlm_108709 |

Extrapolation to I = 0 (25 °C)
- Model used (Davies‑style, per plan): log β(I) ≈ log β° + a·[√I/(1+√I)] + b·I, fit to the finite‑I points (I = 0.1, 0.5, 1.0 M).
- Fit result:
  - log β° (I→0) = 18.19
  - a = −7.58
  - b = +1.30

Comparison vs database I = 0 entry
| Quantity | Value | Notes |
|----------|-------|-------|
| Extrapolated log β° (I→0) | 18.19 | Davies‑style fit to I = 0.1–1.0 M data |
| SRD‑46 log β at I = 0 | 18.0 (vlm_108710) | Same β definition (ML), 25 °C |
| Difference | +0.19 | Extrapolation slightly higher |

Notes and interpretation
- The measured log β decreases with ionic strength, as expected from activity effects; the Davies‑style fit brings the I→0 estimate into close agreement with the database’s I = 0 value (within ~0.2 log units).
- A naïve linear fit vs √I (low‑I approximation) to the same points would underpredict (log β° ≈ 16.8), illustrating why a Davies‑type form better captures curvature at higher I.
- Medium details for these points are not shown in the summary here; differences in supporting electrolyte can introduce small offsets. Nonetheless, the extrapolated thermodynamic constant is consistent with the SRD‑46 I = 0 entry.

Source: NIST Standard Reference Database 46 (SRD‑46). Records: beta_def_812; vlm_108707, vlm_108708, vlm_108709, vlm_108710.

---