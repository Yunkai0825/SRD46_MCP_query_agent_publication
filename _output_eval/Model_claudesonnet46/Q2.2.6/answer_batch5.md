## Metals with Fewer Than 5 VLM Measurements in SRD-46

The database queries (confirmed by `db_count_records` on the `metal_card` table) give the following verified results:

### Key Statistics

| Metric | Value |
|--------|-------|
| Total metals in SRD-46 | **230** |
| Metals with < 5 VLM measurements | **104** |
| Fraction of all metals | **104 / 230 ≈ 45.2%** |

### Breakdown by VLM Count (bins 0–4)

| VLM Count | # of Metals | Notable Examples |
|-----------|-------------|-----------------|
| 0 | 71 | Noble gases (He, Ne, Ar, Kr, Xe, Rn), transactinides (Rf–Lr), Ir³⁺/⁴⁺, Pt⁴⁺, Ta⁵⁺, Yb²⁺, Fr⁺, neutral non-metals (O, F, S, Cl, Br, I) |
| 1 | 12 | Ge²⁺, Md³⁺, Mo³⁺, Np³⁺, Re²⁺, UO₂⁺, Et₂NH₂⁺ |
| 2 | 16 | Eu²⁺, OsO₃, OsO₄, Ru³⁺, Re⁵⁺, Ph₂Pb²⁺, Pr₂Sn²⁺ |
| 3 | 2 | Fm³⁺, Te⁶⁺ |
| 4 | 3 | MeB(OH)₂, m-NO₂PhB(OH)₂, Pa⁵⁺ |
| **< 5 subtotal** | **104** | — |
| ≥ 5 | 126 | Cu²⁺ (8,963 VLMs), H⁺ (20,720), Ni²⁺ (5,325), Zn²⁺ (4,095), Co²⁺ (2,977) |
| **Grand Total** | **230** | — |

### Chemistry Insight

Nearly **half** of all registered metal entities are data-sparse, but this reflects two distinct situations. First, many entries are **registry placeholders**: noble gases, neutral non-metallic atoms, and superheavy transactinides are included for completeness but have no aqueous coordination chemistry data. Second, some are **chemically exotic species** — Ir³⁺/⁴⁺, Pt⁴⁺, Pd⁴⁺, Pb⁴⁺, and high-valent actinides (Pa⁵⁺, U³⁺) are either strongly oxidizing, kinetically inert, or radioactively unstable, making equilibrium measurements extremely difficult to obtain. The remaining **126 metals (≥ 5 VLMs)** represent the true working set of SRD-46, dominated by biologically and industrially important ions such as H⁺, Cu²⁺, Ni²⁺, Zn²⁺, and Co²⁺.

*Source: NIST SRD-46 — Critically Selected Stability Constants of Metal Complexes*

---