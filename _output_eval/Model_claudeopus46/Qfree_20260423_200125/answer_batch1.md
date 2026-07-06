# Qfree_20260423_200125 -- Result (batch 1)

**Section:** freeform -- Fe(III)/Fe(II) ligand selection (corrected)

**Prompt:** I would like to find ligands that can complex Fe(III) to stabilize the acidic solution (pH<5), yet with limited complexation to Fe(II) so that it does not decrease the free Fe2+ concentration too much. This is for Fe electrodeposition since we also try to minimize the hydrogen evolution reaction when Fe electrodeposition happens. The expected concentration of Fe(II) is ~0.1M. Meanwhile, be cautious about ligand pH and its actual state, and be cautious about possible precipitations. If there are missing entries, try to observe similar metal-ligand systems with available data to estimate those with very robust reasons and explanations. You have unlimited time and unlimited turns.

**Tool calls:** 94  |  **Time:** 8018s planning + 356s execution + 0s verdict = 8374s total

---

Now I have all the key data for acetohydroxamic acid (AHA):

**Fe³⁺-AHA (L⁻ = deprotonated hydroxamate):**
- logK₁ = 11.38-11.42 (20-25°C, I=0.1M)
- logβ₂ = 21.1 (20°C, I=0.1M)
- logβ₃ = 28.3 (20°C, I=0.1M)

**Fe²⁺-AHA:**
- logK₁ = 4.8 (20°C, I=0.1M)
- logβ₂ = 8.5 (20°C, I=0.1M)

**ΔlogK₁ = 6.6** — excellent selectivity!

But AHA pKa = 9.29, so at pH < 5, the ligand is fully protonated (HL). The conditional constant at pH 3 would be:
- Fe³⁺: logK₁_cond = 11.42 - 9.29 + pH = 11.42 - 9.29 + 3 = 5.13 → still significant!
- Fe²⁺: logK₁_cond = 4.8 - 9.29 + 3 = -1.49 → negligible!

Wait, that's not right. The equilibrium is M + L⁻ ⇌ ML, and at pH < 5, [L⁻] = [HL]_total × 10^(pH-pKa). So:

logK_cond = logK + log(αL) where αL = [L⁻]/[L]_total = 10^(pH-pKa)/(1+10^(pH-pKa))

At pH 3: αL = 10^(3-9.29) = 10^(-6.29), so log(αL) ≈ -6.29

- Fe³⁺: logK₁_cond = 11.42 - 6.29 = **5.13** → K_cond = 1.3×10⁵ — significant!
- Fe²⁺: logK₁_cond = 4.8 - 6.29 = **-1.49** → K_cond = 0.032 — negligible!

At pH 4: αL = 10^(-5.29), so:
- Fe³⁺: logK₁_cond = 11.42 - 5.29 = **6.13** → K_cond = 1.3×10⁶ — strong!
- Fe²⁺: logK₁_cond = 4.8 - 5.29 = **-0.49** → K_cond = 0.32 — still negligible!

This is **outstanding** selectivity at pH < 5! The protonation of AHA actually HELPS the selectivity because it suppresses the already-weak Fe²⁺ binding much more than the strong Fe³⁺ binding.

Now I have all the data needed for a comprehensive recommendation. Let me compile the final analysis.

---

# Ligand Recommendations for Fe Electrodeposition: Selective Fe(III) Complexation at pH < 5

## Problem Summary

For Fe electrodeposition from acidic solution (pH < 5, ~0.1 M Fe²⁺):
1. **Stabilize Fe³⁺** — prevent Fe(OH)₃ precipitation (Ksp ≈ 10⁻³⁹; precipitates at [Fe³⁺] > 10⁻⁶ M at pH 3)
2. **Preserve free Fe²⁺** — avoid depleting the electroactive species
3. **Minimize HER** — complexing Fe³⁺ reduces its parasitic reduction, shifting potential
4. **Acidic stability** — ligand must function at pH < 5

### Key Thermodynamic Criterion
We need ligands with:
- **High conditional logK(Fe³⁺)** at pH < 5 → effective Fe³⁺ sequestration
- **Low conditional logK(Fe²⁺)** at pH < 5 → free [Fe²⁺] ≈ 0.1 M preserved
- **Large ΔlogK = logK(Fe³⁺) − logK(Fe²⁺)** → selectivity

The conditional stability constant accounts for ligand protonation: logK_cond = logK_intrinsic + log(αL), where αL is the fraction of ligand in the binding form at the working pH.

---

## Comprehensive Ligand Comparison

All data from NIST SRD-46. Intrinsic logK₁ values are for M + L^n⁻ ⇌ ML (fully deprotonated ligand). Conditional values estimated at pH 3 and pH 4.

