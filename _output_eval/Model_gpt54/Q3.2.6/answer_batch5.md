Using SRD-46 values at **25 °C, I = 0.1 M**:

| Quantity | Value |
|---|---:|
| pKa₁ of malonic acid | 2.65 |
| pKa₂ of malonic acid | 5.27 |
| log K for Cu²⁺ + L²⁻ ⇌ CuL | 5.04 |

Here, the reported Cu–malonate constant is for binding of the **fully deprotonated ligand** \(L^{2-}\), so at pH 4 we need the fraction of total free malonate present as \(L^{2-}\).

### 1) Fraction of malonate present as \(L^{2-}\) at pH 4
For diprotic malonic acid \(H_2L \rightleftharpoons HL^- \rightleftharpoons L^{2-}\),

\[
\alpha_{L^{2-}}=\frac{K_{a1}K_{a2}}{[H^+]^2+K_{a1}[H^+]+K_{a1}K_{a2}}
\]

with

\[
K_{a1}=10^{-2.65}=2.24\times 10^{-3}
\]
\[
K_{a2}=10^{-5.27}=5.37\times 10^{-6}
\]
\[
[H^+]=10^{-4}
\]

Then

\[
K_{a1}K_{a2}=(2.24\times 10^{-3})(5.37\times 10^{-6})\approx 1.20\times 10^{-8}
\]

Denominator:

\[
[H^+]^2+K_{a1}[H^+]+K_{a1}K_{a2}
=10^{-8}+2.24\times 10^{-7}+1.20\times 10^{-8}
\approx 2.46\times 10^{-7}
\]

So

\[
\alpha_{L^{2-}} \approx \frac{1.20\times 10^{-8}}{2.46\times 10^{-7}}
\approx 4.89\times 10^{-2}
\]

Thus about **4.9%** of uncomplexed malonate is present as \(L^{2-}\) at pH 4.

### 2) Conditional stability constant
The conditional constant is

\[
K' = \beta_1 \alpha_{L^{2-}}
\]

where

\[
\beta_1 = 10^{5.04} \approx 1.10\times 10^5
\]

Therefore,

\[
K' \approx (1.10\times 10^5)(4.89\times 10^{-2})
\approx 5.4\times 10^3
\]

and

\[
\log K' = 5.04 + \log(4.89\times 10^{-2}) \approx 3.73
\]

## Estimated result

| Quantity | Estimated value |
|---|---:|
| \(\alpha_{L^{2-}}\) at pH 4 | 0.0489 |
| \(K'\) | \(5.4 \times 10^3\) |
| \(\log K'\) | **3.73** |

So the **conditional stability constant for Cu²⁺–malonate at pH 4 is about \(\log K' \approx 3.7\)**.

A quick chemical takeaway: although the intrinsic Cu²⁺–malonate binding to \(L^{2-}\) is fairly strong, pH 4 is below malonic acid’s second pKa, so only a small fraction is fully deprotonated and available in the form used by the tabulated \(K\). That protonation penalty lowers the effective binding by about **1.3 log units**.  

**Source:** NIST SRD-46.

---