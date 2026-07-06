# Q4.7 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "cobalt"
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
  "name": "ethylenediamine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 105 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5948 | N-(2-Aminoethyl)glycine (Ethylenediamine m… (EDMA) | HL | Amino Acids | 30 | `NCCNCC(=O)O` | (-inf, H3L, -1.9, H2L, 6.67, HL, 9.84, L, +inf) |
| ligand_6253 | N-(2-Aminoeth… (Ethylenediamine-N,N-diacetic acid) | H2L | NTA and derivatives | 39 | `NCCN(CC(=O)O)CC(=O)O` | (-inf, H2L, 5.53, HL, 10.87, L, +inf) |
| ligand_7029 | Ethylenediamine | L | Aliphatic amines | 310 | `NCCN` | (-inf, H2L, 7.11, HL, 9.92, L, +inf) |
| ligand_7030 | DL-Methylethylenediamine (1,2-Propylenediami… (pn) | L | Aliphatic amines | 86 | `CC(N)CN` | (-inf, H2L, 6.85, HL, 9.81, L, +inf) |
| ligand_7031 | DL-Ethylethylenediamine (1,2-Butylenediamine) | L | Aliphatic amines | 19 | `CCC(N)CN` | (-inf, H2L, 6.65, HL, 9.66, L, +inf) |

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

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "ammonia",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10103 | Ammonia | L | Inorganic ligands | 447 | `N` | (-inf, HL, 9.26, L, +inf) |

---

### Step 5: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_34"
}
```

[summary]
[CATALOG]
## build_system_catalog — 19 pair(s), 40 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_263 | [M(OH)3L] + [H] <=> [M(OH)2L] + [H2O] |  |
| beta_def_352 | [ML3(s)] <=> [M] + [L]^3 | solid |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_871 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_882 | [H] + [M(OH)L3(fac)] <=> [ML3] + [H2O] |  |
| beta_def_888 | [ML2] + [L] <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_895 | [H] + [M(OH)L4(cis)] <=> [ML4] + [H2O] |  |
| beta_def_905 | [ML4] + [L] <=> [ML5] |  |
| beta_def_906 | *** |  |
| beta_def_907 | [M] + [L]^6 <=> [ML6] |  |
| beta_def_909 | [ML5] + [L] <=> [ML6] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_986 | [M(OH)2L2] + [H] <=> [M(OH)L2] + [H2O] |  |
| beta_def_991 | [H] + [M(OH)2L3(fac)] <=> [M(OH)L3] + [H2O] |  |
| beta_def_993 | [H] + [M(OH)2L4(cis)] <=> [M(OH)L4] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Co^[3+] + Ammonia** (metal_34 + ligand_10103) — ligand_def_HxL: L | 14 ent, 8 sp, 14 vlms (vlm_173305…vlm_173318)
   - species: beta_def_882(1) beta_def_895(1) beta_def_905(3) beta_def_906(1) beta_def_907(2) beta_def_909(4) beta_def_991(1) beta_def_993(1)
   - eq:6 nets T:19~35°C I:-0.05~2.15M max 4n/6e
**2. Co^[3+] + Ethylenediamine** (metal_34 + ligand_7029) — ligand_def_HxL: L | 8 ent, 4 sp, 8 vlms (vlm_122454…vlm_122461)
   - species: beta_def_871(3) beta_def_872(1) beta_def_888(1) beta_def_986(3)
   - eq:3 nets T:16.5~31.5°C I:0.775~1.225M max 4n/3e
**3. Co^[3+] + Chloride ion** (metal_34 + ligand_10163) — ligand_def_HxL: *** | 4 ent, 1 sp, 4 vlms (vlm_177403…vlm_177406)
   - species: beta_def_812(4)
   - eq:2 nets T:16.5~31.5°C I:0.275~3.225M max 1n/0e
**4. Co^[3+] + Hydrogen azide (Hydrazoic acid)** (metal_34 + ligand_10106) — ligand_def_HxL: HL | 4 ent, 4 sp, 4 vlms (vlm_173620…vlm_173623)
   - species: beta_def_812(1) beta_def_840(1) beta_def_872(1) beta_def_894(1)
   - eq:1 nets T:16.5~31.5°C I:1.775~2.225M max 4n/6e
**5. Co^[3+] + Hydroxide ion** (metal_34 + ligand_10076) — ligand_def_HxL: *** | 4 ent, 2 sp, 4 vlms (vlm_170829…vlm_170832)
   - species: beta_def_352(3) beta_def_812(1)
   - eq:2 nets T:19~30°C I:-0.05~3.15M max 1n/0e
**6. Co^[3+] + 2,6-Bis(aminomethyl)pyridine** (metal_34 + ligand_8110) — ligand_def_HxL: L | 3 ent, 3 sp, 3 vlms (vlm_137656, vlm_137657, vlm_137658)
   - species: beta_def_238(1) beta_def_263(1) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 3n/3e
**7. Co^[3+] + cis,cis-1,3,5-Triaminocyclohexane** (metal_34 + ligand_7096) — ligand_def_HxL: L | 3 ent, 3 sp, 3 vlms (vlm_124184, vlm_124185, vlm_124186)
   - species: beta_def_238(1) beta_def_263(1) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 3n/3e
**8. Co^[3+] + Nitrilotris(ethyleneamine) [Tris(2-aminoethyl)amine] (Tren)** (metal_34 + ligand_7345) — ligand_def_HxL: L | 2 ent, 2 sp, 2 vlms (vlm_128135, vlm_128136)
   - species: beta_def_238(1) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 2n/1e
**9. Co^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_34 + ligand_6277) — ligand_def_HxL: H4L | 2 ent, 2 sp, 2 vlms (vlm_108653, vlm_108654)
   - species: beta_def_788(1) beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 2n/1e
**10. Co^[3+] + Nitrilotriacetic acid (NTA)** (metal_34 + ligand_6165) — ligand_def_HxL: H3L | 2 ent, 2 sp, 2 vlms (vlm_105569, vlm_105570)
   - species: beta_def_238(1) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 2n/1e
**11. Co^[3+] + Triethylenetetranitrilohexaacetic acid (TTHA)** (metal_34 + ligand_6366) — ligand_def_HxL: H6L | 1 ent, 1 sp, 1 vlms (vlm_113179)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**12. Co^[3+] + (2-Hydroxytrimethylene)dinitrilotetraacetic acid** (metal_34 + ligand_6333) — ligand_def_HxL: H4L | 1 ent, 1 sp, 1 vlms (vlm_111656)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**13. Co^[3+] + Tetramethylenedinitrilotetraacetic acid** (metal_34 + ligand_6313) — ligand_def_HxL: H4L | 1 ent, 1 sp, 1 vlms (vlm_110747)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**14. Co^[3+] + Trimethylenedinitrilotetraacetic acid (TMDTA)** (metal_34 + ligand_6311) — ligand_def_HxL: H4L | 1 ent, 1 sp, 1 vlms (vlm_110544)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**15. Co^[3+] + trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA)** (metal_34 + ligand_6301) — ligand_def_HxL: H4L | 1 ent, 1 sp, 1 vlms (vlm_109807)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**16. Co^[3+] + meso-(1,2-Dimethylethylene)dinitrilotetraacetic acid** (metal_34 + ligand_6288) — ligand_def_HxL: H4L | 1 ent, 1 sp, 1 vlms (vlm_109254)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**17. Co^[3+] + DL-(Methylethylene)dinitrilotetraacetic acid (PDTA)** (metal_34 + ligand_6278) — ligand_def_HxL: H4L | 1 ent, 1 sp, 1 vlms (vlm_108903)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**18. Co^[3+] + N-(2-Hydroxyethyl)ethylenedinitrilotriacetic acid (HEDTA)** (metal_34 + ligand_6275) — ligand_def_HxL: H3L | 1 ent, 1 sp, 1 vlms (vlm_108147)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**19. Co^[3+] + Iminodiacetic acid (IDA)** (metal_34 + ligand_6127) — ligand_def_HxL: H2L | 1 ent, 1 sp, 1 vlms (vlm_104405)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "EDTA",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 5

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

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "diethylenetriamine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 20 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5958 | Diethylenetriamine-N(1)-acetic acid | HL | Amino Acids | 15 | `NCCNCCNCC(=O)O` | (-inf, H4L, -1.3, H3L, 4.32, H2L, 8.7, HL, 9.92, L, +inf) |
| ligand_7212 | 1,4,7-Triazaheptane (Diethylenetriamine)(dien)(2,… | L | Aliphatic amines seconda… | 126 | `NCCNCCN` | (-inf, H3L, 4.25, H2L, 9.02, HL, 9.84, L, +inf) |
| ligand_7217 | 1,4,7-Triazaoctane (N(1)-Methyldiethylenetriamine) | L | Aliphatic amines seconda… | 24 | `CNCCNCCN` | (-inf, H3L, -3.3, H2L, 9.18, HL, 9.18, L, +inf) |
| ligand_7219 | 3,6,9-Triazaund… (N,N''-Diethyldiethylenetriamine) | L | Aliphatic amines seconda… | 6 | `CCNCCNCCNCC` | (-inf, H3L, 4.31, H2L, 9.85, HL, 10.51, L, +inf) |
| ligand_7220 | 3,6,9-Triazaundecane dinitrile (N,N''-Bis(cyanoet… | L | Aliphatic amines seconda… | 6 | `N#CCCNCCNCCNCCC#N` | (-inf, H3L, 3.65, H2L, 5.83, HL, 8.86, L, +inf) |

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
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_7224 | 1,4,7,10-Tetraazadecane (Triethylenetetramine)(tr… | L | Aliphatic amines seconda… | 127 | `NCCNCCNCCN` | (-inf, H4L, 3.27, H3L, 6.58, H2L, 9.07, HL, 9.75, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 1 | 100% |
| secondary_amine | 1 | 100% |

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_34 AND c.ligand_id IN (ligand_10103, ligand_7029, ligand_6277, ligand_6165, ligand_6127, ligand_7345))",
  "order_by": "c.ligand_id, s.constant_value DESC",
  "limit": 60
}
```

[summary]
## search_stability — 29 row(s)

### logK — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_34 | Co^[3+] | ligand_10103 | Ammonia | L | N | 10 | 8 | 20~30 | 0.1~2 | *** | 5 |
| metal_34 | Co^[3+] | ligand_7029 | Ethylenediamine | L | NCCN | 8 | 4 | 25~30 | 1 | *** | 3 |
| metal_34 | Co^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_34 | Co^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 20~25 | 0.1 | *** | 1 |
| metal_34 | Co^[3+] | ligand_7345 | Nitrilotris(ethyleneamine) … | L | NCCN(CCN)CCN | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_34 | Co^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_34 | Co^[3+] | ligand_10103 | Ammonia | L | N | 2 | 2 | 25 | 0 | *** | 0 |

### ΔS — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_34 | Co^[3+] | ligand_10103 | Ammonia | L | N | 2 | 2 | 25 | 2 | *** | 0 |

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_33 AND c.ligand_id IN (ligand_10103, ligand_7029, ligand_6277, ligand_6165, ligand_6127, ligand_7345) AND c.beta_definition_name LIKE '%ML%')",
  "order_by": "c.ligand_id, s.constant_value DESC",
  "limit": 60
}
```

[summary]
## search_stability — 60 row(s)

### ΔS — 5 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 4 | 2 | 25 | 0.1~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 3 | 3 | 25 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7345 | Nitrilotris(ethyleneamine) … | L | NCCN(CCN)CCN | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 9 | 3 | 25~37 | 0.1~1 | *** | 3 |
| metal_33 | Co^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 4 | 2 | 25 | 0.1~1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 2 | 25 | 0.1~1 | *** | 2 |

### ΔH — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 11 | 2 | 15~35 | 0~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 7 | 3 | 20~25 | 0.1~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 7 | 2 | 15~35 | 0~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 3 | 3 | 25 | 1 | *** | 0 |

---
