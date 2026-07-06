# Q5.1.4 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "zinc"
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 3: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurements",
  "limit": 10,
  "where": {
    "metal_id": 208
  }
}
```

[PHASE ERROR] Tool 'db_ranked_pairs' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 4: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "ligand_class_name",
  "where": {
    "metal_id": 208
  },
  "limit": 15
}
```

[PHASE ERROR] Tool 'db_distribution' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 6: `inspect_card`
**Args:**
```json
{
  "prefix_id": "metal_208"
}
```

[summary]
## inspect_card — Metal | metal_208

**Name:** Zn^[2+]  
**Symbol:** Zn | **Charge:** 2  
**SMILES:** `[Zn+2]`  
**InChI:** `InChI=1S/Zn/q+2`  
**Flags:** simple-ion  

**Partners:** 1169 ligand(s), 4095 measurement(s) total

| ligand_id | Ligand | # meas |
|-----------|--------|--------|
| ligand_5760 | Aminoacetic acid (Glycine) | 37 |
| ligand_7029 | Ethylenediamine | 36 |
| ligand_10076 | Hydroxide ion | 33 |
| ligand_10090 | Hydrogen cyanide (Hydrocyanic acid) | 30 |
| ligand_7795 | 1,3-Diazole (Imidazole) | 30 |
| … | *(showing top 5 of 1169)* | |

### Functional groups across all ligand partners (1140 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 523 | 46% |
| aromatic_ring | 478 | 42% |
| hydroxyl | 361 | 32% |
| tertiary_amine | 310 | 27% |
| primary_amine | 282 | 25% |
| secondary_amine | 231 | 20% |
| pyridine | 153 | 13% |
| amide | 143 | 13% |
| ether | 132 | 12% |
| phenol | 97 | 9% |
| thioether | 72 | 6% |
| phosphate | 50 | 4% |
| phosphonate | 48 | 4% |
| sulfonate | 43 | 4% |
| ketone | 37 | 3% |
| halide | 31 | 3% |
| thiol | 30 | 3% |
| imine | 28 | 2% |
| ester | 15 | 1% |
| aldehyde | 9 | 1% |
| thiazole | 8 | 1% |
| nitrile | 6 | 1% |
| oxime | 6 | 1% |
| imidazole | 5 | 0% |
| pyrazole | 5 | 0% |

---

### Step 7: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurements",
  "limit": 15,
  "where": "lc.metal_id = 208"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurements'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 8: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "ligand_class_name",
  "where": "metal_id = 208",
  "limit": 15
}
```

[summary]
## db_distribution - ligandmetal_card by ligand_class_name

**total_rows:** 4095

| value | count | pct |
|-------|-------|-----|
| Amino Acids | 654 | 15.97% |
| Inorganic ligands | 285 | 6.96% |
| Aliphatic amines | 253 | 6.18% |
| EDTA and derivatives | 203 | 4.96% |
| Pyrroles (azoles) | 201 | 4.91% |
| Pyridines (azines) | 188 | 4.59% |
| Aliphatic amines secondary N | 180 | 4.4% |
| Aza-macrocycles | 167 | 4.08% |
| NTA and derivatives | 143 | 3.49% |
| Aza-oxa-macrocycles | 126 | 3.08% |
| Carboxylic acids diacids | 122 | 2.98% |
| Aminophosphorus acids | 113 | 2.76% |
| Peptides | 109 | 2.66% |
| Naphtols | 109 | 2.66% |
| Aza macrocycles with carboxylic acids | 106 | 2.59% |

---

### Step 9: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "temperature_c",
  "where": "metal_id = 208",
  "limit": 10
}
```

[TOOL ERROR] db_distribution: Error executing tool db_distribution: no such column: metal_id

---

### Step 10: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "ionic_strength_mol_l",
  "where": "metal_id = 208",
  "limit": 10
}
```

[TOOL ERROR] db_distribution: Error executing tool db_distribution: no such column: metal_id

---

### Step 11: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "constant_type",
  "where": "metal_id = 208",
  "limit": 10
}
```

[TOOL ERROR] db_distribution: Error executing tool db_distribution: no such column: metal_id

---
