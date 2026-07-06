# Calcium Oxalate Precipitation: At What pH Does It Become Significant?

All data from **NIST SRD-46**.

---

## Key Equilibrium Data

### 1. Oxalic Acid pKa Values (25 °C, I = 0.1 M)

| Step | Reaction | pKa |
|------|----------|-----|
| pKa₁ | H₂C₂O₄ ⇌ H⁺ + HC₂O₄⁻ | **−1.2** |
| pKa₂ | HC₂O₄⁻ ⇌ H⁺ + C₂O₄²⁻ | **3.8** |

Oxalate dianion (C₂O₄²⁻) becomes the dominant species only **above pH ≈ 3.8**.

---

### 2. Ca²⁺–Oxalate Aqueous Complex (beta_def_812)

| Reaction | log K | T (°C) | I (M) |
|----------|-------|--------|-------|
| Ca²⁺ + C₂O₄²⁻ ⇌ CaC₂O₄(aq) | **3.19** | 25 | 0 |
| Ca²⁺ + C₂O₄²⁻ ⇌ CaC₂O₄(aq) | **2.46** | 37 | 0.1 |

---

### 3. Solubility Products (Ksp) of Solid Phases

| Phase | Reaction | log Ksp | T (°C) | I (M) |
|-------|----------|---------|--------|-------|
| CaC₂O₄·H₂O (whewellite) | CaC₂O₄·H₂O(s) ⇌ Ca²⁺ + C₂O₄²⁻ + H₂O | **−7.86** | 25 | 0.1 |
| CaC₂O₄·H₂O (whewellite) | CaC₂O₄·H₂O(s) ⇌ Ca²⁺ + C₂O₄²⁻ + H₂O | **−8.75** | 25 | 0 |
| CaC₂O₄·3H₂O (caoxite) | CaC₂O₄·3H₂O(s) ⇌ Ca²⁺ + C₂O₄²⁻ + 3H₂O | **−8.32** | 25 | 0 |

The **monohydrate (whewellite)** is the thermodynamically relevant phase at 25 °C (higher Ksp = more soluble, but it is the kinetically and physiologically dominant form — kidney stones).

---

## Precipitation Onset Analysis

The critical insight is that **precipitation requires free C₂O₄²⁻**, whose availability is pH-controlled:

$$\alpha_2(\text{C}_2\text{O}_4^{2-}) = \frac{1}{1 + 10^{pK_{a2}-\text{pH}} + 10^{pK_{a1}+pK_{a2}-2\cdot\text{pH}}}$$

| pH | α₂ (fraction as C₂O₄²⁻) | Comment |
|----|--------------------------|---------|
| 2.0 | ~0.001 | Negligible dianion |
| 3.0 | ~0.06 | Small fraction |
| 3.8 | ~0.33 | Half-equivalence point (pKa₂) |
| 5.0 | ~0.94 | Mostly dianion |
| 6.0 | ~0.99 | Essentially complete |

For a typical physiological or lab scenario with [Ca²⁺] ≈ 2.5 mM and total oxalate ≈ 0.1–1 mM, using **log Ksp ≈ −7.9** (25 °C, I = 0.1 M):

$$[\text{Ca}^{2+}][\text{C}_2\text{O}_4^{2-}] \geq K_{sp} \approx 10^{-7.9}$$

At [Ca²⁺] = 2.5 × 10⁻³ M, precipitation requires [C₂O₄²⁻] ≥ 10⁻⁷·⁹ / 2.5×10⁻³ ≈ **3 × 10⁻⁶ M**. Even at pH 4–5, a modest total oxalate concentration can supply this. The aqueous complex (log K = 3.19) sequesters some Ca²⁺ but does not dramatically shift the threshold.

---

## Conclusion

> **Calcium oxalate precipitation becomes significant at approximately pH 4–5**, with the onset tied directly to pKa₂ = 3.8 of oxalic acid.

- **Below pH ~3.5:** Oxalate exists mainly as HC₂O₄⁻ (monoanion); [C₂O₄²⁻] is too low to exceed Ksp under most conditions — no precipitation.
- **pH 4–5:** The dianion fraction rises steeply (10–90%), and [Ca²⁺][C₂O₄²⁻] can readily exceed Ksp ≈ 10⁻⁷·⁹ — **precipitation begins**.
- **Above pH 5–6:** Oxalate is fully deprotonated; precipitation is essentially complete for any physiologically relevant Ca²⁺ and oxalate concentrations.

This is precisely why **kidney stones (calcium oxalate)** form in slightly acidic to neutral urine (pH 5–7): the combination of near-complete oxalate deprotonation and elevated urinary Ca²⁺ drives the system well past Ksp. The aqueous CaC₂O₄ complex (log K ≈ 3.2) provides a modest buffering effect, slightly raising the total oxalate needed to initiate precipitation.

*Source: NIST SRD-46 (metal_25 × ligand_8872; vlm_151494, vlm_151532, vlm_151599, vlm_151601, vlm_151608, vlm_151610)*

---