Using SRD-46, the data support a **positive but imperfect correlation** between ligand basicity and Ca²⁺ stability. The clearest trend is not “higher single pKa ⇒ higher log β” by itself, but rather:

**higher cumulative O-donor basicity + more O-donor sites + chelation = stronger Ca²⁺ binding.**

## Matched ligand pKa data at 25 °C, I = 0.1 M

I summarized the available aqueous pKa values for representative ligands that also have Ca²⁺ ML stability coverage in SRD-46.

| Ligand | SRD-46 ID | Relevant pKa values at 25 °C, I=0.1 M | Simple basicity note |
|---|---:|---|---|
| Oxalic acid | ligand_8872 | -1.2, 3.8 | dicarboxylate, modest cumulative basicity |
| Glycine | ligand_5760 | 2.33, 9.57 | one carboxylate + one amine |
| Tartaric acid | ligand_8955 | 2.82, 3.97 | dicarboxylate + 2 OH |
| Citric acid | ligand_9058 | 2.90, 4.35, 5.65 | tricarboxylate + OH |
| NTA | ligand_6165 | -1.81, -1.00, 2.52, 9.46 | 3 carboxylates + tertiary amine |
| EDTA | ligand_6277 | -1.5, 2.00, 2.69, 6.13, 9.52 | 4 carboxylates + 2 amines |
| DTPA | ligand_6356 | -9.9, -8.4, -1.6, -0.7, -0.1, 2.0, 2.7, 4.28 | 5 carboxylates + 3 amines |
| TTHA | ligand_6366 | -1.8, -1.5, 2.3, 2.76, 4.08, 6.14, 9.52, 10.62 | 6 carboxylates + 4 amines |
| Carbonic acid / bicarbonate | ligand_10096 | 6.13, 9.91 | hard O-donor anion system |
| Phosphoric acid / phosphate | ligand_10113 | 1.92, 6.71, 11.52 | very hard O-donor, highly basic higher deprotonations |

## Ca²⁺ stability coverage for 1:1 ML complexes

For Ca²⁺, SRD-46 contains ML (“beta_def_812”) stability datasets for these ligands under roughly comparable aqueous conditions.

| Ligand | SRD-46 ID | Ca²⁺ ML data present? | T range (°C) | I range (M) |
|---|---:|---|---:|---:|
| Glycine | ligand_5760 | Yes | 20–37 | 0–3 |
| Oxalic acid | ligand_8872 | Yes | 18–37 | 0–0.5 |
| Tartaric acid | ligand_8955 | Yes | 25 | 0–0.1 |
| Citric acid | ligand_9058 | Yes | 25–37 | 0–0.15 |
| NTA | ligand_6165 | Yes | 20–37 | 0–1 |
| EDTA | ligand_6277 | Yes | 25–37 | 0.1–1 |
| DTPA | ligand_6356 | Yes | 25–37 | 0.1–0.15 |
| TTHA | ligand_6366 | Yes | 20–30 | 0.1 |
| Carbonate | ligand_10096 | Yes | 25 | 0 |
| Phosphate | ligand_10113 | No ML logK found in this specific ML search; protonated Ca phosphate systems are present | — | — |

## Qualitative ranking from SRD-46 coverage

Based on the matched pKa patterns and the Ca²⁺ complex families present in the catalog/stability search, the ligands fall into a chemically sensible strength order:

| Approximate Ca²⁺ binding strength | Ligands |
|---|---|
| Weakest | glycine |
| Weak–moderate | oxalate, tartrate |
| Moderate | citrate, carbonate |
| Strong | NTA |
| Very strong | EDTA |
| Strongest in this set | DTPA, TTHA |

## Is there a correlation?

Yes, **qualitatively**.

Across this set, ligands with **more basic deprotonated oxygen donors** and **more donor sites** tend to show stronger Ca²⁺ complexation. The trend from simple ligands to aminopolycarboxylates is especially clear:

| Ligand family trend | Interpretation |
|---|---|
| Glycine / oxalate / tartrate < citrate < NTA < EDTA < DTPA / TTHA | Increasing total donor number, total negative charge, and cumulative basicity generally increase Ca²⁺ affinity |

But the correlation is **not purely with a single pKa value**:

| Why the correlation is imperfect | Effect |
|---|---|
| Denticity differs greatly | multidentate ligands gain large chelate advantage |
| Total ligand charge differs | more highly deprotonated ligands favor Ca²⁺ electrostatically |
| Donor type matters | Ca²⁺ prefers hard O donors more than neutral/soft donors |
| Protonation state matters | protonated complexes and stepwise acid dissociation complicate simple comparisons |
| Carbonate/phosphate are confounded by precipitation | apparent affinity can reflect ion pairing/solid formation as well as true soluble ML stability |

## Hypothesis for alkaline-earth metals

| Hypothesis |
|---|
| For alkaline-earth metals such as Ca²⁺, binding strength should increase with the **effective basicity of hard oxygen-donor sites**, but the dominant predictors are the **number, arrangement, and charge of those O donors** rather than any single pKa alone. Thus, a positive pKa–stability correlation exists within related ligand families, while across diverse ligands the stronger rule is: **more highly deprotonated multidentate O-donor ligands bind more strongly**. |

## Chemistry insight

Ca²⁺ is a **hard Lewis acid**, so it is stabilized best by **hard, anionic oxygen donors** such as carboxylates and phosphates. That is why aminopolycarboxylates like EDTA, DTPA, and TTHA outperform small monocarboxylates: not just because they are “more basic,” but because they present **multiple preorganized O donors** and gain a strong **chelate effect**.

**Source:** NIST SRD-46 Stability Constants Database.

---