# Co²⁺ vs Co³⁺ Stability Constants: A Crystal-Field Comparison

## Matched Stability Data (log K₁, 25 °C, I = 0.1 M, aqueous)

| Ligand | Donor Set | Denticity | log K₁ (Co²⁺) | log K₁ (Co³⁺) | Δlog K (Co³⁺ − Co²⁺) |
|--------|-----------|-----------|----------------|----------------|------------------------|
| Ethylenediamine (en) | N₂ | 2 | 5.89 | — ¹ | — |
| Iminodiacetic acid (IDA) | N, O₂ | 3 | 7.26 | 29.6 | **+22.3** |
| Nitrilotriacetic acid (NTA) | N, O₃ | 4 | 10.38 | — ² | — |
| EDTA | N₂, O₄ | 6 | 16.31 | 41.4 | **+25.1** |

> ¹ Co³⁺ + en data in SRD-46 exist only as stepwise K₃ and hydrolysis constants, not as the overall β₁ (ML) formation constant.
> ² Co³⁺ + NTA data exist only as hydrolysis constants (M(OH)L species), not β₁.

*Source: NIST SRD-46 Critical Stability Constants Database*

---

## Key Observations

1. **Enormous Δlog K values.** The difference between Co³⁺ and Co²⁺ log K₁ is **22–25 log units** — meaning Co³⁺ complexes are roughly **10²² to 10²⁵ times** more stable than their Co²⁺ analogues with the same ligand under matched conditions.

2. **Trend with denticity.** Moving from the tridentate IDA (Δ ≈ 22.3) to the hexadentate EDTA (Δ ≈ 25.1), the gap widens by nearly 3 log units. Higher denticity amplifies the stabilization advantage of Co³⁺, consistent with the chelate effect compounding on top of the intrinsic electronic preference.

3. **Crystal-field origin.** The massive stability difference has two reinforcing causes:
   - **Electrostatics:** The +3 charge provides ~50% stronger Coulombic attraction to donor atoms than +2.
   - **Crystal-field stabilization energy (CFSE):** Co³⁺ is d⁶ and almost universally adopts a **low-spin octahedral** configuration (t₂g⁶ eg⁰), gaining the maximum possible CFSE of −2.4 Δ_oct. Co²⁺ is d⁷ and typically **high-spin** (t₂g⁵ eg²), with a much smaller CFSE of only −0.8 Δ_oct. Moreover, the higher charge of Co³⁺ increases Δ_oct itself (roughly 50% larger for M³⁺ vs M²⁺), so the absolute CFSE advantage is even greater than the coefficient ratio suggests.

---

## Prediction for a New Polydentate Amine Ligand

| Property | Co²⁺ (d⁷, high-spin) | Co³⁺ (d⁶, low-spin) |
|----------|----------------------|----------------------|
| Expected log K₁ | Moderate (5–15) | Extremely high (30–40+) |
| Predicted Δlog K | — | **+20 to +25 or more** |
| CFSE contribution | Small (−0.8 Δ_oct) | Maximum (−2.4 Δ_oct) |
| Kinetics | Labile (fast ligand exchange) | Inert (very slow substitution) |
| Preferred geometry | Octahedral or tetrahedral | Strictly octahedral |
| Spin state | High-spin | Low-spin |

### Detailed Predictions

1. **Stability with Co³⁺ will be dramatically higher.** Based on the IDA and EDTA benchmarks, a new polydentate amine should show log K₁ values 20–25+ orders of magnitude above Co²⁺. Pure nitrogen donors are strong-field ligands that push Δ_oct even higher for Co³⁺, maximizing the low-spin CFSE advantage. For example, if a tetradentate amine gives log K₁ ≈ 10–12 with Co²⁺, one would predict log K₁ ≈ 32–37 with Co³⁺.

2. **Increasing denticity will widen the gap.** Each additional chelate ring adds both entropic stabilization (chelate effect) and enthalpic reinforcement through CFSE. The data show the gap growing from ~22 (tridentate IDA) to ~25 (hexadentate EDTA). A hexadentate polyamine (e.g., a linear tetramine or macrocyclic amine) should show Δlog K ≥ 25, potentially exceeding 30 if the ligand geometry perfectly matches the octahedral preference of low-spin Co³⁺.

3. **Kinetic inertness of Co³⁺ complexes** is a direct consequence of the t₂g⁶ configuration: there are no electrons in the antibonding eg orbitals, making ligand dissociation extremely slow. Once formed, the polydentate amine–Co³⁺ complex will be extraordinarily resistant to dissociation — a property exploited in vitamin B₁₂ chemistry, cobalt-based catalysts, and radiopharmaceutical chelators.

4. **Co²⁺ complexes will be labile and moderate in stability**, making them useful as precursors that can be oxidized *in situ* to trap the kinetically inert Co³⁺ complex. This is a classic synthetic strategy: form the labile Co²⁺–amine complex rapidly, then oxidize with H₂O₂ or O₂ to lock in the substitution-inert Co³⁺ product.

5. **Amine donors specifically favor Co³⁺.** Nitrogen is a stronger-field donor than oxygen, so the CFSE advantage of Co³⁺ is even more pronounced with amine ligands than with carboxylate-containing ligands like EDTA. A pure polyamine should therefore show a Δlog K at the upper end of (or exceeding) the 22–25 range observed for mixed N/O donors.

---

### Summary

The SRD-46 data unambiguously demonstrate that Co³⁺ forms complexes that are **10²²–10²⁵ times more stable** than the corresponding Co²⁺ complexes. This extraordinary difference — among the largest oxidation-state effects in the periodic table — arises from the synergy of higher ionic charge and the uniquely favorable d⁶ low-spin electronic configuration. A new polydentate amine ligand would be predicted to follow this same pattern, with the stability gap likely at or above 25 log units for a hexadentate system, making such complexes among the most thermodynamically and kinetically stable in aqueous coordination chemistry.

---