# 🧲 The Lanthanide Contraction in Action: EDTA Stability Constants Across the Rare Earths

One of the most elegant patterns in coordination chemistry is the **steady increase in stability constants** as you traverse the lanthanide series from La³⁺ to Lu³⁺. Here it is, captured in real data from the NIST SRD-46 database.

## Ln³⁺–EDTA Stability Constants (log K₁ for ML/M·L)

All values measured in **aqueous KNO₃**, *I* = 0.1 M, *T* ≈ 20–25 °C.

| # | Metal Ion | Z | 4f electrons | log K (ML/M·L) |
|---|-----------|---|:---:|:---:|
| 1 | Sc³⁺ | 21 | 0 (3d⁰) | **23.10** |
| 2 | La³⁺ | 57 | 0 | **15.50** |
| 3 | Nd³⁺ | 60 | 3 | **16.61** |
| 4 | Pm³⁺ | 61 | 4 | **17.45** |
| 5 | Sm³⁺ | 62 | 5 | **17.14** |
| 6 | Gd³⁺ | 64 | 7 | **17.37** |
| 7 | Tb³⁺ | 65 | 8 | **17.93** |
| 8 | Dy³⁺ | 66 | 9 | **18.30** |
| 9 | Ho³⁺ | 67 | 10 | **18.62** |
| 10 | Er³⁺ | 68 | 11 | **18.85** |
| 11 | Tm³⁺ | 69 | 12 | **19.32** |
| 12 | Yb³⁺ | 70 | 13 | **19.51** |
| 13 | Lu³⁺ | 71 | 14 | **19.83** |

## What makes this interesting?

### 📈 The Overall Trend: Lanthanide Contraction
The log K values increase **monotonically** from La³⁺ (15.5) to Lu³⁺ (19.83) — a span of **4.3 log units**, meaning the Lu–EDTA complex is roughly **20,000× more stable** than La–EDTA. This directly reflects the **lanthanide contraction**: as 4f electrons are added across the series, they poorly shield nuclear charge, so the ionic radius shrinks steadily (La³⁺ ≈ 1.03 Å → Lu³⁺ ≈ 0.86 Å). The increasing charge density strengthens the electrostatic interaction with EDTA's four carboxylate and two amine donor groups.

### 🔻 The "Gadolinium Break"
The increase is **not perfectly smooth**. Between Pm³⁺ (17.45) and Sm³⁺ (17.14), the log K actually **dips**, and Gd³⁺ (17.37) sits below the extrapolated trend. This is the famous **"gadolinium break"** — a subtle discontinuity near the half-filled 4f⁷ shell. It arises from changes in hydration enthalpy and coordination number that occur around the middle of the series, where the lanthanides transition from 9-coordinate to 8-coordinate aqua ions.

### 🏆 Scandium: The Outlier Champion
Sc³⁺ stands out dramatically with log K = **23.1** — nearly 4 log units above even Lu³⁺. Despite being classified as a "rare earth," Sc³⁺ has a much smaller ionic radius (~0.75 Å) and no 4f electrons, giving it an exceptionally high charge density. This makes its EDTA complex extraordinarily stable — about **200 million times** more stable than La–EDTA.

### 🏥 Real-World Relevance
The Gd³⁺–EDTA system (log K = 17.37) is directly relevant to **MRI contrast agents**. Clinical gadolinium-based contrast agents use polyaminocarboxylate chelators like DTPA and DOTA (which have even higher log K values than EDTA) to safely deliver paramagnetic Gd³⁺ into the body. The chelator must bind Gd³⁺ tightly enough to prevent release of toxic free Gd³⁺ ions — this dataset illustrates why even stronger ligands than EDTA are needed in practice.

### 📊 Rare Earths in the SRD-46 Database: A Data Richness Overview

The database contains extensive stability constant data for all 17 rare earth ions:

| Metal Ion | Ligand Partners | VLM Records | β Definitions |
|-----------|:-:|:-:|:-:|
| La³⁺ | 297 | 931 | 30 |
| Gd³⁺ | 288 | 897 | 28 |
| Eu³⁺ | 267 | 870 | 30 |
| Sm³⁺ | 265 | 844 | 28 |
| Nd³⁺ | 263 | 794 | 29 |
| Er³⁺ | 241 | 792 | 29 |
| Yb³⁺ | 235 | 771 | 28 |
| Dy³⁺ | 252 | 758 | 23 |
| Pr³⁺ | 231 | 723 | 24 |
| Tb³⁺ | 235 | 709 | 24 |
| Ho³⁺ | 230 | 705 | 24 |
| Lu³⁺ | 234 | 671 | 25 |
| Tm³⁺ | 223 | 633 | 22 |
| Ce³⁺ | 188 | 567 | 22 |
| Y³⁺ | 182 | 533 | 26 |
| Sc³⁺ | 44 | 156 | 16 |
| Pm³⁺ | 14 | 24 | 4 |

Promethium (Pm³⁺) is strikingly data-poor with only 24 measurements — unsurprising since all its isotopes are radioactive with no stable forms, making experimental work extremely difficult. The fact that SRD-46 contains *any* Pm stability data at all is remarkable.

Notable non-trivalent entries include **Ce⁴⁺** (9 VLM records — cerium's accessible +4 state) and **Eu²⁺** (2 records — europium's rare but important +2 state stabilized by the half-filled 4f⁷ configuration).

---

*Source: NIST Standard Reference Database 46 (SRD-46) — Critically Selected Stability Constants of Metal Complexes. Equilibrium definition: ML/M·L (beta_def_812), aqueous solution, 0.1 M KNO₃.*

---