# Q5.1.1 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "symbol": "Hg",
  "limit": 20
}
```

[summary]
## search_metals — 8 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_53 | EtHg^[+] | EHg | 1 |  | *** | *** | beta_totN_4 | ligand_totN_3 | vlm_totN_6 |
| metal_71 | Hg^[2+] | Hg | 2 | ✓ | [Hg+2] | InChI=1S/Hg/q+2 | beta_totN_68 | ligand_totN_310 | vlm_totN_1097 |
| metal_72 | Hg^[+] | Hg | 1 | ✓ | [Hg+] | InChI=1S/Hg/q+1 | beta_totN_12 | ligand_totN_31 | vlm_totN_83 |
| metal_93 | MeHg^[+] | MHg | 1 |  | *** | *** | beta_totN_18 | ligand_totN_79 | vlm_totN_148 |
| metal_136 | PhHg^[+] | PhHg | 1 |  | *** | *** | beta_totN_2 | ligand_totN_8 | vlm_totN_8 |
| metal_145 | PrHg^[+] | Pr | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_176 | O_[3]SPhHg | S | 0 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |

---

### Step 4: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND (\n  c.ligand_name_SRD LIKE '%chloride%' OR\n  c.ligand_name_SRD LIKE '%cyanide%' OR\n  c.ligand_name_SRD LIKE '%ammonia%' OR\n  c.ligand_name_SRD LIKE '%hydroxide%' OR\n  c.ligand_name_SRD LIKE '%iodide%' OR\n  c.ligand_name_SRD LIKE '%thiocyanate%' OR\n  c.ligand_name_SRD LIKE '%EDTA%' OR\n  c.ligand_name_SRD LIKE '%ethylenediaminetetraacetic%' OR\n  c.ligand_name_SRD LIKE '%cysteine%' OR\n  c.ligand_name_SRD LIKE '%glutathione%' OR\n  c.ligand_name_SRD LIKE '%mercaptoacetate%' OR\n  c.ligand_name_SRD LIKE '%thioglycolate%'\n) AND s.temperature_c BETWEEN 293 AND 303 AND (\n  s.solvent_name LIKE '%water%' OR s.solvent_name LIKE '%aqueous%'\n) AND (\n  s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 1.0\n))",
  "order_by": "s.temperature_c ASC",
  "limit": 120
}
```

[summary]
## search_stability — 120 row(s)

### logK — 15 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 10 | 3 | 25 | 0~3 | *** | 4 |
| metal_33 | Co^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 9 | 9 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 9 | 9 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 7 | 5 | 25 | 0.1~0.5 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_9293 | N-Formyl-L-tyrosine | H2L | O=CN[C@@H](Cc1ccc(O)cc1)C(=O)O | 5 | 5 | 20 | 0.5 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 2 | 2 | 20 | 0.5 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 2 | 2 | 20 | 0.5 | *** | 1 |
| metal_68 | H^[+] | ligand_9293 | N-Formyl-L-tyrosine | H2L | O=CN[C@@H](Cc1ccc(O)cc1)C(=O)O | 2 | 2 | 20 | 0.5 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 2 | 2 | 25 | 3 | *** | 1 |
| metal_68 | H^[+] | ligand_5903 | L-1-Carboxy-2-(4-imidazolyl… | HL | C[N+](C)(C)C(Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_5923 | L-[1-Carboxy-2-(4-hydroxyph… | H2L | C[N+](C)(C)C(Cc1ccc(O)cc1)C(=O)O.[Cl-] | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5947 | DL-[1-Carboxy-2-(2-mercapto… | H2L | C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-] | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_112 | Ni^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 8 | 8 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5903 | L-1-Carboxy-2-(4-imidazolyl… | HL | C[N+](C)(C)C(Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

### ΔS — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_112 | Ni^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 8 | 8 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5903 | L-1-Carboxy-2-(4-imidazolyl… | HL | C[N+](C)(C)C(Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

---

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_72 AND (\n  c.ligand_name_SRD LIKE '%chloride%' OR\n  c.ligand_name_SRD LIKE '%cyanide%' OR\n  c.ligand_name_SRD LIKE '%ammonia%' OR\n  c.ligand_name_SRD LIKE '%iodide%' OR\n  c.ligand_name_SRD LIKE '%thiocyanate%'\n) AND s.temperature_c BETWEEN 293 AND 303 AND (\n  s.solvent_name LIKE '%water%' OR s.solvent_name LIKE '%aqueous%'\n) AND (\n  s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 1.0\n))",
  "order_by": "s.temperature_c ASC",
  "limit": 120
}
```

[summary]
## search_stability — 120 row(s)

### logK — 15 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 10 | 3 | 25 | 0~3 | *** | 4 |
| metal_33 | Co^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 9 | 9 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 9 | 9 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 7 | 5 | 25 | 0.1~0.5 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_9293 | N-Formyl-L-tyrosine | H2L | O=CN[C@@H](Cc1ccc(O)cc1)C(=O)O | 5 | 5 | 20 | 0.5 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 2 | 2 | 20 | 0.5 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 2 | 2 | 20 | 0.5 | *** | 1 |
| metal_68 | H^[+] | ligand_9293 | N-Formyl-L-tyrosine | H2L | O=CN[C@@H](Cc1ccc(O)cc1)C(=O)O | 2 | 2 | 20 | 0.5 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 2 | 2 | 25 | 3 | *** | 1 |
| metal_68 | H^[+] | ligand_5903 | L-1-Carboxy-2-(4-imidazolyl… | HL | C[N+](C)(C)C(Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_5923 | L-[1-Carboxy-2-(4-hydroxyph… | H2L | C[N+](C)(C)C(Cc1ccc(O)cc1)C(=O)O.[Cl-] | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5947 | DL-[1-Carboxy-2-(2-mercapto… | H2L | C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-] | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_112 | Ni^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 8 | 8 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5903 | L-1-Carboxy-2-(4-imidazolyl… | HL | C[N+](C)(C)C(Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

### ΔS — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_112 | Ni^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 8 | 8 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5903 | L-1-Carboxy-2-(4-imidazolyl… | HL | C[N+](C)(C)C(Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

---
