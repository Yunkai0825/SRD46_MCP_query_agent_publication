## Cu²⁺–Glycine: Stepwise K₁, K₂ → Overall β₂

### Key Relationships

For stepwise formation constants:

- **K₁**: Cu²⁺ + L⁻ ⇌ CuL⁺ → log K₁
- **K₂**: CuL⁺ + L⁻ ⇌ CuL₂ → log K₂

The overall constant is defined as:

> **β₂ = K₁ × K₂** → **log β₂ = log K₁ + log K₂**

The database reports **log K₁** (beta_def_812: `[M] + [L] ⇌ [ML]`) and **log β₂** (beta_def_840: `[M] + 2[L] ⇌ [ML₂]`). The stepwise log K₂ is obtained by difference: **log K₂ = log β₂ − log K₁**.

### Data at 25 °C (from NIST SRD-46)

| I (mol/L) | log K₁ (reported) | log β₂ (reported) | log K₂ = log β₂ − log K₁ | log β₂(calc) = log K₁ + log K₂ | Δ |
|-----------|-------------------|-------------------|--------------------------|-------------------------------|---|
| 0         | 8.56              | 15.70             | 7.14                     | **15.70**                     | 0.00 |
| 0.1       | 8.19              | 15.10             | 6.91                     | **15.10**                     | 0.00 |
| 0.5       | 8.10              | 15.00             | 6.90                     | **15.00**                     | 0.00 |
| 1.0       | 8.20              | 15.10             | 6.90                     | **15.10**                     | 0.00 |
| 2.0       | 8.38              | 15.40             | 7.02                     | **15.40**                     | 0.00 |
| 2.5       | 8.34              | 15.40             | 7.06                     | **15.40**                     | 0.00 |

### Result

The calculated log β₂ (= log K₁ + log K₂) **matches the directly reported log β₂ exactly** at every ionic strength. This is expected because the database stores the overall constant β₂ directly, and the stepwise constants are thermodynamically self-consistent:

$$\log \beta_2 = \log K_1 + \log K_2 = 8.56 + 7.14 = \boxed{15.70} \quad (25\,°\text{C},\; I = 0)$$

### Chemistry Insight

- **K₂ < K₁** (log K₂ ≈ 7.1 vs log K₁ ≈ 8.6), reflecting the typical statistical effect and increased steric/electrostatic repulsion when binding a second glycinate to the Cu²⁺ center.
- The log β₂ value of ~15.1 at physiological ionic strength (I = 0.1 M) makes Cu²⁺–glycine one of the most stable amino acid complexes, relevant to copper transport in biological fluids.
- The modest decrease in both log K₁ and log β₂ from I = 0 to I = 0.5 M, followed by a slight increase at higher I, is a classic Debye–Hückel-to-specific-ion-interaction transition.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes).*

---