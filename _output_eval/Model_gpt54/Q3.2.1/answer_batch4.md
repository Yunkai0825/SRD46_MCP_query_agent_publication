Using the matched Cu²⁺–glycine data in SRD-46, you can estimate the second stepwise constant from the relation:

\[
\beta_2 = K_1 K_2 \quad \Rightarrow \quad \log K_2 = \log \beta_2 - \log K_1
\]

At **25 °C, I = 0**, the database reports:

| Quantity | Value |
|---|---:|
| logK₁ for Cu²⁺ + L ⇌ ML | 8.56 |
| logβ₂ for Cu²⁺ + 2L ⇌ ML₂ | 15.7 |

So:

| Calculation | Value |
|---|---:|
| logK₂ = 15.7 − 8.56 | 7.14 |
| logβ₂(calc) = logK₁ + logK₂ | 15.70 |

Thus the estimated overall constant is:

| Estimated β₂ | Value |
|---|---:|
| logβ₂(calc) | 15.70 |
| β₂(calc) | \(10^{15.70}\) |

Comparison with the directly reported value:

| Condition | logβ₂(calc) from K₁·K₂ | logβ₂(reported) | Difference |
|---|---:|---:|---:|
| 25 °C, I = 0 | 15.70 | 15.7 | 0.00 |

They agree exactly within the precision reported by the database. This is expected because the SRD-46 entries use the same ligand form **L** and matched conditions, so the thermodynamic identity \( \beta_2 = K_1K_2 \) is internally consistent.

**Source:** NIST SRD-46, Cu²⁺ (`metal_41`) – glycine (`ligand_5760`) stability data.

---