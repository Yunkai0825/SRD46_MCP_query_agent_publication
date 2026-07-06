# Q4.7 - Validation (batch 5)

**31 of 98 claims unsupported**

| # | Para | Type | Unsupported Claim | Context |
|---|------|------|-------------------|---------|
| 1 | 1 | property_attribution | log K₁ | ...## Matched Stability Data (log K₁, 25 °C, I = 0.1 M, aqueous)  \| Ligand \|... |
| 2 | 1 | exact_value | 25 °C | ...## Matched Stability Data (log K₁, 25 °C, I = 0.1 M, aqueous)  \| Ligand \| Donor ... |
| 3 | 1 | exact_value | I = 0.1 M | ... Matched Stability Data (log K₁, 25 °C, I = 0.1 M, aqueous)  \| Ligand \| Donor Set \| Denti... |
| 4 | 1 | property_attribution | aqueous | ...ability Data (log K₁, 25 °C, I = 0.1 M, aqueous)  \| Ligand \| Donor Set \| Denticity \| lo... |
| 5 | 1 | exact_value | \| Ethylenediamine (en) \| N₂ \| 2 \| 5.89 \| — ¹ \| — \| | ...-------------\|------------------------\| \| Ethylenediamine (en) \| N₂ \| 2 \| 5.89 \| — ¹ \| — \| \| Iminodiacetic acid (IDA) \| N, O₂ \| 3 ... |
| 6 | 1 | exact_value | \| Iminodiacetic acid (IDA) \| N, O₂ \| 3 \| 7.26 \| 29.6 \| **+22.3** \| | ...iamine (en) \| N₂ \| 2 \| 5.89 \| — ¹ \| — \| \| Iminodiacetic acid (IDA) \| N, O₂ \| 3 \| 7.26 \| 29.6 \| **+22.3** \| \| Nitrilotriacetic acid (NTA) \| N, O₃ \|... |
| 7 | 1 | exact_value | \| Nitrilotriacetic acid (NTA) \| N, O₃ \| 4 \| 10.38 \| — ² \| — \| | ...\| N, O₂ \| 3 \| 7.26 \| 29.6 \| **+22.3** \| \| Nitrilotriacetic acid (NTA) \| N, O₃ \| 4 \| 10.38 \| — ² \| — \| \| EDTA \| N₂, O₄ \| 6 \| 16.31 \| 41.4 \| **... |
| 8 | 1 | exact_value | \| EDTA \| N₂, O₄ \| 6 \| 16.31 \| 41.4 \| **+25.1** \| | ...d (NTA) \| N, O₃ \| 4 \| 10.38 \| — ² \| — \| \| EDTA \| N₂, O₄ \| 6 \| 16.31 \| 41.4 \| **+25.1** \|  > ¹ Co³⁺ + en data in SRD-46 exist onl... |
| 9 | 1 | existence_absence | ¹ Co³⁺ + en data in SRD-46 exist only as stepwise K₃ and hydrolysis constants, | ... O₄ \| 6 \| 16.31 \| 41.4 \| **+25.1** \|  > ¹ Co³⁺ + en data in SRD-46 exist only as stepwise K₃ and hydrolysis constants, not as the overall β₁ (ML) formation co... |
| 10 | 1 | existence_absence | not as the overall β₁ (ML) formation constant. | ...s stepwise K₃ and hydrolysis constants, not as the overall β₁ (ML) formation constant. > ² Co³⁺ + NTA data exist only as hydro... |
| 11 | 1 | existence_absence | ² Co³⁺ + NTA data exist only as hydrolysis constants (M(OH)L species), | ...e overall β₁ (ML) formation constant. > ² Co³⁺ + NTA data exist only as hydrolysis constants (M(OH)L species), not β₁.  *Source: NIST SRD-46 Critical ... |
| 12 | 1 | existence_absence | not β₁. | ... hydrolysis constants (M(OH)L species), not β₁.  *Source: NIST SRD-46 Critical Stabilit... |
| 13 | 1 | citation | *Source: NIST SRD-46 Critical Stability Constants Database* | ...is constants (M(OH)L species), not β₁.  *Source: NIST SRD-46 Critical Stability Constants Database*... |
| 14 | 2 | range | The difference between Co³⁺ and Co²⁺ log K₁ is **22–25 log units** | ...vations  1. **Enormous Δlog K values.** The difference between Co³⁺ and Co²⁺ log K₁ is **22–25 log units** — meaning Co³⁺ complexes are roughly **... |
| 15 | 2 | calculation | Co³⁺ complexes are roughly **10²² to 10²⁵ times** more stable than their Co²⁺ analogues with the same ligand under matched conditions. | ...log K₁ is **22–25 log units** — meaning Co³⁺ complexes are roughly **10²² to 10²⁵ times** more stable than their Co²⁺ analogues with the same ligand under matched conditions.  2. **Trend with denticity.** Moving fr... |
| 16 | 2 | exact_value | Δ ≈ 22.3 | ...city.** Moving from the tridentate IDA (Δ ≈ 22.3) to the hexadentate EDTA (Δ ≈ 25.1), th... |
| 17 | 2 | exact_value | Δ ≈ 25.1 | ...IDA (Δ ≈ 22.3) to the hexadentate EDTA (Δ ≈ 25.1), the gap widens by nearly 3 log units.... |
| 18 | 2 | calculation | the gap widens by nearly 3 log units. | ....3) to the hexadentate EDTA (Δ ≈ 25.1), the gap widens by nearly 3 log units. Higher denticity amplifies the stabiliz... |
| 19 | 3 | range | \| Predicted Δlog K \| — \| **+20 to +25 or more** \| | ...rate (5–15) \| Extremely high (30–40+) \| \| Predicted Δlog K \| — \| **+20 to +25 or more** \| \| CFSE contribution \| Small (−0.8 Δ_oct... |
| 20 | 4 | range | a new polydentate amine should show log K₁ values 20–25+ orders of magnitude above Co²⁺. | ...* Based on the IDA and EDTA benchmarks, a new polydentate amine should show log K₁ values 20–25+ orders of magnitude above Co²⁺. Pure nitrogen donors are strong-field l... |
| 21 | 4 | range | if a tetradentate amine gives log K₁ ≈ 10–12 with Co²⁺, | ...e low-spin CFSE advantage. For example, if a tetradentate amine gives log K₁ ≈ 10–12 with Co²⁺, one would predict log K₁ ≈ 32–37 with C... |
| 22 | 4 | range | one would predict log K₁ ≈ 32–37 with Co³⁺. | ...e amine gives log K₁ ≈ 10–12 with Co²⁺, one would predict log K₁ ≈ 32–37 with Co³⁺.  2. **Increasing denticity will widen t... |
| 23 | 4 | trend | The data show the gap growing | ...d enthalpic reinforcement through CFSE. The data show the gap growing from ~22 (tridentate IDA) to ~25 (hexad... |
| 24 | 4 | exact_value | ~22 (tridentate IDA) | ...FSE. The data show the gap growing from ~22 (tridentate IDA) to ~25 (hexadentate EDTA). A hexadentat... |
| 25 | 4 | exact_value | ~25 (hexadentate EDTA) | ...ap growing from ~22 (tridentate IDA) to ~25 (hexadentate EDTA). A hexadentate polyamine (e.g., a linea... |
| 26 | 4 | range | Δlog K ≥ 25 | ...amine or macrocyclic amine) should show Δlog K ≥ 25, potentially exceeding 30 if the ligand... |
| 27 | 4 | range | potentially exceeding 30 | ...ocyclic amine) should show Δlog K ≥ 25, potentially exceeding 30 if the ligand geometry perfectly matche... |
| 28 | 4 | range | Δlog K at the upper end of (or exceeding) the 22–25 range | ... pure polyamine should therefore show a Δlog K at the upper end of (or exceeding) the 22–25 range observed for mixed N/O donors.... |
| 29 | 5 | range | 10²²–10²⁵ times more stable | ...te that Co³⁺ forms complexes that are **10²²–10²⁵ times more stable** than the corresponding Co²⁺ complexes... |
| 30 | 5 | comparison | among the largest oxidation-state effects in the periodic table | ...plexes. This extraordinary difference — among the largest oxidation-state effects in the periodic table — arises from the synergy of higher ion... |
| 31 | 5 | range | with the stability gap likely at or above 25 log units for a hexadentate system | ... predicted to follow this same pattern, with the stability gap likely at or above 25 log units for a hexadentate system, making such complexes among the most t... |