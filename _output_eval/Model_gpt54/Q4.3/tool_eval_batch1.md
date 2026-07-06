# Q4.3 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Copper(II), Nickel(II), Zinc(II)",
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
  "name": "ethylenediamine, ammonia",
  "limit": 20
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
  "symbol": "Cu, Ni, Zn",
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
  "name": "ethylenediamine, ammonia, ethane-1,2-diamine, azane",
  "limit": 50
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
  "where": "(c.metal_name_SRD LIKE '%Copper%' OR c.metal_name_SRD LIKE '%Nickel%' OR c.metal_name_SRD LIKE '%Zinc%') AND (c.ligand_name_SRD LIKE '%ethylenediamine%' OR c.ligand_name_SRD LIKE '%ammonia%' OR c.ligand_name_SRD LIKE '%ammine%' OR c.ligand_name_SRD LIKE '%azane%')",
  "order_by": "c.metal_name_SRD, c.ligand_name_SRD, s.temperature_c, s.ionic_strength_mol_l",
  "limit": 200
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 9: `build_system_catalog`
**Args:**
```json
{
  "beta_definition_id": "beta_def_1"
}
```

[summary]
[CATALOG]
## build_system_catalog — 2 pair(s), 6 species

### H^[+] + 2,6-Bis(hydroxymethyl)pyridine
**metal_id:** metal_68 | **ligand_id:** ligand_8003 | **ligand_def_HxL:** L  
**entries:** 3 | **species:** 3 | **vlm_count:** 3

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_1 | [H<sub>-1</sub>L]/[H<sub>-2</sub>L][H] | [H-2L] + [H] <=> [H-1L] | [H-1L](aqueous), [H-2L](aqueous), [H](aqueous) | 1 |
| beta_def_79 | [HL]/[L][H] | [L] + [H] <=> [HL] | [HL](aqueous), [L](aqueous), [H](aqueous) | 1 |
| beta_def_103 | [L]/[H<sub>-1</sub>L][H] | [H-1L] + [H] <=> [L] | [L](aqueous), [H-1L](aqueous), [H](aqueous) | 1 |

**vlm_ids:** vlm_136547, vlm_136548, vlm_136549

**equilibrium_maps:** 1 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_14300 | 3 | 3 | 12.5~27.5 °C | 0.275~0.725 M |

---

### H^[+] + Pyridine-2,6-dicarboxaldehyde
**metal_id:** metal_68 | **ligand_id:** ligand_8012 | **ligand_def_HxL:** L  
**entries:** 3 | **species:** 3 | **vlm_count:** 3

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_1 | [H<sub>-1</sub>L]/[H<sub>-2</sub>L][H] | [H-2L] + [H] <=> [H-1L] | [H-1L](aqueous), [H-2L](aqueous), [H](aqueous) | 1 |
| beta_def_79 | [HL]/[L][H] | [L] + [H] <=> [HL] | [HL](aqueous), [L](aqueous), [H](aqueous) | 1 |
| beta_def_103 | [L]/[H<sub>-1</sub>L][H] | [H-1L] + [H] <=> [L] | [L](aqueous), [H-1L](aqueous), [H](aqueous) | 1 |

**vlm_ids:** vlm_136606, vlm_136607, vlm_136608

