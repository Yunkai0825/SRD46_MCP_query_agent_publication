# Q4.3 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "symbol": "Cu",
  "limit": 20
}
```

[summary]
## search_metals — 3 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_41 | Cu^[2+] | Cu | 2 | ✓ | [Cu+2] | InChI=1S/Cu/q+2 | beta_totN_264 | ligand_totN_1951 | vlm_totN_8963 |
| metal_42 | Cu^[+] | Cu | 1 | ✓ | [Cu+] | InChI=1S/Cu/q+1 | beta_totN_32 | ligand_totN_117 | vlm_totN_285 |
| metal_43 | Cu^[3+] | Cu | 3 | ✓ | [Cu+3] | InChI=1S/Cu/q+3 | beta_totN_4 | ligand_totN_8 | vlm_totN_10 |

---

### Step 3: `search_metals`
**Args:**
```json
{
  "symbol": "Ni",
  "limit": 20
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_112 | Ni^[2+] | Ni | 2 | ✓ | [Ni+2] | InChI=1S/Ni/q+2 | beta_totN_149 | ligand_totN_1369 | vlm_totN_5325 |
| metal_113 | Ni^[3+] | Ni | 3 | ✓ | [Ni+3] | InChI=1S/Ni/q+3 | beta_totN_5 | ligand_totN_4 | vlm_totN_7 |

---

### Step 4: `search_metals`
**Args:**
```json
{
  "symbol": "Zn",
  "limit": 20
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine",
  "limit": 50
}
```

[summary]
## search_ligands — 50 result(s)

**stats:** 105 SQL matches · showing 50 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5948 | N-(2-Aminoethyl)glycine (Ethylenediamine m… (EDMA) | HL | Amino Acids | 30 | `NCCNCC(=O)O` | (-inf, H3L, -1.9, H2L, 6.67, HL, 9.84, L, +inf) |
| ligand_6253 | N-(2-Aminoeth… (Ethylenediamine-N,N-diacetic acid) | H2L | NTA and derivatives | 39 | `NCCN(CC(=O)O)CC(=O)O` | (-inf, H2L, 5.53, HL, 10.87, L, +inf) |
| ligand_7029 | Ethylenediamine | L | Aliphatic amines | 310 | `NCCN` | (-inf, H2L, 7.11, HL, 9.92, L, +inf) |
| ligand_7030 | DL-Methylethylenediamine (1,2-Propylenediami… (pn) | L | Aliphatic amines | 86 | `CC(N)CN` | (-inf, H2L, 6.85, HL, 9.81, L, +inf) |
| ligand_7031 | DL-Ethylethylenediamine (1,2-Butylenediamine) | L | Aliphatic amines | 19 | `CCC(N)CN` | (-inf, H2L, 6.65, HL, 9.66, L, +inf) |
| ligand_7032 | DL-(2-Methyl-2-propyl)et… (t-Butylethylenediamine) | L | Aliphatic amines | 2 | `CC(C)(C)C(N)CN` | (-inf, H2L, 6.26, HL, 9.78, L, +inf) |
| ligand_7033 | 1,1-Dimethylethylenediamine | L | Aliphatic amines | 37 | `CC(C)(N)CN` | (-inf, H2L, 6.46, HL, 9.75, L, +inf) |
| ligand_7034 | DL-1,2-Dimethylethylened… (DL-2,3-Butylenediamine) | L | Aliphatic amines | 46 | `CC(N)C(C)N` | (-inf, H2L, 6.6, HL, 9.7, L, +inf) |
| ligand_7035 | meso-1,2-Dimethylethyl… (meso-2,3-Butylenediamine) | L | Aliphatic amines | 53 | `C[C@H](N)[C@@H](C)N` | (-inf, H2L, 6.63, HL, 9.76, L, +inf) |
| ligand_7036 | 1,1,2,2-Tetramethylethylenediamine | L | Aliphatic amines | 15 | `CC(C)(N)C(C)(C)N` | (-inf, H2L, 6.35, HL, 9.93, L, +inf) |
| ligand_7037 | Trimethylenediamine (1,3-Propylenediamine) | L | Aliphatic amines | 112 | `NCCCN` | (-inf, H2L, 8.78, HL, 10.54, L, +inf) |
| ligand_7038 | DL-1-Methyltrimethylenediam… (1,3-Butylenediamine) | L | Aliphatic amines | 30 | `CC(N)CCN` | (-inf, H2L, 8.68, HL, 10.55, L, +inf) |
| ligand_7039 | 2,2-Dimethylt… (2,2-Dimethyl-1,3-propylenediamine) | L | Aliphatic amines | 31 | `CC(C)(CN)CN` | (-inf, H2L, 8.18, HL, 10.22, L, +inf) |
| ligand_7040 | 2-Methylenetri… (2-Methylene-1,3-propylenediamine) | L | Aliphatic amines | 15 | `C=C(CN)CN` | (-inf, H2L, 8.33, HL, 10.09, L, +inf) |
| ligand_7041 | Tetramethylenediamine (1,4-Butylened… (Putrescine) | L | Aliphatic amines | 42 | `NCCCCN` | (-inf, H2L, 9.46, HL, 10.72, L, +inf) |
| ligand_7042 | Pentamethylenediamine (Cadaverine) | L | Aliphatic amines | 24 | `NCCCCCN` | (-inf, H2L, 9.83, HL, 10.9, L, +inf) |
| ligand_7043 | Hexamethylenediamine | L | Aliphatic amines | 16 | `NCCCCCCN` | (-inf, H2L, 10.07, HL, 10.95, L, +inf) |
| ligand_7044 | Octamethylenediamine | L | Aliphatic amines | 8 | `NCCCCCCCCN` | (-inf, H2L, 10.17, HL, 10.99, L, +inf) |
| ligand_7045 | Decamethylenediamine | L | Aliphatic amines | 8 | `NCCCCCCCCCCN` | (-inf, H2L, 10.25, HL, 10.97, L, +inf) |
| ligand_7052 | DL-1-Phenylethylenediamine | L | Aliphatic amines | 12 | `NCC(N)c1ccccc1` | (-inf, H2L, 6.01, HL, 8.85, L, +inf) |
| ligand_7059 | 1,3-Diamino-2-prop… (2-Hydroxytrimethylenediamine) | L | Aliphatic amines | 54 | `NCC(O)CN` | (-inf, H2L, 8.02, HL, 9.56, L, +inf) |
| ligand_7066 | N,N'-Diglycylethylenediamine (DGEN) | L | Aliphatic amines | 30 | `NCC(=O)NCCNC(=O)CN` | (-inf, H2L, 7.48, HL, 8.22, L, +inf) |
| ligand_7069 | N,N'-Di-L-alanylethylenediamine (DAEN) | L | Aliphatic amines | 7 | `C[C@H](N)C(=O)NCCNC(=O)[C@H](C)N` | (-inf, H2L, 7.3, HL, 8.34, L, +inf) |
| ligand_7072 | N,N'-Diglycyltrimethylenediamine | L | Aliphatic amines | 9 | `NCC(=O)NCCCNC(=O)CN` | (-inf, H2L, 7.72, HL, 8.4, L, +inf) |
| ligand_7073 | N,N'-Diglycyltetramethylenediamine | L | Aliphatic amines | 6 | `NCC(=O)NCCCCNC(=O)CN` | (-inf, H2L, 7.78, HL, 8.41, L, +inf) |
| ligand_7074 | N,N'-Diglycylpentamethylenediamine | L | Aliphatic amines | 6 | `NCC(=O)NCCCCCNC(=O)CN` | (-inf, H2L, 7.73, HL, 8.36, L, +inf) |
| ligand_7075 | N,N'-Diglycylhexamethylenediamine | L | Aliphatic amines | 6 | `NCC(=O)NCCCCCCNC(=O)CN` | (-inf, H2L, 7.78, HL, 8.41, L, +inf) |
| ligand_7076 | N,N'-Diglycyloctamethylenediamine | L | Aliphatic amines | 4 | `NCC(=O)NCCCCCCCCNC(=O)CN` | (-inf, H2L, 7.75, HL, 8.41, L, +inf) |
| ligand_7161 | N-Methylethylenediamine | L | Aliphatic amines seconda… | 79 | `CNCCN` | (-inf, H2L, 7.04, HL, 10.11, L, +inf) |
| ligand_7162 | N-Ethylethylenediamine | L | Aliphatic amines seconda… | 31 | `CCNCCN` | (-inf, H2L, 7.1, HL, 10.16, L, +inf) |
| ligand_7163 | N-Propylethylenediamine | L | Aliphatic amines seconda… | 7 | `CCCNCCN` | (-inf, H2L, -7.39, HL, 10.19, L, +inf) |
| ligand_7164 | N-2-Propylethylenedi… (N-Isopropylethylenediamine) | L | Aliphatic amines seconda… | 10 | `CC(C)NCCN` | (-inf, H2L, 7.11, HL, 10.19, L, +inf) |
| ligand_7165 | N-Butylethylenediamine | L | Aliphatic amines seconda… | 7 | `CCCCNCCN` | (-inf, H2L, -7.38, HL, 10.15, L, +inf) |
| ligand_7166 | 2-(2-Pro… (N-2-Propyl-2,2-dimethylethylenediamine) | L | Aliphatic amines seconda… | 24 | `CC(C)NCC(C)(C)N` | (-inf, H2L, 6.6, HL, 10.07, L, +inf) |
| ligand_7167 | N-Methyltrimethylenediamine | L | Aliphatic amines seconda… | 10 | `CNCCCN` | (-inf, H2L, 8.74, HL, 10.62, L, +inf) |
| ligand_7168 | 2-(Cyc… (N-Cyclohexyl-2,2-dimethylethylenediamine) | L | Aliphatic amines seconda… | 6 | `CC(C)(N)CNC1CCCCC1` | (-inf, H2L, 6.77, HL, 10.18, L, +inf) |
| ligand_7169 | N-Benzylethylenediamine | L | Aliphatic amines seconda… | 4 | `NCCNCc1ccccc1` | (-inf, H2L, 6.48, HL, 9.41, L, +inf) |
| ligand_7170 | N-(4-Methylbenzyl)ethylenediamine | L | Aliphatic amines seconda… | 4 | `Cc1ccc(CNCCN)cc1` | (-inf, H2L, 6.51, HL, 9.41, L, +inf) |
| ligand_7171 | N-(2-Phenylethyl)ethylenediamine | L | Aliphatic amines seconda… | 4 | `NCCNCCc1ccccc1` | (-inf, H2L, 6.59, HL, 9.44, L, +inf) |
| ligand_7172 | N,N'-Dimethylethylenediamine | L | Aliphatic amines seconda… | 83 | `CNCCNC` | (-inf, H2L, 7.04, HL, 10.05, L, +inf) |
| ligand_7173 | N,N'-Diethylethylenediamine | L | Aliphatic amines seconda… | 45 | `CCNCCNCC` | (-inf, H2L, 7.28, HL, 10.16, L, +inf) |
| ligand_7174 | N,N'-Di-2-propylethylenediamine | L | Aliphatic amines seconda… | 2 | `CC(C)NCCNC(C)C` | (-inf, H2L, 7.44, HL, 10.25, L, +inf) |
| ligand_7175 | N,N'-Dipropylethylenediamine | L | Aliphatic amines seconda… | 6 | `CCCNCCNCCC` | (-inf, H2L, 7.38, HL, 10.12, L, +inf) |
| ligand_7176 | N,N'-Dibutylethylenediamine | L | Aliphatic amines seconda… | 5 | `CCCCNCCNCCCC` | (-inf, H2L, 7.31, HL, 10.04, L, +inf) |
| ligand_7177 | N,N'-Dimethyltrimethylenediamine | L | Aliphatic amines seconda… | 12 | `CNCCCNC` | (-inf, H2L, 8.81, HL, 10.64, L, +inf) |
| ligand_7178 | N,N'-Dimethyl-2-methylenetrimethylenediamine | L | Aliphatic amines seconda… | 2 | `C=C(CNC)CNC` | (-inf, H2L, 8.39, HL, 10.42, L, +inf) |
| ligand_7179 | N-(2-Hydroxybenzyl)ethylenediamine (HBEN) | HL | Aliphatic amines seconda… | 3 | `NCCNCc1ccccc1O` | (-inf, H3L, 6.89, H2L, 9.49, HL, 9.49, L, +inf) |
| ligand_7180 | Ethylenebis(iminomethylene-2-phenol) [N,N'-Bis(2-… | H2L | Aliphatic amines seconda… | 7 | `Oc1ccccc1CNCCNCc1ccccc1O` | (-inf, H4L, 6.17, H3L, 8.37, H2L, 9.8, HL, 10.5, L, +inf) |
| ligand_7181 | 2-(2-Aminoethylamino)ethanol [N-(2-Hydroxyethyl)e… | L | Aliphatic amines seconda… | 68 | `NCCNCCO` | (-inf, H2L, 6.55, HL, 9.56, L, +inf) |
| ligand_7182 | DL-1-(2-Aminoethylamino)-2-propanol [N-(2-Hydroxy… | L | Aliphatic amines seconda… | 6 | `CC(O)CNCCN` | (-inf, H2L, 6.78, HL, 9.62, L, +inf) |

### Functional groups across all SQL matches (85 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 58 | 68% |
| secondary_amine | 43 | 51% |
| tertiary_amine | 23 | 27% |
| hydroxyl | 14 | 16% |
| aromatic_ring | 13 | 15% |
| amide | 7 | 8% |
| phosphonate | 4 | 5% |
| thioether | 4 | 5% |
| phenol | 3 | 4% |
| pyridine | 3 | 4% |
| carboxyl | 2 | 2% |
| sulfonate | 1 | 1% |
| thiol | 1 | 1% |

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "ammonia",
  "limit": 50
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10103 | Ammonia | L | Inorganic ligands | 447 | `N` | (-inf, HL, 9.26, L, +inf) |

---

### Step 7: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_41",
  "ligand_id": "ligand_7029"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 2 species

### Cu^[2+] + Ethylenediamine
**metal_id:** metal_41 | **ligand_id:** ligand_7029 | **ligand_def_HxL:** L  
**entries:** 34 | **species:** 2 | **vlm_count:** 34

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 17 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 17 |

**vlm_ids:** vlm_122410, vlm_122411, vlm_122412, vlm_122413, vlm_122414, … vlm_122441, vlm_122442, vlm_122443 (34 listed)

**equilibrium_maps:** 9 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_9598 | 2 | 1 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_9599 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_9600 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_9601 | 2 | 1 | 31~41 °C | 0~0.3 M |
| ref_eq_net_9602 | 2 | 1 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_9603 | 2 | 1 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_9604 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_9605 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_9606 | 2 | 1 | 19~29 °C | -0.15~0.15 M |

---

### Step 8: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_41",
  "ligand_id": "ligand_10103"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 4 species

### Cu^[2+] + Ammonia
**metal_id:** metal_41 | **ligand_id:** ligand_10103 | **ligand_def_HxL:** L  
**entries:** 49 | **species:** 4 | **vlm_count:** 49

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 13 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 12 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 12 |
| beta_def_894 | [ML<sub>4</sub>]/[M][L]<sup>4</sup> | [M] + [L]^4 <=> [ML4] | [ML4](aqueous), [M](aqueous), [L](aqueous) | 12 |

**vlm_ids:** vlm_173242, vlm_173243, vlm_173244, vlm_173245, vlm_173246, … vlm_173288, vlm_173289, vlm_173290 (49 listed)

**equilibrium_maps:** 5 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28241 | 4 | 6 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28242 | 4 | 6 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28243 | 4 | 6 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_28244 | 4 | 6 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_28245 | 1 | 0 | 19~29 °C | -0.15~0.15 M |

---

### Step 9: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_112",
  "ligand_id": "ligand_7029"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 3 species

### Ni^[2+] + Ethylenediamine
**metal_id:** metal_112 | **ligand_id:** ligand_7029 | **ligand_def_HxL:** L  
**entries:** 45 | **species:** 3 | **vlm_count:** 45

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 15 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 15 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 15 |

**vlm_ids:** vlm_122365, vlm_122366, vlm_122367, vlm_122368, vlm_122369, … vlm_122407, vlm_122408, vlm_122409 (45 listed)

**equilibrium_maps:** 7 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_9591 | 3 | 3 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_9592 | 3 | 3 | 31~41 °C | 0~0.3 M |
| ref_eq_net_9593 | 3 | 3 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_9594 | 3 | 3 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_9595 | 3 | 3 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_9596 | 3 | 3 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_9597 | 3 | 3 | 19~29 °C | -0.15~0.15 M |

---

### Step 10: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_112",
  "ligand_id": "ligand_10103"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 6 species

### Ni^[2+] + Ammonia
**metal_id:** metal_112 | **ligand_id:** ligand_10103 | **ligand_def_HxL:** L  
**entries:** 60 | **species:** 6 | **vlm_count:** 60

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 11 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 13 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 10 |
| beta_def_894 | [ML<sub>4</sub>]/[M][L]<sup>4</sup> | [M] + [L]^4 <=> [ML4] | [ML4](aqueous), [M](aqueous), [L](aqueous) | 10 |
| beta_def_903 | [ML<sub>5</sub>]/[M][L]<sup>5</sup> | [M] + [L]^5 <=> [ML5] | [ML5](aqueous), [M](aqueous), [L](aqueous) | 8 |
| beta_def_907 | [ML<sub>6</sub>]/[M][L]<sup>6</sup> | [M] + [L]^6 <=> [ML6] | [ML6](aqueous), [M](aqueous), [L](aqueous) | 8 |

**vlm_ids:** vlm_173182, vlm_173183, vlm_173184, vlm_173185, vlm_173186, … vlm_173239, vlm_173240, vlm_173241 (60 listed)

**equilibrium_maps:** 5 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28236 | 6 | 15 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28237 | 6 | 15 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_28238 | 4 | 6 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28239 | 2 | 1 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_28240 | 1 | 0 | 19~29 °C | 2.85~3.15 M |

---

### Step 11: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_208",
  "ligand_id": "ligand_7029"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 3 species

### Zn^[2+] + Ethylenediamine
**metal_id:** metal_208 | **ligand_id:** ligand_7029 | **ligand_def_HxL:** L  
**entries:** 36 | **species:** 3 | **vlm_count:** 36

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 12 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 12 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 12 |

**vlm_ids:** vlm_122508, vlm_122509, vlm_122510, vlm_122511, vlm_122512, … vlm_122541, vlm_122542, vlm_122543 (36 listed)

**equilibrium_maps:** 8 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_9625 | 3 | 3 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_9626 | 3 | 3 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_9627 | 3 | 3 | 31~41 °C | 0~0.3 M |
| ref_eq_net_9628 | 3 | 3 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_9629 | 3 | 3 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_9630 | 3 | 3 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_9631 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_9632 | 2 | 1 | 19~29 °C | 2.85~3.15 M |

---

### Step 12: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_208",
  "ligand_id": "ligand_10103"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 4 species

### Zn^[2+] + Ammonia
**metal_id:** metal_208 | **ligand_id:** ligand_10103 | **ligand_def_HxL:** L  
**entries:** 21 | **species:** 4 | **vlm_count:** 21

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 6 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 5 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 5 |
| beta_def_894 | [ML<sub>4</sub>]/[M][L]<sup>4</sup> | [M] + [L]^4 <=> [ML4] | [ML4](aqueous), [M](aqueous), [L](aqueous) | 5 |

**vlm_ids:** vlm_173394, vlm_173395, vlm_173396, vlm_173397, vlm_173398, … vlm_173412, vlm_173413, vlm_173414 (21 listed)

**equilibrium_maps:** 4 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28282 | 4 | 6 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28283 | 4 | 6 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28284 | 4 | 6 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_28285 | 1 | 0 | 19~29 °C | -0.15~0.15 M |

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.ligand_id = ligand_7029 AND s.temperature_c BETWEEN 24.5 AND 25.5)",
  "order_by": "s.constant_type ASC",
  "limit": 500
}
```

[summary]
## search_stability — 32 row(s)

### `Cu^[2+]` + Ethylenediamine — 32 measurement(s)
metal_id: metal_41 | ligand_id: ligand_7029
ligand_HxL_def: L | ligand_SMILES: NCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_122419 | *** | beta_def_812 | ΔH | -52.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122420 | *** | beta_def_812 | ΔH | -53.1 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122421 | *** | beta_def_812 | ΔH | -55.2 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122422 | *** | beta_def_812 | ΔH | 0 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122436 | *** | beta_def_840 | ΔH | -104.6 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122437 | *** | beta_def_840 | ΔH | -105.9 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122438 | *** | beta_def_840 | ΔH | -107.1 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122439 | *** | beta_def_840 | ΔH | 0 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122410 | ref_eq_map_9575 | beta_def_812 | logK | 10.49 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122412 | ref_eq_map_9579 | beta_def_812 | logK | 10.64 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122413 | ref_eq_map_9580 | beta_def_812 | logK | 10.8 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122414 | ref_eq_map_9576 | beta_def_812 | logK | 10.84 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122415 | ref_eq_map_9577 | beta_def_812 | logK | 10.96 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122416 | ref_eq_map_9581 | beta_def_812 | logK | 11.26 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122417 | ref_eq_map_9582 | beta_def_812 | logK | 11.38 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122418 | ref_eq_map_9583 | beta_def_812 | logK | 10.5 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122427 | ref_eq_map_9575 | beta_def_840 | logK | 19.6 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122429 | ref_eq_map_9579 | beta_def_840 | logK | 19.9 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122430 | ref_eq_map_9580 | beta_def_840 | logK | 20.3 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122431 | ref_eq_map_9576 | beta_def_840 | logK | 20.08 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122432 | ref_eq_map_9577 | beta_def_840 | logK | 20.6 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122433 | ref_eq_map_9581 | beta_def_840 | logK | 21.12 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122434 | ref_eq_map_9582 | beta_def_840 | logK | 21.35 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122435 | ref_eq_map_9583 | beta_def_840 | logK | 19.58 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122423 | *** | beta_def_812 | ΔS | 22.6 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122424 | *** | beta_def_812 | ΔS | 25.5 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122425 | *** | beta_def_812 | ΔS | 20.1 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122426 | *** | beta_def_812 | ΔS | 0 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122440 | *** | beta_def_840 | ΔS | 24.3 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122441 | *** | beta_def_840 | ΔS | 25.5 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122442 | *** | beta_def_840 | ΔS | 27.2 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122443 | *** | beta_def_840 | ΔS | 0 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.ligand_id = ligand_10103 AND s.temperature_c BETWEEN 24.5 AND 25.5)",
  "order_by": "s.constant_type ASC",
  "limit": 500
}
```

[summary]
## search_stability — 49 row(s)

### `Cu^[2+]` + Ammonia — 49 measurement(s)
metal_id: metal_41 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M] + [L] <=> [ML]` | ΔH | 4 | *** | -23~-20.1 | 25 | 0~3 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔH | 4 | *** | -46.4~-42.3 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^3 <=> [ML3]` | ΔH | 4 | *** | -70.7~-62.3 | 25 | 0~3 | beta_def_872 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^4 <=> [ML4]` | ΔH | 4 | *** | -99.2~-86.6 | 25 | 0~3 | beta_def_894 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | logK | 5 | 5 diff ref_eq_map | 4.02~4.3 | 25 | 0~3 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | logK | 4 | 4 diff ref_eq_map | 7.4~7.91 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^3 <=> [ML3]` | logK | 4 | 4 diff ref_eq_map | 10.2~10.8 | 25 | 0~3 | beta_def_872 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^4 <=> [ML4]` | logK | 4 | 4 diff ref_eq_map | 12.3~13.2 | 25 | 0~3 | beta_def_894 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | ΔS | 4 | *** | 5~9.6 | 25 | 0~3 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔS | 4 | *** | -4.6~0 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^3 <=> [ML3]` | ΔS | 4 | *** | -30.5~-14.2 | 25 | 0~3 | beta_def_872 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^4 <=> [ML4]` | ΔS | 4 | *** | -80.3~-55.2 | 25 | 0~3 | beta_def_894 | *** | [L] | (9.26, L, +inf) |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| ΔH | 16 | 4 | 25 | 0~3 | *** | 0 |
| logK | 17 | 4 | 25 | 0~3 | *** | 5 |
| ΔS | 16 | 4 | 25 | 0~3 | *** | 0 |

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_112 AND c.ligand_id = ligand_7029 AND s.temperature_c BETWEEN 24.5 AND 25.5)",
  "order_by": "s.constant_type ASC",
  "limit": 500
}
```

[summary]
## search_stability — 42 row(s)

### `Ni^[2+]` + Ethylenediamine — 42 measurement(s)
metal_id: metal_112 | ligand_id: ligand_7029
ligand_HxL_def: L | ligand_SMILES: NCCN

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M] + [L] <=> [ML]` | ΔH | 4 | *** | -37.7~0 | 25 | 0.1~3 | beta_def_812 | *** | [L] | (9.92, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔH | 4 | *** | -76.6~0 | 25 | 0.1~3 | beta_def_840 | *** | [L] | (9.92, L, +inf) |
| `[M] + [L]^3 <=> [ML3]` | ΔH | 4 | *** | -117.6~0 | 25 | 0.1~3 | beta_def_872 | *** | [L] | (9.92, L, +inf) |
| `[M] + [L] <=> [ML]` | logK | 6 | 6 diff ref_eq_map | 7.3~7.9 | 25 | 0~3 | beta_def_812 | *** | [L] | (9.92, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | logK | 6 | 6 diff ref_eq_map | -14.77~14.53 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.92, L, +inf) |
| `[M] + [L]^3 <=> [ML3]` | logK | 6 | 6 diff ref_eq_map | -19.7~19.18 | 25 | 0~3 | beta_def_872 | *** | [L] | (9.92, L, +inf) |
| `[M] + [L] <=> [ML]` | ΔS | 4 | *** | 0~18.4 | 25 | 0.1~3 | beta_def_812 | *** | [L] | (9.92, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔS | 4 | *** | 0~10 | 25 | 0.1~3 | beta_def_840 | *** | [L] | (9.92, L, +inf) |
| `[M] + [L]^3 <=> [ML3]` | ΔS | 4 | *** | -58.2~0 | 25 | 0.1~3 | beta_def_872 | *** | [L] | (9.92, L, +inf) |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| ΔH | 12 | 3 | 25 | 0.1~3 | *** | 0 |
| logK | 18 | 3 | 25 | 0~3 | *** | 6 |
| ΔS | 12 | 3 | 25 | 0.1~3 | *** | 0 |

---

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_112 AND c.ligand_id = ligand_10103 AND s.temperature_c BETWEEN 24.5 AND 25.5)",
  "order_by": "s.constant_type ASC",
  "limit": 500
}
```

[summary]
## search_stability — 60 row(s)

### `Ni^[2+]` + Ammonia — 60 measurement(s)
metal_id: metal_112 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M] + [L] <=> [ML]` | ΔH | 4 | *** | -16.3~-15.1 | 25 | 0~3 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔH | 4 | *** | -34.3~-30.5 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^3 <=> [ML3]` | ΔH | 4 | *** | -51.5~-46 | 25 | 0~3 | beta_def_872 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^4 <=> [ML4]` | ΔH | 4 | *** | -69~-64 | 25 | 0~3 | beta_def_894 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^5 <=> [ML5]` | ΔH | 4 | *** | -87.9~-77 | 25 | 0~3 | beta_def_903 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^6 <=> [ML6]` | ΔH | 4 | *** | -107.5~-94.6 | 25 | 0~3 | beta_def_907 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | logK | 4 | 4 diff ref_eq_map | 2.72~2.85 | 25 | 0~2 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | logK | 5 | 5 diff ref_eq_map | 4.88~5.3 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^3 <=> [ML3]` | logK | 3 | ref_eq_map_28127; ref_eq_map_28128; ref_eq_map_28129 | 6.54~6.92 | 25 | 0~2 | beta_def_872 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^4 <=> [ML4]` | logK | 3 | ref_eq_map_28127; ref_eq_map_28128; ref_eq_map_28129 | 7.67~8.16 | 25 | 0~2 | beta_def_894 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^5 <=> [ML5]` | logK | 2 | ref_eq_map_28127; ref_eq_map_28128 | 8.33~8.96 | 25 | 0~2 | beta_def_903 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^6 <=> [ML6]` | logK | 2 | ref_eq_map_28127; ref_eq_map_28128 | 8.3~9.05 | 25 | 0~2 | beta_def_907 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | ΔS | 3 | *** | 1.3~1.7 | 25 | 0~2 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔS | 4 | *** | -13.8~-9.2 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^3 <=> [ML3]` | ΔS | 3 | *** | -31.8~-29.3 | 25 | 0~2 | beta_def_872 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^4 <=> [ML4]` | ΔS | 3 | *** | -69.9~-67.4 | 25 | 0~2 | beta_def_894 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^5 <=> [ML5]` | ΔS | 2 | *** | -110.9~-99.2 | 25 | 0~2 | beta_def_903 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^6 <=> [ML6]` | ΔS | 2 | *** | -171.1~-158.6 | 25 | 0~2 | beta_def_907 | *** | [L] | (9.26, L, +inf) |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| ΔH | 24 | 6 | 25 | 0~3 | *** | 0 |
| logK | 19 | 6 | 25 | 0~3 | *** | 5 |
| ΔS | 17 | 6 | 25 | 0~3 | *** | 0 |

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_7029 AND s.temperature_c BETWEEN 24.5 AND 25.5)",
  "order_by": "s.constant_type ASC",
  "limit": 500
}
```

[summary]
## search_stability — 33 row(s)

### `Zn^[2+]` + Ethylenediamine — 33 measurement(s)
metal_id: metal_208 | ligand_id: ligand_7029
ligand_HxL_def: L | ligand_SMILES: NCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_122516 | *** | beta_def_812 | ΔH | -28 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122517 | *** | beta_def_812 | ΔH | -32.2 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122528 | *** | beta_def_840 | ΔH | -57.7 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122529 | *** | beta_def_840 | ΔH | 0 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122538 | *** | beta_def_872 | ΔH | -77.4 | 25 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.92, L, +inf) |
| vlm_122539 | *** | beta_def_872 | ΔH | -86.6 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.92, L, +inf) |
| vlm_122540 | *** | beta_def_872 | ΔH | -91.6 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.92, L, +inf) |
| vlm_122508 | ref_eq_map_9601 | beta_def_812 | logK | 5.69 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122510 | ref_eq_map_9604 | beta_def_812 | logK | 5.77 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122511 | ref_eq_map_9605 | beta_def_812 | logK | 5.93 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122512 | ref_eq_map_9607 | beta_def_812 | logK | 6.15 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122513 | ref_eq_map_9602 | beta_def_812 | logK | 6.3 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122514 | ref_eq_map_9608 | beta_def_812 | logK | 6.49 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122515 | ref_eq_map_9606 | beta_def_812 | logK | 5.66 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122520 | ref_eq_map_9601 | beta_def_840 | logK | 10.64 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122522 | ref_eq_map_9604 | beta_def_840 | logK | 10.86 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122523 | ref_eq_map_9605 | beta_def_840 | logK | 11.09 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122524 | ref_eq_map_9607 | beta_def_840 | logK | 11.49 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122525 | ref_eq_map_9602 | beta_def_840 | logK | 12.48 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122526 | ref_eq_map_9608 | beta_def_840 | logK | 12.5 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122527 | ref_eq_map_9606 | beta_def_840 | logK | 10.63 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122532 | ref_eq_map_9601 | beta_def_872 | logK | 13 | 25 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.92, L, +inf) |
| vlm_122534 | ref_eq_map_9604 | beta_def_872 | logK | 13 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.92, L, +inf) |
| vlm_122535 | ref_eq_map_9605 | beta_def_872 | logK | 13 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.92, L, +inf) |
| vlm_122536 | ref_eq_map_9602 | beta_def_872 | logK | 14.7 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.92, L, +inf) |
| vlm_122537 | ref_eq_map_9606 | beta_def_872 | logK | -13.9 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.92, L, +inf) |
| vlm_122518 | *** | beta_def_812 | ΔS | 19.2 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122519 | *** | beta_def_812 | ΔS | 12.6 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122530 | *** | beta_def_840 | ΔS | 18.4 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122531 | *** | beta_def_840 | ΔS | -2.9 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122541 | *** | beta_def_872 | ΔS | -10.9 | 25 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.92, L, +inf) |
| vlm_122542 | *** | beta_def_872 | ΔS | -41.8 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.92, L, +inf) |
| vlm_122543 | *** | beta_def_872 | ΔS | -26.4 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.92, L, +inf) |

