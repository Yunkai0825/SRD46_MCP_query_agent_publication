## Cu²⁺–Glycine: Estimating β₂ from Stepwise Constants

### Key Definitions

| Symbol | Equilibrium | Beta Definition |
|--------|------------|-----------------|
| **K₁** | Cu²⁺ + L⁻ ⇌ CuL⁺ | beta_def_812: [ML]/[M][L] |
| **K₂** | CuL⁺ + L⁻ ⇌ CuL₂ | (derived: K₂ = β₂ / K₁) |
| **β₂** | Cu²⁺ + 2L⁻ ⇌ CuL₂ | beta_def_840: [ML₂]/[M][L]² |

The database stores **K₁** and **β₂** directly but not K₂ as a separate entry. Since β₂ = K₁ × K₂, we can derive **K₂ = β₂ / K₁** (or log K₂ = log β₂ − log K₁) from condition-matched pairs, then verify the round-trip.

### Condition-Matched Comparison

Pairing K₁ and β₂ entries at the **same temperature and ionic strength**:

| T (°C) | I (mol/L) | log K₁ | log β₂ (reported) | log K₂ = log β₂ − log K₁ | log β₂ (calc) = log K₁ + log K₂ | Δ |
|---------|-----------|--------|-------------------|--------------------------|----------------------------------|---|
| 10 | 0 | 8.80 | 16.30 | 7.50 | **16.30** | 0.00 |
| 25 | 0 | 8.56 | 15.70 | 7.14 | **15.70** | 0.00 |
| 25 | 0.1 | 8.19 | 15.10 | 6.91 | **15.10** | 0.00 |
| 25 | 0.5 | 8.10 | 15.00 | 6.90 | **15.00** | 0.00 |
| 25 | 1.0 | 8.20 | 15.10 | 6.90 | **15.10** | 0.00 |
| 25 | 2.0 | 8.38 | 15.40 | 7.02 | **15.40** | 0.00 |
| 25 | 2.5 | 8.34 | 15.40 | 7.06 | **15.40** | 0.00 |
| 37 | 0.15 | 7.99 | 14.69 | 6.70 | **14.69** | 0.00 |
| 40 | 0 | 8.37 | 15.30 | 6.93 | **15.30** | 0.00 |

### Result

The calculated log β₂ = log K₁ + log K₂ matches the directly reported log β₂ **exactly** in every condition-matched pair — as expected, since β₂ ≡ K₁ · K₂ by thermodynamic definition.

### Chemistry Insights

- **K₁ > K₂** in every case (log K₁ ≈ 8.2–8.8 vs. log K₂ ≈ 6.7–7.5), reflecting the typical **stepwise decline** — the second glycinate binds more weakly because the first ligand already partially satisfies the metal's coordination demand and introduces steric/electrostatic repulsion.
- At 25 °C and I = 0.1 M (a common reference condition), the recommended values are **log K₁ = 8.19**, **log K₂ = 6.91**, and **log β₂ = 15.10**, consistent with widely cited literature for the Cu²⁺–glycinate system.
- The ratio K₁/K₂ ≈ 10^1.3 ≈ 20 is larger than the statistical factor of 4 expected for a simple octahedral bis-complex, suggesting additional electronic or structural effects in the second binding step.

*Source: NIST SRD-46 Critical Stability Constants Database*

---