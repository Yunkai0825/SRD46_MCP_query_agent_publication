# Q2.1.2 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Mn(II), Fe(II), Co(II), Ni(II), Cu(II), Zn(II)",
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
  "name": "Ammonia, NH3",
  "limit": 10
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
  "symbol": "Mn, Fe, Co, Ni, Cu, Zn",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "formula": "NH3",
  "limit": 20
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 7: `build_system_catalog`
**Args:**
```json
{}
```

[summary]
[CATALOG]
## build_system_catalog

**Error:** Provide at least one of metal_id, ligand_id, or beta_definition_id.

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "c.metal_name_SRD IN ('Manganese(2+)','Iron(2+)','Cobalt(2+)','Nickel(2+)','Copper(2+)','Zinc(2+)') AND (c.ligand_name_SRD LIKE '%amm%' OR c.ligand_name_SRD = 'ammonia' OR c.ligand_SMILES = 'N') AND s.constant_type LIKE '%β1%'",
  "order_by": "c.metal_name_SRD ASC, s.constant_value DESC",
  "limit": 100
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 9: `search_metals`
**Args:**
```json
{
  "exclude": "",
  "limit": 10
}
```

[summary]
## search_metals — 10 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_1 | Ac^[3+] | Ac | 3 | ✓ | [Ac+3] | InChI=1S/Ac/q+3 | beta_totN_4 | ligand_totN_9 | vlm_totN_23 |
| metal_2 | Ag^[+] | Ag | 1 | ✓ | [Ag+] | InChI=1S/Ag/q+1 | beta_totN_68 | ligand_totN_649 | vlm_totN_2885 |
| metal_3 | Ag^[2+] | Ag | 2 | ✓ | [Ag+2] | InChI=1S/Ag/q+2 | beta_totN_1 | ligand_totN_5 | vlm_totN_5 |
| metal_4 | Ag^[3+] | Ag | 3 | ✓ | [Ag+3] | InChI=1S/Ag/q+3 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_5 | Al^[3+] | Al | 3 | ✓ | [Al+3] | InChI=1S/Al/q+3 | beta_totN_108 | ligand_totN_187 | vlm_totN_792 |
| metal_6 | Am^[3+] | Am | 3 | ✓ | [Am+3] | InChI=1S/Am/q+3 | beta_totN_13 | ligand_totN_46 | vlm_totN_190 |
| metal_7 | Am^[4+] | Am | 4 | ✓ | [Am+4] | InChI=1S/Am/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_8 | AmO_[2]^[2+] | Am | 2 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_9 | AmO_[2]^[+] | Am | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_10 | As^[3+] | As | 3 | ✓ | [As+3] | InChI=1S/As/q+3 | beta_totN_17 | ligand_totN_42 | vlm_totN_62 |

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "exclude": "",
  "limit": 20
}
```

[summary]
## search_ligands — 20 result(s)

**stats:** 5750 SQL matches · showing 20 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |
| ligand_5761 | L-2-Aminopropanoic acid (Alanine) | HL | Amino Acids | 159 | `C[C@H](N)C(=O)O` | (-inf, H2L, 2.33, HL, 9.71, L, +inf) |
| ligand_5762 | DL-2-Aminobutanoic acid | HL | Amino Acids | 53 | `CCC(N)C(=O)O` | (-inf, H2L, 2.3, HL, 9.63, L, +inf) |
| ligand_5763 | DL-2-Aminopentanoic acid (Norvaline) | HL | Amino Acids | 35 | `CCC[C@H](N)C(=O)O` | (-inf, H2L, 2.31, HL, 9.65, L, +inf) |
| ligand_5764 | DL-2-Aminohexanoic acid (Norleucine) | HL | Amino Acids | 33 | `CCCC[C@H](N)C(=O)O` | (-inf, H2L, 2.31, HL, 9.68, L, +inf) |
| ligand_5765 | L-2-Amino-3-methylbutanoic acid (Valine) | HL | Amino Acids | 81 | `CC(C)[C@H](N)C(=O)O` | (-inf, H2L, 2.27, HL, 9.52, L, +inf) |
| ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) | HL | Amino Acids | 49 | `CC(C)C[C@H](N)C(=O)O` | (-inf, H2L, 2.32, HL, 9.58, L, +inf) |
| ligand_5767 | L-2-Amino-3-methylpentanoic acid (Isoleucine) | HL | Amino Acids | 51 | `CC[C@H](C)[C@H](N)C(=O)O` | (-inf, H2L, 2.26, HL, 9.6, L, +inf) |
| ligand_5768 | D-allo-2-Amino-3-methylpentan… (D-allo-Isoleucine) | HL | Amino Acids | 16 | `CC[C@H](C)[C@@H](N)C(=O)O` | (-inf, H2L, 2.2, HL, 9.62, L, +inf) |
| ligand_5769 | 2-Amino-2-methylpropanoi… (2-Aminoisobutyric acid) | HL | Amino Acids | 41 | `CC(C)(N)C(=O)O` | (-inf, H2L, 2.34, HL, 10.1, L, +inf) |
| ligand_5770 | DL-2-Amino-4-pentenoic acid | HL | Amino Acids | 18 | `C=CCC(N)C(=O)O` | (-inf, H2L, 2.13, HL, 9.28, L, +inf) |
| ligand_5771 | DL-2-Amino-5-hexenoic acid | HL | Amino Acids | 15 | `C=CCCC(N)C(=O)O` | (-inf, H2L, 2.25, HL, 9.43, L, +inf) |
| ligand_5772 | DL-2-Amino-6-heptenoic acid | HL | Amino Acids | 15 | `C=CCCCC(N)C(=O)O` | (-inf, H2L, 2.34, HL, 9.52, L, +inf) |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) | HL | Amino Acids | 11 | `NC1(C(=O)O)CCCC1` | (-inf, H2L, 2.4, HL, 10.31, L, +inf) |
| ligand_5774 | 1-Aminocyclohexanecarboxylic acid | HL | Amino Acids | 11 | `NC1(C(=O)O)CCCCC1` | (-inf, H2L, 2.41, HL, 10.13, L, +inf) |
| ligand_5775 | 1-Aminocycloheptanecarboxylic acid | HL | Amino Acids | 11 | `NC1(C(=O)O)CCCCCC1` | (-inf, H2L, 2.59, HL, 10.46, L, +inf) |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | Amino Acids | 12 | `NC(C(=O)O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.92, L, +inf) |
| ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | HL | Amino Acids | 138 | `N[C@@H](Cc1ccccc1)C(=O)O` | (-inf, H2L, 2.18, HL, 9.09, L, +inf) |
| ligand_5778 | DL-2-Amino-3-chloropropanoic ac… (3-Chloroalanine) | HL | Amino Acids | 10 | `N[C@@H](CCl)C(=O)O` | (-inf, H2L, 2, HL, 8.18, L, +inf) |
| ligand_5779 | DL-2-Amino-3-chlorobutanoic acid | HL | Amino Acids | 8 | `CC(Cl)C(N)C(=O)O` | (-inf, H2L, -1.5, HL, 8.07, L, +inf) |

