# Q4.3 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "copper, nickel, zinc"
}
```

[summary]
## search_metals

*(no results)*

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine, ammonia"
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 4: `search_metals`
**Args:**
```json
{
  "name": "copper"
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

### Step 5: `search_metals`
**Args:**
```json
{
  "name": "nickel"
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_112 | Ni^[2+] | Ni | 2 | ✓ | [Ni+2] | InChI=1S/Ni/q+2 | beta_totN_149 | ligand_totN_1369 | vlm_totN_5325 |
| metal_113 | Ni^[3+] | Ni | 3 | ✓ | [Ni+3] | InChI=1S/Ni/q+3 | beta_totN_5 | ligand_totN_4 | vlm_totN_7 |

---

### Step 6: `search_metals`
**Args:**
```json
{
  "name": "zinc"
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine"
}
```

[summary]
## search_ligands — 25 result(s)

**stats:** 105 SQL matches · showing 25 · limit 25

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

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "ammonia"
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10103 | Ammonia | L | Inorganic ligands | 447 | `N` | (-inf, HL, 9.26, L, +inf) |

---

### Step 10: `build_system_catalog`
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

### Step 11: `build_system_catalog`
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

### Step 12: `build_system_catalog`
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

### Step 13: `build_system_catalog`
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

### Step 14: `build_system_catalog`
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

### Step 15: `build_system_catalog`
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

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.ligand_id = ligand_7029 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.ionic_strength_mol_l ASC",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### `Cu^[2+]` + Ethylenediamine — 10 measurement(s)
metal_id: metal_41 | ligand_id: ligand_7029
ligand_HxL_def: L | ligand_SMILES: NCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_122418 | ref_eq_map_9583 | beta_def_812 | logK | 10.5 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122410 | ref_eq_map_9575 | beta_def_812 | logK | 10.49 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122419 | *** | beta_def_812 | ΔH | -52.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122423 | *** | beta_def_812 | ΔS | 22.6 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122412 | ref_eq_map_9579 | beta_def_812 | logK | 10.64 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122420 | *** | beta_def_812 | ΔH | -53.1 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122424 | *** | beta_def_812 | ΔS | 25.5 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122413 | ref_eq_map_9580 | beta_def_812 | logK | 10.8 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122421 | *** | beta_def_812 | ΔH | -55.2 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122425 | *** | beta_def_812 | ΔS | 20.1 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.ionic_strength_mol_l ASC",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### `Cu^[2+]` + Ammonia — 10 measurement(s)
metal_id: metal_41 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173246 | ref_eq_map_28136 | beta_def_812 | logK | 4.02 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173247 | *** | beta_def_812 | ΔH | -20.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173251 | *** | beta_def_812 | ΔS | 9.6 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173242 | ref_eq_map_28132 | beta_def_812 | logK | 4.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173243 | ref_eq_map_28133 | beta_def_812 | logK | 4.12 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173248 | *** | beta_def_812 | ΔH | -20.9 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173252 | *** | beta_def_812 | ΔS | 8.8 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173244 | ref_eq_map_28134 | beta_def_812 | logK | 4.2 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173249 | *** | beta_def_812 | ΔH | -22.2 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173253 | *** | beta_def_812 | ΔS | 5.9 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |

---

### Step 19: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_112 AND c.ligand_id = ligand_7029 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.ionic_strength_mol_l ASC",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### `Ni^[2+]` + Ethylenediamine — 10 measurement(s)
metal_id: metal_112 | ligand_id: ligand_7029
ligand_HxL_def: L | ligand_SMILES: NCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_122371 | ref_eq_map_9574 | beta_def_812 | logK | 7.32 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122365 | ref_eq_map_9568 | beta_def_812 | logK | 7.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122372 | *** | beta_def_812 | ΔH | 0 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122376 | *** | beta_def_812 | ΔS | 9.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122367 | ref_eq_map_9570 | beta_def_812 | logK | 7.45 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122373 | *** | beta_def_812 | ΔH | -37.7 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122377 | *** | beta_def_812 | ΔS | 16.3 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122368 | ref_eq_map_9571 | beta_def_812 | logK | 7.56 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122374 | *** | beta_def_812 | ΔH | -37.7 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122378 | *** | beta_def_812 | ΔS | 18.4 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |

---

### Step 20: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_112 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.ionic_strength_mol_l ASC",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### `Ni^[2+]` + Ammonia — 10 measurement(s)
metal_id: metal_112 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173185 | ref_eq_map_28130 | beta_def_812 | logK | 2.72 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173186 | *** | beta_def_812 | ΔH | -15.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173190 | *** | beta_def_812 | ΔS | 1.7 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173182 | ref_eq_map_28127 | beta_def_812 | logK | 2.73 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173183 | ref_eq_map_28129 | beta_def_812 | logK | 2.8 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173187 | *** | beta_def_812 | ΔH | -15.5 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173191 | *** | beta_def_812 | ΔS | 1.7 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173184 | ref_eq_map_28128 | beta_def_812 | logK | 2.85 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173188 | *** | beta_def_812 | ΔH | -15.9 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173192 | *** | beta_def_812 | ΔS | 1.3 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |

---

### Step 21: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_7029 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.ionic_strength_mol_l ASC",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### `Zn^[2+]` + Ethylenediamine — 10 measurement(s)
metal_id: metal_208 | ligand_id: ligand_7029
ligand_HxL_def: L | ligand_SMILES: NCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_122515 | ref_eq_map_9606 | beta_def_812 | logK | 5.66 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122508 | ref_eq_map_9601 | beta_def_812 | logK | 5.69 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122510 | ref_eq_map_9604 | beta_def_812 | logK | 5.77 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122511 | ref_eq_map_9605 | beta_def_812 | logK | 5.93 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122516 | *** | beta_def_812 | ΔH | -28 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122518 | *** | beta_def_812 | ΔS | 19.2 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122512 | ref_eq_map_9607 | beta_def_812 | logK | 6.15 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122513 | ref_eq_map_9602 | beta_def_812 | logK | 6.3 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122514 | ref_eq_map_9608 | beta_def_812 | logK | 6.49 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122517 | *** | beta_def_812 | ΔH | -32.2 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |

---

### Step 22: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.ionic_strength_mol_l ASC",
  "limit": 10
}
```

[summary]
## search_stability — 6 row(s)

### `Zn^[2+]` + Ammonia — 6 measurement(s)
metal_id: metal_208 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173397 | ref_eq_map_28175 | beta_def_812 | logK | 2.21 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173394 | ref_eq_map_28172 | beta_def_812 | logK | 2.33 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173395 | ref_eq_map_28173 | beta_def_812 | logK | 2.3 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173396 | ref_eq_map_28174 | beta_def_812 | logK | 2.41 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173398 | *** | beta_def_812 | ΔH | -10.9 | 27 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173399 | *** | beta_def_812 | ΔS | 9.6 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |

---
