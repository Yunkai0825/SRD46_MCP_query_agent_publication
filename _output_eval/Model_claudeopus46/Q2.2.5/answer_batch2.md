## Distribution of Constant Types in SRD-46 Stability Measurements

The NIST SRD-46 database contains **79,063** stability constant measurements, distributed across three constant types:

| Constant Type | Description | Count | Percentage |
|:---:|---|---:|---:|
| **K** | Stepwise stability constant (log *K*) | 60,540 | 76.57% |
| **H** | Protonation / hydrolysis constant | 9,693 | 12.26% |
| **S** | Overall stability constant (log *β*) | 8,830 | 11.17% |

### Key Observations

- **Stepwise constants (K)** dominate the database, accounting for over three-quarters of all entries. This reflects the common experimental practice of reporting successive ligand-binding equilibria (M + L ⇌ ML, ML + L ⇌ ML₂, etc.).
- **Protonation/hydrolysis constants (H)** make up ~12%, capturing metal-ion hydrolysis and ligand protonation side-reactions that are essential for speciation modeling.
- **Overall (cumulative) constants (S / β)** represent ~11% of entries. These describe the global formation reaction (M + nL ⇌ MLₙ) and are mathematically related to the stepwise constants (β_n = ∏Kᵢ).

*Source: NIST Standard Reference Database 46 (SRD-46)*

---