| Quantity | Value | Conditions | Source (SRD‑46 tool) |
|---|---:|---|---|
| Oxalic acid pKa (H2L ⇌ HL + H+) | −1.2 | 25 °C, I = 0.1 M, water | search_pka_values (vlm_151532) |
| Oxalic acid pKa (HL ⇌ L2− + H+) | 3.8 | 25 °C, I = 0.1 M, water | search_pka_values (vlm_151494) |
| Ca2+ + C2O4²− ⇌ CaC2O4(aq), log β1 | ≈ 3.30 | 25 °C, low I | build_system_catalog (beta_def_812) |
| Ca2+ + HC2O4− ⇌ CaHC2O4+, log β1 | ≈ 1.6 | 25 °C, low I | build_system_catalog |
| CaC2O4·H2O(s) ⇌ Ca2+ + C2O4²−, pKsp (COM) | ≈ 8.6 | 25 °C, low I | build_system_catalog (beta_def_327) |
| CaC2O4·2H2O(s) ⇌ Ca2+ + C2O4²−, pKsp (COT) | ≈ 7.9 | 25 °C, low I | build_system_catalog (beta_def_307) |

Approximate pH for onset of precipitation
- Oxalate is largely present as L2− (C2O4²−) once pH exceeds pKa2. Using the SRD‑46 pKa2 ≈ 3.8, the L2− fraction rises steeply above pH ~4.  
- With millimolar Ca and total oxalate, the ionic product [Ca2+][C2O4²−] will exceed the COM Ksp (pKsp ≈ 8.6, Ksp ≈ 2.5×10^−9) soon after L2− becomes a major species. Accounting for some CaC2O4(aq) complexation (log β1 ≈ 3.3) that buffers free ions, the practical onset is slightly higher than pKa2.

Rule of thumb: Calcium oxalate precipitation becomes significant around pH ≈ 4.5–5 under typical millimolar concentrations in water at ~25 °C, and is strongly favored near neutral pH if the solution is supersaturated.

Notes
- Exact threshold depends on total Ca/oxalate, ionic strength, and which solid hydrate (COM vs COT) controls solubility. Complexation of Ca2+ by oxalate slightly shifts the onset to higher pH by lowering free ion activities.

Source: NIST Standard Reference Database 46 (SRD‑46): pKa data from search_pka_values (vlm_151532, vlm_151494) and Ca–oxalate constants summarized via build_system_catalog for Ca2+–oxalate.

---