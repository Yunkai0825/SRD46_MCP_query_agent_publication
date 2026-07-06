## Final Answer

All the data I need is in hand. Here is the complete analysis.

---

## Calcium Oxalate Precipitation: pH Threshold Analysis

### 1. Oxalic Acid pKa Values (25 °C, I = 0.1 M, SRD-46)

| Step | Equilibrium | pKa |
|------|-------------|-----|
| pKa₁ | H₂C₂O₄ ⇌ HC₂O₄⁻ + H⁺ | −1.2 |
| pKa₂ | HC₂O₄⁻ ⇌ C₂O₄²⁻ + H⁺ | **3.8** |

The fully deprotonated oxalate dianion (C₂O₄²⁻) — the species that precipitates Ca²⁺ — becomes dominant only **above pH ≈ 3.8**.

---

### 2. Ca²⁺–Oxalate Constants (SRD-46)

| Species | β definition | logK | T (°C) | I (M) |
|---------|-------------|------|--------|-------|
| CaC₂O₄·H₂O (s) — monohydrate | Ksp (beta_def_327) | **−8.75** | 25 | 0 |
| CaC₂O₄·H₂O (s) — monohydrate | Ksp (beta_def_327) | −7.86 | 25 | 0.1 |
| CaC₂O₄·3H₂O (s) — trihydrate | Ksp (beta_def_307) | −8.32 | 25 | 0 |
| Ca(C₂O₄)aq complex | β₁ (beta_def_812) | **3.19** | 25 | 0 |

The monohydrate (whewellite, the kidney-stone mineral) is the least soluble phase: **Ksp ≈ 10⁻⁸·⁷⁵** at 25 °C in dilute solution.

---

### 3. pH Threshold Estimation

**Step A — Fraction of oxalate as C₂O₄²⁻**

At pH = pKa₂ = 3.8, exactly 50% of total oxalate is C₂O₄²⁻. The fraction rises steeply above this:

| pH | α(C₂O₄²⁻) ≈ |
|----|-------------|
| 3.0 | ~6% |
| 3.8 | ~50% |
| 4.5 | ~83% |
| 5.5 | ~98% |
| ≥ 6 | ~100% |

**Step B — Ion product vs. Ksp**

For a typical physiological or environmental scenario with [Ca²⁺] ≈ 2–5 mM and total oxalate [Ox]_T ≈ 0.5–1 mM:

- At pH 4.5: [C₂O₄²⁻] ≈ 0.83 × 0.5 mM ≈ 4 × 10⁻⁴ M  
  IP = [Ca²⁺][C₂O₄²⁻] ≈ 3×10⁻³ × 4×10⁻⁴ = **1.2 × 10⁻⁶** → well above Ksp (10⁻⁸·⁷⁵ ≈ 1.8 × 10⁻⁹) ✓

- At pH 3.5: [C₂O₄²⁻] ≈ 0.33 × 0.5 mM ≈ 1.7 × 10⁻⁴ M  
  IP ≈ 3×10⁻³ × 1.7×10⁻⁴ = **5 × 10⁻⁷** → still >> Ksp ✓

- At pH 2.5: [C₂O₄²⁻] ≈ 0.6% → IP ≈ 10⁻¹⁰ → **below Ksp**, no precipitation

**Step C — Aqueous complex correction**

The Ca(C₂O₄)aq complex has log β₁ = 3.19, meaning it sequesters some Ca²⁺ and oxalate into a soluble form. This slightly raises the total oxalate needed to precipitate, but since β₁ ≪ 1/Ksp, the effect is modest and does not shift the pH threshold significantly.

---

### 4. Conclusion

> **Calcium oxalate precipitation becomes significant at approximately pH 4–5**, with the onset closely tied to pKa₂ of oxalic acid (3.8). Below pH ~3.5, the oxalate dianion concentration is too low to exceed the Ksp (10⁻⁸·⁷⁵ for the monohydrate). Above pH ~4.5, the ion product readily surpasses Ksp and precipitation is thermodynamically favored.

**Chemistry insight:** This is directly relevant to kidney stone formation (CaC₂O₄·H₂O, whewellite). Urine pH is typically 5–7, placing it squarely in the precipitation zone — which is why dietary oxalate and urinary calcium are both risk factors. The modest aqueous stability of Ca(oxalate)aq (log β₁ ≈ 3.2) means that complexation provides only limited protection against precipitation compared to, say, citrate chelation (log β ≈ 4–5), which is why citrate supplementation is a clinical strategy for stone prevention.

---
*All constants from NIST SRD-46 (Standard Reference Database 46).*

---