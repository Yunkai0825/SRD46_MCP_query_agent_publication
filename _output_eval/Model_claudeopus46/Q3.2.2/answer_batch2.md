## Ni²⁺–Ethylenediamine: Stability Constants vs. Ionic Strength

### Data at 25 °C in KNO₃ (aqueous)

The NIST SRD-46 database provides a clean series of cumulative formation constants (log β) measured at 25 °C across a wide range of ionic strengths in KNO₃:

| I (mol/L) | log β₁ (ML) | log β₂ (ML₂) | log β₃ (ML₃) |
|-----------|-------------|---------------|---------------|
| 0.0       | 7.90        | 14.53         | 19.18         |
| 0.1       | 7.52        | 13.84         | 18.33         |
| 0.5       | 7.35        | 13.54         | 17.86         |
| 1.0       | 7.28        | 13.40         | 17.64         |
| 2.0       | 7.04        | —*            | —*            |
| 3.0       | 6.98        | 13.04         | 17.00         |

*\*The β₂ and β₃ entries at I = 2.0 M appear as negative values (−14.77 and −19.70) in the database, which are almost certainly sign-convention artifacts or data-entry issues; they are excluded from the trend analysis.*

An additional measurement at **37 °C in NaCl (I = 0.15 M)** gives log β₁ = 7.51, log β₂ = 13.86, log β₃ = 18.28 — consistent with the KNO₃ trend at comparable ionic strength.

### Is there a clear trend?

**Yes — all three cumulative stability constants decrease monotonically with increasing ionic strength.** The drop is steepest going from I = 0 → 0.1 M and then levels off gradually at higher I:

| Species | log β at I = 0 | log β at I = 3 M | Total drop |
|---------|----------------|-------------------|------------|
| [Ni(en)]²⁺   | 7.90  | 6.98  | −0.92 |
| [Ni(en)₂]²⁺  | 14.53 | 13.04 | −1.49 |
| [Ni(en)₃]²⁺  | 19.18 | 17.00 | −2.18 |

The magnitude of the decrease scales roughly with the number of ethylenediamine ligands *n* (about 0.7–0.9 log units per en), which is the pattern expected from Debye–Hückel theory.

### Chemistry Insight

At first glance one might expect little ionic-strength dependence because the overall reaction Ni²⁺ + n(en⁰) → [Ni(en)ₙ]²⁺ involves **no net change in charge**. However, the activity coefficients of the individual species — especially the highly charged Ni²⁺ free ion — are still sensitive to the ionic medium. Higher salt concentrations preferentially stabilise the free ions relative to the complex, lowering the apparent formation constant. The effect is real but modest (~1 log unit over 0–3 M for β₁), which contrasts with metal–anion systems where ionic-strength shifts can be several log units. The smooth, monotonic decrease also confirms that KNO₃ does not participate in significant competing equilibria with Ni²⁺ or ethylenediamine.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes).*

---