Based on my thorough investigation of the SRD-46 database, here is what I found:

---

## Stability Constants in Supercritical CO₂ — SRD-46 Search Results

### 🔍 Finding: No Data Available

After systematically searching the NIST SRD-46 database through multiple approaches:

| Search Method | Result |
|---|---|
| `search_stability` with `solvent_name LIKE '%supercritical%'` | No results |
| `search_stability` with `solvent_name LIKE '%CO2%'` | No results |
| `db_distribution` on `solvent_name` (79,063 rows) | **100% aqueous (H₂O)** |
| `search_networks` for non-standard solvents | Only aqueous systems found |
| Raw SQL on distinct solvent names | Only `H_[2]O` present |

### 📊 Database Solvent Coverage

| Solvent | Records | % of Total |
|---|---|---|
| H₂O (water) | 79,063 | 100% |
| Supercritical CO₂ | 0 | 0% |

---

### 💡 Chemistry Context

**Supercritical CO₂ (scCO₂)** (T > 31.1 °C, P > 73.8 bar) is a non-polar, tunable solvent used in green chemistry and extraction processes. Measuring metal–ligand stability constants in scCO₂ is experimentally challenging because:

1. **Most classical ligands** (amino acids, EDTA, etc.) have very low solubility in non-polar scCO₂ without fluorinated or silicone-based cosolvents.
2. **Fluorinated β-diketones** (e.g., hexafluoroacetylacetone, HFA) and **phosphine oxides** (e.g., TBP, TOPO) are the primary ligands studied in scCO₂ extraction literature — but these measurements are largely in specialized extraction journals, not yet captured in SRD-46.
3. The SRD-46 database is focused on **aqueous solution equilibria**, which is the dominant domain of classical coordination chemistry thermodynamics.

### 📚 Suggested Follow-Up

For scCO₂ stability data, consult:
- **NIST WebBook** for thermophysical properties of CO₂
- Literature on **supercritical fluid extraction (SFE)** of metals with fluorinated ligands (e.g., Laintz, Wai et al., *Anal. Chem.* 1992)
- The **IUPAC Solubility Data Series** for metal complexes in non-aqueous media

> *Source: NIST SRD-46 (Critically Selected Stability Constants of Metal Complexes). All 79,063 stability constant measurements in the database are recorded in aqueous solvent.*

---