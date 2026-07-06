# Irving–Williams Series: Violations Found in NIST SRD-46

## Background

The Irving–Williams series predicts that divalent first-row transition metal complexes should follow this stability ordering:

**Mn²⁺ < Fe²⁺ < Co²⁺ < Ni²⁺ < Cu²⁺ > Zn²⁺**

This trend arises from increasing effective nuclear charge and decreasing ionic radius across the period, with Cu²⁺ anomalously high due to Jahn–Teller distortion, and Zn²⁺ dropping back because its filled d¹⁰ shell provides no crystal-field stabilization energy (CFSE).

---

## Data: log β₁ Values Across Five Metals (β-def 812: M + L ⇌ ML, T = 20–30 °C)

*Fe²⁺ data were absent from this ligand set in the database (likely due to oxidation complications in measurement), so the comparison covers 5 metals. Violations are flagged relative to the expected partial order Mn < Co < Ni < Cu > Zn.*

| Ligand | Mn²⁺ | Co²⁺ | Ni²⁺ | Cu²⁺ | Zn²⁺ | Violations? |
|--------|-------|-------|-------|-------|-------|-------------|
| Glycine | 2.77 | 4.79 | 5.77 | 8.13 | 5.00 | ✅ None |
| Histidine | 3.44 | 6.92 | 8.70 | 10.17 | 6.51 | ✅ None |
| Ethylenediamine | 2.73 | 5.89 | 7.52 | 10.67 | 5.71 | ✅ None |
| 1,10-Phenanthroline | 3.88 | 7.25 | 8.80 | 9.25 | 6.55 | ✅ None |
| NTA | 7.44 | 10.38 | 11.54 | 12.96 | 10.66 | ✅ None |
| Acetylacetone | 4.24 | 5.40 | 6.10 | 8.27 | 5.11 | ✅ None |
| Citric acid | 3.67 | 4.83 | 5.40 | 5.90 | 4.98 | ✅ None |
| Tyrosine | 2.67 | 4.62 | 5.76 | 8.68 | 4.99 | ✅ None |
| Serine | 2.53 | 4.38 | 5.49 | 8.15 | 4.71 | ✅ None |
| Ammonia | 1.00 | 2.11 | 2.75 | 4.31 | 2.37 | ✅ None |
| **ADP** | **3.94** | **4.69** | **4.68** | **6.08** | **4.67** | ⚠️ **Ni²⁺ < Co²⁺; Zn²⁺ < Ni²⁺** |
| **Hydroxide** | **3.40** | **4.35** | **4.14** | **6.30** | **5.04** | ⚠️ **Ni²⁺ < Co²⁺; Zn²⁺ > Ni²⁺** |
| **Tiron** | **5.00** | **6.00** | **6.00** | **7.70** | **5.70** | ⚠️ **Ni²⁺ = Co²⁺ (no rise)** |
| **Maltol** | **3.35** | **4.15** | **4.35** | **6.15** | **4.15** | ⚠️ **Zn²⁺ = Co²⁺** |
| **Kojic acid** | **3.50** | **4.25** | **4.75** | **6.65** | **4.65** | ⚠️ **Zn²⁺ ≈ Ni²⁺** |
| **Fluoride** | **1.36** | **1.30** | **1.23** | **1.23** | **1.15** | ⚠️ **Mn²⁺ > Co²⁺ > Ni²⁺ ≈ Cu²⁺ — full reversal** |
| **Sulfate** | **2.28** | **2.36** | **2.29** | **2.36** | **2.37** | ⚠️ **Nearly flat; no meaningful ordering** |
| **Nitrate** | **0.30** | **0.30** | **0.40** | **0.50** | **0.30** | ⚠️ **Mn²⁺ = Co²⁺ = Zn²⁺; Ni²⁺ > Co²⁺ anomalous** |

---

## Violations Summary

### 1. 🔴 Fluoride — Full Reversal of the Series
**Observed order: Mn²⁺ (1.36) > Co²⁺ (1.30) > Ni²⁺ (1.23) ≈ Cu²⁺ (1.23) > Zn²⁺ (1.15)**

This is the most dramatic violation — the series is essentially *inverted*. Fluoride is a hard donor (HSAB theory), and hard–hard interactions favor metals with higher charge density and more ionic character. Mn²⁺, with its half-filled d⁵ shell and relatively large ionic radius, forms more ionic bonds with F⁻ than the later, softer metals. Cu²⁺ loses its Jahn–Teller advantage entirely because the axial Cu–F bonds are elongated and weakened. This is a textbook example of HSAB overriding CFSE.

