# Q5.2.2 — Tool Results (batch 1)

### Step 2: `search_ligands`
**Args:**
```json
{
  "name": "transferrin, lactoferrin, albumin, metallothionein, apotransferrin, HSA, BSA",
  "limit": 20
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 4: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_name_SRD LIKE '%transferrin%' OR c.ligand_name_SRD LIKE '%apotransferrin%' OR c.ligand_name_SRD LIKE '%lactoferrin%' OR c.ligand_name_SRD LIKE '%albumin%' OR c.ligand_name_SRD LIKE '%serum albumin%' OR c.ligand_name_SRD LIKE '%HSA%' OR c.ligand_name_SRD LIKE '%BSA%' OR c.ligand_name_SRD LIKE '%metallothionein%' OR c.ligand_name_SRD LIKE '%ferritin%' OR c.ligand_name_SRD LIKE '%protein%' OR c.ligand_name_SRD LIKE '%polypeptide%')",
  "limit": 20
}
```

[summary]
## search_stability

*(no results)*

---

### Step 5: `search_networks`
**Args:**
```json
{
  "where": "(c.ligand_name LIKE '%transferrin%' OR c.ligand_name LIKE '%apotransferrin%' OR c.ligand_name LIKE '%lactoferrin%' OR c.ligand_name LIKE '%albumin%' OR c.ligand_name LIKE '%serum albumin%' OR c.ligand_name LIKE '%HSA%' OR c.ligand_name LIKE '%BSA%' OR c.ligand_name LIKE '%metallothionein%' OR c.ligand_name LIKE '%ferritin%' OR c.ligand_name LIKE '%protein%' OR c.ligand_name LIKE '%polypeptide%')",
  "limit": 20
}
```

[summary]
## search_networks

*(no results)*

---

### Step 6: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_name_SRD LIKE '%transferrin%' OR lc.ligand_name_SRD LIKE '%apotransferrin%' OR lc.ligand_name_SRD LIKE '%lactoferrin%' OR lc.ligand_name_SRD LIKE '%albumin%' OR lc.ligand_name_SRD LIKE '%serum albumin%' OR lc.ligand_name_SRD LIKE '%HSA%' OR lc.ligand_name_SRD LIKE '%BSA%' OR lc.ligand_name_SRD LIKE '%metallothionein%' OR lc.ligand_name_SRD LIKE '%ferritin%' OR lc.ligand_name_SRD LIKE '%protein%' OR lc.ligand_name_SRD LIKE '%polypeptide%')",
  "limit": 20
}
```

[summary]
## search_pka_ligands

*(no results)*

---

### Step 7: `search_citations`
**Args:**
```json
{
  "where": "(la.citation LIKE '%transferrin%' OR la.citation LIKE '%apotransferrin%' OR la.citation LIKE '%lactoferrin%' OR la.citation LIKE '%albumin%' OR la.citation LIKE '%serum albumin%' OR la.citation LIKE '%HSA%' OR la.citation LIKE '%BSA%' OR la.citation LIKE '%metallothionein%' OR la.citation LIKE '%ferritin%' OR la.citation LIKE '%protein%')",
  "limit": 20
}
```

[summary]
## search_citations — 5 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_94058 | 176 | lit_642 | 43Eaa | J. T. Edsall in "Proteins, Amino Acids and Peptides", E. J. Cohn and J. T. Edsa… |
| vlm_99994 | 100 | lit_1716 | 80OO | T. Ohsaka, N. Oyama, and H. Matsuda, Bull. Chem. Soc. Japan, 1980, 53, 3601 |
| vlm_182810 | 6 | lit_7985 | 72ESM | G. Eisenman, G. Szabo, S. G. A. McLaughlin, and S. M. Ciane, in "Symposium on M… |
| vlm_138105 | 22 | lit_12764 | 83HOO | K. Hayashi, T. Ohsawa, K. Okamoto, J. Hidaka, and H. Einaga, J. Coord. Chem., 1… |
| vlm_115076 | 24 | lit_14729 | 88CCI | R. Cali, V. Cucinotta, G. Impellizzeri, M. C. Mangeri, and E. Rizzarelli, Int. … |

---
