# pKa–Stability Constant Correlation for Ca²⁺ Complexes

## Data Summary

Using NIST SRD-46 data at 25 °C and I = 0.1 M, here are the ligand pKa values alongside their log K₁ (ML/M·L) stability constants with Ca²⁺:

| Ligand | Class | Denticity | Highest pKa | log K₁ (Ca²⁺) | I (M) |
|--------|-------|-----------|-------------|----------------|-------|
| Lactic acid | Monocarboxylic (hydroxy) | Bidentate (O,O) | 3.67 | 1.07 | 0.1 |
| Succinic acid | Dicarboxylic | Bidentate (O,O) | 5.24 | 1.20 | 0.1 |
| Glycine | Amino acid | Bidentate (N,O) | 9.57 | 1.38 | 0.1 |
| D-Tartaric acid | Dicarboxylic (hydroxy) | Bi/Tridentate | 3.97 | 1.80 | 0.1 |
| Malonic acid | Dicarboxylic | Bidentate (O,O) | 5.27 | 2.35 | 0.1 |
| Oxalic acid | Dicarboxylic | Bidentate (O,O) | 3.80 | 2.89 | 0.1 |
| Citric acid | Tricarboxylic (hydroxy) | Tri/Tetradentate | 5.65 | 3.50 | 0.1 |
| EDTA | Aminopolycarboxylic | Hexadentate (N₂O₄) | 9.52 | 10.61 | 0.1 |

## Analysis: Is There a Simple pKa–log K₁ Correlation?

### Within the simple dicarboxylate series — No simple monotonic correlation

| Dicarboxylate | Highest pKa | log K₁ (Ca²⁺) | Chelate Ring Size |
|---------------|-------------|----------------|-------------------|
| Oxalic acid | 3.80 | 2.89 | 5-membered |
| Malonic acid | 5.27 | 2.35 | 6-membered |
| Succinic acid | 5.24 | 1.20 | 7-membered |

Oxalic acid has the **lowest** highest-pKa (3.80) yet the **strongest** Ca²⁺ binding (log K₁ = 2.89). Succinic acid and malonic acid have nearly identical highest pKa values (~5.2–5.3) but differ by over 1 log unit in stability. This demonstrates that **pKa alone does not predict binding strength** — chelate ring size and geometric factors dominate within this series. The 5-membered chelate ring of oxalate is thermodynamically most favorable, followed by the 6-membered ring of malonate, and then the strained 7-membered ring of succinate.

### Across all ligand classes — Denticity and the chelate effect dominate

The data span nearly 10 orders of magnitude in stability (log K₁ from 1.07 to 10.61), but the highest pKa values do not track this trend monotonically. The key driver is **denticity**:

| Denticity Category | Representative Ligands | log K₁ Range |
|--------------------|----------------------|--------------|
| Mono/Bidentate | Lactic acid, Succinic acid, Glycine | 1.07–1.38 |
| Bidentate (favorable ring) | Oxalic acid, Malonic acid | 2.35–2.89 |
| Tri/Tetradentate | Citric acid | 3.50 |
| Hexadentate | EDTA | 10.61 |

Notably, glycine has the highest pKa in the dataset (9.57, for the amino group) yet only a modest log K₁ of 1.38 — comparable to lactic acid (pKa = 3.67). This is because Ca²⁺ is a hard Lewis acid that preferentially coordinates hard oxygen donors; the basic nitrogen of glycine contributes relatively little to Ca²⁺ binding compared to what it contributes for softer transition metals like Cu²⁺ or Ni²⁺.

## Hypothesis: Basicity and Binding Strength for Alkaline-Earth Metals

Based on the SRD-46 data, I propose the following multi-factor hypothesis:

> **For alkaline-earth metal ions like Ca²⁺ (hard Lewis acids), the stability of metal–ligand complexes is governed by a hierarchy of factors, in which basicity plays only a secondary, conditional role:**
>
> 1. **Denticity and the chelate effect** are the dominant determinants. Each additional coordinating group in a polydentate ligand contributes roughly 1.5–3 log units to log K₁, as seen in the progression from lactic acid (bidentate, log K₁ = 1.07) → citric acid (tri/tetradentate, 3.50) → EDTA (hexadentate, 10.61). The entropic advantage of multidentate chelation overwhelms any basicity differences.
>
> 2. **Chelate ring size** is the second most important factor. Within ligands of the same denticity, 5-membered chelate rings (oxalate, log K₁ = 2.89) are more stable than 6-membered rings (malonate, 2.35), which in turn are more stable than 7-membered rings (succinate, 1.20). This geometric constraint operates independently of pKa.
>
> 3. **Basicity (pKa) correlates with binding strength only within structurally homologous series** sharing the same donor atom type, denticity, and ring size. For example, among simple monodentate carboxylates, a higher carboxylate pKa generally implies greater electron density on the donor oxygen and modestly stronger Ca²⁺ binding. However, this effect is small (typically < 1 log unit) and is easily overridden by the factors above.
>
> 4. **Donor atom hardness matters more than raw basicity.** Ca²⁺ is a hard Lewis acid that strongly prefers hard oxygen donors. Glycine's highly basic amino group (pKa = 9.57) contributes far less to Ca²⁺ stability than it would for borderline or soft metals, explaining why glycine's log K₁ (1.38) is comparable to that of lactic acid (1.07) despite a 6-unit pKa difference.

### Real-World Relevance

This hierarchy explains why EDTA is the chelator of choice for Ca²⁺ titrations and why citrate is an effective biological calcium buffer — their advantage comes overwhelmingly from multidentate chelation rather than from having unusually basic donor groups. It also explains why organisms use proteins with multiple carboxylate side chains (e.g., calmodulin's EF-hand motifs) to achieve high-affinity Ca²⁺ binding: clustering multiple moderate-basicity oxygen donors is far more effective than relying on a single highly basic site.

---

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes). All values at 25 °C in aqueous solution.*

---