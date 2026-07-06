| Quantity | Value | Conditions | SRD‑46 reference |
|---|---:|---|---|
| pKa1 (H2L ⇌ HL− + H+) | 2.65 | 25 °C, I = 0.1 M (aq) | vlm_151949 |
| pKa2 (HL− ⇌ L2− + H+) | 5.27 | 25 °C, I = 0.1 M (aq) | vlm_151918 |
| log β1 for Cu2+ + L2− ⇌ CuL | 5.04 | 25 °C, I = 0.1 M (aq), β_def_812 | vlm_152316 |

Calculation (pH 4, matching I = 0.1 M):
- For a diprotic acid H2L with Ka1 = 10^−pKa1 and Ka2 = 10^−pKa2, the fraction of total ligand present as L2− is:
  αL2− = (Ka1·Ka2) / ([H+]^2 + [H+]·Ka1 + Ka1·Ka2)
- Numbers: pH 4 ⇒ [H+] = 1.0×10^−4 M; Ka1 = 10^−2.65 ≈ 2.24×10^−3; Ka2 = 10^−5.27 ≈ 5.37×10^−6.
  αL2− ≈ (2.24×10^−3 · 5.37×10^−6) / (1.0×10^−8 + 1.0×10^−4·2.24×10^−3 + 2.24×10^−3·5.37×10^−6)
         ≈ 0.049 (log αL2− ≈ −1.31)

- Conditional formation constant at pH 4 for the CuL (with L = L2−) reaction:
  K′ = β1 · αL2−  ⇒  log K′ = log β1 + log αL2− ≈ 5.04 − 1.31 = 3.73

| Result | Value | Notes |
|---|---:|---|
| log K′(pH 4) | ≈ 3.73 | for Cu2+ + L2− ⇌ CuL, referenced to total malonate (H2L + HL− + L2−) at I = 0.1 M |
| K′(pH 4) | ≈ 5.4 × 10^3 | dimensionless (activities≈concentrations under stated conditions) |

Explanation and assumptions:
- The reported log β1 is defined for Cu2+ + L2− ⇌ CuL (β_def_812). At pH 4, only the L2− fraction of total malonate participates in this reaction, so the conditional constant is reduced by αL2−.
- We matched ionic strength (0.1 M) and temperature (25 °C) between pKa and Cu–malonate data from SRD‑46. Using the infinite‑dilution log β1 = 5.8 instead would give log K′ ≈ 4.49, but mixing I values is not recommended.
- At pH 4 most ligand is HL−; protonated complexes like CuHL+ may form, but the above estimate specifically uses the CuL (L2−) constant, as requested.

Source: NIST SRD‑46 (ligand: malonic acid/malonate, ligand_8873; pKa entries vlm_151949, vlm_151918; Cu–malonate formation constant vlm_152316, β_def_812).

---