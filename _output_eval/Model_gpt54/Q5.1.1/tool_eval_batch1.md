# Q5.1.1 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Hg(I), Hg(II), mercury, mercurous, mercuric",
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
  "symbol": "Hg",
  "limit": 20
}
```

[summary]
## search_metals — 8 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_53 | EtHg^[+] | EHg | 1 |  | *** | *** | beta_totN_4 | ligand_totN_3 | vlm_totN_6 |
| metal_71 | Hg^[2+] | Hg | 2 | ✓ | [Hg+2] | InChI=1S/Hg/q+2 | beta_totN_68 | ligand_totN_310 | vlm_totN_1097 |
| metal_72 | Hg^[+] | Hg | 1 | ✓ | [Hg+] | InChI=1S/Hg/q+1 | beta_totN_12 | ligand_totN_31 | vlm_totN_83 |
| metal_93 | MeHg^[+] | MHg | 1 |  | *** | *** | beta_totN_18 | ligand_totN_79 | vlm_totN_148 |
| metal_136 | PhHg^[+] | PhHg | 1 |  | *** | *** | beta_totN_2 | ligand_totN_8 | vlm_totN_8 |
| metal_145 | PrHg^[+] | Pr | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_176 | O_[3]SPhHg | S | 0 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |

---

### Step 5: `db_count_records`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "where": "metal_id = '[''metal_71'', ''metal_72'', ''metal_53'', ''metal_93'', ''metal_136'']'"
}
```

[TOOL ERROR] db_count_records: Error executing tool db_count_records: no such column: metal_id

---

### Step 6: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurement_count",
  "limit": 12,
  "where": "lc.metal_id = 'metal_71'"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurement_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 7: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurement_count",
  "limit": 12,
  "where": "lc.metal_id = 'metal_72'"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurement_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_name_SRD IN ('chloride','bromide','iodide','ammonia','cyanide','thiocyanate','thiosulfate','thiourea','EDTA') AND s.solvent_name LIKE '%water%')",
  "order_by": "c.ligand_name_SRD ASC, s.constant_value DESC",
  "limit": 60
}
```

[summary]
## search_stability

*(no results)*

---

### Step 9: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_71, metal_72))",
  "order_by": "n.node_count DESC",
  "limit": 10
}
```

[summary]
## search_networks — 14 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_713 | ``[MCl2] + [L] <=> [MClL] + [Cl]`` |
| beta_def_845 | ``[MCl2] + [L]^2 <=> [ML2] + [Cl]^2`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|---------------|
| `Hg^[2+]` | metal_71 | Aminoacetic acid (Glycine) | ligand_5760 | HL | 15~30 | -0.05~0.65 | 2 | 2 | NCC(=O)O |
| `Hg^[2+]` | metal_71 | 13,16,21,24-Tetramethyl-4,7-dioxa-1,10,… | ligand_7655 | L | 20~30 | -0.05~0.25 | 1 | 2 | CN1CCN(C)CCN2CCOCCOCCN(CC1)CCN(C)CCN(C)CC2 |
| `Hg^[2+]` | metal_71 | L-2-Amino-5-ureidopentanoic acid (Citru… | ligand_5852 | HL | 20~30 | -0.05~0.25 | 1 | 2 | NC(=O)NCCC[C@H](N)C(=O)O |
| `Hg^[2+]` | metal_71 | 3-Aminopropanoic acid (beta-Alanine) | ligand_5788 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | NCCC(=O)O |
| `Hg^[2+]` | metal_71 | cis-2-Aminocyclopentane-1-carboxylic ac… | ligand_5790 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | N[C@H]1CCC[C@H]1C(=O)O |
| `Hg^[2+]` | metal_71 | cis-2-Aminocyclohexane-1-carboxylic acid | ligand_5792 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | N[C@H]1CCCC[C@H]1C(=O)O |
| `Hg^[2+]` | metal_71 | trans-2-Aminocyclohexane-1-carboxylic a… | ligand_5793 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | N[C@@H]1CCCC[C@H]1C(=O)O |
| `Hg^[2+]` | metal_71 | cis-2-Amino-4-cyclohexene-1-carboxylic … | ligand_5794 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | N[C@H]1CC=CC[C@H]1C(=O)O |
| `Hg^[2+]` | metal_71 | trans-2-Amino-4-cyclohexene-1-carboxyli… | ligand_5795 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | N[C@@H]1CC=CC[C@H]1C(=O)O |

### Max-node network per pair
| metal | metal_id | ligand | ligand_id | max_net_id | max_nodes | max_edge_counts | max_T_range | max_I_range | max_vlm_counts | max_beta_def_ids | max_type | max_values |
|-------|----------|--------|----------|------------|-----------|------------------|-------------|-------------|----------------|------------------|----------|------------|
| `Hg^[2+]` | metal_71 | Aminoacetic acid (Glycine) | ligand_5760 | ref_eq_net_126 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_713; beta_def_845 | logK | 3.42~6.03 |
| `Hg^[2+]` | metal_71 | 13,16,21,24-Tetramethyl-4,7-dioxa-1,10,… | ligand_7655 | ref_eq_net_189 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_788; beta_def_812 | logK | 4.2~26.1 |
| `Hg^[2+]` | metal_71 | L-2-Amino-5-ureidopentanoic acid (Citru… | ligand_5852 | ref_eq_net_983 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_840; beta_def_812 | logK | -10.95~-6.02 |
| `Hg^[2+]` | metal_71 | 3-Aminopropanoic acid (beta-Alanine) | ligand_5788 | ref_eq_net_476 | 1 | 0 | 16.5~31.5 | 0.275~0.725 | 1 | beta_def_812 | logK | 11.31 |
| `Hg^[2+]` | metal_71 | cis-2-Aminocyclopentane-1-carboxylic ac… | ligand_5790 | ref_eq_net_489 | 1 | 0 | 16.5~31.5 | 0.275~0.725 | 1 | beta_def_812 | logK | 11.17 |
| `Hg^[2+]` | metal_71 | cis-2-Aminocyclohexane-1-carboxylic acid | ligand_5792 | ref_eq_net_496 | 1 | 0 | 16.5~31.5 | 0.275~0.725 | 1 | beta_def_812 | logK | 11.46 |
| `Hg^[2+]` | metal_71 | trans-2-Aminocyclohexane-1-carboxylic a… | ligand_5793 | ref_eq_net_501 | 1 | 0 | 16.5~31.5 | 0.275~0.725 | 1 | beta_def_812 | logK | 11.29 |
| `Hg^[2+]` | metal_71 | cis-2-Amino-4-cyclohexene-1-carboxylic … | ligand_5794 | ref_eq_net_506 | 1 | 0 | 16.5~31.5 | 0.275~0.725 | 1 | beta_def_812 | logK | 15.9 |
| `Hg^[2+]` | metal_71 | trans-2-Amino-4-cyclohexene-1-carboxyli… | ligand_5795 | ref_eq_net_510 | 1 | 0 | 16.5~31.5 | 0.275~0.725 | 1 | beta_def_812 | logK | 25.18 |

### Global max-node network: `Hg^[2+]` + Aminoacetic acid (Glycine)
network_id: ref_eq_net_126 | metal_id: metal_71 | ligand_id: ligand_5760 | ligand_def_HxL: HL | nodes: 2

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_713 | ``[MCl2] + [L] <=> [MClL] + [Cl]`` | logK | 3.42 |
| beta_def_845 | ``[MCl2] + [L]^2 <=> [ML2] + [Cl]^2`` | logK | 6.03 |

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id IN (ligand_5760, ligand_5788, ligand_5790, ligand_5792, ligand_5793, ligand_5794, ligand_5795, ligand_5852, ligand_7655))",
  "order_by": "c.ligand_name_SRD ASC, s.constant_value DESC",
  "limit": 40
}
```

