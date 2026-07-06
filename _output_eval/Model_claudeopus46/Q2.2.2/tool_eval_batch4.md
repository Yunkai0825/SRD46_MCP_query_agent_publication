# Q2.2.2 — Tool Results (batch 4)

### Step 2: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "ligand_count",
  "limit": 10
}
```

[PHASE ERROR] Tool 'db_ranked_pairs' is not available yet. Complete PHASE 1 first: call search_metals, then call 0_plan_search_strategy.

---

### Step 3: `search_metals`
**Args:**
```json
{
  "name": "%",
  "limit": 5
}
```

[summary]
## search_metals — 5 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_1 | Ac^[3+] | Ac | 3 | ✓ | [Ac+3] | InChI=1S/Ac/q+3 | beta_totN_4 | ligand_totN_9 | vlm_totN_23 |
| metal_2 | Ag^[+] | Ag | 1 | ✓ | [Ag+] | InChI=1S/Ag/q+1 | beta_totN_68 | ligand_totN_649 | vlm_totN_2885 |
| metal_3 | Ag^[2+] | Ag | 2 | ✓ | [Ag+2] | InChI=1S/Ag/q+2 | beta_totN_1 | ligand_totN_5 | vlm_totN_5 |
| metal_4 | Ag^[3+] | Ag | 3 | ✓ | [Ag+3] | InChI=1S/Ag/q+3 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_5 | Al^[3+] | Al | 3 | ✓ | [Al+3] | InChI=1S/Al/q+3 | beta_totN_108 | ligand_totN_187 | vlm_totN_792 |

---

### Step 5: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "ligand_count",
  "limit": 10
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='ligand_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 6: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "ligands_per_metal",
  "limit": 10
}
```

[summary]
## db_ranked_pairs - ligands_per_metal

| metal_id | name | count |
|----------|------|-------|
| metal_68 | H^[+] | 4081 |
| metal_41 | Cu^[2+] | 1951 |
| metal_112 | Ni^[2+] | 1369 |
| metal_208 | Zn^[2+] | 1169 |
| metal_33 | Co^[2+] | 977 |
| metal_26 | Cd^[2+] | 818 |
| metal_2 | Ag^[+] | 649 |
| metal_25 | Ca^[2+] | 644 |
| metal_92 | Mg^[2+] | 508 |
| metal_94 | Mn^[2+] | 486 |

---
