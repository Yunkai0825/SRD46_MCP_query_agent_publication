# Q3.2.6 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Cu, copper, Cu(II), H+",
  "limit": 10
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
  "name": "malonic acid, malonate",
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
  "symbol": "Cu, H",
  "limit": 10
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
  "formula": "C3H4O4, C3H2O4",
  "limit": 10
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

### Step 8: `search_pka_ligands`
**Args:**
```json
{
  "where": "lc.ligand_name_SRD LIKE '%malon%'",
  "order_by": "lc.ligand_name_SRD ASC",
  "limit": 20
}
```

[PHASE ERROR] Tool 'search_pka_ligands' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 9: `search_metals`
**Args:**
```json
{
  "exclude": [],
  "limit": 20
}
```

[TOOL ERROR] search_metals: Error executing tool search_metals: 1 validation error for search_metalsArguments
exclude
  Input should be a valid string [type=string_type, input_value=[], input_type=list]
    For further information visit https://errors.pydantic.dev/2.11/v/string_type

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "include_groups": [],
  "exclude_groups": [],
  "limit": 50
}
```

[summary]
## search_ligands — 50 result(s)

**stats:** 5750 SQL matches · showing 50 · limit 50

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
| ligand_5780 | DL-2-Amino-3-(2-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1ccccc1F)C(=O)O` | (-inf, H2L, 2.12, HL, 9.01, L, +inf) |
| ligand_5781 | DL-2-Amino-3-(3-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1cccc(F)c1)C(=O)O` | (-inf, H2L, 2.1, HL, 8.98, L, +inf) |
| ligand_5782 | DL-2-Amino-3-(4-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1ccc(F)cc1)C(=O)O` | (-inf, H2L, 2.13, HL, 9.05, L, +inf) |
| ligand_5783 | DL-2-Amino-3-(2-chlorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 2 | `N[C@@H](Cc1ccccc1Cl)C(=O)O` | (-inf, H2L, 2.23, HL, 8.94, L, +inf) |
| ligand_5784 | DL-2-Amino-3-(3-chlorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 2 | `N[C@@H](Cc1cccc(Cl)c1)C(=O)O` | (-inf, H2L, 2.17, HL, 8.91, L, +inf) |
| ligand_5785 | DL-2-Amino-3-(4-chlorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 2 | `N[C@@H](Cc1ccc(Cl)cc1)C(=O)O` | (-inf, H2L, 2.08, HL, 8.96, L, +inf) |
| ligand_5786 | DL-Amino-4-sulfophenylacet… (4-Sulfophenylglycine) | H2L | Amino Acids | 12 | `NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1` | (-inf, H2L, -1.8, HL, 8.66, L, +inf) |
| ligand_5787 | DL-2-Amino-4-sulfobutanoic acid (Homocysteic acid) | H2L | Amino Acids | 4 | `N[C@@H](CCS(=O)(=O)O)C(=O)O` | (-inf, H2L, 2.11, HL, 8.93, L, +inf) |
| ligand_5788 | 3-Aminopropanoic acid (beta-Alanine) | HL | Amino Acids | 111 | `NCCC(=O)O` | (-inf, H2L, 3.51, HL, 10.08, L, +inf) |
| ligand_5789 | DL-3-Aminobutanoic acid | HL | Amino Acids | 33 | `CC(N)CC(=O)O` | (-inf, H2L, 3.43, HL, 10.05, L, +inf) |
| ligand_5790 | cis-2-Aminocyclopentane-1-carboxylic acid | HL | Amino Acids | 6 | `N[C@H]1CCC[C@H]1C(=O)O` | (-inf, H2L, 3.54, HL, 10.1, L, +inf) |
| ligand_5791 | trans-2-Aminocyclopentane-1-carboxylic acid | HL | Amino Acids | 3 | `N[C@@H]1CCC[C@H]1C(=O)O` | (-inf, H2L, 3.75, HL, 9.91, L, +inf) |
| ligand_5792 | cis-2-Aminocyclohexane-1-carboxylic acid | HL | Amino Acids | 6 | `N[C@H]1CCCC[C@H]1C(=O)O` | (-inf, H2L, 3.49, HL, 10.54, L, +inf) |
| ligand_5793 | trans-2-Aminocyclohexane-1-carboxylic acid | HL | Amino Acids | 6 | `N[C@@H]1CCCC[C@H]1C(=O)O` | (-inf, H2L, 3.47, HL, 10.01, L, +inf) |
| ligand_5794 | cis-2-Amino-4-cyclohexene-1-carboxylic acid | HL | Amino Acids | 6 | `N[C@H]1CC=CC[C@H]1C(=O)O` | (-inf, H2L, 3.29, HL, 10.2, L, +inf) |
| ligand_5795 | trans-2-Amino-4-cyclohexene-1-carboxylic acid | HL | Amino Acids | 5 | `N[C@@H]1CC=CC[C@H]1C(=O)O` | (-inf, H2L, 3.33, HL, 10.29, L, +inf) |
| ligand_5796 | DL-3-Amino-3-phenylpropanoi… (Phenyl-beta-Alanine) | HL | Amino Acids | 2 | `NC(CC(=O)O)c1ccccc1` | (-inf, H2L, 3.4, HL, 9, L, +inf) |
| ligand_5797 | 4-Aminobutanoic acid | HL | Amino Acids | 51 | `NCCCC(=O)O` | (-inf, H2L, 4.02, HL, 10.35, L, +inf) |
| ligand_5798 | 5-Aminopentanoic acid | HL | Amino Acids | 20 | `NCCCCC(=O)O` | (-inf, H2L, 4.27, HL, 10.766, L, +inf) |
| ligand_5799 | 6-Aminohexanoic acid | HL | Amino Acids | 29 | `NCCCCCC(=O)O` | (-inf, H2L, 4.373, HL, 10.804, L, +inf) |
| ligand_5800 | 7-Aminoheptanoic acid | HL | Amino Acids | 3 | `NCCCCCCC(=O)O` | (-inf, H2L, 4.502, HL, +inf) |
| ligand_5801 | Aminopropanedioic acid (Aminomalonic acid) | H2L | Amino Acids | 14 | `NC(C(=O)O)C(=O)O` | (-inf, H3L, -1.8, H2L, 2.94, HL, 9.22, L, +inf) |
| ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) | H2L | Amino Acids | 174 | `N[C@@H](CC(=O)O)C(=O)O` | (-inf, H3L, 1.95, H2L, 3.71, HL, 9.66, L, +inf) |
| ligand_5803 | DL-2-Amino-3-methylbutane… (3-Methylaspartic acid) | H2L | Amino Acids | 6 | `CC(C(=O)O)[C@H](N)C(=O)O` | (-inf, H3L, 1.99, H2L, 3.59, HL, 9.48, L, +inf) |
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | H2L | Amino Acids | 94 | `N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H3L, 2.16, H2L, 4.15, HL, 9.58, L, +inf) |
| ligand_5805 | DL-2-Amino-2-methylpentan… (2-Methylglutamic acid) | H2L | Amino Acids | 4 | `C[C@](N)(CCC(=O)O)C(=O)O` | (-inf, H2L, 4.05, HL, 9.72, L, +inf) |
| ligand_5806 | DL-2-Aminohexanedioic acid | H2L | Amino Acids | 1 | `NC(CCCC(=O)O)C(=O)O` | (-inf, HL, 9.73, L, +inf) |
| ligand_5807 | DL-2-Amino-3-hydroxypent… (3-Hydroxyglutamic acid) | H2L | Amino Acids | 8 | `N[C@H](C(=O)O)C(O)CC(=O)O` | (-inf, H3L, 2.09, H2L, 4.08, HL, 9.06, L, +inf) |
| ligand_5808 | (3-Aminopropyl)malonic acid | H2L | Amino Acids | 18 | `NCCCC(C(=O)O)C(=O)O` | (-inf, H3L, 2.52, H2L, 4.86, HL, 10.45, L, +inf) |
| ligand_5809 | L-2-Amino-3-phosphopropanoic acid (Phosphoserine) | H3L | Amino Acids | 52 | `N[C@@H](COP(=O)(O)O)C(=O)O` | (-inf, H4L, -0.7, H3L, 2.14, H2L, 5.7, HL, 9.8, L, +inf) |

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
  "name": "Copper",
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

### Step 12: `search_ligands`
**Args:**
```json
{
  "smiles": "OC(=O)CC(=O)O",
  "limit": 20
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 13: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_41"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 102 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_107 | [M(H-1L)] + [H] <=> [ML] |  |
| beta_def_117 | [M(OH)(H-1L)] + [H] <=> [M(H-1L)] + [H2O] |  |
| beta_def_136 | [M(H-1L)] + [L] <=> [M(H-1L)L] |  |
| beta_def_137 | [M(H-1L)2] + [H] <=> [M(H-1L)L] |  |
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_249 | [M(OH)2L2] + [H] <=> [M(OH)L2] + [H2O] |  |
| beta_def_334 | [ML2(s)] <=> [M] + [L]^2 | solid |
| beta_def_347 | [MO(s)] + [H2O] <=> [M] + [OH]^2 | solid |
| beta_def_423 | [ML]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_424 | [M]^2 + [L]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_427 | [M(OH)L]^2 <=> [M2(OH)2L2] |  |
| beta_def_434 | [M]^2 + [L]^4 + [H2O]^2 <=> [M2(OH)2L4] + [H]^2 |  |
| beta_def_463 | [M2H-2L2] + [H] <=> [M2H-1L2] |  |
| beta_def_477 | [M]^2 + [L]^2 <=> [M2H-2L2] + [H]^2 |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_519 | [M]^2 + [L]^2 <=> [M2L2] |  |
| beta_def_567 | [M(H-1L)] + [M(OH)(H-1L)] <=> [M2(OH)(H-1L)2] |  |
| beta_def_630 | [M2H-2L2] + [M] <=> [M3H-2L2] |  |
| beta_def_649 | [M]^3 + [L]^4 <=> [M3L4] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_798 | [M] + [HL] + [L] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_834 | [M(OH)2L] + [H]^2 <=> [ML] + [H2O]^2 |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_871 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_981 | [ML] + [OH] <=> [M(OH)L] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Cu^[2+] + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine)** (metal_41 + ligand_5898) — ligand_def_HxL: HL | 50 ent, 8 sp, 50 vlms (vlm_98835…vlm_98884)
   - species: beta_def_204(8) beta_def_424(4) beta_def_788(7) beta_def_792(8) beta_def_812(8) beta_def_840(7) beta_def_966(3) beta_def_984(5)
   - eq:6 nets T:19~41°C I:-0.05~3.15M max 8n/22e
**2. Cu^[2+] + Ammonia** (metal_41 + ligand_10103) — ligand_def_HxL: L | 49 ent, 4 sp, 49 vlms (vlm_173242…vlm_173290)
   - species: beta_def_812(13) beta_def_840(12) beta_def_872(12) beta_def_894(12)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 4n/6e
**3. Cu^[2+] + 1,3-Diazole (Imidazole)** (metal_41 + ligand_7795) — ligand_def_HxL: L | 42 ent, 7 sp, 42 vlms (vlm_133893…vlm_133934)
   - species: beta_def_424(1) beta_def_434(2) beta_def_812(10) beta_def_840(10) beta_def_872(10) beta_def_894(7) beta_def_966(2)
   - eq:8 nets T:19~41°C I:-0.15~3.15M max 7n/18e
**4. Cu^[2+] + N,N'-Dimethylethylenediamine** (metal_41 + ligand_7172) — ligand_def_HxL: L | 39 ent, 5 sp, 39 vlms (vlm_125004…vlm_125042)
   - species: beta_def_424(7) beta_def_812(9) beta_def_834(7) beta_def_840(9) beta_def_966(7)
   - eq:5 nets T:19~30°C I:-0.15~2.15M max 5n/8e
**5. Cu^[2+] + Ethanoic acid (Acetic acid)** (metal_41 + ligand_8465) — ligand_def_HxL: HL | 37 ent, 3 sp, 37 vlms (vlm_144741…vlm_144777)
   - species: beta_def_812(16) beta_def_840(16) beta_def_872(5)
   - eq:6 nets T:19~41°C I:-0.15~3.15M max 3n/3e
**6. Cu^[2+] + Glycylglycine (Diglycine)** (metal_41 + ligand_6372) — ligand_def_HxL: HL | 36 ent, 6 sp, 36 vlms (vlm_113537…vlm_113572)
   - species: beta_def_107(7) beta_def_117(6) beta_def_136(7) beta_def_137(1) beta_def_567(5) beta_def_812(10)
   - eq:6 nets T:19~41°C I:-0.15~5.15M max 6n/11e
**7. Cu^[2+] + Hydroxide ion** (metal_41 + ligand_10076) — ligand_def_HxL: *** | 34 ent, 9 sp, 34 vlms (vlm_170713…vlm_170746)
   - species: beta_def_334(5) beta_def_347(2) beta_def_502(3) beta_def_519(9) beta_def_649(4) beta_def_812(7) beta_def_840(2) beta_def_872(1) beta_def_894(1)
   - eq:6 nets T:19~41°C I:-0.15~3.15M max 6n/15e
**8. Cu^[2+] + Ethylenediamine** (metal_41 + ligand_7029) — ligand_def_HxL: L | 34 ent, 2 sp, 34 vlms (vlm_122410…vlm_122443)
   - species: beta_def_812(17) beta_def_840(17)
   - eq:9 nets T:19~41°C I:-0.15~3.15M max 2n/1e
**9. Cu^[2+] + 2,2'-Bipyridyl** (metal_41 + ligand_8156) — ligand_def_HxL: L | 33 ent, 6 sp, 33 vlms (vlm_138609…vlm_138641)
   - species: beta_def_238(3) beta_def_423(3) beta_def_812(8) beta_def_840(8) beta_def_872(8) beta_def_966(3)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 6n/8e
**10. Cu^[2+] + L-2-Amino-3-phenylpropanoic acid (Phenylalanine)** (metal_41 + ligand_5777) — ligand_def_HxL: HL | 33 ent, 3 sp, 33 vlms (vlm_95053…vlm_95085)
   - species: beta_def_788(1) beta_def_812(15) beta_def_840(17)
   - eq:7 nets T:5~45°C I:-0.15~3.15M max 3n/2e
**11. Cu^[2+] + Iminodiacetic acid (IDA)** (metal_41 + ligand_6127) — ligand_def_HxL: H2L | 32 ent, 4 sp, 32 vlms (vlm_104366…vlm_104397)
   - species: beta_def_788(3) beta_def_812(13) beta_def_840(14) beta_def_966(2)
   - eq:6 nets T:19~41°C I:-0.15~1.15M max 4n/4e
**12. Cu^[2+] + L-2-Amino-3-hydroxybutanoic acid (Threonine)** (metal_41 + ligand_5829) — ligand_def_HxL: HL | 32 ent, 5 sp, 32 vlms (vlm_96743…vlm_96774)
   - species: beta_def_249(3) beta_def_812(12) beta_def_840(12) beta_def_966(1) beta_def_984(4)
   - eq:6 nets T:19~41°C I:-0.15~3.15M max 4n/4e
**13. Cu^[2+] + Aminoacetic acid (Glycine)** (metal_41 + ligand_5760) — ligand_def_HxL: HL | 30 ent, 2 sp, 30 vlms (vlm_93847…vlm_93876)
   - species: beta_def_812(15) beta_def_840(15)
   - eq:9 nets T:5~45°C I:-0.15~2.65M max 2n/1e
**14. Cu^[2+] + N-(2-Hydroxyethyl)iminodiacetic acid (HIDA)** (metal_41 + ligand_6204) — ligand_def_HxL: H2L | 29 ent, 4 sp, 29 vlms (vlm_106728…vlm_106756)
   - species: beta_def_812(13) beta_def_840(13) beta_def_966(1) beta_def_984(2)
   - eq:4 nets T:19~30°C I:-0.15~1.15M max 4n/4e
**15. Cu^[2+] + Pyridine (Azine)** (metal_41 + ligand_7890) — ligand_def_HxL: L | 28 ent, 5 sp, 28 vlms (vlm_135256…vlm_135283)
   - species: beta_def_812(7) beta_def_840(7) beta_def_872(7) beta_def_894(6) beta_def_966(1)
   - eq:5 nets T:19~30°C I:-0.15~1.15M max 5n/7e
**16. Cu^[2+] + 1,4,9-Triazanonane (2,4-tri)** (metal_41 + ligand_7214) — ligand_def_HxL: L | 28 ent, 6 sp, 28 vlms (vlm_125799…vlm_125826)
   - species: beta_def_194(4) beta_def_779(6) beta_def_798(3) beta_def_812(6) beta_def_840(3) beta_def_981(6)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 6n/11e
**17. Cu^[2+] + DL-2,6-Diamino-5-hydroxyhexanoic acid** (metal_41 + ligand_5889) — ligand_def_HxL: HL | 28 ent, 7 sp, 28 vlms (vlm_98553…vlm_98580)
   - species: beta_def_194(4) beta_def_204(4) beta_def_463(4) beta_def_477(4) beta_def_630(4) beta_def_779(4) beta_def_788(4)
   - eq:2 nets T:20~41°C I:-0.05~0.3M max 7n/15e
**18. Cu^[2+] + 4-(2-Aminoethyl)imidazole (Histamine)** (metal_41 + ligand_7849) — ligand_def_HxL: L | 27 ent, 6 sp, 27 vlms (vlm_134661…vlm_134687)
   - species: beta_def_424(4) beta_def_788(3) beta_def_792(4) beta_def_812(6) beta_def_840(6) beta_def_871(4)
   - eq:4 nets T:19~41°C I:-0.15~1.15M max 6n/12e
**19. Cu^[2+] + 2-(2-Aminoethylamino)ethanol [N-(2-Hydroxyethyl)ethylenediamine]** (metal_41 + ligand_7181) — ligand_def_HxL: L | 27 ent, 5 sp, 27 vlms (vlm_125163…vlm_125189)
   - species: beta_def_427(4) beta_def_812(7) beta_def_834(5) beta_def_840(7) beta_def_966(4)
   - eq:5 nets T:19~30°C I:-0.15~2.15M max 5n/5e
**20. Cu^[2+] + Glycyl-L-alanine** (metal_41 + ligand_6375) — ligand_def_HxL: HL | 27 ent, 5 sp, 27 vlms (vlm_113707…vlm_113733)
   - species: beta_def_107(6) beta_def_117(6) beta_def_136(6) beta_def_567(3) beta_def_812(6)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 5n/8e

---

### Step 15: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_name_SRD LIKE '%malon%' OR lc.ligand_name_SRD LIKE '%propanedioic%' OR lc.ligand_name_SRD LIKE '%propanedioate%')",
  "order_by": "lc.ligand_name_SRD ASC",
  "limit": 20
}
```

[summary]
## search_pka_ligands — 20 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_5808 | (3-Aminopropyl)malonic acid | H2L | C6H11N1O4 | NCCCC(C(=O)O)C(=O)O | −∞; H3L (M_tot_1); (2.52, vlm_95888); H2L (M_tot_1); (4.86, vlm_95885); HL (M_tot_2); (10.45, vlm_95882); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_9064 | (Carboxymethoxy)propanedioic acid | H3L | C5H6O7 | O=C(O)COC(C(=O)O)C(=O)O | −∞; H3L (M_tot_1); (-1.7, vlm_157847); H2L (M_tot_1); (3.25, vlm_157846); HL (M_tot_13); (4.41, vlm_157845); L (M_tot_13); +∞ | 25 | 0.1 | *** |
| ligand_8906 | 1,3-Diphenylpropane-2,2-dicarboxylic acid (Dibenzylmalonic … | H2L | C17H16O4 | O=C(O)C(Cc1ccccc1)(Cc1ccccc1)C(=O)O | −∞; HL (M_tot_1); (7.75, vlm_153258); L (M_tot_4); +∞ | 25 | 0 | *** |
| ligand_8904 | 1-Phenylpropane-1,1-dicarboxylic acid (Ethylphenylmalonic a… | H2L | C11H12O4 | CCC(C(=O)O)(C(=O)O)c1ccccc1 | −∞; H2L (M_tot_1); (-1.8, vlm_153255); HL (M_tot_1); (7.01, vlm_153254); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_8881 | 2,2-Dimethylpropane-1,1-dicarboxylic acid (t-Butylmalonic a… | H2L | C7H12O4 | CC(C)(C)C(C(=O)O)C(=O)O | −∞; HL (M_tot_1); (7.03, vlm_152747); L (M_tot_7); +∞ | 25 | 0 | *** |
| ligand_8895 | 2,4-Dimethylpentane-3,3-dicarboxylic acid (Di-2-propylmalon… | H2L | C9H16O4 | CC(C)C(C(=O)O)(C(=O)O)C(C)C | −∞; H2L (M_tot_1); (2.07, vlm_153073); HL (M_tot_1); (8.49, vlm_153072); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6001 | 2-Hydroxy-1,3-propylenediiminodipropanedioic acid | H4L | C9H14N2O9 | O=C(O)C(NCC(O)CNC(C(=O)O)C(=O)O)C(=O)O | −∞; H4L (M_tot_1); (2.41, vlm_101215); H3L (M_tot_1); (3.4, vlm_101214); H2L (M_tot_1); (8.9, vlm_101213); HL (M_tot_1); (10.4, vlm_101212); L (M_tot_8); +∞ | 25 | 0.1 | *** |
| ligand_8891 | 2-Methylpentane-3,3-dicarboxylic acid (Ethyl-2-propylmaloni… | H2L | C8H14O4 | CCC(C(=O)O)(C(=O)O)C(C)C | −∞; H2L (M_tot_1); (1.92, vlm_152983); HL (M_tot_1); (7.99, vlm_152982); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_8879 | 2-Methylpropane-1,1-dicarboxylic acid (Isopropylmalonic aci… | H2L | C6H10O4 | CC(C)C(C(=O)O)C(=O)O | −∞; H2L (M_tot_1); (2.78, vlm_152713); HL (M_tot_2); (5.5, vlm_152709); L (M_tot_5); +∞ | 25 | 0.1 | *** |

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND (c.ligand_name_SRD LIKE '%malon%' OR c.ligand_name_SRD LIKE '%propanedioic%' OR c.ligand_name_SRD LIKE '%propanedioate%'))",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### logK — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_7079 | N,N'-Bis(2-aminoethyl)malon… | L | NCCNC(=O)CC(=O)NCCN | 4 | 4 | 22 | 0.1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_8952 | Hydroxypropanedioic acid (H… | H2L | O=C(O)C(O)C(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5808 | (3-Aminopropyl)malonic acid | H2L | NCCCC(C(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5983 | Ethylenediiminodipropanedio… | H4L | O=C(O)C(NCCNC(C(=O)O)C(=O)O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_8885 | 2-Phenylethane-1,1-dicarbox… | H2L | O=C(O)C(Cc1ccccc1)C(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5801 | Aminopropanedioic acid (Ami… | H2L | NC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_5808 | (3-Aminopropyl)malonic acid | H2L | NCCCC(C(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8885 | 2-Phenylethane-1,1-dicarbox… | H2L | O=C(O)C(Cc1ccccc1)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |

### ΔS — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8885 | 2-Phenylethane-1,1-dicarbox… | H2L | O=C(O)C(Cc1ccccc1)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5808 | (3-Aminopropyl)malonic acid | H2L | NCCCC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 17: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id = ligand_8873)",
  "order_by": "p.temperature_c ASC, p.ionic_strength_mol_l ASC, p.pKa ASC",
  "limit": 20
}
```

[summary]
## search_pka_values — 2 row(s)

### pKa 2.5–3.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_151949 | ligand_8873 | Propanedioic acid (Malonic acid) | H2L | O=C(O)CC(=O)O | 2.65 | 25 | 0.1 | HL→H2L | M_tot_2 | M_tot_26 |

### pKa 5.0–5.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_151918 | ligand_8873 | Propanedioic acid (Malonic acid) | H2L | O=C(O)CC(=O)O | 5.27 | 25 | 0.1 | L→HL | M_tot_26 | M_tot_50 |

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.ligand_id = ligand_8873)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC, s.constant_value ASC",
  "limit": 20
}
```

[summary]
## search_stability — 17 row(s)

### `Cu^[2+]` + Propanedioic acid (Malonic acid) — 17 measurement(s)
metal_id: metal_41 | ligand_id: ligand_8873
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_152319 | ref_eq_map_20108 | beta_def_812 | logK | 5.8 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152320 | *** | beta_def_812 | ΔH | 12.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152322 | *** | beta_def_812 | ΔS | 151.9 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152331 | *** | beta_def_779 | ΔH | -0.4 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (2.65, HL, 5.27) |
| vlm_152328 | ref_eq_map_20105 | beta_def_779 | logK | 2.08 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (2.65, HL, 5.27) |
| vlm_152326 | *** | beta_def_840 | ΔH | 5 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (5.27, L, +inf) |
| vlm_152316 | ref_eq_map_20105 | beta_def_812 | logK | 5.04 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152321 | *** | beta_def_812 | ΔH | 5.9 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152324 | ref_eq_map_20105 | beta_def_840 | logK | 7.8 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (5.27, L, +inf) |
| vlm_152332 | *** | beta_def_779 | ΔS | 38.9 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (2.65, HL, 5.27) |
| vlm_152323 | *** | beta_def_812 | ΔS | 116.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152327 | *** | beta_def_840 | ΔS | 166.5 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (5.27, L, +inf) |
| vlm_152330 | ref_eq_map_20107 | beta_def_779 | logK | 1.93 | 25 | 1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (2.65, HL, 5.27) |
| vlm_152318 | ref_eq_map_20107 | beta_def_812 | logK | 4.63 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152329 | ref_eq_map_20106 | beta_def_779 | logK | 2.1 | 37 | 0.15 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (2.65, HL, 5.27) |
| vlm_152317 | ref_eq_map_20106 | beta_def_812 | logK | 5.34 | 37 | 0.15 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152325 | ref_eq_map_20106 | beta_def_840 | logK | 8.3 | 37 | 0.15 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (5.27, L, +inf) |

---
