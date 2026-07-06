# Qfree_20260423_144922 -- Result (batch 1)

**Section:** freeform -- Freeform query

**Prompt:** I would like to find a ligand that can complex Fe(III) to stablize the acidic solution (pH<5), yet with limited complexation to Fe(II) so that it is not decreasing free Fe2+ concentration too much. This is for Fe electrodeposition since we also try to minimize hydrodgen evolution reaction when Fe electroeposition happens. Meanwhile, be cautious about ligand pH and its actual state. If there are missing entries, try to observe the similar metal-ligand systems with available data to estimate those. You have unlimited time.

**Tool calls:** 38  |  **Time:** 1362s planning + 650s execution + 0s verdict = 2012s total

---

# Ligand Selection for Fe(III) Stabilization with Minimal Fe(II) Complexation in Acidic Solution (pH < 5)

## Objective Recap
Find a ligand that:
1. **Strongly complexes Fe(III)** → stabilizes Fe³⁺ in acidic solution
2. **Weakly complexes Fe(II)** → keeps Fe²⁺ free for electrodeposition
3. **Is active at pH < 5** → ligand must be at least partially deprotonated
4. **Minimizes hydrogen evolution** → moderate acidity preferred (pH 3–5)

---

## Comprehensive Comparison Table

All data from **NIST SRD-46**, 25 °C (unless noted), log K₁ = log([ML]/[M][L]):

| Ligand | pKₐ values | Active at pH < 5? | log K₁ Fe(III) | log K₁ Fe(II) | Δlog K₁ | Notes |
|--------|-----------|-------------------|----------------|---------------|---------|-------|
| **Citric acid** | 2.90, 4.35, 5.65 | ✅ H₂L⁻/HL²⁻ dominant | **11.27** (I=0.1) | **4.4** (20°C, I=0.1) | **~6.9** | Excellent selectivity; widely used industrially |
| **Oxalic acid** | −1.2, 3.80 | ✅ HL⁻/L²⁻ dominant | **7.58** (I=1.0) | **3.05** (I=1.0) | **4.5** | Good; fully deprotonated above pH 4 |
| **Fluoride (F⁻)** | 2.94 | ✅ F⁻ dominant above pH 3 | **5.17** (I=0.5) | **0.8** (I=1.0) | **~4.4** | Hard base; excellent Fe³⁺ selectivity |
| **Sulfate (SO₄²⁻)** | 1.54 | ✅ Fully deprotonated | **2.80** (I=0.1) | **−2.39** (I=0) | **~5.2** | Weak binding; already present in FeSO₄ baths |
| **Malonic acid** | 2.65, 5.27 | ⚠️ Partially (HL⁻ form) | **7.50** (I=1.0) | **2.24** (I=1.0) | **5.3** | Good selectivity; one carboxyl active at pH 3–5 |
| **D-Tartaric acid** | 2.82, 3.97 | ✅ HL⁻/L²⁻ dominant | **5.73** (I=1.0) | **2.24** (20°C, I=0.1) | **~3.5** | Moderate; hydroxyl group aids Fe³⁺ binding |
| **Acetohydroxamic acid** | 9.29 | ❌ Fully protonated (HL) | **11.42** (20°C, I=0.1) | **4.8** (20°C, I=0.1) | **6.6** | Strong Fe³⁺ binder BUT inactive at pH < 5 |
| **5-Sulfosalicylic acid** | 2.48, 11.85 | ✅ HL²⁻ form active | **~16*** (I=0.1) | **−5.9†** (20°C, I=0.1) | **>10** | Very high selectivity; conditional constants |
| **Salicylic acid** | 2.80, 13.4 | ✅ HL⁻ form active | **~16*** (I=0.1) | **−6.8†** (20°C, I=0.1) | **>10** | Phenolate not deprotonated at pH < 5 |
| **Catechol** | 9.26, 13.3 | ❌ Fully protonated (H₂L) | **20.0** (I=0.1) | **7.9** (I=0.1) | **12.1** | Extremely strong but inactive at pH < 5 |
| **NTA** | 1.1, 1.65, 9.73 | ⚠️ H₂L⁻ form only | **15.87** (I=0.1) | **8.84** (I=0.1) | **7.0** | Strong but also binds Fe²⁺ significantly |
| **Pyrophosphate** | 0.8, 2.2, 6.6, 8.93 | ⚠️ H₂L²⁻ form | **10.4** (I=0.1) | **5.8** (I=0.1) | **4.6** | Moderate; precipitates Fe³⁺ at higher pH |
| **Thiocyanate (SCN⁻)** | −1.1 | ✅ Fully deprotonated | **2.37** (I=0.1) | **1.31** (I=0) | **~1.1** | Too weak and low selectivity |
| **1,10-Phenanthroline** | 4.92 | ⚠️ Partially protonated | **6.5** (20°C, I=0.1) | **5.85** (I=0.1) | **0.65** | Binds Fe²⁺ almost as strongly — unsuitable |
| **Glycine** | 2.33, 9.57 | ❌ Zwitterion; NH₃⁺ form | — | **4.2** (I=3.0) | — | Amine not available at pH < 5 |

