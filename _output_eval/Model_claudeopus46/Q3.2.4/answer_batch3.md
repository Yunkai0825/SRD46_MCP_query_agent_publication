# Survey of Fe(II) and Fe(III) Ligand Systems in NIST SRD-46

## Database Coverage

| Metal | Ligand partners | β-definitions | VLM measurements |
|-------|----------------|---------------|------------------|
| **Fe³⁺** (metal_61) | 406 | 128 | 1 473 |
| **Fe²⁺** (metal_62) | 217 | 57 | 667 |

Fe(III) has roughly twice the data coverage, reflecting its greater importance in environmental, biological, and industrial chemistry.

---

## Representative Stability Constants (log β, 25 °C, aqueous)

### Fe(III) — Hard Acid (d⁵ high-spin)

| Ligand | Class / Donor set | log β₁ | Higher βₙ | I (M) |
|--------|-------------------|--------|-----------|-------|
| EDTA⁴⁻ | Polyaminocarboxylate (N₂O₄) | **25.1** | — | 0.1 |
| NTA³⁻ | Aminocarboxylate (NO₃) | **15.9** | — | 0.1 |
| CN⁻ | Pseudohalide (C-donor) | — | log β₆ = **43.6** | 0 |
| 8-Hydroxyquinoline | Mixed N,O chelate | **12.2–13.7** | — | 0–1 |
| OH⁻ | Hard O-donor | **11.81** | β₃ = 29.67 | 0–3 |
| Citrate³⁻ | Hydroxy-tricarboxylate (O₄) | **11.5** | — | 0.1 |
| Phenolate | O-donor | **10.47** | — | 0.1 |
| Hydroxamic acid (dihydroxamate) | O,O chelate | **10.53** | β₂ = 19.63 | 0.1 |
| Oxalate²⁻ | Dicarboxylate (O₂) | **7.53** | β₃ = 18.49 | 1 |
| Fluoride⁻ | Hard halide | **5.18** | β₃ = 11.87 | 0.5 |
| Azide⁻ | Pseudohalide | **4.65** | β₄ = 13.83 | 1 |
| Acetate⁻ | Monocarboxylate (O) | **3.38** | — | 1 |
| SCN⁻ | Ambidentate (N/S) | **3.03** | — | 0 |
| Cl⁻ | Soft halide | **1.48** | — | 0–1 |

### Fe(II) — Borderline Acid (d⁶)

| Ligand | Class / Donor set | log β₁ | Higher βₙ | I (M) |
|--------|-------------------|--------|-----------|-------|
| DTPA⁵⁻ | Polyaminocarboxylate (N₃O₅) | **16.55** | — | 0.1 |
| CyDTA⁴⁻ | Polyaminocarboxylate (N₂O₄) | **16.2** | — | 0.1 |
| BAL (dimercaptopropanol) | Dithiol (S₂) | **14.97** | β₂ = 24.67 | 0.1 |
| EDTA⁴⁻ | Polyaminocarboxylate (N₂O₄) | **14.33** | — | 0.1 |
| Tris(2-pyridylmethyl)amine | Polypyridyl-amine (N₄) | **11.1** | — | 0.1 |
| Triethylenetetramine | Polyamine (N₄) | **7.7** | — | 0.1 |
| Terpyridine | Polypyridyl (N₃) | **7.1** | β₂ = 13.8 | 0.1–0.5 |
| 1,10-Phenanthroline | Diimine (N₂) | **5.85** | β₃ = **21.3** | 0–0.1 |
| Diethylenetriamine | Polyamine (N₃) | **5.8** | — | 1 |
| CN⁻ | Pseudohalide (C-donor) | — | log β₆ = **35.4** | 0 |
| 2,2′-Bipyridyl | Diimine (N₂) | **4.2** | β₃ = **17.45** | 0–1 |
| OH⁻ | Hard O-donor | **4.5** | — | 0 |

---

## Key Trends and Thermodynamic Reasoning

### 1. Hard/Soft Acid–Base (HSAB) Dichotomy

The most striking pattern is the **reversal of ligand-class preference** between the two oxidation states:

- **Fe(III)** is a **hard acid** (high charge density, d⁵). It strongly prefers hard O-donors: OH⁻ (log β₁ ≈ 11.8), phenolate (10.5), hydroxamate (10.5), catecholate, and F⁻ (5.2) all bind far more strongly to Fe³⁺ than to Fe²⁺. The EDTA gap is enormous: **log β = 25.1 vs. 14.3** — a factor of ~10¹⁰·⁸ in binding affinity, driven largely by the stronger electrostatic interaction of the tripositive cation with anionic carboxylate oxygens.

- **Fe(II)** is a **borderline-to-soft acid** (lower charge, larger ionic radius, d⁶). It shows enhanced affinity for soft/borderline N- and S-donors: bipyridyl, phenanthroline, thiolates (BAL: log β₁ ≈ 15.0), and cyanide. The Fe(II)–phen system (β₃ = 21.3) is the basis of the classic ferroin indicator.

- **OH⁻ comparison** crystallizes the HSAB effect: Fe(III)–OH⁻ log β₁ = 11.8 vs. Fe(II)–OH⁻ log β₁ = 4.5 — a 7.3 log-unit gap driven purely by charge density matching with the hard hydroxide donor.

