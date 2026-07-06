# Q4.1 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "iron",
  "limit": 10
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "dimethylformamide",
  "limit": 15
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 15

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_11422 | N,N-Dimethylformamide (DMF) | *** | Ligands not selected | 0 | *** | *** |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "acetonitrile",
  "limit": 15
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 15

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9825 | Cyanomethane (Acetonitrile) | L | miscellaneous hydrocarbo… | 7 | `CC#N` | *** |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| nitrile | 1 | 100% |

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "tetrahydrofuran",
  "limit": 15
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "ethylene glycol",
  "limit": 15
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 15

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9621 | Ethane-1,2-diol (Ethylene glycol) | *** | miscellaneous alcohols a… | 22 | *** | *** |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "oxolane",
  "limit": 15
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 15

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6340 | 2,5-Bis[bis(carboxymethyl)aminomethyl]oxolane | H4L | EDTA and derivatives | 5 | `O=C(O)CN(CC(=O)O)CC1CCC(CN(CC(=O)O)CC(=O)O)O1` | (-inf, H4L, 2.42, H3L, 2.73, H2L, 8.67, HL, 8.95, L, +inf) |
| ligand_8979 | H2L Oxolane… (Perhydrofuran-2,5-dicarboxylic acid) | H2L | Carboxylic acids diacids | 1 | `O=C(O)C1CCC(C(=O)O)O1` | *** |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| ether | 2 | 100% |
| tertiary_amine | 1 | 50% |

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "smiles": "C1CCOC1",
  "limit": 15
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "tetramethylene oxide",
  "limit": 15
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id IN (metal_61, metal_62) AND c.ligand_id = ligand_9825",
  "order_by": "s.constant_value DESC",
  "limit": 200
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id IN (metal_61, metal_62) AND (c.ligand_id = ligand_9621 OR c.ligand_name_SRD LIKE '%ethylene glycol%')",
  "order_by": "s.constant_value DESC",
  "limit": 200
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id IN (metal_61, metal_62) AND (c.ligand_id = ligand_11422 OR c.ligand_name_SRD LIKE '%dimethylformamide%' OR c.ligand_name_SRD LIKE '%DMF%')",
  "order_by": "s.constant_value DESC",
  "limit": 200
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id IN (metal_61, metal_62) AND (c.ligand_name_SRD LIKE '%tetrahydrofuran%' OR c.ligand_name_SRD LIKE '%THF%' OR c.ligand_name_SRD LIKE '%oxolane%')",
  "order_by": "s.constant_value DESC",
  "limit": 200
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id IN (metal_61, metal_62) AND (c.ligand_name_SRD LIKE '%acetamide%' OR c.ligand_name_SRD LIKE '%formamide%' OR c.ligand_name_SRD LIKE '%urea%' OR c.ligand_name_SRD LIKE '%dimethylacetamide%' OR c.ligand_name_SRD LIKE '%DMSO%' OR c.ligand_name_SRD LIKE '%dioxane%' OR c.ligand_name_SRD LIKE '%diethyl ether%' OR c.ligand_name_SRD LIKE '%benzonitrile%' OR c.ligand_name_SRD LIKE '%propionitrile%' OR c.ligand_name_SRD LIKE '%diethylene glycol%' OR c.ligand_name_SRD LIKE '%glycerol%')",
  "order_by": "s.constant_value DESC",
  "limit": 300
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 16: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_9825"
}
```

[summary]
[CATALOG]
## build_system_catalog — 3 pair(s), 5 species

### Pd^[2+] + Cyanomethane (Acetonitrile)
**metal_id:** metal_127 | **ligand_id:** ligand_9825 | **ligand_def_HxL:** L  
**entries:** 4 | **species:** 2 | **vlm_count:** 4

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 3 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 1 |

**vlm_ids:** vlm_168277, vlm_168278, vlm_168279, vlm_168280

**equilibrium_maps:** 1 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_26528 | 2 | 1 | 16.5~31.5 °C | 0.775~1.225 M |

---

### Ag^[+] + Cyanomethane (Acetonitrile)
**metal_id:** metal_2 | **ligand_id:** ligand_9825 | **ligand_def_HxL:** L  
**entries:** 2 | **species:** 2 | **vlm_count:** 2

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 1 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 1 |

**vlm_ids:** vlm_168275, vlm_168276

**equilibrium_maps:** 1 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_26527 | 2 | 1 | 20~30 °C | -0.05~0.25 M |

---

### Cu^[+] + Cyanomethane (Acetonitrile)
**metal_id:** metal_42 | **ligand_id:** ligand_9825 | **ligand_def_HxL:** L  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 1 |

**vlm_ids:** vlm_168274

**equilibrium_maps:** 1 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_26526 | 1 | 0 | 20~30 °C | -0.05~0.25 M |

---

### Step 17: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_9621"
}
```

