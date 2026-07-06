## Calcium Oxalate Precipitation: pH Threshold Estimate

### Data from NIST SRD-46

**Oxalic acid pKa values** (25 °C, I = 0.1 M):

| Equilibrium | pKₐ |
|---|---|
| H₂C₂O₄ ⇌ HC₂O₄⁻ + H⁺ | **1.2** |
| HC₂O₄⁻ ⇌ C₂O₄²⁻ + H⁺ | **3.8** |

**Ca²⁺–oxalate constants** (25 °C, I ≈ 0):

| Equilibrium | log K |
|---|---|
| Ca²⁺ + C₂O₄²⁻ ⇌ CaC₂O₄(aq) | **+3.19** |
| CaC₂O₄·H₂O(s) ⇌ Ca²⁺ + C₂O₄²⁻ + H₂O | **−8.75** (Ksp) |

---

### Reasoning

The solubility product for calcium oxalate monohydrate is:

$$K_{sp} = [\text{Ca}^{2+}][\text{C}_2\text{O}_4^{2-}] = 10^{-8.75} \approx 1.8 \times 10^{-9}$$

Precipitation occurs when the ion product exceeds Ksp. The key variable is [C₂O₄²⁻], which depends on pH through the two protonation equilibria. For a total oxalate concentration $C_T$, the fraction present as the fully deprotonated dianion (α₂) is:

$$\alpha_2 = \frac{1}{1 + 10^{(pK_{a2}-pH)} + 10^{(pK_{a1}+pK_{a2}-2\cdot pH)}}$$

At **pH 4** (just above pKₐ₂ = 3.8): α₂ ≈ 0.61, so most oxalate is already deprotonated.

For a typical scenario with [Ca²⁺] ≈ 1–5 mM and total oxalate ≈ 0.5–1 mM:

- At **pH 3**: α₂ ≈ 0.14 → [C₂O₄²⁻] ≈ 1.4 × 10⁻⁴ M → ion product ≈ 10⁻³ × 1.4 × 10⁻⁴ ≈ 1.4 × 10⁻⁷ ≫ Ksp → **already supersaturated**
- At **pH 2**: α₂ ≈ 0.015 → [C₂O₄²⁻] ≈ 1.5 × 10⁻⁵ M → ion product ≈ 1.5 × 10⁻⁸ → **borderline, approaching Ksp**

Because Ksp is so small (10⁻⁸·⁷⁵), even a modest fraction of deprotonated oxalate can exceed the solubility limit. The critical transition occurs around **pH ≈ 2–3**, where α₂ rises steeply as pH passes through pKₐ₂ = 3.8 from below.

### Answer

> **Calcium oxalate precipitation becomes significant at approximately pH 2–3**, well below the second pKₐ of oxalic acid (3.8). By pH 4, essentially all the oxalate is deprotonated and precipitation is strongly favored at millimolar concentrations.

### Chemistry Insight

This is clinically relevant: calcium oxalate is the most common component of kidney stones. Urine pH typically ranges from 5–7, well above the precipitation threshold, which is why even modest urinary oxalate concentrations (hyperoxaluria) can trigger stone formation. The very low Ksp (10⁻⁸·⁷⁵) means that calcium oxalate is one of the least soluble calcium salts, and acidifying urine below pH ~3 would be required to fully dissolve it — far below physiological range.

*Source: NIST Standard Reference Database 46 (SRD-46)*

---