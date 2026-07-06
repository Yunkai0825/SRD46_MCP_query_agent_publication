# Q5.2.2 — Tool Results (batch 2)

### Step 2: `search_ligands`
**Args:**
```json
{
  "name": "transferrin",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "albumin",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "metallothionein",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_name_SRD LIKE '%transferrin%' OR c.ligand_name_SRD LIKE '%albumin%' OR c.ligand_name_SRD LIKE '%metallothionein%')",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 7: `search_networks`
**Args:**
```json
{
  "where": "(c.ligand_name_SRD LIKE '%transferrin%' OR c.ligand_name_SRD LIKE '%albumin%' OR c.ligand_name_SRD LIKE '%metallothionein%')",
  "limit": 50
}
```

[TOOL ERROR] search_networks: Error executing tool search_networks: no such column: c.ligand_name_SRD

---

### Step 8: `search_citations`
**Args:**
```json
{
  "where": "(la.citation LIKE '%transferrin%' OR la.citation LIKE '%albumin%' OR la.citation LIKE '%metallothionein%')",
  "limit": 200
}
```

[summary]
## search_citations

*(no results)*

---

### Step 9: `search_metals`
**Args:**
```json
{
  "symbol": "Fe",
  "limit": 10
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 10: `search_metals`
**Args:**
```json
{
  "symbol": "Al",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_5 | Al^[3+] | Al | 3 | ✓ | [Al+3] | InChI=1S/Al/q+3 | beta_totN_108 | ligand_totN_187 | vlm_totN_792 |

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD LIKE 'Fe%' AND (c.ligand_name_SRD LIKE '%histidine%' OR c.ligand_name_SRD LIKE '%imidazole%'))",
  "limit": 500
}
```

[summary]
## search_stability — 29 row(s)

### logK — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6996 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)NO | 8 | 8 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7862 | 2-(2-Pyridyl)imidazole | L | c1ccc(-c2ncc[nH]2)nc1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7863 | 4-(2-Pyridyl)imidazole | L | c1ccc(-c2c[nH]cn2)nc1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 3 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |

### ΔH — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 3 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7862 | 2-(2-Pyridyl)imidazole | L | c1ccc(-c2ncc[nH]2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7863 | 4-(2-Pyridyl)imidazole | L | c1ccc(-c2c[nH]cn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔS — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 3 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7862 | 2-(2-Pyridyl)imidazole | L | c1ccc(-c2ncc[nH]2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7863 | 4-(2-Pyridyl)imidazole | L | c1ccc(-c2c[nH]cn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD LIKE 'Fe%' AND (c.ligand_name_SRD LIKE '%cysteine%' OR c.ligand_name_SRD LIKE '%cysteinate%'))",
  "limit": 500
}
```

[summary]
## search_stability — 1 row(s)

### `Fe^[2+]` + L-2-Amino-3-mercaptopropanoic acid (Cysteine) — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_5856
ligand_HxL_def: H2L | ligand_SMILES: N[C@@H](CS)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_97413 | ref_eq_map_1005 | beta_def_812 | logK | -6.6 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (10.3, L, +inf) |

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD LIKE 'Fe%' AND (c.ligand_name_SRD LIKE '%glutathione%' OR c.ligand_name_SRD LIKE '%GSH%'))",
  "limit": 500
}
```

[summary]
## search_stability — 195 row(s)