| Ligand | pKa (relevant) | logK₁(Fe³⁺) | logK₁(Fe²⁺) | ΔlogK₁ | Cond. logK Fe³⁺ pH 3 | Cond. logK Fe³⁺ pH 4 | Cond. logK Fe²⁺ pH 3 | Cond. logK Fe²⁺ pH 4 | Precipitation Risk | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **Acetohydroxamic acid (AHA)** | 9.29 | 11.42 | 4.8 | **6.6** | **5.1** | **6.1** | −1.5 | −0.5 | Low | ⭐ **Top pick** |
| **Oxalic acid** | 1.04, 3.82 | 7.58 | 3.05 | **4.5** | **5.4** | **6.8** | 0.9 | 2.3 | ⚠️ FeC₂O₄·2H₂O | Good but ppt risk |
| **Citric acid** | 3.13, 4.76, 6.40 | 11.2 | 3.2–4.4 | **6.8–8.0** | **4.0** | **6.2** | −4.0 | −1.6 | Low | ⭐ **Excellent** |
| **Malonic acid** | 2.65, 5.28 | 8.12 | 2.24 | **5.9** | **4.5** | **6.1** | −1.4 | 0.2 | Low | ⭐ **Very good** |
| **Tartaric acid** | 2.82, 3.95 | 6.49–6.66 | 2.24 | **4.3–4.4** | **4.5** | **5.9** | 0.2 | 1.5 | Low | Good |
| **Sulfosalicylic acid (SSA)** | 2.48, 11.85 | ~10 (vs L²⁻) | 5.40 (vs HL⁻) | **~3.3** (vs HL) | **~2.7** | **~3.7** | ~0.4 | ~1.4 | Low | Moderate |
| **Fluoride** | 2.94 (HF) | 5.17 | 0.8 | **4.4** | **5.2** | **5.2** | 0.8 | 0.8 | Low | Good but toxic |
| **Sulfate** | 1.54 | 2.80 | ~2.3 | **~0.5** | **2.8** | **2.8** | ~2.3 | ~2.3 | Low | Poor selectivity |
| **Phosphate** | 2.15, 7.09 | 3.47 (H₂PO₄⁻) | 0.55 (H₂PO₄⁻) | **2.9** | **3.5** | **3.5** | 0.6 | 0.6 | ⚠️ FePO₄ | Moderate, ppt risk |
| **Gluconic acid** | 3.46 | 3.1 | −1.0 to 1.5 | **1.6–4.1** | **2.6** | **3.1** | <0 | <0 | Low | Too weak |
| **EDTA** | 2.0, 2.7, 6.2, 10.3 | 25.1 | 14.3 | **10.8** | ~8 | ~12 | ~0 | ~4 | Low | Fe²⁺ binding too strong |
| **NTA** | 1.0, 1.8, 2.5, 9.46 | 15.9 | 8.9 | **7.0** | ~3 | ~5 | ~−4 | ~−2 | Low | Marginal |
| **1,10-Phenanthroline** | 4.92 | 6.5 | 5.85 (logβ₃=21) | **−14.6** (β₃) | — | — | — | — | Low | ❌ Binds Fe²⁺ more! |
| **Catechol** | 9.26, 13.3 | 20.4 (vs L²⁻) | 8.3 (vs L²⁻) | **12.1** | ~−2.2 (vs H₂L) | ~0.8 | ~−14 | ~−12 | Low | Too weak at pH<5 |

*Conditional logK values are approximate, calculated as logK_intrinsic − Σ(pKa − pH) for protons that must be displaced. For diprotic ligands like oxalate, the correction depends on which protonation state dominates.*

---

## Detailed Analysis of Top Candidates

### ⭐ 1. Acetohydroxamic Acid (AHA) — **Best Overall Pick**

| Property | Value | Source |
|---|---|---|
| Formula | CH₃C(O)NHOH | — |
| pKa | 9.29 | SRD-46 |
| Fe³⁺ logK₁ (M+L⁻⇌ML) | 11.42 (20°C, I=0.1M) | vlm_168448 |
| Fe³⁺ logβ₂ | 21.1 (20°C, I=0.1M) | vlm_168453 |
| Fe³⁺ logβ₃ | 28.3 (20°C, I=0.1M) | vlm_168455 |
| Fe²⁺ logK₁ (M+L⁻⇌ML) | 4.8 (20°C, I=0.1M) | vlm_168432 |
| Fe²⁺ logβ₂ | 8.5 (20°C, I=0.1M) | vlm_168433 |
| ΔlogK₁ | **6.6** | — |

