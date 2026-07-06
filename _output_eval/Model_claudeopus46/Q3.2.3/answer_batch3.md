I have all the data needed. Let me now work through the chemistry and provide the answer.

---

## Calcium Oxalate Precipitation vs. pH — An SRD-46 Analysis

### Key Thermodynamic Data (from NIST SRD-46)

**Oxalic acid pKa values** (25 °C, I = 0.1 M):

| Equilibrium | pKₐ |
|---|---|
| H₂C₂O₄ ⇌ HC₂O₄⁻ + H⁺ | **1.2** |
| HC₂O₄⁻ ⇌ C₂O₄²⁻ + H⁺ | **3.8** |

**Ca²⁺–Oxalate stability & solubility** (25 °C):

| Equilibrium | log K | Conditions |
|---|---|---|
| Ca²⁺ + C₂O₄²⁻ ⇌ CaC₂O₄(aq) | **3.19** | 25 °C, I = 0 |
| CaC₂O₄·H₂O(s) ⇌ Ca²⁺ + C₂O₄²⁻ + H₂O | **−8.75** | 25 °C, I = 0 |
| CaC₂O₄·H₂O(s) ⇌ Ca²⁺ + C₂O₄²⁻ + H₂O | **−7.86** | 25 °C, I = 0.1 |

### Reasoning

The effective solubility product for calcium oxalate monohydrate (the thermodynamically stable phase) is:

$$K_{sp} = [\text{Ca}^{2+}][\text{C}_2\text{O}_4^{2-}] \approx 10^{-8.75} \;\text{(I = 0)}$$

At any pH, the total dissolved oxalate distributes among H₂C₂O₄, HC₂O₄⁻, and C₂O₄²⁻. The fraction present as the fully deprotonated oxalate dianion (α₂) is:

$$\alpha_2 = \frac{1}{1 + \frac{[\text{H}^+]}{K_{a2}} + \frac{[\text{H}^+]^2}{K_{a1}K_{a2}}}$$

With pKₐ₁ = 1.2 and pKₐ₂ = 3.8:

| pH | α₂ (fraction as C₂O₄²⁻) |
|---|---|
| 2.0 | ~0.0016 |
| 3.0 | ~0.014 |
| 3.8 | ~0.10 |
| 5.0 | ~0.94 |
| 7.0 | ~1.0 |

**Precipitation condition:** CaC₂O₄ precipitates when [Ca²⁺] × [C₂O₄²⁻] > Ksp. Since [C₂O₄²⁻] = α₂ × C_total(oxalate), lowering pH dramatically reduces [C₂O₄²⁻] and suppresses precipitation.

For a typical physiological or analytical scenario (e.g., [Ca²⁺] ≈ 2.5 mM, total oxalate ≈ 0.5 mM):

- The ion product Q = [Ca²⁺] × α₂ × C_ox
- At **pH ≈ 4–5**, α₂ becomes large enough (0.1–0.9) that Q exceeds Ksp ≈ 10⁻⁸·⁷⁵, and precipitation begins.
- Below **pH ≈ 3**, α₂ is so small that even moderately concentrated solutions remain undersaturated.
- Above **pH ≈ 5**, essentially all oxalate is C₂O₄²⁻ and precipitation is strongly favored.

### Answer

**Calcium oxalate precipitation becomes significant at approximately pH 4–5**, roughly one pH unit above pKₐ₂ (3.8) of oxalic acid. This is the region where the oxalate dianion concentration rises sharply enough for the ion product to exceed the very low Ksp (~10⁻⁸·⁸).

### Chemical Insight

This pH dependence is clinically relevant: calcium oxalate kidney stones form preferentially in urine at pH 5–6, where oxalate is fully deprotonated. Acidifying urine below pH 4 would dissolve the precipitate, but this is physiologically impractical. The relatively large aqueous complex formation constant (log K ≈ 3.2) means that some dissolved CaC₂O₄(aq) persists even above the Ksp threshold, slightly increasing total calcium oxalate solubility — but the Ksp is so low that this effect is modest.

*Source: NIST Standard Reference Database 46 (SRD-46)*

---