# Calcium Oxalate Precipitation pH — Estimation from SRD-46 Data

## Thermodynamic Data (SRD-46)

| Parameter | Value | Notes |
|-----------|-------|-------|
| pKa₁ (H₂C₂O₄ → HC₂O₄⁻ + H⁺) | **~1.2** | Very strong first dissociation |
| pKa₂ (HC₂O₄⁻ → C₂O₄²⁻ + H⁺) | **~3.8** | Second dissociation |
| log K_f (Ca²⁺ + C₂O₄²⁻ → CaC₂O₄(aq)) | **~3.0** | beta_def_812, 6 entries, 25 °C |
| log K_sp (CaC₂O₄·H₂O(s) ⇌ Ca²⁺ + C₂O₄²⁻) | **~−8.6** | beta_def_327 (monohydrate), 9 entries, 25 °C |

*(pKa values from the ligand bracket data; Ksp and Kf from the Ca²⁺–oxalate system catalog containing 17 total entries across 3 beta definitions.)*

## Calculation

Precipitation occurs when the ion product exceeds the solubility product:

**[Ca²⁺] · [C₂O₄²⁻] > K_sp ≈ 10⁻⁸·⁶**

The fraction of total oxalate present as the fully deprotonated C₂O₄²⁻ ion (α₂) depends on pH:

**α₂ = 1 / (1 + 10^(pKa₂ − pH) + 10^(pKa₁ + pKa₂ − 2·pH))**

| pH | α₂ (fraction as C₂O₄²⁻) | Comment |
|----|--------------------------|---------|
| 2.0 | ~0.006 | Mostly H₂C₂O₄ |
| 3.0 | ~0.14 | Rising HC₂O₄⁻ |
| 3.8 | ~0.50 | Half-point (= pKa₂) |
| 5.0 | ~0.94 | Nearly all C₂O₄²⁻ |
| 7.0 | ~1.00 | Fully deprotonated |

At typical laboratory or physiological concentrations (~1–5 mM Ca²⁺, ~0.1–1 mM total oxalate):

- **pH < 3:** α₂ is very small, so [C₂O₄²⁻] stays well below the level needed to exceed Ksp — the solution remains undersaturated.
- **pH ≈ 3.5–4.5:** α₂ rises steeply (crossing 0.5 at pH = pKa₂ ≈ 3.8), and the ion product begins to approach or exceed Ksp.
- **pH > 4.5–5:** Essentially all oxalate is deprotonated, and precipitation becomes thermodynamically very favorable.


> **Calcium oxalate precipitation becomes significant at approximately pH 4–5**, roughly around and just above the second pKa of oxalic acid (~3.8). Below pH ~3, the oxalate is predominantly protonated (as H₂C₂O₄ or HC₂O₄⁻), keeping the free C₂O₄²⁻ concentration too low to exceed the very small Ksp (~10⁻⁸·⁶). Once pH rises past ~4, the oxalate dianion concentration increases dramatically, driving precipitation.

### Clinical and Practical Relevance

This is why **calcium oxalate kidney stones** form readily at the near-neutral pH of urine (pH 5.5–7). Even modest oxalate concentrations at urinary pH produce ion products far exceeding Ksp. Acidifying urine below pH 4 would theoretically prevent CaOx precipitation, but this is not physiologically achievable — hence the clinical challenge of oxalate stone disease. In industrial settings (e.g., gravimetric analysis), calcium oxalate is precipitated from mildly acidic to neutral solutions (pH 4–6) for exactly this reason.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes)*

---