**Why AHA is ideal:**
- **Protonation works in your favor**: At pH 3, only ~10⁻⁶·³ fraction of AHA is deprotonated (L⁻). This dramatically suppresses Fe²⁺ binding (conditional logK₁ ≈ −1.5) while Fe³⁺ still binds effectively (conditional logK₁ ≈ 5.1) because Fe³⁺ is a much harder Lewis acid that can displace the proton from the hydroxamic group.
- **No precipitation risk**: Fe(III)-hydroxamate complexes are highly soluble (this is how siderophores work in biology).
- **Redox-inert**: Unlike ascorbate, AHA does not reduce Fe³⁺.
- **Simple, commercially available, non-toxic**.

**Speciation estimate at pH 3, 0.1 M Fe²⁺, 0.1 M AHA, trace Fe³⁺:**
- Fe²⁺: K_cond = 10⁻¹·⁵ = 0.032 → [FeL⁺]/[Fe²⁺][L_total] ≈ 0.032 → **>99% Fe²⁺ remains free** ✓
- Fe³⁺: K_cond = 10⁵·¹ = 1.3×10⁵ → with 0.1 M AHA, virtually all Fe³⁺ is complexed ✓

**At pH 4:**
- Fe²⁺: K_cond = 10⁻⁰·⁵ = 0.32 → ~3% complexed at 0.1M AHA → **~97% Fe²⁺ free** ✓
- Fe³⁺: K_cond = 10⁶·¹ → all Fe³⁺ complexed ✓

### ⭐ 2. Citric Acid — **Excellent, Widely Available**

| Property | Value | Source |
|---|---|---|
| Formula | C₆H₈O₇ (H₃L) | — |
| pKa₁, pKa₂, pKa₃ | 3.13, 4.76, 6.40 | SRD-46 |
| Fe³⁺ logK₁ (M+L³⁻⇌ML) | 11.2 (25°C, I=0.1M) | SRD-46 |
| Fe²⁺ logK₁ (M+L³⁻⇌ML) | 3.2–4.4 (20-25°C, I=0.1M) | SRD-46 |
| Fe²⁺ logK (M+HL⇌MHL) | 2.6–2.9 | SRD-46 |
| ΔlogK₁ | **6.8–8.0** | — |

**Why citric acid works well:**
- At pH 3–4, citrate exists as H₂L⁻/H₃L. The conditional Fe³⁺ binding is still significant (~logK_cond ≈ 4–6) because Fe³⁺ can chelate through the carboxylate and hydroxyl groups even in protonated forms.
- Fe²⁺ binding at pH < 5 is very weak (conditional logK < 0) — free Fe²⁺ is preserved.
- **No precipitation risk** — Fe(III)-citrate complexes are highly soluble.
- **Cheap, food-grade, non-toxic, widely used in electroplating**.
- Caution: dinuclear Fe₂(OH)₂(cit)₂ species can form at higher Fe³⁺ concentrations.

### ⭐ 3. Malonic Acid — **Very Good, Simple**

| Property | Value | Source |
|---|---|---|
| Formula | CH₂(COOH)₂ (H₂L) | — |
| pKa₁, pKa₂ | 2.65, 5.28 | SRD-46 |
| Fe³⁺ logK₁ (M+L²⁻⇌ML) | 8.12 (25°C, I=0.1M) | SRD-46 |
| Fe³⁺ logβ₂ | 14.00 (25°C, I=0.1M) | SRD-46 |
| Fe²⁺ logK₁ (M+L²⁻⇌ML) | 2.24 (25°C, I=1M) | SRD-46 |
| ΔlogK₁ | **5.9** | — |

**Why malonic acid is good:**
- At pH 3–4, malonate is partially deprotonated (HL⁻ dominant between pH 2.65–5.28), providing good availability for Fe³⁺ complexation.
- Conditional Fe³⁺ logK at pH 3 ≈ 4.5 — adequate for Fe³⁺ stabilization.
- Fe²⁺ binding is very weak (conditional logK < 0 at pH 3) — free Fe²⁺ preserved.
- **No precipitation risk** — Fe(III)-malonate complexes are soluble.
- Simple bidentate chelate ring (6-membered) — kinetically labile, good for dynamic equilibrium.

### 4. Oxalic Acid — **Good Selectivity but Precipitation Risk**

| Property | Value | Source |
|---|---|---|
| pKa₁, pKa₂ | 1.04, 3.82 | SRD-46 |
| Fe³⁺ logK₁ | 7.58 (25°C, I=1M) | SRD-46 |
| Fe³⁺ logβ₃ | 18.6 (25°C, I=1M) | SRD-46 |
| Fe²⁺ logK₁ | 3.05 (25°C, I=1M) | SRD-46 |
| ΔlogK₁ | **4.5** | — |

