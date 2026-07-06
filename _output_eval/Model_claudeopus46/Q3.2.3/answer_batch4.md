## Calcium Oxalate Precipitation vs. pH — An SRD-46 Analysis

### Key Thermodynamic Data (25 °C, I = 0.1 M)

| Parameter | Value | Source (SRD-46) |
|-----------|-------|-----------------|
| pK_a1 (H₂C₂O₄ ⇌ HC₂O₄⁻ + H⁺) | **1.2** | vlm_151532 |
| pK_a2 (HC₂O₄⁻ ⇌ C₂O₄²⁻ + H⁺) | **3.8** | vlm_151494 |
| log K_sp (CaC₂O₄·H₂O) | **−7.86** | vlm_151601 (I = 0.1 M, 25 °C) |
| log K_sp (CaC₂O₄·H₂O, I → 0) | **−8.75** | vlm_151608 (25 °C) |
| log β₁ (Ca²⁺ + C₂O₄²⁻ ⇌ CaC₂O₄(aq)) | **3.19** | vlm_151599 (25 °C, I → 0) |

### Reasoning

The dissolution equilibrium for calcium oxalate monohydrate is:

$$\text{CaC}_2\text{O}_4 \cdot \text{H}_2\text{O}_{(s)} \rightleftharpoons \text{Ca}^{2+} + \text{C}_2\text{O}_4^{2-} + \text{H}_2\text{O}$$

$$K_{sp} = [\text{Ca}^{2+}][\text{C}_2\text{O}_4^{2-}] \approx 10^{-7.86} \approx 1.4 \times 10^{-8} \;\;(I = 0.1\text{ M})$$

The fraction of total oxalate present as the fully deprotonated dianion C₂O₄²⁻ depends on pH:

$$\alpha_{L^{2-}} = \frac{1}{1 + 10^{(3.8-\text{pH})} + 10^{(3.8+1.2-2\text{pH})}}$$

| pH | α(C₂O₄²⁻) |
|----|------------|
| 2.0 | 0.006 |
| 3.0 | 0.06 |
| 3.8 | 0.33 |
| 4.5 | 0.83 |
| 5.0 | 0.94 |
| 7.0 | ~1.00 |

**Precipitation condition:** The ion product Q = [Ca²⁺] × [C₂O₄²⁻] must exceed K_sp. Since [C₂O₄²⁻] = α × C_total(oxalate), lowering pH reduces the effective oxalate dianion concentration and suppresses precipitation.

For a representative scenario (1 mM Ca²⁺, 1 mM total oxalate):

$$Q = (10^{-3}) \times (\alpha \times 10^{-3}) = \alpha \times 10^{-6}$$

Precipitation occurs when Q > K_sp:

$$\alpha \times 10^{-6} > 10^{-7.86} \implies \alpha > 10^{-1.86} \approx 0.014$$

Solving for pH: α ≈ 0.014 corresponds to **pH ≈ 2.0**. So even at millimolar concentrations, precipitation can begin at surprisingly low pH.

At more dilute, physiologically relevant concentrations (~0.01 mM each), the threshold shifts upward to roughly **pH 3–4**.

### Summary

> **Calcium oxalate precipitation becomes significant at approximately pH 2–4**, depending on total calcium and oxalate concentrations. Above pH ~4.5, essentially all oxalate is in the dianion form and precipitation is strongly favored at virtually any concentration above micromolar levels. Below pH ~2, the protonation of oxalic acid (pK_a1 = 1.2) suppresses the dianion enough to keep the ion product below K_sp.

### Chemistry Insight

This pH dependence is clinically relevant: calcium oxalate kidney stones form most readily in neutral-to-slightly-acidic urine (pH 5–7), where oxalate is fully deprotonated. The aqueous complex CaC₂O₄(aq) (log β = 3.19) actually sequesters some free ions, raising the effective solubility by roughly an order of magnitude — but this is insufficient to prevent precipitation at the supersaturation levels found in biological fluids. Acidifying urine below pH ~4 would thermodynamically disfavor stone formation, though this is not physiologically achievable.

*Data source: NIST Standard Reference Database 46 (SRD-46)*

---