### Functional groups across all SQL matches (4054 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 1903 | 47% |
| carboxyl | 1693 | 42% |
| hydroxyl | 1430 | 35% |
| primary_amine | 1101 | 27% |
| tertiary_amine | 820 | 20% |
| amide | 756 | 19% |
| secondary_amine | 724 | 18% |
| phenol | 462 | 11% |
| pyridine | 428 | 11% |
| ether | 291 | 7% |
| halide | 268 | 7% |
| thioether | 261 | 6% |
| sulfonate | 203 | 5% |
| phosphonate | 181 | 4% |
| thiol | 119 | 3% |
| imine | 109 | 3% |
| phosphate | 99 | 2% |
| ester | 92 | 2% |
| ketone | 90 | 2% |
| oxime | 48 | 1% |
| aldehyde | 44 | 1% |
| nitrile | 39 | 1% |
| thiazole | 10 | 0% |
| imidazole | 8 | 0% |
| pyrazole | 8 | 0% |
| carboxylate | 1 | 0% |

---

### Step 11: `search_metals`
**Args:**
```json
{
  "symbol": "Mn",
  "limit": 20
}
```

[summary]
## search_metals — 4 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_94 | Mn^[2+] | Mn | 2 | ✓ | [Mn+2] | InChI=1S/Mn/q+2 | beta_totN_44 | ligand_totN_486 | vlm_totN_1273 |
| metal_95 | Mn^[3+] | Mn | 3 | ✓ | [Mn+3] | InChI=1S/Mn/q+3 | beta_totN_8 | ligand_totN_12 | vlm_totN_26 |
| metal_96 | Mn^[4+] | Mn | 4 | ✓ | [Mn+4] | InChI=1S/Mn/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_97 | MeNH_[3]^[+] | MNH3 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_5 | vlm_totN_9 |

