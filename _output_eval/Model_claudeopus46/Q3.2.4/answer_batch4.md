Based on the comprehensive data retrieved from SRD-46, here is the survey and analysis.

---

# Fe(II) vs Fe(III) Ligand Systems in NIST SRD-46: Stability Trends & Thermodynamic Rationale

## Database Coverage

| Metal | Charge | Ligand Systems | VLM Records | β-Definitions |
|-------|--------|---------------|-------------|---------------|
| Fe(III) | +3 | 406 | 1,473 | 128 |
| Fe(II) | +2 | 217 | 667 | 57 |

Fe(III) has roughly **twice** the coverage of Fe(II), reflecting its greater importance in environmental, biological, and industrial chemistry.

---

## Representative ML Stability Constants (log β₁, 20–30 °C, I = 0–1 M)

### Fe(III) — Ranked by Average log β₁

| Ligand Class | n | Avg log β₁ | Range | Dominant Donors |
|---|---|---|---|---|
| Catechols | 42 | **19.6** | 12.1–44.0 | O⁻ (phenolate) |
| Hydroxamic acids | 54 | **11.2** | 4.5–28.7 | O⁻ (hydroxamate) |
| Phenols / salicylic acids | 35 | **10.8** | 3.5–16.3 | O⁻ (phenolate/carboxylate) |
| Phenols | 10 | **10.8** | 6.3–16.3 | O⁻ |
| Naphthols | 8 | **10.3** | 5.0–15.0 | O⁻ |
| Hydroxy-diacids | 8 | **9.7** | 3.0–15.2 | O⁻ (carboxylate/hydroxyl) |
| Pyridine carboxylic acids | 3 | **9.0** | 7.0–11.0 | N/O |
| Cyclic ketones | 14 | **8.7** | 5.0–11.4 | O |
| Polycarboxylic acids | 15 | **8.1** | 3.0–11.4 | O⁻ |
| Amino acids | 40 | **7.9** | 3.4–12.0 | N/O⁻ |
| Dicarboxylic acids | 14 | **7.5** | 3.0–10.0 | O⁻ |
| Aliphatic amines | 5 | **5.8** | 3.4–10.2 | N |
| Carboxylic acids (mono) | 20 | **3.9** | 1.4–7.3 | O⁻ |
| Inorganic ligands | 43 | **3.5** | −1.5–14.0 | F⁻, Cl⁻, SO₄²⁻, etc. |

### Fe(II) — Ranked by Average log β₁

| Ligand Class | n | Avg log β₁ | Range | Dominant Donors |
|---|---|---|---|---|
| Phenanthrolines | 15 | **6.0** | 4.1–7.1 | N (aromatic) |
| Bipyridines | 14 | **4.5** | 3.4–5.8 | N (aromatic) |
| Amino acids | 25 | **4.0** | 1.5–8.5 | N/O⁻ |
| Pyridines | 4 | **3.4** | 2.2–4.3 | N |
| Aliphatic amines | 3 | **3.1** | 2.1–4.2 | N |
| Carboxylic acids (poly) | 7 | **2.9** | 1.3–4.7 | O⁻ |
| Inorganic ligands | 20 | **1.3** | −0.2–6.5 | Cl⁻, F⁻, etc. |

---

## Key Trends and Thermodynamic Reasoning

### 1. Hard/Soft Acid–Base (HSAB) Theory — The Dominant Trend

Fe(III) (d⁵, high charge density) is a **hard Lewis acid**. Its strongest complexes are with **hard, anionic oxygen donors**: catecholates (avg log β₁ ≈ 20), hydroxamates (≈ 11), and phenolates/salicylates (≈ 11). These ligands provide charge-dense O⁻ donors that match Fe(III)'s high charge-to-radius ratio.

Fe(II) (d⁶, lower charge density) is a **borderline acid**. Its strongest ML complexes are with **borderline/soft nitrogen donors**: phenanthrolines (≈ 6.0) and bipyridines (≈ 4.5) — aromatic N-heterocycles that can accept π-back-donation from Fe(II)'s filled t₂g orbitals.

> **The HSAB crossover is stark**: Fe(III)–catecholate (log β₁ ≈ 20) dwarfs Fe(II)–catecholate, while Fe(II)–phenanthroline (log β₁ ≈ 6) far exceeds Fe(III)–phenanthroline. This is the single most important organizing principle.

