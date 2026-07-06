# Q4.7 — Tool Results (batch 1)

### Step 3: `search_metals`
**Args:**
```json
{
  "name": "cobalt",
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

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "ammonia, ammine, ethylenediamine, diethylenetriamine, triethylenetetramine, tris(2-aminoethyl)amine, tren, cyclam, cyclen, EDTA, ethylenediaminetetraacetic, nitrilotriacetic, NTA, 1,10-phenanthroline",
  "limit": 200
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id IN (metal_33, metal_34) AND (c.ligand_name_SRD LIKE '%ethylenediamine%' OR c.ligand_name_SRD LIKE '%diethylenetriamine%' OR c.ligand_name_SRD LIKE '%triethylenetetramine%' OR c.ligand_name_SRD LIKE '%tris(2-aminoethyl)amine%' OR c.ligand_name_SRD LIKE '%tren%' OR c.ligand_name_SRD LIKE '%cyclam%' OR c.ligand_name_SRD LIKE '%cyclen%' OR c.ligand_name_SRD LIKE '%ethylenediaminetetraacetic%' OR c.ligand_name_SRD LIKE '%nitrilotriacetic%' OR c.ligand_name_SRD LIKE '%ammonia%' OR c.ligand_name_SRD LIKE '%ammine%' OR c.ligand_name_SRD LIKE '%1,10-phenanthroline%') AND (s.solvent_name LIKE '%water%') AND (s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.ligand_name_SRD ASC, c.beta_definition_name ASC, c.metal_id ASC, s.constant_type ASC, s.constant_value DESC",
  "limit": 400
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---
