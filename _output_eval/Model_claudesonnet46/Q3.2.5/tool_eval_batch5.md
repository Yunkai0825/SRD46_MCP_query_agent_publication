# Q3.2.5 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "zinc",
  "limit": 5
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 3: `search_ligands`
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

### Step 4: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_208",
  "ligand_id": "ligand_6277"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 4 species

### Zn^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)
**metal_id:** metal_208 | **ligand_id:** ligand_6277 | **ligand_def_HxL:** H4L  
**entries:** 18 | **species:** 4 | **vlm_count:** 18

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_739 | [MH<sub>2</sub>L]/[MHL][H] | [MHL] + [H] <=> [MH2L] | [MH2L](aqueous), [MHL](aqueous), [H](aqueous) | 1 |
| beta_def_788 | [MHL]/[ML][H] | [ML] + [H] <=> [MHL] | [MHL](aqueous), [ML](aqueous), [H](aqueous) | 5 |
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 6 |
| beta_def_966 | [ML]/[M(OH)L][H] | [M(OH)L] + [H] <=> [ML] + [H2O] | [ML](aqueous), [H2O](aqueous), [M(OH)L](aqueous), [H](aqueous) | 6 |

**vlm_ids:** vlm_108707, vlm_108708, vlm_108709, vlm_108710, vlm_108711, … vlm_108722, vlm_108723, vlm_108724 (18 listed)

**equilibrium_maps:** 5 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_5056 | 3 | 3 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_5057 | 4 | 5 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_5058 | 1 | 0 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_5059 | 1 | 0 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_5060 | 1 | 0 | 19~29 °C | 2.85~3.15 M |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812)",
  "order_by": "s.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_stability — 6 row(s)

### `Zn^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 6 measurement(s)
metal_id: metal_208 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108710 | ref_eq_map_5053 | beta_def_812 | logK | 18 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108707 | ref_eq_map_5050 | beta_def_812 | logK | 16.5 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108711 | *** | beta_def_812 | ΔH | -19.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108712 | *** | beta_def_812 | ΔS | 250.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108708 | ref_eq_map_5052 | beta_def_812 | logK | 15.7 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108709 | ref_eq_map_5051 | beta_def_812 | logK | 15.7 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_6277)",
  "order_by": "s.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_stability — 18 row(s)

### `Zn^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 18 measurement(s)
metal_id: metal_208 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108710 | ref_eq_map_5053 | beta_def_812 | logK | 18 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108707 | ref_eq_map_5050 | beta_def_812 | logK | 16.5 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108711 | *** | beta_def_812 | ΔH | -19.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108712 | *** | beta_def_812 | ΔS | 250.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108713 | ref_eq_map_5050 | beta_def_788 | logK | 3 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108716 | *** | beta_def_788 | ΔH | -9.2 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108717 | *** | beta_def_788 | ΔS | 26.4 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108719 | ref_eq_map_5050 | beta_def_966 | logK | -11.6 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_108721 | *** | beta_def_966 | ΔH | 0 | 20 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_108723 | *** | beta_def_966 | ΔS | -25.5 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_108708 | ref_eq_map_5052 | beta_def_812 | logK | 15.7 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108709 | ref_eq_map_5051 | beta_def_812 | logK | 15.7 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108714 | ref_eq_map_5051 | beta_def_788 | logK | 2.8 | 25 | 1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108718 | ref_eq_map_5051 | beta_def_739 | logK | -1.2 | 25 | 1 | `[MHL] + [H] <=> [MH2L]` | *** |  |  |
| vlm_108720 | ref_eq_map_5051 | beta_def_966 | logK | -12 | 25 | 1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_108722 | *** | beta_def_966 | ΔH | -35.6 | 25 | 1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_108724 | *** | beta_def_966 | ΔS | -110.5 | 25 | 1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_108715 | ref_eq_map_5054 | beta_def_788 | logK | 3.1 | 25 | 3 | `[ML] + [H] <=> [MHL]` | *** |  |  |

---

