## Conditional Stability Constant for Cu²⁺–Malonate at pH 4

### Data from SRD-46 (25 °C, I = 0.1 M)

| Parameter | Value | Source |
|-----------|-------|--------|
| pK_a1 (H₂L → HL⁻ + H⁺) | 2.65 | vlm_151949 |
| pK_a2 (HL⁻ → L²⁻ + H⁺) | 5.27 | vlm_151918 |
| log K₁ (Cu²⁺ + L²⁻ ⇌ CuL) | 5.04 | vlm_152316 |

All three values are at **25 °C, I = 0.1 M**, ensuring a self-consistent calculation.

---

### Step-by-Step Calculation

The **conditional (effective) stability constant** K′ accounts for the fact that at pH 4, not all of the "free" ligand is in the fully deprotonated form L²⁻ that binds Cu²⁺. We define:

$$K' = K_1 \cdot \alpha_{L^{2-}}$$

where α_{L²⁻} is the fraction of total free ligand present as L²⁻.

**1. Compute the side-reaction coefficient α_L(H)**

$$\alpha_L(H) = 1 + \frac{[\text{H}^+]}{K_{a2}} + \frac{[\text{H}^+]^2}{K_{a1} \cdot K_{a2}}$$

At pH 4: [H⁺] = 10⁻⁴ M; K_a1 = 10⁻²·⁶⁵; K_a2 = 10⁻⁵·²⁷

| Term | Expression | Value |
|------|-----------|-------|
| 1 | — | 1.00 |
| [H⁺]/K_a2 | 10⁻⁴ / 10⁻⁵·²⁷ = 10¹·²⁷ | 18.62 |
| [H⁺]²/(K_a1·K_a2) | 10⁻⁸ / 10⁻⁷·⁹² = 10⁻⁰·⁰⁸ | 0.83 |
| **α_L(H)** | **Sum** | **20.45** |

**2. Fraction of ligand as L²⁻**

$$\alpha_{L^{2-}} = \frac{1}{\alpha_L(H)} = \frac{1}{20.45} = 0.0489$$

$$\log \alpha_{L^{2-}} = -1.31$$

**3. Conditional stability constant**

$$\log K' = \log K_1 + \log \alpha_{L^{2-}} = 5.04 + (-1.31) = \boxed{3.73}$$

---

### Interpretation

| Quantity | log value |
|----------|-----------|
| Thermodynamic log K₁ (for L²⁻) | 5.04 |
| log α_{L²⁻} at pH 4 | −1.31 |
| **Conditional log K′ at pH 4** | **3.73** |

At pH 4, the conditional constant drops by about 1.3 log units relative to the thermodynamic value. This makes physical sense: pH 4 sits between pK_a1 (2.65) and pK_a2 (5.27), so the dominant free-ligand species is the monoprotonated HL⁻, not the fully deprotonated L²⁻ that coordinates Cu²⁺. Only ~5% of the total free ligand is present as L²⁻, weakening the effective binding. Despite this, log K′ ≈ 3.7 still indicates significant complex formation — Cu²⁺–malonate complexes remain important even at mildly acidic pH, which is relevant in environmental and biological contexts where malonate acts as a metal buffer.

*Source: NIST Standard Reference Database 46 (SRD-46).*

---