\* Salicylate/sulfosalicylate Fe(III) log K₁ values: The database reports conditional constants [ML][H]/[M][HL] ≈ 2.7–2.9. Converting to [ML]/[M][L] using pKₐ₁ ≈ 2.8–2.5 gives log K₁(ML/ML) ≈ 15–16.
† Fe(II) conditional constants [ML][H]/[M][HL] are negative, indicating very weak binding through the protonated form.

---

## Critical Analysis: Protonation State at pH < 5

This is the most important filter. Many ligands with high Fe(III) affinity are **inactive at the target pH**:

- **Catechol** (pKₐ = 9.26): Both −OH groups protonated → no donor atoms available at pH < 5
- **Acetohydroxamic acid** (pKₐ = 9.29): The hydroxamate N−OH is protonated → the enormous log K₁ = 11.4 refers to the **deprotonated L⁻ form** which barely exists below pH 5
- **Glycine** (pKₐ₂ = 9.57): The amine is protonated → only carboxylate available, very weak binding
- **EDTA/NTA**: Amine groups protonated at pH < 5; only carboxylate arms active → effective binding reduced by several log units

Ligands that **are genuinely active** at pH 3–5:
- **Citric acid**: All three carboxylates have pKₐ < 5.65; at pH 4, ~2 carboxylates are deprotonated
- **Oxalic acid**: pKₐ₂ = 3.80; fully deprotonated above pH 4
- **Fluoride**: pKₐ = 2.94; >90% F⁻ above pH 4
- **Sulfosalicylic acid**: pKₐ₁ = 2.48; carboxylate/sulfonate active
- **Salicylic acid**: pKₐ₁ = 2.80; carboxylate active (phenol stays protonated)

---

## Estimation for Missing Data

For ligands where Fe(II) data was missing, I used the **HSAB principle** and analogous systems:

| Ligand | Fe(II) estimate basis | Estimated log K₁ Fe(II) |
|--------|----------------------|------------------------|
| **Sulfosalicylic acid** | Fe(II)-salicylate conditional constant −6.8 → log K₁(ML/ML) ≈ 6–7 using pKₐ correction; but salicylate binds through carboxylate + phenolate, and phenolate is protonated at pH < 5, so **effective Fe(II) binding ≈ 1–2** | ~1–2 (conditional, pH < 5) |
| **Fluoride** (Fe²⁺) | Direct data: log K₁ = 0.8 (I=1.0). Fe²⁺ is a borderline acid, F⁻ is a hard base → weak interaction confirmed | **0.8** (measured) |

---

## 🏆 Top Recommendations

### **1. Citric Acid — Best Overall Choice** ⭐
- **log K₁(Fe³⁺)** = 11.27 vs **log K₁(Fe²⁺)** = 4.4 → **Δ = 6.9 log units**
- At pH 4: citrate exists as H₂L⁻/HL²⁻ with 2 active carboxylates + hydroxyl group
- Fe³⁺ forms very stable [Fe(cit)]⁰ complex preventing hydrolysis/precipitation
- Fe²⁺ binding (log K₁ ≈ 4.4) is moderate — at typical plating concentrations (0.1–0.5 M Fe²⁺), only a small fraction is complexed
- **Widely used in Fe electrodeposition baths** in practice
- Non-toxic, inexpensive, biodegradable

