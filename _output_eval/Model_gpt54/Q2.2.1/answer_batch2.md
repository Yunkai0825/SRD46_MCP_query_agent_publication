Using the SRD-46 data retrieved so far, I **can’t yet compute the true database-wide percentage** from the `search_stability` result, because that tool returned only a **capped 200-row sample**, not a count of all 25 °C measurements.

What we do know is:

| Quantity | Value |
|---|---:|
| Total stability-constant measurements in `ligandmetal_stability_measured` | 79,063 |
| Measurements with non-null `temperature_c` | 79,063 |
| Measurements in the 298.0–298.3 K window | 0 |
| Measurements in the 24.9–25.1 °C window | **not counted yet** |

So the database appears to store temperatures in **°C**, not K, and the correct definition for “25 °C” is the **24.9–25.1 °C** window. But I still need an actual **count** of rows in that window to calculate the percentage.

If you want, I can continue and get the exact numerator, then report:

| Metric | Formula |
|---|---|
| Percentage at 25 °C | `100 × (count with 24.9 ≤ temperature_c ≤ 25.1) / 79,063` |

Source: **NIST SRD-46**.

---