**equilibrium_maps:** 1 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_14319 | 3 | 3 | 16.5~31.5 °C | 0.275~0.725 M |

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "((c.metal_name_SRD LIKE '%Copper%' OR c.metal_name_SRD LIKE '%Nickel%' OR c.metal_name_SRD LIKE '%Zinc%' OR c.metal_name_SRD LIKE '%cupric%' OR c.metal_name_SRD LIKE '%nickel(II)%' OR c.metal_name_SRD LIKE '%zinc(II)%') AND (c.ligand_name_SRD LIKE '%amm%' OR c.ligand_name_SRD LIKE '%ammon%' OR c.ligand_name_SRD LIKE '%ethylenediam%' OR c.ligand_name_SRD LIKE '%ethane-1,2-diam%' OR c.ligand_name_SRD LIKE '%1,2-diaminoethane%' OR c.ligand_name_SRD = 'en'))",
  "order_by": "c.metal_name_SRD, c.ligand_name_SRD, s.temperature_c, s.ionic_strength_mol_l, s.constant_value",
  "limit": 200
}
```

[summary]
## search_stability — 128 row(s)

### logK — 32 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_6575 | Glycylglycyl-L-histidine | HL | NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O | 9 | 6 | 25~37 | 0.1~1 | *** | 3 |
| metal_68 | H^[+] | ligand_6575 | Glycylglycyl-L-histidine | HL | NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O | 9 | 3 | 20~37 | 0.1~0.15 | *** | 3 |
| metal_41 | Cu^[2+] | ligand_5961 | L-2-(Benzylamino)-3-(4-imid… | HL | O=C(O)C(Cc1cnc[nH]1)NCc1ccccc1 | 6 | 4 | 25 | 0.1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_6027 | L-2-(Dimethylamino)-3-(4-im… | HL | CN(C)C(Cc1cnc[nH]1)C(=O)O | 6 | 4 | 25 | 0.1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_5960 | L-2-(Methylamino)-3-(4-imid… | HL | CNC(Cc1cnc[nH]1)C(=O)O | 5 | 4 | 25 | 0.1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_6463 | L-Leucyl-L-histidine | HL | CC(C)C[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O | 5 | 5 | 37 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6575 | Glycylglycyl-L-histidine | HL | NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O | 5 | 5 | 25 | 0.1~1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_6575 | Glycylglycyl-L-histidine | HL | NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O | 5 | 5 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6027 | L-2-(Dimethylamino)-3-(4-im… | HL | CN(C)C(Cc1cnc[nH]1)C(=O)O | 5 | 3 | 25 | 0.1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_5961 | L-2-(Benzylamino)-3-(4-imid… | HL | O=C(O)C(Cc1cnc[nH]1)NCc1ccccc1 | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_6027 | L-2-(Dimethylamino)-3-(4-im… | HL | CN(C)C(Cc1cnc[nH]1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_5960 | L-2-(Methylamino)-3-(4-imid… | HL | CNC(Cc1cnc[nH]1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_6648 | Glycylglycylglycyl-L-histid… | HL | NCC(=O)NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6648 | Glycylglycylglycyl-L-histid… | HL | NCC(=O)NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5902 | L-1-Carboxy-2-(4-imidazolyl… | HL | C[NH+](C)C(Cc1cnc[nH]1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5961 | L-2-(Benzylamino)-3-(4-imid… | HL | O=C(O)C(Cc1cnc[nH]1)NCc1ccccc1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6027 | L-2-(Dimethylamino)-3-(4-im… | HL | CN(C)C(Cc1cnc[nH]1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5960 | L-2-(Methylamino)-3-(4-imid… | HL | CNC(Cc1cnc[nH]1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6463 | L-Leucyl-L-histidine | HL | CC(C)C[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O | 3 | 3 | 37 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6525 | L-Methionyl-L-histidine | HL | CSCC[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6517 | N-(3-Mercaptopropionyl)-L-h… | H2L | O=C(CCS)N[C@@H](Cc1cnc[nH]1)C(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6516 | N-(Mercaptoacetyl)-L-histid… | H2L | O=C(CS)N[C@@H](Cc1cnc[nH]1)C(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6594 | N-(Mercaptoacetyl)glycyl-L-… | H2L | O=C(CS)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6648 | Glycylglycylglycyl-L-histid… | HL | NCC(=O)NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5961 | L-2-(Benzylamino)-3-(4-imid… | HL | O=C(O)C(Cc1cnc[nH]1)NCc1ccccc1 | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_6027 | L-2-(Dimethylamino)-3-(4-im… | HL | CN(C)C(Cc1cnc[nH]1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_5960 | L-2-(Methylamino)-3-(4-imid… | HL | CNC(Cc1cnc[nH]1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5961 | L-2-(Benzylamino)-3-(4-imid… | HL | O=C(O)C(Cc1cnc[nH]1)NCc1ccccc1 | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5960 | L-2-(Methylamino)-3-(4-imid… | HL | CNC(Cc1cnc[nH]1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_6463 | L-Leucyl-L-histidine | HL | CC(C)C[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O | 3 | 3 | 37 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6525 | L-Methionyl-L-histidine | HL | CSCC[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6525 | L-Methionyl-L-histidine | HL | CSCC[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |

### ΔS — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5902 | L-1-Carboxy-2-(4-imidazolyl… | HL | C[NH+](C)C(Cc1cnc[nH]1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |

### ΔH — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5902 | L-1-Carboxy-2-(4-imidazolyl… | HL | C[NH+](C)C(Cc1cnc[nH]1)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |

---

### Step 12: `search_networks`
**Args:**
```json
{
  "where": "((c.metal_name LIKE '%Copper%' OR c.metal_name LIKE '%Nickel%' OR c.metal_name LIKE '%Zinc%' OR c.metal_name LIKE '%cupric%') AND (c.ligand_name LIKE '%amm%' OR c.ligand_name LIKE '%ammon%' OR c.ligand_name LIKE '%ethylenediam%' OR c.ligand_name LIKE '%ethane-1,2-diam%' OR c.ligand_name LIKE '%1,2-diaminoethane%' OR c.ligand_name = 'en'))",
  "order_by": "c.metal_name, c.ligand_name, n.network_db_id",
  "limit": 100
}
```

[summary]
## search_networks — 122 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_107 | ``[M(H-1L)] + [H] <=> [ML]`` |
| beta_def_831 | ``[M(H-2L)] + [H]^2 <=> [ML]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_721 | ``[M(H-2L)] + [H] <=> [MH(H-2L)]`` |
| beta_def_729 | ``[MH(H-2L)] + [H] <=> [MH2(H-2L)]`` |
| beta_def_143 | ``[M(H-2L)] + [H] <=> [M(H-1L)]`` |
| beta_def_182 | ``[M(H-3L)] + [H] <=> [M(H-2L)]`` |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` |
| beta_def_117 | ``[M(OH)(H-1L)] + [H] <=> [M(H-1L)] + [H2O]`` |
| beta_def_860 | ``[M(H-1L)L] + [H] <=> [ML2]`` |
| beta_def_32 | ``[HL] + [H] <=> [H2L]`` |
| beta_def_53 | ``[H2L] + [H] <=> [H3L]`` |
| beta_def_79 | ``[L] + [H] <=> [HL]`` |
| beta_def_723 | `*` |
| beta_def_528 | ``[ML]^2 <=> [M2L2]`` |
| beta_def_531 | ``[M2(H-1L)L] + [H] <=> [M2L2]`` |
| beta_def_384 | ``[M2(H-1L)2] + [H] <=> [M2(H-1L)L]`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_783 | ``[M(H-1L)] + [H]^2 <=> [MHL]`` |
| beta_def_800 | ``[MHL] + [L] <=> [MHL2]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | max_net_id | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|------------|---------------|
| `Co^[2+]` | metal_33 | L-2-(Benzylamino)-3-(4-imidazolyl)propa… | ligand_5961 | HL | 19~30 | -0.05~0.25 | 2 | 2 | ref_eq_net_1690 | O=C(O)C(Cc1cnc[nH]1)NCc1ccccc1 |
| `Co^[2+]` | metal_33 | L-2-(Dimethylamino)-3-(4-imidazolyl)pro… | ligand_6027 | HL | 19~30 | -0.05~0.25 | 2 | 2 | ref_eq_net_2326 | CN(C)C(Cc1cnc[nH]1)C(=O)O |
| `Co^[2+]` | metal_33 | L-2-(Methylamino)-3-(4-imidazolyl)propa… | ligand_5960 | HL | 19~30 | -0.05~0.25 | 2 | 2 | ref_eq_net_1681 | CNC(Cc1cnc[nH]1)C(=O)O |
| `Cu^[2+]` | metal_41 | Glycylglycyl-L-histidine | ligand_6575 | HL | 19~41 | -0.05~1.15 | 3 | 4 | ref_eq_net_7633 | NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O |
| `Cu^[2+]` | metal_41 | Glycylglycylglycyl-L-histidine | ligand_6648 | HL | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_7826 | NCC(=O)NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-(Benzylamino)-3-(4-imidazolyl)propa… | ligand_5961 | HL | 19~30 | -0.05~0.25 | 2 | 4 | ref_eq_net_1694 | O=C(O)C(Cc1cnc[nH]1)NCc1ccccc1 |
| `Cu^[2+]` | metal_41 | L-2-(Dimethylamino)-3-(4-imidazolyl)pro… | ligand_6027 | HL | 19~30 | -0.05~0.25 | 2 | 4 | ref_eq_net_2330 | CN(C)C(Cc1cnc[nH]1)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-(Methylamino)-3-(4-imidazolyl)propa… | ligand_5960 | HL | 19~30 | -0.05~0.25 | 2 | 4 | ref_eq_net_1685 | CNC(Cc1cnc[nH]1)C(=O)O |
| `Cu^[2+]` | metal_41 | L-Leucyl-L-histidine | ligand_6463 | HL | 28.5~43.5 | -0.125~0.325 | 1 | 5 | ref_eq_net_7333 | CC(C)C[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O |
| `Cu^[2+]` | metal_41 | L-Methionyl-L-histidine | ligand_6525 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_7485 | CSCC[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O |
| `H^[+]` | metal_68 | Glycylglycyl-L-histidine | ligand_6575 | HL | 15~41 | -0.05~0.3 | 3 | 3 | ref_eq_net_7627 | NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O |
| `H^[+]` | metal_68 | Glycylglycylglycyl-L-histidine | ligand_6648 | HL | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_7824 | NCC(=O)NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O |
| `H^[+]` | metal_68 | L-1-Carboxy-2-(4-imidazolyl)ethyl(dimet… | ligand_5902 | HL | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_1374 | C[NH+](C)C(Cc1cnc[nH]1)C(=O)O |
| `H^[+]` | metal_68 | L-2-(Benzylamino)-3-(4-imidazolyl)propa… | ligand_5961 | HL | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_1689 | O=C(O)C(Cc1cnc[nH]1)NCc1ccccc1 |
| `H^[+]` | metal_68 | L-2-(Dimethylamino)-3-(4-imidazolyl)pro… | ligand_6027 | HL | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_2325 | CN(C)C(Cc1cnc[nH]1)C(=O)O |
| `H^[+]` | metal_68 | L-2-(Methylamino)-3-(4-imidazolyl)propa… | ligand_5960 | HL | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_1680 | CNC(Cc1cnc[nH]1)C(=O)O |
| `H^[+]` | metal_68 | L-Leucyl-L-histidine | ligand_6463 | HL | 28.5~43.5 | -0.125~0.325 | 1 | 3 | ref_eq_net_7332 | CC(C)C[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O |
| `H^[+]` | metal_68 | L-Methionyl-L-histidine | ligand_6525 | HL | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_7483 | CSCC[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O |
| `H^[+]` | metal_68 | N-(3-Mercaptopropionyl)-L-histidine | ligand_6517 | H2L | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_7466 | O=C(CCS)N[C@@H](Cc1cnc[nH]1)C(=O)O |
| `H^[+]` | metal_68 | N-(Mercaptoacetyl)-L-histidine | ligand_6516 | H2L | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_7465 | O=C(CS)N[C@@H](Cc1cnc[nH]1)C(=O)O |
| `H^[+]` | metal_68 | N-(Mercaptoacetyl)glycyl-L-histidine | ligand_6594 | H2L | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_7705 | O=C(CS)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O |
| `Ni^[2+]` | metal_112 | Glycylglycyl-L-histidine | ligand_6575 | HL | 19~30 | -0.05~1.15 | 3 | 3 | ref_eq_net_7630 | NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O |
| `Ni^[2+]` | metal_112 | Glycylglycylglycyl-L-histidine | ligand_6648 | HL | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_7825 | NCC(=O)NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O |
| `Ni^[2+]` | metal_112 | L-2-(Benzylamino)-3-(4-imidazolyl)propa… | ligand_5961 | HL | 19~30 | -0.05~0.25 | 2 | 2 | ref_eq_net_1692 | O=C(O)C(Cc1cnc[nH]1)NCc1ccccc1 |
| `Ni^[2+]` | metal_112 | L-2-(Dimethylamino)-3-(4-imidazolyl)pro… | ligand_6027 | HL | 19~30 | -0.05~0.25 | 2 | 2 | ref_eq_net_2328 | CN(C)C(Cc1cnc[nH]1)C(=O)O |
| `Ni^[2+]` | metal_112 | L-2-(Methylamino)-3-(4-imidazolyl)propa… | ligand_5960 | HL | 19~30 | -0.05~0.25 | 2 | 2 | ref_eq_net_1683 | CNC(Cc1cnc[nH]1)C(=O)O |
| `Ni^[2+]` | metal_112 | L-Methionyl-L-histidine | ligand_6525 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_7484 | CSCC[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O |
| `Zn^[2+]` | metal_208 | Glycylglycyl-L-histidine | ligand_6575 | HL | 28.5~43.5 | -0.075~0.375 | 1 | 5 | ref_eq_net_7636 | NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O |
| `Zn^[2+]` | metal_208 | L-2-(Benzylamino)-3-(4-imidazolyl)propa… | ligand_5961 | HL | 19~30 | -0.05~0.25 | 2 | 2 | ref_eq_net_1696 | O=C(O)C(Cc1cnc[nH]1)NCc1ccccc1 |
| `Zn^[2+]` | metal_208 | L-2-(Dimethylamino)-3-(4-imidazolyl)pro… | ligand_6027 | HL | 19~30 | -0.05~0.25 | 3 | 3 | ref_eq_net_2332 | CN(C)C(Cc1cnc[nH]1)C(=O)O |
| `Zn^[2+]` | metal_208 | L-2-(Methylamino)-3-(4-imidazolyl)propa… | ligand_5960 | HL | 19~30 | -0.05~0.25 | 2 | 2 | ref_eq_net_1687 | CNC(Cc1cnc[nH]1)C(=O)O |
| `Zn^[2+]` | metal_208 | L-Leucyl-L-histidine | ligand_6463 | HL | 28.5~43.5 | -0.125~0.325 | 1 | 3 | ref_eq_net_7334 | CC(C)C[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O |

### Global max-node network: `Cu^[2+]` + L-Leucyl-L-histidine
network_id: ref_eq_net_7333 | metal_id: metal_41 | ligand_id: ligand_6463 | ligand_def_HxL: HL | nodes: 5

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_107 | ``[M(H-1L)] + [H] <=> [ML]`` | logK | 4.35 |
| beta_def_860 | ``[M(H-1L)L] + [H] <=> [ML2]`` | logK | 7.1 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 8.98 |
| beta_def_117 | ``[M(OH)(H-1L)] + [H] <=> [M(H-1L)] + [H2O]`` | logK | 9.42 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 14.3 |

---
