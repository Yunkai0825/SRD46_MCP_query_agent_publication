Here’s a matched-condition check using the Cu2+–glycine system (HL definition; aqueous), where both β1 (logK for [ML]/[M][L]) and β2 (logK for [ML2]/[M][L]2) are reported under identical conditions. The overall relation is β2 = K1 × K2, or in logs: logβ2 = logK1 + logK2.

I used 25 °C and I = 0.00 M (same reference-network cluster; aqueous). SRD-46 provides β1 and β2; stepwise K2 is not stored separately for this pair, so I derived logK2 = logβ2 − logK1 to illustrate the relationship (this means the check is not independent, just a consistency demonstration).

| T (°C) | I (M) | logK1 (ML; β1) | logK2 (stepwise; derived) | logβ2 (calc = logK1+logK2) | logβ2 (reported) | Δ (calc − rep) |
|---:|---:|---:|---:|---:|---:|---:|
| 25 | 0.00 | 8.56 | 7.14 | 15.70 | 15.7 | 0.00 |

- Data points: β1 at 25 °C, I=0.00 M (vlm_93854, beta_def_812); β2 at 25 °C, I=0.00 M (vlm_93869, beta_def_840).
- Result: The estimated overall β2 from stepwise K1 and K2 (logβ2_calc = 15.70) matches the β2 directly reported (15.7) within rounding.
- Chemistry note: K2 is smaller than K1 (here, ~7.14 vs 8.56 in log units), reflecting the expected decrease in incremental binding strength for the second glycine to Cu2+.

If you’d like, we can repeat the same calculation at other matched conditions in SRD-46 (e.g., 25 °C at I = 0.10, 0.5, 1.0, 2.0 M; or 10 °C and 40 °C) to show the trend with ionic strength and temperature.

Source: NIST Standard Reference Database 46 (SRD‑46) equilibrium data for Cu2+–glycine (metal_41, ligand_5760).

---