---

### Step 19: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_10103 AND s.temperature_c BETWEEN 24.5 AND 25.5)",
  "order_by": "s.constant_type ASC",
  "limit": 500
}
```

[summary]
## search_stability — 17 row(s)

### `Zn^[2+]` + Ammonia — 17 measurement(s)
metal_id: metal_208 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173394 | ref_eq_map_28172 | beta_def_812 | logK | 2.33 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173395 | ref_eq_map_28173 | beta_def_812 | logK | 2.3 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173396 | ref_eq_map_28174 | beta_def_812 | logK | 2.41 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173397 | ref_eq_map_28175 | beta_def_812 | logK | 2.21 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173400 | ref_eq_map_28173 | beta_def_840 | logK | 4.83 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173401 | ref_eq_map_28174 | beta_def_840 | logK | 4.95 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173402 | ref_eq_map_28172 | beta_def_840 | logK | 4.5 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173405 | ref_eq_map_28173 | beta_def_872 | logK | 7.11 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.26, L, +inf) |
| vlm_173406 | ref_eq_map_28174 | beta_def_872 | logK | 7.46 | 25 | 2 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.26, L, +inf) |
| vlm_173407 | ref_eq_map_28172 | beta_def_872 | logK | 6.86 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.26, L, +inf) |
| vlm_173410 | ref_eq_map_28173 | beta_def_894 | logK | 9.34 | 25 | 1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (9.26, L, +inf) |
| vlm_173411 | ref_eq_map_28174 | beta_def_894 | logK | 9.73 | 25 | 2 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (9.26, L, +inf) |
| vlm_173412 | ref_eq_map_28172 | beta_def_894 | logK | 8.89 | 25 | 0 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (9.26, L, +inf) |
| vlm_173399 | *** | beta_def_812 | ΔS | 9.6 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173404 | *** | beta_def_840 | ΔS | 14.6 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173409 | *** | beta_def_872 | ΔS | 7.9 | 25 | 2 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.26, L, +inf) |
| vlm_173414 | *** | beta_def_894 | ΔS | -21.8 | 25 | 2 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (9.26, L, +inf) |

---