### Step 8: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_108710"
}
```

[summary]
## inspect_literature — vlm_108710 — 34 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_791 | 49AS | H. Ackerman and G. Schwarzenbach, Helv. Chim. Acta, 1949, 32, 1543 |
| lit_1814 | 53BK | K. Bril and P. Krumholz, J. Phys. Chem., 1953, 57, 874 |
| lit_1864 | 53HM | V. L. Hughes and A. E. Martell, J. Phys. Chem., 1953, 57, 694 |
| lit_1973 | 54C | R. G. Charles, J. Amer. Chem. Soc., 1954, 76, 5854 |
| lit_2071 | 54SG | G. Schwarzenbach, R. Gut, and G. Anderegg, Helv. Chim. Acta, 1954, 37, 937 |
| lit_1205 | 56CS | R. A. Care and L. A. K. Staveley, J. Chem. Soc., 1956, 4571 |
| lit_2306 | 56SR | R. W. Schmid and C. N. Reilley, J. Amer. Chem. Soc., 1956, 78, 5513 |
| lit_2432 | 57JA | J. Jordan and T. G. Alleman, Anal. Chem., 1957, 29, 9 |
| lit_2532 | 57SAa | G. Schwarzenbach and G. Anderegg, Helv. Chim. Acta, 1957, 40, 1773 |
| lit_3910 | 63Aa | G. Anderegg, Helv. Chim. Acta, 1963, 46, 1833 |
| lit_4660 | 64YL | C. H. Yen and S. C. Liu, Hua Hsueh Hsueh Pao (Acta Chim. Sinica), 1964, 30, 546 |
| lit_4830 | 65JM | V. Jokl and J. Majer, Chem. Zvesti, 1965, 19, 249 |
| lit_4838 | 65Kb | J. Kula, Anal. Chem., 1965, 37, 989 |
| lit_4916 | 65O | H. Ogino, Bull. Chem. Soc. Japan, 1965, 38, 771 |
| lit_4941 | 65PSS | P. T. Priestley, W. S. Sebborn, and R. F. W. Selman, Analyst (London), 1965, 90… |
| lit_5038 | 65WHR | D. L. Wright, J. H. Holloway, and C. N. Reilley, Anal. Chem., 1965, 37, 884 |
| lit_5792 | 67S | J. Stary, in "Solv. Extr. Chem. ", D. Dyrssen, J. O. Liljenzin, and J. Rydberg,… |
| lit_6185 | 68LPP | S. Laxmi, S. Prakash, and S. Prakash, Z. Phys. Chem. N. F. (Frankfurt), 1968, 6… |
| lit_1293 | 69BNS | A. P. Brunetti, G. H. Nancollas, and P. N. Smith, J. Amer. Chem. Soc., 1969, 91… |
| lit_7027 | 70FD | A. Ya. Fridman, N. M. Dyatlova, and R. P. Lastovskii, Russ. J. Inorg. Chem., 19… |
| lit_8604 | 73HRa | E. H. Hansen and J. Ruzicka, Talanta, 1973, 20, 1105 |
| lit_9944 | 76CWW | A. M. Corrie, M. D. Walker, and D. R. Williams, J. Chem. Soc. Dalton, 1976, 1012 |
| lit_10315 | 77Aee | G. Anderegg, "Critical Survey of Stability Constants of EDTA Complexes", Pergam… |
| lit_10659 | 78BKb | V. N. Belinskii, V. S. Kublanovskii, and T. S. Glushchak, Soviet Progr. Chem. (… |
| lit_10805 | 78KVc | V. I. Kornev, V. A. Valyaeva, and S. I. Zobnin, Russ. J. Phys. Chem., 1978, 52,… |
| lit_11185 | 79JPC | T. J. Janjic, L. B. Pfendt, and M. B. Celap, J. Inorg. Nucl. Chem., 1979, 41, 1… |
| lit_11186 | 79JPP | T. J. Janjic, L. B. Pfendt, and V. Popov, J. Inorg. Nucl. Chem., 1979, 41, 63 |
| lit_12202 | 82AKB | A. Avdeef, D. L. Kearney, J. A. Brown, and A. R. Chemotti, Jr., Anal. Chem., 19… |
| lit_12770 | 83IE | L. Ilcheva, N. Elenkova, and M. Tabbara, God. Vissh. Khim. Teknol. Inst., Sofia… |
| lit_13154 | 84DMW | J. R. Duffield, P. M. May, and D. R. Williams, J. Inorg. Biochem., 1984, 20, 199 |
| lit_13903 | 85VG | V. P. Vasilev, N. K. Grechina, and M. V. Tikhomirova, Russ. J. Inorg. Chem., 19… |
| lit_13911 | 85VKK | V. P. Vasilev, E. V. Kozlovskii, E. N. Kalachev, and G. V. Chistyakova, Russ. J… |
| lit_13927 | 85YW | A. Yuchi, H. Wada, and G. Nakagawa, Anal. Sci., 1985, 1, 19 |
| lit_15666 | 90OB | R. bin Othman, N. G. Buckman, J. O. Hill, and R. J. Magee, Thermochim. Acta, 19… |

---

### Step 9: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_108707"
}
```