---

### Step 12: `search_metals`
**Args:**
```json
{
  "symbol": "Fe",
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

### Step 13: `search_metals`
**Args:**
```json
{
  "symbol": "Co",
  "limit": 20
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

### Step 14: `search_metals`
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

### Step 15: `search_metals`
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

### Step 16: `search_metals`
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

### Step 17: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_94"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 57 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_311 | [ML(s)] <=> [M] + [L] | solid |
| beta_def_321 | [ML(s,rhodochrosite)] <=> [M] + [L] | solid |
| beta_def_334 | [ML2(s)] <=> [M] + [L]^2 | solid |
| beta_def_374 | [M]^2 + [L]^2 <=> [M2(H-1L)2] + [H]^2 |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_540 | [M]^2 + [L]^3 <=> [M2L3] |  |
| beta_def_732 | [M] + [H2L] <=> [MH2L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_823 | [M] + [H2L] <=> [ML] + [H]^2 |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_853 | [ML] + [H2L] <=> [ML2] + [H]^2 |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_876 | [ML2] + [H2L] <=> [ML3] + [H]^2 |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |

*(all species aqueous unless noted)*

**1. Mn^[2+] + Ammonia** (metal_94 + ligand_10103) — ligand_def_HxL: L | 32 ent, 4 sp, 32 vlms (vlm_173099…vlm_173130)
   - species: beta_def_812(8) beta_def_840(8) beta_def_872(8) beta_def_894(8)
   - eq:6 nets T:19~30°C I:-0.05~5.15M max 4n/6e
**2. Mn^[2+] + Aminoacetic acid (Glycine)** (metal_94 + ligand_5760) — ligand_def_HxL: HL | 14 ent, 2 sp, 14 vlms (vlm_93733…vlm_93746)
   - species: beta_def_812(11) beta_def_840(3)
   - eq:6 nets T:5~45°C I:-0.15~0.65M max 2n/1e
**3. Mn^[2+] + Nitrate ion** (metal_94 + ligand_10109) — ligand_def_HxL: *** | 12 ent, 2 sp, 12 vlms (vlm_173955…vlm_173966)
   - species: beta_def_812(6) beta_def_840(6)
   - eq:6 nets T:19~30°C I:-0.05~4.15M max 2n/1e
**4. Mn^[2+] + Hydroxide ion** (metal_94 + ligand_10076) — ligand_def_HxL: *** | 12 ent, 5 sp, 12 vlms (vlm_170660…vlm_170671)
   - species: beta_def_334(1) beta_def_502(2) beta_def_540(2) beta_def_812(6) beta_def_894(1)
   - eq:4 nets T:19~30°C I:-0.15~2.15M max 5n/10e
**5. Mn^[2+] + L-2-Amino-3-(4-hydroxyphenyl)propanoic acid (Tyrosine)** (metal_94 + ligand_5819) — ligand_def_HxL: H2L | 12 ent, 4 sp, 12 vlms (vlm_96246…vlm_96257)
   - species: beta_def_194(3) beta_def_204(3) beta_def_779(3) beta_def_792(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 4n/3e
**6. Mn^[2+] + DL-2-Amino-3-(3-hydroxyphenyl)propanoic acid (m-Tyrosine)** (metal_94 + ligand_5818) — ligand_def_HxL: H2L | 12 ent, 4 sp, 12 vlms (vlm_96152…vlm_96163)
   - species: beta_def_194(3) beta_def_204(3) beta_def_779(3) beta_def_792(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 4n/3e
**7. Mn^[2+] + 5-Hydroxy-2-hydroxymethyl-4-pyrone (Kojic acid)** (metal_94 + ligand_9593) — ligand_def_HxL: HL | 11 ent, 3 sp, 11 vlms (vlm_166471…vlm_166481)
   - species: beta_def_812(4) beta_def_840(4) beta_def_872(3)
   - eq:2 nets T:19~30°C I:-0.05~2.15M max 3n/3e
**8. Mn^[2+] + Ethylenediamine** (metal_94 + ligand_7029) — ligand_def_HxL: L | 11 ent, 3 sp, 11 vlms (vlm_122330…vlm_122340)
   - species: beta_def_812(4) beta_def_840(4) beta_def_872(3)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**9. Mn^[2+] + Hydrogen fluoride (Hydrofluoric acid)** (metal_94 + ligand_10162) — ligand_def_HxL: HL | 10 ent, 1 sp, 10 vlms (vlm_176944…vlm_176953)
   - species: beta_def_812(10)
   - eq:6 nets T:19~30°C I:-0.15~3.15M max 1n/0e
**10. Mn^[2+] + Hydrogen sulfate ion (Sulfuric acid)** (metal_94 + ligand_10148) — ligand_def_HxL: HL | 10 ent, 1 sp, 10 vlms (vlm_176001…vlm_176010)
   - species: beta_def_812(10)
   - eq:6 nets T:19~30°C I:-0.05~4.15M max 1n/0e
**11. Mn^[2+] + Hydrogen carbonate (Carbonic acid)** (metal_94 + ligand_10096) — ligand_def_HxL: H2L | 10 ent, 4 sp, 10 vlms (vlm_172852…vlm_172861)
   - species: beta_def_311(3) beta_def_321(1) beta_def_779(4) beta_def_812(2)
   - eq:3 nets T:19~30°C I:-0.05~3.15M max 4n/6e
**12. Mn^[2+] + Pentane-2,4-dione (Acetylacetone)** (metal_94 + ligand_9526) — ligand_def_HxL: *** | 10 ent, 2 sp, 10 vlms (vlm_165373…vlm_165382)
   - species: beta_def_812(5) beta_def_840(5)
   - eq:3 nets T:19~30°C I:-0.15~1.15M max 2n/1e
**13. Mn^[2+] + 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron)** (metal_94 + ligand_9358) — ligand_def_HxL: H4L | 10 ent, 4 sp, 10 vlms (vlm_162048…vlm_162057)
   - species: beta_def_788(3) beta_def_823(3) beta_def_853(2) beta_def_876(2)
   - eq:3 nets T:19~30°C I:-0.15~1.15M max 4n/6e
**14. Mn^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_94 + ligand_9058) — ligand_def_HxL: H3L | 10 ent, 4 sp, 10 vlms (vlm_157609…vlm_157618)
   - species: beta_def_374(2) beta_def_732(1) beta_def_779(2) beta_def_812(5)
   - eq:5 nets T:19~41°C I:-0.05~0.3M max 4n/6e
**15. Mn^[2+] + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine)** (metal_94 + ligand_5898) — ligand_def_HxL: HL | 10 ent, 2 sp, 10 vlms (vlm_98771…vlm_98780)
   - species: beta_def_812(5) beta_def_840(5)
   - eq:3 nets T:19~41°C I:-0.05~3.15M max 2n/1e
**16. Mn^[2+] + L-2-Amino-3-hydroxypropanoic acid (Serine)** (metal_94 + ligand_5828) — ligand_def_HxL: HL | 10 ent, 2 sp, 10 vlms (vlm_96529…vlm_96538)
   - species: beta_def_812(5) beta_def_840(5)
   - eq:3 nets T:19~41°C I:-0.05~3.15M max 2n/1e
**17. Mn^[2+] + 3-Hydroxy-2-methyl-4-pyrone (Maltol)** (metal_94 + ligand_9586) — ligand_def_HxL: HL | 9 ent, 3 sp, 9 vlms (vlm_166200…vlm_166208)
   - species: beta_def_812(3) beta_def_840(3) beta_def_872(3)
   - eq:1 nets T:16.5~31.5°C I:1.775~2.225M max 3n/3e
**18. Mn^[2+] + Adenosine-5'-(trihydrogendiphosphate) (ADP)** (metal_94 + ligand_8318) — ligand_def_HxL: H3L | 9 ent, 2 sp, 9 vlms (vlm_141334…vlm_141342)
   - species: beta_def_779(1) beta_def_812(8)
   - eq:4 nets T:19~41°C I:-0.05~0.3M max 2n/1e
**19. Mn^[2+] + 1,10-Phenanthroline (Dipyridino[a,c]benzene)** (metal_94 + ligand_8191) — ligand_def_HxL: L | 9 ent, 3 sp, 9 vlms (vlm_139257…vlm_139265)
   - species: beta_def_812(3) beta_def_840(3) beta_def_872(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 3n/3e
**20. Mn^[2+] + Nitrilotriacetic acid (NTA)** (metal_94 + ligand_6165) — ligand_def_HxL: H3L | 9 ent, 2 sp, 9 vlms (vlm_105486…vlm_105494)
   - species: beta_def_812(5) beta_def_840(4)
   - eq:3 nets T:15~30°C I:-0.15~0.25M max 2n/1e

---

### Step 19: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND c.metal_id IN (metal_94, metal_62, metal_33, metal_112, metal_41, metal_208) AND s.solvent_name = 'water' AND s.temperature_c >= 20 AND s.temperature_c <= 30 AND s.ionic_strength_mol_l >= 0 AND s.ionic_strength_mol_l <= 0.1)",
  "order_by": "c.metal_name_SRD ASC, ABS(s.temperature_c - 25) ASC, s.ionic_strength_mol_l ASC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 20: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND c.metal_id IN (metal_94, metal_62, metal_33, metal_112, metal_41, metal_208) AND s.temperature_c >= 20 AND s.temperature_c <= 30)",
  "order_by": "c.metal_name_SRD ASC, ABS(s.temperature_c - 25) ASC, s.ionic_strength_mol_l ASC",
  "limit": 100
}
```

[summary]
## search_stability — 53 row(s)

### logK — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 6 | 1 | 25 | 0~6 | *** | 6 |
| metal_94 | Mn^[2+] | ligand_10103 | Ammonia | L | N | 6 | 1 | 25 | 0~5 | *** | 6 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 5 | 1 | 25 | 0~5 | *** | 5 |
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 5 | 1 | 25 | 0~3 | *** | 5 |
| metal_112 | Ni^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~2 | *** | 4 |
| metal_208 | Zn^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~2 | *** | 4 |

### ΔH — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~3 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~3 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 27 | 2 | *** | 0 |

### ΔS — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~3 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_10103 | Ammonia | L | N | 3 | 1 | 25 | 0~2 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |

---

### Step 21: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND c.metal_id IN (metal_94, metal_62, metal_33, metal_112, metal_41, metal_208))",
  "order_by": "c.metal_name_SRD ASC, ABS(s.temperature_c - 25) ASC, s.ionic_strength_mol_l ASC",
  "limit": 100
}
```

[summary]
## search_stability — 53 row(s)

### logK — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 6 | 1 | 25 | 0~6 | *** | 6 |
| metal_94 | Mn^[2+] | ligand_10103 | Ammonia | L | N | 6 | 1 | 25 | 0~5 | *** | 6 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 5 | 1 | 25 | 0~5 | *** | 5 |
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 5 | 1 | 25 | 0~3 | *** | 5 |
| metal_112 | Ni^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~2 | *** | 4 |
| metal_208 | Zn^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~2 | *** | 4 |

### ΔH — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~3 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~3 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 27 | 2 | *** | 0 |

### ΔS — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~3 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_10103 | Ammonia | L | N | 3 | 1 | 25 | 0~2 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |

---
