# Q5.1.6 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Scandium, Yttrium, Lanthanum, Cerium, Praseodymium, Neodymium, Promethium, Samarium, Europium, Gadolinium, Terbium, Dysprosium, Holmium, Erbium, Thulium, Ytterbium, Lutetium",
  "limit": 200
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
  "symbol": "Sc, Y, La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu",
  "limit": 200
}
```

[summary]
## search_metals

*(no results)*

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "EDTA, ethylenediaminetetraacetic",
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
  "where": "((c.metal_name_SRD LIKE 'Lanthanum%' OR c.metal_name_SRD LIKE 'Cerium%' OR c.metal_name_SRD LIKE 'Praseodymium%' OR c.metal_name_SRD LIKE 'Neodymium%' OR c.metal_name_SRD LIKE 'Samarium%' OR c.metal_name_SRD LIKE 'Europium%' OR c.metal_name_SRD LIKE 'Gadolinium%' OR c.metal_name_SRD LIKE 'Terbium%' OR c.metal_name_SRD LIKE 'Dysprosium%' OR c.metal_name_SRD LIKE 'Holmium%' OR c.metal_name_SRD LIKE 'Erbium%' OR c.metal_name_SRD LIKE 'Thulium%' OR c.metal_name_SRD LIKE 'Ytterbium%' OR c.metal_name_SRD LIKE 'Lutetium%' OR c.metal_name_SRD LIKE 'Yttrium%') AND c.metal_name_SRD LIKE '%(III)%' AND c.ligand_name_SRD LIKE '%ethylenediaminetetraacet%' AND c.beta_definition_name = 'M + L = ML' AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "c.metal_name_SRD ASC, s.temperature_c ASC",
  "limit": 500
}
```

[summary]
## search_stability

