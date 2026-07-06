# Q2.1.3 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "H+",
  "limit": 10
}
```

[summary]
## search_metals — 10 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_23 | BuNH_[3]^[+] | B | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_24 | C(NH_[2])_[3]^[+] | C | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_45 | Et_[2]NH_[2]^[+] | E2NH2 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_48 | Et_[3]NH^[+] | E3NH | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_53 | EtHg^[+] | EHg | 1 |  | *** | *** | beta_totN_4 | ligand_totN_3 | vlm_totN_6 |
| metal_54 | EtNH_[3]^[+] | ENH3 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_3 | vlm_totN_3 |
| metal_68 | H^[+] | H | 1 | ✓ | [H+] | InChI=1S/p+1 | beta_totN_82 | ligand_totN_4081 | vlm_totN_20720 |
| metal_69 | H_[5]TeO_[6]^[-] | H | -1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_2 |
| metal_70 | Hf^[4+] | Hf | 4 | ✓ | [Hf+4] | InChI=1S/Hf/q+4 | beta_totN_10 | ligand_totN_14 | vlm_totN_49 |

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

### Step 5: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_68",
  "ligand_id": "ligand_5760"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 2 species

### H^[+] + Aminoacetic acid (Glycine)
**metal_id:** metal_68 | **ligand_id:** ligand_5760 | **ligand_def_HxL:** HL  
**entries:** 48 | **species:** 2 | **vlm_count:** 48

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_32 | [H<sub>2</sub>L]/[HL][H] | [HL] + [H] <=> [H2L] | [H2L](aqueous), [HL](aqueous), [H](aqueous) | 27 |
| beta_def_79 | [HL]/[L][H] | [L] + [H] <=> [HL] | [HL](aqueous), [L](aqueous), [H](aqueous) | 21 |

**vlm_ids:** vlm_93606, vlm_93607, vlm_93608, vlm_93609, vlm_93610, … vlm_93651, vlm_93652, vlm_93653 (48 listed)

**equilibrium_maps:** 15 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_1 | 2 | 1 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_2 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_3 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_4 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_5 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_6 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_7 | 2 | 1 | 31~41 °C | 0~0.3 M |
| ref_eq_net_8 | 2 | 1 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_9 | 2 | 1 | 19~29 °C | 0.55~0.85 M |
| ref_eq_net_10 | 2 | 1 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_11 | 2 | 1 | 5~15 °C | -0.15~0.15 M |
| ref_eq_net_12 | 2 | 1 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_13 | 2 | 1 | 35~45 °C | -0.15~0.15 M |
| ref_eq_net_14 | 1 | 0 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_15 | 1 | 0 | 19~29 °C | 2.85~3.15 M |

---

### Step 7: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (ligand_5760, ligand_5761) AND p.solvent_name LIKE '%water%' AND p.temperature_c BETWEEN 24 AND 26)",
  "order_by": "lc.ligand_id ASC, p.ionic_strength_mol_l ASC, p.pKa ASC",
  "limit": 50
}
```

[summary]
## search_pka_values

*(no results)*

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_68 AND c.ligand_id IN (ligand_5760, ligand_5761) AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 24 AND 26)",
  "order_by": "c.ligand_id ASC, s.ionic_strength_mol_l ASC, s.constant_value ASC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 9: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (ligand_5760, ligand_5761))",
  "order_by": "lc.ligand_id ASC",
  "limit": 20
}
```

[summary]
## search_pka_ligands — 4 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | C2H5N1O2 | NCC(=O)O | −∞; H2L (M_tot_1); (2.33, vlm_93627); HL (M_tot_20); (9.57, vlm_93606); L (M_tot_43); +∞ | 25 | 0.1 | *** |
| ligand_5761 | L-2-Aminopropanoic acid (Alanine) | HL | C3H7N1O2 | C[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.33, vlm_94078); HL (M_tot_6); (9.71, vlm_94058); L (M_tot_19); +∞ | 25 | 0.1 | *** |

---

### Step 10: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (ligand_5760, ligand_5761))",
  "order_by": "lc.ligand_id ASC, p.temperature_c ASC, p.ionic_strength_mol_l ASC, p.pKa ASC",
  "limit": 100
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