### 2. Chelate Effect and Denticity

Across both oxidation states, **multidentate ligands dramatically outperform monodentate ones**:

| Comparison (Fe³⁺) | Denticity | log β₁ |
|------------|-----------|--------|
| Acetate (monodentate O) | 1 | 3.4 |
| Oxalate (bidentate O₂) | 2 | 7.5 |
| Citrate (tri/tetradentate O₃/O₄) | 3–4 | 11.5 |
| NTA (tetradentate NO₃) | 4 | 15.9 |
| EDTA (hexadentate N₂O₄) | 6 | 25.1 |

Each additional chelate ring adds roughly **3–5 log units**, reflecting the entropic advantage (fewer translational degrees of freedom lost upon complexation) and reduced strain of pre-organized donors. The same trend holds for Fe(II): dien (N₃, 5.8) → trien (N₄, 7.7) → tris(pyridylmethyl)amine (N₄, 11.1) → EDTA (N₂O₄, 14.3) → DTPA (N₃O₅, 16.6).

### 3. Crystal-Field / Ligand-Field Stabilization Energy (LFSE)

- **Fe(II) d⁶ with strong-field N-donors**: Polypyridyl and cyanide ligands induce a **low-spin** configuration in Fe(II), gaining substantial LFSE (−2.4 Dq for low-spin d⁶ vs. −0.4 Dq for high-spin). This explains the **cooperative stepwise binding** seen in Fe(II)–phen: log K₁ = 5.85, log K₂ ≈ 5.60, log K₃ ≈ 9.85 — the third ligand benefits from the spin-crossover to a fully low-spin t₂g⁶ state, giving an anomalously large K₃.

- **Fe(III) d⁵ high-spin** has **zero LFSE** regardless of field strength (all five d-orbitals singly occupied), so there is no crystal-field bonus for strong-field ligands. This is why Fe(III)–bipyridyl complexes are relatively weak and rarely studied, while Fe(II)–bipyridyl is iconic.

- **Hexacyanoferrate**: Both oxidation states form [Fe(CN)₆]ⁿ⁻, but Fe(III) has the higher cumulative β₆ (43.6 vs. 35.4). Cyanide is both a strong σ-donor and π-acceptor; the higher charge of Fe³⁺ enhances σ-bonding, and the d⁵ → low-spin transition still yields significant LFSE (−2.0 Dq). The 8-log-unit gap also reflects the greater electrostatic stabilization of the +3 cation surrounded by six anionic ligands.

### 4. Notable Edge Cases

| System | Observation | Explanation |
|--------|-------------|-------------|
| **Fe(III)–SCN⁻** (log β₁ = 3.0) | Surprisingly weak for a classic qualitative test | SCN⁻ is a soft/borderline ligand; the blood-red color is intense (ε ≈ 5000 M⁻¹cm⁻¹) but the equilibrium constant is modest — the test works because of high molar absorptivity, not high stability. |
| **Fe(II)–BAL** (log β₁ = 15.0) | Rivals EDTA despite being only bidentate | Thiolate S⁻ is an excellent soft donor for borderline Fe²⁺; the high basicity of thiolate (pKₐ ≈ 10) contributes a large intrinsic affinity. This is a dramatic illustration of HSAB matching. |
| **Fe(III)–OH⁻** vs. **Fe(II)–OH⁻** | 7.3 log-unit gap | Pure HSAB + electrostatic effect: the +3 charge strongly polarizes the hard hydroxide. This drives Fe(III) hydrolysis at much lower pH. |
| **Fe(III)–phenolate** (10.5) | Very high for a monodentate ligand | Phenolate is a hard, anionic O-donor with π-donation capability into the Fe(III) t₂g orbitals; this interaction underpins siderophore chemistry (catecholate/hydroxamate). |
| **Fe(II)–phen β₃ cooperativity** | K₃ > K₁ | Spin-state change at the third ligand addition (high-spin → low-spin crossover) provides an extra ~4 log units of LFSE-driven stabilization — a textbook anomaly. |

### 5. Biological & Environmental Relevance

The data rationalize why nature uses **catecholate and hydroxamate siderophores** to scavenge Fe(III) from the environment (exploiting the hard–hard match and chelate effect to achieve log β > 30 for hexadentate siderophores like enterobactin), while **heme and iron–sulfur clusters** preferentially stabilize Fe(II) through softer N- and S-donor environments. The enormous difference in EDTA binding (Δlog β ≈ 10.8) is also the thermodynamic basis for using EDTA to sequester Fe(III) in water treatment and food preservation.

---

## Summary

The SRD-46 data for iron systems beautifully illustrate three interlocking principles:

1. **HSAB theory** governs the oxidation-state selectivity: Fe(III) favors O-donors; Fe(II) favors N- and S-donors.
2. **The chelate effect** provides a roughly additive 3–5 log β per ring, making polydentate ligands (EDTA, siderophores, polypyridyls) dominant in both oxidation states.
3. **LFSE/spin-state effects** uniquely enhance Fe(II) complexes with strong-field ligands (phen, bpy, CN⁻), producing cooperative binding and spin-crossover phenomena absent in the LFSE-null d⁵ Fe(III).

**Source:** All numeric values from NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes). Conditions as noted (25 °C unless stated, aqueous solution).

---