*(no results)*

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "((c.metal_name_SRD LIKE 'Lanthanum%' OR c.metal_name_SRD LIKE 'Cerium%' OR c.metal_name_SRD LIKE 'Praseodymium%' OR c.metal_name_SRD LIKE 'Neodymium%' OR c.metal_name_SRD LIKE 'Samarium%' OR c.metal_name_SRD LIKE 'Europium%' OR c.metal_name_SRD LIKE 'Gadolinium%' OR c.metal_name_SRD LIKE 'Terbium%' OR c.metal_name_SRD LIKE 'Dysprosium%' OR c.metal_name_SRD LIKE 'Holmium%' OR c.metal_name_SRD LIKE 'Erbium%' OR c.metal_name_SRD LIKE 'Thulium%' OR c.metal_name_SRD LIKE 'Ytterbium%' OR c.metal_name_SRD LIKE 'Lutetium%' OR c.metal_name_SRD LIKE 'Yttrium%') AND c.metal_name_SRD LIKE '%(III)%' AND c.ligand_name_SRD LIKE '%fluorid%' AND c.beta_definition_name = 'M + L = ML' AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "c.metal_name_SRD ASC, s.temperature_c ASC",
  "limit": 500
}
```

[summary]
## search_stability — 200 row(s)

### logK — 55 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_5 | Al^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 15 | 5 | 25 | 0~1 | solid | 4 |
| metal_19 | Be^[2+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 15 | 6 | 20~25 | 0.5~3 | *** | 4 |
| metal_26 | Cd^[2+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 6 | 1 | 25 | 0~3 | *** | 6 |
| metal_27 | Ce^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 6 | 2 | 25 | 0~1 | solid | 4 |
| metal_33 | Co^[2+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 6 | 1 | 25 | 0~3 | *** | 6 |
| metal_6 | Am^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 5 | 3 | 25 | 0~1 | solid | 3 |
| metal_15 | B^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 4 | 4 | 25 | 1 | *** | 1 |
| metal_1 | Ac^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 3 | 3 | 25 | 0.5 | *** | 1 |
| metal_2 | Ag^[+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 3 | 1 | 25 | 0~1 | *** | 3 |
| metal_37 | Cr^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 3 | 2 | 25 | 0~0.5 | *** | 2 |
| metal_2 | Ag^[+] | ligand_7546 | Perhydro-1,4-oxazine (Morph… | L | C1COCCN1 | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_2 | Ag^[+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_2 | Ag^[+] | ligand_7639 | 4,10,16,22,27,32-Hexaoxa-1,… | L | C1CN2CCOCCN(CCO1)CCOCCN1CCOCCN(CCOCC1)CCOCC2 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 2 | 2 | 25 | 0~1 | solid | 2 |
| metal_25 | Ca^[2+] | ligand_7600 | 4,7,13,16,21-Pentaoxa-1,10-… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCC2 | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_25 | Ca^[2+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 2 | 2 | 25 | 0~1 | solid | 2 |
| metal_26 | Cd^[2+] | ligand_7569 | 1-Oxa-4,7-diazacyclononane … | L | C1CNCCOCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_26 | Cd^[2+] | ligand_7639 | 4,10,16,22,27,32-Hexaoxa-1,… | L | C1CN2CCOCCN(CCO1)CCOCCN1CCOCCN(CCOCC1)CCOCC2 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7569 | 1-Oxa-4,7-diazacyclononane … | L | C1CNCCOCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7639 | 4,10,16,22,27,32-Hexaoxa-1,… | L | C1CN2CCOCCN(CCO1)CCOCCN1CCOCCN(CCOCC1)CCOCC2 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_7596 | 4,7,13,18-Tetraoxa-1,10-dia… | L | C1COCCN2CCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_7600 | 4,7,13,16,21-Pentaoxa-1,10-… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_7596 | 4,7,13,18-Tetraoxa-1,10-dia… | L | C1COCCN2CCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_7600 | 4,7,13,16,21-Pentaoxa-1,10-… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_10 | As^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 22 | 1 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_7600 | 4,7,13,16,21-Pentaoxa-1,10-… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_7638 | 4,10,16,22,27,32-Hexaoxa-1,… | L | C1CN2CCOCCN3CCOCCN(CCO1)CCOCCN(CCOCC2)CCOCC3 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_7639 | 4,10,16,22,27,32-Hexaoxa-1,… | L | C1CN2CCOCCN(CCO1)CCOCCN1CCOCCN(CCOCC1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_21 | Bi^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 30 | 2 | *** | 1 |
| metal_22 | Bk^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_7596 | 4,7,13,18-Tetraoxa-1,10-dia… | L | C1COCCN2CCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_7638 | 4,10,16,22,27,32-Hexaoxa-1,… | L | C1CN2CCOCCN3CCOCCN(CCO1)CCOCCN(CCOCC2)CCOCC3 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_7639 | 4,10,16,22,27,32-Hexaoxa-1,… | L | C1CN2CCOCCN(CCO1)CCOCCN1CCOCCN(CCOCC1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7596 | 4,7,13,18-Tetraoxa-1,10-dia… | L | C1COCCN2CCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7600 | 4,7,13,16,21-Pentaoxa-1,10-… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_29 | Cf^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 1 | *** | 1 |
| metal_31 | Cm^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7596 | 4,7,13,18-Tetraoxa-1,10-dia… | L | C1COCCN2CCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7600 | 4,7,13,16,21-Pentaoxa-1,10-… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_37 | Cr^[3+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_37 | Cr^[3+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_37 | Cr^[3+] | ligand_7596 | 4,7,13,18-Tetraoxa-1,10-dia… | L | C1COCCN2CCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_37 | Cr^[3+] | ligand_7600 | 4,7,13,16,21-Pentaoxa-1,10-… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 18 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_5 | Al^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 11 | 4 | 25~35 | 0.1~1 | *** | 0 |
| metal_19 | Be^[2+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 4 | 4 | 25 | 1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 4 | 1 | 15~35 | 1~3 | *** | 0 |
| metal_6 | Am^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 3 | 2 | 25 | 0.1~1 | *** | 0 |
| metal_2 | Ag^[+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 2 | 2 | 25 | 0~1 | solid | 0 |
| metal_25 | Ca^[2+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 2 | 2 | 25 | 0~1 | solid | 0 |
| metal_33 | Co^[2+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 2 | 1 | 25 | 0.5~3 | *** | 0 |
| metal_2 | Ag^[+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_7600 | 4,7,13,16,21-Pentaoxa-1,10-… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_22 | Bk^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_7596 | 4,7,13,18-Tetraoxa-1,10-dia… | L | C1COCCN2CCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_7600 | 4,7,13,16,21-Pentaoxa-1,10-… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_29 | Cf^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 1 | *** | 0 |
| metal_31 | Cm^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 1 | *** | 0 |
| metal_37 | Cr^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 0.5 | *** | 0 |

### ΔS — 18 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_5 | Al^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 8 | 4 | 25 | 0.1~1 | *** | 0 |
| metal_19 | Be^[2+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 4 | 4 | 25 | 1 | *** | 0 |
| metal_6 | Am^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 3 | 2 | 25 | 0.1~1 | *** | 0 |
| metal_2 | Ag^[+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 2 | 2 | 25 | 0~1 | solid | 0 |
| metal_25 | Ca^[2+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 2 | 2 | 25 | 0~1 | solid | 0 |
| metal_26 | Cd^[2+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 2 | 1 | 25 | 0.5~3 | *** | 0 |
| metal_2 | Ag^[+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_7600 | 4,7,13,16,21-Pentaoxa-1,10-… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_22 | Bk^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_7596 | 4,7,13,18-Tetraoxa-1,10-dia… | L | C1COCCN2CCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_7600 | 4,7,13,16,21-Pentaoxa-1,10-… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_29 | Cf^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 1 | *** | 0 |
| metal_31 | Cm^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 1 | *** | 0 |
| metal_37 | Cr^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 0.5 | *** | 0 |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "((c.metal_name_SRD LIKE 'Lanthanum%' OR c.metal_name_SRD LIKE 'Cerium%' OR c.metal_name_SRD LIKE 'Praseodymium%' OR c.metal_name_SRD LIKE 'Neodymium%' OR c.metal_name_SRD LIKE 'Samarium%' OR c.metal_name_SRD LIKE 'Europium%' OR c.metal_name_SRD LIKE 'Gadolinium%' OR c.metal_name_SRD LIKE 'Terbium%' OR c.metal_name_SRD LIKE 'Dysprosium%' OR c.metal_name_SRD LIKE 'Holmium%' OR c.metal_name_SRD LIKE 'Erbium%' OR c.metal_name_SRD LIKE 'Thulium%' OR c.metal_name_SRD LIKE 'Ytterbium%' OR c.metal_name_SRD LIKE 'Lutetium%' OR c.metal_name_SRD LIKE 'Yttrium%') AND c.metal_name_SRD LIKE '%(III)%' AND c.ligand_name_SRD LIKE '%oxalat%' AND c.beta_definition_name = 'M + L = ML' AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "c.metal_name_SRD ASC, s.temperature_c ASC",
  "limit": 500
}
```

