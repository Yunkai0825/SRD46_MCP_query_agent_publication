# Q3.1.1 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "lead",
  "symbol": "Pb",
  "limit": 10
}
```

[summary]
## search_metals — 10 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_16 | Bu_[3]Pb^[+] | B | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_46 | Et_[2]Pb^[2+] | E2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_49 | Et_[3]Pb^[+] | E3Pb | 1 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_84 | Me_[2]Pb^[2+] | M2Pb | 2 |  | *** | *** | beta_totN_5 | ligand_totN_4 | vlm_totN_9 |
| metal_87 | Me_[3]Pb^[+] | M3Pb | 1 |  | *** | *** | beta_totN_7 | ligand_totN_23 | vlm_totN_33 |
| metal_125 | Pb^[2+] | Pb | 2 | ✓ | [Pb+2] | InChI=1S/Pb/q+2 | beta_totN_80 | ligand_totN_470 | vlm_totN_1585 |
| metal_126 | Pb^[4+] | Pb | 4 | ✓ | [Pb+4] | InChI=1S/Pb/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_129 | Ph_[2]Pb^[2+] | Ph2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_130 | Ph_[3]Pb^[+] | Ph3Pb | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_140 | Pr_[2]Pb^[2+] | Pr | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |

---

### Step 4: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND s.constant_type = 'beta' AND s.reaction_type = 'overall' AND c.beta_definition_name LIKE '%a=1%' AND c.beta_definition_name LIKE '%b=0%' AND c.beta_definition_name LIKE '%c=1%' AND c.beta_definition_name NOT LIKE '%OH%' AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 20 AND 30) AND (s.ionic_strength_mol_l BETWEEN 0.05 AND 0.15))",
  "order_by": "s.constant_value DESC",
  "limit": 1000
}
```

[summary]
## search_stability

*(no results)*

---

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND s.constant_type = 'beta' AND s.reaction_type = 'overall' AND c.beta_definition_name LIKE '%a=1%' AND c.beta_definition_name LIKE '%b=0%' AND c.beta_definition_name LIKE '%c=2%' AND c.beta_definition_name NOT LIKE '%OH%' AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 20 AND 30) AND (s.ionic_strength_mol_l BETWEEN 0.05 AND 0.15))",
  "order_by": "s.constant_value DESC",
  "limit": 1000
}
```

[summary]
## search_stability

*(no results)*

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND s.constant_type = 'beta' AND s.reaction_type = 'overall' AND (c.beta_definition_name NOT LIKE '%OH%' AND c.beta_definition_name NOT LIKE '%H2O%' AND c.beta_definition_name NOT LIKE '%CO3%' AND c.beta_definition_name NOT LIKE '%SO4%'))",
  "order_by": "s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 7: `search_citations`
**Args:**
```json
{
  "where": "(la.citation LIKE '%succimer%' OR la.citation LIKE '%DMSA%' OR la.citation LIKE '%CaNa2EDTA%' OR la.citation LIKE '%edetate%' OR la.citation LIKE '%DTPA%' OR la.citation LIKE '%DMPS%' OR la.citation LIKE '%penicillamine%' OR la.citation LIKE '%dimercaprol%' OR la.citation LIKE '%chelation therapy%' OR la.citation LIKE '%lead poisoning%')",
  "limit": 50
}
```

[summary]
## search_citations

*(no results)*

---
