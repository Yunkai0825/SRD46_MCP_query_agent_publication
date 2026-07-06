## Results: Stability Constants in Supercritical CO₂

After an exhaustive search of the NIST SRD-46 database using multiple query strategies — including direct `solvent_name` filtering for all known supercritical CO₂ synonyms (`supercritical`, `scCO2`, `CO2`, `carbon dioxide`, `compressed`, `dense`), citation text searches, and schema inspection — **no stability constants measured in supercritical CO₂ as solvent are present in SRD-46**.

### What the Database Contains

| Solvent | Record Count |
|---------|-------------|
| H₂O (water) | 79,063 |
| All other solvents | 0 (not represented) |

The `ligandmetal_stability_measured` table contains only a single distinct solvent: **water**. The SRD-46 database is fundamentally a **aqueous-phase thermodynamic database** — all 79,063 stability constant measurements are for metal–ligand complexation in water.

### Why This Makes Chemical Sense

Supercritical CO₂ (critical point: 304.1 K, 73.8 bar) is a non-polar solvent with very low dielectric constant (ε ≈ 1.5), making it a poor medium for ionic metal–ligand equilibria. The handful of literature studies on metal extraction into scCO₂ (e.g., with fluorinated β-diketone ligands like TTA or HFA) typically report **distribution ratios** or **extraction efficiencies**, not thermodynamic stability constants in the IUPAC sense — and these have not been incorporated into SRD-46.

### Recommendation

If you are researching metal complexation in scCO₂, the relevant literature is found in journals such as *J. Supercritical Fluids* and *Analytical Chemistry* (e.g., work by Laintz, Wai, and Darr on lanthanide/actinide extraction with fluorinated ligands). SRD-46 is not the appropriate resource for non-aqueous or supercritical-fluid equilibria.

> **Source:** NIST SRD-46 (Critically Selected Stability Constants of Metal Complexes Database), queried exhaustively for supercritical CO₂ solvent entries — none found.

---