[summary]
## search_stability

*(no results)*

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "((c.metal_name_SRD LIKE 'Lanthanum%' OR c.metal_name_SRD LIKE 'Cerium%' OR c.metal_name_SRD LIKE 'Praseodymium%' OR c.metal_name_SRD LIKE 'Neodymium%' OR c.metal_name_SRD LIKE 'Samarium%' OR c.metal_name_SRD LIKE 'Europium%' OR c.metal_name_SRD LIKE 'Gadolinium%' OR c.metal_name_SRD LIKE 'Terbium%' OR c.metal_name_SRD LIKE 'Dysprosium%' OR c.metal_name_SRD LIKE 'Holmium%' OR c.metal_name_SRD LIKE 'Erbium%' OR c.metal_name_SRD LIKE 'Thulium%' OR c.metal_name_SRD LIKE 'Ytterbium%' OR c.metal_name_SRD LIKE 'Lutetium%' OR c.metal_name_SRD LIKE 'Yttrium%') AND c.metal_name_SRD LIKE '%(III)%' AND c.ligand_name_SRD LIKE '%carbonat%' AND c.beta_definition_name = 'M + L = ML' AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "c.metal_name_SRD ASC, s.temperature_c ASC",
  "limit": 500
}
```

[summary]
## search_stability — 200 row(s)

### logK — 31 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_5 | Al^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 16 | 9 | 25 | 0.1~1 | *** | 4 |
| metal_6 | Am^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 15 | 3 | 20~25 | 0.1~9 | *** | 7 |
| metal_5 | Al^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 10 | 4 | 25 | 0~1 | *** | 4 |
| metal_6 | Am^[3+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 10 | 4 | 25 | 0~1 | solid | 3 |
| metal_5 | Al^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 9 | 3 | 25 | 0~1 | *** | 4 |
| metal_19 | Be^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 8 | 4 | 25 | 0.1~1 | *** | 3 |
| metal_19 | Be^[2+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 8 | 7 | 25 | 0.5~1 | *** | 2 |
| metal_5 | Al^[3+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 7 | 4 | 25 | 0.1~0.5 | *** | 2 |
| metal_19 | Be^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 7 | 7 | 25 | 3 | *** | 1 |
| metal_2 | Ag^[+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 6 | 3 | 25 | 0~3 | solid | 2 |
| metal_5 | Al^[3+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 6 | 2 | 25 | 0.1~3 | *** | 3 |
| metal_18 | Ba^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 6 | 3 | 25 | 0~1 | solid | 4 |
| metal_19 | Be^[2+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 6 | 4 | 25 | 0.1~0.5 | *** | 2 |
| metal_6 | Am^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 5 | 3 | 20~25 | 0.5~2 | *** | 2 |
| metal_1 | Ac^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 4 | 2 | 25 | 0.1~1 | *** | 2 |
| metal_6 | Am^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 4 | 3 | 20~25 | 0.5~2 | *** | 2 |
| metal_15 | B^[3+] | ligand_10143 | Hydrogen peroxide | H2L | OO | 3 | 2 | 25 | 0~0.5 | *** | 2 |
| metal_18 | Ba^[2+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_2 | Ag^[+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 2 | 2 | 25 | 3 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 18~20 | 0~0.1 | solid | 2 |
| metal_18 | Ba^[2+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_18 | Ba^[2+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_18 | Ba^[2+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_19 | Be^[2+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 1 | 1 | 25 | 0 | solid | 1 |
| metal_15 | B^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_15 | B^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_15 | B^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_22 | Bk^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 2 | *** | 1 |
| metal_22 | Bk^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 1 | 1 | 25 | 2 | *** | 1 |

### ΔH — 11 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_19 | Be^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 4 | 4 | 25 | 0.5 | *** | 0 |
| metal_19 | Be^[2+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 4 | 4 | 25 | 0.5 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 3 | 3 | 25 | 0 | solid | 0 |
| metal_19 | Be^[2+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 3 | 3 | 25 | 0.5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 0 | *** | 0 |
| metal_5 | Al^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_5 | Al^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 2 | 2 | 25 | 0 | *** | 0 |
| metal_5 | Al^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_6 | Am^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_6 | Am^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 1 | 1 | 25 | 2 | *** | 0 |
| metal_22 | Bk^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 1 | 1 | 25 | 2 | *** | 0 |

### ΔS — 11 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_19 | Be^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 4 | 4 | 25 | 0.5 | *** | 0 |
| metal_19 | Be^[2+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 4 | 4 | 25 | 0.5 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 3 | 3 | 25 | 0 | solid | 0 |
| metal_19 | Be^[2+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 3 | 3 | 25 | 0.5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 0 | *** | 0 |
| metal_5 | Al^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_5 | Al^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 2 | 2 | 25 | 0 | *** | 0 |
| metal_5 | Al^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_6 | Am^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_6 | Am^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 1 | 1 | 25 | 2 | *** | 0 |
| metal_22 | Bk^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 1 | 1 | 25 | 2 | *** | 0 |

---
