# Q3.2.4 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "iron"
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 4: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "ligand_class_name",
  "where": "metal_id = 61",
  "limit": 25
}
```

[summary]
## db_distribution - ligandmetal_card by ligand_class_name

**total_rows:** 1473

| value | count | pct |
|-------|-------|-----|
| Inorganic ligands | 198 | 13.44% |
| Catechols | 140 | 9.5% |
| miscellaneous hydroxamic acids | 124 | 8.42% |
| Amino Acids | 116 | 7.88% |
| EDTA and derivatives | 106 | 7.2% |
| Aliphatic amines | 102 | 6.92% |
| Phenols salicylic acids | 99 | 6.72% |
| Phenols | 67 | 4.55% |
| Carboxylic acids | 61 | 4.14% |
| Pyridines (azines) | 49 | 3.33% |
| NTA and derivatives | 45 | 3.05% |
| Aza macrocycles with carboxylic acids | 42 | 2.85% |
| Carboxylic acids diacids | 36 | 2.44% |
| cyclic ketones | 34 | 2.31% |
| Carboxylic acids polyacids | 33 | 2.24% |
| Aminophosphorus acids | 33 | 2.24% |
| Naphtols | 29 | 1.97% |
| Quinolines | 22 | 1.49% |
| Aza-macrocycles | 15 | 1.02% |
| Aliphatic amines secondary N | 15 | 1.02% |
| Aliphatic amines tertiary N | 14 | 0.95% |
| Carboxylic acids diacids hydroxy | 13 | 0.88% |
| Pyridine carboxylic acids | 12 | 0.81% |
| Phenanthrolines | 11 | 0.75% |
| Ketones (oxo ligands) | 9 | 0.61% |

---

### Step 5: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "ligand_class_name",
  "where": "metal_id = 62",
  "limit": 25
}
```

[summary]
## db_distribution - ligandmetal_card by ligand_class_name

**total_rows:** 667

| value | count | pct |
|-------|-------|-----|
| Amino Acids | 101 | 15.14% |
| EDTA and derivatives | 78 | 11.69% |
| Inorganic ligands | 75 | 11.24% |
| Phenanthrolines | 33 | 4.95% |
| Aminophosphorus acids | 31 | 4.65% |
| Bipyridines | 30 | 4.5% |
| NTA and derivatives | 29 | 4.35% |
| Pyridines (azines) | 28 | 4.2% |
| Pyridine carboxylic acids | 24 | 3.6% |
| Carboxylic acids polyacids | 23 | 3.45% |
| Iminodiacetic acid and derivatives | 20 | 3.0% |
| Aza macrocycles with carboxylic acids | 18 | 2.7% |
| Pyrroles (azoles) | 16 | 2.4% |
| Aza-macrocycles | 16 | 2.4% |
| Tripyridines | 15 | 2.25% |
| Catechols | 15 | 2.25% |
| Aza-oxa-macrocycles | 15 | 2.25% |
| Aliphatic amines secondary N | 15 | 2.25% |
| Carboxylic acids diacids S-Se-Te-P-As | 11 | 1.65% |
| Carboxylic acids diacids | 11 | 1.65% |
| Aliphatic amines tertiary N | 10 | 1.5% |
| miscellaneous hydroxamic acids | 9 | 1.35% |
| Aliphatic amines | 9 | 1.35% |
| Ketones (oxo ligands) | 5 | 0.75% |
| miscellaneous ureas, hadrazides, amidines | 4 | 0.6% |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND s.temperature_c BETWEEN 20 AND 30 AND s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2)",
  "order_by": "s.constant_value DESC",
  "limit": 40
}
```

[summary]
## search_stability — 40 row(s)

### ΔS — 17 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_10076 | Hydroxide ion | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9414 | N,N',N''-Tris(2,3-dihydroxy… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9192 | Hydroxybenzene (Phenol) | HL | Oc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9251 | 3-Cyanophenol | HL | N#Cc1cccc(O)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9218 | 3-Chlorophenol | HL | Oc1cccc(Cl)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9237 | 3-Nitrophenol | HL | O=[N+]([O-])c1cccc(O)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9217 | 2-Chlorophenol | HL | Oc1ccccc1Cl | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9219 | 4-Chlorophenol | HL | Oc1ccc(Cl)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9250 | 2-Cyanophenol | HL | N#Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9302 | 4-Hydroxybenzaldehyde | HL | O=Cc1ccc(O)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9252 | 4-Cyanophenol | HL | N#Cc1ccc(O)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9238 | 4-Nitrophenol | HL | O=[N+]([O-])c1ccc(O)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9402 | N,N',N''-Tris(2,3-dihydroxy… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9410 | 1,3,5-Tris(2,3-dihydroxy-5-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 21 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_9894 | Trimethylenedihydroxamic ac… | H2L | O=C(CCCC(=O)NO)NO | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7391 | Piperazine-N,N'-diacetohydr… | H2L | O=C(CN1CCN(C(=O)NO)CC1)NO | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9901 | N,N'-Di-2-propylpentamethyl… | H2L | CC(C)N(O)C(=O)CCCCCC(=O)N(O)C(C)C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9902 | N,N'-Di-2-propylhexamethyle… | H2L | CC(C)N(O)C(=O)CCCCCCC(=O)N(O)C(C)C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9900 | N,N'-Di-2-propyltetramethyl… | H2L | CC(C)N(O)C(=O)CCCCC(=O)N(O)C(C)C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9906 | Rhodotorulic acid | H2L | CC(=O)N(O)CCCC1NC(=O)C(CCCN(O)C(C)=O)NC1=O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9899 | N,N'-Di-2-propyltrimethylen… | H2L | CC(C)N(O)C(=O)CCCC(=O)N(O)C(C)C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9905 | Trimethylenebis[aminocarbon… | H2L | O=C(NCCCNC(=O)c1cccc(=O)n1O)c1cccc(=O)n1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7422 | 1,4,7-Tris(3-hydroxy-6-meth… | H3L | Cc1ccc(O)c(CN2CCN(Cc3nc(C)ccc3O)CCN(Cc3nc(C)ccc3O)CC2)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7154 | Iminodiacetohydroxamic acid | H2L | O=C(CNCC(=O)NO)NO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6371 | 1,4-Bis[2,5,5-tris(carboxym… | H6L | O=C(O)CN(CCN(CC(=O)O)Cc1ccc(CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)cc1)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6021 | N,N-Bis(2-hydroxyethyl)glyc… | HL | O=C(O)CN(CCO)CCO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6124 | 6,16-Bis(carboxymethyl)-1,1… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7340 | 1,3,5-Tris(dimethylamino)-1… | L | CN(C)[C@H]1[C@@H](O)[C@@H](N(C)C)[C@@H](O)[C@@H](N(C)C)[C@H]1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8126 | 8-Hydroxyquinoline (8-Quino… | HL | Oc1cccc2cccnc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6038 | N,N'-Bis(2-hydroxy-5-sulfob… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1cc(S(=O)(=O)O)ccc1O)Cc1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7950 | 1,2-Diethyl-3,4-dihydroxypy… | HL | CCc1c(O)c(=O)ccn1CC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6125 | 7,19-Bis(carboxymethyl)-1,1… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7949 | 1,2-Dimethyl-3,4-dihydroxyp… | HL | Cc1c(O)c(=O)ccn1C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5995 | rac-Ethylenediiminobis[(2-h… | H4L | O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND s.temperature_c BETWEEN 20 AND 30 AND s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2)",
  "order_by": "s.constant_value DESC",
  "limit": 40
}
```

