## pKa Comparison: Glycine vs. Alanine

Both glycine and alanine are simple α-amino acids with two ionizable groups: a **carboxyl group** (–COOH, pKa₁) and an **ammonium group** (–NH₃⁺, pKa₂). The NIST SRD-46 database contains multiple high-quality (grade A) measurements at 25 °C in aqueous solution for both.

---

### Measured pKa Values at 25 °C (Quality Grade A)

#### pKa₁ — Carboxyl Group (H₂L → HL)

| Amino Acid | SRD-46 ID | Ionic Strength (M) | Electrolyte | pKa₁ (observed range) |
|---|---|---|---|---|
| Glycine | ligand_5760 | 0.0 | KCl | 2.34 |
| Glycine | ligand_5760 | 0.1 | KNO₃ | 2.35 – 2.36 |
| Glycine | ligand_5760 | 0.1 | NaClO₄ | 2.36 |
| Alanine | ligand_5761 | 0.0 | KCl | 2.33 |
| Alanine | ligand_5761 | 0.1 | KNO₃ | 2.34 |

#### pKa₂ — Ammonium Group (HL → L)

| Amino Acid | SRD-46 ID | Ionic Strength (M) | Electrolyte | pKa₂ (observed range) |
|---|---|---|---|---|
| Glycine | ligand_5760 | 0.0 | KCl | 9.55 |
| Glycine | ligand_5760 | 0.1 | KNO₃ | 9.58 |
| Glycine | ligand_5760 | 0.1 | NaClO₄ | 9.60 |
| Alanine | ligand_5761 | 0.0 | KCl | 9.69 |
| Alanine | ligand_5761 | 0.1 | KNO₃ | 9.71 |

---

### Head-to-Head Comparison at Matched Conditions

| Parameter | Glycine | Alanine | Δ (Ala − Gly) |
|---|---|---|---|
| **pKa₁** (I = 0.0 M, KCl, 25 °C) | 2.34 | 2.33 | **−0.01** |
| **pKa₁** (I = 0.1 M, KNO₃, 25 °C) | 2.35–2.36 | 2.34 | **~−0.01 to −0.02** |
| **pKa₂** (I = 0.0 M, KCl, 25 °C) | 9.55 | 9.69 | **+0.14** |
| **pKa₂** (I = 0.1 M, KNO₃, 25 °C) | 9.58 | 9.71 | **+0.13** |

---

### Are the Differences Significant?

**No — the differences are small but real and chemically interpretable:**

- **pKa₁ (carboxyl):** Essentially identical (~2.33–2.36 for both). The methyl side chain of alanine is too remote from the carboxyl group to exert a meaningful inductive effect. The ~0.01–0.02 unit difference is within experimental scatter.

- **pKa₂ (ammonium):** Alanine is consistently **~0.13–0.14 units higher** than glycine across all conditions. This small but reproducible difference reflects the **electron-donating inductive effect** of alanine's methyl group, which stabilizes the positive charge on –NH₃⁺ slightly more, making it marginally harder to deprotonate. The difference is real and consistent across multiple independent measurements, but it is chemically minor — both amino acids behave nearly identically in physiological buffering (pH 7.4) and metal coordination chemistry.

---

### Chemistry Insight

The near-identical pKa₁ values confirm that the α-carboxyl group acidity is insensitive to simple alkyl substitution at the α-carbon. The modest pKa₂ difference (+0.14 units for alanine) is a classic demonstration of the **alkyl inductive effect** in amino acid chemistry. In practical terms, both amino acids have essentially the same isoelectric point (~6.0) and coordinate metals through their amino and carboxylate groups with very similar affinities — glycine has 428 VLM entries in SRD-46 vs. 159 for alanine, reflecting glycine's greater use as a model ligand in coordination chemistry studies.

*Source: NIST SRD-46 (ligand_5760 = Glycine, ligand_5761 = Alanine)*

---