### 2. Crystal-Field Stabilization Energy (CFSE)

- **Fe(II) + strong-field N-donors** (phen, bipy): Fe(II) d⁶ in an octahedral strong field adopts a **low-spin t₂g⁶** configuration with maximum CFSE (−24 Dq). This provides an extra thermodynamic driving force for Fe(II)–polypyridyl complexes and explains why [Fe(phen)₃]²⁺ is famously stable and kinetically inert.
- **Fe(III) d⁵**: In a weak O-donor field, Fe(III) is high-spin (t₂g³ eg²) with zero LFSE, so its stability is driven purely by electrostatics and covalency — hence the dominance of multiply-charged anionic O-donors.

### 3. The Chelate Effect

The data clearly shows chelating ligands outperforming monodentate analogues within each donor class:

| Comparison | Avg log β₁ |
|---|---|
| Fe(III) + catechol (bidentate O,O) | ~20 |
| Fe(III) + simple phenol (monodentate O) | ~11 |
| Fe(III) + monocarboxylate | ~4 |
| Fe(III) + polycarboxylate (multidentate) | ~8 |

The entropic advantage of ring closure (ΔS > 0 upon chelation) systematically boosts stability by several log units. EDTA-class and NTA-class hexadentate/pentadentate aminocarboxylates (well-represented in both Fe(II) and Fe(III) systems) are expected to show the highest cumulative β values in the database.

### 4. Macrocyclic Effect

Fe(II) has notable coverage of **aza-macrocycles** (16 systems), **aza-oxa-macrocycles** (15), and **aza-thia-macrocycles** (4). The pre-organized cavity of macrocyclic ligands provides an additional enthalpic and entropic boost beyond the chelate effect, particularly for Fe(II) with N-donor macrocycles (porphyrins, cyclams) — biologically critical in hemoglobin and cytochromes.

### 5. Edge Cases and Anomalies

| Observation | Explanation |
|---|---|
| **Fe(III)–catechol range 12–44 log units** | The enormous spread reflects siderophore-type hexadentate tris-catecholates (e.g., enterobactin, log β ≈ 44–49) vs. simple catechol. These are nature's Fe(III) scavengers. |
| **Fe(III)–hydroxamate range 4.5–28.7** | Same pattern: desferrioxamine-type tris-hydroxamates reach log β > 25, while mono-hydroxamates are ~10. |
| **Fe(III) with aliphatic amines (log β ≈ 5.8)** | Surprisingly low for a trivalent ion — pure N-donors are too soft for hard Fe(III). Hydrolysis competes strongly at the pH needed to deprotonate amines. |
| **Fe(II) with S-donors** (mercaptans, thia-macrocycles) | Sparse data (3–4 systems) but present — reflects the borderline-to-soft character of Fe(II), relevant to iron–sulfur cluster biochemistry. |
| **Inorganic ligands: wide ranges** | Fe(III)–F⁻ is strong (hard–hard), Fe(III)–Cl⁻ is weak; Fe(II)–CN⁻ is very strong (low-spin d⁶ + strong π-acceptor) — a classic HSAB/CFSE synergy. |

### 6. Biological Relevance

The database trends mirror biology perfectly:
- **Fe(III) acquisition**: Organisms deploy catecholate and hydroxamate siderophores — the two highest-ranking Fe(III) ligand classes — to solubilize Fe(III) from insoluble oxides (Ksp of Fe(OH)₃ ≈ 10⁻³⁹).
- **Fe(II) function**: Heme (N₄-macrocycle), iron–sulfur clusters (S-donors), and non-heme enzymes (mixed N/O) exploit Fe(II)'s borderline character and CFSE advantages.

---

## Summary

The stability constant landscape for iron in SRD-46 is governed by a hierarchy of effects:

1. **HSAB matching** (dominant): Fe(III) → O⁻ donors; Fe(II) → N donors
2. **Chelate/macrocyclic effects**: multidentate >> monodentate, macrocyclic > open-chain
3. **CFSE**: Fe(II) d⁶ low-spin bonus with strong-field ligands (phen, bipy, CN⁻)
4. **Electrostatics**: higher-charged anionic ligands stabilize higher-charged Fe(III)

These principles, operating in concert, produce the >40 log-unit span observed across the database and explain both the general trends and the remarkable outliers like siderophore complexes.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes)*

---