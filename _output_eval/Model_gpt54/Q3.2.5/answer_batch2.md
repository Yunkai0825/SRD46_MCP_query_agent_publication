Using the Zn–EDTA **ML/[M][L]** definition (`beta_def_812`) at **25 °C**, SRD‑46 gives the following logK values:

| Ionic strength, I / M | logK |
|---:|---:|
| 0.0 | 18.0 |
| 0.1 | 16.5 |
| 0.5 | 15.7 |
| 1.0 | 15.7 |

A simple low-ionic-strength extrapolation can be made from the nonzero points using the common empirical form **logK = a + b√I**.

Using the three nonzero data points:

| I / M | √I | logK |
|---:|---:|---:|
| 0.1 | 0.316 | 16.5 |
| 0.5 | 0.707 | 15.7 |
| 1.0 | 1.000 | 15.7 |

The resulting straight-line estimate is approximately:

| Fit form | Estimated value |
|---|---:|
| logK ≈ a + b√I | a ≈ **16.9** |

So the **extrapolated zero-ionic-strength value** is about:

| Quantity | logK at I = 0 |
|---|---:|
| Extrapolated from nonzero-I data | **~16.9** |
| Explicit SRD‑46 entry at I = 0 | **18.0** |

### Comparison
| Source | logK(0) |
|---|---:|
| Extrapolated trend | ~16.9 |
| Database zero-ionic-strength entry | 18.0 |
| Difference | ~1.1 log units |

### Interpretation
The explicit **I = 0** SRD‑46 value is **substantially higher** than the value obtained by extrapolating the sparse nonzero-I series. That suggests the nonzero-I points do not follow a clean linear dependence in √I over this whole range, or that the entries may come from different supporting media / conventions not exposed in the summary table. In practice, for metal–EDTA systems, conditional stability usually decreases as ionic strength rises, so the direction of the trend is chemically sensible; the mismatch in magnitude means the extrapolation should be treated as **rough**, while the database’s direct **I = 0** entry is the better thermodynamic reference.

**Source:** NIST SRD‑46, Zn²⁺ + EDTA, `beta_def_812` (`[M] + [L] <=> [ML]`), 25 °C.

---