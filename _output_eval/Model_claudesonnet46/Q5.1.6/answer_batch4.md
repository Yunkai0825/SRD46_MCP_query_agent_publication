# 🌟 Rare Earth Metals in NIST SRD-46: A Complete Exploration

---

## 1. The Lanthanide Series — Database Coverage at a Glance

All 14 lanthanides plus Y³⁺ and Sc³⁺ are well-represented in SRD-46, exclusively as M³⁺ ions in solution:

| Metal | Symbol | ID | Ligand Partners | VLM Entries | β-Definitions |
|-------|--------|----|-----------------|-------------|---------------|
| Lanthanum | La³⁺ | metal_79 | **297** | **931** | 30 |
| Cerium | Ce³⁺ | metal_27 | 188 | 567 | 22 |
| Praseodymium | Pr³⁺ | metal_139 | 231 | 723 | 24 |
| Neodymium | Nd³⁺ | metal_110 | 263 | 794 | 29 |
| Samarium | Sm³⁺ | metal_173 | 265 | 844 | 28 |
| Europium | Eu³⁺ | metal_58 | 267 | 870 | 30 |
| Gadolinium | Gd³⁺ | metal_65 | **288** | **897** | 28 |
| Terbium | Tb³⁺ | metal_179 | 235 | 709 | 24 |
| Dysprosium | Dy³⁺ | metal_44 | 252 | 758 | 23 |
| Holmium | Ho³⁺ | metal_73 | 230 | 705 | 24 |
| Erbium | Er³⁺ | metal_55 | 241 | 792 | 29 |
| Thulium | Tm³⁺ | metal_192 | 223 | 633 | 22 |
| Ytterbium | Yb³⁺ | metal_206 | 235 | 771 | 28 |
| Lutetium | Lu³⁺ | metal_81 | 234 | 671 | 25 |
| Yttrium | Y³⁺ | metal_205 | 182 | 533 | 26 |
| Scandium | Sc³⁺ | metal_169 | **44** | **156** | 16 |

> **Key observation:** La³⁺ has the most ligand partners (297) and VLMs (931) of any lanthanide — it is the most-studied member in solution equilibrium chemistry, partly because its large ionic radius and simple 4f⁰ configuration make it the ideal "reference" lanthanide. Data density peaks in the early-to-mid series (La, Gd, Eu) and tapers toward the heavy end (Tm, Lu). **Sc³⁺ is a dramatic outlier** with only 44 ligand partners — its much smaller ionic radius (~0.75 Å vs. ~1.0 Å for La) and distinct coordination preferences set it apart from the true lanthanides.

---

## 2. 🚨 Anomalous Oxidation States — Rare Earths Breaking the Rules

Most lanthanides are locked into +3, but a few break the mold — and the database reflects how experimentally challenging these species are:

| Species | ID | Ligand Partners | VLMs | Chemistry Note |
|---------|-----|-----------------|------|----------------|
| Ce³⁺ | metal_27 | 188 | 567 | Normal Ln(III), well-studied |
| **Ce⁴⁺** | metal_28 | **3** | **9** | Strong oxidizer; hydrolyzes rapidly |
| Eu³⁺ | metal_58 | 267 | 870 | Normal Ln(III), well-studied |
| **Eu²⁺** | metal_59 | **2** | **2** | Rare reducing form; nearly absent |
| Yb³⁺ | metal_206 | 235 | 771 | Normal Ln(III), well-studied |
| **Yb²⁺** | metal_207 | **0** | **0** | No binding data whatsoever |

> **Chemistry insight:** Ce⁴⁺ is a powerful oxidant (E° ≈ +1.72 V vs. NHE) that rapidly hydrolyzes in water, making solution equilibrium measurements extremely difficult — hence only 9 VLMs in the entire database. Eu²⁺ is isoelectronic with Gd³⁺ (half-filled 4f⁷) and is stable enough to measure in deoxygenated solutions, but its reducing power (E° ≈ −0.35 V) means ligand-binding studies are rare. Yb²⁺ has literally zero binding data — it is too unstable in aqueous solution to characterize.

---

## 3. 🧪 La³⁺ Ligand Diversity — A Window into Lanthanide Coordination

The La³⁺ catalog (20 top ligand pairs) beautifully illustrates the breadth of lanthanide coordination chemistry:

