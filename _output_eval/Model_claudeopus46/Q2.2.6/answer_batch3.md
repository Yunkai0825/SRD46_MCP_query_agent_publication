I have all the data I need from the search_metals results. Let me compute the answer directly from the 230 metals returned.

Going through all 230 metals and counting those with `vlm_count < 5`:

**vlm_count = 0 → 74 metals**
**vlm_count = 1 → 13 metals**
**vlm_count = 2 → 16 metals**
**vlm_count = 3 → 3 metals**
**vlm_count = 4 → 3 metals**

**Total with < 5 VLM measurements: 109**

---


| Metric | Value |
|---|---|
| Total metals in SRD-46 | **230** |
| Metals with < 5 VLM measurements | **109** |
| Fraction of all metals | **109 / 230 ≈ 47.4%** |

### Breakdown by VLM count

| VLM count | Number of metals |
|---|---|
| 0 | 74 |
| 1 | 13 |
| 2 | 16 |
| 3 | 3 |
| 4 | 3 |
| **Total < 5** | **109** |

Nearly half of all metal entries in NIST SRD-46 have fewer than 5 VLM measurements. The vast majority of these (74 out of 109) have **zero** measurements — including noble gases (He, Ne, Ar, Kr, Xe, Rn), superheavy elements (Rf, Db, Sg, Bh, Hs, Mt, Lr), and exotic oxidation states (e.g., Ir³⁺, Ir⁴⁺, Pb⁴⁺, Sb⁵⁺, V⁴⁺). This highlights how stability constant data is heavily concentrated among a small set of commonly studied metal ions — Cu²⁺ alone accounts for ~9,000 VLM measurements, while H⁺ leads with ~20,700.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes)*

---