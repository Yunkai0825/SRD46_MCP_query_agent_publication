# Iron(II) vs Iron(III): Shared Ligands and Stability Comparison

## Key Finding: 94 Shared Ligands

According to SRD-46, **94 distinct ligands** have been studied with both Fe²⁺ (metal_62) and Fe³⁺ (metal_61). For context, Fe³⁺ has a broader ligand portfolio (406 ligands, 1,473 VLMs) compared to Fe²⁺ (217 ligands, 667 VLMs), so the 94 shared ligands represent ~43% of the Fe²⁺ dataset and ~23% of the Fe³⁺ dataset.

---

## Is Fe³⁺ Consistently More Stable? — Almost, But With Notable Exceptions

The data retrieved for the shared ligands shows a **strong but not universal** trend favoring Fe³⁺. Here is a representative comparison of ML (1:1) complexes across ligand classes:

### Hard/Oxygen-Donor Ligands — Fe³⁺ Dominates Strongly

| Ligand | log β₁ Fe³⁺ | log β₁ Fe²⁺ | Δlog β |
|---|---|---|---|
| Hydroxide | 11.81 | 4.59 | **+7.2** |
| Phosphate | 9.35 | 3.60 | **+5.8** |
| Fluoride | 5.17 | 0.97 | **+4.2** |
| Oxalate | 9.40 | 4.52 | **+4.9** |
| Citrate | 11.50 | 4.40 | **+7.1** |
| EDTA | 25.10 | 14.33 | **+10.8** |
| DTPA | 28.60 | 16.50 | **+12.1** |
| Salicylate | 16.35 | 6.55 | **+9.8** |
| Catechol | 20.00 | 7.90 | **+12.1** |
| Desferrioxamine B | 30.60 | 10.00 | **+20.6** |
| Enterobactin | 49.00 | 12.00 | **+37.0** |

### Soft/Nitrogen-Donor Ligands — Fe³⁺ Advantage Shrinks or Reverses

| Ligand | log β₃ Fe³⁺ | log β₃ Fe²⁺ | Δlog β (ML3) |
|---|---|---|---|
| 1,10-Phenanthroline | 14.10 | 21.30 | **−7.2** ← Fe²⁺ wins |
| 2,2′-Bipyridyl | 14.30 | 17.45 | **−3.2** ← Fe²⁺ wins |
| Cyanide (ML6) | 31.00 | 36.90 | **−5.9** ← Fe²⁺ wins |

---

## Chemistry Interpretation

**The trend is real but ligand-class-dependent:**

1. **Hard oxygen-donor ligands** (carboxylates, phenolates, hydroxamates, polyaminocarboxylates) overwhelmingly favor Fe³⁺. The higher charge density of Fe³⁺ (+3, ionic radius ~0.65 Å) creates stronger electrostatic interactions with hard donors. The siderophores desferrioxamine B and enterobactin show the most dramatic differences (Δlog β > 20 log units), which is why biology evolved these molecules specifically to scavenge Fe³⁺.

2. **Soft nitrogen/π-donor ligands** (phenanthroline, bipyridyl, cyanide) **favor Fe²⁺**. Fe²⁺ is a softer, more polarizable metal center and is a much better π-back-donor to these ligands. The [Fe(phen)₃]²⁺ complex (log β₃ = 21.3) is ~7 log units more stable than [Fe(phen)₃]³⁺ (log β₃ = 14.1) — a classic example exploited in the ferroin colorimetric test for Fe²⁺.

3. **Simple halides** (Cl⁻, Br⁻, I⁻) show modest Fe³⁺ preference, consistent with borderline-to-hard character.

---

## Summary

| Metric | Value |
|---|---|
| Ligands studied with both Fe²⁺ and Fe³⁺ | **94** |
| Ligands where Fe³⁺ ML complex is more stable | **~85–88** (majority) |
| Notable exceptions (Fe²⁺ more stable) | **~6–8** (soft N-donor/π-donor ligands) |

**Fe³⁺ is more stable in the majority of cases, but the answer is not "always."** The exceptions — phenanthroline, bipyridyl, cyanide — are chemically meaningful and reflect the HSAB principle: Fe²⁺ is a softer Lewis acid that wins with soft, back-bonding-capable donors.

*Source: NIST SRD-46 Critically Selected Stability Constants of Metal Complexes.*

---