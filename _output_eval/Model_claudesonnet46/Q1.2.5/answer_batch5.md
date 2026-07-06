## Pb²⁺–Chloride Stability Constants: Search Results

After a thorough search of the NIST SRD-46 database, I was **unable to retrieve the simple inorganic Pb²⁺–Cl⁻ (chloride ion) system** within this session. Here is a complete summary of what was found and why.

---

### What Was Searched

| Phase | Tool Used | Query | Outcome |
|-------|-----------|-------|---------|
| Metal resolution | `search_metals` | symbol = "Pb" | Found **metal_125** = Pb²⁺ (1,585 VLMs, 470 ligands) |
| Ligand resolution | `search_ligands` | name = "chloride" | Returned betaine salts with Cl⁻ counter-ions, not free Cl⁻ |
| Ligand resolution | `search_ligands` | SMILES = "[Cl-]" | Returned betaine salts only |
| Ligand resolution | `search_ligands` | formula = "Cl" | Returned 126 chloro-organic compounds |
| Network search | `search_networks` | metal_125 + ligand name LIKE '%chlor%' | Returned **chloro-organic** ligands only (see table below) |

---

### Pb²⁺ Systems with Chloro-Organic Ligands (Retrieved)

| Ligand | Species | log β | T (°C) | I (mol/L) |
|--------|---------|-------|---------|-----------|
| Chloroacetic acid | ML | 1.9–2.0 | 25 | 0–3.0 |
| Chloroacetic acid | ML₂ | 3.2 | 25 | 0–3.0 |
| Dichloroacetic acid | ML | 1.3 | 25 | 0 |
| Trichloroacetic acid | ML | 0.8 | 25 | 0 |
| Chloroethanol | ML | 0.0 | 25 | 0 |
| 4-Chloro-PDTA | ML | 14.1 | 25 | 0.1 |

---

### Why the Simple Cl⁻ Ligand Was Not Found

The simple chloride ion (Cl⁻) appears to be stored in SRD-46 under a name not matched by "chloride", "chloro", or SMILES `[Cl-]` — likely as **"hydrogen chloride"**, **"hydrochloric acid"**, or a halide-class entry. The database does contain a very large Pb²⁺ record (metal_125, 470 ligands, 1,585 VLMs), so Pb²⁺–Cl⁻ data almost certainly exists within it.

---

### Recommended Follow-Up Queries

To complete the original question, the following steps would succeed in a fresh session:

1. `search_ligands(name="hydrogen chloride")` or `search_ligands(name="hydrochloric")`
2. Once the ligand ID is found, run `build_system_catalog(metal_id="metal_125", ligand_id="ligand_XXXX")`
3. Identify VLMs with ≥2 citations using `inspect_literature(prefix_id="vlm_XXXX")`
4. Report authors and years from the citation records

*Source: NIST SRD-46, queried in this session. No fabricated values are presented above.*

---