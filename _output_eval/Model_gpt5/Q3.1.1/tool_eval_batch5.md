# Q3.1.1 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "symbol": "Pb",
  "limit": 10
}
```

[summary]
## search_metals — 10 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_16 | Bu_[3]Pb^[+] | B | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_46 | Et_[2]Pb^[2+] | E2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_49 | Et_[3]Pb^[+] | E3Pb | 1 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_84 | Me_[2]Pb^[2+] | M2Pb | 2 |  | *** | *** | beta_totN_5 | ligand_totN_4 | vlm_totN_9 |
| metal_87 | Me_[3]Pb^[+] | M3Pb | 1 |  | *** | *** | beta_totN_7 | ligand_totN_23 | vlm_totN_33 |
| metal_125 | Pb^[2+] | Pb | 2 | ✓ | [Pb+2] | InChI=1S/Pb/q+2 | beta_totN_80 | ligand_totN_470 | vlm_totN_1585 |
| metal_126 | Pb^[4+] | Pb | 4 | ✓ | [Pb+4] | InChI=1S/Pb/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_129 | Ph_[2]Pb^[2+] | Ph2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_130 | Ph_[3]Pb^[+] | Ph3Pb | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_140 | Pr_[2]Pb^[2+] | Pr | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |

---

### Step 4: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND s.temperature_c BETWEEN 24 AND 26)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 50 row(s)

### ΔS — 33 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_125 | Pb^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 3 | 3 | 25 | 3 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 3 | 3 | 25 | 3 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_8673 | 3-Hydroxypropanoic acid | HL | O=C(O)CCO | 2 | 2 | 25 | 2 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_10114 | Hydrogen diphosphate (Pyrop… | H4L | O=P(O)(O)OP(=O)(O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7522 | 3,6,9,12-Tetraaza-1(2,9)-1,… | L | c1cc2ccc3ccc4nc3c2nc1CNCCNCCNCCNC4 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7532 | 3,6,9,12,15-Pentaaza-1(2,9)… | L | c1cc2ccc3ccc4nc3c2nc1CNCCNCCNCCNCCNC4 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6793 | N-(2-Pyridylmethyl)iminodia… | H2L | O=C(O)CN(CC(=O)O)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7509 | 3,6,9-Triaza-1(2,9)-1,10-ph… | L | c1cc2ccc3ccc4nc3c2nc1CNCCNCCNC4 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6140 | N-Methyliminodiacetic acid … | H2L | CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7528 | 3,6,10,13-Tetraaza-1,8(2,6)… | L | c1cc2nc(c1)CNCCNCc1cccc(n1)CNCCNC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6316 | Octamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |
| metal_125 | Pb^[2+] | ligand_7588 | 7,16-Bis(2-hydroxyethyl)-1,… | L | OCCN1CCOCCOCCN(CCO)CCOCCOCC1 | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7529 | 3,7,11,15-Tetraaza-1,9(2,6)… | L | c1cc2nc(c1)CNCCCNCc1cccc(n1)CNCCCNC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_10163 | Chloride ion | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_8206 | Nitrilotris[methylene(6-met… | L | Cc1cccc(CN(Cc2cccc(C)n2)Cc2cccc(C)n2)n1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7601 | 4,7,13,16,21,24-Hexaoxa-1,1… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCCOCC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_125 | Pb^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 3 | 1 | 25 | 0~3 | *** | 3 |
| metal_125 | Pb^[2+] | ligand_9747 | 2-Mercaptoethanol | HL | OCCS | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_125 | Pb^[2+] | ligand_9748 | 3-Mercaptopropane-1,2-diol … | HL | OCC(O)CS | 1 | 1 | 25 | 0.5 | *** | 1 |

### ΔH — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_125 | Pb^[2+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |
| metal_125 | Pb^[2+] | ligand_10080 | Hydrogen molybdate (Molybdi… | H2L | [O]=[Mo](=[O])([OH])[OH] | 1 | 1 | 25 | 0 | solid | 0 |
| metal_125 | Pb^[2+] | ligand_10081 | Hydrogen tungstate (Tungsti… | H2L | [O]=[W](=[O])([OH])[OH] | 1 | 1 | 25 | 0 | solid | 0 |
| metal_125 | Pb^[2+] | ligand_10079 | Hydrogen chromate (Chromic … | H2L | [O]=[Cr](=[O])([OH])[OH] | 1 | 1 | 25 | 0 | solid | 0 |

---

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND s.temperature_c BETWEEN 24 AND 26 AND s.reaction_type LIKE 'M + L = ML' AND (\n  c.ligand_name_SRD LIKE '%ethylenedinitrilotetraaceti%'\n  OR c.ligand_name_SRD LIKE '%diethylenetriaminopentaacetic%'\n  OR c.ligand_name_SRD LIKE '%diethylenetrinitrilopentaaceti%'\n  OR c.ligand_name_SRD LIKE '%oxybis(ethylenenitrilo)tetraacetic%'\n  OR c.ligand_name_SRD LIKE '%cyclohexylenedinitrilotetraacetic%'\n  OR c.ligand_name_SRD LIKE '%n-(2-hydroxyethyl)ethylenediaminetriacetic%'\n  OR c.ligand_name_SRD LIKE '%nitrilotriacetic%'\n  OR c.ligand_name_SRD LIKE '%dimercaptosuccinic%'\n  OR c.ligand_name_SRD LIKE '%succimer%'\n  OR c.ligand_name_SRD LIKE '%dimercapto-1-propanesulfonic%'\n  OR c.ligand_name_SRD LIKE '%dimercaprol%'\n  OR c.ligand_name_SRD LIKE '%2,3-dimercapto-1-propanol%'\n  OR c.ligand_name_SRD LIKE '%penicillamine%'\n  OR c.ligand_name_SRD LIKE '%tetraazacyclododecane%'\n  OR c.ligand_name_SRD LIKE '%DOTA%'\n))",
  "order_by": "s.constant_value DESC",
  "limit": 120
}
```

