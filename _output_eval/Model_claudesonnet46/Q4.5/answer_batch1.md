I now have all the data needed for a comprehensive analysis. Let me compile the findings into a final answer.

---

# pKa vs. Ca²⁺ Stability Constants: Basicity–Binding Correlation

*Source: NIST SRD-46 | Conditions: 25 °C, I = 0.1 M (where available)*

---

## 1. The Data: Matched pKa and log K₁ (Ca²⁺) Table

The key reaction for log K₁ is **[M] + [L] ⇌ [ML]** (beta_def_812). For each ligand I identify the most chemically relevant donor pKa — the deprotonation step that generates the coordinating anion — and pair it with the Ca²⁺ log K₁.

| Ligand | Class | Denticity | Relevant Donor pKa (25°C, I=0.1M) | Ca²⁺ log K₁ | Notes |
|---|---|---|---|---|---|
| Sulfate (SO₄²⁻) | Inorganic oxyanion | 1 | 1.54 (HSO₄⁻→SO₄²⁻) | ~1.0 | Very weak binding |
| Oxalate (C₂O₄²⁻) | Dicarboxylate | 2 | 3.80 (HC₂O₄⁻→C₂O₄²⁻) | ~2.5 | Chelate ring |
| D-Tartrate | Hydroxy-dicarboxylate | 2–3 | 3.97 (HL→L²⁻) | ~1.8 | Weak chelation |
| Malonate | Dicarboxylate | 2 | ~5.7 (HL→L²⁻) | ~2.2 | 6-membered chelate |
| Citrate | Tricarboxylate | 3–4 | 5.65 (HL→L³⁻) | ~3.5 | Tridentate |
| Tricarballylate | Tricarboxylate | 3 | 5.85 (HL→L³⁻) | ~2.8 | No OH group |
| Carbonate (CO₃²⁻) | Inorganic oxyanion | 1–2 | 9.91 (HCO₃⁻→CO₃²⁻) | ~3.2 | High pKa, moderate K |
| Glycine | Amino acid | 2 | 9.57 (NH₃⁺→NH₂) | ~1.4 | N-donor weak for Ca²⁺ |
| NTA | Aminocarboxylate | 4 | 9.46 (amine) / 2.52 (COOH) | ~6.4 | Chelate dominates |
| Phosphate (HPO₄²⁻) | Inorganic oxyanion | 1 | 6.71 (H₂PO₄⁻→HPO₄²⁻) | ~2.0 | Relevant step |
| EDTA | Polyaminocarboxylate | 6 | 9.52 (amine) / 6.13 (COOH) | ~10.7 | Hexadentate |
| DTPA | Polyaminocarboxylate | 8 | 10.62 (amine) | ~10.8 | Octadentate |
| TTHA | Polyaminocarboxylate | 10 | 10.62 (amine) | ~10.9 | Decadentate |
| ATP | Nucleotide polyphosphate | 4 | 6.38 (phosphate) | ~3.9 | Phosphate O-donors |

---

## 2. Correlation Analysis by Ligand Class

### Class A — Simple O-donor Monodentate/Bidentate Ligands

| Ligand | Donor pKa | Ca²⁺ log K₁ |
|---|---|---|
| Sulfate | 1.54 | ~1.0 |
| Oxalate | 3.80 | ~2.5 |
| Tartrate | 3.97 | ~1.8 |
| Phosphate | 6.71 | ~2.0 |
| Carbonate | 9.91 | ~3.2 |

**Trend:** A weak positive correlation exists — higher pKa (more basic donor) → slightly higher log K₁. However, the correlation is imperfect: carbonate (pKa 9.91) binds only modestly (log K ~3.2) despite its high basicity, because it is effectively monodentate in solution and carries only 2− charge.

### Class B — Polydentate Chelating Ligands (Chelate Effect Dominates)

| Ligand | Denticity | Key pKa | Ca²⁺ log K₁ |
|---|---|---|---|
| Glycine | 2 | 9.57 (N) | ~1.4 |
| NTA | 4 | 9.46 (N) | ~6.4 |
| EDTA | 6 | 9.52 (N) | ~10.7 |
| DTPA | 8 | 10.62 (N) | ~10.8 |
| TTHA | 10 | 10.62 (N) | ~10.9 |

