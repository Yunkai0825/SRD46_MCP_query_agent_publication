# Q5.1.5 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "iron(III), iron(II), copper(II), zinc(II), calcium(II), magnesium(II), lead(II), nickel(II), cobalt(II), aluminum(III)",
  "limit": 20
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
  "name": "EDTA, ethylenediaminetetraacetic acid",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 5: `build_system_catalog`
**Args:**
```json
{}
```

[summary]
[CATALOG]
## build_system_catalog

**Error:** Provide at least one of metal_id, ligand_id, or beta_definition_id.

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine",
  "limit": 20
}
```

[summary]
## search_ligands — 20 result(s)

**stats:** 105 SQL matches · showing 20 · limit 20

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
  "formula": "C10H16N2O8",
  "limit": 20
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 3 SQL matches · showing 3 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5984 | Ethylenediiminodibutanedioic acid (EDDS) | H4L | Amino Acids | 108 | `O=C(O)CC(NCCNC(CC(=O)O)C(=O)O)C(=O)O` | (-inf, H4L, 2.95, H3L, 3.86, H2L, 6.84, HL, 10.01, L, +inf) |
| ligand_5986 | meso-(1,2-Dimethylethylene)diiminodipropanedioic … | H4L | Amino Acids | 22 | `C[C@H](NC(C(=O)O)C(=O)O)[C@@H](C)NC(C(=O)O)C(=O)O` | (-inf, H4L, 2.34, H3L, 2.75, H2L, 6.06, HL, 9.94, L, +inf) |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | EDTA and derivatives | 596 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H5L, -1.5, H4L, 2, H3L, 2.69, H2L, 6.13, HL, 9.52, L, +inf) |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 3 | 100% |
| secondary_amine | 2 | 67% |
| tertiary_amine | 1 | 33% |

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediaminetetraacetic acid",
  "limit": 20
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | EDTA and derivatives | 596 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H5L, -1.5, H4L, 2, H3L, 2.69, H2L, 6.13, HL, 9.52, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| tertiary_amine | 1 | 100% |

---

### Step 9: `search_metals`
**Args:**
```json
{
  "symbol": "Fe, Cu, Zn, Ca, Mg, Pb, Ni, Co, Al",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 10: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_6277"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 66 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_32 | [HL] + [H] <=> [H2L] |  |
| beta_def_53 | [H2L] + [H] <=> [H3L] |  |
| beta_def_64 | [H3L] + [H] <=> [H4L] |  |
| beta_def_68 | [H4L] + [H] <=> [H5L] |  |
| beta_def_72 | [H5L] + [H] <=> [H6L] |  |
| beta_def_79 | [L] + [H] <=> [HL] |  |
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_423 | [ML]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_427 | [M(OH)L]^2 <=> [M2(OH)2L2] |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_536 | [M2L] + [L] <=> [M2L2] |  |
| beta_def_570 | [M2(OH)L] + [H] <=> [M2L] + [H2O] |  |
| beta_def_662 | [M]^4 + [L]^2 + [H2O]^4 <=> [M4(OH)4L2] + [H]^4 |  |
| beta_def_699 | [M]^6 + [L]^3 + [H2O]^4 <=> [M6(OH)4L3] + [H]^4 |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_751 | [MH2L] + [H] <=> [MH3L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |

*(all species aqueous)*

**1. H^[+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_68 + ligand_6277) — ligand_def_HxL: H4L | 75 ent, 6 sp, 75 vlms (vlm_108224…vlm_108298)
   - species: beta_def_32(18) beta_def_53(10) beta_def_64(7) beta_def_68(6) beta_def_72(4) beta_def_79(30)
   - eq:14 nets T:19~41°C I:-0.15~3.15M max 6n/15e
**2. Cd^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_26 + ligand_6277) — ligand_def_HxL: H4L | 23 ent, 4 sp, 23 vlms (vlm_108725…vlm_108747)
   - species: beta_def_739(1) beta_def_788(5) beta_def_812(14) beta_def_966(3)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 4n/5e
**3. Cu^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_41 + ligand_6277) — ligand_def_HxL: H4L | 20 ent, 4 sp, 20 vlms (vlm_108604…vlm_108623)
   - species: beta_def_739(2) beta_def_788(4) beta_def_812(8) beta_def_966(6)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 4n/5e
**4. Ni^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_112 + ligand_6277) — ligand_def_HxL: H4L | 19 ent, 4 sp, 19 vlms (vlm_108585…vlm_108603)
   - species: beta_def_739(1) beta_def_788(4) beta_def_812(8) beta_def_966(6)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**5. Zn^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_208 + ligand_6277) — ligand_def_HxL: H4L | 18 ent, 4 sp, 18 vlms (vlm_108707…vlm_108724)
   - species: beta_def_739(1) beta_def_788(5) beta_def_812(6) beta_def_966(6)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 4n/5e
**6. Mg^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_92 + ligand_6277) — ligand_def_HxL: H4L | 18 ent, 2 sp, 18 vlms (vlm_108326…vlm_108343)
   - species: beta_def_788(2) beta_def_812(16)
   - eq:6 nets T:19~41°C I:-0.05~1.15M max 2n/1e
**7. Ca^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_25 + ligand_6277) — ligand_def_HxL: H4L | 18 ent, 2 sp, 18 vlms (vlm_108344…vlm_108361)
   - species: beta_def_788(2) beta_def_812(16)
   - eq:6 nets T:19~41°C I:-0.05~1.15M max 2n/1e
