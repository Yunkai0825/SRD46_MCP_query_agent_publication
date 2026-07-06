Below is a quick, pH‑4 estimate using the malonic‑acid pKa’s and the Cu2+–malonate (ML) log K from SRD‑46.

Key data (SRD‑46)
| Quantity | Value | Notes |
|---|---|---|
| pKa1 (H2L ⇌ HL− + H+) | 2.65 | ligand_8873 (malonic acid) |
| pKa2 (HL− ⇌ L2− + H+) | 5.27 | ligand_8873 (malonic acid) |
| log β1 ≡ log10([ML]/[M][L2−]) | 5.80 | 25 °C, I ≈ 0 (vlm_152319; beta_def_812) |
| log K (MHL) ≡ log10([MHL]/[M][HL−]) | 2.08 | 25 °C, I = 0.1 M (vlm_152328; beta_def_779) |

Ligand protonation fractions at pH 4
- Ka1 = 10^−2.65 = 2.24×10^−3; Ka2 = 10^−5.27 = 5.37×10^−6; [H+] = 10^−4 M
- Denominator D = [H+]^2 + Ka1[H+] + Ka1Ka2 = 1.00×10^−8 + 2.24×10^−7 + 1.20×10^−8 = 2.46×10^−7
- α_L2− = (Ka1Ka2)/D = 1.20×10^−8 / 2.46×10^−7 ≈ 0.049 (log10 α_L2− ≈ −1.31)
- (for context at pH 4: α_HL− ≈ 0.91; α_H2L ≈ 0.041)

Conditional stability constant at pH 4 (referenced to total ligand, L_T)
- Using only CuL (as requested by “Cu²⁺–malonate log K”):
  - K′_ML = β1·α_L2− ⇒ log K′_ML = log β1 + log α_L2− = 5.80 − 1.31 ≈ 4.49
  - K′_ML ≈ 3.1×10^4

Optional check including CuHL (same pH, matched to I = 0.1 M set)
| Set | log β1(ML) | log K(MHL) | α_L2− | α_HL− | K′ = β1·α_L2− + K_MHL·α_HL− | log K′ |
|---|---:|---:|---:|---:|---:|---:|
| 25 °C, I = 0.1 M | 5.04 | 2.08 | 0.049 | 0.910 | (10^5.04·0.049) + (10^2.08·0.910) ≈ 5.5×10^3 | 3.74 |

Interpretation
- At pH 4, HL− dominates the ligand population, but the much larger β1 for ML means the ML term still controls the conditional constant; adding MHL changes K′ only slightly in this system.
- Because the pKa conditions in the ligand record are not explicitly specified, the I ≈ 0 estimate (log K′ ≈ 4.49) is a reasonable “infinite-dilution” benchmark; at I = 0.1 M, a consistent calculation gives log K′ ≈ 3.74.

Source: NIST Stability Constants of Metal Complexes Database, SRD‑46 (metal_41 with ligand_8873; vlm_152319, vlm_152316, vlm_152328).

---