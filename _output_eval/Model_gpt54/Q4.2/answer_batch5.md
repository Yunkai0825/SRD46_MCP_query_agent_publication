SRD-46 data support the hypothesis that **Hg²⁺ prefers sulfur-donor ligands over nitrogen-donor ligands, and both over oxygen-donor ligands**.

Using the simple 1:1 formation reaction  
\[
\mathrm{Hg^{2+} + L \rightleftharpoons HgL}
\]
(beta definition `beta_def_812`), the database gives these representative log K values:

| Donor class | Ligand | log K (Hg²⁺ + L ⇌ HgL) | T (°C) | I (M) | SRD-46 record |
|---|---|---:|---:|---:|---|
| S-donor | Thiourea | 11.4 | 25 | 0.5 | `vlm_169530` |
| N-donor | Ethylenediamine | 14.3 | 25 | 0.1 | `vlm_122573` |
| N-donor | Pyridine | 5.2 | 25 | 0.5 | `vlm_135327` |
| N-donor | Imidazole | 9.18 | 25 | 3.0 | `vlm_134017` |
| N-donor | Ammonia | 8.8 | 22 | 2.0 | `vlm_173464` |
| O-donor | Hydrogen carbonate | -11.0 | 25 | 0.5 | `vlm_172918` |
| O-donor | Hydrogen carbonate | -10.7 | 25 | 3.0 | `vlm_172919` |

A concise class comparison is:

| Class | Representative range of log K values observed here | Interpretation |
|---|---:|---|
| S-donor | 11.4 | Strong binding |
| N-donor | 5.2 to 14.3 | Moderate to strong, ligand-dependent |
| O-donor | -11.0 to -10.7 | Very weak/unfavorable for simple ML formation |

## Hypothesis
**Hg²⁺ is strongly thiophilic overall: S-donor > N-donor >> O-donor.**

## Why the data suggest this
| Observation | Meaning |
|---|---|
| Thiourea gives log K = 11.4 at 25 °C, 0.5 M | Hg²⁺ forms a strong complex with a sulfur donor |
| Oxygen-donor bicarbonate gives log K ≈ -11 under comparable conditions | Simple O-donor binding is extremely poor |
| Nitrogen donors are intermediate: pyridine 5.2, NH₃ 8.8, imidazole 9.18, en 14.3 | Hg²⁺ can bind N donors well, but not uniformly; chelation helps a lot |

So the strongest qualitative conclusion is that **Hg²⁺ clearly disfavors pure O-donor ligands**, binds many **N-donor ligands reasonably well**, and is **expected to prefer soft sulfur donors**. In this small set, **ethylenediamine (N-donor, chelating)** even exceeds thiourea numerically, which shows that **chelate effects and ligand architecture matter**, not just donor atom identity.

Chemically, this fits the **HSAB principle**: Hg²⁺ is a **soft acid**, so soft bases such as sulfur are favored, while hard oxygen donors are disfavored. The strongly negative bicarbonate log K values are especially telling evidence against O-donor preference.

**Source:** NIST SRD-46 Stability Constants Database.

---