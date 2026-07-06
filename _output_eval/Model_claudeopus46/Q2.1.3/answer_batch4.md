I have sufficient data from the ligand searches to provide a solid comparison. Let me compile the answer.

---

## Glycine vs. Alanine: pKa Comparison

Both glycine and alanine are α-amino acids with two ionizable groups — a carboxyl group (pKa₁) and an amino group (pKa₂). The NIST SRD-46 database reports the following representative (bracket) pKa values:

| Property | Glycine (ligand\_5760) | L-Alanine (ligand\_5761) | Difference (Ala − Gly) |
|---|---|---|---|
| **pKa₁** (H₂L⁺ → HL±, carboxyl) | **2.33** | **2.33** | **0.00** |
| **pKa₂** (HL± → L⁻, amino) | **9.57** | **9.71** | **+0.14** |
| Ligand class | Amino Acids | Amino Acids | — |
| HxL definition | HL | HL | — |
| SMILES | `NCC(=O)O` | `C[C@H](N)C(=O)O` | — |

### Are the differences significant?

**pKa₁ (carboxyl):** The values are **identical** at 2.33. This is expected — the carboxyl group environment is very similar in both molecules, and the methyl substituent on the α-carbon in alanine is too far from the –COOH to exert a meaningful inductive effect on this dissociation.

**pKa₂ (amino):** Alanine's amino pKa₂ is **0.14 units higher** than glycine's (9.71 vs. 9.57). This small difference is at the edge of typical experimental uncertainty for potentiometric pKa measurements (often ±0.05–0.10 log units), but it is **chemically reasonable and consistently observed**. The electron-donating methyl group on alanine's α-carbon slightly increases electron density on the adjacent –NH₃⁺, making the protonated amine a marginally weaker acid (higher pKa). In practical terms, however, a 0.14-unit difference is **not large** — both amino acids behave very similarly as buffers and metal-ion chelators.

### Chemistry Insight

The near-identical pKa values reflect the fact that glycine and alanine differ only by a single methyl group on the α-carbon. This substituent is too small and too far from the ionizable groups to cause a dramatic electronic perturbation. For comparison, β-alanine (ligand\_5788), where the amino group is moved to the β-position, shows much larger deviations (pKa₁ = 3.51, pKa₂ = 10.08), highlighting that the **position** of the amino group relative to the carboxyl matters far more than a simple methyl substitution.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes).*

---