### logK — 41 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 18 | 4 | 25~37 | 0.1~3 | *** | 5 |
| metal_208 | Zn^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 13 | 7 | 25~37 | 0.15~3 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_6411 | L-Glutamylglycine | H2L | N[C@@H](CCC(=O)O)C(=O)NCC(=O)O | 8 | 4 | 25 | 0.1~0.5 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 8 | 8 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 7 | 7 | 25 | 3 | *** | 1 |
| metal_68 | H^[+] | ligand_6411 | L-Glutamylglycine | H2L | N[C@@H](CCC(=O)O)C(=O)NCC(=O)O | 6 | 3 | 25 | 0.1~0.5 | *** | 2 |
| metal_33 | Co^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 6 | 3 | 25 | 0.1~0.5 | *** | 2 |
| metal_125 | Pb^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 6 | 6 | 25 | 3 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6502 | L-5-Glutamyl-L-7-lysine | H2L | NC(CCCCNC(=O)CCC(N)C(=O)O)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6502 | L-5-Glutamyl-L-7-lysine | H2L | NC(CCCCNC(=O)CCC(N)C(=O)O)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6502 | L-5-Glutamyl-L-7-lysine | H2L | NC(CCCCNC(=O)CCC(N)C(=O)O)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6553 | L-Leucyl-L-leucylglycine | HL | CC(C)C[C@H](NC(=O)[C@@H](N)CC(C)C)C(=O)NCC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6554 | L-Leucyl-D-leucylglycine | HL | CC(C)C[C@H](N)C(=O)N[C@H](CC(C)C)C(=O)NCC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 4 | 4 | 37 | 0.15 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 4 | 4 | 37 | 0.15 | *** | 1 |
| metal_74 | In^[3+] | ligand_8784 | DL-(2,3-Dimercaptopropionyl… | H3L | O=C(O)CNC(=O)C(S)CS | 4 | 4 | 20 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6416 | L-Cysteinylglycine | H2L | N[C@@H](CS)C(=O)NCC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6545 | Glycyl-L-leucylglycine | HL | CC(C)C[C@H](NC(=O)CN)C(=O)NCC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 3 | 3 | 37 | 0.15 | *** | 1 |
| metal_68 | H^[+] | ligand_8784 | DL-(2,3-Dimercaptopropionyl… | H3L | O=C(O)CNC(=O)C(S)CS | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_8784 | DL-(2,3-Dimercaptopropionyl… | H3L | O=C(O)CNC(=O)C(S)CS | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6416 | L-Cysteinylglycine | H2L | N[C@@H](CS)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6416 | L-Cysteinylglycine | H2L | N[C@@H](CS)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6416 | L-Cysteinylglycine | H2L | N[C@@H](CS)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_6416 | L-Cysteinylglycine | H2L | N[C@@H](CS)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6545 | Glycyl-L-leucylglycine | HL | CC(C)C[C@H](NC(=O)CN)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6553 | L-Leucyl-L-leucylglycine | HL | CC(C)C[C@H](NC(=O)[C@@H](N)CC(C)C)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6554 | L-Leucyl-D-leucylglycine | HL | CC(C)C[C@H](N)C(=O)N[C@H](CC(C)C)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6574 | Glycyl-DL-serylglycine | HL | NCC(=O)NC(CO)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_185 | Th^[4+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 2 | 2 | 25 | 1 | *** | 1 |
| metal_42 | Cu^[+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_87 | Me_[3]Pb^[+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_68 | H^[+] | ligand_6657 | L-5-Glutamyl-3-(D-2-amino-2… | H3L | CC(C)(SSCC(NC(=O)CCC(N)C(=O)O)C(=O)NCC(=O)O)C(N)C(=O)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_68 | H^[+] | ligand_6545 | Glycyl-L-leucylglycine | HL | CC(C)C[C@H](NC(=O)CN)C(=O)NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_195 | UO_[2]^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_68 | H^[+] | ligand_6593 | L-5-Glutamyl-(S-methyl-L-cy… | H2L | CSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_6593 | L-5-Glutamyl-(S-methyl-L-cy… | H2L | CSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6593 | L-5-Glutamyl-(S-methyl-L-cy… | H2L | CSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6593 | L-5-Glutamyl-(S-methyl-L-cy… | H2L | CSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6593 | L-5-Glutamyl-(S-methyl-L-cy… | H2L | CSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 6 | 4 | 25 | 1~3 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6411 | L-Glutamylglycine | H2L | N[C@@H](CCC(=O)O)C(=O)NCC(=O)O | 4 | 4 | 25 | 0.5 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 4 | 4 | 25 | 3 | *** | 0 |
| metal_68 | H^[+] | ligand_6411 | L-Glutamylglycine | H2L | N[C@@H](CCC(=O)O)C(=O)NCC(=O)O | 3 | 3 | 25 | 0.5 | *** | 0 |
| metal_185 | Th^[4+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_195 | UO_[2]^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 1 | 1 | 25 | 1 | *** | 0 |

### ΔS — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 6 | 4 | 25 | 1~3 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6411 | L-Glutamylglycine | H2L | N[C@@H](CCC(=O)O)C(=O)NCC(=O)O | 4 | 4 | 25 | 0.5 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 4 | 4 | 25 | 3 | *** | 0 |
| metal_68 | H^[+] | ligand_6411 | L-Glutamylglycine | H2L | N[C@@H](CCC(=O)O)C(=O)NCC(=O)O | 3 | 3 | 25 | 0.5 | *** | 0 |
| metal_185 | Th^[4+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_195 | UO_[2]^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 1 | 1 | 25 | 1 | *** | 0 |

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD LIKE 'Fe%' AND (c.ligand_name_SRD LIKE '%Gly-His%' OR c.ligand_name_SRD LIKE '%Gly-Gly-His%' OR c.ligand_name_SRD LIKE '%glycylhistidine%' OR c.ligand_name_SRD LIKE '%glycylglycylhistidine%'))",
  "limit": 500
}
```

[summary]
## search_stability

*(no results)*

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD LIKE 'Al%' AND (c.ligand_name_SRD LIKE '%histidine%' OR c.ligand_name_SRD LIKE '%imidazole%'))",
  "limit": 500
}
```

[summary]
## search_stability — 2 row(s)

### `Al^[3+]` + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine) — 2 measurement(s)
metal_id: metal_5 | ligand_id: ligand_5898
ligand_HxL_def: HL | ligand_SMILES: N[C@@H](Cc1c[nH]cn1)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_98951 | ref_eq_map_1366 | beta_def_960 | logK | 8.11 | 25 | 0.5 | `[M] + [L] + [H2O] <=> [M(OH)(HL)]` | *** | [L] | (9.1, L, +inf) |
| vlm_98952 | ref_eq_map_1366 | beta_def_961 | logK | 4.36 | 25 | 0.5 | `[M(OH)L] + [H] <=> [M(OH)(HL)]` | *** |  |  |

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD LIKE 'Al%' AND (c.ligand_name_SRD LIKE '%cysteine%' OR c.ligand_name_SRD LIKE '%cysteinate%'))",
  "limit": 500
}
```

[summary]
## search_stability — 200 row(s)

### logK — 43 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 21 | 3 | 25~37 | 0~3 | *** | 7 |
| metal_68 | H^[+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 14 | 2 | 10~40 | 0~5 | *** | 7 |
| metal_41 | Cu^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 11 | 3 | 25~37 | 0.1~2 | *** | 5 |
| metal_25 | Ca^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 6 | 2 | 25~37 | 0~0.15 | *** | 3 |
| metal_41 | Cu^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 5 | 3 | 25 | 0.1~5 | *** | 2 |
| metal_139 | Pr^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 5 | 3 | 25~30 | 0.1 | *** | 2 |
| metal_110 | Nd^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 5 | 3 | 25~30 | 0.1 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 5 | 3 | 25 | 0.1~0.5 | *** | 2 |
| metal_6 | Am^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 4 | 2 | 25 | 0.1~0.7 | *** | 2 |
| metal_195 | UO_[2]^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 4 | 3 | 25 | 0.1~1 | *** | 3 |
| metal_33 | Co^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 4 | 2 | 25~30 | 0.1 | *** | 2 |
| metal_37 | Cr^[3+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5778 | DL-2-Amino-3-chloropropanoi… | HL | N[C@@H](CCl)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_5778 | DL-2-Amino-3-chloropropanoi… | HL | N[C@@H](CCl)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_27 | Ce^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 3 | 3 | 30 | 0.1 | *** | 1 |
| metal_36 | Cr^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 3 | 3 | 25 | 1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 3 | *** | 1 |
| metal_68 | H^[+] | ligand_5778 | DL-2-Amino-3-chloropropanoi… | HL | N[C@@H](CCl)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_5778 | DL-2-Amino-3-chloropropanoi… | HL | N[C@@H](CCl)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_106 | Na^[+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_79 | La^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_192 | Tm^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_19 | Be^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_92 | Mg^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_177 | Sr^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_153 | Ra^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_185 | Th^[4+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |

### ΔH — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 9 | 3 | 25 | 0~1 | *** | 0 |
| metal_68 | H^[+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 4 | 2 | 10~40 | 0 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 4 | 2 | 25 | 0.1~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_195 | UO_[2]^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_185 | Th^[4+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 25 | 1 | *** | 0 |

### ΔS — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 9 | 3 | 25 | 0~1 | *** | 0 |
| metal_68 | H^[+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_195 | UO_[2]^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_185 | Th^[4+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 25 | 1 | *** | 0 |

---

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD LIKE 'Al%' AND (c.ligand_name_SRD LIKE '%glutathione%' OR c.ligand_name_SRD LIKE '%GSH%'))",
  "limit": 500
}
```

[summary]
## search_stability — 195 row(s)

### logK — 41 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 18 | 4 | 25~37 | 0.1~3 | *** | 5 |
| metal_208 | Zn^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 13 | 7 | 25~37 | 0.15~3 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_6411 | L-Glutamylglycine | H2L | N[C@@H](CCC(=O)O)C(=O)NCC(=O)O | 8 | 4 | 25 | 0.1~0.5 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 8 | 8 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 7 | 7 | 25 | 3 | *** | 1 |
| metal_68 | H^[+] | ligand_6411 | L-Glutamylglycine | H2L | N[C@@H](CCC(=O)O)C(=O)NCC(=O)O | 6 | 3 | 25 | 0.1~0.5 | *** | 2 |
| metal_33 | Co^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 6 | 3 | 25 | 0.1~0.5 | *** | 2 |
| metal_125 | Pb^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 6 | 6 | 25 | 3 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6502 | L-5-Glutamyl-L-7-lysine | H2L | NC(CCCCNC(=O)CCC(N)C(=O)O)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6502 | L-5-Glutamyl-L-7-lysine | H2L | NC(CCCCNC(=O)CCC(N)C(=O)O)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6502 | L-5-Glutamyl-L-7-lysine | H2L | NC(CCCCNC(=O)CCC(N)C(=O)O)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6553 | L-Leucyl-L-leucylglycine | HL | CC(C)C[C@H](NC(=O)[C@@H](N)CC(C)C)C(=O)NCC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6554 | L-Leucyl-D-leucylglycine | HL | CC(C)C[C@H](N)C(=O)N[C@H](CC(C)C)C(=O)NCC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 4 | 4 | 37 | 0.15 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 4 | 4 | 37 | 0.15 | *** | 1 |
| metal_74 | In^[3+] | ligand_8784 | DL-(2,3-Dimercaptopropionyl… | H3L | O=C(O)CNC(=O)C(S)CS | 4 | 4 | 20 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6416 | L-Cysteinylglycine | H2L | N[C@@H](CS)C(=O)NCC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6545 | Glycyl-L-leucylglycine | HL | CC(C)C[C@H](NC(=O)CN)C(=O)NCC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 3 | 3 | 37 | 0.15 | *** | 1 |
| metal_68 | H^[+] | ligand_8784 | DL-(2,3-Dimercaptopropionyl… | H3L | O=C(O)CNC(=O)C(S)CS | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_8784 | DL-(2,3-Dimercaptopropionyl… | H3L | O=C(O)CNC(=O)C(S)CS | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6416 | L-Cysteinylglycine | H2L | N[C@@H](CS)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6416 | L-Cysteinylglycine | H2L | N[C@@H](CS)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6416 | L-Cysteinylglycine | H2L | N[C@@H](CS)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_6416 | L-Cysteinylglycine | H2L | N[C@@H](CS)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6545 | Glycyl-L-leucylglycine | HL | CC(C)C[C@H](NC(=O)CN)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6553 | L-Leucyl-L-leucylglycine | HL | CC(C)C[C@H](NC(=O)[C@@H](N)CC(C)C)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6554 | L-Leucyl-D-leucylglycine | HL | CC(C)C[C@H](N)C(=O)N[C@H](CC(C)C)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6574 | Glycyl-DL-serylglycine | HL | NCC(=O)NC(CO)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_185 | Th^[4+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 2 | 2 | 25 | 1 | *** | 1 |
| metal_42 | Cu^[+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_87 | Me_[3]Pb^[+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_68 | H^[+] | ligand_6657 | L-5-Glutamyl-3-(D-2-amino-2… | H3L | CC(C)(SSCC(NC(=O)CCC(N)C(=O)O)C(=O)NCC(=O)O)C(N)C(=O)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_68 | H^[+] | ligand_6545 | Glycyl-L-leucylglycine | HL | CC(C)C[C@H](NC(=O)CN)C(=O)NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_195 | UO_[2]^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_68 | H^[+] | ligand_6593 | L-5-Glutamyl-(S-methyl-L-cy… | H2L | CSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_6593 | L-5-Glutamyl-(S-methyl-L-cy… | H2L | CSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6593 | L-5-Glutamyl-(S-methyl-L-cy… | H2L | CSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6593 | L-5-Glutamyl-(S-methyl-L-cy… | H2L | CSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6593 | L-5-Glutamyl-(S-methyl-L-cy… | H2L | CSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 6 | 4 | 25 | 1~3 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6411 | L-Glutamylglycine | H2L | N[C@@H](CCC(=O)O)C(=O)NCC(=O)O | 4 | 4 | 25 | 0.5 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 4 | 4 | 25 | 3 | *** | 0 |
| metal_68 | H^[+] | ligand_6411 | L-Glutamylglycine | H2L | N[C@@H](CCC(=O)O)C(=O)NCC(=O)O | 3 | 3 | 25 | 0.5 | *** | 0 |
| metal_185 | Th^[4+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_195 | UO_[2]^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 1 | 1 | 25 | 1 | *** | 0 |

### ΔS — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 6 | 4 | 25 | 1~3 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6411 | L-Glutamylglycine | H2L | N[C@@H](CCC(=O)O)C(=O)NCC(=O)O | 4 | 4 | 25 | 0.5 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 4 | 4 | 25 | 3 | *** | 0 |
| metal_68 | H^[+] | ligand_6411 | L-Glutamylglycine | H2L | N[C@@H](CCC(=O)O)C(=O)NCC(=O)O | 3 | 3 | 25 | 0.5 | *** | 0 |
| metal_185 | Th^[4+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_195 | UO_[2]^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 1 | 1 | 25 | 1 | *** | 0 |

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD LIKE 'Al%' AND (c.ligand_name_SRD LIKE '%Gly-His%' OR c.ligand_name_SRD LIKE '%Gly-Gly-His%' OR c.ligand_name_SRD LIKE '%glycylhistidine%' OR c.ligand_name_SRD LIKE '%glycylglycylhistidine%'))",
  "limit": 500
}
```

[summary]
## search_stability

*(no results)*

---

### Step 19: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_name_SRD LIKE '%histidine%' OR lc.ligand_name_SRD LIKE '%imidazole%')",
  "order_by": "p.pKa ASC",
  "limit": 100
}
```

[summary]
## search_pka_values — 100 row(s)

### pKa -14.5–-14.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_133793 | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | -14.5 | 25 | 0 | H-1L→L | M_tot_15 | M_tot_1 |

### pKa -13.0–-12.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_134277 | ligand_7814 | Benzo-1,3-diazole (Benzimidazole) | L | c1ccc2[nH]cnc2c1 | -12.8 | 25 | 0 | H-1L→L | M_tot_8 | M_tot_1 |

### pKa -12.0–-11.5 (3 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_97676 | ligand_5860 | DL-2-Amino-3-(2-mercaptoimidazo-4-… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | -11.77 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_9 |
| vlm_134481 | ligand_7837 | 4-(2-Aminoethyl)-2-mercaptoimidazo… | HL | NCCc1c[nH]c(S)n1 | -11.62 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_1 |
| vlm_134467 | ligand_7836 | N-Methyl-2-mercaptoimidazole | HL | Cn1ccnc1S | -11.58 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_1 |

### pKa -11.5–-11.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_134456 | ligand_7835 | 2-Mercaptoimidazole | HL | Sc1ncc[nH]1 | -11.21 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_1 |

### pKa -9.5–-9.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_115947 | ligand_6528 | D-Prolyl-L-histidine | HL | O=C(O)[C@H](Cc1cnc[nH]1)NC(=O)[C@H]1CCCN1 | -9.16 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_2 |

### pKa -9.0–-8.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_115940 | ligand_6527 | L-Prolyl-L-histidine | HL | O=C(O)[C@H](Cc1cnc[nH]1)NC(=O)[C@@H]1CCCN1 | -8.82 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_2 |
| vlm_134222 | ligand_7806 | 2-Ethyl-4-methylimidazole | L | CCc1nc(C)c[nH]1 | -8.68 | 25 | 0.5 | L→HL | M_tot_1 | M_tot_5 |

### pKa -7.0–-6.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_115941 | ligand_6527 | L-Prolyl-L-histidine | HL | O=C(O)[C@H](Cc1cnc[nH]1)NC(=O)[C@@H]1CCCN1 | -6.84 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |
| vlm_115948 | ligand_6528 | D-Prolyl-L-histidine | HL | O=C(O)[C@H](Cc1cnc[nH]1)NC(=O)[C@H]1CCCN1 | -6.77 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |

### pKa -3.0–-2.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_114909 | ligand_6434 | L-Alanyl-L-histidine | HL | C[C@H](N)C(=O)N[C@@H](CC1C=NC=N1)C(=O)O | -2.68 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |

### pKa -2.0–-1.5 (5 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_99015 | ligand_5901 | L-4-(2-Amino-3-carboxypropyl)-1,3-… | HL | Cn1c[n+](C)cc1C[C@H](N)C(=O)O | -1.98 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |
| vlm_98988 | ligand_5899 | L-2-Amino-3-(N(1)-methyl-4-imidazo… | HL | Cn1cnc(C[C@H](N)C(=O)O)c1 | -1.72 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_98740 | ligand_5898 | L-2-Amino-3-(4-imidazolyl)propanoi… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | -1.7 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_3 |
| vlm_99002 | ligand_5900 | L-2-Amino-3-(N(3)-methyl-4-imidazo… | HL | Cn1cncc1C[C@H](N)C(=O)O | -1.65 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_99079 | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-imidazol… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | -1.55 | 25 | 0.5 | H3L→H4L | M_tot_1 | M_tot_1 |

### pKa -1.5–-1.0 (5 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_99055 | ligand_5905 | L-2-Amino-3-(5-iodo-4-imidazolyl)p… | HL | N[C@@H](Cc1nc[nH]c1I)C(=O)O | -1.47 | 25 | 0.5 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_100104 | ligand_5960 | L-2-(Methylamino)-3-(4-imidazolyl)… | HL | CNC(Cc1cnc[nH]1)C(=O)O | -1.4 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_100121 | ligand_5961 | L-2-(Benzylamino)-3-(4-imidazolyl)… | HL | O=C(O)C(Cc1cnc[nH]1)NCc1ccccc1 | -1.3 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_101725 | ligand_6027 | L-2-(Dimethylamino)-3-(4-imidazoly… | HL | CN(C)C(Cc1cnc[nH]1)C(=O)O | -1.1 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_99024 | ligand_5902 | L-1-Carboxy-2-(4-imidazolyl)ethyl(… | HL | C[NH+](C)C(Cc1cnc[nH]1)C(=O)O | -1.03 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |

### pKa -1.0–-0.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_99030 | ligand_5903 | L-1-Carboxy-2-(4-imidazolyl)ethyl(… | HL | C[N+](C)(C)C(Cc1c[nH]cn1)C(=O)O | -0.98 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |

### pKa 1.5–2.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_99035 | ligand_5904 | L-2-Amino-3-(N(3)-benzyl-4-imidazo… | HL | NC(Cc1cncn1Cc1ccccc1)C(=O)O | 1.94 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |

### pKa 2.0–2.5 (4 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_100139 | ligand_5962 | L-2-(Benzylamino)-3-(3-benzyl-5-im… | HL | O=C(O)C(Cc1cn(Cc2ccccc2)cn1)NCc1ccccc1 | 2 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_115820 | ligand_6515 | D-Histidyl-L-histidine | HL | N[C@H](Cc1c[nH]cn1)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O | 2.18 | 25 | 0.1 | H3L→H4L | M_tot_1 | M_tot_1 |
| vlm_115579 | ligand_6492 | L-Tyrosyl-D-histidine | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)N[C@H](Cc1cnc[nH]1)C(=O)O | 2.35 | 25 | 0.1 | H3L→H4L | M_tot_1 | M_tot_1 |
| vlm_115283 | ligand_6463 | L-Leucyl-L-histidine | HL | CC(C)C[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O | 2.4 | 37 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |

### pKa 2.5–3.0 (20 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_114278 | ligand_6401 | Glycyl-L-histidine | HL | NCC(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O | 2.52 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_114690 | ligand_6422 | beta-Alanyl-L-histidine (L-Carnosi… | HL | NCCC(=O)N[C@@H](CC1C=NC=N1)C(=O)O | 2.54 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_117147 | ligand_6651 | Glycyl-L-histidylglycyl-L-histidine | *** | *** | 2.57 | 25 | 0.1 | H3L→H4L | M_tot_1 | M_tot_1 |
| vlm_117154 | ligand_6652 | L-Alanylglycylglycyl-L-(N(Im)-benz… | *** | *** | 2.57 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_115805 | ligand_6514 | L-Histidyl-L-histidine | HL | N[C@@H](Cc1c[nH]cn1)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O | 2.6 | 25 | 0.1 | H3L→H4L | M_tot_1 | M_tot_1 |

**Band stats (all 20 entries):**

| stat | value |
|------|-------|
| entries | 20 |
| unique ligands | 20 |
| pKa range | 2.52 – 2.98 |
| T°C range | 22 – 25 |
| I(M) range | 0.1 – 0.5 |
| HxL forms | HL(14), None(5), H2L(1) |
| functional groups | carboxyl(15), amide(14), aromatic_ring(12), primary_amine(9), imine(3), ester(1), halide(1), hydroxyl(1), phenol(1), secondary_amine(1), thioether(1) |

### pKa 3.0–3.5 (7 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_116468 | ligand_6578 | L-Aspartyl-L-alanyl-L-histidine me… | HL | CNC(=O)[C@H](Cc1cnc[nH]1)NC(=O)[C@H](C)NC(=O)[C@@H](N)CC(=O)O | 3 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_115942 | ligand_6527 | L-Prolyl-L-histidine | HL | O=C(O)[C@H](Cc1cnc[nH]1)NC(=O)[C@@H]1CCCN1 | 3.02 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_100257 | ligand_5973 | N-Acetylglycylglycylglycyl-L-histi… | HL | CC(=O)NCC(=O)NCC(=O)NCC(=O)N[C@@H](CC1C=NC=N1)C(=O)O | 3.04 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |
| vlm_115794 | ligand_6513 | L-Picolyl-L-histidine | HL | O=C(N[C@@H](Cc1cnc[nH]1)C(=O)O)c1ccccn1 | 3.05 | 22 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |
| vlm_115834 | ligand_6516 | N-(Mercaptoacetyl)-L-histidine | H2L | O=C(CS)N[C@@H](Cc1cnc[nH]1)C(=O)O | 3.43 | 20 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |

**Band stats (all 7 entries):**

| stat | value |
|------|-------|
| entries | 7 |
| unique ligands | 7 |
| pKa range | 3.00 – 3.48 |
| T°C range | 20 – 25 |
| I(M) range | 0.1 – 0.1 |
| HxL forms | HL(4), H2L(3) |
| functional groups | amide(7), carboxyl(7), aromatic_ring(6), thiol(3), imine(1), primary_amine(1), pyridine(1), secondary_amine(1) |

### pKa 4.0–4.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_134836 | ligand_7861 | Pyridino[2,3-d]-1,3-diazole (4-Aza… | L | c1cnc2nc[nH]c2c1 | 4.1 | 25 | 0.5 | L→HL | M_tot_1 | M_tot_7 |
| vlm_99054 | ligand_5905 | L-2-Amino-3-(5-iodo-4-imidazolyl)p… | HL | N[C@@H](Cc1nc[nH]c1I)C(=O)O | 4.21 | 25 | 0.5 | HL→H2L | M_tot_1 | M_tot_1 |

### pKa 4.5–5.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_134570 | ligand_7848 | 4-(Aminomethyl)imidazole | L | NCc1c[nH]cn1 | 4.62 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |

### pKa 5.0–5.5 (7 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_134766 | ligand_7853 | L-Histidine methyl ester | L | COC(=O)[C@@H](N)Cc1c[nH]cn1 | 5.27 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |
| vlm_134377 | ligand_7823 | 2-(Hydroxymethyl)benzimidazole | L | OCc1nc2ccccc2[nH]1 | 5.28 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_1 |
| vlm_115818 | ligand_6515 | D-Histidyl-L-histidine | HL | N[C@H](Cc1c[nH]cn1)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O | 5.32 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_121740 | ligand_6996 | L-2-Amino-3-(4-imidazolyl)propanoh… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)NO | 5.34 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_2 |
| vlm_134379 | ligand_7824 | 1-Methyl-2-(hydroxymethyl)benzimid… | L | Cn1c(CO)nc2ccccc21 | 5.43 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_1 |

**Band stats (all 7 entries):**

| stat | value |
|------|-------|
| entries | 7 |
| unique ligands | 7 |
| pKa range | 5.27 – 5.49 |
| T°C range | 25 – 25 |
| I(M) range | 0.1 – 0.1 |
| HxL forms | L(5), HL(2) |
| functional groups | aromatic_ring(7), hydroxyl(3), primary_amine(3), amide(2), pyridine(2), carboxyl(1), ester(1) |

### pKa 5.5–6.0 (12 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_100138 | ligand_5962 | L-2-(Benzylamino)-3-(3-benzyl-5-im… | HL | O=C(O)C(Cc1cn(Cc2ccccc2)cn1)NCc1ccccc1 | 5.5 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |
| vlm_99034 | ligand_5904 | L-2-Amino-3-(N(3)-benzyl-4-imidazo… | HL | NC(Cc1cncn1Cc1ccccc1)C(=O)O | 5.53 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_4 |
| vlm_134280 | ligand_7814 | Benzo-1,3-diazole (Benzimidazole) | L | c1ccc2[nH]cnc2c1 | 5.53 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_8 |
| vlm_134315 | ligand_7815 | 1-Methylbenzimidazole | L | Cn1cnc2ccccc21 | 5.56 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_2 |
| vlm_115804 | ligand_6514 | L-Histidyl-L-histidine | HL | N[C@@H](Cc1c[nH]cn1)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O | 5.66 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |

**Band stats (all 12 entries):**

| stat | value |
|------|-------|
| entries | 12 |
| unique ligands | 12 |
| pKa range | 5.50 – 5.94 |
| T°C range | 25 – 25 |
| I(M) range | 0.1 – 0.5 |
| HxL forms | HL(6), L(6) |
| functional groups | aromatic_ring(12), carboxyl(6), primary_amine(4), secondary_amine(4), amide(1), hydroxyl(1), tertiary_amine(1) |

### pKa 6.0–6.5 (22 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_99027 | ligand_5903 | L-1-Carboxy-2-(4-imidazolyl)ethyl(… | HL | C[N+](C)(C)C(Cc1c[nH]cn1)C(=O)O | 6 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_1 |
| vlm_117146 | ligand_6651 | Glycyl-L-histidylglycyl-L-histidine | *** | *** | 6 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_134275 | ligand_7813 | 4-Phenylimidazole | L | c1ccc(-c2c[nH]cn2)cc1 | 6 | 25 | 0 | L→HL | M_tot_1 | M_tot_1 |
| vlm_101724 | ligand_6027 | L-2-(Dimethylamino)-3-(4-imidazoly… | HL | CN(C)C(Cc1cnc[nH]1)C(=O)O | 6.01 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |
| vlm_99021 | ligand_5902 | L-1-Carboxy-2-(4-imidazolyl)ethyl(… | HL | C[NH+](C)C(Cc1cnc[nH]1)C(=O)O | 6.03 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |

**Band stats (all 22 entries):**

| stat | value |
|------|-------|
| entries | 22 |
| unique ligands | 22 |
| pKa range | 6.00 – 6.48 |
| T°C range | 25 – 37 |
| I(M) range | 0 – 1 |
| HxL forms | L(13), HL(7), None(2) |
| functional groups | aromatic_ring(17), primary_amine(8), carboxyl(7), amide(6), imine(4), ester(3), hydroxyl(3), tertiary_amine(1) |

### pKa 6.5–7.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_115927 | ligand_6525 | L-Methionyl-L-histidine | HL | CSCC[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O | 6.57 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |

---

### Step 20: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_name_SRD LIKE '%cysteine%' OR lc.ligand_name_SRD LIKE '%cysteinate%')",
  "order_by": "p.pKa ASC",
  "limit": 100
}
```

[summary]
## search_pka_values — 53 row(s)

### pKa -11.5–-11.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_101323 | ligand_6007 | L,L-Ethylenediimino-2,2'-bis(merca… | H4L | O=C(O)C(CS)NCCNC(CS)C(=O)O | -11.14 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_8 |

### pKa -2.0–-1.5 (4 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_97397 | ligand_5856 | L-2-Amino-3-mercaptopropanoic acid… | H2L | N[C@@H](CS)C(=O)O | -1.9 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_2 |
| vlm_97762 | ligand_5862 | L-2-Amino-3-(ethylthio)propanoic a… | HL | CCSC[C@H](N)C(=O)O | -1.9 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_2 |
| vlm_98099 | ligand_5879 | L-2-Amino-3-(2-aminoethylthio)prop… | HL | NCCSC[C@H](N)C(=O)O | -1.7 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_101327 | ligand_6007 | L,L-Ethylenediimino-2,2'-bis(merca… | H4L | O=C(O)C(CS)NCCNC(CS)C(=O)O | -1.7 | 25 | 0.1 | H4L→H5L | M_tot_1 | M_tot_1 |

### pKa 2.0–2.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_97702 | ligand_5861 | L-2-Amino-3-(methylthio)propanoic … | HL | CSC[C@H](N)C(=O)O | 2 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_2 |
| vlm_97673 | ligand_5859 | DL-2-Amino-4-mercaptobutanoic acid… | H2L | NC(CCS)C(=O)O | 2.15 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |

### pKa 2.5–3.0 (7 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_115882 | ligand_6522 | D-Methionyl-L-S-methylcysteine | HL | CSCC[C@@H](N)C(=O)N[C@@H](CSC)C(=O)O | 2.72 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |
| vlm_114214 | ligand_6397 | Glycyl-L-cysteine | H2L | NCC(=O)N[C@@H](CS)C(=O)O | 2.73 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_114886 | ligand_6433 | L-Alanyl-L-cysteine | H2L | C[C@H](N)C(=O)N[C@@H](CS)C(=O)O | 2.89 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_114225 | ligand_6398 | Glycyl-L-S-methylcysteine | HL | CSC[C@H](NC(=O)CN)C(=O)O | 2.9 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |
| vlm_115842 | ligand_6518 | L-S-Methylcysteinyl-L-S-methylcyst… | HL | CSC[C@H](NC(=O)[C@@H](N)CSC)C(=O)O | 2.92 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |

**Band stats (all 7 entries):**

| stat | value |
|------|-------|
| entries | 7 |
| unique ligands | 7 |
| pKa range | 2.72 – 2.98 |
| T°C range | 25 – 25 |
| I(M) range | 0.1 – 0.1 |
| HxL forms | HL(4), H2L(3) |
| functional groups | amide(7), carboxyl(7), primary_amine(7), thioether(4), thiol(3), aromatic_ring(1) |

### pKa 3.0–3.5 (4 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_116318 | ligand_6567 | Glycylglycyl-L-cysteine | H2L | NCC(=O)NCC(=O)N[C@@H](CS)C(=O)O | 3.07 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_150799 | ligand_8772 | N-Acetyl-L-cysteine | H2L | CC(=O)N[C@@H](CS)C(=O)O | 3.11 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |
| vlm_116323 | ligand_6568 | L-Alanyl-L-alanyl-L-cysteine | H2L | C[C@H](N)C(=O)N[C@@H](C)C(=O)N[C@@H](CS)C(=O)O | 3.22 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_150893 | ligand_8783 | DL-(2-Mercaptopropionyl)-L-cysteine | H3L | CC(S)C(=O)N[C@@H](CS)C(=O)O | 3.26 | 20 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |

### pKa 5.0–5.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_101326 | ligand_6007 | L,L-Ethylenediimino-2,2'-bis(merca… | H4L | O=C(O)C(CS)NCCNC(CS)C(=O)O | 5.4 | 25 | 0.1 | H3L→H4L | M_tot_1 | M_tot_1 |

### pKa 6.5–7.0 (3 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_121980 | ligand_7008 | L-Cysteine methyl ester | HL | COC(=O)[C@@H](N)CS | 6.53 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |
| vlm_122008 | ligand_7009 | L-Cysteine ethyl ester | H2L | CCOC(=O)[C@@H](N)CS | 6.55 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |
| vlm_122226 | ligand_7019 | L-S-Methylcysteine methyl ester | L | COC(=O)[C@@H](N)CSC | 6.7 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_1 |

### pKa 7.0–7.5 (3 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_115841 | ligand_6518 | L-S-Methylcysteinyl-L-S-methylcyst… | HL | CSC[C@H](NC(=O)[C@@H](N)CSC)C(=O)O | 7.03 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_2 |
| vlm_115393 | ligand_6474 | L-Phenylalanyl-L-cysteine | H2L | N[C@@H](Cc1ccccc1)C(=O)N[C@@H](CS)C(=O)O | 7.25 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |
| vlm_115871 | ligand_6521 | L-Methionyl-L-S-methylcysteine | HL | CSCC[C@H](N)C(=O)N[C@@H](CSC)C(=O)O | 7.4 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_2 |

### pKa 7.5–8.0 (5 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_115881 | ligand_6522 | D-Methionyl-L-S-methylcysteine | HL | CSCC[C@@H](N)C(=O)N[C@@H](CSC)C(=O)O | 7.62 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_2 |
| vlm_116317 | ligand_6567 | Glycylglycyl-L-cysteine | H2L | NCC(=O)NCC(=O)N[C@@H](CS)C(=O)O | 7.82 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_2 |
| vlm_101325 | ligand_6007 | L,L-Ethylenediimino-2,2'-bis(merca… | H4L | O=C(O)C(CS)NCCNC(CS)C(=O)O | 7.91 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_116322 | ligand_6568 | L-Alanyl-L-alanyl-L-cysteine | H2L | C[C@H](N)C(=O)N[C@@H](C)C(=O)N[C@@H](CS)C(=O)O | 7.96 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_3 |
| vlm_114885 | ligand_6433 | L-Alanyl-L-cysteine | H2L | C[C@H](N)C(=O)N[C@@H](CS)C(=O)O | 7.98 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_2 |

### pKa 8.0–8.5 (6 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_114213 | ligand_6397 | Glycyl-L-cysteine | H2L | NCC(=O)N[C@@H](CS)C(=O)O | 8.04 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |
| vlm_114224 | ligand_6398 | Glycyl-L-S-methylcysteine | HL | CSC[C@H](NC(=O)CN)C(=O)O | 8.12 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_2 |
| vlm_97384 | ligand_5856 | L-2-Amino-3-mercaptopropanoic acid… | H2L | N[C@@H](CS)C(=O)O | 8.18 | 25 | 0.1 | HL→H2L | M_tot_2 | M_tot_9 |
| vlm_98097 | ligand_5879 | L-2-Amino-3-(2-aminoethylthio)prop… | HL | NCCSC[C@H](N)C(=O)O | 8.32 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_5 |
| vlm_98005 | ligand_5871 | L-2-Amino-3-(2-Cyanoethylthio)prop… | HL | N#CCCSCC(N)C(=O)O | 8.46 | 30 | 0.5 | L→HL | M_tot_1 | M_tot_1 |

**Band stats (all 6 entries):**

| stat | value |
|------|-------|
| entries | 6 |
| unique ligands | 6 |
| pKa range | 8.04 – 8.46 |
| T°C range | 20 – 30 |
| I(M) range | 0.1 – 0.5 |
| HxL forms | HL(3), H2L(2), H3L(1) |
| functional groups | carboxyl(6), primary_amine(5), amide(3), thioether(3), thiol(3), nitrile(1) |

### pKa 8.5–9.0 (6 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_98006 | ligand_5872 | L-2-Amino-3-(Ethoxy-3-oxopropylthi… | HL | CCOC(=O)CCSCC(N)C(=O)O | 8.51 | 30 | 0.5 | L→HL | M_tot_1 | M_tot_1 |
| vlm_97672 | ligand_5859 | DL-2-Amino-4-mercaptobutanoic acid… | H2L | NC(CCS)C(=O)O | 8.57 | 30 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |
| vlm_97756 | ligand_5862 | L-2-Amino-3-(ethylthio)propanoic a… | HL | CCSC[C@H](N)C(=O)O | 8.65 | 25 | 0.1 | L→HL | M_tot_2 | M_tot_8 |
| vlm_97696 | ligand_5861 | L-2-Amino-3-(methylthio)propanoic … | HL | CSC[C@H](N)C(=O)O | 8.74 | 25 | 0.1 | L→HL | M_tot_2 | M_tot_10 |
| vlm_121977 | ligand_7008 | L-Cysteine methyl ester | HL | COC(=O)[C@@H](N)CS | 8.93 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_6 |

**Band stats (all 6 entries):**

| stat | value |
|------|-------|
| entries | 6 |
| unique ligands | 6 |
| pKa range | 8.51 – 8.96 |
| T°C range | 25 – 30 |
| I(M) range | 0.1 – 0.5 |
| HxL forms | HL(4), H2L(2) |
| functional groups | primary_amine(6), carboxyl(4), ester(3), thioether(3), thiol(3) |

### pKa 9.0–9.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_114212 | ligand_6397 | Glycyl-L-cysteine | H2L | NCC(=O)N[C@@H](CS)C(=O)O | 9.48 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_4 |
| vlm_116316 | ligand_6567 | Glycylglycyl-L-cysteine | H2L | NCC(=O)NCC(=O)N[C@@H](CS)C(=O)O | 9.48 | 25 | 0.1 | L→HL | M_tot_2 | M_tot_2 |

### pKa 9.5–10.0 (6 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_114884 | ligand_6433 | L-Alanyl-L-cysteine | H2L | C[C@H](N)C(=O)N[C@@H](CS)C(=O)O | 9.52 | 25 | 0.1 | L→HL | M_tot_2 | M_tot_5 |
| vlm_150796 | ligand_8772 | N-Acetyl-L-cysteine | H2L | CC(=O)N[C@@H](CS)C(=O)O | 9.58 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_5 |
| vlm_115392 | ligand_6474 | L-Phenylalanyl-L-cysteine | H2L | N[C@@H](Cc1ccccc1)C(=O)N[C@@H](CS)C(=O)O | 9.61 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_2 |
| vlm_98095 | ligand_5879 | L-2-Amino-3-(2-aminoethylthio)prop… | HL | NCCSC[C@H](N)C(=O)O | 9.67 | 25 | 0.1 | L→HL | M_tot_5 | M_tot_1 |
| vlm_116321 | ligand_6568 | L-Alanyl-L-alanyl-L-cysteine | H2L | C[C@H](N)C(=O)N[C@@H](C)C(=O)N[C@@H](CS)C(=O)O | 9.73 | 25 | 0.1 | L→HL | M_tot_3 | M_tot_5 |

**Band stats (all 6 entries):**

| stat | value |
|------|-------|
| entries | 6 |
| unique ligands | 6 |
| pKa range | 9.52 – 9.88 |
| T°C range | 25 – 25 |
| I(M) range | 0.1 – 0.1 |
| HxL forms | H2L(4), HL(1), H4L(1) |
| functional groups | carboxyl(6), thiol(5), amide(4), primary_amine(4), aromatic_ring(1), secondary_amine(1), thioether(1) |

### pKa 10.0–10.5 (3 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_150891 | ligand_8783 | DL-(2-Mercaptopropionyl)-L-cysteine | H3L | CC(S)C(=O)N[C@@H](CS)C(=O)O | 10.17 | 20 | 0.1 | L→HL | M_tot_1 | M_tot_2 |
| vlm_97371 | ligand_5856 | L-2-Amino-3-mercaptopropanoic acid… | H2L | N[C@@H](CS)C(=O)O | 10.3 | 25 | 0.1 | L→HL | M_tot_9 | M_tot_17 |
| vlm_97671 | ligand_5859 | DL-2-Amino-4-mercaptobutanoic acid… | H2L | NC(CCS)C(=O)O | 10.38 | 30 | 0.1 | L→HL | M_tot_1 | M_tot_1 |

---

### Step 21: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_name_SRD LIKE '%glutathione%' OR lc.ligand_name_SRD LIKE '%GSH%')",
  "order_by": "p.pKa ASC",
  "limit": 100
}
```

[summary]
## search_pka_values — 11 row(s)

### pKa -1.5–-1.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_117394 | ligand_6682 | N,N-[N'',N''''-Di(L-5-glutamyl)-L-… | *** | *** | -1.5 | 25 | 0.1 | H5L→H6L | M_tot_1 | M_tot_1 |

### pKa 2.0–2.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_116621 | ligand_6592 | L-5-Glutamyl-L-cysteinylglycine (G… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 2.08 | 25 | 0.1 | H3L→H4L | M_tot_1 | M_tot_1 |
| vlm_117392 | ligand_6682 | N,N-[N'',N''''-Di(L-5-glutamyl)-L-… | *** | *** | 2.35 | 25 | 0.1 | H4L→H5L | M_tot_1 | M_tot_1 |

### pKa 3.0–3.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_117388 | ligand_6682 | N,N-[N'',N''''-Di(L-5-glutamyl)-L-… | *** | *** | 3.16 | 25 | 0.1 | H3L→H4L | M_tot_1 | M_tot_1 |
| vlm_116612 | ligand_6592 | L-5-Glutamyl-L-cysteinylglycine (G… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 3.49 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_4 |

### pKa 3.5–4.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_117384 | ligand_6682 | N,N-[N'',N''''-Di(L-5-glutamyl)-L-… | *** | *** | 3.83 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |

### pKa 8.5–9.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_116606 | ligand_6592 | L-5-Glutamyl-L-cysteinylglycine (G… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 8.64 | 25 | 0.1 | HL→H2L | M_tot_4 | M_tot_4 |
| vlm_117379 | ligand_6682 | N,N-[N'',N''''-Di(L-5-glutamyl)-L-… | *** | *** | 8.85 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |

### pKa 9.0–9.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_116714 | ligand_6593 | L-5-Glutamyl-(S-methyl-L-cysteinyl… | H2L | CSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O | 9.08 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_5 |

### pKa 9.5–10.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_116600 | ligand_6592 | L-5-Glutamyl-L-cysteinylglycine (G… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 9.51 | 25 | 0.1 | L→HL | M_tot_4 | M_tot_9 |
| vlm_117374 | ligand_6682 | N,N-[N'',N''''-Di(L-5-glutamyl)-L-… | *** | *** | 9.81 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_6 |

---