**8. Fe^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_61 + ligand_6277) — ligand_def_HxL: H4L | 14 ent, 4 sp, 14 vlms (vlm_108639…vlm_108652)
   - species: beta_def_427(3) beta_def_788(3) beta_def_812(4) beta_def_966(4)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**9. VO_[2]^[+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_202 + ligand_6277) — ligand_def_HxL: H4L | 13 ent, 4 sp, 13 vlms (vlm_108673…vlm_108685)
   - species: beta_def_739(5) beta_def_751(1) beta_def_788(5) beta_def_812(2)
   - eq:3 nets T:19~30°C I:-0.05~3.15M max 4n/4e
**10. Co^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_33 + ligand_6277) — ligand_def_HxL: H4L | 13 ent, 3 sp, 13 vlms (vlm_108572…vlm_108584)
   - species: beta_def_739(1) beta_def_788(4) beta_def_812(8)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 2n/1e
**11. Al^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_5 + ligand_6277) — ligand_def_HxL: H4L | 13 ent, 4 sp, 13 vlms (vlm_108770…vlm_108782)
   - species: beta_def_238(2) beta_def_788(4) beta_def_812(3) beta_def_966(4)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 4n/5e
**12. La^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_79 + ligand_6277) — ligand_def_HxL: H4L | 12 ent, 2 sp, 12 vlms (vlm_108389…vlm_108400)
   - species: beta_def_788(3) beta_def_812(9)
   - eq:4 nets T:15~30°C I:-0.05~1.15M max 2n/1e
**13. Nd^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_110 + ligand_6277) — ligand_def_HxL: H4L | 11 ent, 2 sp, 11 vlms (vlm_108416…vlm_108426)
   - species: beta_def_788(2) beta_def_812(9)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 2n/1e
**14. Hg^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_71 + ligand_6277) — ligand_def_HxL: H4L | 11 ent, 4 sp, 11 vlms (vlm_108748…vlm_108758)
   - species: beta_def_739(1) beta_def_788(4) beta_def_812(5) beta_def_966(1)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**15. Eu^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_58 + ligand_6277) — ligand_def_HxL: H4L | 11 ent, 2 sp, 11 vlms (vlm_108438…vlm_108448)
   - species: beta_def_788(1) beta_def_812(10)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 1n/0e
**16. UO_[2]^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_195 + ligand_6277) — ligand_def_HxL: H4L | 10 ent, 6 sp, 10 vlms (vlm_108542…vlm_108551)
   - species: beta_def_502(2) beta_def_536(1) beta_def_570(1) beta_def_662(1) beta_def_699(1) beta_def_779(4)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 6n/13e
**17. Th^[4+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_185 + ligand_6277) — ligand_def_HxL: H4L | 10 ent, 4 sp, 10 vlms (vlm_108521…vlm_108530)
   - species: beta_def_423(2) beta_def_788(3) beta_def_812(4) beta_def_966(1)
   - eq:3 nets T:15~30°C I:-0.05~0.65M max 4n/6e
**18. Sm^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_173 + ligand_6277) — ligand_def_HxL: H4L | 10 ent, 2 sp, 10 vlms (vlm_108428…vlm_108437)
   - species: beta_def_788(1) beta_def_812(9)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 1n/0e
**19. Sr^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_177 + ligand_6277) — ligand_def_HxL: H4L | 9 ent, 2 sp, 9 vlms (vlm_108362…vlm_108370)
   - species: beta_def_788(1) beta_def_812(8)
   - eq:2 nets T:20~41°C I:-0.05~0.3M max 2n/1e
**20. Na^[+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_106 + ligand_6277) — ligand_def_HxL: H4L | 9 ent, 1 sp, 9 vlms (vlm_108307…vlm_108315)
   - species: beta_def_812(9)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 1n/0e

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812 AND c.metal_id IN (metal_25, metal_92, metal_41, metal_208, metal_112, metal_61, metal_5))",
  "order_by": "c.metal_name_SRD ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 61 row(s)

### ΔH — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 1 | 15~35 | 0~1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 1 | 15~35 | 0~1 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 1 | 15~35 | 0~1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 1 | 15~35 | 0~1 | *** | 0 |
| metal_5 | Al^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔS — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_5 | Al^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 1 | 25~37 | 0.1~1 | *** | 6 |
| metal_92 | Mg^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 1 | 25~37 | 0.1~1 | *** | 6 |
| metal_208 | Zn^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 1 | 25 | 0~1 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_5 | Al^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

---

### Step 13: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_6277"
}
```

[summary]
## inspect_card — Ligand | ligand_6277

**Name:** Ethylenedinitrilotetraacetic acid (EDTA)  
**Formula:** C10H16N2O8 | **Class:** EDTA and derivatives  
**SMILES:** `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O`  
**InChI:** `InChI=1S/C10H16N2O8/c13-7(14)3-11(4-8(15)16)1-2-12(5-9(17)18)6-10(19)20/h1-6H2,(H,13,14)(H,15,16)(H,17,18)(H,19,20)`  
**HxL definition:** H4L  

**pKa values:** 5

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_108289 | -1.50 | 25.0 | 0.1 | H4L → H5L | *** | *** | *** |
| vlm_108282 | 2.00 | 25.0 | 0.1 | H3L → H4L | *** | *** | *** |
| vlm_108272 | 2.69 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_108254 | 6.13 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_108224 | 9.52 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 75 metal(s), 596 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 75 |
| metal_26 | Cd^[2+] | 23 |
| metal_41 | Cu^[2+] | 20 |
| metal_112 | Ni^[2+] | 19 |
| metal_208 | Zn^[2+] | 18 |
| … | *(showing top 5 of 75)* | |

---
