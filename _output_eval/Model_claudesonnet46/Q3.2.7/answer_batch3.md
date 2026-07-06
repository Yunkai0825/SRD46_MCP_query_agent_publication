I now have all the data needed. Let me compute and present the final answer.

---

## Cu²⁺–Ammonia Stepwise Constants K₁–K₄ (25 °C, Aqueous)

### Cumulative β values from SRD-46 (log β, 25 °C)

I'll use the internally consistent dataset at **I = 0 M** (infinite dilution extrapolation, ref_eq_map_28132) and **I = 1 M** (ref_eq_map_28133) to show the pattern is robust across ionic strengths.

| Species | β definition | log β (I = 0 M) | log β (I = 1 M) |
|---------|-------------|-----------------|-----------------|
| Cu(NH₃)²⁺ | β₁ | 4.02 | 4.12 |
| Cu(NH₃)₂²⁺ | β₂ | 7.40 | 7.58 |
| Cu(NH₃)₃²⁺ | β₃ | 10.20 | 10.40 |
| Cu(NH₃)₄²⁺ | β₄ | 12.30 | 12.60 |

### Stepwise Constants Kₙ = βₙ / βₙ₋₁ (log Kₙ)

> log Kₙ = log βₙ − log βₙ₋₁

| Step | Reaction | log Kₙ (I = 0 M) | log Kₙ (I = 1 M) | Kₙ (I = 0 M) |
|------|----------|-------------------|-------------------|--------------|
| K₁ | Cu²⁺ + NH₃ → Cu(NH₃)²⁺ | **4.02** | **4.12** | ~10,500 |
| K₂ | Cu(NH₃)²⁺ + NH₃ → Cu(NH₃)₂²⁺ | **3.38** | **3.46** | ~2,400 |
| K₃ | Cu(NH₃)₂²⁺ + NH₃ → Cu(NH₃)₃²⁺ | **2.80** | **2.82** | ~630 |
| K₄ | Cu(NH₃)₃²⁺ + NH₃ → Cu(NH₃)₄²⁺ | **2.10** | **2.20** | ~126 |

---

### Do They Decrease Monotonically?

**Yes — strictly and consistently.** At both ionic strengths:

$$\log K_1 > \log K_2 > \log K_3 > \log K_4$$

$$4.02 > 3.38 > 2.80 > 2.10 \quad (I = 0\text{ M})$$

The stepwise drop is remarkably regular (~0.6–0.7 log units per step), which is close to the **statistical expectation** for a simple sequential substitution (each successive step has fewer available sites and more steric/electrostatic repulsion from already-bound NH₃ ligands).

---

### What Does This Tell Us About Coordination Geometry?

Several important insights emerge:

1. **Square-planar preference stops at n = 4.** Cu²⁺ is a d⁹ Jahn–Teller-active ion. Its preferred geometry is **square planar** (or elongated octahedral), with four strong equatorial bonds. The series terminates naturally at Cu(NH₃)₄²⁺ — a fifth ammonia would have to occupy an axial position, which is so weakly bound that no stable Cu(NH₃)₅²⁺ complex is observed in aqueous solution.

2. **The monotonic decrease is "well-behaved."** The ~0.6 log-unit drop per step is consistent with purely statistical and electrostatic effects — no anomalous jump or plateau appears between K₃ and K₄. This contrasts sharply with, e.g., Ni²⁺–ammonia (which forms octahedral Cu(NH₃)₆²⁺) or with systems showing a geometric change mid-series.

3. **Thermodynamic signature reinforces geometry.** The ΔH values grow more negative with each step (ΔH₁ ≈ −20.1, cumulative ΔH₄ ≈ −86.6 kJ/mol at I = 0 M), while ΔS becomes increasingly negative (from +9.6 to −55.2 J/mol·K for the cumulative β₄). The large entropy penalty at n = 4 reflects the rigid, ordered square-planar geometry and loss of translational freedom of four NH₃ molecules.

4. **Practical relevance.** The deep blue color of [Cu(NH₃)₄]²⁺ (Schweizer's reagent) exploits exactly this stable tetrammine complex. The fact that K₄ is still substantial (log K₄ ≈ 2.1, K₄ ≈ 126) means the tetrammine is thermodynamically accessible under moderate ammonia concentrations, making it useful for dissolving cellulose and precipitating copper in analytical chemistry.

---

*Source: NIST SRD-46 (Critically Selected Stability Constants of Metal Complexes), metal_41 (Cu²⁺) + ligand_10103 (NH₃), 25 °C, aqueous, ref_eq_map_28132 (I = 0 M) and ref_eq_map_28133 (I = 1 M).*

---