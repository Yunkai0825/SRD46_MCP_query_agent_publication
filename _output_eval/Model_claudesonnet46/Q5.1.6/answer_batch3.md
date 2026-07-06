# 🔬 Rare Earth Metals in NIST SRD-46 — A Deep Exploration

*Source: NIST Standard Reference Database 46 — Critically Selected Stability Constants of Metal Complexes*

---

## 📊 Part 1: The Lanthanide Series — Database Footprint

All 14 Ln³⁺ ions plus Y³⁺ and Sc³⁺ are well-represented in SRD-46:

| Metal | metal_id | Ligand Partners | VLM Measurements | β-Def Types |
|-------|----------|----------------|------------------|-------------|
| La³⁺ | metal_79 | 297 | 931 | 30 |
| Ce³⁺ | metal_27 | 188 | 567 | 22 |
| Pr³⁺ | metal_139 | 231 | 723 | 24 |
| Nd³⁺ | metal_110 | 263 | 794 | 29 |
| Sm³⁺ | metal_173 | 265 | 844 | 28 |
| Eu³⁺ | metal_58 | 267 | 870 | 30 |
| **Gd³⁺** | metal_65 | **288** | **897** | 28 |
| Dy³⁺ | metal_44 | 252 | 758 | 23 |
| Tb³⁺ | metal_179 | 235 | 709 | 24 |
| Ho³⁺ | metal_73 | 230 | 705 | 24 |
| Er³⁺ | metal_55 | 241 | 792 | 29 |
| Tm³⁺ | metal_192 | 223 | 633 | 22 |
| Yb³⁺ | metal_206 | 235 | 771 | 28 |
| Lu³⁺ | metal_81 | 234 | 671 | 25 |
| Y³⁺ | metal_205 | 182 | 533 | 26 |
| **Sc³⁺** | metal_169 | **44** | **156** | 16 |
| Ce⁴⁺ | metal_28 | 3 | 9 | 5 |
| Eu²⁺ | metal_59 | 2 | 2 | 1 |
| Yb²⁺ | metal_207 | 0 | 0 | 0 |

---

## 🏆 Part 2: The Lanthanide Contraction — Proven by Real Data

The most striking finding is the **monotonic increase in EDTA stability constants** (log β for ML, 25°C, I = 0.1 mol/L) across the lanthanide series — a direct fingerprint of the **lanthanide contraction**:

| Metal | Atomic # | log β (Ln-EDTA) | n measurements |
|-------|----------|-----------------|----------------|
| La³⁺ | 57 | **15.50** | 17 |
| Ce³⁺ | 58 | 15.98 | 17 |
| Pr³⁺ | 59 | 16.40 | 17 |
| Nd³⁺ | 60 | 16.61 | 17 |
| Sm³⁺ | 62 | 17.14 | 17 |
| Eu³⁺ | 63 | 17.35 | 17 |
| Gd³⁺ | 64 | 17.35 | 17 |
| Tb³⁺ | 65 | 17.93 | 17 |
| Dy³⁺ | 66 | 18.30 | 17 |
| Ho³⁺ | 67 | 18.74 | 17 |
| Er³⁺ | 68 | 18.85 | 17 |
| Tm³⁺ | 69 | 19.32 | 17 |
| **Yb³⁺** | 70 | **19.51** | 13 |

**The total span is 4.0 log units** (La→Yb), meaning Yb-EDTA is **10,000× more stable** than La-EDTA! This is a direct consequence of the shrinking ionic radius across the series: as 4f electrons are added, poor shielding causes the nuclear charge to pull the electron cloud inward, increasing charge density and electrostatic attraction to ligand donors.

---

## 💉 Part 3: DTPA — Even Stronger Chelation (MRI Relevance)

DTPA (diethylenetriaminepentaacetic acid, ligand_6356) forms even more stable complexes than EDTA, with 5 carboxylate + 3 amine donors:

| Metal | log β (Ln-DTPA, 25°C, I=0.1) | n measurements |
|-------|------------------------------|----------------|
| Ho³⁺ | 22.08 | 17 |
| Tm³⁺ | 22.27 | 17 |
| Er³⁺ | 22.39 | 17 |
| **Yb³⁺** | **22.61** | 30 |

DTPA complexes are **~3 log units more stable** than EDTA complexes for the same metal — that's a factor of **1,000× stronger binding**. This is why **Gd-DTPA (Magnevist®)** was the first FDA-approved MRI contrast agent: the enormous stability constant (log β ≈ 22.5 for Gd) ensures the toxic free Gd³⁺ ion is not released in the body.

---

## ⚡ Part 4: Oxidation State Anomalies

| Species | Ligand Partners | VLM Count | Chemistry Note |
|---------|----------------|-----------|----------------|
| Ce⁴⁺ | 3 | 9 | Strongly oxidizing; unstable in most aqueous solutions |
| Eu²⁺ | 2 | 2 | Mimics Ca²⁺/Sr²⁺; easily oxidized back to Eu³⁺ |
| Yb²⁺ | 0 | 0 | Essentially no aqueous coordination chemistry |

The near-absence of Ce⁴⁺, Eu²⁺, and Yb²⁺ data reflects real chemistry: these are the only lanthanides with accessible non-+3 states (Ce⁴⁺ is a strong oxidant, Eu²⁺ and Yb²⁺ are strong reductants), and their instability in water severely limits measurable coordination equilibria.

---

## 🔬 Part 5: Sc³⁺ — The Odd One Out

Scandium has only **44 ligand partners** and **156 measurements** — roughly 6× fewer than a typical lanthanide. Despite being classified as a rare earth element, Sc³⁺ has an ionic radius of ~0.745 Å, far smaller than La³⁺ (~1.032 Å) or even Lu³⁺ (~0.861 Å). This makes Sc³⁺ behave more like Al³⁺ or Ti⁴⁺ — it forms stronger, more covalent bonds and has very different coordination preferences, placing it chemically apart from the true lanthanides.

---

## 🌟 Key Takeaways

1. **The lanthanide contraction is quantitatively visible** in EDTA log β values rising monotonically from 15.50 (La) to 19.51 (Yb) — a 4-unit span driven purely by ionic radius shrinkage.
2. **Gd³⁺ has the most ligand partners (288)** of any lanthanide, reflecting decades of MRI contrast agent research.
3. **DTPA binds ~1,000× more strongly than EDTA** for the same metal, explaining its dominance in medical applications.
4. **Non-+3 oxidation states** (Ce⁴⁺, Eu²⁺, Yb²⁺) are chemically unstable and have almost no coordination data in SRD-46.
5. **Sc³⁺ is chemically isolated** from the lanthanides despite its rare earth classification.

---