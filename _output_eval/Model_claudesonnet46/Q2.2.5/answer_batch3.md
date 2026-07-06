Here is the distribution of constant types across all **79,063** stability constant measurements in SRD-46:

| Constant Type | Count | Percentage | Description |
|---|---|---|---|
| **K** | 60,540 | 76.57% | Stepwise stability constants (Kₙ) |
| **H** | 9,693 | 12.26% | Enthalpy-related constants (ΔH) |
| **S** | 8,830 | 11.17% | Entropy-related constants (ΔS) |
| **Total** | **79,063** | 100% | All measurements |

---

### 🔬 Chemistry Insights

1. **K dominates (~77%)** — Stepwise stability constants are by far the most commonly reported quantity. These describe the sequential addition of each ligand to the metal center (e.g., M + L ⇌ ML, ML + L ⇌ ML₂), and are the primary thermodynamic descriptor for complex formation.

2. **H and S are thermodynamic companions (~23% combined)** — Enthalpy (ΔH) and entropy (ΔS) values are measured less frequently, typically via calorimetry or van't Hoff analysis. Their near-equal counts suggest they are often reported together as a pair when researchers go beyond simple equilibrium measurements to characterize the full thermodynamic picture (ΔG = ΔH − TΔS).

3. **No β (overall) type listed separately** — In SRD-46, overall formation constants (β) are encoded in the `beta_definition` schema rather than as a separate `constant_type` flag, so the K values here include both stepwise and overall constants depending on the associated beta definition.

> **Source:** NIST SRD-46 `ligandmetal_stability_measured` table, 79,063 total records.

---