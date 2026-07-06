Here’s the dataset-wide distribution of constant types in SRD-46 stability-constant measurements (ligandmetal_stability_measured):

| Constant type | Count | Percent of measurements |
|---|---:|---:|
| K | 60,540 | 76.57% |
| H | 9,693 | 12.26% |
| S | 8,830 | 11.17% |
| Total | 79,063 | 100% |

Notes and context:
- The constant_type field in the measured-data table is dominated by equilibrium constants (K). Thermodynamic quantities (H, S) make up the remaining ~23.4% of entries.
- If you’d like a breakdown by specific formation-constant definitions (e.g., β, βn for stepwise/overall formation), we can group measurements by their beta_definition instead of the generic constant_type.

Source: NIST Standard Reference Database 46 (SRD‑46).

---