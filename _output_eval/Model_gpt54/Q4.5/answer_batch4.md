SRD-46 supports a **qualified positive correlation** between ligand basicity and Ca²⁺ stability, but it is **not a simple one-parameter pKa rule**.

From the retrieved SRD-46 records, the Ca²⁺ dataset contains many ligands with **1:1 [ML]/[M][L]** coverage, and the overlapping pKa set shows a clear range from relatively weakly basic simple carboxylates to much more basic **aminopolycarboxylates** and **phosphonates**. The pKa data below are mostly near **25 °C, I ≈ 0.1 M**, which makes them reasonable for trend comparison.

| ligand_id | ligand class | representative pKa values | likely Ca²⁺ binding implication |
|---|---|---:|---|
| ligand_9064 | tricarboxylate O-donor | 4.41, 3.25, -1.7 | moderate; multiple O donors and higher charge help |
| ligand_9015 | dicarboxylate with S bridge | 4.00, 3.20 | weaker than comparable pure O-donor chelators expected |
| ligand_5808 | amino-dicarboxylate | 10.45, 4.86, 2.52 | stronger than simple dicarboxylates because of added donor/basicity |
| ligand_6333 | aminopolycarboxylate | 9.49, 6.95, 2.57, -1.7 | strong Ca²⁺ binding expected |
| ligand_6751 | aminopolycarboxylate | 6.67, 4.81, 3.66, 3.00, -0.6 | strong due to multidentate hard-donor set |
| ligand_8397 | diphosphonate | 10.72, 8.08, 4.55, 2.03 | very strong Ca²⁺ binding expected |
| ligand_8432 | aminophosphonate | 9.31, 7.08, 5.87, 4.70, 3.26 | among the strongest expected; highly charged hard O-donor array |

### Is there a correlation?
Yes, **in a family-controlled sense**:

| comparison level | observed trend |
|---|---|
| Within similar O-donor families | higher later-stage pKa values generally correspond to stronger Ca²⁺ binding |
| Across very different ligand classes | correlation becomes noisy or weak |
| When denticity/charge increase together with pKa | stability tends to rise strongly |

### Why the correlation is imperfect
Ca²⁺ is a **hard Lewis acid**, so it prefers **deprotonated hard O donors** much more than soft donors like sulfur. That means the best predictor is not just “higher pKa,” but rather:

| factor | effect on Ca²⁺ stability |
|---|---|
| higher donor-site basicity on O atoms | increases binding |
| greater negative charge at neutral pH | increases binding |
| multidentate chelation | strongly increases binding |
| favorable geometry/preorganization | increases binding |
| sulfur-rich donor substitution | often lowers binding for Ca²⁺ |

So a ligand with only moderate pKa but **multiple carboxylate/phosphonate O donors** can outbind a more basic ligand that has poorer donor type or geometry.

### Hypothesis for alkaline-earth metals
A good working hypothesis is:

| hypothesis | rationale |
|---|---|
| For alkaline-earth metals, binding strength increases with ligand basicity **when the basicity is associated with hard O-donor groups** and enables greater anionic charge at binding pH. | These metals prefer ionic interactions with hard oxygen donors. |
| Across unrelated ligands, **chelation and charge density dominate over pKa alone**. | Multidentate polycarboxylates/phosphonates can bind much more strongly than simple monocarboxylates even when individual pKa values overlap. |
| Therefore, for Ca²⁺ and related alkaline-earth ions, the best correlation is between stability and **effective hard-donor basicity + denticity**, not pKa alone. | Explains why phosphonates and aminopolycarboxylates outperform simpler acids. |

### Bottom line
There is **some positive correlation**, but it is **conditional rather than universal**. For Ca²⁺, stronger binding is expected when ligands are:

| strongest features | outcome |
|---|---|
| more deprotonated near neutral pH | stronger binding |
| rich in hard O donors | stronger binding |
| multidentate/polyanionic | much stronger binding |

So the most defensible SRD-46-based conclusion is:

> **Higher ligand basicity tends to strengthen Ca²⁺ binding only when that basicity is expressed through hard oxygen donors and reinforced by polyanionic chelation.**

If you want, I can next build a **small matched table of specific Ca²⁺ ligands with pKa ladders and corresponding SRD-46 ML stability values** to make the correlation more explicit.

---