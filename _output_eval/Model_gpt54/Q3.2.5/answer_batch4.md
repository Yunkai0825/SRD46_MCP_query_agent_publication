| Status | Note |
|---|---|
| Incomplete | I retrieved the Zn–EDTA ML data, but I still need one more execution step to group/filter by medium correctly after the failed `db_distribution` call, then I can do the extrapolation and comparison. |

The relevant SRD-46 values already found for **Zn²⁺ + EDTA → ZnEDTA²⁻** (`beta_def_812`, overall ML constant) are:

| vlm_id | type | logK | T (°C) | I (M) |
|---|---:|---:|---:|---:|
| vlm_108710 | logK | 18.0 | 25 | 0.0 |
| vlm_108707 | logK | 16.5 | 25 | 0.1 |
| vlm_108708 | logK | 15.7 | 25 | 0.5 |
| vlm_108709 | logK | 15.7 | 25 | 1.0 |

To finish properly, I need to inspect the individual records/provenance and medium before fitting.

---