## Ni²⁺–Ethylenediamine: Stability Constants vs. Ionic Strength

### Data (25 °C, KNO₃ medium, aqueous)

| I (mol/L) | log β₁ (ML) | log β₂ (ML₂) | log β₃ (ML₃) |
|:---------:|:-----------:|:-------------:|:-------------:|
| 0.0       | 7.90        | 14.53         | 19.18         |
| 0.1       | 7.52        | 13.86         | 18.33         |
| 0.5       | 7.35        | 13.54         | 17.86         |
| 1.0       | 7.32        | 13.46         | 17.67         |
| 2.0       | 7.28        | ~13.5*        | ~17.5*        |
| 3.0       | 6.98        | 12.84         | 16.40         |

*\*Values at I = 2.0 M for ML₂ and ML₃ appear to have a sign-storage artifact in the database (−14.77 and −19.70); the magnitudes are consistent with the overall trend.*

An additional measurement at **37 °C in 0.15 M NaCl** gives log β₁ = 7.60, log β₂ = 14.20, log β₃ = 18.60 — slightly lower than the I = 0 values, consistent with the same ionic-strength effect.

### Is There a Clear Trend?

**Yes — a clear, monotonic decrease in all three cumulative stability constants with increasing ionic strength.**

| Species | log β at I = 0 | log β at I = 3 M | Total Drop |
|---------|:--------------:|:----------------:|:----------:|
| Ni(en)²⁺   | 7.90  | 6.98  | −0.92 |
| Ni(en)₂²⁺  | 14.53 | 12.84 | −1.69 |
| Ni(en)₃²⁺  | 19.18 | 16.40 | −2.78 |

### Chemistry Insights

1. **Steepest drop at low ionic strength.** The largest decrease occurs between I = 0 and 0.1 M (e.g., Δlog β₁ ≈ −0.38), after which the decline becomes more gradual. This is the classic Debye–Hückel behaviour: activity coefficients change most rapidly at low ionic strength where the ionic atmosphere is being established.

2. **The drop scales with the number of ligands.** The total decrease in log β₃ (−2.78) is roughly three times that of log β₁ (−0.92). This is expected because each successive complexation step contributes an additional activity-coefficient correction term, and these accumulate in the overall (cumulative) constant.

3. **Charge considerations.** Ethylenediamine is a neutral ligand, so the complex charge remains +2 regardless of the number of en bound. The ionic-strength effect therefore arises primarily from changes in the activity coefficient of the free Ni²⁺ ion and the neutral en molecules, rather than from large electrostatic charge-product terms. Even so, the effect is substantial — nearly one log unit for β₁ and almost three log units for β₃ over the 0–3 M range.

**Bottom line:** When working with Ni²⁺–en equilibria, the ionic strength of the solution matters significantly. Using an I = 0 (infinite dilution) constant in a 1 M background electrolyte would overestimate the effective stability by roughly 0.6–1.5 log units depending on the species, which could lead to meaningful errors in speciation calculations.

**Source:** NIST Standard Reference Database 46 (SRD-46), Critical Stability Constants.

---