## Final Answer

All the data I need is now in hand. Here is the complete analysis.

---

## Ca²⁺–Oxalate Precipitation: pH Threshold Analysis

### Key Constants from SRD-46

#### Oxalic Acid pKa Values (25 °C, I = 0.1 M)

| Step | Equilibrium | pKa | Species above pKa |
|------|-------------|-----|-------------------|
| pKa₁ | H₂C₂O₄ ⇌ HC₂O₄⁻ + H⁺ | −1.2 | HC₂O₄⁻ (monoanion) |
| pKa₂ | HC₂O₄⁻ ⇌ C₂O₄²⁻ + H⁺ | **3.8** | C₂O₄²⁻ (dianion) |

#### Ca²⁺–Oxalate Stability Constants (25 °C)

| Species | Reaction | log K | Conditions |
|---------|----------|-------|------------|
| CaC₂O₄(aq) complex | Ca²⁺ + C₂O₄²⁻ ⇌ CaC₂O₄(aq) | **+3.19** | 25 °C, I → 0 |
| CaC₂O₄·H₂O(s) — Ksp | CaC₂O₄·H₂O ⇌ Ca²⁺ + C₂O₄²⁻ | **−8.75** | 25 °C, I → 0 |
| CaC₂O₄·3H₂O(s) — Ksp | CaC₂O₄·3H₂O ⇌ Ca²⁺ + C₂O₄²⁻ | **−8.32** | 25 °C, I → 0 |

---

### The pH Calculation

**Step 1 — Fraction of free oxalate dianion (α₂) as a function of pH**

Using the two pKa values (pKa₁ = −1.2, pKa₂ = 3.8):

$$\alpha_2(\text{pH}) = \frac{1}{1 + 10^{(pK_{a2}-\text{pH})} + 10^{(pK_{a1}+pK_{a2}-2\cdot\text{pH})}}$$

| pH | α₂ (fraction as C₂O₄²⁻) |
|----|--------------------------|
| 2.0 | ~0.0006 (0.06%) |
| 3.0 | ~0.06 (6%) |
| 3.8 | ~0.50 (50%) |
| 5.0 | ~0.99 (99%) |
| 6.0 | ~1.00 (≈100%) |

**Step 2 — Effective ion product vs. Ksp**

For the monohydrate (the clinically relevant whewellite form):

$$K_{sp} = [\text{Ca}^{2+}][\text{C}_2\text{O}_4^{2-}] = 10^{-8.75}$$

The effective solubility product in terms of *total* oxalate concentration is:

$$[\text{Ca}^{2+}] \cdot \alpha_2 \cdot C_{\text{ox,total}} \geq K_{sp}$$

For typical physiological/laboratory concentrations (e.g., [Ca²⁺] ≈ 2.5 mM, [oxalate]_total ≈ 0.5 mM):

$$\text{IP} = (2.5\times10^{-3}) \times \alpha_2 \times (5\times10^{-4})$$

Setting IP = Ksp = 10⁻⁸·⁷⁵ ≈ 1.78 × 10⁻⁹:

$$\alpha_2 \geq \frac{1.78\times10^{-9}}{1.25\times10^{-6}} \approx 0.0014$$

This α₂ ≈ 0.14% is reached at **pH ≈ 2.6** — but this is the *thermodynamic* onset. In practice, the aqueous CaC₂O₄ complex (log K = +3.19) sequesters a significant fraction of both ions, delaying visible precipitation.

---

### Bottom Line

> **Calcium oxalate precipitation becomes significant above approximately pH 4–5.**

| pH Range | What Happens |
|----------|-------------|
| < 3 | Oxalate exists mainly as H₂C₂O₄ / HC₂O₄⁻; [C₂O₄²⁻] too low to exceed Ksp |
| 3–4 | Thermodynamic threshold crossed for high concentrations; aqueous CaC₂O₄ complex buffers precipitation |
| **4–5** | **α₂ rises sharply past 50%; precipitation becomes robust and observable** |
| > 6 | Essentially all oxalate is C₂O₄²⁻; precipitation is rapid and nearly complete |

The critical driver is **pKa₂ = 3.8**: below this pH, the dianion fraction is suppressed and the ion product stays below Ksp (10⁻⁸·⁷⁵). Above pH ~4–5, α₂ → 1 and the full oxalate concentration is available to precipitate calcium.

**Clinical relevance:** Kidney stones (calcium oxalate) form in urine at pH 5–7, exactly where this analysis predicts robust precipitation. Acidic urine (pH < 5.5) slightly inhibits oxalate stone formation by protonating oxalate — a fact exploited in dietary management of hyperoxaluria.

*Source: NIST SRD-46 (ligand_8872, metal_25; vlm_151494, vlm_151532, vlm_151608, vlm_151599)*

---