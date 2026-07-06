## Final Answer

All the data needed is now in hand. Here is the complete analysis.

---

## Cu²⁺–Glycine: Stepwise → Overall β₂ Comparison

### Equilibrium Definitions (from SRD-46)

| Symbol | Beta Definition | Equation |
|--------|----------------|----------|
| β₁ (= K₁) | `beta_def_812` | Cu²⁺ + Gly⁻ ⇌ [CuGly]⁺ |
| β₂ | `beta_def_840` | Cu²⁺ + 2 Gly⁻ ⇌ [CuGly₂] |

The **stepwise K₂** is not stored separately as its own beta definition; it is implicit as the ratio β₂/β₁. In log terms:

> **log K₂ = log β₂ − log β₁**

---

### Data at 25 °C, Two Ionic Strengths

#### At I = 0 M (infinite dilution), 25 °C

| Constant | log value | Source |
|----------|-----------|--------|
| log K₁ (= log β₁) | **8.56** | vlm_93854, `beta_def_812` |
| log β₂ (reported) | **15.70** | vlm_93869, `beta_def_840` |
| **log K₂** (derived) | **15.70 − 8.56 = 7.14** | — |
| **log β₂ (estimated)** = log K₁ + log K₂ | **8.56 + 7.14 = 15.70** | — |
| Δ (estimated − reported) | **0.00** | ✅ exact |

#### At I = 0.1 M, 25 °C

| Constant | log value | Source |
|----------|-----------|--------|
| log K₁ (= log β₁) | **8.19** | vlm_93847, `beta_def_812` |
| log β₂ (reported) | **15.10** | vlm_93862, `beta_def_840` |
| **log K₂** (derived) | **15.10 − 8.19 = 6.91** | — |
| **log β₂ (estimated)** = log K₁ + log K₂ | **8.19 + 6.91 = 15.10** | — |
| Δ (estimated − reported) | **0.00** | ✅ exact |

---

### The Mathematics

The relationship between stepwise and overall constants is exact by definition:

$$\beta_2 = K_1 \times K_2 \quad \Longleftrightarrow \quad \log\beta_2 = \log K_1 + \log K_2$$

Because β₁ and β₂ are both defined relative to the **free metal and free ligand**, the stepwise K₂ is simply the ratio β₂/β₁. There is no approximation involved — the agreement is mathematically exact, not a coincidence of measurement.

---

### Chemistry Insight

- **log β₂ ≈ 15.7** at 25 °C, I → 0 places Cu²⁺–bis(glycinate) among the most stable 1:2 amino acid complexes of divalent transition metals, reflecting the strong chelate effect of glycine's –NH₂/–COO⁻ bidentate coordination.
- The **stepwise ratio K₁/K₂ ≈ 10^(8.56−7.14) = 10^1.42 ≈ 26** at I = 0. This factor of ~26 is larger than the statistical factor of 4 expected for two identical binding sites, indicating a modest **negative cooperativity**: binding the first glycine slightly reduces the affinity for the second, likely due to steric and electrostatic effects in the square-planar [Cu(gly)₂] complex.
- Increasing ionic strength from 0 → 0.1 M lowers both log K₁ (8.56 → 8.19) and log β₂ (15.70 → 15.10), consistent with Debye–Hückel screening of the highly charged Cu²⁺ centre.

*Source: NIST SRD-46, metal_41 (Cu²⁺) + ligand_5760 (Glycine), beta_def_812 & beta_def_840.*

---