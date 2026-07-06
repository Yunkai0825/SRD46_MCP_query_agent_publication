# Q3.1.4 - Validation (batch 1)

**16 of 54 claims unsupported**

| # | Para | Type | Unsupported Claim | Context |
|---|------|------|-------------------|---------|
| 1 | 0 | exact_value | \| Fe³⁺ \| metal_61 \| 406 \| 1,473 \| | ... \| VLM Measurements \| \|---\|---\|---\|---\| \| Fe³⁺ \| metal_61 \| 406 \| 1,473 \| \| Fe²⁺ \| metal_62 \| 217 \| 667 \|  Fe³⁺ h... |
| 2 | 0 | exact_value | \| Fe²⁺ \| metal_62 \| 217 \| 667 \| | ...\|---\| \| Fe³⁺ \| metal_61 \| 406 \| 1,473 \| \| Fe²⁺ \| metal_62 \| 217 \| 667 \|  Fe³⁺ has been studied with roughly **t... |
| 3 | 0 | property_attribution | a direct SQL query on the `ligandmetal_card` table with `HAVING COUNT(DISTINCT metal_id) = 2` would give the precise figure. | ...on due to schema resolution issues, but a direct SQL query on the `ligandmetal_card` table with `HAVING COUNT(DISTINCT metal_id) = 2` would give the precise figure.... |
| 4 | 1 | trend | Yes, for the overwhelming majority of ligands | ...ently More Stable?  **The short answer: Yes, for the overwhelming majority of ligands — but with important exceptions.**  \| L... |
| 5 | 1 | range | \| Aminopolycarboxylates (EDTA, NTA, DTPA) \| O, N \| Fe³⁺ ≫ Fe²⁺ (Δlog β ≈ 10–15) \| Fe³⁺ is a harder Lewis acid \| | ...³⁺ vs Fe²⁺ \| Reason \| \|---\|---\|---\|---\| \| Aminopolycarboxylates (EDTA, NTA, DTPA) \| O, N \| Fe³⁺ ≫ Fe²⁺ (Δlog β ≈ 10–15) \| Fe³⁺ is a harder Lewis acid \| \| Hydroxamates, catecholates, phenolate... |
| 6 | 1 | exact_value | log β(Fe³⁺) ≈ 25.1 | ...o hard O- and N-donors. For EDTA alone, log β(Fe³⁺) ≈ 25.1 vs log β(Fe²⁺) ≈ 14.3 — a difference of... |
| 7 | 1 | exact_value | log β(Fe²⁺) ≈ 14.3 | .... For EDTA alone, log β(Fe³⁺) ≈ 25.1 vs log β(Fe²⁺) ≈ 14.3 — a difference of ~11 log units, meanin... |
| 8 | 1 | calculation | a difference of ~11 log units | ... β(Fe³⁺) ≈ 25.1 vs log β(Fe²⁺) ≈ 14.3 — a difference of ~11 log units, meaning Fe³⁺ binds ~10¹¹ times more st... |
| 9 | 1 | calculation | Fe³⁺ binds ~10¹¹ times more strongly. | ... a difference of ~11 log units, meaning Fe³⁺ binds ~10¹¹ times more strongly. This pattern holds broadly across the S... |
| 10 | 1 | trend | This pattern holds broadly across the SRD-46 dataset for oxygen-donor ligands. | ...g Fe³⁺ binds ~10¹¹ times more strongly. This pattern holds broadly across the SRD-46 dataset for oxygen-donor ligands.  The exceptions arise with **π-acceptin... |
| 11 | 2 | comparison | 2.2× larger ligand coverage for Fe³⁺ | ...Why Fe³⁺ Has a Much Larger Dataset  The 2.2× larger ligand coverage for Fe³⁺ (406 vs 217) and 2.2× more measurements... |
| 12 | 2 | counting | (406 vs 217) | ...he 2.2× larger ligand coverage for Fe³⁺ (406 vs 217) and 2.2× more measurements (1,473 vs 66... |
| 13 | 2 | counting | (1,473 vs 667) | ...(406 vs 217) and 2.2× more measurements (1,473 vs 667) reflects real-world chemical priorities... |
| 14 | 3 | property_attribution | the following query would work: | ... count** and a systematic Δlog β table, the following query would work:  ```sql SELECT c.ligand_id, c.ligand_na... |
| 15 | 3 | property_attribution | This would yield the precise number of shared ligands | ...ING COUNT(DISTINCT c.metal_id) = 2 ```  This would yield the precise number of shared ligands and enable a matched-condition comparis... |
| 16 | 3 | property_attribution | enable a matched-condition comparison of log β values for each. | ...he precise number of shared ligands and enable a matched-condition comparison of log β values for each.  *All counts sourced from NIST SRD-46 (... |