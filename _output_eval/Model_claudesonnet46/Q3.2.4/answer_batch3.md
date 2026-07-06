Based on all data retrieved, I'll now synthesize the comprehensive survey.

---

# Fe(II) & Fe(III) Ligand Systems in SRD-46: Stability Constant Survey

## 1. Database Coverage

| Metal | metal_id | Charge | β-definitions | Ligand partners | VLMs |
|-------|----------|--------|---------------|-----------------|------|
| Fe(III) | metal_61 | +3 | 128 | 406 | ~1473 |
| Fe(II) | metal_62 | +2 | 57 | 217 | ~667 |

Fe(III) dominates the database — roughly **2× more ligand partners and 2.3× more β-definitions** than Fe(II) — reflecting its greater thermodynamic stability in aqueous coordination chemistry and the historical focus of analytical/environmental research on Fe³⁺ speciation.

---

## 2. Representative Systems by Ligand Class

### Fe(III) — metal_61

| Ligand Class | Representative Ligand | Denticity | Approx. log β (ML or MLn) | Notes |
|---|---|---|---|---|
| Hard halide | F⁻ | 1 | ~6 (ML₃ ~12) | Hard–hard; F⁻ >> Cl⁻ |
| Hard halide | Cl⁻ | 1 | ~1.4 | Weak electrostatic only |
| Pseudohalide | SCN⁻ | 1 | ~3 | Soft donor on hard Fe³⁺; weak |
| Pseudohalide | N₃⁻ | 1 | moderate | π-donor; borderline |
| Simple O-donor | Acetate | 1 | ~3–4 | Monodentate; low β |
| Chelate O-donor | Malonate | 2 | ~7 | 5-membered ring |
| Chelate O-donor | Salicylate | 2 | ~16 | Phenolate + carboxylate |
| Catecholate | Tiron | 2 | ~20 (ML₃ ~43) | Strongest O-donor class |
| Hydroxide | OH⁻ | 1 | very high | Hydrolysis dominant; forms FeOOH, Fe₂O₃ |
| Aminocarboxylate | NTA | 4 | ~15 | Tetradentate N+O |
| Aminopolycarboxylate | EDTA | 6 | ~25 | Hexadentate; large chelate effect |
| Aminopolycarboxylate | CDTA | 6 | ~27 | Rigid cyclohexyl; highest in class |

### Fe(II) — metal_62

| Ligand Class | Representative Ligand | Denticity | Approx. log β (ML or MLn) | Notes |
|---|---|---|---|---|
| Simple N-donor | NH₃ | 1 | low–moderate | Weak; Fe²⁺ not strongly N-basic |
| Bidentate N-donor | Ethylenediamine (en) | 2 | moderate | Chelate effect active |
| Aromatic N-donor | 2,2′-Bipyridyl (bipy) | 2 | high (ML₃ dominant) | π-backbonding; Fe²⁺ soft character |
| Aromatic N-donor | 1,10-Phenanthroline (phen) | 2 | high (ML₃ dominant) | Rigid; stronger than bipy |
| Aromatic N-donor | 5-Me-phen | 2 | high | Methyl enhances π-donation |
| Mixed N/O | Glycine | 2 | ~4–5 (ML) | Amino acid; moderate |
| Mixed N/O | Serine, Threonine | 2 | ~4–5 | Similar to glycine |
| Hydroxy acid | Citrate | 3–4 | ~5–7 | Multidentate; moderate |
| Aminopolycarboxylate | NTA | 4 | ~8–10 | Lower than Fe(III) |
| Aminopolycarboxylate | DTPA | 8 | high | Octadentate; large chelate |
| Phosphonate | 2,6-PDPA | 4 | high | Pyridyl + phosphonate |

---

## 3. Stability Constant Trends Across Ligand Classes

### Ordering for Fe(III) (hard acid, charge +3, r = 0.65 Å)

```
OH⁻ ≫ Catecholate > Hydroxamate ≈ CDTA > EDTA > Salicylate > NTA > Malonate > F⁻ > Oxalate > Acetate > N₃⁻ > SCN⁻ > Cl⁻
```

### Ordering for Fe(II) (borderline acid, charge +2, r = 0.78 Å)

```
Phen > Bipy > DTPA > Polypyridyl hydrazone > NTA > Citrate > Glycine ≈ Amino acids > NH₃ > Phosphate
```

---

## 4. Thermodynamic Reasoning

### A. Hard–Soft Acid–Base (HSAB) Theory

**Fe(III)** is a **hard acid** (high charge, small radius, low polarizability). It forms its strongest bonds with **hard donors**: O⁻ (phenolate, catecholate, hydroxamate, hydroxide) and F⁻. The log β hierarchy F⁻ >> Cl⁻ >> SCN⁻ (thiocyanate) is a textbook HSAB demonstration — soft S-donor SCN⁻ is poorly matched to hard Fe³⁺.

**Fe(II)** is a **borderline-to-soft acid** (lower charge, larger radius, more polarizable d⁶ center). It shows markedly higher affinity for **N-donors**, especially aromatic π-systems (bipy, phen), where **metal-to-ligand π-backbonding** (Fe²⁺ d → ligand π*) provides additional stabilization unavailable to Fe³⁺ (which is d⁵, high-spin, poor π-donor).