[summary]
## search_stability — 40 row(s)

### ΔS — 14 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7345 | Nitrilotris(ethyleneamine) … | L | NCCN(CCN)CCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7348 | Ethylenedinitrilotetrakis(e… | L | NCCN(CCN)CCN(CCN)CCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8205 | Nitrilotris(methylene-2-pyr… | L | c1ccc(CN(Cc2ccccn2)Cc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8174 | Iminobis(methylene-2-pyridi… | L | c1ccc(CNCc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8209 | Ethylenedinitrilotetrakis(m… | L | c1ccc(CN(CCN(Cc2ccccn2)Cc2ccccn2)Cc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8204 | 2,6-Di(2-pyridyl)pyridine (… | L | c1ccc(-c2cccc(-c3ccccn3)n2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 23 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_9759 | 2,3-Dimercaptopropanol (BAL) | H2L | OCC(S)CS | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6349 | Dithiobis(ethylenenitrilo)t… | H4L | O=C(O)CN(CCSSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6287 | rac-(1,2-Dimethylethylene)d… | H4L | CC(C(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8193 | 5-Methyl-1,10-phenanthroline | L | Cc1cc2cccnc2c2ncccc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8204 | 2,6-Di(2-pyridyl)pyridine (… | L | c1ccc(-c2cccc(-c3ccccn3)n2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8199 | 5-Chloro-1,10-phenanthroline | L | Clc1cc2cccnc2c2ncccc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8156 | 2,2'-Bipyridyl | L | c1ccc(-c2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8176 | 2-(2-Pyridylmethylenehydraz… | L | C(=N/Nc1ccccn1)\c1ccccn1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6084 | 1-Oxa-4,7,10-triazacyclodod… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6366 | Triethylenetetranitrilohexa… | H6L | O=C(O)CN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8360 | Amino(phenyl)methylenedipho… | H4L | NC(c1ccccc1)(P(=O)(O)O)P(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8434 | Pyridine-2,6-diphosphonic a… | H4L | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6288 | meso-(1,2-Dimethylethylene)… | H4L | C[C@H]([C@H](C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6193 | N-(Phosphonomethyl)iminodia… | H4L | O=C(O)CN(CC(=O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-… | H2L | Cc1cc2c(O)c(c1)CNCc1cccc(n1)CNCc1cc(C)cc(c1O)CNCc1cccc(n1)CNC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7661 | 5-(2-Hydroxyphenyl)-1,4,8,1… | HL | Oc1ccccc1C1CCNCCNCCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6082 | 1-Oxa-4,7,10-triazacyclodod… | H2L | O=C(O)CN1CCNCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |

---
