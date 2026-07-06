# Q4.7 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "cobalt",
  "limit": 100
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

### Step 4: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_33, metal_34) AND s.constant_type LIKE '%Beta1%' AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 20 AND 30 AND c.ligand_class_name LIKE '%amine%')",
  "order_by": "c.ligand_name_SRD ASC, c.metal_id ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 2000
}
```

[summary]
## search_stability

*(no results)*

---

### Step 5: `search_ligands`
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

### Step 6: `search_ligands`
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

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "diethylenetriamine",
  "limit": 50
}
```

[summary]
## search_ligands — 20 result(s)

**stats:** 20 SQL matches · showing 20 · limit 50

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
| ligand_7333 | 5-Methyl-2… (N,N',N''-Trimethyldiethylenetriamine) | L | Aliphatic amines tertiar… | 15 | `CNCCN(C)CCNC` | (-inf, H3L, 3.13, H2L, 9.84, HL, 10.36, L, +inf) |
| ligand_7334 | 4,7-Dimethyl… (N,N,N'-Trimethyldiethylenetriamine) | L | Aliphatic amines tertiar… | 16 | `CN(C)CCN(C)CCN` | (-inf, H3L, 3.19, H2L, 9.23, HL, 9.88, L, +inf) |
| ligand_7335 | 6-Ethyl-3,6… (N,N',N''-Triethyldiethylenetriamine) | L | Aliphatic amines tertiar… | 5 | `CCNCCN(CC)CCNCC` | (-inf, H3L, 2.93, H2L, 9.37, HL, 10.13, L, +inf) |
| ligand_7336 | 2,8-D… (N,N,N'',N''-Tetramethyldiethylenetriamine) | L | Aliphatic amines tertiar… | 18 | `CN(C)CCNCCN(C)C` | (-inf, H3L, 3.84, H2L, 8.96, HL, 9.59, L, +inf) |
| ligand_7337 | 3,9-Di… (N,N,N'',N''-Tetraethyldiethylenetriamine) | L | Aliphatic amines tertiar… | 5 | `CCN(CC)CCNCCN(CC)CC` | (-inf, H3L, 3.39, H2L, 9.03, HL, 9.78, L, +inf) |
| ligand_7338 | 2,… (N,N,N',N'',N''-Pentamethyldiethylenetriamine) | L | Aliphatic amines tertiar… | 20 | `CN(C)CCN(C)CCN(C)C` | (-inf, H3L, 2.09, H2L, 8.41, HL, 9.22, L, +inf) |
| ligand_7339 | 3,9-Diethyl-6-methyl-3,6,9-triazaundecane (N,N,N'… | L | Aliphatic amines tertiar… | 3 | `CCN(CC)CCN(C)CCN(CC)CC` | (-inf, H3L, 2.29, H2L, 9.02, HL, 9.71, L, +inf) |
| ligand_7341 | N,N''-Bis(2-hydroxybenzyl)-N'-benzyldiethylenetri… | H2L | Aliphatic amines tertiar… | 4 | `Oc1ccccc1CNCCN(CCNCc1ccccc1O)Cc1ccccc1` | (-inf, H5L, 3.05, H4L, 7.51, H3L, 8.5, H2L, 10.55, HL, +inf) |
| ligand_7342 | N,N''-Bis(2-pyridylmethyl)-N'-benzyldiethylenetri… | L | Aliphatic amines tertiar… | 3 | `c1ccc(CN(CCNCc2ccccn2)CCNCc2ccccn2)cc1` | (-inf, H3L, 3.18, H2L, 7.23, HL, 8.45, L, +inf) |
| ligand_10660 | N,N'-Bis(2-tetrazol-5-ylethyl)diethylenetriamine | *** | Ligands not selected | 0 | *** | *** |

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

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "triethylenetetramine",
  "limit": 50
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_7224 | 1,4,7,10-Tetraazadecane (Triethylenetetramine)(tr… | L | Aliphatic amines seconda… | 127 | `NCCNCCNCCN` | (-inf, H4L, 3.27, H3L, 6.58, H2L, 9.07, HL, 9.75, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 1 | 100% |
| secondary_amine | 1 | 100% |

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "tris(2-aminoethyl)amine",
  "limit": 50
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_7345 | Nitrilotris(ethyleneamine) [Tris(2-aminoet… (Tren) | L | Aliphatic amines tertiar… | 87 | `NCCN(CCN)CCN` | (-inf, H3L, 8.42, H2L, 9.43, HL, 10.13, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 1 | 100% |
| tertiary_amine | 1 | 100% |

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "cyclen",
  "limit": 50
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_7425 | 1,4,7,10-Tetraazacyclododecane ([12]aneN4)(Cyclen) | L | Aza-macrocycles | 52 | `C1CNCCNCCNCCN1` | (-inf, H3L, -1.4, H2L, 9.64, HL, 10.65, L, +inf) |
| ligand_10592 | 12-(2-Hydroxybenzyl)-11,13-dioxo-1,4,7,10-Tetraaz… | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| secondary_amine | 1 | 100% |

---

### Step 11: `search_ligands`
**Args:**
```json
{
  "name": "cyclam",
  "limit": 50
}
```

[summary]
## search_ligands — 9 result(s)

**stats:** 9 SQL matches · showing 9 · limit 50

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

### Step 12: `search_ligands`
**Args:**
```json
{
  "name": "1,4,7-triazacyclononane",
  "limit": 50
}
```

[summary]
## search_ligands — 15 result(s)

**stats:** 15 SQL matches · showing 15 · limit 50

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
| ligand_7422 | 1,4,7-Tris(3-hydroxy-6-methyl-2-pyridylmethyl)-1,… | H3L | Aza-macrocycles | 22 | `Cc1ccc(O)c(CN2CCN(Cc3nc(C)ccc3O)CCN(Cc3nc(C)ccc3O)CC2)n1` | (-inf, H7L, 2, H6L, 4.28, H5L, 5.35, H4L, 7, H3L, 9.73, H2L, 10.86, HL, 10.86, L, +inf) |
| ligand_7668 | 1,4,7-Tris(2-hydroxyethyl)-1,4,7-triazacyclononane | L | Aza-macrocycles | 9 | `OCCN1CCN(CCO)CCN(CCO)CC1` | (-inf, H2L, 3.42, HL, 3.42, L, +inf) |
| ligand_8401 | 1,4,7-Triazacyclononane-1,4,7-tris(methyle… (NOTP) | H6L | Aminophosphorus acids | 11 | `O=P(O)(O)CN1CCN(CP(=O)(O)O)CCN(CP(=O)(O)O)CC1` | (-inf, H6L, -0.9, H5L, 3.1, H4L, 5.8, H3L, 7.5, H2L, 9.1, HL, 9.1, L, +inf) |
| ligand_10585 | 1,4,7-Trimethyl-1,4,7-triazacyclononane | *** | Ligands not selected | 0 | *** | *** |
| ligand_10862 | 1,4,7-Triazacyclononane-1,4,7-tris(ethylphosphoni… | *** | Ligands not selected | 0 | *** | *** |

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

### Step 13: `search_ligands`
**Args:**
```json
{
  "name": "EDTA",
  "limit": 50
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 50

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

### Step 14: `search_ligands`
**Args:**
```json
{
  "name": "NTA",
  "limit": 50
}
```

[summary]
## search_ligands — 50 result(s)

**stats:** 298 SQL matches · showing 50 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5763 | DL-2-Aminopentanoic acid (Norvaline) | HL | Amino Acids | 35 | `CCC[C@H](N)C(=O)O` | (-inf, H2L, 2.31, HL, 9.65, L, +inf) |
| ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) | HL | Amino Acids | 49 | `CC(C)C[C@H](N)C(=O)O` | (-inf, H2L, 2.32, HL, 9.58, L, +inf) |
| ligand_5767 | L-2-Amino-3-methylpentanoic acid (Isoleucine) | HL | Amino Acids | 51 | `CC[C@H](C)[C@H](N)C(=O)O` | (-inf, H2L, 2.26, HL, 9.6, L, +inf) |
| ligand_5768 | D-allo-2-Amino-3-methylpentan… (D-allo-Isoleucine) | HL | Amino Acids | 16 | `CC[C@H](C)[C@@H](N)C(=O)O` | (-inf, H2L, 2.2, HL, 9.62, L, +inf) |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) | HL | Amino Acids | 11 | `NC1(C(=O)O)CCCC1` | (-inf, H2L, 2.4, HL, 10.31, L, +inf) |
| ligand_5790 | cis-2-Aminocyclopentane-1-carboxylic acid | HL | Amino Acids | 6 | `N[C@H]1CCC[C@H]1C(=O)O` | (-inf, H2L, 3.54, HL, 10.1, L, +inf) |
| ligand_5791 | trans-2-Aminocyclopentane-1-carboxylic acid | HL | Amino Acids | 3 | `N[C@@H]1CCC[C@H]1C(=O)O` | (-inf, H2L, 3.75, HL, 9.91, L, +inf) |
| ligand_5798 | 5-Aminopentanoic acid | HL | Amino Acids | 20 | `NCCCCC(=O)O` | (-inf, H2L, 4.27, HL, 10.766, L, +inf) |
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | H2L | Amino Acids | 94 | `N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H3L, 2.16, H2L, 4.15, HL, 9.58, L, +inf) |
| ligand_5805 | DL-2-Amino-2-methylpentan… (2-Methylglutamic acid) | H2L | Amino Acids | 4 | `C[C@](N)(CCC(=O)O)C(=O)O` | (-inf, H2L, 4.05, HL, 9.72, L, +inf) |
| ligand_5807 | DL-2-Amino-3-hydroxypent… (3-Hydroxyglutamic acid) | H2L | Amino Acids | 8 | `N[C@H](C(=O)O)C(O)CC(=O)O` | (-inf, H3L, 2.09, H2L, 4.08, HL, 9.06, L, +inf) |
| ligand_5840 | DL-2-Aminopentanedioic acid 5… (5-Ethyl glutamate) | HL | Amino Acids | 2 | `CCOC(=O)CC[C@H](N)C(=O)O` | (-inf, H2L, 2.15, HL, 9.19, L, +inf) |
| ligand_5841 | L-2-Aminopentanedioic acid 5… (5-Benzyl glutamate) | HL | Amino Acids | 2 | `N[C@@H](CCC(=O)OCc1ccccc1)C(=O)O` | (-inf, H2L, 2.06, HL, 8.89, L, +inf) |
| ligand_5842 | DL-2-Aminopentanedioic acid 1… (1-Ethyl glutamate) | HL | Amino Acids | 2 | `CCOC(=O)[C@@H](N)CCC(=O)O` | (-inf, H2L, 3.85, HL, 7.84, L, +inf) |
| ligand_5844 | L-2-Aminopentanedioic acid 5-amide (Glutamine) | HL | Amino Acids | 71 | `NC(=O)CC[C@H](N)C(=O)O` | (-inf, H2L, 2.19, HL, 9, L, +inf) |
| ligand_5852 | L-2-Amino-5-ureidopentanoic acid (Citrulline) | HL | Amino Acids | 16 | `NC(=O)NCCC[C@H](N)C(=O)O` | (-inf, H2L, 2.3, HL, 9.33, L, +inf) |
| ligand_5858 | DL-2-Amino-3-mercapto-3-methylpentanoic acid | H2L | Amino Acids | 2 | `CCC(C)(S)C(N)C(=O)O` | (-inf, H2L, 7.96, HL, 10.5, L, +inf) |
| ligand_5875 | 5-Amino-3-thi… (S-2-Aminoethylmercaptoacetic acid) | HL | Amino Acids | 32 | `NCCSCC(=O)O` | (-inf, H2L, 3.18, HL, 9.53, L, +inf) |
| ligand_5886 | L-2,5-Diaminopentanoic acid (Ornithine) | HL | Amino Acids | 84 | `NCCC[C@H](N)C(=O)O` | (-inf, H3L, 2, H2L, 8.78, HL, 10.52, L, +inf) |
| ligand_5917 | L-2-Amino-5-guanidopentanoic acid (Arginine) | H2L | Amino Acids | 45 | `N=C(N)NCCC[C@H](N)C(=O)O` | (-inf, H3L, 2.03, H2L, 9, HL, 9, L, +inf) |
| ligand_5934 | L-2-(Iminomethylamino)pentanedioic acid | H2L | Amino Acids | 6 | `N=CNC(CCC(=O)O)C(=O)O` | (-inf, H2L, 4.44, HL, 11, L, +inf) |
| ligand_5985 | Ethylenediiminodi-2-pentanedioic acid (EDDG) | H4L | Amino Acids | 63 | `O=C(O)CCC(NCCNC(CCC(=O)O)C(=O)O)C(=O)O` | (-inf, H4L, -3.28, H3L, 4.25, H2L, 6.81, HL, 6.81, L, +inf) |
| ligand_6017 | N,N-Pentamethyleneglyc… (Piperidine-N-acetic acid) | HL | Amino Acids | 6 | `O=C(O)CN1CCCCC1` | (-inf, H2L, 2.13, HL, 10.25, L, +inf) |
| ligand_6062 | 1,4-Diazacycloheptane-N,N'-di(2-pentanoic acid) | H2L | Aza macrocycles with car… | 3 | `CCCC(C(=O)O)N1CCCN(C(CCC)C(=O)O)CC1` | (-inf, H2L, 5.67, HL, 9.88, L, +inf) |
| ligand_6070 | 1,4,10-Trioxa-7,13-diazacyclopentadecane-N,N'-dia… | H2L | Aza macrocycles with car… | 74 | `O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCC1` | (-inf, H3L, 2, H2L, 8.45, HL, 8.63, L, +inf) |
| ligand_6080 | 1,4,8-Triazacyclodecane-N,N',N''-triacetic… (UNTA) | H3L | Aza macrocycles with car… | 3 | `O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCC1` | (-inf, H4L, -1.7, H3L, 3.4, H2L, 7.2, HL, +inf) |
| ligand_6087 | 1,7-Dioxa-4,10,13-triazacyclopentadecane-N,N',N''… | H3L | Aza macrocycles with car… | 50 | `O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CCOCC1` | (-inf, H4L, -1.6, H3L, 4.51, H2L, 8.92, HL, 9.55, L, +inf) |
| ligand_6089 | 9,14-Dioxo-1,4,7,10,13-pentaazacyclopentadecane-1… | H3L | Aza macrocycles with car… | 41 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCNC(=O)CN(CC(=O)O)CC1` | (-inf, H4L, 2, H3L, 3.42, H2L, 4.2, HL, 9.49, L, +inf) |
| ligand_6090 | 9,15-Dioxo-1,4,7,10,14-pentaazacyclohexadecane-1,… | H3L | Aza macrocycles with car… | 24 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCCNC(=O)CN(CC(=O)O)CC1` | (-inf, H4L, -1.8, H3L, 3.58, H2L, 4.42, HL, 9.66, L, +inf) |
| ligand_6091 | 9,16-Dioxo-1,4,7,10,15-pentaazacycloheptadecane-1… | H3L | Aza macrocycles with car… | 25 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCCCNC(=O)CN(CC(=O)O)CC1` | (-inf, H4L, -1.8, H3L, 3.37, H2L, 4.45, HL, 9.05, L, +inf) |
| ligand_6092 | 9,16-Dioxo-1,4,7,10,15-pentaaza-cis-cycloheptadec… | *** | Aza macrocycles with car… | 6 | *** | (-inf, H4L, 2, H3L, 3.32, H2L, 4.67, HL, 9.68, L, +inf) |
| ligand_6093 | 9,17-Dioxo-1,4,7,10,16-pentaazacyclooctadecane-1,… | H3L | Aza macrocycles with car… | 6 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCCCCNC(=O)CN(CC(=O)O)CC1` | (-inf, H4L, -1.8, H3L, 3.13, H2L, 4.48, HL, 9.09, L, +inf) |
| ligand_6094 | 3,6,9-Tris(carboxymethyl)-4,14-dioxo-3,6,9,12,15-… | H3L | Aza macrocycles with car… | 6 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCc2cccc(c2)CNC(=O)CN(CC(=O)O)CC1` | (-inf, H4L, -1.5, H3L, 3.31, H2L, 4.29, HL, 8.3, L, +inf) |
| ligand_6095 | 9,20-Dioxo-13,16-dioxa-1,4,7,10,19-pentaazacycloh… | H3L | Aza macrocycles with car… | 18 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCOCCOCCNC(=O)CN(CC(=O)O)CC1` | (-inf, H4L, -1.6, H3L, 3.49, H2L, 4.6, HL, 8.98, L, +inf) |
| ligand_6096 | 6,14-Dioxo-1,4,7,10,13-pentaazacyclopentadecane-1… | H3L | Aza macrocycles with car… | 18 | `O=C(O)CN1CCNC(=O)CN(CC(=O)O)CCN(CC(=O)O)CC(=O)NCC1` | (-inf, H4L, -1.4, H3L, 3.72, H2L, 7.22, HL, 7.42, L, +inf) |
| ligand_6112 | 1,4,8,12-Tetraazacyclopentadecane-N,N',N'… (PENTA) | H4L | Aza macrocycles with car… | 34 | `O=C(O)CN1CCCN(CC(=O)O)CCCN(CC(=O)O)CCN(CC(=O)O)CCC1` | (-inf, H5L, 2.59, H4L, 3.8, H3L, 5.68, H2L, 9.68, HL, 10.9, L, +inf) |
| ligand_6113 | 1-Oxa-4,7,10,13-tetraazacyclopentadecane-4,7,10,1… | H4L | Aza macrocycles with car… | 46 | `O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1` | (-inf, H4L, 2.69, H3L, 4.74, H2L, 9.03, HL, 10.33, L, +inf) |
| ligand_6114 | 1,4,7,10,13-Pentaazacyclopentadecane-N-met… (PCBA) | HL | Aza macrocycles with car… | 6 | `O=C(O)c1cccc(CN2CCNCCNCCNCCNCC2)c1` | (-inf, H4L, 3.6, H3L, 4.67, H2L, 9.31, HL, 9.76, L, +inf) |
| ligand_6115 | 1,4,7,10,13-Pentaazacyclopentadecane-N,N',… (PEPA) | H5L | Aza macrocycles with car… | 39 | `O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1` | (-inf, H5L, 3.19, H4L, 4.11, H3L, 6.14, H2L, 9.41, HL, 10.15, L, +inf) |
| ligand_6119 | 2,12,19,29-Tetraoxo-1,4,7,10,13,18,21,24,27,30-de… | *** | Aza macrocycles with car… | 13 | *** | (-inf, H6L, 3.23, H5L, 3.84, H4L, 4.5, H3L, 5.27, H2L, 9.18, HL, 9.7, L, +inf) |
| ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | NTA and derivatives | 534 | `O=C(O)CN(CC(=O)O)CC(=O)O` | (-inf, H4L, -1, H3L, -1, H2L, 2.52, HL, 9.46, L, +inf) |
| ligand_6294 | DL-Ethylenedinitrilo-N,N'-di(2-pentanoic)-N,N'-di… | H4L | EDTA and derivatives | 29 | `CCCC(C(=O)O)N(CCN(CC(=O)O)C(CCC)C(=O)O)CC(=O)O` | (-inf, H4L, -1.9, H3L, 2.79, H2L, 6.15, HL, 10.47, L, +inf) |
| ligand_6314 | Pentamethylenedinitrilotetraacetic acid | H4L | EDTA and derivatives | 93 | `O=C(O)CN(CCCCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, 2.31, H3L, 2.7, H2L, 9.44, HL, 10.54, L, +inf) |
| ligand_6325 | DL-(1-Carboxypentamethylene)dinitrilotetraacetic … | H5L | EDTA and derivatives | 41 | `O=C(O)CN(CCCCC(C(=O)O)N(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H5L, -1.8, H4L, 2.41, H3L, 3.07, H2L, 9.41, HL, 10.66, L, +inf) |
| ligand_6343 | N,N'-Diglycyl-1,2-diaminoethane-N'',N'',… (DGENTA) | H4L | EDTA and derivatives | 24 | `O=C(O)CN(CC(=O)O)CC(=O)NCCNC(=O)CN(CC(=O)O)CC(=O)O` | (-inf, H5L, -1.2, H4L, -1.2, H3L, 2.65, H2L, 6.15, HL, 7.28, L, +inf) |
| ligand_6344 | N,N'-Diglycyl-1,4-diaminobutane-N'',N'',… (DGBNTA) | H4L | EDTA and derivatives | 18 | `O=C(O)CN(CC(=O)O)CC(=O)NCCCCNC(=O)CN(CC(=O)O)CC(=O)O` | (-inf, H4L, 2, H3L, 2.55, H2L, 6.14, HL, 7.06, L, +inf) |
| ligand_6345 | N-(Glycylglycyl)-1,2-diaminoethane-N',N'… (GGENTA) | *** | EDTA and derivatives | 16 | *** | (-inf, H4L, 2.1, H3L, 2.9, H2L, 6.2, HL, 8.7, L, +inf) |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | H5L | EDTA and derivatives | 322 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O` | (-inf, H8L, -0.1, H7L, -0.1, H6L, -0.7, H5L, 2, H4L, 2.7, H3L, 4.28, H2L, 4.28, HL, -8.4, L, +inf) |
| ligand_6359 | Diethylenetrinitrilopentapropanoic acid (DTPP) | H5L | EDTA and derivatives | 61 | `O=C(O)CCN(CCC(=O)O)CCN(CCC(=O)O)CCN(CCC(=O)O)CCC(=O)O` | (-inf, H7L, 2.79, H6L, 3.24, H5L, 3.79, H4L, 4.23, H3L, 4.94, H2L, 8.78, HL, 9.61, L, +inf) |
| ligand_6362 | Diethylenetrinitrilopentaacetic acid N… (DTPA-BMA) | *** | EDTA and derivatives | 43 | *** | (-inf, H4L, -1.4, H3L, 3.31, H2L, 4.38, HL, 9.37, L, +inf) |

### Functional groups across all SQL matches (223 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 88 | 39% |
| secondary_amine | 81 | 36% |
| tertiary_amine | 60 | 27% |
| amide | 46 | 21% |
| primary_amine | 45 | 20% |
| hydroxyl | 38 | 17% |
| ether | 37 | 17% |
| aromatic_ring | 31 | 14% |
| thioether | 13 | 6% |
| phosphonate | 10 | 4% |
| pyridine | 9 | 4% |
| imine | 7 | 3% |
| ketone | 7 | 3% |
| ester | 6 | 3% |
| halide | 6 | 3% |
| thiol | 5 | 2% |
| oxime | 3 | 1% |
| phenol | 2 | 1% |
| phosphate | 2 | 1% |
| sulfonate | 1 | 0% |

---

### Step 15: `search_ligands`
**Args:**
```json
{
  "name": "DTPA",
  "limit": 50
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 50

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

### Step 16: `search_ligands`
**Args:**
```json
{
  "name": "TREN",
  "limit": 50
}
```

[summary]
## search_ligands — 7 result(s)

**stats:** 7 SQL matches · showing 7 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_7244 | 1,4,7,10,13-Pentaazatridecane (Tetraethylenepenta… | L | Aliphatic amines seconda… | 106 | `NCCNCCNCCNCCN` | (-inf, H5L, 2.97, H4L, 4.65, H3L, 8.1, H2L, 9.18, HL, 9.76, L, +inf) |
| ligand_7345 | Nitrilotris(ethyleneamine) [Tris(2-aminoet… (Tren) | L | Aliphatic amines tertiar… | 87 | `NCCN(CCN)CCN` | (-inf, H3L, 8.42, H2L, 9.43, HL, 10.13, L, +inf) |
| ligand_7352 | Nitrilotris(ethylenedimethylamin… (Hexamethyltren) | L | Aliphatic amines tertiar… | 24 | `CN(C)CCN(CCN(C)C)CCN(C)C` | (-inf, H3L, -7.44, H2L, -7.44, HL, -8.68, L, +inf) |
| ligand_7544 | 1,4,10,13,16,22,27,33-Octaazabicyclo[… (C-Bistren) | L | Aza-macrocycles | 14 | `C1CCNCCN2CCNCCCCCNCCN(CCNCC1)CCNCCCCCNCC2` | (-inf, H6L, 7.72, H5L, 8.14, H4L, 8.38, H3L, 8.87, H2L, 9.88, HL, 10.35, L, +inf) |
| ligand_7545 | 1,4,8,11,14,18,23,27-Octaaza-6,16,25(1,3)-tribenz… | L | Aza-macrocycles | 20 | `c1cc2cc(c1)CNCCN1CCNCc3cccc(c3)CNCCN(CCNC2)CCNCc2cccc(c2)CNCC1` | (-inf, H6L, 6.69, H5L, 7.21, H4L, 7.75, H3L, 8.76, H2L, 9.3, HL, 9.92, L, +inf) |
| ligand_7657 | 7,19,30-Trioxa-1,4,10,13,16,22,27,33-… (O-Bistren) | L | Aza-oxa-macrocycles | 84 | `C1COCCNCCN2CCNCCOCCNCCN(CCN1)CCNCCOCCNCC2` | (-inf, H6L, 6.58, H5L, 7.32, H4L, 7.91, H3L, 8.26, H2L, 9.24, HL, 9.9, L, +inf) |
| ligand_9417 | N,N',N''-Tris(2,3-dihydroxybenzoyl)nitr… (TRENCAM) | *** | Catechols | 7 | *** | (-inf, H7L, 5.88, H6L, 6.71, H5L, 8.61, H4L, 8.75, H3L, +inf) |

### Functional groups across all SQL matches (6 parseable SMILES)

| group | count | % |
|-------|-------|---|
| tertiary_amine | 5 | 83% |
| secondary_amine | 4 | 67% |
| primary_amine | 2 | 33% |
| aromatic_ring | 1 | 17% |
| ether | 1 | 17% |

---

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_33, metal_34) AND c.ligand_id IN (ligand_7029, ligand_7212, ligand_7345, ligand_7402, ligand_7425, ligand_7436, ligand_7439, ligand_6277, ligand_6165) AND s.solvent_name LIKE '%water%' AND s.constant_type LIKE '%logBeta%')",
  "order_by": "c.ligand_id ASC, c.metal_id ASC, s.constant_type ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 2000
}
```

[summary]
## search_stability

*(no results)*

---
