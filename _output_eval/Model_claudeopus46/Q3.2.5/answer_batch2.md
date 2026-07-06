## Zn²⁺–EDTA Stability Constant: Ionic-Strength Extrapolation to I = 0

### Raw Data from SRD-46

All measurements are for the 1:1 formation reaction **[M] + [L] ⇌ [ML]** (beta_def_812) at **25 °C**:

| vlm_id | Quantity | log K / value | I (mol L⁻¹) |
|--------|----------|---------------|--------------|
| vlm_108710 | log K | **18.0** | **0** |
| vlm_108707 | log K | 16.5 | 0.1 |
| vlm_108711 | ΔH (kJ mol⁻¹) | −19.7 | 0.1 |
| vlm_108712 | ΔS (J mol⁻¹ K⁻¹) | 250.2 | 0.1 |
| vlm_108708 | log K | 15.7 | 0.5 |
| vlm_108709 | log K | 15.7 | 1.0 |

### Extrapolation to I → 0

Using the three finite-ionic-strength log K values and a simple linear fit of **log K vs √I**:

| I (M) | √I | log K |
|-------|----|-------|
| 0.1 | 0.316 | 16.5 |
| 0.5 | 0.707 | 15.7 |
| 1.0 | 1.000 | 15.7 |

A least-squares line through these three points gives:

- **Slope ≈ −1.03**
- **Intercept (I → 0) ≈ 16.9**

This is consistent with the Debye–Hückel expectation: the formation of ZnEDTA²⁻ from Zn²⁺ and EDTA⁴⁻ involves a large change in charge product (Δz² = −12), so log K should increase substantially as ionic strength drops and activity coefficients diverge from unity.

### Comparison with the Database I = 0 Value

| Source | log K (I = 0, 25 °C) |
|--------|----------------------|
| **SRD-46 entry** (vlm_108710) | **18.0** |
| **Linear √I extrapolation** | **≈ 16.9** |
| **Difference** | **≈ 1.1 log units** |

### Interpretation

The simple linear extrapolation undershoots the thermodynamic (I = 0) value by about **1 log unit**. This gap is expected for several reasons:

1. **Non-linear activity-coefficient behaviour.** The Debye–Hückel limiting law is only linear in √I at very low ionic strength (I < ~0.01 M). At I = 0.1–1.0 M the relationship curves, so a straight line through these points underestimates the true intercept.
2. **Large charge product.** For Zn²⁺ + EDTA⁴⁻ → ZnEDTA²⁻, the Δz² term is very large (−12), amplifying the curvature and making the correction from I = 0.1 to I = 0 much steeper than a linear fit captures.
3. **Medium effects.** The three data points may come from different background electrolytes, adding scatter.

A more rigorous treatment (extended Debye–Hückel, Davies equation, or SIT) would curve upward at low √I and converge much closer to the database value of **log K° = 18.0**. The SRD-46 thermodynamic value of 18.0 is therefore fully consistent with the finite-I data once proper activity-coefficient corrections are applied.

*Source: NIST Standard Reference Database 46 (SRD-46).*

---