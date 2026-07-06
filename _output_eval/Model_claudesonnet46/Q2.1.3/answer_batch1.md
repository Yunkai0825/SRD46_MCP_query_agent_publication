## pKa Comparison: Glycine vs. Alanine

Here are the critically evaluated pKa values from NIST SRD-46 at **25 °C, I → 0 M** (extrapolated to zero ionic strength), quality grade **A** — the highest reliability tier:

| Property | Glycine (ligand_5760) | Alanine (ligand_5761) | Difference (Δ) |
|---|---|---|---|
| Full name | Aminoacetic acid | L-2-Aminopropanoic acid | — |
| SMILES | `NCC(=O)O` | `C[C@H](N)C(=O)O` | — |
| **pKa₁ (–COOH)** | **2.35** | **2.35** | **0.00** |
| **pKa₂ (–NH₃⁺)** | **9.78** | **9.87** | **+0.09** |
| Temperature | 25 °C | 25 °C | — |
| Ionic strength | 0 M (extrapolated) | 0 M (extrapolated) | — |
| Quality grade | A | A | — |

Values were consistent across multiple electrolyte backgrounds (KNO₃, NaClO₄, KCl, NaCl, NaNO₃), confirming the robustness of the I → 0 extrapolation.

---

### Are they significantly different?

**No — the differences are chemically minor:**

- **pKa₁ (carboxyl group):** Identical at **2.35** for both. The –COOH group sits directly on the α-carbon in both molecules, and alanine's methyl group exerts negligible inductive influence at this distance.

- **pKa₂ (ammonium group):** Alanine is slightly higher (**9.87** vs. **9.78**, Δ = **+0.09 units**). This tiny increase reflects the weak **electron-donating inductive effect** of alanine's methyl side chain, which marginally stabilizes the protonated –NH₃⁺ form and thus raises the pKa slightly.

---

### Chemistry Insight

A difference of **0.09 pKa units** sits at the edge of typical potentiometric measurement uncertainty (~0.02–0.05 units per measurement). While the trend is real and reproducible across multiple independent datasets in SRD-46, it is **not chemically significant** in most practical contexts. Both amino acids share essentially the same isoelectric point (~6.0), the same zwitterionic character at physiological pH, and behave nearly identically as chelating ligands in metal coordination chemistry. Alanine's methyl group is truly "spectator" chemistry — it adds hydrophobicity and steric bulk but barely perturbs the acid-base equilibria that govern metal binding and biological reactivity.

> **Source:** NIST SRD-46 — Critically Selected Stability Constants of Metal Complexes Database

---