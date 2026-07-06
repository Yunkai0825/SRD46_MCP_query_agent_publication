Using SRD-46 data for **malonic acid** and **Cu²⁺–malonate**, an estimate at **pH 4** is:

| Quantity | Value | Conditions / note |
|---|---:|---|
| pKa1 | 2.65 | malonic acid, 25 °C, I = 0.1 M |
| pKa2 | 5.27 | malonic acid, 25 °C, I = 0.1 M |
| log K (Cu²⁺ + L²⁻ ⇌ CuL) | 5.04 | Cu–malonate, 25 °C, I = 0.1 M |
| Estimated log K′ at pH 4 | 3.82 | conditional for total uncomplexed malonate acid/base pool |

### Calculation

For diprotic malonic acid:

| Equilibrium | Expression |
|---|---|
| H₂L ⇌ H⁺ + HL⁻ | \(K_{a1} = 10^{-2.65}\) |
| HL⁻ ⇌ H⁺ + L²⁻ | \(K_{a2} = 10^{-5.27}\) |

At pH 4, \([H^+] = 10^{-4}\).

The fraction of total free ligand present as **L²⁻** is:

| Formula | Value |
|---|---:|
| \(\alpha_{L^{2-}} = \dfrac{K_{a1}K_{a2}}{[H^+]^2 + [H^+]K_{a1} + K_{a1}K_{a2}}\) | — |

Numerically:

| Term | Value |
|---|---:|
| \(K_{a1}\) | \(2.24 \times 10^{-3}\) |
| \(K_{a2}\) | \(5.37 \times 10^{-6}\) |
| \(K_{a1}K_{a2}\) | \(1.20 \times 10^{-8}\) |
| \([H^+]^2\) | \(1.00 \times 10^{-8}\) |
| \([H^+]K_{a1}\) | \(2.24 \times 10^{-7}\) |
| Denominator | \(2.46 \times 10^{-7}\) |
| \(\alpha_{L^{2-}}\) | 0.0487 |

So only about **4.9%** of free malonate is in the fully deprotonated **L²⁻** form at pH 4.

Now use:

| Relation | Value |
|---|---:|
| \(K' = K \alpha_{L^{2-}}\) | — |
| \(K = 10^{5.04}\) | \(1.10 \times 10^{5}\) |
| \(K' = 1.10 \times 10^5 \times 0.0487\) | \(5.35 \times 10^3\) |

Therefore:

| Conditional constant | Value |
|---|---:|
| \(K'\) | \(5.4 \times 10^3\) |
| \(\log K'\) | **3.73** |

### Note on the reported estimate
If you instead use the **I = 0** value from SRD-46, **log K = 5.80**, then:

| Assumption | log K′ at pH 4 |
|---|---:|
| using log K = 5.80 | 4.49 |
| using log K = 5.04 (matched to pKa ionic strength 0.1 M) | **3.73** |

### Interpretation

At pH 4, Cu²⁺ binding is weakened by about **1.31 log units** relative to the intrinsic \( \mathrm{Cu^{2+} + L^{2-} \rightleftharpoons CuL} \) constant, because most malonate is present as **HL⁻**, not **L²⁻**. So the best matched SRD-46 estimate is **log K′ ≈ 3.73** at 25 °C, I = 0.1 M.

**Source:** NIST SRD-46 entries for malonic acid pKa (ligand_8873; vlm_151949, vlm_151918) and Cu²⁺–malonate stability constant (beta_def_812; vlm_152316).

---