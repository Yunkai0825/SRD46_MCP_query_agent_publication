Here is the distribution of stability constant types across all **79,063 measurements** in the SRD-46 database:

| Constant Type | Count | Percentage | Description |
|---|---|---|---|
| **K** | 60,540 | 76.57% | Stepwise stability constants (Kₙ) |
| **H** | 9,693 | 12.26% | Enthalpy-related constants (ΔH) |
| **S** | 8,830 | 11.17% | Overall (cumulative) stability constants (β) |

> *Source: NIST SRD-46 — `ligandmetal_stability_measured` table*

---

### 🔍 Chemistry Insights

1. **K dominates (76.6%)** — Stepwise constants are by far the most commonly reported, reflecting the field's preference for describing successive ligand additions (ML, ML₂, ML₃, …) individually. They are directly interpretable and experimentally accessible via potentiometry.

2. **H values (12.3%)** — Enthalpy measurements (calorimetric data) are a significant minority, enabling thermodynamic decomposition of stability into enthalpic and entropic contributions (ΔG = ΔH − TΔS). Their presence highlights the database's value for thermodynamic profiling beyond just equilibrium constants.

3. **S / β values (11.2%)** — Overall (cumulative) formation constants (β = K₁·K₂·…·Kₙ) are less numerous but critical for modeling speciation in solution, especially in environmental and biological contexts where total complex formation matters more than stepwise details.

---