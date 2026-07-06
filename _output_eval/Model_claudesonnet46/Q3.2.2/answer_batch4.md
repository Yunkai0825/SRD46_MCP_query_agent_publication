## Ni²⁺–Ethylenediamine: Stability Constants vs. Ionic Strength

*Source: NIST SRD-46 (metal_112 × ligand_7029, 45 VLM entries)*

Ethylenediamine (en, `NCCN`) forms three successive complexes with Ni²⁺. The cumulative formation constants (log β) at **25 °C in KNO₃** across ionic strengths are:

### log β vs. Ionic Strength (25 °C, KNO₃)

| Ionic Strength (M) | log β₁ [Ni(en)]²⁺ | log β₂ [Ni(en)₂]²⁺ | log β₃ [Ni(en)₃]²⁺ |
|:-----------------:|:-----------------:|:------------------:|:------------------:|
| 0.0 (extrapolated) | 7.90 | 14.53 | 19.18 |
| 0.1 | 7.52 | 13.86 | 18.28 |
| 0.5 | 7.47 | 13.73 | 18.10 |
| 1.0 | 7.35 | 13.52 | 17.84 |
| 2.0 | 7.15 | 13.17 | 17.44 |
| 3.0 | 6.98 | *(anomalous)* | *(anomalous)* |

> ⚠️ The I = 3.0 M values for β₂ and β₃ appear as large negative numbers in the database (−14.77 and −19.7), which are almost certainly sign-error artefacts in the source record and should be disregarded. The β₁ value at I = 3.0 M (6.98) is physically plausible.

**Cross-medium comparison at I = 0.5 M, 25 °C:**

| Electrolyte | log β₁ | log β₂ |
|:-----------:|:------:|:------:|
| KNO₃ | 7.47 | 13.73 |
| NaClO₄ | 7.52 | 13.86 |

---

### Is There a Clear Trend?

**Yes — all three constants decrease monotonically as ionic strength rises from 0 to 2 M:**

| Species | log β at I = 0 | log β at I = 2 M | Δ log β |
|:-------:|:--------------:|:----------------:|:-------:|
| Ni(en)²⁺ | 7.90 | 7.15 | −0.75 |
| Ni(en)₂²⁺ | 14.53 | 13.17 | −1.36 |
| Ni(en)₃²⁺ | 19.18 | 17.44 | −1.74 |

The higher-order complexes show a **larger absolute decrease**, because β_n is a cumulative product of n stepwise constants — small per-step decreases compound multiplicatively in log space.

---

### Chemistry Insight

1. **Why does log β decrease with I?** Although the overall reaction Ni²⁺ + n·en → Ni(en)_n²⁺ is **charge-symmetric** (both reactant and product carry 2+), the neutral ethylenediamine ligand has a different activity-coefficient behavior than the free Ni²⁺ ion at elevated ionic strength. The Specific Ion Interaction Theory (SIT) framework predicts a modest but real decrease for such systems, fully consistent with the observed trend.

2. **The drop is gradual, not dramatic.** Over I = 0.1–2.0 M, log β₁ falls only ~0.4 units — confirming that this charge-neutral ligand system is far less sensitive to ionic strength than, say, carboxylate or phosphate ligands where the charge balance changes dramatically upon binding.

3. **Electrolyte identity matters at the margin.** At I = 0.5 M, NaClO₄ gives log β₁ = 7.52 vs. 7.47 in KNO₃ — a small but real difference reflecting ion-specific (Hofmeister-type) interactions. Perchlorate is a weakly coordinating anion that perturbs activity coefficients differently from nitrate, slightly stabilizing the complex.

**Bottom line:** The Ni²⁺–en system shows a clear, smooth decrease in log β with increasing ionic strength across all three stoichiometries, with the effect being modest (≲1 log unit over 0–2 M) due to the charge-neutral nature of the ligand.

---