**⚠️ Critical concern: FeC₂O₄·2H₂O precipitation**
- Iron(II) oxalate dihydrate (humboldtine) has Ksp ≈ 2×10⁻⁷.
- At 0.1 M Fe²⁺, precipitation occurs when [C₂O₄²⁻] > 2×10⁻⁶ M.
- At pH 3 with 0.1 M total oxalate: [C₂O₄²⁻] ≈ 0.1 × 10^(3−3.82) ≈ 0.015 M → **precipitation WILL occur!**
- **Oxalic acid is NOT recommended** unless used at very low concentrations (<10⁻⁴ M), which limits its Fe³⁺ stabilization capacity.

### 5. Tartaric Acid — **Good, Safe Choice**

| Property | Value | Source |
|---|---|---|
| pKa₁, pKa₂ | 2.82, 3.95 | SRD-46 |
| Fe³⁺ logK₁ | 6.49–6.66 (20-25°C, I=0.1M) | SRD-46 |
| Fe²⁺ logK₁ | 2.24 (20°C, I=0.1M) | SRD-46 |
| ΔlogK₁ | **4.3** | — |

- Moderate Fe³⁺ binding, weak Fe²⁺ binding.
- Both pKa values < 5, so tartrate is substantially deprotonated at pH 3–5 — good ligand availability.
- No precipitation risk. Widely used in electroplating.
- Slightly weaker Fe³⁺ binding than citrate or malonate.

---

## Ligands to AVOID

| Ligand | Reason |
|---|---|
| **EDTA** | Fe²⁺ logK₁ = 14.3 — binds Fe²⁺ too strongly, would deplete free Fe²⁺ |
| **1,10-Phenanthroline** | Fe²⁺ logβ₃ = 21 > Fe³⁺ logβ₃ = 14 — preferentially sequesters Fe²⁺! |
| **NTA** | Fe²⁺ logK₁ = 8.9 — significant Fe²⁺ depletion at 0.1 M |
| **Oxalic acid** | FeC₂O₄·2H₂O precipitation at 0.1 M Fe²⁺ |
| **Ascorbic acid** | Reduces Fe³⁺ → Fe²⁺ (redox-active), defeating the purpose |
| **Phosphate** | FePO₄ precipitation risk (Ksp ≈ 10⁻²²) |
| **Catechol** | pKa₁ = 9.26 → fully protonated at pH < 5, negligible binding |
| **Glycine** | Too weak Fe³⁺ binding at pH < 5 (conditional logK ≈ 2) |

---

## Estimation for Missing Fe(II) Data

For several hydroxamic acids, Fe(II) data is missing in SRD-46. We can estimate based on:

1. **AHA benchmark**: Fe³⁺ logK₁ = 11.4, Fe²⁺ logK₁ = 4.8, ΔlogK = 6.6
2. **HSAB principle**: Hydroxamic acids are hard O,O-donors that strongly prefer hard Fe³⁺ over softer Fe²⁺
3. **Irving-Williams series**: For a given ligand, logK typically follows Mn²⁺ < Fe²⁺ < Co²⁺ < Ni²⁺ < Cu²⁺ > Zn²⁺

For **nitrilotriacetohydroxamic acid (NTAHA)**, Fe³⁺ logK₁ = 19.4:
- Estimated Fe²⁺ logK₁ ≈ 19.4 − 6.6 ≈ **12.8** (using AHA ΔlogK)
- This would be too strong for Fe²⁺ — would deplete free Fe²⁺
- However, NTAHA pKa values (5.92, 6.81, 8.84) mean at pH < 5, the ligand is fully protonated → conditional Fe²⁺ binding negligible

For **4-nitrocatechol** (Fe³⁺ + H₂L ⇌ FeL + 2H⁺, logK = −2.0):
- Using catechol ΔlogK ≈ 12: Fe²⁺ + H₂L ⇌ FeL + 2H⁺, logK ≈ −14
- At pH 3: conditional Fe³⁺ logK ≈ −2 + 2×3 = 4; Fe²⁺ logK ≈ −14 + 6 = −8
- Excellent selectivity but moderate Fe³⁺ binding

---

## Final Recommendations

### Primary Recommendation: **Acetohydroxamic Acid (AHA)**
- Best balance of Fe³⁺ selectivity (ΔlogK = 6.6), adequate conditional binding at pH 3–5, no precipitation, redox stability, and commercial availability.
- Suggested concentration: 0.05–0.2 M (adjust based on expected Fe³⁺ concentration)
- At pH 3–4 with 0.1 M AHA: >99% Fe²⁺ remains free, virtually all Fe³⁺ complexed

### Secondary Recommendation: **Citric Acid**
- Excellent selectivity (ΔlogK