# Q2.2.6 - Validation (batch 3)

**16 of 33 claims unsupported**

| # | Para | Type | Unsupported Claim | Context |
|---|------|------|-------------------|---------|
| 1 | 0 | exact_value | \| **Metals with < 5 VLM measurements** \| **84** \| | ... \| **Total metals in database** \| 200 \| \| **Metals with < 5 VLM measurements** \| **84** \| \| **Fraction** \| **84 / 200 = 42.0%** \|... |
| 2 | 0 | exact_value | \| **Fraction** \| **84 / 200 = 42.0%** \| | ... with < 5 VLM measurements** \| **84** \| \| **Fraction** \| **84 / 200 = 42.0%** \|... |
| 3 | 1 | exact_value | \| 0 \| 50 \| Ag³⁺, Am⁴⁺, Cr⁴⁺, Ir³⁺, Ir⁴⁺, Mn⁴⁺, Pb⁴⁺, In⁺, No²⁺ \| | ...Representative Examples \| \|---\|---\|---\| \| 0 \| 50 \| Ag³⁺, Am⁴⁺, Cr⁴⁺, Ir³⁺, Ir⁴⁺, Mn⁴⁺, Pb⁴⁺, In⁺, No²⁺ \| \| 1 \| 12 \| CrO₄²⁻, Ge²⁺, Md³⁺, Np³⁺, Re... |
| 4 | 1 | exact_value | \| 1 \| 12 \| CrO₄²⁻, Ge²⁺, Md³⁺, Np³⁺, Re²⁺, UO₂⁺ \| | ...⁴⁺, Ir³⁺, Ir⁴⁺, Mn⁴⁺, Pb⁴⁺, In⁺, No²⁺ \| \| 1 \| 12 \| CrO₄²⁻, Ge²⁺, Md³⁺, Np³⁺, Re²⁺, UO₂⁺ \| \| 2 \| 16 \| Eu²⁺, OsO₃, OsO₄, Ru³⁺, TcO²... |
| 5 | 1 | exact_value | \| 2 \| 16 \| Eu²⁺, OsO₃, OsO₄, Ru³⁺, TcO²⁺, Mo₂O₇²⁻ \| | ... CrO₄²⁻, Ge²⁺, Md³⁺, Np³⁺, Re²⁺, UO₂⁺ \| \| 2 \| 16 \| Eu²⁺, OsO₃, OsO₄, Ru³⁺, TcO²⁺, Mo₂O₇²⁻ \| \| 3 \| 3 \| Fm³⁺, EtNH₃⁺, Te⁶⁺ \| \| 4 \| 3 ... |
| 6 | 1 | exact_value | \| 3 \| 3 \| Fm³⁺, EtNH₃⁺, Te⁶⁺ \| | ...u²⁺, OsO₃, OsO₄, Ru³⁺, TcO²⁺, Mo₂O₇²⁻ \| \| 3 \| 3 \| Fm³⁺, EtNH₃⁺, Te⁶⁺ \| \| 4 \| 3 \| MeB(OH)₂, m-NO₂PhB(OH)₂, Pa⁵⁺... |
| 7 | 1 | exact_value | \| 4 \| 3 \| MeB(OH)₂, m-NO₂PhB(OH)₂, Pa⁵⁺ \| | ...o₂O₇²⁻ \| \| 3 \| 3 \| Fm³⁺, EtNH₃⁺, Te⁶⁺ \| \| 4 \| 3 \| MeB(OH)₂, m-NO₂PhB(OH)₂, Pa⁵⁺ \| \| **Total < 5** \| **84** \| — \|... |
| 8 | 1 | exact_value | \| **Total < 5** \| **84** \| — \| | ...4 \| 3 \| MeB(OH)₂, m-NO₂PhB(OH)₂, Pa⁵⁺ \| \| **Total < 5** \| **84** \| — \|... |
| 9 | 2 | counting | Nearly **42% of all catalogued metals** have fewer than 5 VLM measurements | ...### Chemistry Insight  Nearly **42% of all catalogued metals** have fewer than 5 VLM measurements — a striking data sparsity that reflect... |
| 10 | 2 | counting | The remaining **116 metals (58%)** | ... rarely studied as central metal ions.  The remaining **116 metals (58%)** carry the vast majority of the database... |
| 11 | 2 | counting | Cu²⁺ (~8,963 VLMs) | ...s, with a handful of workhorse metals — Cu²⁺ (~8,963 VLMs), H⁺ (~20,720), Ni²⁺ (~5,325), Co²⁺ (~2,... |
| 12 | 2 | counting | H⁺ (~20,720) | ... workhorse metals — Cu²⁺ (~8,963 VLMs), H⁺ (~20,720), Ni²⁺ (~5,325), Co²⁺ (~2,977), Cd²⁺ (~2... |
| 13 | 2 | counting | Ni²⁺ (~5,325) | ...als — Cu²⁺ (~8,963 VLMs), H⁺ (~20,720), Ni²⁺ (~5,325), Co²⁺ (~2,977), Cd²⁺ (~2,828) — dominat... |
| 14 | 2 | counting | Co²⁺ (~2,977) | ...963 VLMs), H⁺ (~20,720), Ni²⁺ (~5,325), Co²⁺ (~2,977), Cd²⁺ (~2,828) — dominating the dataset... |
| 15 | 2 | counting | Cd²⁺ (~2,828) | ...~20,720), Ni²⁺ (~5,325), Co²⁺ (~2,977), Cd²⁺ (~2,828) — dominating the dataset.  *Source: NIS... |
| 16 | 2 | counting | 200 total metal entries. | ...6, `metal_card` LEFT JOIN `vlm` tables, 200 total metal entries.*... |