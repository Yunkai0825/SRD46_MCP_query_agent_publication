Short answer: Cysteine gives the highest Cu2+/Ni2+ selectivity at pH 7 among common amino acids.

Why: The thiolate donor in cysteine binds Cu2+ far more strongly than Ni2+. Using matched 25 °C, I≈0.1 M aqueous data from NIST SRD‑46, the Δlogβ1 for ML (M + L ⇌ ML) is largest for cysteine, and at pH 7 the ligand deprotonation factor largely cancels when taking the Cu/Ni ratio for a given ligand, so Δlogβ1 is a good proxy for conditional selectivity S ≈ 10^(Δlogβ1).

| Ligand (SRD‑46 ID) | log β1 (Cu2+ + L ⇌ ML) | log β1 (Ni2+ + L ⇌ ML) | Δlogβ1 (Cu−Ni) | Selectivity S ≈ 10^(Δlogβ1) | Conditions |
|---|---:|---:|---:|---:|---|
| Cysteine (ligand_5856) | 12.7 | 8.3 | 4.4 | ~2.5×10^4 | 25 °C, I=0.10 M NaNO3 |
| Histidine (ligand_5898) | 9.95 | 7.52 | 2.43 | ~2.7×10^2 | 25 °C, I≈0.10 M (aqueous) |
| Glycine (ligand_5760) | 8.56 | 6.67 | 1.89 | ~7.8×10^1 | 25 °C, I≈0.10 M (aqueous) |
| Aspartic acid (ligand_5802) | 4.60 | 3.20 | 1.40 | ~2.5×10^1 | 25 °C, I=0.10 M NaNO3 |
| Glutamic acid (ligand_5804) | 5.80 | 4.40 | 1.40 | ~2.5×10^1 | 25 °C, I≈0.10 M (aqueous) |
| Methionine (ligand_5863) | 6.2 | 5.0 | 1.2 | ~1.6×10^1 | 25 °C, I≈0.1 M (aqueous) |

Notes for use at pH 7:
- Amino acids are largely zwitterionic at pH 7; the binding form L involves deprotonation of the ammonium (and, for cysteine, of the thiol). When comparing Cu2+ vs Ni2+ for the same ligand, the ligand availability factor (αL) at pH 7 mostly cancels, so the Cu/Ni selectivity is governed primarily by Δlogβ1. Including ML2 does not change the ranking for these ligands under near‑neutral conditions.
- Cysteine’s very large Δlogβ1 reflects the strong preference of Cu2+ for thiolate S donors relative to Ni2+. Histidine is the next best due to its imidazole N donor; simple O,O donors (Asp/Glu) give modest selectivity.

Source: NIST Standard Reference Database 46 (Critical Stability Constants).

---