# Q2.1.3 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "hydrogen",
  "symbol": "H",
  "limit": 5
}
```

[summary]
## search_metals — 5 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_23 | BuNH_[3]^[+] | B | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_24 | C(NH_[2])_[3]^[+] | C | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_45 | Et_[2]NH_[2]^[+] | E2NH2 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_48 | Et_[3]NH^[+] | E3NH | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "glycine",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 170 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | Amino Acids | 12 | `NC(C(=O)O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.92, L, +inf) |
| ligand_5786 | DL-Amino-4-sulfophenylacet… (4-Sulfophenylglycine) | H2L | Amino Acids | 12 | `NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1` | (-inf, H2L, -1.8, HL, 8.66, L, +inf) |
| ligand_5838 | DL-Amino-4-Methoxyphenyl… (4-Methoxyphenylglycine) | HL | Amino Acids | 12 | `COc1ccc(C(N)C(=O)O)cc1` | (-inf, H2L, 2, HL, 9.07, L, +inf) |
| ligand_5925 | N-Methylglycine (Sarcosine) | HL | Amino Acids | 39 | `CNCC(=O)O` | (-inf, H2L, 2.18, HL, 9.98, L, +inf) |
| ligand_5926 | N-Ethylglycine | HL | Amino Acids | 6 | `CCNCC(=O)O` | (-inf, H2L, 2.3, HL, 10.1, L, +inf) |
| ligand_5927 | N-Propylglycine | HL | Amino Acids | 6 | `CCCNCC(=O)O` | (-inf, H2L, 2.28, HL, 10.03, L, +inf) |
| ligand_5928 | N-Butylglycine | HL | Amino Acids | 6 | `CCCCNCC(=O)O` | (-inf, H2L, 2.29, HL, 10.07, L, +inf) |
| ligand_5929 | N-(2-Propyl)glycine | HL | Amino Acids | 5 | `CC(C)NCC(=O)O` | (-inf, H2L, 2.36, HL, 10.06, L, +inf) |
| ligand_5937 | N-(Phosphonomethyl)glycine (Glyphosate) | H3L | Amino Acids | 146 | `O=C(O)CNCP(=O)(O)O` | (-inf, H4L, -0.5, H3L, 2.2, H2L, 5.45, HL, 10.1, L, +inf) |

