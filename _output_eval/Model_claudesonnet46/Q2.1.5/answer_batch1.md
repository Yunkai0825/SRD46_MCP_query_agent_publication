## Results: Ni²⁺ Binding — Ammonia vs. Ethylenediamine

### Stepwise log K₁ at 25 °C (β_def_812: M + L ⇌ ML)

| Ligand | I = 0 (extrapolated) | I = 0.1 M | I = 1.0 M |
|--------|----------------------|-----------|-----------|
| Ammonia (NH₃) | **2.72** | 2.73 | 2.80 |
| Ethylenediamine (en) | **7.32** | 7.30 | 7.56 |
| **Δ log K (en − NH₃)** | **+4.60** | **+4.57** | **+4.76** |

*Source: NIST SRD-46 (vlm_173185 for NH₃; vlm_122371 for en)*

---

### Answer

**Ethylenediamine (en) binds far more strongly to Ni²⁺ than ammonia does.**

At 25 °C and I → 0 (extrapolated to zero ionic strength):

| Quantity | Value |
|----------|-------|
| log K₁ (Ni²⁺ + NH₃) | 2.72 |
| log K₁ (Ni²⁺ + en) | 7.32 |
| **Δ log K₁ (en − NH₃)** | **+4.60** |

This corresponds to a **~40,000-fold** greater equilibrium constant for en vs. NH₃ (10^4.60 ≈ 40,000). The difference is remarkably consistent across ionic strengths (Δ ≈ 4.6–4.8 log units), confirming it is a genuine thermodynamic effect rather than an ionic-strength artifact.

---

### Chemistry Insight: The Chelate Effect

This dramatic difference is the textbook **chelate effect**. Ethylenediamine is a *bidentate* ligand — its two –NH₂ groups simultaneously coordinate to Ni²⁺, forming a stable five-membered chelate ring. This provides:

1. **Entropic advantage**: Replacing two monodentate NH₃ molecules with one en molecule releases one extra free particle into solution, increasing entropy (ΔS > 0).
2. **Macrochelate rigidity**: Once one end of en binds, the second –NH₂ is held in close proximity, making ring closure kinetically and thermodynamically favorable.

The thermodynamic data confirm this: for en, ΔH ≈ 0 kJ/mol at I = 0.1 M (vlm_122372), meaning the binding is *entirely entropy-driven* — a hallmark of the chelate effect. For NH₃, ΔH ≈ −15 kJ/mol (vlm_173186), so binding is enthalpically driven but entropically less favorable.

> **Source:** NIST Standard Reference Database 46 (SRD-46), aqueous phase, 25 °C.

---