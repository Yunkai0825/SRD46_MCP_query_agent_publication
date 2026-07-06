# Qfree_20260423_162116 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Fe(II), Fe(III), H+",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 3: `search_metals`
**Args:**
```json
{
  "name": "iron, ferric, ferrous, Fe",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 5: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "metal_name_SRD",
  "where": "metal_name_SRD LIKE '%Fe%' OR metal_name_SRD LIKE '%iron%' OR metal_name_SRD LIKE '%ferr%' OR metal_name_SRD LIKE '%ferrous%'",
  "limit": 50
}
```

[summary]
## db_distribution - ligandmetal_card by metal_name_SRD

**total_rows:** 2140

| value | count | pct |
|-------|-------|-----|
| Fe^[3+] | 1473 | 68.83% |
| Fe^[2+] | 667 | 31.17% |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD LIKE '%Fe%' OR c.metal_name_SRD LIKE '%iron%' OR c.metal_name_SRD LIKE '%ferr%' OR c.metal_name_SRD LIKE '%ferrous%')",
  "order_by": "c.ligand_name_SRD ASC",
  "limit": 50
}
```

[TOOL ERROR] search_stability: Error executing tool search_stability: SQL parse error: Invalid expression / Unexpected token. Line 1, Col: 47.
  SELECT 1 FROM _stub WHERE c.ligand_name_SRD [4mASC[0m

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD LIKE '%Fe%' OR c.metal_name_SRD LIKE '%iron%' OR c.metal_name_SRD LIKE '%ferr%' OR c.metal_name_SRD LIKE '%ferrous%')",
  "limit": 50
}
```

[summary]
## search_stability — 50 row(s)

