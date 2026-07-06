Using the **matched 25 °C, I = 0.1 M** SRD‑46 data for malonic acid and Cu²⁺–malonate:

| quantity | SRD‑46 value |
|---|---:|
| pKa₁ for H₂L ⇌ HL⁻ + H⁺ | 2.65 |
| pKa₂ for HL⁻ ⇌ L²⁻ + H⁺ | 5.27 |
| log K for Cu²⁺ + L²⁻ ⇌ CuL | 5.04 |

we can estimate the **conditional** constant at **pH 4**.

### 1) Convert pKa to Ka

| quantity | calculation | value |
|---|---|---:|
| \(K_{a1}\) | \(10^{-2.65}\) | \(2.24\times10^{-3}\) |
| \(K_{a2}\) | \(10^{-5.27}\) | \(5.37\times10^{-6}\) |
| \([H^+]\) | \(10^{-4}\) | \(1.00\times10^{-4}\) |

### 2) Fraction of free malonate present as \(L^{2-}\) at pH 4

For a diprotic acid \( \mathrm{H_2L} \), the fraction as \( \mathrm{L^{2-}} \) is

| expression |
|---|
| \(\alpha_{L^{2-}}=\dfrac{K_{a1}K_{a2}}{[H^+]^2+[H^+]K_{a1}+K_{a1}K_{a2}}\) |

Substituting the values:

| term | value |
|---|---:|
| \(K_{a1}K_{a2}\) | \(1.20\times10^{-8}\) |
| \([H^+]^2\) | \(1.00\times10^{-8}\) |
| \([H^+]K_{a1}\) | \(2.24\times10^{-7}\) |
| denominator | \(2.46\times10^{-7}\) |

So:

| quantity | value |
|---|---:|
| \(\alpha_{L^{2-}}\) | \( \dfrac{1.20\times10^{-8}}{2.46\times10^{-7}} \approx 4.88\times10^{-2}\) |

Thus only about **4.9%** of total free malonic acid is in the fully deprotonated **malonate \(L^{2-}\)** form at pH 4.

### 3) Convert the intrinsic Cu–malonate constant

| quantity | calculation | value |
|---|---|---:|
| \(K\) | \(10^{5.04}\) | \(1.10\times10^{5}\) |

### 4) Compute the conditional constant

Using \(K' = K\,\alpha_{L^{2-}}\):

| quantity | calculation | value |
|---|---|---:|
| \(K'\) | \((1.10\times10^{5})(4.88\times10^{-2})\) | \(5.4\times10^{3}\) |
| \(\log K'\) | \(5.04 + \log(4.88\times10^{-2})\) | \(3.73\) |


| result | value |
|---|---:|
| Conditional stability constant at pH 4, \(K'\) | \(\approx 5.4\times10^{3}\) |
| Conditional \(\log K'\) | **\(\approx 3.73\)** |

So at **pH 4**, the Cu²⁺–malonate complex is effectively weaker than the intrinsic \( \log K = 5.04 \) because most malonic acid is still protonated and only a small fraction is available as the binding form \( \mathrm{L^{2-}} \).

**Source:** NIST SRD‑46 values used: malonic acid pKa values **2.65** and **5.27** at **25 °C, I = 0.1 M**; Cu²⁺ + malonate \( \mathrm{L^{2-}} \to \mathrm{CuL} \) **log K = 5.04** at **25 °C, I = 0.1 M**.

---