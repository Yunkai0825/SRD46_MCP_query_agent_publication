# Q4.7 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "cobalt",
  "symbol": "Co",
  "limit": 10
}
```

[summary]
## search_metals — 3 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_33 | Co^[2+] | Co | 2 | ✓ | [Co+2] | InChI=1S/Co/q+2 | beta_totN_92 | ligand_totN_977 | vlm_totN_2977 |
| metal_34 | Co^[3+] | Co | 3 | ✓ | [Co+3] | InChI=1S/Co/q+3 | beta_totN_20 | ligand_totN_19 | vlm_totN_55 |
| metal_181 | TcO^[2+] | Tc | 2 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "ammonia",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10103 | Ammonia | L | Inorganic ligands | 447 | `N` | (-inf, HL, 9.26, L, +inf) |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 105 SQL matches · showing 10 · limit 10

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

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "diethylenetriamine",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 20 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5958 | Diethylenetriamine-N(1)-acetic acid | HL | Amino Acids | 15 | `NCCNCCNCC(=O)O` | (-inf, H4L, -1.3, H3L, 4.32, H2L, 8.7, HL, 9.92, L, +inf) |
| ligand_7212 | 1,4,7-Triazaheptane (Diethylenetriamine)(dien)(2,… | L | Aliphatic amines seconda… | 126 | `NCCNCCN` | (-inf, H3L, 4.25, H2L, 9.02, HL, 9.84, L, +inf) |
| ligand_7217 | 1,4,7-Triazaoctane (N(1)-Methyldiethylenetriamine) | L | Aliphatic amines seconda… | 24 | `CNCCNCCN` | (-inf, H3L, -3.3, H2L, 9.18, HL, 9.18, L, +inf) |
| ligand_7219 | 3,6,9-Triazaund… (N,N''-Diethyldiethylenetriamine) | L | Aliphatic amines seconda… | 6 | `CCNCCNCCNCC` | (-inf, H3L, 4.31, H2L, 9.85, HL, 10.51, L, +inf) |
| ligand_7220 | 3,6,9-Triazaundecane dinitrile (N,N''-Bis(cyanoet… | L | Aliphatic amines seconda… | 6 | `N#CCCNCCNCCNCCC#N` | (-inf, H3L, 3.65, H2L, 5.83, HL, 8.86, L, +inf) |
| ligand_7221 | 1,9-Bis(2-hydroxyphenyl)-2,5,8-triazanonane (N,N'… | H2L | Aliphatic amines seconda… | 8 | `Oc1ccccc1CNCCNCCNCc1ccccc1O` | (-inf, H5L, 4.18, H4L, 7.94, H3L, 9.09, H2L, 10.41, HL, 11.06, L, +inf) |
| ligand_7222 | 4,7,10-Triazatridecanedioic acid diamide (N,N''-B… | L | Aliphatic amines seconda… | 6 | `NC(=O)CCNCCNCCNCCC(N)=O` | (-inf, H3L, 3.93, H2L, 8.31, HL, 9.34, L, +inf) |
| ligand_7330 | 4-Methyl-1,4,7-… (N,N'-Dimethyldiethylenetriamine) | L | Aliphatic amines tertiar… | 22 | `CNCCN(C)CCN` | (-inf, H3L, 2.82, H2L, 9.35, HL, 10.03, L, +inf) |
| ligand_7331 | 7-Methyl-1,4,7-t… (N,N-Dimethyldiethylenetriamine) | L | Aliphatic amines tertiar… | 23 | `CN(C)CCNCCN` | (-inf, H3L, 3.62, H2L, 8.63, HL, 9.62, L, +inf) |
| ligand_7332 | 7-Ethyl-1,4,7-tri… (N,N-Diethyldiethylenetriamine) | L | Aliphatic amines tertiar… | 5 | `CCN(CC)CCNCCN` | (-inf, H3L, 3.93, H2L, 9.1, HL, 9.9, L, +inf) |

### Functional groups across all SQL matches (19 parseable SMILES)

| group | count | % |
|-------|-------|---|
| secondary_amine | 16 | 84% |
| tertiary_amine | 12 | 63% |
| primary_amine | 7 | 37% |
| aromatic_ring | 3 | 16% |
| hydroxyl | 2 | 11% |
| phenol | 2 | 11% |
| amide | 1 | 5% |
| carboxyl | 1 | 5% |
| nitrile | 1 | 5% |
| pyridine | 1 | 5% |

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "triethylenetetramine",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_7224 | 1,4,7,10-Tetraazadecane (Triethylenetetramine)(tr… | L | Aliphatic amines seconda… | 127 | `NCCNCCNCCN` | (-inf, H4L, 3.27, H3L, 6.58, H2L, 9.07, HL, 9.75, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 1 | 100% |
| secondary_amine | 1 | 100% |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "tris(2-aminoethyl)amine",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_7345 | Nitrilotris(ethyleneamine) [Tris(2-aminoet… (Tren) | L | Aliphatic amines tertiar… | 87 | `NCCN(CCN)CCN` | (-inf, H3L, 8.42, H2L, 9.43, HL, 10.13, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 1 | 100% |
| tertiary_amine | 1 | 100% |

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "1,4,7-triazacyclononane",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 15 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6075 | 1,4,7-Triazacyclononane-N-acetic acid (NOMA) | HL | Aza macrocycles with car… | 17 | `O=C(O)CN1CCNCCNCC1` | (-inf, H3L, 2.82, H2L, 7.45, HL, 7.45, L, +inf) |
| ligand_6076 | 1,4,7-Triazacyclononane-N,N',N''-triacetic… (NOTA) | H3L | Aza macrocycles with car… | 55 | `O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CC1` | (-inf, H4L, -1.7, H3L, 3.17, H2L, 5.7, HL, 5.7, L, +inf) |
| ligand_7402 | 1,4,7-Triazacyclononane ([9]aneN3) | L | Aza-macrocycles | 33 | `C1CNCCNCCN1` | (-inf, H2L, 6.81, HL, 10.44, L, +inf) |
| ligand_7403 | 1,4,7-Trimethyl-1,4,7-triazacyclononane | L | Aza-macrocycles | 2 | `CN1CCN(C)CCN(C)CC1` | *** |
| ligand_7404 | Ethylenebis(1,4,7-triazacyclononane) | L | Aza-macrocycles | 5 | `C1CNCCN(CCN2CCNCCNCC2)CCN1` | (-inf, H4L, 5.6, H3L, 6.31, H2L, 10.18, HL, 10.18, L, +inf) |
| ligand_7405 | Trimethylenebis(1,4,7-triazacyclononane) | L | Aza-macrocycles | 9 | `C(CN1CCNCCNCC1)CN1CCNCCNCC1` | (-inf, H4L, 5.77, H3L, 6.47, H2L, 10.38, HL, 10.38, L, +inf) |
| ligand_7406 | Tetramethylenebis(1,4,7-triazacyclononane) | L | Aza-macrocycles | 9 | `C(CCN1CCNCCNCC1)CN1CCNCCNCC1` | (-inf, H4L, 5.87, H3L, 6.57, H2L, 10.48, HL, 10.48, L, +inf) |
| ligand_7407 | Pentamethylenebis(1,4,7-triazacyclononane) | L | Aza-macrocycles | 10 | `C(CCN1CCNCCNCC1)CCN1CCNCCNCC1` | (-inf, H4L, 5.98, H3L, 6.64, H2L, 10.5, HL, 10.5, L, +inf) |
| ligand_7408 | Hexamethylenebis(1,4,7-triazacyclononane) | L | Aza-macrocycles | 10 | `C(CCCN1CCNCCNCC1)CCN1CCNCCNCC1` | (-inf, H4L, 6.03, H3L, 6.66, H2L, 10.52, HL, 10.52, L, +inf) |
| ligand_7421 | 1,4,7-Tris(2-mercaptoethyl)-1,4,7-triazacyclonona… | H3L | Aza-macrocycles | 15 | `SCCN1CCN(CCS)CCN(CCS)CC1` | (-inf, H5L, 2.5, H4L, 8.26, H3L, 9.45, H2L, 10.97, HL, 10.97, L, +inf) |

### Functional groups across all SQL matches (13 parseable SMILES)

| group | count | % |
|-------|-------|---|
| tertiary_amine | 12 | 92% |
| secondary_amine | 7 | 54% |
| hydroxyl | 3 | 23% |
| carboxyl | 2 | 15% |
| aromatic_ring | 1 | 8% |
| phosphonate | 1 | 8% |
| pyridine | 1 | 8% |
| thiol | 1 | 8% |

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "cyclen",
  "limit": 10
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_7425 | 1,4,7,10-Tetraazacyclododecane ([12]aneN4)(Cyclen) | L | Aza-macrocycles | 52 | `C1CNCCNCCNCCN1` | (-inf, H3L, -1.4, H2L, 9.64, HL, 10.65, L, +inf) |
| ligand_10592 | 12-(2-Hydroxybenzyl)-11,13-dioxo-1,4,7,10-Tetraaz… | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| secondary_amine | 1 | 100% |

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "cyclam",
  "limit": 10
}
```

[summary]
## search_ligands — 9 result(s)

**stats:** 9 SQL matches · showing 9 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_7436 | 1,4,7,11-Tetraazacyclotetradecane (Isocyclam) | L | Aza-macrocycles | 30 | `C1CNCCCNCCNCCNC1` | (-inf, H4L, -0.9, H3L, 4.01, H2L, 9.86, HL, 10.93, L, +inf) |
| ligand_7439 | 1,4,8,11-Tetraazacyclotetradecane ([14]aneN4)(Cyc… | L | Aza-macrocycles | 50 | `C1CNCCNCCCNCCNC1` | (-inf, H4L, -2.1, H3L, -1.6, H2L, 10.28, HL, 10.28, L, +inf) |
| ligand_7451 | cis-2,6,9,13-Tetraazad… (cis-2,3-Cyclohexylcyclam) | L | Aza-macrocycles | 3 | `C1CNCCNCCCNC2CCCCC2NC1` | (-inf, H3L, 3.2, H2L, 9.99, HL, 9.99, L, +inf) |
| ligand_7452 | trans-2,6,9,13-Tetra… (trans-2,3-Cyclohexylcyclam) | L | Aza-macrocycles | 3 | `C1CNCCNCCCNC2CCCCC2NC1` | (-inf, H3L, 2.4, H2L, 10.64, HL, 10.64, L, +inf) |
| ligand_7453 | cis-anti-cis-2,6,13,17-Tetra… (Dicyclohexylcyclam) | L | Aza-macrocycles | 3 | `C1CNC2CCCCC2NCCCNC2CCCCC2NC1` | (-inf, H3L, -1.7, H2L, 10.41, HL, 10.95, L, +inf) |
| ligand_7454 | cis-syn-cis-2,6,13,17-Tetraa… (Dicyclohexylcyclam) | L | Aza-macrocycles | 3 | `C1CNC2CCCCC2NCCCNC2CCCCC2NC1` | (-inf, H3L, -1.5, H2L, 10.37, HL, 10.37, L, +inf) |
| ligand_7720 | Bis(11,13-dioxo-1,4,7,10-tet… ([13]Bisdioxocyclam) | L | Aza-oxo-macrocycles | 7 | `O=C1NCCNCCNCCNC(=O)C1C1C(=O)NCCNCCNCCNC1=O` | (-inf, H4L, 2.78, H3L, 3.71, H2L, 8.51, HL, 8.98, L, +inf) |
| ligand_7721 | Bis(5,7-dioxo-1,4,8,11-tetra… ([14]Bisdioxocyclam) | L | Aza-oxo-macrocycles | 10 | `O=C1NCCNCCCNCCNC(=O)C1C1C(=O)NCCNCCCNCCNC1=O` | (-inf, H4L, 4.62, H3L, 5.4, H2L, 9.45, HL, 9.96, L, +inf) |
| ligand_10593 | Dicyclohexylcyclam | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (8 parseable SMILES)

| group | count | % |
|-------|-------|---|
| secondary_amine | 8 | 100% |
| amide | 2 | 25% |

---

### Step 11: `search_ligands`
**Args:**
```json
{
  "name": "EDTA",
  "limit": 10
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6118 | 6,11,18,23-Tetraoxo-1,4,7,10,13,16,19,… (24edtaen) | *** | Aza macrocycles with car… | 15 | *** | (-inf, H4L, 3.3, H3L, 4.18, H2L, 7.26, HL, 7.78, L, +inf) |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriace… (HEDTA) | H3L | EDTA and derivatives | 237 | `O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O` | (-inf, H3L, 2.62, H2L, 5.38, HL, 9.7, L, +inf) |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | EDTA and derivatives | 596 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H5L, -1.5, H4L, 2, H3L, 2.69, H2L, 6.13, HL, 9.52, L, +inf) |
| ligand_6335 | Oxybis(ethylenenitrilo)tetraacetic acid (EEDTA) | H4L | EDTA and derivatives | 124 | `O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, -1.8, H3L, 2.76, H2L, 8.75, HL, 9.39, L, +inf) |
| ligand_6348 | Thiobis(ethylenenitrilo)tetraacetic acid (TEDTA) | H4L | EDTA and derivatives | 101 | `O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, 2, H3L, 2.68, H2L, 8.37, HL, 9.31, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| tertiary_amine | 4 | 100% |
| ether | 1 | 25% |
| hydroxyl | 1 | 25% |
| thioether | 1 | 25% |

---

### Step 12: `search_ligands`
**Args:**
```json
{
  "name": "DTPA",
  "limit": 10
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6117 | 9,17-Dioxo-1,4,7,10,13,16-hexaazacycl… (DTPA-dien) | H3L | Aza macrocycles with car… | 6 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCNCCNC(=O)CN(CC(=O)O)CC1` | (-inf, H5L, -1.8, H4L, 2.62, H3L, 4.1, H2L, 8.87, HL, 10.02, L, +inf) |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | H5L | EDTA and derivatives | 322 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O` | (-inf, H8L, -0.1, H7L, -0.1, H6L, -0.7, H5L, 2, H4L, 2.7, H3L, 4.28, H2L, 4.28, HL, -8.4, L, +inf) |
| ligand_6362 | Diethylenetrinitrilopentaacetic acid N… (DTPA-BMA) | *** | EDTA and derivatives | 43 | *** | (-inf, H4L, -1.4, H3L, 3.31, H2L, 4.38, HL, 9.37, L, +inf) |
| ligand_6363 | Diethylenetrinitrilopentaacetic acid N… (DTPA-BBA) | *** | EDTA and derivatives | 9 | *** | (-inf, H3L, 3.31, H2L, 4.44, HL, 9.36, L, +inf) |
| ligand_6364 | N,N"-Bis(2-pyridylmethyl)diethylenetrin… (DTPA-BP) | *** | EDTA and derivatives | 14 | *** | (-inf, H5L, 2.28, H4L, 3.41, H3L, 4.76, H2L, 6.46, HL, 9.5, L, +inf) |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| tertiary_amine | 2 | 100% |
| amide | 1 | 50% |
| secondary_amine | 1 | 50% |

---

### Step 14: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_33",
  "ligand_id": "ligand_10103"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 5 species

### Co^[2+] + Ammonia
**metal_id:** metal_33 | **ligand_id:** ligand_10103 | **ligand_def_HxL:** L  
**entries:** 19 | **species:** 5 | **vlm_count:** 19

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 7 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 3 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 3 |
| beta_def_894 | [ML<sub>4</sub>]/[M][L]<sup>4</sup> | [M] + [L]^4 <=> [ML4] | [ML4](aqueous), [M](aqueous), [L](aqueous) | 3 |
| beta_def_903 | [ML<sub>5</sub>]/[M][L]<sup>5</sup> | [M] + [L]^5 <=> [ML5] | [ML5](aqueous), [M](aqueous), [L](aqueous) | 3 |

**vlm_ids:** vlm_173163, vlm_173164, vlm_173165, vlm_173166, vlm_173167, … vlm_173179, vlm_173180, vlm_173181 (19 listed)

**equilibrium_maps:** 5 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28231 | 5 | 10 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28232 | 5 | 10 | 19~29 °C | 4.85~5.15 M |
| ref_eq_net_28233 | 5 | 10 | 25~35 °C | 1.85~2.15 M |
| ref_eq_net_28234 | 1 | 0 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28235 | 1 | 0 | 19~29 °C | -0.15~0.15 M |

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_33, metal_34) AND c.ligand_id IN (ligand_10103, ligand_7029, ligand_7212, ligand_7224, ligand_7345, ligand_7402, ligand_7425, ligand_7439, ligand_6277, ligand_6356) AND (s.solvent_name IS NULL OR LOWER(s.solvent_name) LIKE '%water%') AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2) AND s.temperature_c BETWEEN 20 AND 30 AND (s.electrolyte_composition IS NULL OR LOWER(s.electrolyte_composition) NOT LIKE '%cl%'))",
  "order_by": "ABS(s.temperature_c - 25) ASC, s.ionic_strength_mol_l ASC",
  "limit": 1000
}
```

[summary]
## search_stability

*(no results)*

---
