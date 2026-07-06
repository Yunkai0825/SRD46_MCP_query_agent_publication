I now have all the data needed. Let me compile the final answer.

---

# The Chelate Effect: Ethylenediamine vs. Ammonia across Cu²⁺, Ni²⁺, and Zn²⁺

## Raw Data (25 °C, I = 0 M, aqueous)

All values are stepwise log K₁ for the reaction **M + L ⇌ ML** (beta_def_812) from NIST SRD-46.

| Metal | log K₁(en) | vlm_id | log K₁(NH₃) | vlm_id | 2·log K₁(NH₃) | **Δ = log K₁(en) − 2·log K₁(NH₃)** |
|-------|-----------|--------|-------------|--------|---------------|--------------------------------------|
| **Cu²⁺** | 10.50 | vlm_122418 | 4.02 | vlm_173246 | 8.04 | **+2.46** |
| **Ni²⁺** | 7.32 | vlm_122371 | 2.72 | vlm_173185 | 5.44 | **+1.88** |
| **Zn²⁺** | 5.66 | vlm_122515 | 2.21 | vlm_173397 | 4.42 | **+1.24** |

> All entries at 25 °C, I = 0 M, aqueous solution, with L defined as the neutral (unprotonated) ligand.

## Thermodynamic Breakdown (where available)

| Metal | Ligand | ΔH (kJ/mol) | ΔS (J/mol·K) | Conditions |
|-------|--------|-------------|--------------|------------|
| Cu²⁺ | en | −52.7 | +22.6 | 25 °C, I = 0.1 M |
| Cu²⁺ | NH₃ | −20.1 | +9.6 | 25 °C, I = 0 M |
| Ni²⁺ | en | ~0 | +9.2 | 25 °C, I = 0.1 M |
| Ni²⁺ | NH₃ | −15.1 | +1.7 | 25 °C, I = 0 M |
| Zn²⁺ | NH₃ | −10.9 | +9.6 | 27 °C, I = 2 M |

## Key Finding: The Chelate Effect Varies Significantly

The chelate enhancement Δ is **not constant** across the three metals:

| Metal | Δ (log units) |
|-------|--------------|
| Cu²⁺ | **+2.46** |
| Ni²⁺ | **+1.88** |
| Zn²⁺ | **+1.24** |

The chelate effect is largest for Cu²⁺ and smallest for Zn²⁺, spanning a range of ~1.2 log units — a factor of ~16 in equilibrium constant.

## Hypothesis for the Variation

Several factors likely contribute to the metal-dependent magnitude of the chelate effect:

1. **Crystal-field stabilisation and Jahn–Teller effects (Cu²⁺).** Cu²⁺ (d⁹) undergoes a strong Jahn–Teller distortion that creates a pronounced preference for equatorial coordination. Ethylenediamine, as a chelate, locks both donor atoms in the favoured equatorial plane, maximising the CFSE gain. Two separate NH₃ molecules have a statistical probability of occupying axial (weaker) positions, so the chelate gains a disproportionate advantage. This amplifies Δ for Cu²⁺ beyond the "pure" entropic chelate effect.

2. **Entropic contribution scales with binding strength.** The classical entropic chelate effect (release of a "free" solvent/ligand particle upon chelation) contributes roughly the same ΔS bonus for all metals. However, the thermodynamic data show that the **enthalpic** contribution differs markedly: Cu²⁺–en has a very large favourable ΔH (−52.7 kJ/mol vs. 2 × −20.1 = −40.2 kJ/mol for two NH₃), giving an extra ~12 kJ/mol enthalpic bonus. For Ni²⁺, the en ΔH is near zero while NH₃ binding is exothermic, meaning the chelate effect for Ni²⁺ is almost entirely entropy-driven.

3. **Ring-strain and metal-ion size matching.** The five-membered chelate ring formed by en has an optimal bite angle that matches Cu²⁺ and Ni²⁺ (ionic radii ~0.57–0.69 Å) better than the slightly larger Zn²⁺ (0.74 Å, tetrahedral preference). Zn²⁺ also favours tetrahedral geometry, where the geometric constraint of the chelate ring is less advantageous compared to octahedral metals, reducing the enthalpic bonus.

4. **Irving–Williams series correlation.** The ordering Cu > Ni > Zn for Δ mirrors the Irving–Williams series, suggesting that the same factors governing absolute complex stability (ligand-field effects, ionic radius, electronegativity) also modulate the *relative* advantage of chelation.

## Conclusion

The chelate effect is **real and significant for all three metals** (Δ = +1.2 to +2.5 log units), but its magnitude is **metal-dependent**, not a universal constant. Cu²⁺ shows the largest chelate enhancement (~2.5 log units, a factor of ~300), driven by both entropic and substantial enthalpic contributions linked to Jahn–Teller-favoured equatorial chelation. Zn²⁺ shows the smallest enhancement (~1.2 log units, factor of ~17), consistent with its tetrahedral preference and poorer geometric match to the en chelate ring.

---

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes). All log K values are stepwise K₁ at 25 °C, I = 0 M, aqueous solution.*

---