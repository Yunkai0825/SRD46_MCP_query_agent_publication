To estimate the conditional stability constant for Cu2+–malonate at pH 4, we factor how much of malonic acid is in the binding-active form (L2−) at that pH and scale the intrinsic 1:1 formation constant accordingly.

Data (SRD‑46):
- Malonic acid (H2L) pKa1 = 2.65; pKa2 = 5.27 (ligand_8873; aqueous).
- At pH 4, the fraction of total ligand present as L2− is:
  α(L2−) = (Ka1·Ka2)/([H+]^2 + [H+]·Ka1 + Ka1·Ka2)
         = 10^(−pKa1)·10^(−pKa2) / (10^(−2pH) + 10^(−pH−pKa1) + 10^(−pKa1−pKa2))
         ≈ 0.049 at pH 4 (log10 α ≈ −1.31).

Relationship to the conditional constant:
- Let β11 (or Kf) be the intrinsic 1:1 formation constant for Cu2+ + L2− ⇌ CuL (log β11 = log Kf) under the same medium (usually 25 °C, dilute ionic strength).
- The conditional formation constant for total ligand (LT) at pH 4 (assuming complexation mainly with L2−) is:
  K′(pH 4) = β11 × α(L2−)
  log K′(pH 4) = log β11 + log α(L2−) ≈ log β11 − 1.31

Worked form (plug in your intrinsic Cu2+–malonate log β11):
- Example: if log β11 = 3.50, then log K′(pH 4) ≈ 3.50 − 1.31 = 2.19, so K′ ≈ 10^2.19 ≈ 1.6×10^2 M^−1.

Notes and caveats:
- At pH 4 the HL− form is abundant; some datasets also report an MHL complex ([MHL]/[M][HL], beta_def_779). If MHL is significant under your conditions, the ML-only K′ is a lower bound to total conditional complexation.
- Use β11 measured in the same solvent, temperature, and ionic strength as the pKa data for the most consistent estimate.

Table (inputs and result at pH 4):
| Quantity | Value | Source/Comment |
|---------|-------|----------------|
| pKa1 (H2L ⇌ HL− + H+) | 2.65 | SRD‑46 (ligand_8873) |
| pKa2 (HL− ⇌ L2− + H+) | 5.27 | SRD‑46 (ligand_8873) |
| α(L2−) at pH 4 | 0.049 (log α = −1.31) | from pKa values above |
| log β11 (Cu2+ + L2− ⇌ CuL) | your value | SRD‑46 (Cu–malonate, beta_def_812) |
| log K′(pH 4) | log β11 − 1.31 | K′ = β11 × α(L2−) |

Source: NIST Standard Reference Database 46 (SRD‑46): Critically Selected Stability Constants of Metal Complexes.

---