### 2. 🟠 ADP — Ni²⁺ ≈ Co²⁺ (Collapse of the Co→Ni Rise)
**Observed: Mn (3.94) < Co (4.69) ≈ Ni (4.68) < Cu (6.08) > Zn (4.67)**

ADP is a bulky, flexible polyphosphate ligand. The expected Co→Ni rise disappears. Ni²⁺ is kinetically inert (substitution-slow, d⁸ character in octahedral field) and may not achieve the optimal coordination geometry with the sterically demanding triphosphate backbone. Co²⁺, being more labile, can adapt more readily.

### 3. 🟠 Hydroxide — Ni²⁺ < Co²⁺ and Zn²⁺ > Ni²⁺
**Observed: Mn (3.40) < Co (4.35) > Ni (4.14) < Cu (6.30) < Zn (5.04)**

Hydroxide is a hard, compact donor. The Ni²⁺ < Co²⁺ inversion here may reflect the tendency of Ni²⁺ to form polynuclear hydroxo-bridged species rather than simple ML complexes, reducing the apparent log β₁. The Zn²⁺ > Ni²⁺ ordering is also notable: Zn²⁺ has a strong affinity for OH⁻ due to its Lewis acidity and the thermodynamic drive toward Zn(OH)₂ precipitation.

### 4. 🟡 Tiron (catecholate-type) — Ni²⁺ = Co²⁺
**Observed: Mn (5.00) < Co (6.00) = Ni (6.00) < Cu (7.70) > Zn (5.70)**

The catecholate oxygen donors in Tiron are hard donors that partially neutralize the CFSE advantage of Ni²⁺ over Co²⁺. The chelate ring geometry may also be better optimized for Co²⁺ (which can be tetrahedral or octahedral) than for Ni²⁺ (strongly prefers octahedral).

### 5. 🟡 Maltol & Kojic acid — Zn²⁺ ≈ Co²⁺ or Ni²⁺
**Maltol: Zn (4.15) = Co (4.15); Kojic acid: Zn (4.65) ≈ Ni (4.75)**

These hydroxypyrone ligands bind via O,O-chelation. Zn²⁺ is known to form unusually stable complexes with hard oxygen donors due to its d¹⁰ configuration and flexible coordination geometry (tetrahedral or octahedral). The expected Zn²⁺ < Ni²⁺ drop is suppressed or eliminated.

---

## Hypotheses for the Exceptions

| Violation Type | Root Cause |
|----------------|------------|
| **Fluoride / hard-O donors reversing the series** | HSAB hard–hard interactions favor Mn²⁺ and Zn²⁺ over soft-leaning late metals; CFSE advantage of Ni²⁺/Cu²⁺ is irrelevant for purely ionic bonding |
| **Ni²⁺ ≈ Co²⁺ with bulky/flexible ligands (ADP)** | Kinetic inertness of Ni²⁺ and steric mismatch suppress its thermodynamic CFSE advantage |
| **Zn²⁺ anomalously high with O-donor chelates** | Zn²⁺ d¹⁰ configuration allows flexible geometry; strong Lewis acidity toward hard O-donors compensates for lack of CFSE |
| **Hydroxide inversions** | Polynuclear hydroxo-complex formation by Ni²⁺ reduces apparent mononuclear β₁; Zn²⁺ has exceptional affinity for OH⁻ |
| **Weak ligands (sulfate, nitrate) — flat ordering** | When log β₁ < ~2.5, differences are within experimental error; the series only manifests clearly for moderate-to-strong donors |

---

## Key Takeaway

The Irving–Williams series is a *statistical trend*, not a universal law. It holds robustly for N-donor and mixed N,O-donor ligands of moderate denticity (glycine, en, histidine, NTA, phen all conform perfectly). Violations emerge when:

1. **Ligand hardness** (F⁻, OH⁻, catecholates) shifts the dominant interaction from covalent/CFSE to ionic/HSAB.
2. **Steric or geometric constraints** (ADP, polyphosphates) penalize the kinetically inert Ni²⁺.
3. **Zn²⁺ Lewis acidity** toward hard O-donors is underestimated by the simple CFSE model.

*Source: NIST SRD-46 stability constant database; all log β₁ values from β-def 812 (M + L ⇌ ML), aqueous solution, T = 20–30 °C, averaged over available measurements.*

---