[summary]
## search_stability — 120 row(s)

### ΔS — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_6229 | N-(Carbamylmethyl)iminodiac… | H2L | NC(=O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |

### logK — 107 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_6229 | N-(Carbamylmethyl)iminodiac… | H2L | NC(=O)CN(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_6229 | N-(Carbamylmethyl)iminodiac… | H2L | NC(=O)CN(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_34 | Co^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_192 | Tm^[3+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_192 | Tm^[3+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_192 | Tm^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_205 | Y^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_31 | Cm^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_6 | Am^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_139 | Pr^[3+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_139 | Pr^[3+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_139 | Pr^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_27 | Ce^[3+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_27 | Ce^[3+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6051 | DL-1-Ethylethylenedinitrilo… | H2L | CCC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6050 | DL-1-Methylethylenedinitril… | H2L | CC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_27 | Ce^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6050 | DL-1-Methylethylenedinitril… | H2L | CC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6051 | DL-1-Ethylethylenedinitrilo… | H2L | CCC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6145 | N-(2-Methylpropyl)iminodiac… | H2L | CC(C)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_192 | Tm^[3+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6051 | DL-1-Ethylethylenedinitrilo… | H2L | CCC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6050 | DL-1-Methylethylenedinitril… | H2L | CC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_55 | Er^[3+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6052 | rac-1,2-Dimethylethylenedin… | H2L | CC(C(C)N(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6052 | rac-1,2-Dimethylethylenedin… | H2L | CC(C(C)N(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6053 | meso-1,2-Dimethylethylenedi… | H2L | CC(C(C)N(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6229 | N-(Carbamylmethyl)iminodiac… | H2L | NC(=O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6051 | DL-1-Ethylethylenedinitrilo… | H2L | CCC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_139 | Pr^[3+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6052 | rac-1,2-Dimethylethylenedin… | H2L | CC(C(C)N(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_68 | H^[+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |

---
