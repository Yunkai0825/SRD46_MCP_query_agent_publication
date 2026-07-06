# Q4.4 — Validation (batch 3)

**20 of 89 claims unsupported**

| # | Para | Type | Unsupported Claim | Context |
|---|------|------|-------------------|---------|
| 1 | 1 | exact_value | \| Glycine \| ligand_5760 \| N, O \| Benchmark bidentate; log β₁ ≈ 5.0 \| | …Donor Atoms \| Notes \| \|---\|---\|---\|---\| \| Glycine \| ligand_5760 \| N, O \| Benchmark bidentate; log β₁ ≈ 5.0 \| \| Alanine \| ligand_5761 \| N, O \| Simila… |
| 2 | 1 | exact_value | \| Alanine \| ligand_5761 \| N, O \| Similar to Gly; log β₁ ≈ 4.9 \| | …O \| Benchmark bidentate; log β₁ ≈ 5.0 \| \| Alanine \| ligand_5761 \| N, O \| Similar to Gly; log β₁ ≈ 4.9 \| \| Histidine \| ligand_5898 \| N(α-amino),… |
| 3 | 1 | exact_value | \| Histidine \| ligand_5898 \| N(α-amino), N(imidazole), O \| Tridentate capable; log β₁ ≈ 6.5 \| | …\| N, O \| Similar to Gly; log β₁ ≈ 4.9 \| \| Histidine \| ligand_5898 \| N(α-amino), N(imidazole), O \| Tridentate capable; log β₁ ≈ 6.5 \| \| Cysteine \| ligand_5856 \| N, O, S(thio… |
| 4 | 2 | exact_value | \| **Selenocysteine** \| ~2.0 \| ~9.0 \| ~5.2 (SeH) \| Selenol (Se) \| | …Key Extra Donor \| \|---\|---\|---\|---\|---\| \| **Selenocysteine** \| ~2.0 \| ~9.0 \| ~5.2 (SeH) \| Selenol (Se) \| \| **Methionine** \| 2.13 \| 9.27 \| — \| Th… |
| 5 | 2 | exact_value | \| **Methionine** \| 2.13 \| 9.27 \| — \| Thioether (S) \| | ….0 \| ~9.0 \| ~5.2 (SeH) \| Selenol (Se) \| \| **Methionine** \| 2.13 \| 9.27 \| — \| Thioether (S) \| \| **Tryptophan** \| 2.38 \| 9.39 \| — \| In… |
| 6 | 2 | exact_value | \| **Tryptophan** \| 2.38 \| 9.39 \| — \| Indole N \| | …e** \| 2.13 \| 9.27 \| — \| Thioether (S) \| \| **Tryptophan** \| 2.38 \| 9.39 \| — \| Indole N \| \| **DOPA (3,4-dihydroxyphenylalanine)**… |
| 7 | 3 | comparison | **Selenocysteine** Would Form the Most Stable Zn²⁺ Complex | …### 🏆 Prediction: **Selenocysteine** Would Form the Most Stable Zn²⁺ Complex  **Reasoning:**  1. **Donor atom hierar… |
| 8 | 3 | exact_value | The selenol pKa (~5.2) | …Zn²⁺ more tightly than harder O donors. The selenol pKa (~5.2) means it is **already deprotonated at p… |
| 9 | 3 | exact_value | ~8.3 for cysteine thiol | …     The very low selenol pKa (~5.2 vs. ~8.3 for cysteine thiol) means the selenolate form dominates at… |
| 10 | 4 | comparison | DOPA would rank below selenocysteine. | …ver, Zn²⁺ prefers N/S over O donors, so DOPA would rank below selenocysteine. It would still be significantly more st… |
| 11 | 4 | comparison | It would still be significantly more stable than simple aliphatic amino acids like glycine. | …o DOPA would rank below selenocysteine. It would still be significantly more stable than simple aliphatic amino acids like glycine.… |
| 12 | 5 | range | \| **Selenocysteine** ⭐ \| Selenolate (Se⁻) \| Very soft \| N, O, Se (tridentate) \| **~10–12** \| | …d log β₁ (est.) \| \|---\|---\|---\|---\|---\| \| **Selenocysteine** ⭐ \| Selenolate (Se⁻) \| Very soft \| N, O, Se (tridentate) \| **~10–12** \| \| Cysteine (studied) \| Thiolate (S⁻) \| … |
| 13 | 5 | range | \| Cysteine (studied) \| Thiolate (S⁻) \| Soft \| N, O, S (tridentate) \| ~9–10 \| | … \| N, O, Se (tridentate) \| **~10–12** \| \| Cysteine (studied) \| Thiolate (S⁻) \| Soft \| N, O, S (tridentate) \| ~9–10 \| \| Histidine (studied) \| Imidazole N \| B… |
| 14 | 5 | exact_value | \| Histidine (studied) \| Imidazole N \| Borderline \| N, N, O (tridentate) \| ~6.5 \| | …\| Soft \| N, O, S (tridentate) \| ~9–10 \| \| Histidine (studied) \| Imidazole N \| Borderline \| N, N, O (tridentate) \| ~6.5 \| \| DOPA \| Catecholate O,O \| Hard \| N, O,… |
| 15 | 5 | range | \| DOPA \| Catecholate O,O \| Hard \| N, O, O, O \| ~6–8 \| | …derline \| N, N, O (tridentate) \| ~6.5 \| \| DOPA \| Catecholate O,O \| Hard \| N, O, O, O \| ~6–8 \| \| Glycine (studied) \| — \| Hard \| N, O (… |
| 16 | 5 | exact_value | \| Glycine (studied) \| — \| Hard \| N, O (bidentate) \| ~5.0 \| | …holate O,O \| Hard \| N, O, O, O \| ~6–8 \| \| Glycine (studied) \| — \| Hard \| N, O (bidentate) \| ~5.0 \|  ---  **Conclusion:** Among amino acids… |
| 17 | 5 | existence_absence | Among amino acids not yet studied with Zn²⁺ in SRD-46, | …dentate) \| ~5.0 \|  ---  **Conclusion:** Among amino acids not yet studied with Zn²⁺ in SRD-46, **selenocysteine** is predicted to form… |
| 18 | 5 | comparison | **selenocysteine** is predicted to form the most stable zinc complex, | …ds not yet studied with Zn²⁺ in SRD-46, **selenocysteine** is predicted to form the most stable zinc complex, driven by its ultra-soft selenolate don… |
| 19 | 5 | trend | supported by the observed trend in SRD-46 data | …n is grounded in the HSAB framework and supported by the observed trend in SRD-46 data where S-donor amino acids (cysteine, pe… |
| 20 | 5 | comparison | already show higher Zn²⁺ affinity than N,O-only donors like glycine. | …r amino acids (cysteine, penicillamine) already show higher Zn²⁺ affinity than N,O-only donors like glycine.  *Source: NIST SRD-46 Critically Select… |