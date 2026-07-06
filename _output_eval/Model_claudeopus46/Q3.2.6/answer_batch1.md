Now I have all the data I need. Let me present the full calculation.

---

## Conditional Stability Constant for Cu²⁺–Malonate at pH 4

### Data from NIST SRD-46

All values at **25 °C, I = 0.1 M**:

| Parameter | Value | Source |
|-----------|-------|--------|
| pKₐ₁ (H₂L ⇌ HL⁻ + H⁺) | 2.65 | vlm_151949 |
| pKₐ₂ (HL⁻ ⇌ L²⁻ + H⁺) | 5.27 | vlm_151918 |
| log K₁ (Cu²⁺ + L²⁻ ⇌ CuL) | 5.04 | vlm_152316 |

Here **L²⁻** is the fully deprotonated malonate dianion, and **H₂L** is malonic acid.

---

### Step 1 — Compute the side-reaction coefficient αL at pH 4

The fraction of total free ligand present as L²⁻ is:

$$\alpha_{L^{2-}} = \frac{[L^{2-}]}{C_L} = \frac{1}{1 + 10^{(\text{p}K_{a2} - \text{pH})} + 10^{(\text{p}K_{a1} + \text{p}K_{a2} - 2\text{pH})}}$$

Plugging in pH = 4, pKₐ₁ = 2.65, pKₐ₂ = 5.27:

| Term | Exponent | Value |
|------|----------|-------|
| 10^(pKₐ₂ − pH) | 5.27 − 4 = 1.27 | 18.62 |
| 10^(pKₐ₁ + pKₐ₂ − 2·pH) | 2.65 + 5.27 − 8 = −0.08 | 0.832 |
| Denominator | 1 + 18.62 + 0.832 | **20.45** |

$$\alpha_{L^{2-}} = \frac{1}{20.45} = 0.0489$$

$$\log \alpha_{L^{2-}} = \log(0.0489) = -1.31$$

### Step 2 — Compute the conditional constant K′

The conditional (or effective) stability constant referenced to **total free ligand** at pH 4 is:

$$K' = K_1 \times \alpha_{L^{2-}}$$

$$\log K' = \log K_1 + \log \alpha_{L^{2-}} = 5.04 + (-1.31) = \boxed{3.73}$$

$$K' = 10^{3.73} \approx 5{,}370$$

---

### Summary

| Quantity | Value |
|----------|-------|
| log K₁ (thermodynamic) | 5.04 |
| α(L²⁻) at pH 4 | 0.049 |
| log α(L²⁻) | −1.31 |
| **log K′ (conditional, pH 4)** | **3.73** |
| **K′** | **≈ 5,400** |

### Physical Interpretation

At pH 4, malonic acid sits between its two pKₐ values (2.65 and 5.27), so the **mono-protonated form HL⁻ dominates** (~91% of free ligand). Only about 5% exists as the fully deprotonated L²⁻ that binds Cu²⁺ most effectively. This proton competition reduces the effective binding strength by about 1.3 log units — from log K = 5.04 down to log K′ ≈ 3.73. The complex is still reasonably stable (K′ ≈ 5,400), meaning Cu²⁺–malonate complexation remains significant at pH 4, which is relevant in environmental and analytical chemistry contexts.

> **Note:** This simplified calculation neglects the protonated complex CuHL⁺ (beta_def_779 in SRD-46), which would slightly *increase* the effective binding at pH 4 since HL⁻ is the dominant ligand form. Including it would give a modestly higher conditional constant.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes)*

---