[summary]
[CATALOG]
## build_system_catalog — 18 pair(s), 20 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_85 | [M(OH)4] + [L]^2 <=> [HMO(H-2L)2] + [H] + [H2O]^3 |  |
| beta_def_86 | [M(OH)4] + [L] <=> [HMO2(H-2L)] + [H] + [H2O]^2 |  |
| beta_def_169 | [M(OH)4] + [L]^2 <=> [M(H-2L)2] + [H2O]^4 |  |
| beta_def_225 | [M(OH)4] + [L] <=> [M(OH)2(H-2L)] + [H2O]^2 |  |
| beta_def_726 | [M] + [L] <=> [MH-1L] + [H] |  |
| beta_def_956 | [M(OH)3] + [L] <=> [M(OH)(H-2L)] + [H2O]^2 |  |

*(all species aqueous)*

**1. B^[3+] + Ethane-1,2-diol (Ethylene glycol)** (metal_15 + ligand_9621) — ligand_def_HxL: *** | 4 ent, 2 sp, 4 vlms (vlm_166932…vlm_166935)
   - species: beta_def_169(1) beta_def_225(3)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 2n/1e
**2. Ge^[4+] + Ethane-1,2-diol (Ethylene glycol)** (metal_66 + ligand_9621) — ligand_def_HxL: *** | 2 ent, 2 sp, 2 vlms (vlm_166936, vlm_166937)
   - species: beta_def_85(1) beta_def_86(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 2n/1e
**3. Yb^[3+] + Ethane-1,2-diol (Ethylene glycol)** (metal_206 + ligand_9621) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_166929)
   - species: beta_def_726(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**4. Y^[3+] + Ethane-1,2-diol (Ethylene glycol)** (metal_205 + ligand_9621) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_166916)
   - species: beta_def_726(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**5. Tm^[3+] + Ethane-1,2-diol (Ethylene glycol)** (metal_192 + ligand_9621) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_166928)
   - species: beta_def_726(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**6. Tb^[3+] + Ethane-1,2-diol (Ethylene glycol)** (metal_179 + ligand_9621) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_166924)
   - species: beta_def_726(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**7. Sm^[3+] + Ethane-1,2-diol (Ethylene glycol)** (metal_173 + ligand_9621) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_166921)
   - species: beta_def_726(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**8. Pr^[3+] + Ethane-1,2-diol (Ethylene glycol)** (metal_139 + ligand_9621) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_166919)
   - species: beta_def_726(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**9. Pb^[2+] + Ethane-1,2-diol (Ethylene glycol)** (metal_125 + ligand_9621) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_166931)
   - species: beta_def_956(1)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 1n/0e