### **2. Fluoride (F⁻) — Simple Inorganic Option**
- **log K₁(Fe³⁺)** = 5.17 vs **log K₁(Fe²⁺)** = 0.8 → **Δ = 4.4 log units**
- pKₐ = 2.94 → fully active above pH 3
- Hard base perfectly matched to hard acid Fe³⁺; negligible Fe²⁺ binding
- **Caution**: HF toxicity; corrosive; limited to specialized applications

### **3. Oxalic Acid — Strong Chelator**
- **log K₁(Fe³⁺)** = 7.58 vs **log K₁(Fe²⁺)** = 3.05 → **Δ = 4.5 log units** (at I=1.0)
- pKₐ₂ = 3.80 → fully deprotonated above pH 4
- Forms stable [Fe(ox)]⁺ and [Fe(ox)₂]⁻ complexes
- **Caution**: Fe(III)-oxalate is photosensitive; oxalate can precipitate as CaC₂O₄ if Ca²⁺ present

### **4. 5-Sulfosalicylic Acid — High Selectivity**
- Fe(III) conditional log K [ML][H]/[M][HL] = 2.7 at 25°C → true log K₁ ≈ 14–16
- Fe(II) binding extremely weak (conditional constant −5.9)
- pKₐ₁ = 2.48 → carboxylate/sulfonate active at pH 3–5
- **Selectivity Δ > 10 log units** — the highest among practical candidates
- Used as Fe(III) indicator in analytical chemistry
- **Caution**: Phenolate group (pKₐ = 11.85) is protonated at pH < 5, so binding is through carboxylate only; the enormous selectivity partly reflects Fe³⁺'s ability to force phenolate deprotonation

### **5. Malonic Acid — Moderate Alternative**
- **log K₁(Fe³⁺)** = 7.50 vs **log K₁(Fe²⁺)** = 2.24 → **Δ = 5.3 log units** (at I=1.0)
- pKₐ₁ = 2.65 → one carboxylate active at pH 3; both active above pH 5.3
- Good compromise between binding strength and selectivity

---

## Ligands to AVOID for This Application

| Ligand | Reason |
|--------|--------|
| **1,10-Phenanthroline / 2,2'-Bipyridyl** | Binds Fe²⁺ almost as strongly as Fe³⁺ (Δ < 1); would sequester Fe²⁺ |
| **EDTA / NTA** | Very strong Fe²⁺ binding (log K₁ = 14.3 / 8.84); would deplete free Fe²⁺ |
| **Catechol** | Inactive at pH < 5 (pKₐ = 9.26); also binds Fe²⁺ strongly (log K₁ = 7.9) |
| **Acetohydroxamic acid** | pKₐ = 9.29 → inactive at pH < 5 despite excellent intrinsic selectivity |
| **Thiocyanate** | Too weak (log K₁ Fe³⁺ = 2.4) and low selectivity (Δ = 1.1) |

---

## Summary & Practical Recommendation

**Citric acid is the recommended ligand** for Fe electrodeposition at pH 3–5. It offers:

- The **largest practical selectivity** (Δlog K₁ ≈ 6.9) among ligands that are genuinely active at pH < 5
- Sufficient Fe(III) binding (log K₁ = 11.3) to prevent Fe(OH)₃ precipitation
- Moderate Fe(II) binding (log K₁ = 4.4) that leaves most Fe²⁺ free at typical plating concentrations
- All three carboxylate groups progressively deprotonate between pH 2.9–5.7, providing buffering capacity in the target pH range
- The hydroxyl group provides an additional hard-donor site that preferentially stabilizes Fe³⁺ (hard acid) over Fe²⁺ (borderline acid)

For applications where even lower Fe²⁺ complexation is needed, **fluoride** (Δ = 4.4, but Fe²⁺ log K₁ = 0.8 — essentially no binding) or **sulfosalicylic acid** (Δ > 10) are alternatives, though with practical limitations (HF toxicity; SSA cost).

*All stability constants from NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes).*