### logK — 20 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 10 | 3 | 10~40 | 0~3 | *** | 7 |
| metal_61 | Fe^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 3 | 25 | 0.5~3 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 4 | 3 | 20~25 | 1~3 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 4 | 3 | 20~25 | 1~3 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_7653 | 6,16-Dioxa-3,9,13,19-tetraa… | L | c1cc2nc(c1)CNCCOCCNCc1cccc(n1)CNCCOCCNC2 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5809 | L-2-Amino-3-phosphopropanoi… | H3L | N[C@@H](COP(=O)(O)O)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 2 | 1 | 25~37 | 0.1~0.15 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5765 | L-2-Amino-3-methylbutanoic … | HL | CC(C)[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5766 | L-2-Amino-4-methylpentanoic… | HL | CC(C)C[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5769 | 2-Amino-2-methylpropanoic a… | HL | CC(C)(N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5770 | DL-2-Amino-4-pentenoic acid | HL | C=CCC(N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5788 | 3-Aminopropanoic acid (beta… | HL | NCCC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5804 | L-2-Aminopentanedioic acid … | H2L | N[C@@H](CCC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5804 | L-2-Aminopentanedioic acid … | H2L | N[C@@H](CCC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5826 | L-2-Amino-3-(3,4-dihydroxyp… | H3L | NC(Cc1ccc(O)c(O)c1)C(=O)O | 1 | 1 | 25 | 1 | *** | 1 |

### ΔH — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 1 | 10~40 | 0 | *** | 0 |

### ΔS — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |

---

### Step 8: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurement_count",
  "limit": 40,
  "where": "metal_name_SRD IN ('Fe^[3+]', 'Fe^[2+]')"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurement_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 9: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_name = 'Fe^[3+]' OR c.metal_name = 'Fe^[2+]')",
  "order_by": "n.node_count DESC",
  "limit": 20
}
```

[TOOL ERROR] search_networks: Error executing tool search_networks: SQL parse error: Invalid expression / Unexpected token. Line 1, Col: 43.
  SELECT 1 FROM _stub WHERE n.node_count [4mDESC[0m

---

### Step 10: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurements_per_ligand",
  "limit": 30,
  "where": "metal_name_SRD IN ('Fe^[3+]', 'Fe^[2+]')"
}
```

[summary]
## db_ranked_pairs - measurements_per_ligand

| ligand_id | name | count |
|-----------|------|-------|
| ligand_10076 | Hydroxide ion | 51 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | 41 |
| ligand_10103 | Ammonia | 32 |
| ligand_6165 | Nitrilotriacetic acid (NTA) | 23 |
| ligand_10106 | Hydrogen azide (Hydrazoic acid) | 22 |
| ligand_5760 | Aminoacetic acid (Glycine) | 20 |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | 20 |
| ligand_6301 | trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA) | 20 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | 19 |
| ligand_6371 | 1,4-Bis[2,5,5-tris(carboxymethyl)-2,5-diazapentyl]benzene (… | 17 |
| ligand_8465 | Ethanoic acid (Acetic acid) | 17 |
| ligand_8873 | Propanedioic acid (Malonic acid) | 17 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | 17 |
| ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-dihydroxy-5,13(5)-dimethyl-1,9(2… | 16 |
| ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) | 16 |
| ligand_8434 | Pyridine-2,6-diphosphonic acid (2,6-PDPA) | 16 |
| ligand_9358 | 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron) | 16 |
| ligand_10113 | Hydrogen phosphate (Phosphoric acid) | 16 |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriacetic acid (HEDTA) | 15 |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | 15 |
| ligand_10163 | Chloride ion | 15 |
| ligand_10162 | Hydrogen fluoride (Hydrofluoric acid) | 14 |
| ligand_5828 | L-2-Amino-3-hydroxypropanoic acid (Serine) | 13 |
| ligand_8126 | 8-Hydroxyquinoline (8-Quinolinol)(Oxine) | 13 |
| ligand_8872 | Ethanedioic acid (Oxalic acid) | 13 |
| ligand_9297 | 4-Amino-2-hydroxybenzoic acid (p-Aminosalicylic acid) | 13 |
| ligand_6770 | Pyridine-2-phosphonic-6-carboxylic acid (2PP6C) | 12 |
| ligand_6995 | DL-2-Amino-3-hydroxybutanohydroxamic acid (Threoninehydroxa… | 12 |
| ligand_9526 | Pentane-2,4-dione (Acetylacetone) | 12 |
| ligand_9873 | Acetohydroxamic acid | 12 |

---

### Step 11: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_name_SRD IN ('glycine', 'phenylalanine', 'aspartic acid', 'glutamic acid', 'phosphoserine', 'DOPA', 'alanine', 'serine', 'valine', 'leucine', 'beta-alanine'))",
  "limit": 100
}
```

[summary]
## search_pka_ligands

*(no results)*

---

### Step 12: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_name IN ('Fe^[3+]', 'Fe^[2+]'))",
  "limit": 20
}
```

[summary]
## search_networks — 31 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_194 | ``[M] + [HL]^2 <=> [M(HL)2]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|---------------|
| `Fe^[2+]` | metal_62 | Aminoacetic acid (Glycine) | ligand_5760 | HL | 5~45 | -0.15~3.15 | 7 | 3 | NCC(=O)O |
| `Fe^[3+]` | metal_61 | Aminoacetic acid (Glycine) | ligand_5760 | HL | 16.5~31.5 | 0.275~3.225 | 3 | 3 | NCC(=O)O |
| `Fe^[2+]` | metal_62 | L-2-Aminopropanoic acid (Alanine) | ligand_5761 | HL | 12.5~27.5 | 0.775~1.225 | 1 | 1 | C[C@H](N)C(=O)O |
| `Fe^[2+]` | metal_62 | 6,16-Dioxa-3,9,13,19-tetraaza-1,11(2,6)… | ligand_7653 | L | 20~30 | -0.05~0.25 | 1 | 3 | c1cc2nc(c1)CNCCOCCNCc1cccc(n1)CNCCOCCNC2 |
| `Fe^[3+]` | metal_61 | L-2-Aminopropanoic acid (Alanine) | ligand_5761 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 2 | C[C@H](N)C(=O)O |
| `Fe^[2+]` | metal_62 | DL-2-Aminobutanoic acid | ligand_5762 | HL | 12.5~27.5 | 0.775~1.225 | 1 | 1 | CCC(N)C(=O)O |
| `Fe^[2+]` | metal_62 | L-2-Amino-3-methylbutanoic acid (Valine) | ligand_5765 | HL | 12.5~27.5 | 0.775~1.225 | 1 | 1 | CC(C)[C@H](N)C(=O)O |
| `Fe^[2+]` | metal_62 | L-2-Amino-4-methylpentanoic acid (Leuci… | ligand_5766 | HL | 12.5~27.5 | 0.775~1.225 | 1 | 1 | CC(C)C[C@H](N)C(=O)O |
| `Fe^[2+]` | metal_62 | 2-Amino-2-methylpropanoic acid (2-Amino… | ligand_5769 | HL | 12.5~27.5 | 0.775~1.225 | 1 | 1 | CC(C)(N)C(=O)O |
| `Fe^[2+]` | metal_62 | DL-2-Amino-4-pentenoic acid | ligand_5770 | HL | 20~30 | -0.05~0.25 | 1 | 1 | C=CCC(N)C(=O)O |
| `Fe^[2+]` | metal_62 | L-2-Amino-3-phenylpropanoic acid (Pheny… | ligand_5777 | HL | 12.5~31.5 | 0.775~3.225 | 2 | 3 | N[C@@H](Cc1ccccc1)C(=O)O |

### Max-node network per pair
| metal | metal_id | ligand | ligand_id | max_net_id | max_nodes | max_edge_counts | max_T_range | max_I_range | max_vlm_counts | max_beta_def_ids | max_type | max_values |
|-------|----------|--------|----------|------------|-----------|------------------|-------------|-------------|----------------|------------------|----------|------------|
| `Fe^[2+]` | metal_62 | Aminoacetic acid (Glycine) | ligand_5760 | ref_eq_net_64 | 3 | 3 | 19~29 | 0.85~1.15 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 3.73~8.87 |
| `Fe^[3+]` | metal_61 | Aminoacetic acid (Glycine) | ligand_5760 | ref_eq_net_96 | 3 | 3 | 16.5~31.5 | 2.775~3.225 | 3 | beta_def_812; beta_def_779; beta_def_194 | logK | -9.25~3.7 |
| `Fe^[2+]` | metal_62 | L-2-Aminopropanoic acid (Alanine) | ligand_5761 | ref_eq_net_155 | 1 | 0 | 12.5~27.5 | 0.775~1.225 | 1 | beta_def_812 | logK | 3.54 |
| `Fe^[2+]` | metal_62 | 6,16-Dioxa-3,9,13,19-tetraaza-1,11(2,6)… | ligand_7653 | ref_eq_net_167 | 3 | 3 | 20~30 | -0.05~0.25 | 3 | beta_def_966; beta_def_812; beta_def_788 | logK | 5.09~7.64 |
| `Fe^[3+]` | metal_61 | L-2-Aminopropanoic acid (Alanine) | ligand_5761 | ref_eq_net_207 | 2 | 1 | 16.5~31.5 | 0.275~0.725 | 2 | beta_def_812; beta_def_966 | logK | -8.88~2.17 |
| `Fe^[2+]` | metal_62 | DL-2-Aminobutanoic acid | ligand_5762 | ref_eq_net_234 | 1 | 0 | 12.5~27.5 | 0.775~1.225 | 1 | beta_def_812 | logK | 3.37 |
| `Fe^[2+]` | metal_62 | L-2-Amino-3-methylbutanoic acid (Valine) | ligand_5765 | ref_eq_net_271 | 1 | 0 | 12.5~27.5 | 0.775~1.225 | 1 | beta_def_812 | logK | 3.39 |
| `Fe^[2+]` | metal_62 | L-2-Amino-4-methylpentanoic acid (Leuci… | ligand_5766 | ref_eq_net_299 | 1 | 0 | 12.5~27.5 | 0.775~1.225 | 1 | beta_def_812 | logK | 3.42 |
| `Fe^[2+]` | metal_62 | 2-Amino-2-methylpropanoic acid (2-Amino… | ligand_5769 | ref_eq_net_334 | 1 | 0 | 12.5~27.5 | 0.775~1.225 | 1 | beta_def_812 | logK | 3.48 |
| `Fe^[2+]` | metal_62 | DL-2-Amino-4-pentenoic acid | ligand_5770 | ref_eq_net_343 | 1 | 0 | 20~30 | -0.05~0.25 | 1 | beta_def_812 | logK | 3.73 |
| `Fe^[2+]` | metal_62 | L-2-Amino-3-phenylpropanoic acid (Pheny… | ligand_5777 | ref_eq_net_396 | 3 | 3 | 16.5~31.5 | 2.775~3.225 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 3.74~10.7 |

### Global max-node network: `Fe^[2+]` + Aminoacetic acid (Glycine)
network_id: ref_eq_net_64 | metal_id: metal_62 | ligand_id: ligand_5760 | ligand_def_HxL: HL | nodes: 3

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 3.73 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 6.65 |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` | logK | 8.87 |

---