**10. Nd^[3+] + Ethane-1,2-diol (Ethylene glycol)** (metal_110 + ligand_9621) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_166920)
   - species: beta_def_726(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**11. Lu^[3+] + Ethane-1,2-diol (Ethylene glycol)** (metal_81 + ligand_9621) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_166930)
   - species: beta_def_726(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**12. La^[3+] + Ethane-1,2-diol (Ethylene glycol)** (metal_79 + ligand_9621) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_166917)
   - species: beta_def_726(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**13. Ho^[3+] + Ethane-1,2-diol (Ethylene glycol)** (metal_73 + ligand_9621) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_166926)
   - species: beta_def_726(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**14. Gd^[3+] + Ethane-1,2-diol (Ethylene glycol)** (metal_65 + ligand_9621) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_166923)
   - species: beta_def_726(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**15. Eu^[3+] + Ethane-1,2-diol (Ethylene glycol)** (metal_58 + ligand_9621) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_166922)
   - species: beta_def_726(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**16. Er^[3+] + Ethane-1,2-diol (Ethylene glycol)** (metal_55 + ligand_9621) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_166927)
   - species: beta_def_726(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**17. Dy^[3+] + Ethane-1,2-diol (Ethylene glycol)** (metal_44 + ligand_9621) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_166925)
   - species: beta_def_726(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**18. Ce^[3+] + Ethane-1,2-diol (Ethylene glycol)** (metal_27 + ligand_9621) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_166918)
   - species: beta_def_726(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e

---

### Step 18: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_11422"
}
```

[summary]
[CATALOG]
## build_system_catalog

*(no pairs found)*

**summary:** {'n_metals': 0, 'n_ligands': 0, 'n_pairs': 0, 'total_species': 0}

---

### Step 20: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND c.ligand_id = ligand_9825)",
  "order_by": "s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 21: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND c.ligand_id = ligand_9621)",
  "order_by": "s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 22: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND (c.ligand_id = ligand_11422 OR c.ligand_name_SRD LIKE '%dimethylformamide%' OR c.ligand_name_SRD LIKE '%DMF%'))",
  "order_by": "s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 23: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND (c.ligand_name_SRD LIKE '%tetrahydrofuran%' OR c.ligand_name_SRD LIKE '%THF%' OR c.ligand_name_SRD LIKE '%oxolane%'))",
  "order_by": "s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 24: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND (c.ligand_name_SRD LIKE '%formamide%' OR c.ligand_name_SRD LIKE '%acetamide%' OR c.ligand_name_SRD LIKE '%dimethylacetamide%' OR c.ligand_name_SRD LIKE '%DMAc%' OR c.ligand_name_SRD LIKE '%urea%'))",
  "order_by": "s.constant_value DESC",
  "limit": 300
}
```

[summary]
## search_stability

*(no results)*

---

### Step 25: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND (c.ligand_name_SRD LIKE '%benzonitrile%' OR c.ligand_name_SRD LIKE '%propionitrile%'))",
  "order_by": "s.constant_value DESC",
  "limit": 300
}
```

[summary]
## search_stability — 136 row(s)

### ΔS — 23 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_139 | Pr^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_58 | Eu^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_173 | Sm^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_195 | UO_[2]^[2+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_192 | Tm^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_81 | Lu^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_55 | Er^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_73 | Ho^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_205 | Y^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_44 | Dy^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_179 | Tb^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_110 | Nd^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_65 | Gd^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_2 | Ag^[+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_80 | Li^[+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_106 | Na^[+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_78 | K^[+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔH — 23 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_139 | Pr^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_58 | Eu^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_173 | Sm^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_195 | UO_[2]^[2+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_192 | Tm^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_81 | Lu^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_55 | Er^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_73 | Ho^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_205 | Y^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_44 | Dy^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_179 | Tb^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_110 | Nd^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_65 | Gd^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_2 | Ag^[+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_80 | Li^[+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_106 | Na^[+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_78 | K^[+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 52 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 5 | 1 | 25~37 | 0~3 | *** | 5 |
| metal_25 | Ca^[2+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 3 | 1 | 25~37 | 0~0.15 | *** | 3 |
| metal_92 | Mg^[2+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 3 | 1 | 25~37 | 0~0.15 | *** | 3 |
| metal_80 | Li^[+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 3 | 1 | 25~37 | 0~0.15 | *** | 3 |
| metal_106 | Na^[+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 3 | 1 | 25~37 | 0~0.15 | *** | 3 |
| metal_78 | K^[+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 3 | 1 | 25~37 | 0~0.15 | *** | 3 |
| metal_79 | La^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_139 | Pr^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_195 | UO_[2]^[2+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_27 | Ce^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_8984 | (2-Carboxyphenyloxy)acetic … | H2L | O=C(O)COc1ccccc1C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 2 | 1 | 25~37 | 0.1~0.15 | *** | 2 |
| metal_192 | Tm^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_205 | Y^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_8753 | 2-Methoxyphenoxyacetic acid | HL | COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_8729 | 2-Methylphenoxyacetic acid | HL | Cc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_8741 | 2-Iodophenoxyacetic acid | HL | O=C(O)COc1ccccc1I | 1 | 1 | 25 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_8738 | 2-Bromophenoxyacetic acid | HL | O=C(O)COc1ccccc1Br | 1 | 1 | 25 | 0 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_8984 | (2-Carboxyphenyloxy)acetic … | H2L | O=C(O)COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_8732 | 2-Fluorophenoxyacetic acid | HL | O=C(O)COc1ccccc1F | 1 | 1 | 25 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_8735 | 2-Chlorophenoxyacetic acid | HL | O=C(O)COc1ccccc1Cl | 1 | 1 | 25 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_8750 | 2-Cyanophenoxyacetic acid | HL | N#Cc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_8752 | 4-Cyanophenoxyacetic acid | HL | N#Cc1ccc(OCC(=O)O)cc1 | 1 | 1 | 25 | 0 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_8984 | (2-Carboxyphenyloxy)acetic … | H2L | O=C(O)COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_177 | Sr^[2+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_8984 | (2-Carboxyphenyloxy)acetic … | H2L | O=C(O)COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_8984 | (2-Carboxyphenyloxy)acetic … | H2L | O=C(O)COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_8725 | Phenoxyacetic acid | HL | O=C(O)COc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_8984 | (2-Carboxyphenyloxy)acetic … | H2L | O=C(O)COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

---

### Step 26: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND (c.ligand_name_SRD LIKE '%1,4-dioxane%' OR c.ligand_name_SRD LIKE '%dioxane%' OR c.ligand_name_SRD LIKE '%dimethoxyethane%' OR c.ligand_name_SRD LIKE '%monoglyme%' OR c.ligand_name_SRD LIKE '%diethyl ether%' OR c.ligand_name_SRD LIKE '%tetrahydropyran%'))",
  "order_by": "s.constant_value DESC",
  "limit": 300
}
```