[summary]
## inspect_literature — vlm_108707 — 34 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_791 | 49AS | H. Ackerman and G. Schwarzenbach, Helv. Chim. Acta, 1949, 32, 1543 |
| lit_1814 | 53BK | K. Bril and P. Krumholz, J. Phys. Chem., 1953, 57, 874 |
| lit_1864 | 53HM | V. L. Hughes and A. E. Martell, J. Phys. Chem., 1953, 57, 694 |
| lit_1973 | 54C | R. G. Charles, J. Amer. Chem. Soc., 1954, 76, 5854 |
| lit_2071 | 54SG | G. Schwarzenbach, R. Gut, and G. Anderegg, Helv. Chim. Acta, 1954, 37, 937 |
| lit_1205 | 56CS | R. A. Care and L. A. K. Staveley, J. Chem. Soc., 1956, 4571 |
| lit_2306 | 56SR | R. W. Schmid and C. N. Reilley, J. Amer. Chem. Soc., 1956, 78, 5513 |
| lit_2432 | 57JA | J. Jordan and T. G. Alleman, Anal. Chem., 1957, 29, 9 |
| lit_2532 | 57SAa | G. Schwarzenbach and G. Anderegg, Helv. Chim. Acta, 1957, 40, 1773 |
| lit_3910 | 63Aa | G. Anderegg, Helv. Chim. Acta, 1963, 46, 1833 |
| lit_4660 | 64YL | C. H. Yen and S. C. Liu, Hua Hsueh Hsueh Pao (Acta Chim. Sinica), 1964, 30, 546 |
| lit_4830 | 65JM | V. Jokl and J. Majer, Chem. Zvesti, 1965, 19, 249 |
| lit_4838 | 65Kb | J. Kula, Anal. Chem., 1965, 37, 989 |
| lit_4916 | 65O | H. Ogino, Bull. Chem. Soc. Japan, 1965, 38, 771 |
| lit_4941 | 65PSS | P. T. Priestley, W. S. Sebborn, and R. F. W. Selman, Analyst (London), 1965, 90… |
| lit_5038 | 65WHR | D. L. Wright, J. H. Holloway, and C. N. Reilley, Anal. Chem., 1965, 37, 884 |
| lit_5792 | 67S | J. Stary, in "Solv. Extr. Chem. ", D. Dyrssen, J. O. Liljenzin, and J. Rydberg,… |
| lit_6185 | 68LPP | S. Laxmi, S. Prakash, and S. Prakash, Z. Phys. Chem. N. F. (Frankfurt), 1968, 6… |
| lit_1293 | 69BNS | A. P. Brunetti, G. H. Nancollas, and P. N. Smith, J. Amer. Chem. Soc., 1969, 91… |
| lit_7027 | 70FD | A. Ya. Fridman, N. M. Dyatlova, and R. P. Lastovskii, Russ. J. Inorg. Chem., 19… |
| lit_8604 | 73HRa | E. H. Hansen and J. Ruzicka, Talanta, 1973, 20, 1105 |
| lit_9944 | 76CWW | A. M. Corrie, M. D. Walker, and D. R. Williams, J. Chem. Soc. Dalton, 1976, 1012 |
| lit_10315 | 77Aee | G. Anderegg, "Critical Survey of Stability Constants of EDTA Complexes", Pergam… |
| lit_10659 | 78BKb | V. N. Belinskii, V. S. Kublanovskii, and T. S. Glushchak, Soviet Progr. Chem. (… |
| lit_10805 | 78KVc | V. I. Kornev, V. A. Valyaeva, and S. I. Zobnin, Russ. J. Phys. Chem., 1978, 52,… |
| lit_11185 | 79JPC | T. J. Janjic, L. B. Pfendt, and M. B. Celap, J. Inorg. Nucl. Chem., 1979, 41, 1… |
| lit_11186 | 79JPP | T. J. Janjic, L. B. Pfendt, and V. Popov, J. Inorg. Nucl. Chem., 1979, 41, 63 |
| lit_12202 | 82AKB | A. Avdeef, D. L. Kearney, J. A. Brown, and A. R. Chemotti, Jr., Anal. Chem., 19… |
| lit_12770 | 83IE | L. Ilcheva, N. Elenkova, and M. Tabbara, God. Vissh. Khim. Teknol. Inst., Sofia… |
| lit_13154 | 84DMW | J. R. Duffield, P. M. May, and D. R. Williams, J. Inorg. Biochem., 1984, 20, 199 |
| lit_13903 | 85VG | V. P. Vasilev, N. K. Grechina, and M. V. Tikhomirova, Russ. J. Inorg. Chem., 19… |
| lit_13911 | 85VKK | V. P. Vasilev, E. V. Kozlovskii, E. N. Kalachev, and G. V. Chistyakova, Russ. J… |
| lit_13927 | 85YW | A. Yuchi, H. Wada, and G. Nakagawa, Anal. Sci., 1985, 1, 19 |
| lit_15666 | 90OB | R. bin Othman, N. G. Buckman, J. O. Hill, and R. J. Magee, Thermochim. Acta, 19… |

---

### Step 10: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_108708"
}
```

[summary]
## inspect_literature — vlm_108708 — 34 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_791 | 49AS | H. Ackerman and G. Schwarzenbach, Helv. Chim. Acta, 1949, 32, 1543 |
| lit_1814 | 53BK | K. Bril and P. Krumholz, J. Phys. Chem., 1953, 57, 874 |
| lit_1864 | 53HM | V. L. Hughes and A. E. Martell, J. Phys. Chem., 1953, 57, 694 |
| lit_1973 | 54C | R. G. Charles, J. Amer. Chem. Soc., 1954, 76, 5854 |
| lit_2071 | 54SG | G. Schwarzenbach, R. Gut, and G. Anderegg, Helv. Chim. Acta, 1954, 37, 937 |
| lit_1205 | 56CS | R. A. Care and L. A. K. Staveley, J. Chem. Soc., 1956, 4571 |
| lit_2306 | 56SR | R. W. Schmid and C. N. Reilley, J. Amer. Chem. Soc., 1956, 78, 5513 |
| lit_2432 | 57JA | J. Jordan and T. G. Alleman, Anal. Chem., 1957, 29, 9 |
| lit_2532 | 57SAa | G. Schwarzenbach and G. Anderegg, Helv. Chim. Acta, 1957, 40, 1773 |
| lit_3910 | 63Aa | G. Anderegg, Helv. Chim. Acta, 1963, 46, 1833 |
| lit_4660 | 64YL | C. H. Yen and S. C. Liu, Hua Hsueh Hsueh Pao (Acta Chim. Sinica), 1964, 30, 546 |
| lit_4830 | 65JM | V. Jokl and J. Majer, Chem. Zvesti, 1965, 19, 249 |
| lit_4838 | 65Kb | J. Kula, Anal. Chem., 1965, 37, 989 |
| lit_4916 | 65O | H. Ogino, Bull. Chem. Soc. Japan, 1965, 38, 771 |
| lit_4941 | 65PSS | P. T. Priestley, W. S. Sebborn, and R. F. W. Selman, Analyst (London), 1965, 90… |
| lit_5038 | 65WHR | D. L. Wright, J. H. Holloway, and C. N. Reilley, Anal. Chem., 1965, 37, 884 |
| lit_5792 | 67S | J. Stary, in "Solv. Extr. Chem. ", D. Dyrssen, J. O. Liljenzin, and J. Rydberg,… |
| lit_6185 | 68LPP | S. Laxmi, S. Prakash, and S. Prakash, Z. Phys. Chem. N. F. (Frankfurt), 1968, 6… |
| lit_1293 | 69BNS | A. P. Brunetti, G. H. Nancollas, and P. N. Smith, J. Amer. Chem. Soc., 1969, 91… |
| lit_7027 | 70FD | A. Ya. Fridman, N. M. Dyatlova, and R. P. Lastovskii, Russ. J. Inorg. Chem., 19… |
| lit_8604 | 73HRa | E. H. Hansen and J. Ruzicka, Talanta, 1973, 20, 1105 |
| lit_9944 | 76CWW | A. M. Corrie, M. D. Walker, and D. R. Williams, J. Chem. Soc. Dalton, 1976, 1012 |
| lit_10315 | 77Aee | G. Anderegg, "Critical Survey of Stability Constants of EDTA Complexes", Pergam… |
| lit_10659 | 78BKb | V. N. Belinskii, V. S. Kublanovskii, and T. S. Glushchak, Soviet Progr. Chem. (… |
| lit_10805 | 78KVc | V. I. Kornev, V. A. Valyaeva, and S. I. Zobnin, Russ. J. Phys. Chem., 1978, 52,… |
| lit_11185 | 79JPC | T. J. Janjic, L. B. Pfendt, and M. B. Celap, J. Inorg. Nucl. Chem., 1979, 41, 1… |
| lit_11186 | 79JPP | T. J. Janjic, L. B. Pfendt, and V. Popov, J. Inorg. Nucl. Chem., 1979, 41, 63 |
| lit_12202 | 82AKB | A. Avdeef, D. L. Kearney, J. A. Brown, and A. R. Chemotti, Jr., Anal. Chem., 19… |
| lit_12770 | 83IE | L. Ilcheva, N. Elenkova, and M. Tabbara, God. Vissh. Khim. Teknol. Inst., Sofia… |
| lit_13154 | 84DMW | J. R. Duffield, P. M. May, and D. R. Williams, J. Inorg. Biochem., 1984, 20, 199 |
| lit_13903 | 85VG | V. P. Vasilev, N. K. Grechina, and M. V. Tikhomirova, Russ. J. Inorg. Chem., 19… |
| lit_13911 | 85VKK | V. P. Vasilev, E. V. Kozlovskii, E. N. Kalachev, and G. V. Chistyakova, Russ. J… |
| lit_13927 | 85YW | A. Yuchi, H. Wada, and G. Nakagawa, Anal. Sci., 1985, 1, 19 |
| lit_15666 | 90OB | R. bin Othman, N. G. Buckman, J. O. Hill, and R. J. Magee, Thermochim. Acta, 19… |

---

### Step 11: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_108709"
}
```