### B. Chelate Effect

Multidentate ligands show dramatically enhanced stability over monodentate analogues due to the **chelate effect** (favorable ΔS from release of water molecules). The progression is clear for Fe(III):

| Denticity | Example | log β |
|---|---|---|
| 1 | Acetate | ~3–4 |
| 2 | Malonate | ~7 |
| 2 | Salicylate | ~16 |
| 2 | Catecholate (Tiron) | ~20 |
| 4 | NTA | ~15 |
| 6 | EDTA | ~25 |
| 6 | CDTA | ~27 |

Each additional chelate ring contributes ~3–5 log units. CDTA > EDTA despite identical donor set because the rigid cyclohexyl backbone pre-organizes the ligand, reducing the entropic cost of binding (macrocyclic/preorganization effect).

### C. Crystal-Field / Ligand-Field Considerations

Fe(II) d⁶ with strong-field N-donors (bipy, phen) undergoes **low-spin conversion**, gaining **crystal-field stabilization energy (CFSE)** of ~2.4 Δₒ for t₂g⁶ vs. ~0.4 Δₒ for high-spin d⁶. This extra ~2 Δₒ stabilization (~40–80 kJ/mol) is a major contributor to the exceptionally high log β values for Fe(II)–phen₃ and Fe(II)–bipy₃ complexes (log β₃ > 17). Fe(III) d⁵ high-spin has **zero CFSE** in octahedral fields, so it cannot exploit this stabilization — explaining why Fe(III) does not form comparably stable polypyridyl complexes.

### D. Charge Density and Electrostatics

Fe(III) (+3, r = 0.65 Å) has a **charge density ~2.5× higher** than Fe(II) (+2, r = 0.78 Å). This drives the enormous preference of Fe³⁺ for anionic O-donors (catecholate, hydroxamate, phenolate) where charge–charge attraction is maximized. The log β for Fe(III)–catecholate (ML₃ ~43) vs. Fe(II)–catecholate (much lower) illustrates this perfectly.

### E. Edge Cases

| Edge Case | Explanation |
|---|---|
| Fe(III)–SCN⁻ is weak (log β₁ ~3) despite SCN⁻ being a decent ligand for other metals | Hard–soft mismatch; Fe³⁺ is a hard acid, SCN⁻ is a soft/borderline donor |
| Fe(II)–phen₃ is exceptionally stable (log β₃ > 17) | Low-spin d⁶ CFSE + π-backbonding; kinetically inert |
| CDTA > EDTA for Fe(III) despite same donors | Preorganization/macrocyclic-like rigidity lowers ΔH‡ and improves ΔS of binding |
| Fe(III) hydrolysis dominates at pH > 3 | OH⁻ is the ultimate hard donor; competes with all other ligands |
| Fe(II)–citrate is moderate despite multidentate | Citrate is an O-only donor; Fe²⁺ prefers N-donors; also redox instability |

---

## 5. Summary Table: Fe(III) vs. Fe(II) Class Comparison

| Ligand Class | Fe(III) log β (typical) | Fe(II) log β (typical) | Δ log β (III–II) | Dominant Factor |
|---|---|---|---|---|
| Catecholate (O,O) | ~20–43 | low | >> | Hard–hard; charge density |
| Hydroxamate (O,O) | ~18–25 | low | >> | Hard–hard |
| Aminopolycarboxylate (N,O) | ~25–27 | ~8–16 | ~10–15 | Chelate + charge |
| Salicylate (O,O) | ~16 | low | >> | Phenolate hard donor |
| Fluoride | ~6 | ~1 | ~5 | Hard–hard |
| Aromatic N-donor (bipy/phen) | low | ~17–21 | << | CFSE + π-backbonding |
| Aliphatic N-donor (en, NH₃) | low | moderate | < | Borderline character of Fe²⁺ |
| Chloride | ~1.4 | ~0.5 | ~1 | Both weak; electrostatic |
| Thiocyanate | ~3 | ~1 | ~2 | Hard–soft mismatch for Fe³⁺ |

---

## Key Takeaways

1. **Fe(III) strongly prefers hard O-donors** (catecholate ≫ hydroxamate > salicylate > carboxylate > F⁻ ≫ Cl⁻ > SCN⁻), driven by charge density and HSAB hard–hard matching.
2. **Fe(II) strongly prefers aromatic N-donors** (phen > bipy >> en > NH₃), driven by crystal-field stabilization energy (low-spin d⁶) and π-backbonding.
3. **The chelate effect amplifies both**: multidentate ligands gain 3–5 log units per additional chelate ring, with preorganized ligands (CDTA, macrocycles) gaining extra entropy advantage.
4. **Hydrolysis is the dominant Fe(III) reaction** above pH 3, making OH⁻ the de facto strongest competitor for all other ligands.
5. **The Fe(II)/Fe(III) redox couple** means that ligand choice can shift the reduction potential by hundreds of mV — ligands stabilizing Fe(III) (catecholates, hydroxamates) lower E°, while those stabilizing Fe(II) (phen, bipy) raise it, with profound implications for biological iron transport (siderophores use hydroxamates/catecholates) and analytical chemistry (ferroin uses phen).

*Source: NIST SRD-46 Critically Selected Stability Constants of Metal Complexes Database.*

---