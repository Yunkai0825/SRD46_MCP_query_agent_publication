Using the SRD‑46 Zn–EDTA **ML** formation constant entries at 25 °C, the reported values are:

| I / M | log β(ZnEDTA) |
|---:|---:|
| 0.0 | 18.0 |
| 0.1 | 16.5 |
| 0.5 | 15.7 |
| 1.0 | 15.7 |

A simple empirical extrapolation from the **nonzero ionic-strength points** to \(I=0\) gives a zero-ionic-strength intercept close to the database’s explicit \(I=0\) value:

| Fit basis | Extrapolation form | Estimated log β at I = 0 |
|---|---|---:|
| 0.1, 0.5, 1.0 M points | linear in \(I\) | ~16.7 |
| 0.1, 0.5, 1.0 M points | linear in \(\sqrt{I}\) | ~17.0 |

Comparison with the SRD‑46 zero-ionic-strength record:

| Source in SRD‑46 | T / °C | I / M | log β |
|---|---:|---:|---:|
| `vlm_108710` | 25 | 0.0 | 18.0 |

### Interpretation
The measured trend is the expected one: **log β decreases as ionic strength increases**. However, extrapolating only from the three nonzero points gives **log β° ≈ 16.7–17.0**, which is about **1.0–1.3 log units lower** than the explicit SRD‑46 \(I=0\) value of **18.0**.

### Likely reason
This suggests the ionic-strength dependence here is **not well described by a simple straight-line extrapolation** across 0.1–1.0 M, or that the \(I=0\) entry is a **reference/standard-state value** rather than just another point on the same linear trend. The flattening between 0.5 and 1.0 M also warns against overfitting a Debye–Hückel-type form from only three points.

### Bottom line
| Quantity | log β |
|---|---:|
| Extrapolated to \(I=0\) from nonzero-I data | ~16.7–17.0 |
| SRD‑46 explicit \(I=0\) value | 18.0 |
| Difference | ~1.0–1.3 |

So, the database **does contain a zero-ionic-strength value**, and it is **significantly higher** than a naive extrapolation from the nonzero ionic-strength measurements.

*Source: NIST SRD‑46 / Stability Constants Database, Zn²⁺–EDTA (`beta_def_812`, ML formation constant) entries at 25 °C.*

---