[summary]
## search_stability — 1 row(s)

### `Fe^[2+]` + N-(2-Tetrahydropyranylmethyl)iminodiacetic acid — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_6224
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CN(CC(=O)O)CC1CCCCO1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_107056 | ref_eq_map_4409 | beta_def_812 | logK | 7.4 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.04, L, +inf) |

---

### Step 27: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND (c.ligand_name_SRD LIKE '%diethylene glycol%' OR c.ligand_name_SRD LIKE '%triethylene glycol%' OR c.ligand_name_SRD LIKE '%glycerol%' OR c.ligand_name_SRD LIKE '%propylene glycol%'))",
  "order_by": "s.constant_value DESC",
  "limit": 300
}
```

[summary]
## search_stability — 200 row(s)

### ΔS — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 4 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_7583 | 1,4,7,13-Tetraoxa-10,16-dia… | L | C1COCCNCCOCCOCCOCCN1 | 2 | 2 | 25 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_7546 | Perhydro-1,4-oxazine (Morph… | L | C1COCCN1 | 2 | 1 | 25 | 0~0.5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_177 | Sr^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 73 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 12 | 6 | 25~35 | 0.1 | *** | 3 |
| metal_41 | Cu^[2+] | ligand_7649 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 8 | 8 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 8 | 8 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7649 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 8 | 8 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 8 | 8 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 7 | 7 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 7 | 7 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 7 | 7 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 6 | 2 | 25 | 0~0.5 | *** | 3 |
| metal_68 | H^[+] | ligand_7546 | Perhydro-1,4-oxazine (Morph… | L | C1COCCN1 | 6 | 1 | 10~40 | 0~1 | *** | 6 |
| metal_68 | H^[+] | ligand_7649 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7642 | 1,4-Dioxa-7,10,13,16,19-pen… | L | C1CNCCNCCOCCOCCNCCNCCN1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 4 | 2 | 25~35 | 0.1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_7642 | 1,4-Dioxa-7,10,13,16,19-pen… | L | C1CNCCNCCOCCOCCNCCNCCN1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_68 | H^[+] | ligand_7583 | 1,4,7,13-Tetraoxa-10,16-dia… | L | C1COCCNCCOCCOCCOCCN1 | 2 | 2 | 25 | 0 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_2 | Ag^[+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7642 | 1,4-Dioxa-7,10,13,16,19-pen… | L | C1CNCCNCCOCCOCCNCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7642 | 1,4-Dioxa-7,10,13,16,19-pen… | L | C1CNCCNCCOCCOCCNCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7642 | 1,4-Dioxa-7,10,13,16,19-pen… | L | C1CNCCNCCOCCOCCNCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7572 | 1,4-Dioxa-7,10-diazacyclodo… | L | C1CNCCOCCOCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_37 | Cr^[3+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_37 | Cr^[3+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7572 | 1,4-Dioxa-7,10-diazacyclodo… | L | C1CNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7572 | 1,4-Dioxa-7,10-diazacyclodo… | L | C1CNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7572 | 1,4-Dioxa-7,10-diazacyclodo… | L | C1CNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_7546 | Perhydro-1,4-oxazine (Morph… | L | C1COCCN1 | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |

---
