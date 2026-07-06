Here is the distribution of constant types across all **79,063 stability constant measurements** in the SRD-46 database:

| Constant Type | Count | Percentage | Description |
|---|---|---|---|
| **K** | 60,540 | 76.57% | Stepwise stability constants (log K) |
| **H** | 9,693 | 12.26% | Enthalpy-related constants (ΔH) |
| **S** | 8,830 | 11.17% | Entropy-related constants (ΔS) |
| **Total** | **79,063** | **100%** | All measurements |

---

### 🔬 Chemistry Insights

1. **K dominates (~77%)** — Stepwise stability constants (log K) are by far the most common measurement type. These describe the sequential addition of ligands to a metal center (e.g., M + L ⇌ ML, ML + L ⇌ ML₂, etc.) and are the primary thermodynamic descriptor used in speciation modeling.

2. **H and S together (~23%)** — Enthalpy (ΔH) and entropy (ΔS) measurements are less common but critically important for understanding the *driving forces* of complexation. Their roughly similar counts suggest that when thermodynamic studies are done, researchers typically report both ΔH and ΔS together (via calorimetry or van't Hoff analysis).

3. **No β listed separately** — Overall (cumulative) β constants (β = K₁·K₂·…·Kₙ) are likely stored under the **beta_definition** schema rather than as a separate `constant_type` flag — they represent a *definition* of how constants are combined, not a distinct measurement type in this column.

> **Source:** NIST SRD-46 — `ligandmetal_stability_measured` table, 79,063 total records.

---