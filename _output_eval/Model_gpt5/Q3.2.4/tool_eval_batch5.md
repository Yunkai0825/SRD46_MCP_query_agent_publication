# Q3.2.4 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "iron",
  "limit": 20
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
  "where": "metal_id = metal_61",
  "limit": 100
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
| Iminodiacetic acid and derivatives | 8 | 0.54% |
| Carboxylic acids hydroxy | 8 | 0.54% |
| Catechols fuchsons | 6 | 0.41% |
| Carboxylic acids diacids S-Se-Te-P-As | 6 | 0.41% |
| Cyclic amines  | 5 | 0.34% |
| Aza-oxa-macrocycles | 5 | 0.34% |
| Organophosphorus and arsenic acids | 4 | 0.27% |
| Aza-oxo-macrocycles | 2 | 0.14% |
| miscellaneous mercaptans | 1 | 0.07% |
| Peptides | 1 | 0.07% |
| Bipyridines | 1 | 0.07% |
| Aniline carboxylic acids | 1 | 0.07% |

---

### Step 5: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "ligand_class_name",
  "where": "metal_id = metal_62",
  "limit": 100
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
| Aza-thia-macrocycles | 4 | 0.6% |
| miscellaneous mercaptans | 3 | 0.45% |
| Phenols salicylic acids | 3 | 0.45% |
| Aniline carboxylic acids | 3 | 0.45% |
| cyclic ketones | 2 | 0.3% |
| Naphtols | 2 | 0.3% |
| Carboxylic acids thio | 2 | 0.3% |
| Carboxylic acids hydroxy | 2 | 0.3% |
| Carboxylic acids diacids hydroxy | 2 | 0.3% |
| Peptides | 1 | 0.15% |
| Carboxylic acids keto | 1 | 0.15% |
| Carboxylic acids | 1 | 0.15% |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 0.2) AND c.ligand_class_name IN ('EDTA and derivatives','NTA and derivatives','Catechols','miscellaneous hydroxamic acids','Inorganic ligands','Phenols salicylic acids','Carboxylic acids diacids','Aminophosphorus acids','Amino Acids'))",
  "order_by": "s.constant_value DESC",
  "limit": 60
}
```

[summary]
## search_stability — 60 row(s)

### ΔS — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_10076 | Hydroxide ion | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9414 | N,N',N''-Tris(2,3-dihydroxy… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9302 | 4-Hydroxybenzaldehyde | HL | O=Cc1ccc(O)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_10163 | Chloride ion | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9402 | N,N',N''-Tris(2,3-dihydroxy… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9410 | 1,3,5-Tris(2,3-dihydroxy-5-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 25 | 0 | *** | 0 |

### logK — 47 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10076 | Hydroxide ion | *** | *** | 2 | 2 | 25 | 0 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9894 | Trimethylenedihydroxamic ac… | H2L | O=C(CCCC(=O)NO)NO | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9910 | Desferriferrioxamin B | H3L | CC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCN | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9901 | N,N'-Di-2-propylpentamethyl… | H2L | CC(C)N(O)C(=O)CCCCCC(=O)N(O)C(C)C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9902 | N,N'-Di-2-propylhexamethyle… | H2L | CC(C)N(O)C(=O)CCCCCCC(=O)N(O)C(C)C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9900 | N,N'-Di-2-propyltetramethyl… | H2L | CC(C)N(O)C(=O)CCCCC(=O)N(O)C(C)C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9906 | Rhodotorulic acid | H2L | CC(=O)N(O)CCCC1NC(=O)C(CCCN(O)C(C)=O)NC1=O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9899 | N,N'-Di-2-propyltrimethylen… | H2L | CC(C)N(O)C(=O)CCCC(=O)N(O)C(C)C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9905 | Trimethylenebis[aminocarbon… | H2L | O=C(NCCCNC(=O)c1cccc(=O)n1O)c1cccc(=O)n1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_10090 | Hydrogen cyanide (Hydrocyan… | HL | C#N | 1 | 1 | 25 | 0 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6371 | 1,4-Bis[2,5,5-tris(carboxym… | H6L | O=C(O)CN(CCN(CC(=O)O)Cc1ccc(CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)cc1)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6021 | N,N-Bis(2-hydroxyethyl)glyc… | HL | O=C(O)CN(CCO)CCO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6038 | N,N'-Bis(2-hydroxy-5-sulfob… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1cc(S(=O)(=O)O)ccc1O)Cc1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5995 | rac-Ethylenediiminobis[(2-h… | H4L | O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6046 | N,N'-Bis(3-hydroxy-6-methyl… | H4L | Cc1ccc(O)c(CN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5998 | meso-Trimethylenebis[2-(2-h… | H4L | Cc1cc(C)c(O)c([C@H](NCCCN[C@@H](C(=O)O)c2cc(C)cc(C)c2O)C(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5997 | rac-Trimethylenebis[2-(2-hy… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6041 | N,N'-Bis(3-hydroxy-5-phosph… | H6L | Cc1ncc(COP(=O)(O)O)c(CN(CCN(CC(=O)O)Cc2c(COP(=O)(O)O)cnc(C)c2O)CC(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5996 | meso-Ethylenediiminobis[(2-… | H4L | O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6045 | N-(2-Hydroxy-3,5-dimethylbe… | H4L | Cc1cc(C)c(O)c(CN(CCN(CC(=O)O)Cc2c(C)c[n+](C)c(C)c2[O-])CC(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6047 | N,N''-Bis(3-hydroxy-6-methy… | H5L | Cc1ccc(O)c(CN(CCN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9912 | Desferriferrioxamin E (Noca… | H3L | O=C1CCC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCN1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6276 | N-(2-Hydroxybenzyl)ethylene… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5994 | N,N'-Bis(2-hydroxyphenyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)c1ccccc1O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8453 | Ethylenebis[imino(2-hydroxy… | H4L | CP(=O)(O)C(NCCNC(c1ccccc1O)P(C)(=O)O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6044 | N-(2-Hydroxybenzyl)-N'-(3-h… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2ccccc2O)CC(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8442 | Ethylenebis(imino(2-hydroxy… | H4L | O=[PH](O)C(NCCNC(c1ccccc1O)[PH](=O)O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8380 | Iminobis(methylenephosphoni… | H4L | O=P(O)(O)CNCP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6042 | N,N'-Bis(3-hydroxy-5-hydrox… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2c(CO)cnc(C)c2O)CC(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9911 | N-Acetyldesferriferrioxamin… | H3L | CC(=O)NCCCCCN(O)C(=O)CCC(=O)NCCCCCN(O)C(=O)CCC(=O)NCCCCCN(O)C(C)=O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6039 | N,N"-Bis(2-hydroxybenzyl)di… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6054 | N,N'-Bis(carboxymethyl)ethy… | H4L | CC(C)N(O)C(=O)CN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9916 | Desferricoprogen | H3L | CC(=O)NC(CCCN(O)C(=O)/C=C(\C)CCO)C(=O)OCC/C(C)=C\C(=O)N(O)CCCC1NC(=O)C(CCCN(O)C(=O)/C=C(\C)CO)NC1=O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9914 | Desferriferrichrysin | *** | *** | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6057 | N,N',N''-Tris(carboxymethyl… | H5L | CC(C)N(O)C(=O)CN(CCN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5911 | L-2-Amino-3-(3-hydroxo-4-ox… | HL | N[C@@H](Cn1ccc(=O)c(O)c1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9909 | 1,13-Dimethyl-3,11,15,23,26… | H3L | CC12COCCCN(O)C(=O)CCOCC(C)(COCCC(=O)N(O)CCCOC1)COCCC(=O)N(O)CCCOC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9913 | Desferriferrichrome | *** | *** | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8434 | Pyridine-2,6-diphosphonic a… | H4L | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9873 | Acetohydroxamic acid | HL | CC(=O)NO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8454 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | COP(=O)(O)C(NCCNC(c1ccccc1O)P(=O)(O)OC)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8455 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | CCOP(=O)(O)C(NCCNC(c1ccccc1O)P(=O)(O)OCC)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9907 | 1,1,1-Tris{[2-{(N-methylhyd… | H3L | CN(O)C(=O)CCOCC(C)(COCCC(=O)N(C)O)COCCC(=O)N(C)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6287 | rac-(1,2-Dimethylethylene)d… | H4L | CC(C(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 0.2) AND c.ligand_class_name IN ('Phenanthrolines','Bipyridines','Pyridines (azines)','Inorganic ligands','EDTA and derivatives','Aliphatic amines','Aminophosphorus acids','Amino Acids','NTA and derivatives'))",
  "order_by": "s.constant_value DESC",
  "limit": 60
}
```

