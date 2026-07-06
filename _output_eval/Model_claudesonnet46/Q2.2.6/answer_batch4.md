## Results: Metals with Fewer Than 5 VLM Measurements

| Metric | Value |
|---|---|
| **Total metals in database** | 230 |
| **Metals with < 5 VLM measurements** | 114 |
| **Fraction** | 114 / 230 ≈ **49.6%** |

---

### Key Takeaways

Nearly **half of all metals** in SRD-46 have fewer than 5 VLM (Value-Linked Measurement) entries — meaning the database coverage is highly skewed. A relatively small number of well-studied metals (e.g., Cu²⁺, Fe³⁺, Zn²⁺, Ni²⁺) likely account for the bulk of the measurements, while many rarer or less-studied metal species (including exotic oxidation states, organometallic entries, or uncommon elements) have very sparse data.

This kind of long-tail distribution is typical in thermodynamic databases: decades of research focus on biologically and industrially relevant metals, leaving many others with only a handful of literature measurements.

*Source: NIST SRD-46, queried via LEFT JOIN of `metal_card` → `eq_node` (equilibrium database).*

---