### Functional groups across all SQL matches (129 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 114 | 88% |
| amide | 96 | 74% |
| primary_amine | 78 | 60% |
| aromatic_ring | 26 | 20% |
| hydroxyl | 25 | 19% |
| secondary_amine | 22 | 17% |
| tertiary_amine | 14 | 11% |
| ester | 9 | 7% |
| thiol | 9 | 7% |
| phenol | 7 | 5% |
| imine | 5 | 4% |
| phosphonate | 3 | 2% |
| thioether | 3 | 2% |
| phosphate | 2 | 2% |
| pyridine | 2 | 2% |
| sulfonate | 2 | 2% |
| ether | 1 | 1% |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "alanine",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 130 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5761 | L-2-Aminopropanoic acid (Alanine) | HL | Amino Acids | 159 | `C[C@H](N)C(=O)O` | (-inf, H2L, 2.33, HL, 9.71, L, +inf) |
| ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | HL | Amino Acids | 138 | `N[C@@H](Cc1ccccc1)C(=O)O` | (-inf, H2L, 2.18, HL, 9.09, L, +inf) |
| ligand_5778 | DL-2-Amino-3-chloropropanoic ac… (3-Chloroalanine) | HL | Amino Acids | 10 | `N[C@@H](CCl)C(=O)O` | (-inf, H2L, 2, HL, 8.18, L, +inf) |
| ligand_5780 | DL-2-Amino-3-(2-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1ccccc1F)C(=O)O` | (-inf, H2L, 2.12, HL, 9.01, L, +inf) |
| ligand_5781 | DL-2-Amino-3-(3-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1cccc(F)c1)C(=O)O` | (-inf, H2L, 2.1, HL, 8.98, L, +inf) |
| ligand_5782 | DL-2-Amino-3-(4-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1ccc(F)cc1)C(=O)O` | (-inf, H2L, 2.13, HL, 9.05, L, +inf) |
| ligand_5783 | DL-2-Amino-3-(2-chlorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 2 | `N[C@@H](Cc1ccccc1Cl)C(=O)O` | (-inf, H2L, 2.23, HL, 8.94, L, +inf) |
| ligand_5784 | DL-2-Amino-3-(3-chlorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 2 | `N[C@@H](Cc1cccc(Cl)c1)C(=O)O` | (-inf, H2L, 2.17, HL, 8.91, L, +inf) |
| ligand_5785 | DL-2-Amino-3-(4-chlorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 2 | `N[C@@H](Cc1ccc(Cl)cc1)C(=O)O` | (-inf, H2L, 2.08, HL, 8.96, L, +inf) |
| ligand_5788 | 3-Aminopropanoic acid (beta-Alanine) | HL | Amino Acids | 111 | `NCCC(=O)O` | (-inf, H2L, 3.51, HL, 10.08, L, +inf) |

### Functional groups across all SQL matches (106 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 96 | 91% |
| primary_amine | 93 | 88% |
| amide | 81 | 76% |
| aromatic_ring | 43 | 41% |
| hydroxyl | 9 | 8% |
| secondary_amine | 8 | 8% |
| ester | 7 | 7% |
| halide | 7 | 7% |
| phenol | 5 | 5% |
| thioether | 3 | 3% |
| pyridine | 2 | 2% |
| thiol | 2 | 2% |
| ether | 1 | 1% |
| tertiary_amine | 1 | 1% |

---

### Step 6: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_5760"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 67 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_32 | [HL] + [H] <=> [H2L] |  |
| beta_def_79 | [L] + [H] <=> [HL] |  |
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_208 | [M] + [HL]^3 <=> [M(HL)3] |  |
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_427 | [M(OH)L]^2 <=> [M2(OH)2L2] |  |
| beta_def_713 | [MCl2] + [L] <=> [MClL] + [Cl] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_845 | [MCl2] + [L]^2 <=> [ML2] + [Cl]^2 |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |

*(all species aqueous)*

**1. Ni^[2+] + Aminoacetic acid (Glycine)** (metal_112 + ligand_5760) — ligand_def_HxL: HL | 49 ent, 3 sp, 49 vlms (vlm_93798…vlm_93846)
   - species: beta_def_812(17) beta_def_840(17) beta_def_872(15)
   - eq:9 nets T:5~45°C I:-0.15~3.15M max 3n/3e
**2. H^[+] + Aminoacetic acid (Glycine)** (metal_68 + ligand_5760) — ligand_def_HxL: HL | 48 ent, 2 sp, 48 vlms (vlm_93606…vlm_93653)
   - species: beta_def_32(27) beta_def_79(21)
   - eq:15 nets T:5~45°C I:-0.15~3.15M max 2n/1e
**3. Zn^[2+] + Aminoacetic acid (Glycine)** (metal_208 + ligand_5760) — ligand_def_HxL: HL | 37 ent, 4 sp, 37 vlms (vlm_93924…vlm_93960)
   - species: beta_def_812(12) beta_def_840(13) beta_def_872(11) beta_def_966(1)
   - eq:7 nets T:5~45°C I:-0.15~1.15M max 4n/4e
**4. Co^[2+] + Aminoacetic acid (Glycine)** (metal_33 + ligand_5760) — ligand_def_HxL: HL | 37 ent, 4 sp, 37 vlms (vlm_93761…vlm_93797)
   - species: beta_def_812(12) beta_def_840(12) beta_def_872(12) beta_def_966(1)
   - eq:7 nets T:5~45°C I:-0.15~1.15M max 4n/4e
**5. Cd^[2+] + Aminoacetic acid (Glycine)** (metal_26 + ligand_5760) — ligand_def_HxL: HL | 32 ent, 3 sp, 32 vlms (vlm_93961…vlm_93992)
   - species: beta_def_812(11) beta_def_840(11) beta_def_872(10)
   - eq:7 nets T:5~45°C I:-0.15~1.15M max 3n/3e
**6. Cu^[2+] + Aminoacetic acid (Glycine)** (metal_41 + ligand_5760) — ligand_def_HxL: HL | 30 ent, 2 sp, 30 vlms (vlm_93847…vlm_93876)
   - species: beta_def_812(15) beta_def_840(15)
   - eq:9 nets T:5~45°C I:-0.15~2.65M max 2n/1e
**7. Pb^[2+] + Aminoacetic acid (Glycine)** (metal_125 + ligand_5760) — ligand_def_HxL: HL | 25 ent, 8 sp, 25 vlms (vlm_94001…vlm_94025)
   - species: beta_def_194(2) beta_def_204(1) beta_def_208(1) beta_def_779(5) beta_def_792(1) beta_def_812(8) beta_def_840(4) beta_def_966(3)
   - eq:4 nets T:19~30°C I:-0.05~3.15M max 6n/11e
**8. Mn^[2+] + Aminoacetic acid (Glycine)** (metal_94 + ligand_5760) — ligand_def_HxL: HL | 14 ent, 2 sp, 14 vlms (vlm_93733…vlm_93746)
   - species: beta_def_812(11) beta_def_840(3)
   - eq:6 nets T:5~45°C I:-0.15~0.65M max 2n/1e
**9. Fe^[2+] + Aminoacetic acid (Glycine)** (metal_62 + ligand_5760) — ligand_def_HxL: HL | 14 ent, 3 sp, 14 vlms (vlm_93747…vlm_93760)
   - species: beta_def_812(11) beta_def_840(2) beta_def_872(1)
   - eq:7 nets T:5~45°C I:-0.15~3.15M max 3n/3e
**10. Ag^[+] + Aminoacetic acid (Glycine)** (metal_2 + ligand_5760) — ligand_def_HxL: HL | 14 ent, 4 sp, 14 vlms (vlm_93900…vlm_93913)
   - species: beta_def_779(1) beta_def_812(6) beta_def_840(6) beta_def_966(1)
   - eq:4 nets T:19~30°C I:-0.15~3.15M max 4n/4e
**11. VO^[2+] + Aminoacetic acid (Glycine)** (metal_201 + ligand_5760) — ligand_def_HxL: HL | 13 ent, 9 sp, 13 vlms (vlm_93886…vlm_93898)
   - species: beta_def_194(3) beta_def_238(1) beta_def_427(1) beta_def_779(3) beta_def_792(1) beta_def_812(1) beta_def_840(1) beta_def_966(1) beta_def_984(1)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 9n/17e
**12. Ca^[2+] + Aminoacetic acid (Glycine)** (metal_25 + ligand_5760) — ligand_def_HxL: HL | 12 ent, 2 sp, 12 vlms (vlm_93666…vlm_93677)
   - species: beta_def_779(4) beta_def_812(8)
   - eq:6 nets T:15~41°C I:-0.15~3.15M max 2n/1e
**13. Th^[4+] + Aminoacetic acid (Glycine)** (metal_185 + ligand_5760) — ligand_def_HxL: HL | 9 ent, 3 sp, 9 vlms (vlm_93712…vlm_93720)
   - species: beta_def_194(3) beta_def_208(3) beta_def_779(3)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 3n/3e
**14. Mg^[2+] + Aminoacetic acid (Glycine)** (metal_92 + ligand_5760) — ligand_def_HxL: HL | 9 ent, 3 sp, 9 vlms (vlm_93657…vlm_93665)
   - species: beta_def_779(1) beta_def_812(7) beta_def_840(1)
   - eq:5 nets T:15~30°C I:-0.15~3.15M max 2n/1e
**15. Hg^[2+] + Aminoacetic acid (Glycine)** (metal_71 + ligand_5760) — ligand_def_HxL: HL | 8 ent, 4 sp, 8 vlms (vlm_93993…vlm_94000)
   - species: beta_def_713(3) beta_def_812(1) beta_def_840(1) beta_def_845(3)
   - eq:2 nets T:15~30°C I:-0.05~0.65M max 2n/1e
**16. UO_[2]^[2+] + Aminoacetic acid (Glycine)** (metal_195 + ligand_5760) — ligand_def_HxL: HL | 7 ent, 2 sp, 7 vlms (vlm_93724…vlm_93730)
   - species: beta_def_194(3) beta_def_779(4)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 2n/1e
**17. Fe^[3+] + Aminoacetic acid (Glycine)** (metal_61 + ligand_5760) — ligand_def_HxL: HL | 6 ent, 3 sp, 6 vlms (vlm_93880…vlm_93885)
   - species: beta_def_194(1) beta_def_779(3) beta_def_812(2)
   - eq:3 nets T:16.5~31.5°C I:0.275~3.225M max 3n/3e
**18. Eu^[3+] + Aminoacetic acid (Glycine)** (metal_58 + ligand_5760) — ligand_def_HxL: HL | 4 ent, 2 sp, 4 vlms (vlm_93694…vlm_93697)
   - species: beta_def_779(3) beta_def_812(1)
   - eq:2 nets T:19~30°C I:-0.05~2.15M max 1n/0e
**19. Ti^[3+] + Aminoacetic acid (Glycine)** (metal_187 + ligand_5760) — ligand_def_HxL: HL | 3 ent, 3 sp, 3 vlms (vlm_93877, vlm_93878, vlm_93879)
   - species: beta_def_779(1) beta_def_812(1) beta_def_966(1)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 3n/2e
**20. Pm^[3+] + Aminoacetic acid (Glycine)** (metal_137 + ligand_5760) — ligand_def_HxL: HL | 3 ent, 1 sp, 3 vlms (vlm_93690, vlm_93691, vlm_93692)
   - species: beta_def_779(3)
   - eq:1 nets T:12.5~27.5°C I:1.775~2.225M max 1n/0e

---

### Step 7: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_5761"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 43 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_32 | [HL] + [H] <=> [H2L] |  |
| beta_def_79 | [L] + [H] <=> [HL] |  |
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |

*(all species aqueous)*

**1. H^[+] + L-2-Aminopropanoic acid (Alanine)** (metal_68 + ligand_5761) — ligand_def_HxL: HL | 40 ent, 2 sp, 40 vlms (vlm_94058…vlm_94097)
   - species: beta_def_32(20) beta_def_79(20)
   - eq:11 nets T:5~45°C I:-0.15~5.15M max 2n/1e
**2. Ni^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_112 + ligand_5761) — ligand_def_HxL: HL | 24 ent, 3 sp, 24 vlms (vlm_94125…vlm_94272)
   - species: beta_def_812(9) beta_def_840(9) beta_def_872(6)
   - eq:5 nets T:19~41°C I:-0.15~1.15M max 3n/3e
**3. Cu^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_41 + ligand_5761) — ligand_def_HxL: HL | 21 ent, 3 sp, 21 vlms (vlm_94273…vlm_94293)
   - species: beta_def_788(1) beta_def_812(9) beta_def_840(11)
   - eq:7 nets T:19~41°C I:-0.15~5.15M max 3n/2e
**4. Zn^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_208 + ligand_5761) — ligand_def_HxL: HL | 19 ent, 4 sp, 19 vlms (vlm_94305…vlm_94323)
   - species: beta_def_812(7) beta_def_840(7) beta_def_872(3) beta_def_966(2)
   - eq:5 nets T:19~41°C I:-0.15~1.15M max 4n/4e
**5. Co^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_33 + ligand_5761) — ligand_def_HxL: HL | 11 ent, 3 sp, 11 vlms (vlm_94114…vlm_94124)
   - species: beta_def_812(5) beta_def_840(5) beta_def_872(1)
   - eq:3 nets T:19~41°C I:-0.15~0.3M max 3n/3e
**6. Cd^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_26 + ligand_5761) — ligand_def_HxL: HL | 9 ent, 3 sp, 9 vlms (vlm_94324…vlm_94332)
   - species: beta_def_812(4) beta_def_840(3) beta_def_872(2)
   - eq:5 nets T:15~41°C I:-0.05~0.85M max 3n/3e
**7. Ca^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_25 + ligand_5761) — ligand_def_HxL: HL | 6 ent, 2 sp, 6 vlms (vlm_94099…vlm_94104)
   - species: beta_def_779(3) beta_def_812(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 2n/1e
**8. Pb^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_125 + ligand_5761) — ligand_def_HxL: HL | 4 ent, 3 sp, 4 vlms (vlm_94337…vlm_94340)
   - species: beta_def_779(1) beta_def_812(2) beta_def_840(1)
   - eq:2 nets T:12.5~31.5°C I:0.275~3.225M max 3n/3e
**9. Mn^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_94 + ligand_5761) — ligand_def_HxL: HL | 4 ent, 2 sp, 4 vlms (vlm_94109…vlm_94112)
   - species: beta_def_812(2) beta_def_840(2)
   - eq:2 nets T:20~41°C I:-0.05~0.3M max 2n/1e
**10. Me_[2]Sn^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_85 + ligand_5761) — ligand_def_HxL: HL | 4 ent, 4 sp, 4 vlms (vlm_94333…vlm_94336)
   - species: beta_def_238(1) beta_def_788(1) beta_def_812(1) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 4n/5e
**11. Ag^[+] + L-2-Aminopropanoic acid (Alanine)** (metal_2 + ligand_5761) — ligand_def_HxL: HL | 3 ent, 2 sp, 3 vlms (vlm_94297, vlm_94298, vlm_94299)
   - species: beta_def_812(1) beta_def_840(2)
   - eq:2 nets T:19~30°C I:-0.15~0.25M max 2n/1e
**12. Pd^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_127 + ligand_5761) — ligand_def_HxL: HL | 2 ent, 2 sp, 2 vlms (vlm_94303, vlm_94304)
   - species: beta_def_194(1) beta_def_779(1)
   - eq:1 nets T:12.5~27.5°C I:0.775~1.225M max 2n/1e
**13. MeHg^[+] + L-2-Aminopropanoic acid (Alanine)** (metal_93 + ligand_5761) — ligand_def_HxL: HL | 2 ent, 2 sp, 2 vlms (vlm_94300, vlm_94301)
   - species: beta_def_812(1) beta_def_840(1)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 2n/1e
**14. Fe^[3+] + L-2-Aminopropanoic acid (Alanine)** (metal_61 + ligand_5761) — ligand_def_HxL: HL | 2 ent, 2 sp, 2 vlms (vlm_94294, vlm_94295)
   - species: beta_def_812(1) beta_def_966(1)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 2n/1e
**15. Tl^[+] + L-2-Aminopropanoic acid (Alanine)** (metal_191 + ligand_5761) — ligand_def_HxL: HL | 1 ent, 1 sp, 1 vlms (vlm_94302)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**16. Sr^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_177 + ligand_5761) — ligand_def_HxL: HL | 1 ent, 1 sp, 1 vlms (vlm_94105)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**17. Nd^[3+] + L-2-Aminopropanoic acid (Alanine)** (metal_110 + ligand_5761) — ligand_def_HxL: HL | 1 ent, 1 sp, 1 vlms (vlm_94107)
   - species: beta_def_779(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**18. Mg^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_92 + ligand_5761) — ligand_def_HxL: HL | 1 ent, 1 sp, 1 vlms (vlm_94098)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**19. Fe^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_62 + ligand_5761) — ligand_def_HxL: HL | 1 ent, 1 sp, 1 vlms (vlm_94113)
   - species: beta_def_812(1)
   - eq:1 nets T:12.5~27.5°C I:0.775~1.225M max 1n/0e
**20. Eu^[3+] + L-2-Aminopropanoic acid (Alanine)** (metal_58 + ligand_5761) — ligand_def_HxL: HL | 1 ent, 1 sp, 1 vlms (vlm_94108)
   - species: beta_def_779(1)
   - eq:1 nets T:16.5~31.5°C I:1.775~2.225M max 1n/0e

---

### Step 9: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (ligand_5760, ligand_5761) AND (p.solvent_name LIKE '%water%' OR p.solvent_name IS NULL) AND p.temperature_c BETWEEN 20 AND 30 AND (p.ionic_strength_mol_l IS NULL OR p.ionic_strength_mol_l <= 0.2))",
  "order_by": "lc.ligand_id, p.pKa_type ASC, ABS(p.temperature_c - 25) ASC",
  "limit": 20
}
```

[summary]
## search_pka_values — 4 row(s)

### pKa 2.0–2.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_93627 | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2.33 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_20 |
| vlm_94078 | ligand_5761 | L-2-Aminopropanoic acid (Alanine) | HL | C[C@H](N)C(=O)O | 2.33 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_6 |

### pKa 9.5–10.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_93606 | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 9.57 | 25 | 0.1 | L→HL | M_tot_20 | M_tot_43 |
| vlm_94058 | ligand_5761 | L-2-Aminopropanoic acid (Alanine) | HL | C[C@H](N)C(=O)O | 9.71 | 25 | 0.1 | L→HL | M_tot_6 | M_tot_19 |

---