| Ligand | Type | Species | VLMs | Max Stoichiometry |
|--------|------|---------|------|-------------------|
| Malonate | Dicarboxylate | 4 | 20 | ML₄ |
| Tartrate | Hydroxy-dicarboxylate | 3 | 19 | ML₂ |
| Glycolate | Hydroxy-carboxylate | 4 | 19 | ML₄ |
| Acetate | Simple carboxylate | 3 | 17 | ML₃ |
| EDTA | Aminopolycarboxylate | 2 | 12 | ML (+ MHL) |
| NTA | Aminotriacetate | 3 | 11 | ML₃ |
| Dipicolinate | Pyridine-dicarboxylate | 3 | 9 | ML₃ |
| Fluoride | Halide | 2 | 8 | LaF²⁺ + LaF₃(s) |
| Acetylacetone | β-diketone | 3 | 14 | ML₃ |
| Thioglycolate | Thio-carboxylate | 2 | 8 | MHL₂ |

> **Notable:** La³⁺ forms up to ML₄ complexes with simple monodentate carboxylates (glycolate, malonate), reflecting its large coordination sphere (typically 8–10 coordinate). With multidentate chelators like EDTA, the 1:1 ML complex dominates because EDTA already occupies 6 coordination sites. The presence of LaF₃(s) solid-phase data alongside solution data shows the database captures both solubility products and formation constants.

---

## 4. 💊 The Chelator Landscape — EDTA, DTPA, and Biomedical Relevance

The two dominant aminopolycarboxylate chelators studied with rare earths:

| Ligand | ID | VLMs | pKa Values | Donor Atoms | Key Application |
|--------|-----|------|-----------|-------------|-----------------|
| EDTA | ligand_6277 | 596 | 2.0, 2.69, 6.13, 9.52 | 6 | Industrial separation, general chelation |
| DTPA | ligand_6356 | 322 | 2.0, 2.7, 4.28, 4.28, ~8.4 | 8 | MRI contrast agents (Gd-DTPA = Magnevist®) |
| HEDTA | ligand_6275 | 237 | 2.62, 5.38, 9.7 | 5 | Intermediate chelation strength |

> **Chemistry insight:** DTPA has 8 donor atoms vs. EDTA's 6, giving it significantly higher stability constants with lanthanides (typically 2–4 log units stronger). This is precisely why **Gd-DTPA (Magnevist®)** became the first FDA-approved MRI contrast agent in 1988 — the extra chelation prevents toxic free Gd³⁺ release in the body. The database's 322 DTPA VLMs reflect decades of biomedical research. The 596 EDTA VLMs make it the single most-measured ligand for rare earths in SRD-46.

---

## 5. ⚡ Charge Dominates Stability — EDTA Across the Periodic Table

The EDTA stability search revealed a striking charge-dependence that puts lanthanides in context:

| Metal | Charge | log β (ML) | Conditions |
|-------|--------|-----------|------------|
| Th⁴⁺ | +4 | **23.2** | 25°C, I = 0.1 M NaClO₄ |
| Hf⁴⁺ | +4 | 19.1–20.0 | 25°C, I = 0.1 M NaClO₄ |
| Ln³⁺ | +3 | ~15–19 | (typical lanthanide range) |

> **The pattern is unmistakable:** tetravalent metals bind EDTA orders of magnitude more strongly than trivalent lanthanides. Each unit increase in metal charge adds roughly 4–5 log units to the stability constant — a direct consequence of the predominantly electrostatic (ionic) nature of lanthanide coordination, where covalent bonding contributions are minimal. This is why nuclear fuel reprocessing uses carefully tuned pH and ligand concentration to separate Th⁴⁺ from Ln³⁺ impurities.

---

## 🔑 Summary: Five Fascinating Facts About Rare Earths in SRD-46

| # | Finding | Data Point |
|---|---------|-----------|
| 1 | **La³⁺ is the most-studied lanthanide** | 297 ligands, 931 VLMs |
| 2 | **Sc³⁺ is the odd one out** | Only 44 ligands vs. 230–297 for true Ln |
| 3 | **Anomalous oxidation states are data deserts** | Ce⁴⁺: 9 VLMs; Eu²⁺: 2 VLMs; Yb²⁺: 0 VLMs |
| 4 | **EDTA is the most-measured rare-earth ligand** | 596 VLMs across the series |
| 5 | **Charge dominates stability** | Th⁴⁺-EDTA log β = 23.2 vs. ~15–19 for Ln³⁺ |

The lanthanide series is a chemist's dream for studying **systematic trends** — 14 elements with nearly identical chemistry, differing only in ionic radius by ~0.17 Å from La to Lu. That subtle contraction, the **lanthanide contraction**, drives measurable increases in stability constants across the series and is the physical basis for lanthanide separation by ion-exchange chromatography — a process essential for producing the rare earth metals used in permanent magnets, phosphors, and catalysts.

*Source: NIST SRD-46 Critically Selected Stability Constants of Metal Complexes Database*

---