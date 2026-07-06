## Conditional Stability Constant for Cu²⁺–Malonate at pH 4

### Data from NIST SRD-46

| Parameter | Value | Conditions |
|-----------|-------|------------|
| pKa₁ (H₂L → HL⁻ + H⁺) | **2.65** | 25 °C, I = 0.1 M |
| pKa₂ (HL⁻ → L²⁻ + H⁺) | **5.27** | 25 °C, I = 0.1 M |
| log K (Cu²⁺ + L²⁻ ⇌ CuL) | **5.04** | 25 °C, I = 0.1 M |

I chose the log K = 5.04 entry (vlm_152316) because its conditions (25 °C, I = 0.1 M) exactly match the pKa data.

---

### Calculation

The **conditional (effective) stability constant** K′ accounts for the fact that at pH 4, not all free ligand is in the fully deprotonated form L²⁻. We define:

$$\log K' = \log K - \log \alpha_{L}$$

where **α_L** is the side-reaction coefficient for protonation of the ligand:

$$\alpha_L = 1 + \frac{[\text{H}^+]}{K_{a2}} + \frac{[\text{H}^+]^2}{K_{a1} \cdot K_{a2}}$$

**Step 1 — Convert to Ka values:**

| Quantity | Expression | Value |
|----------|-----------|-------|
| Ka₁ | 10⁻²·⁶⁵ | 2.239 × 10⁻³ |
| Ka₂ | 10⁻⁵·²⁷ | 5.370 × 10⁻⁶ |
| [H⁺] at pH 4 | 10⁻⁴ | 1.000 × 10⁻⁴ |

**Step 2 — Compute each term of α_L:**

| Term | Calculation | Value |
|------|-------------|-------|
| 1 | — | 1.00 |
| [H⁺]/Ka₂ | 10⁻⁴ / 10⁻⁵·²⁷ = 10¹·²⁷ | **18.62** |
| [H⁺]²/(Ka₁·Ka₂) | 10⁻⁸ / 10⁻⁷·⁹² = 10⁻⁰·⁰⁸ | **0.83** |

$$\alpha_L = 1 + 18.62 + 0.83 = \mathbf{20.45}$$

$$\log \alpha_L = \log(20.45) = \mathbf{1.31}$$

**Step 3 — Conditional constant:**

$$\log K' = 5.04 - 1.31 = \boxed{3.73}$$

$$K' \approx 5.4 \times 10^3$$

---

### Interpretation

At pH 4, the effective binding of Cu²⁺ to malonate drops by about **1.3 log units** compared to the thermodynamic constant. This makes chemical sense: pH 4 sits between pKa₁ (2.65) and pKa₂ (5.27), so the dominant ligand species is **HL⁻** (the mono-protonated form), not the fully deprotonated L²⁻ that binds Cu²⁺ most strongly. Only about 5% of the free ligand exists as L²⁻ at this pH. Despite this, log K′ ≈ 3.7 still indicates appreciable complex formation — malonate remains a reasonably effective chelator of Cu²⁺ even under mildly acidic conditions, owing to its relatively high intrinsic affinity (log K = 5.04) and the stabilisation provided by the five-membered chelate ring.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes).*

---