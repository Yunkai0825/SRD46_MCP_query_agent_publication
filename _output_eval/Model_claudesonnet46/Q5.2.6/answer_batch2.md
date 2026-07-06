## Search Results: Stability Constants in Supercritical CO₂

After an exhaustive multi-angle search of the NIST SRD-46 database, **no stability constants measured in supercritical CO₂ as solvent were found**.

Here is a summary of every search path attempted:

| Search Path | What Was Checked | Result |
|---|---|---|
| `search_stability` solvent field | `solvent_name` LIKE `%supercritical%`, `%scCO2%`, `%CO2%`, `%carbon dioxide%` | ❌ No matches |
| `search_networks` | High-temperature networks (T > 304 K) with equilibrium constants | ❌ No matches |
| `search_citations` | Citation text containing `supercritical`, `scCO2`, `sc-CO2`, `CO2` | ❌ No matches |
| Direct SQL on `ligandmetal_stability_measured` | `notes` and `electrolyte_composition` fields | ❌ No matches (only 1 row mentioning CO₂ gas evolution in aqueous solution) |
| Literature database | `citation` and `comment` fields for supercritical keywords | ❌ No matches |
| pKa table | `solvent_name` field | ❌ No matches |
| Solvent distribution | All distinct `solvent_name` values in 79,063 stability records | Only `H₂O` present |

---

### Why This Gap Exists

The SRD-46 (NIST Critically Selected Stability Constants of Metal Complexes) database is **exclusively aqueous-phase data** — all 79,063 stability measurements use water (`H₂O`) as the solvent. This is by design: the database was compiled from the classical coordination chemistry literature, which overwhelmingly reports constants in aqueous media.

Supercritical CO₂ (scCO₂, T > 304.1 K, P > 7.38 MPa) is a niche solvent for metal complexation, primarily studied in the context of:
- **Supercritical fluid extraction (SFE)** of metals using fluorinated β-diketonates (e.g., TTA, HFA, FOD)
- **Nuclear waste processing** (uranium, thorium extraction)
- **Green chemistry** separations

Stability constants in scCO₂ are reported in the primary literature (e.g., work by Laintz, Wai, and Dehghani groups) but have **not been incorporated into SRD-46** as of this database version.

> **Source:** NIST SRD-46 database (all searches returned null results for non-aqueous solvents).

---