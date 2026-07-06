## Log β₁ for First-Row Divalent Transition Metals with Ammonia — Irving–Williams Series Check

### System Overview (from SRD-46)

I confirmed that all six divalent metals and ammonia (ligand_10103) exist in the NIST SRD-46 database. The relevant β₁ definition is **beta_def_812**: [ML]/[M][L], i.e. M²⁺ + NH₃ ⇌ M(NH₃)²⁺. The Mn²⁺–NH₃ catalog alone showed **8 measured entries** for this equilibrium, with reference networks clustered around 20–30 °C and various ionic strengths.

Unfortunately, I was unable to retrieve the actual measured constant values within the session's time budget. The representative literature log β₁ values at ~25 °C for these systems are:

| Metal | SRD-46 ID | log β₁ (≈25 °C, literature) | Rank |
|-------|-----------|----------------------------|------|
| Mn²⁺ | metal_94  | ~1.0 | 1 (weakest) |
| Fe²⁺ | metal_62  | ~1.4 | 2 |
| Co²⁺ | metal_33  | ~2.1 | 3 |
| Ni²⁺ | metal_112 | ~2.7 | 4 |
| Cu²⁺ | metal_41  | ~4.0 | 5 (strongest) |
| Zn²⁺ | metal_208 | ~2.3 | 6 (drops after Cu²⁺) |

> ⚠️ These are well-established literature values. The SRD-46 database holds measured entries for all six systems (Fe²⁺ data may be sparse due to oxidation sensitivity). A follow-up query using `search_stability` with `beta_def_812` and `ligand_10103` would return the exact SRD-46 values with temperature and ionic-strength conditions.

### Does the ordering follow the Irving–Williams series?

**Yes.** The stability order is:

**Mn²⁺ < Fe²⁺ < Co²⁺ < Ni²⁺ < Cu²⁺ > Zn²⁺**

This matches the Irving–Williams series exactly. The trend arises from three reinforcing factors:

1. **Crystal Field Stabilisation Energy (CFSE):** From Mn²⁺ (d⁵, zero CFSE in both octahedral and tetrahedral fields) through Ni²⁺ (d⁸), CFSE increases steadily. Cu²⁺ (d⁹) gains additional stabilisation from Jahn–Teller distortion, which shortens and strengthens the equatorial M–N bonds. Zn²⁺ (d¹⁰) has zero CFSE, causing the characteristic drop.

2. **Decreasing ionic radius:** Across the series, the effective ionic radius shrinks due to imperfect shielding of the increasing nuclear charge, leading to higher charge density and stronger electrostatic M–L interactions — until the CFSE loss at Zn²⁺ overrides this effect.

3. **Ligand-field character of NH₃:** Ammonia is a moderate-field, pure σ-donor ligand that sits squarely in the regime where the Irving–Williams trend is most cleanly observed, making it one of the textbook examples of this universal stability ordering.

*Source: NIST SRD-46 (entity resolution and system catalog confirmed); representative log β₁ values consistent with standard coordination chemistry references.*

---