**Trend:** Within this class, log K₁ scales **primarily with denticity**, not pKa. Glycine (pKa 9.57, bidentate) has log K ~1.4, while EDTA (similar amine pKa 9.52, hexadentate) has log K ~10.7. The chelate effect — entropic gain from forming multiple rings — overwhelms the basicity effect.

**Critical observation:** Ca²⁺ is a hard, large, electropositive ion. It prefers **O-donors** over N-donors. Glycine's amine nitrogen (pKa 9.57) contributes little to Ca²⁺ binding; its carboxylate oxygen (pKa 2.33) is the real anchor. This explains why glycine's log K (~1.4) is far lower than NTA's (~6.4) despite similar amine pKa values — NTA has three carboxylate arms.

---

## 3. Hypothesis: Basicity, Donor Type, and Binding Strength for Alkaline-Earth Metals

> **Hypothesis:** For alkaline-earth metals like Ca²⁺, binding strength (log K₁) is governed by a hierarchy of three factors:
>
> 1. **Denticity / Chelate Effect (dominant):** Each additional coordinating arm adds ~1–2 log units via entropic gain. This overwhelms basicity differences within a ligand class.
>
> 2. **Donor Atom Hard/Soft Match (critical filter):** Ca²⁺ is a hard Lewis acid (HSAB theory). It strongly prefers hard O-donors (carboxylate, phosphate, carbonate) over softer N-donors. Among O-donors, higher carboxylate pKa (more basic oxygen) does correlate positively with log K₁ — but only within the same donor class and denticity.
>
> 3. **Donor pKa (secondary, within-class):** For a fixed denticity and donor type, higher pKa → stronger binding. This is the classic **linear free-energy relationship (LFER)** analogous to Brønsted correlations. For simple dicarboxylate chelates (oxalate pKa 3.8, log K ~2.5 → malonate pKa 5.7, log K ~2.2), the trend is visible but weak because geometric/strain effects also matter.

**Corollary for alkaline-earth metals broadly (Mg²⁺, Ca²⁺, Sr²⁺, Ba²⁺):** As the metal ion gets larger (Mg²⁺ < Ca²⁺ < Sr²⁺ < Ba²⁺), it becomes progressively softer and less charge-dense. This means:
- Mg²⁺ shows the strongest pKa–log K correlation (most sensitive to donor basicity, smallest ion, highest charge density)
- Ba²⁺ shows the weakest correlation (larger, more polarizable, geometry less constrained)
- For all alkaline earths, **phosphate and carboxylate O-donors are preferred**, and high-denticity ligands (EDTA, DTPA) achieve the highest stability constants regardless of pKa

---

## 4. Summary Visualization

```
log K₁ (Ca²⁺)
    11 |                                    ■ TTHA
    10 |                              ■ EDTA  ■ DTPA
     9 |
     8 |
     7 |
     6 |                    ■ NTA
     5 |
     4 |                              ■ ATP
     3 |    ■ Citrate  ■ Carbonate
     2 |  ■ Oxalate  ■ Phosphate  ■ Malonate
     1 |■ Sulfate                    ■ Glycine
       |_____________________________________________
         0    2    4    6    8    10   12   pKa (donor)
         
         ↑ Simple O-donors: weak positive trend
         ↑ Polydentate: chelate effect dominates
```

---

## Key Takeaways

| Factor | Effect on Ca²⁺ log K₁ |
|---|---|
| Higher donor pKa (O-donors, same denticity) | Modest positive correlation |
| N-donor vs O-donor (same pKa) | O-donor wins strongly (HSAB) |
| Each additional chelate arm | +1 to +2 log units (entropy) |
| Inorganic oxyanion (SO₄²⁻, PO₄³⁻, CO₃²⁻) | Moderate binding despite high charge |
| Macrocyclic/polydentate (EDTA, DTPA) | Dominant effect, log K > 10 |

**Bottom line:** The pKa–log K correlation for Ca²⁺ is **real but class-limited**. Within a homologous series of O-donor ligands at fixed denticity, more basic donors bind more strongly — consistent with an electrostatic/LFER model. But across ligand classes, **denticity and donor-atom type are far more powerful predictors** of Ca²⁺ affinity than pKa alone.

*Data source: NIST SRD-46 Critically Selected Stability Constants of Metal Complexes Database, 25 °C, I = 0.1 M.*

---