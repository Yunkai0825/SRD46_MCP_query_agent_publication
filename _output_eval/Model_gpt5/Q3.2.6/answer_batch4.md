Below I use matched (25 °C, I ≈ 0.1 M) SRD‑46 data for malonic acid pKa and Cu²⁺–malonate stability to compute the conditional 1:1 formation constant at pH 4.

Data used (SRD‑46)
| Quantity | Value | Conditions | SRD‑46 IDs |
|---|---:|---|---|
| pKa₁ (H₂L ⇌ HL⁻ + H⁺) | 2.65 | 25 °C, I = 0.10 M | vlm_151949 |
| pKa₂ (HL⁻ ⇌ L²⁻ + H⁺) | 5.27 | 25 °C, I = 0.10 M | vlm_151918 |
| log K (Cu²⁺ + L²⁻ ⇌ CuL) | 5.04 | 25 °C, I = 0.10 M | vlm_152316, beta_def_812 |
| log K (Cu²⁺ + HL⁻ ⇌ CuHL⁺) | 2.08 | 25 °C, I = 0.10 M | vlm_152328, beta_def_779 |

Speciation of malonic acid at pH 4 (from pKa₁, pKa₂)
| Species | Fraction αᵢ |
|---|---:|
| H₂L | 0.0407 |
| HL⁻ | 0.910 |
| L²⁻ | 0.0489 |

Calculation and result
- Convert pKa to Ka: Ka₁ = 10^−2.65 = 2.24×10^−3; Ka₂ = 10^−5.27 = 5.37×10^−6; [H⁺] = 10^−4 M.
- Fractions αᵢ are computed with D = 1 + Ka₁/[H⁺] + Ka₁Ka₂/[H⁺]², then
  α(H₂L) = 1/D, α(HL⁻) = (Ka₁/[H⁺])/D, α(L²⁻) = (Ka₁Ka₂/[H⁺]²)/D.
- Conditional formation constant referenced to total ligand, including both 1:1 products (CuL and CuHL⁺):
  K′(pH 4) = 10^(5.04)·α(L²⁻) + 10^(2.08)·α(HL⁻)
           ≈ (1.10×10^5)(0.0489) + (1.20×10^2)(0.910)
           ≈ 5.36×10^3 + 1.09×10^2 ≈ 5.47×10^3
  ⇒ log K′(pH 4) ≈ 3.74.

If you prefer the conditional constant for the unprotonated complex only (CuL, referenced to total ligand):
- K′_CuL(pH 4) = 10^(5.04)·α(L²⁻) ≈ 5.36×10^3 ⇒ log K′_CuL ≈ 3.73.

Notes
- At pH 4, HL⁻ dominates the free ligand pool (~91%), so CuHL⁺ contributes measurably despite its much smaller intrinsic log K; CuL remains the major contributor because its intrinsic stability is high.
- ML₂ is negligible under these conditions unless ligand ≫ metal.

Source: NIST Standard Reference Database 46 (SRD‑46): measurements and pKa values cited above.

---