[summary]
## search_stability — 18 row(s)

### logK — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 4 | 4 | 20~25 | 0~0.5 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_7655 | 13,16,21,24-Tetramethyl-4,7… | L | CN1CCN(C)CCN2CCOCCOCCN(CC1)CCN(C)CCN(C)CC2 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_5852 | L-2-Amino-5-ureidopentanoic… | HL | NC(=O)NCCC[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_5788 | 3-Aminopropanoic acid (beta… | HL | NCCC(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_5794 | cis-2-Amino-4-cyclohexene-1… | HL | N[C@H]1CC=CC[C@H]1C(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_5792 | cis-2-Aminocyclohexane-1-ca… | HL | N[C@H]1CCCC[C@H]1C(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_5790 | cis-2-Aminocyclopentane-1-c… | HL | N[C@H]1CCC[C@H]1C(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_5795 | trans-2-Amino-4-cyclohexene… | HL | N[C@@H]1CC=CC[C@H]1C(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_5793 | trans-2-Aminocyclohexane-1-… | HL | N[C@@H]1CCCC[C@H]1C(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |

### ΔS — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

### ΔH — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 2 | 25 | 0 | *** | 0 |

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_72)",
  "order_by": "s.constant_value DESC",
  "limit": 25
}
```

[summary]
## search_stability — 25 row(s)

### ΔS — 2 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_72 | Hg^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_72 | Hg^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |

### ΔH — 2 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_72 | Hg^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |
| metal_72 | Hg^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 12 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_72 | Hg^[+] | ligand_10076 | Hydroxide ion | *** | *** | 4 | 3 | 25 | 0.5~3 | *** | 2 |
| metal_72 | Hg^[+] | ligand_10114 | Hydrogen diphosphate (Pyrop… | H4L | O=P(O)(O)OP(=O)(O)O | 2 | 2 | 27 | 0.7 | *** | 1 |
| metal_72 | Hg^[+] | ligand_10117 | Hydrogen triphosphate (Trip… | H5L | O=P(O)(O)OP(=O)(O)OP(=O)(O)O | 2 | 2 | 27 | 0.7 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8887 | Propane-2,2-dicarboxylic ac… | H2L | CC(C)(C(=O)O)C(=O)O | 2 | 2 | 27 | 0.7 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 2 | 2 | 27 | 2.5 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 27 | 2.5 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8467 | Propanoic acid (Propionic a… | HL | CCC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8724 | 3-Methoxypropanoic acid | HL | COCCC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 1 | 1 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8464 | Methanoic acid (Formic acid) | HL | O=CO | 1 | 1 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8721 | Methoxyacetic acid | HL | COCC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |

---
