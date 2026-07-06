SRD-46 gives matched values for Cu²⁺–glycine under several conditions, but it reports **β₁ (ML)** and **β₂ (ML₂)** directly, not a separate stepwise **K₂** row. So the best we can do from the database entries shown is infer the stepwise second constant as:

\[
\log K_2 = \log \beta_2 - \log \beta_1
\]

and then check that

\[
\log \beta_2(\text{calc}) = \log K_1 + \log K_2
\]

Using the matched 25 °C, \(I=0.10\) M pair:

| Quantity | SRD-46 value |
|---|---:|
| \(\log K_1 = \log \beta_1\) for \([M]+[L]\rightleftharpoons [ML]\) | 8.19 |
| \(\log \beta_2\) for \([M]+2[L]\rightleftharpoons [ML_2]\) | 15.1 |
| Inferred \(\log K_2 = 15.1 - 8.19\) | 6.91 |
| Calculated \(\log \beta_2 = \log K_1 + \log K_2\) | 15.1 |

So:

| Comparison | Value |
|---|---:|
| Directly reported \(\log \beta_2\) | 15.1 |
| Calculated \(\log \beta_2\) from \(K_1K_2\) | 15.1 |
| Difference | 0.00 |

At 25 °C, \(I=0.10\) M, the corresponding linear overall constant is approximately:

| Form | Value |
|---|---:|
| \(\beta_2 = 10^{15.1}\) | \(1.26 \times 10^{15}\) |

This exact agreement is expected because, by definition, \(\beta_2 = K_1K_2\). Chemically, the inferred drop from \(\log K_1 = 8.19\) to \(\log K_2 = 6.91\) is reasonable: binding of the second glycinate is weaker than the first, reflecting reduced availability and increasing crowding around Cu²⁺.  
**Source:** NIST SRD-46, Cu²⁺ (metal_41) + glycine (ligand_5760), matched entries **vlm_93847** (\(\log \beta_1\)) and **vlm_93862** (\(\log \beta_2\)).

---