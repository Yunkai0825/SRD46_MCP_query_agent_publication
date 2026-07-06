# Q2.2.6 - Validation (batch 5)

**15 of 35 claims unsupported**

| # | Para | Type | Unsupported Claim | Context |
|---|------|------|-------------------|---------|
| 1 | 0 | citation | (confirmed by `db_count_records` on the `metal_card` table) | ...rements in SRD-46  The database queries (confirmed by `db_count_records` on the `metal_card` table) give the following verified results:... |
| 2 | 1 | exact_value | \| Metals with < 5 VLM measurements \| **104** \| | ...-\| \| Total metals in SRD-46 \| **230** \| \| Metals with < 5 VLM measurements \| **104** \| \| Fraction of all metals \| **104 / 230 ... |
| 3 | 1 | calculation | \| Fraction of all metals \| **104 / 230 ≈ 45.2%** \| | ...s with < 5 VLM measurements \| **104** \| \| Fraction of all metals \| **104 / 230 ≈ 45.2%** \|... |
| 4 | 2 | exact_value | \| 0 \| 71 \| Noble gases (He, Ne, Ar, Kr, Xe, Rn), transactinides (Rf–Lr), Ir³⁺/⁴⁺, Pt⁴⁺, Ta⁵⁺, Yb²⁺, Fr⁺, neutral non-metals (O, F, S, Cl, Br, I) \| | ...------\|-------------\|-----------------\| \| 0 \| 71 \| Noble gases (He, Ne, Ar, Kr, Xe, Rn), transactinides (Rf–Lr), Ir³⁺/⁴⁺, Pt⁴⁺, Ta⁵⁺, Yb²⁺, Fr⁺, neutral non-metals (O, F, S, Cl, Br, I) \| \| 1 \| 12 \| Ge²⁺, Md³⁺, Mo³⁺, Np³⁺, Re²⁺... |
| 5 | 2 | exact_value | \| 1 \| 12 \| Ge²⁺, Md³⁺, Mo³⁺, Np³⁺, Re²⁺, UO₂⁺, Et₂NH₂⁺ \| | ...utral non-metals (O, F, S, Cl, Br, I) \| \| 1 \| 12 \| Ge²⁺, Md³⁺, Mo³⁺, Np³⁺, Re²⁺, UO₂⁺, Et₂NH₂⁺ \| \| 2 \| 16 \| Eu²⁺, OsO₃, OsO₄, Ru³⁺, Re⁵⁺... |
| 6 | 2 | exact_value | \| 2 \| 16 \| Eu²⁺, OsO₃, OsO₄, Ru³⁺, Re⁵⁺, Ph₂Pb²⁺, Pr₂Sn²⁺ \| | ...Md³⁺, Mo³⁺, Np³⁺, Re²⁺, UO₂⁺, Et₂NH₂⁺ \| \| 2 \| 16 \| Eu²⁺, OsO₃, OsO₄, Ru³⁺, Re⁵⁺, Ph₂Pb²⁺, Pr₂Sn²⁺ \| \| 3 \| 2 \| Fm³⁺, Te⁶⁺ \| \| 4 \| 3 \| MeB(OH... |
| 7 | 2 | exact_value | \| 3 \| 2 \| Fm³⁺, Te⁶⁺ \| | ...₃, OsO₄, Ru³⁺, Re⁵⁺, Ph₂Pb²⁺, Pr₂Sn²⁺ \| \| 3 \| 2 \| Fm³⁺, Te⁶⁺ \| \| 4 \| 3 \| MeB(OH)₂, m-NO₂PhB(OH)₂, Pa⁵⁺... |
| 8 | 2 | exact_value | \| 4 \| 3 \| MeB(OH)₂, m-NO₂PhB(OH)₂, Pa⁵⁺ \| | ...₂Pb²⁺, Pr₂Sn²⁺ \| \| 3 \| 2 \| Fm³⁺, Te⁶⁺ \| \| 4 \| 3 \| MeB(OH)₂, m-NO₂PhB(OH)₂, Pa⁵⁺ \| \| **< 5 subtotal** \| **104** \| — \| \| ≥ ... |
| 9 | 2 | exact_value | \| **< 5 subtotal** \| **104** \| — \| | ...4 \| 3 \| MeB(OH)₂, m-NO₂PhB(OH)₂, Pa⁵⁺ \| \| **< 5 subtotal** \| **104** \| — \| \| ≥ 5 \| 126 \| Cu²⁺ (8,963 VLMs), H⁺ (20... |
| 10 | 2 | exact_value | \| ≥ 5 \| 126 \| Cu²⁺ (8,963 VLMs), H⁺ (20,720), Ni²⁺ (5,325), Zn²⁺ (4,095), Co²⁺ (2,977) \| | ...⁵⁺ \| \| **< 5 subtotal** \| **104** \| — \| \| ≥ 5 \| 126 \| Cu²⁺ (8,963 VLMs), H⁺ (20,720), Ni²⁺ (5,325), Zn²⁺ (4,095), Co²⁺ (2,977) \| \| **Grand Total** \| **230** \| — \|... |
| 11 | 3 | counting | Nearly **half** of all registered metal entities are data-sparse | ...### Chemistry Insight  Nearly **half** of all registered metal entities are data-sparse, but this reflects two distinct situati... |
| 12 | 3 | counting | this reflects two distinct situations | ...red metal entities are data-sparse, but this reflects two distinct situations. First, many entries are **registry pla... |
| 13 | 3 | property_attribution | are included for completeness | ...ic atoms, and superheavy transactinides are included for completeness but have no aqueous coordination chemis... |
| 14 | 3 | counting | The remaining **126 metals (≥ 5 VLMs)** | ...urements extremely difficult to obtain. The remaining **126 metals (≥ 5 VLMs)** represent the true working set of SRD-4... |
| 15 | 3 | property_attribution | represent the true working set of SRD-46 | ...The remaining **126 metals (≥ 5 VLMs)** represent the true working set of SRD-46, dominated by biologically and industri... |