[summary]
## search_stability — 60 row(s)

### ΔS — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8174 | Iminobis(methylene-2-pyridi… | L | c1ccc(CNCc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 42 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 3 | 2 | 25 | 0~0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6193 | N-(Phosphonomethyl)iminodia… | H4L | O=C(O)CN(CC(=O)O)CP(=O)(O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6371 | 1,4-Bis[2,5,5-tris(carboxym… | H6L | O=C(O)CN(CCN(CC(=O)O)Cc1ccc(CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)cc1)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6349 | Dithiobis(ethylenenitrilo)t… | H4L | O=C(O)CN(CCSSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8193 | 5-Methyl-1,10-phenanthroline | L | Cc1cc2cccnc2c2ncccc12 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8156 | 2,2'-Bipyridyl | L | c1ccc(-c2ccccn2)nc1 | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8176 | 2-(2-Pyridylmethylenehydraz… | L | C(=N/Nc1ccccn1)\c1ccccn1 | 2 | 1 | 20~25 | 0~0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6287 | rac-(1,2-Dimethylethylene)d… | H4L | CC(C(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_10090 | Hydrogen cyanide (Hydrocyan… | HL | C#N | 1 | 1 | 25 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8174 | Iminobis(methylene-2-pyridi… | L | c1ccc(CNCc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8196 | 5,6-Dimethyl-1,10-phenanthr… | L | Cc1c(C)c2cccnc2c2ncccc12 | 1 | 1 | 25 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8199 | 5-Chloro-1,10-phenanthroline | L | Clc1cc2cccnc2c2ncccc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8201 | 5-Nitro-1,10-phenanthroline | L | O=[N+]([O-])c1cc2cccnc2c2ncccc12 | 1 | 1 | 25 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6366 | Triethylenetetranitrilohexa… | H6L | O=C(O)CN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8360 | Amino(phenyl)methylenedipho… | H4L | NC(c1ccccc1)(P(=O)(O)O)P(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8434 | Pyridine-2,6-diphosphonic a… | H4L | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6288 | meso-(1,2-Dimethylethylene)… | H4L | C[C@H]([C@H](C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6292 | DL-Ethylenedinitrilo-N,N'-d… | H4L | CC(C(=O)O)N(CCN(CC(=O)O)C(C)C(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6253 | N-(2-Aminoethyl)iminodiacet… | H2L | NCCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8412 | Nitrilotris(methylenephosph… | H6L | O=P(O)(O)CN(CP(=O)(O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8427 | N-(2-Hydroxyethyl)ethylened… | H6L | O=P(O)(O)CN(CCO)CCN(CP(=O)(O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8072 | 4-(2-Pyridyl)-1,3-thiazole | L | c1ccc(-c2cscn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8172 | 6,6'-Bis(aminomethyl)-2,2'-… | L | NCc1cccc(-c2cccc(CN)n2)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6056 | N,N'-Bis(2-pyridylmethyl)et… | H2L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccn1)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6248 | N-(2-Mercaptoethyl)iminodia… | H3L | O=C(O)CN(CCS)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8198 | 2-Chloro-1,10-phenanthroline | L | Clc1ccc2ccc3cccnc3c2n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5937 | N-(Phosphonomethyl)glycine … | H3L | O=C(O)CNCP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6316 | Octamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6315 | Hexamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |

---
