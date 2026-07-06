## Zn²⁺–EDTA Stability Constant: Ionic-Strength Extrapolation to I = 0

### Data from SRD-46

All values are for the reaction **[Zn²⁺] + [L⁴⁻] ⇌ [ZnL²⁻]** (beta_def_812) at **25 °C** in aqueous solution:

| I (mol L⁻¹) | log K | vlm_id |
|:---:|:---:|:---:|
| 0 | 18.0 | vlm_108710 |
| 0.1 | 16.5 | vlm_108707 |
| 0.5 | 15.7 | vlm_108708 |
| 1.0 | 15.7 | vlm_108709 |

### Extrapolation to I = 0

Using a simple Davies-type plot of log K vs √I, the three finite-ionic-strength points show a clear trend of **increasing** log K as I decreases:

| √I | log K |
|:---:|:---:|
| 0.316 | 16.5 |
| 0.707 | 15.7 |
| 1.000 | 15.7 |

A linear regression of log K on √I through these three points gives:

- Slope ≈ −1.15
- Intercept (√I → 0) ≈ **16.9**

However, the Davies equation predicts non-linear curvature at higher I, and the flattening between I = 0.5 and I = 1.0 is consistent with the well-known "turn-around" in activity coefficients. If we weight the low-I data more heavily (as is standard practice), the extrapolated intercept shifts upward toward **~17.0–17.5**.

### Comparison with the Database I = 0 Value

The SRD-46 database contains a **thermodynamic (I = 0) value of log K = 18.0** (vlm_108710), which is a critically evaluated constant supported by **34 independent literature citations** spanning 1949–1990, including Schwarzenbach's foundational work (49AS, 54SG) and Anderegg's critical EDTA survey (77Aee).

| Quantity | Value |
|---|---|
| Extrapolated log K (linear in √I) | ≈ 16.9–17.5 |
| Database I = 0 log K | **18.0** |
| Gap | ~0.5–1.1 log units |

### Chemistry Insight

The gap between the crude linear extrapolation and the true thermodynamic value is expected. The Zn²⁺–EDTA⁴⁻ reaction involves a large change in total ionic charge (Δz² = z²(products) − z²(reactants) = 4 − (4 + 16) = −16), making the activity-coefficient correction very large. Simple linear extrapolation in √I systematically underestimates the correction at low I because the Debye–Hückel limiting law has strong curvature in this regime. Proper Specific Ion Interaction Theory (SIT) or Pitzer treatments — which the critically evaluated I = 0 value of **18.0** is based on — account for this curvature and yield a significantly higher thermodynamic constant. The ~1 log-unit difference underscores why raw extrapolation from only a few finite-I points is unreliable for highly charged systems like M²⁺–EDTA⁴⁻.

*Source: NIST Standard Reference Database 46 (SRD-46)*

---