[summary]
## inspect_literature — vlm_108709 — 34 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_791 | 49AS | H. Ackerman and G. Schwarzenbach, Helv. Chim. Acta, 1949, 32, 1543 |
| lit_1814 | 53BK | K. Bril and P. Krumholz, J. Phys. Chem., 1953, 57, 874 |
| lit_1864 | 53HM | V. L. Hughes and A. E. Martell, J. Phys. Chem., 1953, 57, 694 |
| lit_1973 | 54C | R. G. Charles, J. Amer. Chem. Soc., 1954, 76, 5854 |
| lit_2071 | 54SG | G. Schwarzenbach, R. Gut, and G. Anderegg, Helv. Chim. Acta, 1954, 37, 937 |
| lit_1205 | 56CS | R. A. Care and L. A. K. Staveley, J. Chem. Soc., 1956, 4571 |
| lit_2306 | 56SR | R. W. Schmid and C. N. Reilley, J. Amer. Chem. Soc., 1956, 78, 5513 |
| lit_2432 | 57JA | J. Jordan and T. G. Alleman, Anal. Chem., 1957, 29, 9 |
| lit_2532 | 57SAa | G. Schwarzenbach and G. Anderegg, Helv. Chim. Acta, 1957, 40, 1773 |
| lit_3910 | 63Aa | G. Anderegg, Helv. Chim. Acta, 1963, 46, 1833 |
| lit_4660 | 64YL | C. H. Yen and S. C. Liu, Hua Hsueh Hsueh Pao (Acta Chim. Sinica), 1964, 30, 546 |
| lit_4830 | 65JM | V. Jokl and J. Majer, Chem. Zvesti, 1965, 19, 249 |
| lit_4838 | 65Kb | J. Kula, Anal. Chem., 1965, 37, 989 |
| lit_4916 | 65O | H. Ogino, Bull. Chem. Soc. Japan, 1965, 38, 771 |
| lit_4941 | 65PSS | P. T. Priestley, W. S. Sebborn, and R. F. W. Selman, Analyst (London), 1965, 90… |
| lit_5038 | 65WHR | D. L. Wright, J. H. Holloway, and C. N. Reilley, Anal. Chem., 1965, 37, 884 |
| lit_5792 | 67S | J. Stary, in "Solv. Extr. Chem. ", D. Dyrssen, J. O. Liljenzin, and J. Rydberg,… |
| lit_6185 | 68LPP | S. Laxmi, S. Prakash, and S. Prakash, Z. Phys. Chem. N. F. (Frankfurt), 1968, 6… |
| lit_1293 | 69BNS | A. P. Brunetti, G. H. Nancollas, and P. N. Smith, J. Amer. Chem. Soc., 1969, 91… |
| lit_7027 | 70FD | A. Ya. Fridman, N. M. Dyatlova, and R. P. Lastovskii, Russ. J. Inorg. Chem., 19… |
| lit_8604 | 73HRa | E. H. Hansen and J. Ruzicka, Talanta, 1973, 20, 1105 |
| lit_9944 | 76CWW | A. M. Corrie, M. D. Walker, and D. R. Williams, J. Chem. Soc. Dalton, 1976, 1012 |
| lit_10315 | 77Aee | G. Anderegg, "Critical Survey of Stability Constants of EDTA Complexes", Pergam… |
| lit_10659 | 78BKb | V. N. Belinskii, V. S. Kublanovskii, and T. S. Glushchak, Soviet Progr. Chem. (… |
| lit_10805 | 78KVc | V. I. Kornev, V. A. Valyaeva, and S. I. Zobnin, Russ. J. Phys. Chem., 1978, 52,… |
| lit_11185 | 79JPC | T. J. Janjic, L. B. Pfendt, and M. B. Celap, J. Inorg. Nucl. Chem., 1979, 41, 1… |
| lit_11186 | 79JPP | T. J. Janjic, L. B. Pfendt, and V. Popov, J. Inorg. Nucl. Chem., 1979, 41, 63 |
| lit_12202 | 82AKB | A. Avdeef, D. L. Kearney, J. A. Brown, and A. R. Chemotti, Jr., Anal. Chem., 19… |
| lit_12770 | 83IE | L. Ilcheva, N. Elenkova, and M. Tabbara, God. Vissh. Khim. Teknol. Inst., Sofia… |
| lit_13154 | 84DMW | J. R. Duffield, P. M. May, and D. R. Williams, J. Inorg. Biochem., 1984, 20, 199 |
| lit_13903 | 85VG | V. P. Vasilev, N. K. Grechina, and M. V. Tikhomirova, Russ. J. Inorg. Chem., 19… |
| lit_13911 | 85VKK | V. P. Vasilev, E. V. Kozlovskii, E. N. Kalachev, and G. V. Chistyakova, Russ. J… |
| lit_13927 | 85YW | A. Yuchi, H. Wada, and G. Nakagawa, Anal. Sci., 1985, 1, 19 |
| lit_15666 | 90OB | R. bin Othman, N. G. Buckman, J. O. Hill, and R. J. Magee, Thermochim. Acta, 19… |

---
