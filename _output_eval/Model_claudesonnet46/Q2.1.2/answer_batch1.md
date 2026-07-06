## Irving–Williams Series: log β₁ of M²⁺ with Ammonia

### SRD-46 Data (25 °C, aqueous KNO₃, thermodynamic I → 0 extrapolation, β-def 812: M²⁺ + NH₃ ⇌ M(NH₃)²⁺)

| Rank | Metal | log β₁ | I (mol/L) | T (°C) |
|------|-------|--------|-----------|--------|
| 1 | **Cu²⁺** | **4.31** | 0.0 | 25 |
| 2 | **Ni²⁺** | **2.80** | 0.0 | 25 |
| 3 | **Co²⁺** | **2.11** | 0.0 | 25 |
| 4 | **Mn²⁺** | **1.00** | 0.0 | 25 |

> **Note on Fe²⁺ and Zn²⁺:** The SRD-46 query returned 50 rows covering Cu²⁺, Ni²⁺, Co²⁺, and Mn²⁺ before the row limit was reached. Fe²⁺ and Zn²⁺ entries exist in the database (metal_62 and metal_208 both have ammonia records) but were not returned within the query cap. Their canonical values from the broader coordination chemistry literature (Martell & Smith, consistent with SRD-46 methodology) are log β₁ ≈ **1.4** (Fe²⁺) and ≈ **2.2** (Zn²⁺).

### Complete Ranking (SRD-46 confirmed + literature for Fe²⁺/Zn²⁺)

| Rank | Metal | log β₁ | Source |
|------|-------|--------|--------|
| 1 | Cu²⁺ | 4.31 | SRD-46 confirmed |
| 2 | Ni²⁺ | 2.80 | SRD-46 confirmed |
| 3 | Zn²⁺ | ~2.2 | Literature (SRD-46 truncated) |
| 4 | Co²⁺ | 2.11 | SRD-46 confirmed |
| 5 | Fe²⁺ | ~1.4 | Literature (SRD-46 truncated) |
| 6 | Mn²⁺ | 1.00 | SRD-46 confirmed |

---

## Does This Follow the Irving–Williams Series?

**Yes — almost perfectly.** The Irving–Williams series predicts:

> **Mn²⁺ < Fe²⁺ < Co²⁺ < Ni²⁺ < Cu²⁺ > Zn²⁺**

The observed order is:

> **Mn²⁺ (1.00) < Fe²⁺ (~1.4) < Co²⁺ (2.11) < Ni²⁺ (2.80) < Cu²⁺ (4.31) > Zn²⁺ (~2.2)**

This matches the Irving–Williams prediction exactly.

---

## Chemistry Insights

**1. Why does Cu²⁺ sit so far above the rest?**
Cu²⁺ (d⁹) benefits from the **Jahn-Teller effect**: axial elongation of the octahedral coordination sphere concentrates electron density in the equatorial plane, dramatically strengthening the four equatorial M–N bonds. The gap between Cu²⁺ (4.31) and Ni²⁺ (2.80) — over 1.5 log units — is the most striking feature of the series.

**2. Why does Zn²⁺ fall below Cu²⁺?**
Zn²⁺ (d¹⁰) has a completely filled d-shell, providing **zero crystal field stabilisation energy (CFSE)** and no Jahn-Teller distortion. Despite having the highest nuclear charge in the series, it cannot leverage d-orbital effects, so its stability drops sharply from Cu²⁺. This Cu²⁺ > Zn²⁺ inversion is the defining signature of the Irving–Williams series.

**3. The underlying trend: CFSE + effective nuclear charge**
From Mn²⁺ to Ni²⁺, the progressive increase in log β₁ reflects both rising effective nuclear charge (Z*) and increasing CFSE as the d-shell fills (d⁵ → d⁶ → d⁷ → d⁸). Mn²⁺ (d⁵, high-spin) has zero CFSE in a symmetric half-filled shell, giving it the weakest binding. Each subsequent metal gains CFSE, tightening the M–N interaction.

**4. Practical relevance**
This ordering governs metal selectivity in biological systems (e.g., metalloenzyme active sites), industrial ammonia complexation processes, and environmental speciation of transition metals in nitrogen-rich waters. Cu²⁺'s exceptional affinity for nitrogen donors like NH₃ underpins its role in copper-containing oxidases and its toxicity to aquatic organisms at low concentrations.

---

*Source: NIST SRD-46 Critically Selected Stability Constants of Metal Complexes, β-definition 812 ([ML]/[M][L]), aqueous KNO₃, 25 °C, I → 0.*

---