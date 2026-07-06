SRD-46 has four Zn²⁺–EDTA **ML** formation constants at 25 °C for the same species definition (**beta_def_812**, `[M] + [L] ⇌ [ML]`), including an explicit **I = 0** entry. Using the nonzero ionic-strength points, the trend is a clear decrease of logK with increasing ionic strength.

| I / M | logK |
|---:|---:|
| 0.0 | 18.0 |
| 0.1 | 16.5 |
| 0.5 | 15.7 |
| 1.0 | 15.7 |

### Simple extrapolation to I = 0
Using the three nonzero points only, a quick linear fit of **logK vs I** gives an intercept of about **16.4** at **I = 0**.

| Fit used | Data used | Extrapolated logK at I = 0 |
|---|---|---:|
| Linear in I | I = 0.1, 0.5, 1.0 M | ~16.4 |

### Comparison with the database zero-ionic-strength value
SRD-46 also contains a direct **I = 0** measurement/value for the same Zn–EDTA ML equilibrium:

| Source in SRD-46 | T / °C | I / M | logK |
|---|---:|---:|---:|
| `vlm_108710` | 25 | 0.0 | 18.0 |

### Difference
| Quantity | Value |
|---|---:|
| Extrapolated from nonzero-I points | ~16.4 |
| Explicit SRD-46 I = 0 value | 18.0 |
| Difference | ~1.6 log units |

### Interpretation
The nonzero-I series is sparse and already quite depressed by ionic strength, so a simple linear extrapolation from 0.1–1.0 M **underestimates** the database’s zero-ionic-strength value. In other words, for Zn²⁺–EDTA the ionic-strength dependence appears **strongly nonlinear near very low I**, or the **I = 0 entry is itself a reference/extrapolated standard-state value** rather than just another point on the same medium-specific series.

If you want, I can next pull the **literature/citation records** for `vlm_108710`, `vlm_108707`, `vlm_108708`, and `vlm_108709` to check whether the **I = 0** number is explicitly measured or author-extrapolated.

---