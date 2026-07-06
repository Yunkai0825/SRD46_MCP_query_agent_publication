## Conditional Stability Constant for Cu²⁺–Malonate at pH 4

### Data from SRD-46 (matched conditions: 25 °C, I = 0.1 M)

| Parameter | Value | Source (vlm_id) |
|-----------|-------|-----------------|
| pKa₁ (H₂L ⇌ H⁺ + HL⁻) | 2.65 | vlm_151949 |
| pKa₂ (HL⁻ ⇌ H⁺ + L²⁻) | 5.27 | vlm_151918 |
| log K₁ (Cu²⁺ + L²⁻ ⇌ CuL) | 5.04 | vlm_152316 |

---

### Step-by-step Calculation

**Goal:** Find the conditional (effective) stability constant log K′ at pH 4, defined as:

$$K' = \frac{[\text{CuL}]}{[\text{Cu}^{2+}][\text{L}']}$$

where [L′] = total free ligand in all protonation states = [L²⁻] + [HL⁻] + [H₂L].

**Step 1 — Compute the ligand side-reaction coefficient α_L**

The side-reaction coefficient accounts for protonation competing with metal binding:

$$\alpha_L = 1 + \frac{[\text{H}^+]}{K_{a2}} + \frac{[\text{H}^+]^2}{K_{a1} \cdot K_{a2}}$$

At pH 4: [H⁺] = 10⁻⁴ M

| Term | Expression | Value |
|------|-----------|-------|
| Term 1 | 1 | 1 |
| Term 2 | 10⁻⁴ / 10⁻⁵·²⁷ | 10¹·²⁷ = 18.62 |
| Term 3 | 10⁻⁸ / (10⁻²·⁶⁵ × 10⁻⁵·²⁷) = 10⁻⁸ / 10⁻⁷·⁹² | 10⁻⁰·⁰⁸ = 0.832 |

$$\alpha_L = 1 + 18.62 + 0.832 = 20.45$$

$$\log \alpha_L = \log(20.45) = 1.31$$

**Step 2 — Compute the conditional constant**

$$\log K' = \log K_1 - \log \alpha_L = 5.04 - 1.31 = \boxed{3.73}$$

---

### Interpretation

| Quantity | Value |
|----------|-------|
| log K₁ (intrinsic, for L²⁻) | 5.04 |
| log α_L at pH 4 | 1.31 |
| **log K′ at pH 4** | **3.73** |

At pH 4, malonic acid is predominantly in the HL⁻ form (the mono-protonated species dominates between pH 2.65 and 5.27). Only about 1/20 of the total free ligand exists as the fully deprotonated L²⁻ that binds Cu²⁺ most effectively. This reduces the effective formation constant by ~1.3 log units — from log K = 5.04 down to log K′ ≈ 3.73.

Despite this reduction, K′ ≈ 5,400 still indicates **significant complex formation** at pH 4, which is why malonate is a useful buffer/complexing agent in mildly acidic copper solutions (e.g., in electroplating baths and analytical chemistry).

> **Note:** This calculation neglects the protonated complex CuHL⁺ (beta_def_779 in SRD-46) and any Cu²⁺ hydrolysis side reactions, both of which are minor at pH 4. Including CuHL⁺ would slightly increase the effective complexation.

*Source: NIST Standard Reference Database 46 (SRD-46)*

---