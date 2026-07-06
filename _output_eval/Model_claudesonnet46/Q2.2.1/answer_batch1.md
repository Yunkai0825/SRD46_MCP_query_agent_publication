## Results

Based on a direct query of the SRD-46 `ligandmetal_stability_measured` table:

| Metric | Count |
|---|---|
| **Total stability-constant measurements** | 79,063 |
| **Measurements at 25 °C (±0.1 °C)** | 67,237 |
| **Percentage at 25 °C** | **85.0 %** |

### Key Takeaways

- **85 %** of all stability-constant measurements in the NIST SRD-46 database were conducted at exactly (or very near) 25 °C — an overwhelming majority.
- This reflects the long-standing convention in solution thermodynamics to report equilibrium constants at 25 °C (298.15 K), making data directly comparable across laboratories and publications.
- The remaining ~15 % of measurements span other temperatures (e.g., 20 °C, 37 °C, or variable-temperature studies), which are valuable for deriving enthalpy/entropy of complexation via van't Hoff analysis.

*Source: NIST SRD-46 database, `ligandmetal_stability_measured` table; temperature filter: |T − 25.0 °C| ≤ 0.1 °C.*

---