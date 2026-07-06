# Qfree_20260423_200125 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "iron"
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 4: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligandmetal_card"
}
```

[summary]
## get_table_schema - 17 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | card_id | INTEGER | False | True |
| 1 | complex_system_id | INTEGER | True | False |
| 2 | metal_id | INTEGER | True | False |
| 3 | ligand_id | INTEGER | True | False |
| 4 | beta_definition_id | INTEGER | True | False |
| 5 | complex_id | TEXT | False | False |
| 6 | ligand_class_id | INTEGER | False | False |
| 7 | ligand_class_name | TEXT | False | False |
| 8 | metal_name_SRD | TEXT | False | False |
| 9 | metal_SMILES | TEXT | False | False |
| 10 | metal_InChi | TEXT | False | False |
| 11 | ligand_name_SRD | TEXT | False | False |
| 12 | ligand_SMILES | TEXT | False | False |
| 13 | ligand_InChi | TEXT | False | False |
| 14 | ligand_HxL_definition_SRD | TEXT | False | False |
| 15 | beta_definition_name | TEXT | False | False |
| 16 | created_at | TIMESTAMP | False | False |

---

### Step 5: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligandmetal_stability_measured"
}
```

[summary]
## get_table_schema - 25 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | stability_id | INTEGER | False | True |
| 1 | card_id | INTEGER | True | False |
| 2 | constant_type | TEXT | False | False |
| 3 | constant_value | REAL | False | False |
| 4 | temperature_c | REAL | False | False |
| 5 | ionic_strength_mol_l | REAL | False | False |
| 6 | solvent_id | INTEGER | False | False |
| 7 | solvent_name | TEXT | False | False |
| 8 | electrolyte_composition | TEXT | False | False |
| 9 | equation_python | TEXT | False | False |
| 10 | raw_definition | TEXT | False | False |
| 11 | normalized_definition | TEXT | False | False |
| 12 | equation_str | TEXT | False | False |
| 13 | equation_tree_json | TEXT | False | False |
| 14 | equation_sides_json | TEXT | False | False |
| 15 | LHS_species_json | TEXT | False | False |
| 16 | RHS_species_json | TEXT | False | False |
| 17 | HxL_involved_json | TEXT | False | False |
| 18 | presence_flags_json | TEXT | False | False |
| 19 | reaction_type | TEXT | False | False |
| 20 | element_conserved | INTEGER | False | False |
| 21 | citations_json | TEXT | False | False |
| 22 | audit_timestamp | TEXT | False | False |
| 23 | error | TEXT | False | False |
| 24 | notes | TEXT | False | False |

---

### Step 6: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c3.ligand_id, c3.ligand_name_SRD, c3.beta_definition_name AS fe3_beta_def, s3.constant_type AS fe3_const_type, s3.constant_value AS fe3_logK, s3.temperature_c AS fe3_temp, s3.ionic_strength_mol_l AS fe3_ionic, c2.beta_definition_name AS fe2_beta_def, s2.constant_type AS fe2_const_type, s2.constant_value AS fe2_logK, s2.temperature_c AS fe2_temp, s2.ionic_strength_mol_l AS fe2_ionic, (s3.constant_value - s2.constant_value) AS delta_logK FROM ligandmetal_card AS c3 JOIN ligandmetal_stability_measured AS s3 ON c3.card_id = s3.card_id JOIN ligandmetal_card AS c2 ON c3.ligand_id = c2.ligand_id JOIN ligandmetal_stability_measured AS s2 ON c2.card_id = s2.card_id WHERE c3.metal_id = 61 AND c2.metal_id = 62 AND s3.constant_type = 'logK' AND s2.constant_type = 'logK' AND c3.beta_definition_name LIKE '%1:1%' AND c2.beta_definition_name LIKE '%1:1%' AND s3.temperature_c BETWEEN 20 AND 30 AND s2.temperature_c BETWEEN 20 AND 30 ORDER BY delta_logK DESC LIMIT 80",
  "task_description": "Find ligands with both Fe(III) and Fe(II) 1:1 logK data to compare selectivity for Fe3+ over Fe2+",
  "column_legend": {
    "ligand_id": "ligand_id from ligandmetal_card, identifies the ligand",
    "ligand_name_SRD": "SRD ligand name",
    "fe3_beta_def": "beta definition name for Fe(III) complex",
    "fe3_const_type": "constant type for Fe(III), should be logK",
    "fe3_logK": "log stability constant for Fe(III) 1:1 complex",
    "fe3_temp": "temperature in °C for Fe(III) measurement",
    "fe3_ionic": "ionic strength in mol/L for Fe(III) measurement",
    "fe2_beta_def": "beta definition name for Fe(II) complex",
    "fe2_const_type": "constant type for Fe(II), should be logK",
    "fe2_logK": "log stability constant for Fe(II) 1:1 complex",
    "fe2_temp": "temperature in °C for Fe(II) measurement",
    "fe2_ionic": "ionic strength in mol/L for Fe(II) measurement",
    "delta_logK": "fe3_logK - fe2_logK, higher means more selective for Fe(III)"
  }
}
```

[summary]
## execute_srd46_sql — REJECTED

**Error:** execute_srd46_sql `column_legend` entries must each be a non-empty string of at least 20 characters. Too-short / non-string entries: ['ligand_name_SRD']. Each entry must cover (1) source table.column or formula, (2) filter/join (metal_id, beta_definition_name, constant_type, T/I window, pKa bracket), (3) physical meaning + units + species or protonation state, and (4) for computed cols, formula AND interpretation (sign convention, what 'positive' means).

---

### Step 7: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c3.ligand_id, c3.ligand_name_SRD, c3.beta_definition_name AS fe3_beta_def, s3.constant_type AS fe3_const_type, s3.constant_value AS fe3_logK, s3.temperature_c AS fe3_temp, s3.ionic_strength_mol_l AS fe3_ionic, c2.beta_definition_name AS fe2_beta_def, s2.constant_type AS fe2_const_type, s2.constant_value AS fe2_logK, s2.temperature_c AS fe2_temp, s2.ionic_strength_mol_l AS fe2_ionic, (s3.constant_value - s2.constant_value) AS delta_logK FROM ligandmetal_card AS c3 JOIN ligandmetal_stability_measured AS s3 ON c3.card_id = s3.card_id JOIN ligandmetal_card AS c2 ON c3.ligand_id = c2.ligand_id JOIN ligandmetal_stability_measured AS s2 ON c2.card_id = s2.card_id WHERE c3.metal_id = 61 AND c2.metal_id = 62 AND s3.constant_type = 'logK' AND s2.constant_type = 'logK' AND c3.beta_definition_name LIKE '%1:1%' AND c2.beta_definition_name LIKE '%1:1%' AND s3.temperature_c BETWEEN 20 AND 30 AND s2.temperature_c BETWEEN 20 AND 30 ORDER BY delta_logK DESC LIMIT 80",
  "task_description": "Find ligands with both Fe(III) and Fe(II) 1:1 logK data to compare selectivity for Fe3+ over Fe2+",
  "column_legend": {
    "ligand_id": "c3.ligand_id — ligand entity identifier from ligandmetal_card table, used to join Fe(III) and Fe(II) systems",
    "ligand_name_SRD": "c3.ligand_name_SRD — standard SRD name of the ligand from ligandmetal_card, identifies the chemical species",
    "fe3_beta_def": "c3.beta_definition_name — beta definition name for the Fe(III) complex, filtered to contain '1:1' stoichiometry",
    "fe3_const_type": "s3.constant_type — type of stability constant for Fe(III), filtered to 'logK' (log formation constant)",
    "fe3_logK": "s3.constant_value — log stability constant value for Fe(III) 1:1 complex, dimensionless, higher = stronger binding",
    "fe3_temp": "s3.temperature_c — measurement temperature in degrees Celsius for Fe(III) data, filtered 20-30°C",
    "fe3_ionic": "s3.ionic_strength_mol_l — ionic strength in mol/L for Fe(III) measurement conditions",
    "fe2_beta_def": "c2.beta_definition_name — beta definition name for the Fe(II) complex, filtered to contain '1:1' stoichiometry",
    "fe2_const_type": "s2.constant_type — type of stability constant for Fe(II), filtered to 'logK' (log formation constant)",
    "fe2_logK": "s2.constant_value — log stability constant value for Fe(II) 1:1 complex, dimensionless, higher = stronger binding",
    "fe2_temp": "s2.temperature_c — measurement temperature in degrees Celsius for Fe(II) data, filtered 20-30°C",
    "fe2_ionic": "s2.ionic_strength_mol_l — ionic strength in mol/L for Fe(II) measurement conditions",
    "delta_logK": "fe3_logK minus fe2_logK — selectivity metric: positive means ligand prefers Fe(III) over Fe(II), larger = more selective"
  }
}
```

[summary]
## execute_srd46_sql — 0 row(s)

<tool_context>
**Task (agent-stated intent):**

> Find ligands with both Fe(III) and Fe(II) 1:1 logK data to compare selectivity for Fe3+ over Fe2+

**Column legend (agent-stated chemistry origin of each column):**

| column | meaning / source table+filter / species or (T, I) |
|--------|----------------------------------------------------|
| `ligand_id` | c3.ligand_id — ligand entity identifier from ligandmetal_card table, used to join Fe(III) and Fe(II) systems |
| `ligand_name_SRD` | c3.ligand_name_SRD — standard SRD name of the ligand from ligandmetal_card, identifies the chemical species |
| `fe3_beta_def` | c3.beta_definition_name — beta definition name for the Fe(III) complex, filtered to contain '1:1' stoichiometry |
| `fe3_const_type` | s3.constant_type — type of stability constant for Fe(III), filtered to 'logK' (log formation constant) |
| `fe3_logK` | s3.constant_value — log stability constant value for Fe(III) 1:1 complex, dimensionless, higher = stronger binding |
| `fe3_temp` | s3.temperature_c — measurement temperature in degrees Celsius for Fe(III) data, filtered 20-30°C |
| `fe3_ionic` | s3.ionic_strength_mol_l — ionic strength in mol/L for Fe(III) measurement conditions |
| `fe2_beta_def` | c2.beta_definition_name — beta definition name for the Fe(II) complex, filtered to contain '1:1' stoichiometry |
| `fe2_const_type` | s2.constant_type — type of stability constant for Fe(II), filtered to 'logK' (log formation constant) |
| `fe2_logK` | s2.constant_value — log stability constant value for Fe(II) 1:1 complex, dimensionless, higher = stronger binding |
| `fe2_temp` | s2.temperature_c — measurement temperature in degrees Celsius for Fe(II) data, filtered 20-30°C |
| `fe2_ionic` | s2.ionic_strength_mol_l — ionic strength in mol/L for Fe(II) measurement conditions |
| `delta_logK` | fe3_logK minus fe2_logK — selectivity metric: positive means ligand prefers Fe(III) over Fe(II), larger = more selective |
| `ligand_id` *(not in result)* | c3.ligand_id — ligand entity identifier from ligandmetal_card table, used to join Fe(III) and Fe(II) systems |
| `ligand_name_SRD` *(not in result)* | c3.ligand_name_SRD — standard SRD name of the ligand from ligandmetal_card, identifies the chemical species |
| `fe3_beta_def` *(not in result)* | c3.beta_definition_name — beta definition name for the Fe(III) complex, filtered to contain '1:1' stoichiometry |
| `fe3_const_type` *(not in result)* | s3.constant_type — type of stability constant for Fe(III), filtered to 'logK' (log formation constant) |
| `fe3_logK` *(not in result)* | s3.constant_value — log stability constant value for Fe(III) 1:1 complex, dimensionless, higher = stronger binding |
| `fe3_temp` *(not in result)* | s3.temperature_c — measurement temperature in degrees Celsius for Fe(III) data, filtered 20-30°C |
| `fe3_ionic` *(not in result)* | s3.ionic_strength_mol_l — ionic strength in mol/L for Fe(III) measurement conditions |
| `fe2_beta_def` *(not in result)* | c2.beta_definition_name — beta definition name for the Fe(II) complex, filtered to contain '1:1' stoichiometry |
| `fe2_const_type` *(not in result)* | s2.constant_type — type of stability constant for Fe(II), filtered to 'logK' (log formation constant) |
| `fe2_logK` *(not in result)* | s2.constant_value — log stability constant value for Fe(II) 1:1 complex, dimensionless, higher = stronger binding |
| `fe2_temp` *(not in result)* | s2.temperature_c — measurement temperature in degrees Celsius for Fe(II) data, filtered 20-30°C |
| `fe2_ionic` *(not in result)* | s2.ionic_strength_mol_l — ionic strength in mol/L for Fe(II) measurement conditions |
| `delta_logK` *(not in result)* | fe3_logK minus fe2_logK — selectivity metric: positive means ligand prefers Fe(III) over Fe(II), larger = more selective |

**SQL executed (post AST-rewrite):**

```sql
SELECT c3.ligand_id, c3.ligand_name_SRD, c3.beta_definition_name AS fe3_beta_def, s3.constant_type AS fe3_const_type, s3.constant_value AS fe3_logK, s3.temperature_c AS fe3_temp, s3.ionic_strength_mol_l AS fe3_ionic, c2.beta_definition_name AS fe2_beta_def, s2.constant_type AS fe2_const_type, s2.constant_value AS fe2_logK, s2.temperature_c AS fe2_temp, s2.ionic_strength_mol_l AS fe2_ionic, (s3.constant_value - s2.constant_value) AS delta_logK FROM ligandmetal_card AS c3 JOIN ligandmetal_stability_measured AS s3 ON c3.card_id = s3.card_id JOIN ligandmetal_card AS c2 ON c3.ligand_id = c2.ligand_id JOIN ligandmetal_stability_measured AS s2 ON c2.card_id = s2.card_id WHERE c3.metal_id = 61 AND c2.metal_id = 62 AND s3.constant_type = 'logK' AND s2.constant_type = 'logK' AND c3.beta_definition_name LIKE '%1:1%' AND c2.beta_definition_name LIKE '%1:1%' AND s3.temperature_c BETWEEN 20 AND 30 AND s2.temperature_c BETWEEN 20 AND 30 ORDER BY delta_logK DESC LIMIT 80
```
</tool_context>

*(0 rows returned)*

---

### Step 8: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "constant_type",
  "limit": 20
}
```

[summary]
## db_distribution - ligandmetal_stability_measured by constant_type

**total_rows:** 79063

| value | count | pct |
|-------|-------|-----|
| K | 60540 | 76.57% |
| H | 9693 | 12.26% |
| S | 8830 | 11.17% |

---

### Step 9: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "beta_definition_name",
  "where": "metal_id = 61",
  "limit": 30
}
```

[summary]
## db_distribution - ligandmetal_card by beta_definition_name

**total_rows:** 1473

| value | count | pct |
|-------|-------|-----|
| [ML]/[M][L] | 487 | 33.06% |
| [ML<sub>2</sub>]/[M][L]<sup>2</sup> | 100 | 6.79% |
| [MHL]/[ML][H] | 85 | 5.77% |
| [ML][H]/[M][HL] | 72 | 4.89% |
| [ML]/[M(OH)L][H] | 68 | 4.62% |
| [MHL]/[M][HL] | 68 | 4.62% |
| [ML<sub>3</sub>]/[M][L]<sup>3</sup> | 65 | 4.41% |
| [ML][H]<sup>2</sup>/[M][H<sub>2</sub>L] | 28 | 1.9% |
| [MH<sub>2</sub>L]/[MHL][H] | 28 | 1.9% |
| [M(OH)L]/[M(OH)<sub>2</sub>L][H] | 24 | 1.63% |
| [ML][H]<sup>3</sup>/[M][H<sub>3</sub>L] | 23 | 1.56% |
| [M<sub>3</sub>(OH)<sub>2</sub>L<sub>6</sub>][H]<sup>2</sup>/[M]<sup>3</sup>[L]<… | 23 | 1.56% |
| [ML<sub>2</sub>][H]/[ML][HL] | 20 | 1.36% |
| [MH<sub>3</sub>L]/[MH<sub>2</sub>L][H] | 20 | 1.36% |
| [MHL<sub>2</sub>]/[ML<sub>2</sub>][H] | 19 | 1.29% |
| [ML<sub>2</sub>][H]<sup>2</sup>/[ML][H<sub>2</sub>L] | 18 | 1.22% |
| [ML<sub>3</sub>][H]<sup>2</sup>/[ML<sub>2</sub>][H<sub>2</sub>L] | 14 | 0.95% |
| [ML<sub>3</sub>][H]/[ML<sub>2</sub>][HL] | 13 | 0.88% |
| [M(HL)<sub>2</sub>]/[M][HL]<sup>2</sup> | 13 | 0.88% |
| [M<sub>2</sub>(OH)<sub>2</sub>L<sub>2</sub>]/[M(OH)L]<sup>2</sup> | 11 | 0.75% |
| [MH<sub>2</sub>L]/[M][H<sub>2</sub>L] | 10 | 0.68% |
| [M<sub>2</sub>L<sub>2</sub>]/[M]<sup>2</sup>[L]<sup>2</sup> | 10 | 0.68% |
| [M(OH)L]/[ML][OH] | 9 | 0.61% |
| [ML<sub>2</sub>]/[M(OH)L<sub>2</sub>][H] | 8 | 0.54% |
| [MHL<sub>3</sub>]/[ML<sub>3</sub>][H] | 8 | 0.54% |
| [M(OH)<sub>2</sub>L]/[M(OH)L][OH] | 8 | 0.54% |
| [ML<sub>3</sub>]/[M(OH)L<sub>3</sub>][H] | 7 | 0.48% |
| [MHL][H]/[M][H<sub>2</sub>L] | 7 | 0.48% |
| [MH<sub>4</sub>L]/[MH<sub>3</sub>L][H] | 7 | 0.48% |
| [MH<sub>2</sub>L]/[ML][H]<sup>2</sup> | 7 | 0.48% |

---

### Step 10: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c3.ligand_id, c3.ligand_name_SRD, c3.ligand_class_name, c3.beta_definition_name AS fe3_beta_def, s3.constant_value AS fe3_logK, s3.temperature_c AS fe3_temp, s3.ionic_strength_mol_l AS fe3_ionic, c2.beta_definition_name AS fe2_beta_def, s2.constant_value AS fe2_logK, s2.temperature_c AS fe2_temp, s2.ionic_strength_mol_l AS fe2_ionic, (s3.constant_value - s2.constant_value) AS delta_logK FROM ligandmetal_card AS c3 JOIN ligandmetal_stability_measured AS s3 ON c3.card_id = s3.card_id JOIN ligandmetal_card AS c2 ON c3.ligand_id = c2.ligand_id JOIN ligandmetal_stability_measured AS s2 ON c2.card_id = s2.card_id WHERE c3.metal_id = 61 AND c2.metal_id = 62 AND s3.constant_type = 'K' AND s2.constant_type = 'K' AND c3.beta_definition_name = '[ML]/[M][L]' AND c2.beta_definition_name = '[ML]/[M][L]' AND s3.temperature_c BETWEEN 20 AND 30 AND s2.temperature_c BETWEEN 20 AND 30 ORDER BY delta_logK DESC LIMIT 100",
  "task_description": "Find ligands with both Fe(III) and Fe(II) 1:1 logK data using correct column values to compare selectivity",
  "column_legend": {
    "ligand_id": "c3.ligand_id from ligandmetal_card — unique ligand identifier, joined between Fe(III) and Fe(II) card tables",
    "ligand_name_SRD": "c3.ligand_name_SRD from ligandmetal_card — standard reference name of the ligand chemical species",
    "ligand_class_name": "c3.ligand_class_name from ligandmetal_card — classification category of the ligand (e.g. amino acid, carboxylic acid)",
    "fe3_beta_def": "c3.beta_definition_name for Fe(III) — equilibrium expression, filtered to [ML]/[M][L] meaning 1:1 metal-ligand complex",
    "fe3_logK": "s3.constant_value from stability_measured for Fe(III) — log10 of formation constant K for ML complex, dimensionless",
    "fe3_temp": "s3.temperature_c from stability_measured for Fe(III) — measurement temperature in degrees Celsius, filtered 20-30°C",
    "fe3_ionic": "s3.ionic_strength_mol_l from stability_measured for Fe(III) — ionic strength of solution in mol/L",
    "fe2_beta_def": "c2.beta_definition_name for Fe(II) — equilibrium expression, filtered to [ML]/[M][L] meaning 1:1 metal-ligand complex",
    "fe2_logK": "s2.constant_value from stability_measured for Fe(II) — log10 of formation constant K for ML complex, dimensionless",
    "fe2_temp": "s2.temperature_c from stability_measured for Fe(II) — measurement temperature in degrees Celsius, filtered 20-30°C",
    "fe2_ionic": "s2.ionic_strength_mol_l from stability_measured for Fe(II) — ionic strength of solution in mol/L",
    "delta_logK": "s3.constant_value minus s2.constant_value — selectivity metric: positive = ligand prefers Fe(III), larger = more selective for Fe3+ over Fe2+"
  }
}
```

[summary]
## execute_srd46_sql — 50 row(s)

<tool_context>
**Task (agent-stated intent):**

> Find ligands with both Fe(III) and Fe(II) 1:1 logK data using correct column values to compare selectivity

**Column legend (agent-stated chemistry origin of each column):**

| column | meaning / source table+filter / species or (T, I) |
|--------|----------------------------------------------------|
| `ligand_id` | c3.ligand_id from ligandmetal_card — unique ligand identifier, joined between Fe(III) and Fe(II) card tables |
| `ligand_name_SRD` | c3.ligand_name_SRD from ligandmetal_card — standard reference name of the ligand chemical species |
| `ligand_class_name` | c3.ligand_class_name from ligandmetal_card — classification category of the ligand (e.g. amino acid, carboxylic acid) |
| `fe3_beta_def` | c3.beta_definition_name for Fe(III) — equilibrium expression, filtered to [ML]/[M][L] meaning 1:1 metal-ligand complex |
| `fe3_logK` | s3.constant_value from stability_measured for Fe(III) — log10 of formation constant K for ML complex, dimensionless |
| `fe3_temp` | s3.temperature_c from stability_measured for Fe(III) — measurement temperature in degrees Celsius, filtered 20-30°C |
| `fe3_ionic` | s3.ionic_strength_mol_l from stability_measured for Fe(III) — ionic strength of solution in mol/L |
| `fe2_beta_def` | c2.beta_definition_name for Fe(II) — equilibrium expression, filtered to [ML]/[M][L] meaning 1:1 metal-ligand complex |
| `fe2_logK` | s2.constant_value from stability_measured for Fe(II) — log10 of formation constant K for ML complex, dimensionless |
| `fe2_temp` | s2.temperature_c from stability_measured for Fe(II) — measurement temperature in degrees Celsius, filtered 20-30°C |
| `fe2_ionic` | s2.ionic_strength_mol_l from stability_measured for Fe(II) — ionic strength of solution in mol/L |
| `delta_logK` | s3.constant_value minus s2.constant_value — selectivity metric: positive = ligand prefers Fe(III), larger = more selective for Fe3+ over Fe2+ |

**Auto-enriched entities (filling in fields missing from the SELECT):**

*ligand_id → ligand_card (+ ligand_pka_bracket)*

| ligand_id | definition_HxL | ligand_SMILES | pka_brackets |
|-----------|----------------|---------------|--------------|
| ligand_6288 | H4L | C[C@H]([C@H](C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | (-inf, H4L, -1.8, H3L, 2.5, H2L, 6.27, HL, 6.27, L, +inf) |
| ligand_7673 | H2L | Cc1cc2c(O)c(c1)CNCc1cccc(n1)CNCc1cc(C)cc(c1O)CNCc1cccc(n1)CNC2 | (-inf, H6L, 4.52, H5L, 6.65, H4L, 8.92, H3L, 9.18, H2L, 9.18, HL, -11.3, L, +in… |
| ligand_9058 | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | (-inf, H3L, 2.9, H2L, 4.35, HL, 5.65, L, +inf) |
| ligand_6109 | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCCN(CC(=O)O)CC1 | (-inf, H4L, 3.27, H3L, 4.11, H2L, 10.13, HL, 10.75, L, +inf) |
| ligand_5843 | HL | NC(=O)C[C@H](N)C(=O)O | (-inf, H2L, 2.16, HL, 8.73, L, +inf) |
| ligand_8191 | L | c1cnc2c(c1)ccc1cccnc12 | (-inf, H2L, -1.8, HL, 4.92, L, +inf) |
| ligand_6356 | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | (-inf, H8L, -0.1, H7L, -0.1, H6L, -0.7, H5L, 2, H4L, 2.7, H3L, 4.28, H2L, 4.28,… |
| ligand_6301 | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | (-inf, H4L, 2.4, H3L, 3.49, H2L, 6.07, HL, 6.07, L, +inf) |
| ligand_6292 | H4L | CC(C(=O)O)N(CCN(CC(=O)O)C(C)C(=O)O)CC(=O)O | (-inf, H4L, -1.9, H3L, 2, H2L, 6.65, HL, 10.42, L, +inf) |
| ligand_6366 | H6L | O=C(O)CN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | (-inf, H8L, -1.5, H7L, -1.5, H6L, 2.3, H5L, 2.76, H4L, 4.08, H3L, 6.14, H2L, 9.… |
| ligand_6287 | H4L | CC(C(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | (-inf, H4L, 2.4, H3L, 3.49, H2L, 6.07, HL, 6.07, L, +inf) |
| ligand_6277 | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | (-inf, H5L, -1.5, H4L, 2, H3L, 2.69, H2L, 6.13, HL, 9.52, L, +inf) |
| ligand_8434 | H4L | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | (-inf, H3L, 3.14, H2L, 4.67, HL, 9.12, L, +inf) |
| ligand_6278 | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | (-inf, H4L, -1.8, H3L, 2.79, H2L, 6.24, HL, 10.85, L, +inf) |
| ligand_6335 | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | (-inf, H4L, -1.8, H3L, 2.76, H2L, 8.75, HL, 9.39, L, +inf) |
| ligand_6084 | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CC1 | (-inf, H4L, 2.7, H3L, 4.03, H2L, 7.73, HL, 7.73, L, +inf) |
| ligand_6104 | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | (-inf, H4L, 3.27, H3L, 4.3, H2L, 9.8, HL, 9.8, L, +inf) |
| ligand_8360 | H4L | NC(c1ccccc1)(P(=O)(O)O)P(=O)(O)O | (-inf, H4L, -1.6, H3L, 5.29, H2L, 8.17, HL, 10.29, L, +inf) |
| ligand_6102 | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | (-inf, H4L, 4.23, H3L, 4.47, H2L, 9.69, HL, 9.69, L, +inf) |
| ligand_5937 | H3L | O=C(O)CNCP(=O)(O)O | (-inf, H4L, -0.5, H3L, 2.2, H2L, 5.45, HL, 10.1, L, +inf) |
| ligand_6348 | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | (-inf, H4L, 2, H3L, 2.68, H2L, 8.37, HL, 9.31, L, +inf) |
| ligand_6342 | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | (-inf, H4L, -1.9, H3L, 2.7, H2L, 8.71, HL, 9.32, L, +inf) |
| ligand_5804 | H2L | N[C@@H](CCC(=O)O)C(=O)O | (-inf, H3L, 2.16, H2L, 4.15, HL, 9.58, L, +inf) |
| ligand_6310 | H4L | O=C(O)CCN(CCC(=O)O)CCN(CCC(=O)O)CCC(=O)O | (-inf, H6L, -1.5, H5L, 2.94, H4L, 3.35, H3L, 4.23, H2L, 6.19, HL, 9.74, L, +inf) |
| ligand_6333 | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | (-inf, H4L, -1.7, H3L, 2.57, H2L, 6.95, HL, 9.49, L, +inf) |

**SQL executed (post AST-rewrite):**

```sql
SELECT c3.ligand_id, c3.ligand_name_SRD, c3.ligand_class_name, c3.beta_definition_name AS fe3_beta_def, s3.constant_value AS fe3_logK, s3.temperature_c AS fe3_temp, s3.ionic_strength_mol_l AS fe3_ionic, c2.beta_definition_name AS fe2_beta_def, s2.constant_value AS fe2_logK, s2.temperature_c AS fe2_temp, s2.ionic_strength_mol_l AS fe2_ionic, (s3.constant_value - s2.constant_value) AS delta_logK FROM ligandmetal_card AS c3 JOIN ligandmetal_stability_measured AS s3 ON c3.card_id = s3.card_id JOIN ligandmetal_card AS c2 ON c3.ligand_id = c2.ligand_id JOIN ligandmetal_stability_measured AS s2 ON c2.card_id = s2.card_id WHERE c3.metal_id = 61 AND c2.metal_id = 62 AND s3.constant_type = 'K' AND s2.constant_type = 'K' AND c3.beta_definition_name = '[ML]/[M][L]' AND c2.beta_definition_name = '[ML]/[M][L]' AND s3.temperature_c BETWEEN 20 AND 30 AND s2.temperature_c BETWEEN 20 AND 30 ORDER BY delta_logK DESC LIMIT 100
```
</tool_context>

**Shared across all 50 rows:**

- `fe3_beta_def` = [ML]/[M][L]
- `fe2_beta_def` = [ML]/[M][L]

| ligand_id | ligand_name_SRD | ligand_class_name | fe3_logK | fe3_temp | fe3_ionic | fe2_logK | fe2_temp | fe2_ionic | delta_logK |
|-----------|-----------------|-------------------|----------|----------|-----------|----------|----------|-----------|------------|
| ligand_6288 | meso-(1,2-Dimethylethylene)dinitrilotetraacetic acid | EDTA and derivatives | 25.65 | 25.0 | 0.1 | -15.11 | 20.0 | 0.1 | 40.76 |
| ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-dihydroxy-5,13(5)-dimethyl-1,9(2,6)-dipyridina-5,13(… | Aza-macrocycles | 32.0 | 25.0 | 0.1 | 15.3 | 25.0 | 0.1 | 16.7 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | Carboxylic acids polyacids | 11.27 | 25.0 | 0.1 | -4.8 | 25.0 | 0.1 | 16.07 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | Carboxylic acids polyacids | 11.19 | 25.0 | 0.1 | -4.8 | 25.0 | 0.1 | 15.989999999999998 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | Carboxylic acids polyacids | 10.25 | 25.0 | 1.0 | -4.8 | 25.0 | 0.1 | 15.05 |
| ligand_6109 | 1,4,8,11-Tetraazacyclotetradecane-N,N',N'',N'''-tetraacetic acid (TETA) | Aza macrocycles with carboxylic acids | 26.46 | 25.0 | 0.1 | 13.32 | 25.0 | 0.1 | 13.14 |
| ligand_5843 | L-2-Aminobutanedioic acid 4-amide (Asparagine) | Amino Acids | 8.6 | 20.0 | 1.0 | -4.37 | 25.0 | 3.0 | 12.969999999999999 |
| ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) | Phenanthrolines | 6.5 | 20.0 | 0.1 | -5.87 | 25.0 | 0.0 | 12.370000000000001 |
| ligand_5843 | L-2-Aminobutanedioic acid 4-amide (Asparagine) | Amino Acids | 8.6 | 20.0 | 1.0 | -3.4 | 20.0 | 1.0 | 12.0 |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | EDTA and derivatives | 28.0 | 25.0 | 0.1 | 16.2 | 25.0 | 0.1 | 11.8 |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | EDTA and derivatives | 27.8 | 20.0 | 0.1 | 16.2 | 25.0 | 0.1 | 11.600000000000001 |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | EDTA and derivatives | 27.6 | 20.0 | 0.1 | 16.2 | 25.0 | 0.1 | 11.400000000000002 |
| ligand_6301 | trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA) | EDTA and derivatives | 30.1 | 20.0 | 0.1 | 18.9 | 25.0 | 0.1 | 11.200000000000003 |
| ligand_6292 | DL-Ethylenedinitrilo-N,N'-di(2-propanoic)-N,N'-diacetic acid | EDTA and derivatives | 25.28 | 20.0 | 0.1 | 14.18 | 20.0 | 0.1 | 11.100000000000001 |
| ligand_6301 | trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA) | EDTA and derivatives | 30.0 | 25.0 | 0.1 | 18.9 | 25.0 | 0.1 | 11.100000000000001 |
| ligand_6366 | Triethylenetetranitrilohexaacetic acid (TTHA) | EDTA and derivatives | 26.8 | 25.0 | 0.1 | 15.8 | 25.0 | 0.1 | 11.0 |
| ligand_6287 | rac-(1,2-Dimethylethylene)dinitrilotetraacetic acid | EDTA and derivatives | 28.05 | 25.0 | 0.1 | 17.08 | 25.0 | 0.1 | 10.970000000000002 |
| ligand_6287 | rac-(1,2-Dimethylethylene)dinitrilotetraacetic acid | EDTA and derivatives | 28.05 | 25.0 | 0.1 | 17.18 | 20.0 | 0.1 | 10.870000000000001 |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | EDTA and derivatives | 25.1 | 25.0 | 0.1 | 14.3 | 25.0 | 0.1 | 10.8 |
| ligand_8434 | Pyridine-2,6-diphosphonic acid (2,6-PDPA) | Aminophosphorus acids | 20.87 | 25.0 | 0.1 | 10.12 | 25.0 | 0.1 | 10.750000000000002 |
| ligand_6278 | DL-(Methylethylene)dinitrilotetraacetic acid (PDTA) | EDTA and derivatives | 26.0 | 25.0 | 0.1 | 15.5 | 25.0 | 0.1 | 10.5 |
| ligand_6335 | Oxybis(ethylenenitrilo)tetraacetic acid (EEDTA) | EDTA and derivatives | 24.7 | 20.0 | 0.1 | 14.2 | 25.0 | 0.1 | 10.5 |
| ligand_6288 | meso-(1,2-Dimethylethylene)dinitrilotetraacetic acid | EDTA and derivatives | 25.65 | 25.0 | 0.1 | 15.33 | 25.0 | 0.1 | 10.319999999999999 |
| ligand_6084 | 1-Oxa-4,7,10-triazacyclododecane-4,7,10-triacetic acid | Aza macrocycles with carboxylic acids | 26.8 | 25.0 | 0.1 | 16.55 | 25.0 | 0.1 | 10.25 |
| ligand_6104 | 1,4,7,10-Tetraazacyclotridecane-N,N',N'',N'''-tetraacetic acid (TRITA) | Aza macrocycles with carboxylic acids | 27.5 | 25.0 | 0.1 | 17.6 | 25.0 | 0.1 | 9.899999999999999 |
| ligand_8360 | Amino(phenyl)methylenediphosphonic acid | Aminophosphorus acids | 20.15 | 25.0 | 0.1 | 10.4 | 25.0 | 0.1 | 9.749999999999998 |
| ligand_6102 | 1,4,7,10-Tetraazacyclododecane-N,N',N'',N'''-tetraacetic acid (DOTA) | Aza macrocycles with carboxylic acids | 29.4 | 25.0 | 0.1 | 19.8 | 25.0 | 0.1 | 9.599999999999998 |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | EDTA and derivatives | 23.8 | 25.0 | 1.0 | 14.3 | 25.0 | 0.1 | 9.5 |
| ligand_5937 | N-(Phosphonomethyl)glycine (Glyphosate) | Amino Acids | 16.09 | 25.0 | 0.1 | 6.87 | 25.0 | 0.1 | 9.219999999999999 |
| ligand_6348 | Thiobis(ethylenenitrilo)tetraacetic acid (TEDTA) | EDTA and derivatives | 20.41 | 20.0 | 0.1 | 11.57 | 20.0 | 0.1 | 8.84 |
| ligand_6342 | Ethylenebis(oxyethylenenitrilo)tetraacetic acid (EGTA) | EDTA and derivatives | 20.5 | 25.0 | 0.1 | 11.8 | 25.0 | 0.1 | 8.7 |
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | Amino Acids | 12.1 | 20.0 | 1.0 | 3.52 | 20.0 | 1.0 | 8.58 |
| ligand_6310 | Ethylenedinitrilotetra(3-propanoic acid) (EDTP) | EDTA and derivatives | 14.4 | 30.0 | 0.1 | 6.2 | 30.0 | 0.1 | 8.2 |
| ligand_6333 | (2-Hydroxytrimethylene)dinitrilotetraacetic acid | EDTA and derivatives | 20.1 | 20.0 | 0.1 | 11.91 | 20.0 | 0.1 | 8.190000000000001 |
| ligand_6311 | Trimethylenedinitrilotetraacetic acid (TMDTA) | EDTA and derivatives | 21.61 | 20.0 | 0.1 | 13.42 | 20.0 | 0.1 | 8.19 |
| ligand_6135 | L-2-(Carboxymethyl)iminodiacetic acid | Iminodiacetic acid and derivatives | 15.7 | 25.0 | 0.1 | 7.66 | 25.0 | 0.1 | 8.04 |
| ligand_6311 | Trimethylenedinitrilotetraacetic acid (TMDTA) | EDTA and derivatives | 21.4 | 20.0 | 0.1 | 13.42 | 20.0 | 0.1 | 7.979999999999999 |
| ligand_6165 | Nitrilotriacetic acid (NTA) | NTA and derivatives | 15.9 | 25.0 | 0.1 | 8.05 | 25.0 | 1.0 | 7.85 |
| ligand_10076 | Hydroxide ion | Inorganic ligands | 11.81 | 25.0 | 0.0 | 4.2 | 25.0 | 0.1 | 7.61 |
| ligand_10076 | Hydroxide ion | Inorganic ligands | 11.81 | 25.0 | 0.0 | 4.3 | 25.0 | 1.0 | 7.510000000000001 |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriacetic acid (HEDTA) | EDTA and derivatives | 19.7 | 25.0 | 0.1 | 12.2 | 25.0 | 0.1 | 7.5 |
| ligand_6770 | Pyridine-2-phosphonic-6-carboxylic acid (2PP6C) | Pyridine carboxylic acids | 15.97 | 25.0 | 0.1 | 8.7 | 25.0 | 0.1 | 7.270000000000001 |
| ligand_10076 | Hydroxide ion | Inorganic ligands | 11.81 | 25.0 | 0.0 | 4.6 | 25.0 | 0.0 | 7.210000000000001 |
| ligand_6253 | N-(2-Aminoethyl)iminodiacetic acid (Ethylenediamine-N,N-diacetic acid) | NTA and derivatives | 16.92 | 20.0 | 0.1 | 9.81 | 20.0 | 0.1 | 7.110000000000001 |
| ligand_6165 | Nitrilotriacetic acid (NTA) | NTA and derivatives | 15.9 | 25.0 | 0.1 | 8.83 | 20.0 | 0.1 | 7.07 |
| ligand_10076 | Hydroxide ion | Inorganic ligands | 11.27 | 25.0 | 0.1 | 4.2 | 25.0 | 0.1 | 7.069999999999999 |
| ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) | Amino Acids | 11.4 | 20.0 | 1.0 | 4.34 | 20.0 | 1.0 | 7.0600000000000005 |
| ligand_10076 | Hydroxide ion | Inorganic ligands | 11.21 | 25.0 | 3.0 | 4.2 | 25.0 | 0.1 | 7.010000000000001 |
| ligand_6165 | Nitrilotriacetic acid (NTA) | NTA and derivatives | 15.9 | 25.0 | 0.1 | 8.9 | 25.0 | 0.1 | 7.0 |
| ligand_10076 | Hydroxide ion | Inorganic ligands | 11.27 | 25.0 | 0.1 | 4.3 | 25.0 | 1.0 | 6.97 |

---

### Step 11: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (9058, 6277, 6165, 8191, 5937, 8434, 6770))",
  "order_by": "lc.ligand_id, p.pKa ASC"
}
```

[summary]
## search_pka_ligands — 23 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_5937 | N-(Phosphonomethyl)glycine (Glyphosate) | H3L | C3H8N1O5P1 | O=C(O)CNCP(=O)(O)O | −∞; H4L (M_tot_1); (-0.5, vlm_99756); H3L (M_tot_1); (2.2, vlm_99734); H2L (M_tot_1); (5.45, vlm_99712); HL (M_tot_2); (10.1, vlm_99687); L (M_tot_14); +∞ | 20~25 | 0.1 | *** |
| ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | C6H9N1O6 | O=C(O)CN(CC(=O)O)CC(=O)O | −∞; H3L (M_tot_1); (-1.81, vlm_105204); H2L (M_tot_2); (-1, vlm_105223); H3L (M_tot_1); (2.52, vlm_105186); HL (M_tot_2); (9.46, vlm_105158); L (M_tot_68); +∞ | 25 | 0.1 | *** |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | C10H16N2O8 | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | −∞; H5L (M_tot_1); (-1.5, vlm_108289); H4L (M_tot_2); (2, vlm_108282); H3L (M_tot_2); (2.69, vlm_108272); H2L (M_tot_1); (6.13, vlm_108254); HL (M_tot_7); (9.52, vlm_108224); L (M_tot_70); +∞ | 25 | 0.1 | *** |
| ligand_6770 | Pyridine-2-phosphonic-6-carboxylic acid (2PP6C) | H3L | C6H6N1O5 | O=C(O)c1cccc(P(=O)(O)O)n1 | −∞; H2L (M_tot_1); (3.66, vlm_119187); HL (M_tot_1); (7.11, vlm_119186); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) | L | C12H8N2 | c1cnc2c(c1)ccc1cccnc12 | −∞; H2L (M_tot_1); (-1.8, vlm_139234); HL (M_tot_1); (4.92, vlm_139221); L (M_tot_25); +∞ | 25 | 0.1 | *** |
| ligand_8434 | Pyridine-2,6-diphosphonic acid (2,6-PDPA) | H4L | C5H7N1O6 | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | −∞; H3L (M_tot_1); (3.14, vlm_143981); H2L (M_tot_1); (4.67, vlm_143980); HL (M_tot_1); (9.12, vlm_143979); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | H3L | C6H8O7 | O=C(O)CC(O)(CC(=O)O)C(=O)O | −∞; H3L (M_tot_1); (2.9, vlm_157473); H2L (M_tot_12); (4.35, vlm_157459); HL (M_tot_18); (5.65, vlm_157439); L (M_tot_57); +∞ | 25 | 0.1 | *** |

---

### Step 12: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, c.ligand_class_name, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND c.ligand_class_name IN ('Carboxylic acids polyacids', 'Carboxylic acids monoacids', 'Hydroxamic acids', 'Catechols', 'Phenols', 'Sulfonic acids', 'Phosphoric acids') AND s.temperature_c BETWEEN 20 AND 30 ORDER BY s.constant_value DESC LIMIT 60",
  "task_description": "Find Fe(III) 1:1 logK values for simple acid-type ligands that might be good for acidic electrodeposition",
  "column_legend": {
    "ligand_id": "c.ligand_id from ligandmetal_card — unique identifier for the ligand entity in the SRD-46 database",
    "ligand_name_SRD": "c.ligand_name_SRD from ligandmetal_card — standard reference name of the ligand chemical species",
    "ligand_class_name": "c.ligand_class_name from ligandmetal_card — classification of the ligand type (carboxylic, hydroxamic, etc.)",
    "beta_definition_name": "c.beta_definition_name from ligandmetal_card — equilibrium expression [ML]/[M][L] for 1:1 metal-ligand formation",
    "constant_value": "s.constant_value from stability_measured — log10 of formation constant K for Fe(III)-L complex, dimensionless",
    "temperature_c": "s.temperature_c from stability_measured — measurement temperature in degrees Celsius, filtered 20-30°C range",
    "ionic_strength_mol_l": "s.ionic_strength_mol_l from stability_measured — ionic strength of solution in mol/L at measurement conditions"
  }
}
```

[summary]
## execute_srd46_sql — 50 row(s)

<tool_context>
**Task (agent-stated intent):**

> Find Fe(III) 1:1 logK values for simple acid-type ligands that might be good for acidic electrodeposition

**Column legend (agent-stated chemistry origin of each column):**

| column | meaning / source table+filter / species or (T, I) |
|--------|----------------------------------------------------|
| `ligand_id` | c.ligand_id from ligandmetal_card — unique identifier for the ligand entity in the SRD-46 database |
| `ligand_name_SRD` | c.ligand_name_SRD from ligandmetal_card — standard reference name of the ligand chemical species |
| `ligand_class_name` | c.ligand_class_name from ligandmetal_card — classification of the ligand type (carboxylic, hydroxamic, etc.) |
| `beta_definition_name` | c.beta_definition_name from ligandmetal_card — equilibrium expression [ML]/[M][L] for 1:1 metal-ligand formation |
| `constant_value` | s.constant_value from stability_measured — log10 of formation constant K for Fe(III)-L complex, dimensionless |
| `temperature_c` | s.temperature_c from stability_measured — measurement temperature in degrees Celsius, filtered 20-30°C range |
| `ionic_strength_mol_l` | s.ionic_strength_mol_l from stability_measured — ionic strength of solution in mol/L at measurement conditions |

**Auto-enriched entities (filling in fields missing from the SELECT):**

*ligand_id → ligand_card (+ ligand_pka_bracket)*

| ligand_id | definition_HxL | ligand_SMILES | pka_brackets |
|-----------|----------------|---------------|--------------|
| ligand_9068 | H5L | CC(=O)N(O)CCCCC(NC(=O)CC(O)(CC(=O)NC(CCCCN(O)C(C)=O)C(=O)O)C(=O)O)C(=O)O | (-inf, H5L, 3.11, H4L, 3.48, H3L, 4.31, H2L, 8.93, HL, 9.44, L, +inf) |
| ligand_9096 | H6L | O=C(O)CC(OC(C(=O)O)C(OC(CC(=O)O)C(=O)O)C(=O)O)C(=O)O | (-inf, H6L, 2.28, H5L, 2.99, H4L, 3.69, H3L, 4.4, H2L, 5.4, HL, 5.97, L, +inf) |
| ligand_9076 | H4L | O=C(O)CC(OC(CC(=O)O)C(=O)O)C(=O)O | (-inf, H4L, 2.07, H3L, 3.98, H2L, 4.85, HL, 5.97, L, +inf) |
| ligand_9075 | H4L | O=C(O)CC(OC(CC(=O)O)C(=O)O)C(=O)O | (-inf, H4L, 2.57, H3L, 3.4, H2L, 4.79, HL, 5.97, L, +inf) |
| ligand_9058 | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | (-inf, H3L, 2.9, H2L, 4.35, HL, 5.65, L, +inf) |
| ligand_9077 | H4L | O=C(O)CC(OC(C(=O)O)C(O)C(=O)O)C(=O)O | (-inf, H4L, 2.41, H3L, 3.34, H2L, 4.38, HL, 5.73, L, +inf) |
| ligand_9314 | HL | CC(=O)c1ccccc1O | (-inf, HL, 9.94, L, +inf) |
| ligand_9332 | H2L | CCCN(CCCS(=O)(=O)O)c1ccc(N=O)c(O)c1 | (-inf, H2L, 2.61, HL, 8.23, L, +inf) |
| ligand_9195 | HL | Cc1ccc(O)cc1 | (-inf, HL, 10.04, L, +inf) |
| ligand_9194 | HL | Cc1cccc(O)c1 | (-inf, HL, 10.095, L, +inf) |
| ligand_9315 | HL | CC(=O)c1cccc(O)c1 | (-inf, HL, 9.25, L, +inf) |
| ligand_9214 | HL | Oc1ccc(F)cc1 | (-inf, HL, 9.46, L, +inf) |
| ligand_9192 | HL | Oc1ccccc1 | (-inf, HL, 9.78, L, +inf) |
| ligand_9316 | HL | CC(=O)c1ccc(O)cc1 | (-inf, HL, 7.85, L, +inf) |
| ligand_9219 | HL | Oc1ccc(Cl)cc1 | (-inf, HL, 9.2, L, +inf) |
| ligand_9218 | HL | Oc1cccc(Cl)c1 | (-inf, HL, 8.78, L, +inf) |
| ligand_9253 | H2L | O=S(=O)(O)c1ccc(O)cc1 | (-inf, HL, 8.62, L, +inf) |
| ligand_9251 | HL | N#Cc1cccc(O)c1 | (-inf, HL, 8.36, L, +inf) |
| ligand_9217 | HL | Oc1ccccc1Cl | (-inf, HL, 8.29, L, +inf) |
| ligand_9237 | HL | O=[N+]([O-])c1cccc(O)c1 | (-inf, HL, 8.16, L, +inf) |
| ligand_9252 | HL | N#Cc1ccc(O)cc1 | (-inf, HL, 7.74, L, +inf) |
| ligand_9250 | HL | N#Cc1ccccc1O | (-inf, HL, 6.86, L, +inf) |
| ligand_9238 | HL | O=[N+]([O-])c1ccc(O)cc1 | (-inf, HL, 6.96, L, +inf) |
| ligand_9236 | HL | O=[N+]([O-])c1ccccc1O | (-inf, HL, 7.04, L, +inf) |
| ligand_9228 | HL | Oc1ccccc1Br | (-inf, HL, 8.22, L, +inf) |

**SQL executed (post AST-rewrite):**

```sql
SELECT c.ligand_id, c.ligand_name_SRD, c.ligand_class_name, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND c.ligand_class_name IN ('Carboxylic acids polyacids', 'Carboxylic acids monoacids', 'Hydroxamic acids', 'Catechols', 'Phenols', 'Sulfonic acids', 'Phosphoric acids') AND s.temperature_c BETWEEN 20 AND 30 ORDER BY s.constant_value DESC LIMIT 60
```
</tool_context>

**Shared across all 50 rows:**

- `beta_definition_name` = [ML]/[M][L]
- `temperature_c` = 25.0

| ligand_id | ligand_name_SRD | ligand_class_name | constant_value | ionic_strength_mol_l |
|-----------|-----------------|-------------------|----------------|----------------------|
| ligand_9068 | Aerobactin | Carboxylic acids polyacids | 22.5 | 0.1 |
| ligand_9096 | rac-3,6-Dioxaoctane-1,2,4,5,7,8-hexacarboxylic acid (TDS) | Carboxylic acids polyacids | 20.96 | 0.1 |
| ligand_9076 | meso-Oxybis(butanedioic acid) | Carboxylic acids polyacids | 12.01 | 0.1 |
| ligand_9075 | rac-Oxybis(butanedioic acid) | Carboxylic acids polyacids | 11.43 | 0.1 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | Carboxylic acids polyacids | 11.27 | 0.1 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | Carboxylic acids polyacids | 11.19 | 0.1 |
| ligand_9077 | rac-1-Hydroxy-3-oxapentane-1,2,4,5-tetracarboxylic acid (TMS) | Carboxylic acids polyacids | 10.7 | 0.1 |
| ligand_9314 | 2-Acetylphenol (2-Hydroxyacetophenone) | Phenols | 10.52 | 3.0 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | Carboxylic acids polyacids | 10.25 | 1.0 |
| ligand_9332 | 2-Nitroso-5-(N-propyl-3-sulfopropylamino)phenol | Phenols | 9.3 | 0.1 |
| ligand_9195 | 4-Methylphenol (p-Cresol) | Phenols | 9.26 | 0.0 |
| ligand_9194 | 3-Methylphenol (m-Cresol) | Phenols | 8.51 | 0.0 |
| ligand_9315 | 3-Acetylphenol (3-Hydroxyacetophenone) | Phenols | 8.36 | 0.0 |
| ligand_9195 | 4-Methylphenol (p-Cresol) | Phenols | 8.33 | 0.5 |
| ligand_9214 | 4-Fluorophenol | Phenols | 8.29 | 0.1 |
| ligand_9192 | Hydroxybenzene (Phenol) | Phenols | 8.2 | 0.0 |
| ligand_9192 | Hydroxybenzene (Phenol) | Phenols | 7.78 | 0.1 |
| ligand_9316 | 4-Acetylphenol (4-Hydroxyacetophenone) | Phenols | 7.2 | 0.0 |
| ligand_9219 | 4-Chlorophenol | Phenols | 6.97 | 0.1 |
| ligand_9218 | 3-Chlorophenol | Phenols | 6.9 | 0.1 |
| ligand_9253 | 4-Hydroxybenzenesulfonic acid (4-Sulfophenol) | Phenols | 6.72 | 0.5 |
| ligand_9251 | 3-Cyanophenol | Phenols | 6.31 | 0.1 |
| ligand_9217 | 2-Chlorophenol | Phenols | 6.09 | 0.1 |
| ligand_9237 | 3-Nitrophenol | Phenols | 6.09 | 0.1 |
| ligand_9252 | 4-Cyanophenol | Phenols | 5.8 | 0.1 |
| ligand_9250 | 2-Cyanophenol | Phenols | 5.54 | 0.1 |
| ligand_9238 | 4-Nitrophenol | Phenols | 5.06 | 0.1 |
| ligand_9238 | 4-Nitrophenol | Phenols | -5.6 | 0.5 |
| ligand_9238 | 4-Nitrophenol | Phenols | -5.74 | 0.0 |
| ligand_9236 | 2-Nitrophenol | Phenols | -5.99 | 0.1 |
| ligand_9237 | 3-Nitrophenol | Phenols | -6.69 | 0.5 |
| ligand_9228 | 2-Bromophenol | Phenols | -6.98 | 0.1 |
| ligand_9212 | 2-Fluorophenol | Phenols | -7.19 | 0.1 |
| ligand_9228 | 2-Bromophenol | Phenols | -7.19 | 0.0 |
| ligand_9237 | 3-Nitrophenol | Phenols | -7.22 | 0.0 |
| ligand_9217 | 2-Chlorophenol | Phenols | -7.32 | 0.0 |
| ligand_9212 | 2-Fluorophenol | Phenols | -7.33 | 0.0 |
| ligand_9232 | 2-Iodophenol | Phenols | -7.43 | 0.0 |
| ligand_9233 | 3-Iodophenol | Phenols | -7.57 | 0.1 |
| ligand_9229 | 3-Bromophenol | Phenols | -7.65 | 0.1 |
| ligand_9230 | 4-Bromophenol | Phenols | -7.72 | 0.5 |
| ligand_9213 | 3-Fluorophenol | Phenols | -7.77 | 0.1 |
| ligand_9213 | 3-Fluorophenol | Phenols | -7.77 | 0.0 |
| ligand_9192 | Hydroxybenzene (Phenol) | Phenols | -7.81 | 0.5 |
| ligand_9218 | 3-Chlorophenol | Phenols | -7.89 | 0.0 |
| ligand_9219 | 4-Chlorophenol | Phenols | -7.92 | 0.0 |
| ligand_9230 | 4-Bromophenol | Phenols | -8.0 | 0.1 |
| ligand_9230 | 4-Bromophenol | Phenols | -8.1 | 0.0 |
| ligand_9214 | 4-Fluorophenol | Phenols | -8.38 | 0.0 |
| ligand_9234 | 4-Iodophenol | Phenols | -8.63 | 0.0 |

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.beta_definition_name = '[ML]/[M][L]' AND s.constant_type = 'K' AND c.ligand_class_name LIKE '%Hydroxamic%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### logK — 19 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_9906 | Rhodotorulic acid | H2L | CC(=O)N(O)CCCC1NC(=O)C(CCCN(O)C(C)=O)NC1=O | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9912 | Desferriferrioxamin E (Noca… | H3L | O=C1CCC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCN1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9911 | N-Acetyldesferriferrioxamin… | H3L | CC(=O)NCCCCCN(O)C(=O)CCC(=O)NCCCCCN(O)C(=O)CCC(=O)NCCCCCN(O)C(C)=O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9916 | Desferricoprogen | H3L | CC(=O)NC(CCCN(O)C(=O)/C=C(\C)CCO)C(=O)OCC/C(C)=C\C(=O)N(O)CCCC1NC(=O)C(CCCN(O)C(=O)/C=C(\C)CO)NC1=O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9914 | Desferriferrichrysin | *** | *** | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9909 | 1,13-Dimethyl-3,11,15,23,26… | H3L | CC12COCCCN(O)C(=O)CCOCC(C)(COCCC(=O)N(O)CCCOC1)COCCC(=O)N(O)CCCOC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9913 | Desferriferrichrome | *** | *** | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9907 | 1,1,1-Tris{[2-{(N-methylhyd… | H3L | CN(O)C(=O)CCOCC(C)(COCCC(=O)N(C)O)COCCC(=O)N(C)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9908 | 1,1,1-Tris{[3-(N-acetylhydr… | H3L | CC(=O)N(O)CCCOCC(C)(COCCCN(O)C(C)=O)COCCCN(O)C(C)=O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9915 | N,N'N''-Tris[2-(N-hydroxyca… | H3L | O=C(CCNC(=O)c1cc(C(=O)NCCC(=O)NO)cc(C(=O)NCCC(=O)NO)c1)NO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9899 | N,N'-Di-2-propyltrimethylen… | H2L | CC(C)N(O)C(=O)CCCC(=O)N(O)C(C)C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9900 | N,N'-Di-2-propyltetramethyl… | H2L | CC(C)N(O)C(=O)CCCCC(=O)N(O)C(C)C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9901 | N,N'-Di-2-propylpentamethyl… | H2L | CC(C)N(O)C(=O)CCCCCC(=O)N(O)C(C)C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9902 | N,N'-Di-2-propylhexamethyle… | H2L | CC(C)N(O)C(=O)CCCCCCC(=O)N(O)C(C)C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9898 | Octamethylenedihydroxamic a… | H2L | O=C(CCCCCCCCC(=O)NO)NO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9897 | Heptamethylenedihydroxamic … | H2L | O=C(CCCCCCCC(=O)NO)NO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9896 | Hexamethylenedihydroxamic a… | H2L | O=C(CCCCCCC(=O)NO)NO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9895 | Tetramethylenedihydroxamic … | H2L | O=C(CCCCC(=O)NO)NO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9890 | N-Methyl-4-methoxybenzohydr… | HL | COc1ccc(C(=O)N(C)O)cc1 | 1 | 1 | 25 | 2 | *** | 1 |

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.beta_definition_name = '[ML]/[M][L]' AND s.constant_type = 'K' AND c.ligand_name_SRD LIKE '%oxal%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 4 row(s)

### `Fe^[3+]` + Pyridine-2-carboxaldehyde oxime — 1 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8047
ligand_HxL_def: HL | ligand_SMILES: O/N=C/c1ccccn1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_136897 | ref_eq_map_14392 | beta_def_812 | logK | 11.9 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.99, L, +inf) |

### `Fe^[3+]` + Ethanedioic acid (Oxalic acid) — 3 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8872
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_151795 | ref_eq_map_19978 | beta_def_812 | logK | 7.74 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |
| vlm_151794 | ref_eq_map_19976 | beta_def_812 | logK | 7.58 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |
| vlm_151793 | ref_eq_map_19977 | beta_def_812 | logK | 7.53 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.beta_definition_name = '[ML]/[M][L]' AND s.constant_type = 'K' AND c.ligand_name_SRD LIKE '%tartar%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 3 row(s)

### `Fe^[3+]` + meso-2,3-Dihydroxybutanedioic acid (meso-Tartaric acid) — 1 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8956
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)[C@@H](O)[C@@H](O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_155157 | ref_eq_map_21222 | beta_def_812 | logK | 6.66 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (4.49, L, +inf) |

### `Fe^[3+]` + D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) — 2 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8955
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)C(O)C(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_155036 | ref_eq_map_21191 | beta_def_812 | logK | 6.49 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.97, L, +inf) |
| vlm_155037 | ref_eq_map_21192 | beta_def_812 | logK | 5.73 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.97, L, +inf) |

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.beta_definition_name = '[ML]/[M][L]' AND s.constant_type = 'K' AND c.ligand_name_SRD LIKE '%oxal%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 1 row(s)

### `Fe^[2+]` + Ethanedioic acid (Oxalic acid) — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8872
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_151749 | ref_eq_map_19964 | beta_def_812 | logK | 3.05 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |

---

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.beta_definition_name = '[ML]/[M][L]' AND s.constant_type = 'K' AND c.ligand_name_SRD LIKE '%tartar%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 1 row(s)

### `Fe^[2+]` + D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8955
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)C(O)C(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_155002 | ref_eq_map_21180 | beta_def_812 | logK | 2.24 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.97, L, +inf) |

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.beta_definition_name = '[ML]/[M][L]' AND s.constant_type = 'K' AND c.ligand_name_SRD LIKE '%sulfosalicyl%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### ΔS — 11 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 2 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_9362 | 2,5-Dihydroxybenzenecarboxy… | H3L | O=C(O)c1cc(O)ccc1O | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_44 | Dy^[3+] | ligand_9362 | 2,5-Dihydroxybenzenecarboxy… | H3L | O=C(O)c1cc(O)ccc1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_9362 | 2,5-Dihydroxybenzenecarboxy… | H3L | O=C(O)c1cc(O)ccc1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_173 | Sm^[3+] | ligand_9362 | 2,5-Dihydroxybenzenecarboxy… | H3L | O=C(O)c1cc(O)ccc1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_65 | Gd^[3+] | ligand_9362 | 2,5-Dihydroxybenzenecarboxy… | H3L | O=C(O)c1cc(O)ccc1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_55 | Er^[3+] | ligand_9362 | 2,5-Dihydroxybenzenecarboxy… | H3L | O=C(O)c1cc(O)ccc1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_73 | Ho^[3+] | ligand_9362 | 2,5-Dihydroxybenzenecarboxy… | H3L | O=C(O)c1cc(O)ccc1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_139 | Pr^[3+] | ligand_9362 | 2,5-Dihydroxybenzenecarboxy… | H3L | O=C(O)c1cc(O)ccc1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_110 | Nd^[3+] | ligand_9362 | 2,5-Dihydroxybenzenecarboxy… | H3L | O=C(O)c1cc(O)ccc1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 0.5 | *** | 0 |

### logK — 2 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 5 | 1 | 25 | 0~3 | *** | 5 |
| metal_19 | Be^[2+] | ligand_9362 | 2,5-Dihydroxybenzenecarboxy… | H3L | O=C(O)c1cc(O)ccc1O | 1 | 1 | 25 | 0.5 | *** | 1 |

### ΔH — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 0.5 | *** | 0 |

---

### Step 19: `search_ligands`
**Args:**
```json
{
  "name": "sulfosalicylic"
}
```

[summary]
## search_ligands — 7 result(s)

**stats:** 7 SQL matches · showing 7 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic … (5-Sulfosalicylic acid) | H3L | Phenols salicylic acids | 127 | `O=C(O)c1cc(S(=O)(=O)O)ccc1O` | (-inf, H2L, 2.48, HL, 11.85, L, +inf) |
| ligand_9285 | 3-Bromo-2-hydroxy… (3-Bromo-5-sulfosalicylic acid) | H3L | Phenols salicylic acids | 89 | `O=C(O)c1cc(S(=O)(=O)O)cc(Br)c1O` | (-inf, H2L, 2.02, HL, 10.52, L, +inf) |
| ligand_9287 | 2-Hydroxy-3,5-disulfo… (3,5-Disulfosalicylic acid) | H4L | Phenols salicylic acids | 51 | `O=C(O)c1cc(S(=O)(=O)O)cc(S(=O)(=O)O)c1O` | (-inf, H2L, 2.03, HL, 2.03, L, +inf) |
| ligand_11011 | 3-Methyl-5-sulfosalicylic acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_11012 | 4-Methyl-5-sulfosalicylic acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_11013 | 5-Methyl-3-sulfosalicylic acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_11015 | 3-Amino-5-sulfosalicylic acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 3 | 100% |
| carboxyl | 3 | 100% |
| hydroxyl | 3 | 100% |
| phenol | 3 | 100% |
| sulfonate | 3 | 100% |
| halide | 1 | 33% |

---

### Step 20: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id = ligand_9284 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 7 row(s)

### `Fe^[3+]` + 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) — 7 measurement(s)
metal_id: metal_61 | ligand_id: ligand_9284
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)c1cc(S(=O)(=O)O)ccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_160912 | ref_eq_map_23323 | beta_def_821 | logK | 2.7 | 25 | 0.1 | `[M] + [HL] <=> [ML] + [H]` | *** | [HL] | (2.48, HL, 11.85) |
| vlm_160914 | ref_eq_map_23326 | beta_def_821 | logK | 2.69 | 25 | 1 | `[M] + [HL] <=> [ML] + [H]` | *** | [HL] | (2.48, HL, 11.85) |
| vlm_160915 | ref_eq_map_23324 | beta_def_821 | logK | 2.68 | 25 | 3 | `[M] + [HL] <=> [ML] + [H]` | *** | [HL] | (2.48, HL, 11.85) |
| vlm_160913 | ref_eq_map_23325 | beta_def_821 | logK | 2.65 | 20 | 0.1 | `[M] + [HL] <=> [ML] + [H]` | *** | [HL] | (2.48, HL, 11.85) |
| vlm_160919 | ref_eq_map_23324 | beta_def_846 | logK | -0.9 | 25 | 3 | `[ML] + [HL] <=> [ML2] + [H]` | *** | [HL] | (2.48, HL, 11.85) |
| vlm_160918 | ref_eq_map_23323 | beta_def_846 | logK | -1.4 | 20 | 0.1 | `[ML] + [HL] <=> [ML2] + [H]` | *** | [HL] | (2.48, HL, 11.85) |
| vlm_160920 | ref_eq_map_23324 | beta_def_873 | logK | -4.7 | 25 | 3 | `[ML2] + [HL] <=> [ML3] + [H]` | *** | [HL] | (2.48, HL, 11.85) |

---

### Step 21: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.ligand_id = ligand_9284 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 1 row(s)

### `Fe^[2+]` + 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_9284
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)c1cc(S(=O)(=O)O)ccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_160888 | ref_eq_map_23310 | beta_def_821 | logK | -5.9 | 20 | 0.1 | `[M] + [HL] <=> [ML] + [H]` | *** | [HL] | (2.48, HL, 11.85) |

---

### Step 22: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.ligand_id = ligand_9058 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 5 row(s)

### `Fe^[2+]` + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) — 5 measurement(s)
metal_id: metal_62 | ligand_id: ligand_9058
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CC(O)(CC(=O)O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_157619 | ref_eq_map_22111 | beta_def_812 | logK | 4.4 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.65, L, +inf) |
| vlm_157623 | ref_eq_map_22109 | beta_def_779 | logK | 2.9 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (4.35, HL, 5.65) |
| vlm_157624 | ref_eq_map_22111 | beta_def_779 | logK | 2.65 | 20 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (4.35, HL, 5.65) |
| vlm_157626 | ref_eq_map_22113 | beta_def_779 | logK | 2.6 | 25 | 3 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (4.35, HL, 5.65) |
| vlm_157620 | ref_eq_map_22109 | beta_def_812 | logK | -4.8 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.65, L, +inf) |

---

### Step 23: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id = ligand_9058 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 6 row(s)

### `Fe^[3+]` + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) — 6 measurement(s)
metal_id: metal_61 | ligand_id: ligand_9058
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CC(O)(CC(=O)O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_157689 | ref_eq_map_22123 | beta_def_424 | logK | 21.2 | 20 | 0.1 | `[M]^2 + [L]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2` | *** | [L] | (5.65, L, +inf) |
| vlm_157683 | ref_eq_map_22124 | beta_def_812 | logK | 11.27 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.65, L, +inf) |
| vlm_157682 | ref_eq_map_22123 | beta_def_812 | logK | 11.19 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.65, L, +inf) |
| vlm_157684 | ref_eq_map_22125 | beta_def_812 | logK | 10.25 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.65, L, +inf) |
| vlm_157687 | ref_eq_map_22123 | beta_def_779 | logK | 6.7 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (4.35, HL, 5.65) |
| vlm_157688 | ref_eq_map_22123 | beta_def_966 | logK | 2.7 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |

---

### Step 24: `search_ligands`
**Args:**
```json
{
  "name": "fluoride"
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10162 | Hydrogen fluoride (Hydrofluoric acid) | HL | Inorganic ligands | 642 | `F` | (-inf, HL, 2.94, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| halide | 1 | 100% |

---

### Step 25: `search_ligands`
**Args:**
```json
{
  "name": "sulfate"
}
```

[summary]
## search_ligands — 11 result(s)

**stats:** 11 SQL matches · showing 11 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6852 | 2-Aminoethyl(hydrogensulfate) | HL | Aliphatic amines | 5 | `NCCOS(=O)(=O)O` | (-inf, HL, 9.182, L, +inf) |
| ligand_9382 | 2,3,4-Trihydroxybenzenesulfon… (Pyrogallolsulfate) | H4L | Catechols | 4 | `O=S(=O)(O)c1ccc(O)c(O)c1O` | (-inf, H3L, 8.28, H2L, 11.3, HL, +inf) |
| ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | HL | Inorganic ligands | 581 | `O=S(=O)([O-])O` | (-inf, HL, 1.54, L, +inf) |
| ligand_10149 | Hydrogen thiosulfate (Thiosulfuric acid) | H2L | Inorganic ligands | 117 | `O=S(O)(O)=S` | (-inf, H2L, -0.6, HL, -0.6, L, +inf) |
| ligand_10150 | Selenosulfate ion | *** | Inorganic ligands | 1 | *** | *** |
| ligand_10151 | Hydrogen amidosulfate (Sulfamic acid) | HL | Inorganic ligands | 22 | `NS(=O)(=O)O` | (-inf, HL, 0.034, L, +inf) |
| ligand_10152 | Hydrogen hydroxyl… (Hydroxylamine-O-sulfonic acid) | HL | Inorganic ligands | 1 | `NOS(=O)(=O)O` | (-inf, HL, 1.48, L, +inf) |
| ligand_10153 | Hydrogen amidodisulfate (Aminodisulfonic acid) | H2L | Inorganic ligands | 1 | `O=S(=O)(O)NS(=O)(=O)O` | (-inf, HL, 8.5, L, +inf) |
| ligand_10154 | Hydrogen peroxosulfate | H2L | Inorganic ligands | 1 | `O=S(=O)(O)OO` | (-inf, HL, 9.86, L, +inf) |
| ligand_10155 | Hydrogen peroxydisulfate (Peroxydisulfuric acid) | H2L | Inorganic ligands | 27 | `O=S(=O)(O)OOS(=O)(=O)O` | *** |
| ligand_11517 | Hydrogen imidobis(fluorosulfate) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (9 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 9 | 100% |
| sulfonate | 8 | 89% |
| primary_amine | 3 | 33% |
| aromatic_ring | 1 | 11% |
| phenol | 1 | 11% |
| secondary_amine | 1 | 11% |

---

### Step 26: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id = ligand_10162 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 7 row(s)

### `Fe^[3+]` + Hydrogen fluoride (Hydrofluoric acid) — 7 measurement(s)
metal_id: metal_61 | ligand_id: ligand_10162
ligand_HxL_def: HL | ligand_SMILES: F

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_177006 | ref_eq_map_29571 | beta_def_872 | logK | 12.2 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (2.94, L, +inf) |
| vlm_177005 | ref_eq_map_29570 | beta_def_872 | logK | 12 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (2.94, L, +inf) |
| vlm_177001 | ref_eq_map_29570 | beta_def_840 | logK | 9.12 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (2.94, L, +inf) |
| vlm_177002 | ref_eq_map_29571 | beta_def_840 | logK | 9.11 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (2.94, L, +inf) |
| vlm_176998 | ref_eq_map_29569 | beta_def_812 | logK | 6.04 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (2.94, L, +inf) |
| vlm_176996 | ref_eq_map_29570 | beta_def_812 | logK | 5.17 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (2.94, L, +inf) |
| vlm_176997 | ref_eq_map_29571 | beta_def_812 | logK | 5.15 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (2.94, L, +inf) |

---

### Step 27: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.ligand_id = ligand_10162 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 1 row(s)

### `Fe^[2+]` + Hydrogen fluoride (Hydrofluoric acid) — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_10162
ligand_HxL_def: HL | ligand_SMILES: F

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_176954 | ref_eq_map_29545 | beta_def_812 | logK | 0.8 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (2.94, L, +inf) |

---

### Step 28: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id = ligand_10148 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 5 row(s)

### `Fe^[3+]` + Hydrogen sulfate ion (Sulfuric acid) — 5 measurement(s)
metal_id: metal_61 | ligand_id: ligand_10148
ligand_HxL_def: HL | ligand_SMILES: O=S(=O)([O-])O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_176065 | ref_eq_map_29192 | beta_def_812 | logK | 4.05 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (1.54, L, +inf) |
| vlm_176061 | ref_eq_map_29188 | beta_def_812 | logK | 2.8 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (1.54, L, +inf) |
| vlm_176062 | ref_eq_map_29189 | beta_def_812 | logK | 2.34 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (1.54, L, +inf) |
| vlm_176063 | ref_eq_map_29190 | beta_def_812 | logK | 1.96 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (1.54, L, +inf) |
| vlm_176064 | ref_eq_map_29191 | beta_def_812 | logK | 1.93 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (1.54, L, +inf) |

---

### Step 29: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.ligand_id = ligand_10148 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 1 row(s)

### `Fe^[2+]` + Hydrogen sulfate ion (Sulfuric acid) — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_10148
ligand_HxL_def: HL | ligand_SMILES: O=S(=O)([O-])O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_176011 | ref_eq_map_29163 | beta_def_812 | logK | -2.39 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (1.54, L, +inf) |

---

### Step 30: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND c.ligand_class_name LIKE '%Hydroxamic%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 1 row(s)

### `Fe^[2+]` + Acetohydroxamic acid — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_9873
ligand_HxL_def: HL | ligand_SMILES: CC(=O)NO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_168432 | ref_eq_map_26534 | beta_def_812 | logK | 4.8 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.29, L, +inf) |

---

### Step 31: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND c.ligand_name_SRD LIKE '%malon%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 2 row(s)

### `Fe^[2+]` + Propanedioic acid (Malonic acid) — 2 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8873
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_152297 | ref_eq_map_20098 | beta_def_812 | logK | 2.24 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152296 | ref_eq_map_20097 | beta_def_812 | logK | 2.17 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |

---

### Step 32: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND c.ligand_name_SRD LIKE '%succin%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 1 row(s)

### `Fe^[2+]` + L-Hydroxybutanedioic acid (Hydroxysuccinic acid)(Malic acid) — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8953
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CC(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_154812 | ref_eq_map_21103 | beta_def_812 | logK | 2.6 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (4.68, L, +inf) |

---

### Step 33: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND c.ligand_name_SRD LIKE '%picolinic%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 1 row(s)

### `Fe^[3+]` + Pyridine-2,6-dicarboxylic acid (Dipicolinic acid) — 1 measurement(s)
metal_id: metal_61 | ligand_id: ligand_6774
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1cccc(C(=O)O)n1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_119514 | ref_eq_map_8532 | beta_def_812 | logK | 10.91 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (4.66, L, +inf) |

---

### Step 34: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND c.ligand_name_SRD LIKE '%picolinic%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 2 row(s)

### `Fe^[2+]` + Pyridine-2,6-dicarboxylic acid (Dipicolinic acid) — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_6774
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1cccc(C(=O)O)n1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_119483 | ref_eq_map_8525 | beta_def_812 | logK | 5.71 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (4.66, L, +inf) |

### `Fe^[2+]` + Pyridine-2-carboxylic acid (Picolinic acid) — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_6762
ligand_HxL_def: HL | ligand_SMILES: O=C(O)c1ccccn1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_118872 | ref_eq_map_8350 | beta_def_812 | logK | 4.9 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.21, L, +inf) |

---

### Step 35: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND c.ligand_id = ligand_6762 AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### `Tm^[3+]` + Pyridine-2,6-dicarboxylic acid (Dipicolinic acid) — 2 measurement(s)
metal_id: metal_192 | ligand_id: ligand_6774
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1cccc(C(=O)O)n1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_119459 | *** | beta_def_840 | ΔS | 238.1 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (4.66, L, +inf) |
| vlm_119462 | *** | beta_def_872 | ΔS | 238.1 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (4.66, L, +inf) |

### `Lu^[3+]` + Pyridine-2,6-dicarboxylic acid (Dipicolinic acid) — 2 measurement(s)
metal_id: metal_81 | ligand_id: ligand_6774
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1cccc(C(=O)O)n1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_119477 | *** | beta_def_840 | ΔS | 236 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (4.66, L, +inf) |
| vlm_119480 | *** | beta_def_872 | ΔS | 230.1 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (4.66, L, +inf) |

### `Yb^[3+]` + Pyridine-2,6-dicarboxylic acid (Dipicolinic acid) — 2 measurement(s)
metal_id: metal_206 | ligand_id: ligand_6774
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1cccc(C(=O)O)n1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_119468 | *** | beta_def_840 | ΔS | 235.6 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (4.66, L, +inf) |
| vlm_119471 | *** | beta_def_872 | ΔS | 231.8 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (4.66, L, +inf) |

### `Y^[3+]` + Pyridine-2,6-dicarboxylic acid (Dipicolinic acid) — 1 measurement(s)
metal_id: metal_205 | ligand_id: ligand_6774
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1cccc(C(=O)O)n1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_119354 | *** | beta_def_872 | ΔS | 234.3 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (4.66, L, +inf) |

### `Er^[3+]` + Pyridine-2,6-dicarboxylic acid (Dipicolinic acid) — 2 measurement(s)
metal_id: metal_55 | ligand_id: ligand_6774
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1cccc(C(=O)O)n1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_119453 | *** | beta_def_872 | ΔS | 232.2 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (4.66, L, +inf) |
| vlm_119450 | *** | beta_def_840 | ΔS | 231.4 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (4.66, L, +inf) |

### `Ho^[3+]` + Pyridine-2,6-dicarboxylic acid (Dipicolinic acid) — 1 measurement(s)
metal_id: metal_73 | ligand_id: ligand_6774
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1cccc(C(=O)O)n1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_119444 | *** | beta_def_872 | ΔS | 228.4 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (4.66, L, +inf) |

---

### Step 36: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND c.ligand_name_SRD LIKE '%phospho%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 15 row(s)

### logK — 15 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6041 | N,N'-Bis(3-hydroxy-5-phosph… | H6L | Cc1ncc(COP(=O)(O)O)c(CN(CCN(CC(=O)O)Cc2c(COP(=O)(O)O)cnc(C)c2O)CC(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8442 | Ethylenebis(imino(2-hydroxy… | H4L | O=[PH](O)C(NCCNC(c1ccccc1O)[PH](=O)O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8389 | Ethylenebis[imino(2-hydroxy… | H4L | O=P(O)(O)C(NCCNC(c1ccccc1O)P(=O)(O)O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8421 | N,N'-Dimethylethylenebis(ni… | H4L | CN(CCN(C)CP(=O)(O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8424 | N,N'-Bis(2-hydroxyethyl)eth… | H4L | O=P(O)(O)CN(CCO)CCN(CCO)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8434 | Pyridine-2,6-diphosphonic a… | H4L | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8360 | Amino(phenyl)methylenedipho… | H4L | NC(c1ccccc1)(P(=O)(O)O)P(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8400 | Perhydro-1,4-oxazine-4-ylme… | H4L | O=P(O)(O)C(N1CCOCC1)P(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8427 | N-(2-Hydroxyethyl)ethylened… | H6L | O=P(O)(O)CN(CCO)CCN(CP(=O)(O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6195 | N-(2-Carboxyethyl)-N-(phosp… | H4L | O=C(O)CCN(CC(=O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5937 | N-(Phosphonomethyl)glycine … | H3L | O=C(O)CNCP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6770 | Pyridine-2-phosphonic-6-car… | H3L | O=C(O)c1cccc(P(=O)(O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8388 | Ethylenebis[imino(phenyl)me… | H4L | O=P(O)(O)C(NCCNC(c1ccccc1)P(=O)(O)O)c1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9145 | Benzo-1,3-dioxole-2,2-dipho… | H4L | O=P(O)(O)C1(P(=O)(O)O)Oc2ccccc2O1 | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6019 | N,N-Bis(phosphonomethyl)gly… | H5L | O=C(O)CN(CP(=O)(O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

---

### Step 37: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND c.ligand_name_SRD LIKE '%acetohydroxam%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### logK — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6054 | N,N'-Bis(carboxymethyl)ethy… | H4L | CC(C)N(O)C(=O)CN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6057 | N,N',N''-Tris(carboxymethyl… | H5L | CC(C)N(O)C(=O)CN(CCN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7320 | Ethylenedinitrilotetraaceto… | H4L | O=C(CN(CCN(CC(=O)NO)CC(=O)NO)CC(=O)NO)NO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6036 | N,N'-Bis(carboxymethyl)ethy… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)NO)CC(=O)NO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7295 | Nitrilotriacetohydroxamic a… | H3L | O=C(CN(CC(=O)NO)CC(=O)NO)NO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6020 | N-(Carboxymethyl)-N-(2-hydr… | H2L | O=C(O)CN(CCO)CC(=O)NO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7391 | Piperazine-N,N'-diacetohydr… | H2L | O=C(CN1CCN(C(=O)NO)CC1)NO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6203 | N,N-Bis(carboxymethyl)amino… | H3L | O=C(O)CN(CC(=O)O)CC(=O)NO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5938 | (Carboxymethylamino)acetohy… | H2L | O=C(O)CNCC(=O)NO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7154 | Iminodiacetohydroxamic acid | H2L | O=C(CNCC(=O)NO)NO | 1 | 1 | 20 | 0.1 | *** | 1 |

---

### Step 38: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND c.ligand_name_SRD LIKE '%salicyl%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### `Cu^[2+]` + Benzene-1,2-dicarboxylic acid (Phthalic acid) — 2 measurement(s)
metal_id: metal_41 | ligand_id: ligand_8938
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_154479 | *** | beta_def_840 | ΔS | 157.3 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (4.92, L, +inf) |
| vlm_154472 | *** | beta_def_812 | ΔS | 105 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (4.92, L, +inf) |

### `H^[+]` + Phosphoric acid 1-naphthyl ester (alpha-Naphthyl phosphate) — 1 measurement(s)
metal_id: metal_68 | ligand_id: ligand_9154
ligand_HxL_def: H2L | ligand_SMILES: O=P(O)(O)Oc1cccc2ccccc12

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_159458 | *** | beta_def_79 | ΔS | 125.1 | 25 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-0.9, HL, 5.74, L, +inf) |

### `Cu^[2+]` + Phosphoric acid phenyl ester (Phenyl phosphate) — 1 measurement(s)
metal_id: metal_41 | ligand_id: ligand_9152
ligand_HxL_def: H2L | ligand_SMILES: O=P(O)(O)Oc1ccccc1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_159441 | *** | beta_def_812 | ΔS | 124.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.78, L, +inf) |

### `H^[+]` + Phosphoric acid phenyl ester (Phenyl phosphate) — 1 measurement(s)
metal_id: metal_68 | ligand_id: ligand_9152
ligand_HxL_def: H2L | ligand_SMILES: O=P(O)(O)Oc1ccccc1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_159430 | *** | beta_def_79 | ΔS | 123 | 25 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-0.9, HL, 5.78, L, +inf) |

### `Cu^[2+]` + Phosphoric acid 1-naphthyl ester (alpha-Naphthyl phosphate) — 1 measurement(s)
metal_id: metal_41 | ligand_id: ligand_9154
ligand_HxL_def: H2L | ligand_SMILES: O=P(O)(O)Oc1cccc2ccccc12

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_159465 | *** | beta_def_812 | ΔS | 115.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.74, L, +inf) |

### `H^[+]` + Benzene-1,2-dicarboxylic acid (Phthalic acid) — 2 measurement(s)
metal_id: metal_68 | ligand_id: ligand_8938
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_154376 | *** | beta_def_79 | ΔS | 110.9 | 25 | 0 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (2.76, HL, 4.92, L, +inf) |
| vlm_154377 | *** | beta_def_79 | ΔS | 100 | 25 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (2.76, HL, 4.92, L, +inf) |

### `H^[+]` + 2-Methoxybenzoic acid — 1 measurement(s)
metal_id: metal_68 | ligand_id: ligand_8758
ligand_HxL_def: HL | ligand_SMILES: COc1ccccc1C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_150325 | *** | beta_def_79 | ΔS | 100.8 | 25 | 0 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-inf, HL, 3.87, L, +inf) |

### `Zn^[2+]` + Benzene-1,2-dicarboxylic acid (Phthalic acid) — 1 measurement(s)
metal_id: metal_208 | ligand_id: ligand_8938
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_154494 | *** | beta_def_812 | ΔS | 100.8 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (4.92, L, +inf) |

---

### Step 39: `search_ligands`
**Args:**
```json
{
  "name": "salicylic acid"
}
```

[summary]
## search_ligands — 25 result(s)

**stats:** 43 SQL matches · showing 25 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8701 | 2-Acetoxybenzoic acid (Acetylsalicylic acid) | HL | Carboxylic acids keto | 5 | `CC(=O)Oc1ccccc1C(=O)O` | (-inf, HL, 3.45, L, +inf) |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | H2L | Phenols salicylic acids | 227 | `O=C(O)c1ccccc1O` | (-inf, H2L, 2.8, HL, 2.8, L, +inf) |
| ligand_9265 | 2-Hydroxy-3-methylbenzoic acid (3-Methylsalicylic… | H2L | Phenols salicylic acids | 9 | `Cc1cccc(C(=O)O)c1O` | (-inf, H2L, 2.83, HL, 2.83, L, +inf) |
| ligand_9266 | 2-Hydroxy-4-methylbenzoic acid (4-Methylsalicylic… | H2L | Phenols salicylic acids | 8 | `Cc1ccc(C(=O)O)c(O)c1` | (-inf, H2L, 2.96, HL, 2.96, L, +inf) |
| ligand_9267 | 2-Hydroxy-5-methylbenzoic acid (5-Methylsalicylic… | H2L | Phenols salicylic acids | 6 | `Cc1ccc(O)c(C(=O)O)c1` | (-inf, H2L, 2.88, HL, 2.88, L, +inf) |
| ligand_9268 | 2-Hydroxy-6-methylbenzoi… (6-Methylsalicylic acid) | H2L | Phenols salicylic acids | 5 | `Cc1cccc(O)c1C(=O)O` | (-inf, H2L, 3.16, HL, +inf) |
| ligand_9269 | 2-Hydroxy-3-(2-propyl… (3-Isopropylsalicylic acid) | H2L | Phenols salicylic acids | 2 | `CC(C)c1cccc(C(=O)O)c1O` | (-inf, H2L, 2.76, HL, +inf) |
| ligand_9274 | 5-Fluoro-2-hydroxybenzoi… (5-Fluorosalicylic acid) | H2L | Phenols salicylic acids | 3 | `O=C(O)c1cc(F)ccc1O` | (-inf, H2L, 2.56, HL, 2.56, L, +inf) |
| ligand_9275 | 5-Chloro-2-hydroxybenzoi… (5-Chlorosalicylic acid) | H2L | Phenols salicylic acids | 19 | `O=C(O)c1cc(Cl)ccc1O` | (-inf, H2L, 2.46, HL, 2.46, L, +inf) |
| ligand_9276 | 6-Chloro-2-hydroxybenzoi… (6-Chlorosalicylic acid) | H2L | Phenols salicylic acids | 1 | `O=C(O)c1c(O)cccc1Cl` | (-inf, H2L, 2.63, HL, +inf) |
| ligand_9277 | 5-Bromo-2-hydroxybenzoic … (5-Bromosalicylic acid) | H2L | Phenols salicylic acids | 11 | `O=C(O)c1cc(Br)ccc1O` | (-inf, H2L, 2.44, HL, 2.44, L, +inf) |
| ligand_9278 | 2-Hydroxy-5-iodobenzoic ac… (5-Iodosalicylic acid) | H2L | Phenols salicylic acids | 10 | `O=C(O)c1cc(I)ccc1O` | (-inf, H2L, -2.54, HL, -2.54, L, +inf) |
| ligand_9279 | 2-Hydroxy-3-nitrobenzoic … (3-Nitrosalicylic acid) | H2L | Phenols salicylic acids | 14 | `O=C(O)c1cccc([N+](=O)[O-])c1O` | (-inf, H2L, -1.73, HL, 9.87, L, +inf) |
| ligand_9280 | 2-Hydroxy-4-nitrobenzoic … (4-Nitrosalicylic acid) | H2L | Phenols salicylic acids | 4 | `O=C(O)c1ccc([N+](=O)[O-])cc1O` | (-inf, H2L, 2.05, HL, 10.91, L, +inf) |
| ligand_9281 | 2-Hydroxy-5-nitrobenzoic … (5-Nitrosalicylic acid) | H2L | Phenols salicylic acids | 36 | `O=C(O)c1cc([N+](=O)[O-])ccc1O` | (-inf, H2L, -1.94, HL, 9.9, L, +inf) |
| ligand_9282 | 2-Hydroxy-6-nitrobenzoic … (6-Nitrosalicylic acid) | H2L | Phenols salicylic acids | 4 | `O=C(O)c1c(O)cccc1[N+](=O)[O-]` | (-inf, H2L, 1.99, HL, 9.04, L, +inf) |
| ligand_9283 | 2-Hydroxy-3,5-dinitro… (3,5-Dinitrosalicylic acid) | H2L | Phenols salicylic acids | 35 | `O=C(O)c1cc([N+](=O)[O-])cc([N+](=O)[O-])c1O` | (-inf, H2L, -0.3, HL, 7.07, L, +inf) |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic … (5-Sulfosalicylic acid) | H3L | Phenols salicylic acids | 127 | `O=C(O)c1cc(S(=O)(=O)O)ccc1O` | (-inf, H2L, 2.48, HL, 11.85, L, +inf) |
| ligand_9285 | 3-Bromo-2-hydroxy… (3-Bromo-5-sulfosalicylic acid) | H3L | Phenols salicylic acids | 89 | `O=C(O)c1cc(S(=O)(=O)O)cc(Br)c1O` | (-inf, H2L, 2.02, HL, 10.52, L, +inf) |
| ligand_9287 | 2-Hydroxy-3,5-disulfo… (3,5-Disulfosalicylic acid) | H4L | Phenols salicylic acids | 51 | `O=C(O)c1cc(S(=O)(=O)O)cc(S(=O)(=O)O)c1O` | (-inf, H2L, 2.03, HL, 2.03, L, +inf) |
| ligand_9288 | 2-Hydroxy-3-methoxybenz… (3-Methoxysalicylic acid) | H2L | Phenols salicylic acids | 3 | `COc1cccc(C(=O)O)c1O` | (-inf, H2L, 2.69, HL, 2.69, L, +inf) |
| ligand_9289 | 2-Hydroxy-5-methoxybenz… (5-Methoxysalicylic acid) | H2L | Phenols salicylic acids | 3 | `COc1ccc(O)c(C(=O)O)c1` | (-inf, H2L, 2.92, HL, 2.92, L, +inf) |
| ligand_9296 | 2-Hydroxy-5-cyanobenzoic … (5-Cyanosalicylic acid) | H2L | Phenols salicylic acids | 3 | `N#Cc1ccc(O)c(C(=O)O)c1` | (-inf, H2L, 2.36, HL, 2.36, L, +inf) |
| ligand_9297 | 4-Amino-2-hydroxybenzoic … (p-Aminosalicylic acid) | H2L | Phenols salicylic acids | 31 | `Nc1ccc(C(=O)O)c(O)c1` | (-inf, H3L, -1.8, H2L, 3.63, HL, +inf) |
| ligand_9298 | 5-Amino-2-hydroxybenzoic … (m-Aminosalicylic acid) | H2L | Phenols salicylic acids | 18 | `Nc1ccc(O)c(C(=O)O)c1` | (-inf, H3L, 2.28, H2L, 2.28, HL, -5.6, L, +inf) |

### Functional groups across all SQL matches (25 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 25 | 100% |
| carboxyl | 25 | 100% |
| hydroxyl | 24 | 96% |
| phenol | 24 | 96% |
| halide | 6 | 24% |
| tertiary_amine | 5 | 20% |
| sulfonate | 3 | 12% |
| primary_amine | 2 | 8% |
| ester | 1 | 4% |
| nitrile | 1 | 4% |

---

### Step 40: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id = ligand_9257 AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### `Cu^[2+]` + Benzene-1,2-dicarboxylic acid (Phthalic acid) — 3 measurement(s)
metal_id: metal_41 | ligand_id: ligand_8938
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_154479 | *** | beta_def_840 | ΔS | 157.3 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (4.92, L, +inf) |
| vlm_154472 | *** | beta_def_812 | ΔS | 105 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (4.92, L, +inf) |
| vlm_154473 | *** | beta_def_812 | ΔS | 96.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (4.92, L, +inf) |

### `Yb^[3+]` + 2-Hydroxybenzoic acid (Salicylic acid) — 1 measurement(s)
metal_id: metal_206 | ligand_id: ligand_9257
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_160348 | *** | beta_def_194 | ΔS | 128.9 | 25 | 0.1 | `[M] + [HL]^2 <=> [M(HL)2]` | *** | [HL] | (-13.4, HL, 2.8) |

### `H^[+]` + Benzene-1,2-dicarboxylic acid (Phthalic acid) — 2 measurement(s)
metal_id: metal_68 | ligand_id: ligand_8938
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_154376 | *** | beta_def_79 | ΔS | 110.9 | 25 | 0 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (2.76, HL, 4.92, L, +inf) |
| vlm_154377 | *** | beta_def_79 | ΔS | 100 | 25 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (2.76, HL, 4.92, L, +inf) |

### `Lu^[3+]` + 2-Hydroxybenzoic acid (Salicylic acid) — 1 measurement(s)
metal_id: metal_81 | ligand_id: ligand_9257
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_160354 | *** | beta_def_194 | ΔS | 101.7 | 25 | 0.1 | `[M] + [HL]^2 <=> [M(HL)2]` | *** | [HL] | (-13.4, HL, 2.8) |

### `Zn^[2+]` + Benzene-1,2-dicarboxylic acid (Phthalic acid) — 1 measurement(s)
metal_id: metal_208 | ligand_id: ligand_8938
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_154494 | *** | beta_def_812 | ΔS | 100.8 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (4.92, L, +inf) |

### `Ho^[3+]` + 2-Hydroxybenzoic acid (Salicylic acid) — 1 measurement(s)
metal_id: metal_73 | ligand_id: ligand_9257
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_160330 | *** | beta_def_194 | ΔS | 96.7 | 25 | 0.1 | `[M] + [HL]^2 <=> [M(HL)2]` | *** | [HL] | (-13.4, HL, 2.8) |

### `Tm^[3+]` + 2-Hydroxybenzoic acid (Salicylic acid) — 1 measurement(s)
metal_id: metal_192 | ligand_id: ligand_9257
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_160342 | *** | beta_def_194 | ΔS | 96.2 | 25 | 0.1 | `[M] + [HL]^2 <=> [M(HL)2]` | *** | [HL] | (-13.4, HL, 2.8) |

---

### Step 41: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.ligand_id = ligand_9257 AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### `Cu^[2+]` + Benzene-1,2-dicarboxylic acid (Phthalic acid) — 3 measurement(s)
metal_id: metal_41 | ligand_id: ligand_8938
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_154479 | *** | beta_def_840 | ΔS | 157.3 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (4.92, L, +inf) |
| vlm_154472 | *** | beta_def_812 | ΔS | 105 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (4.92, L, +inf) |
| vlm_154473 | *** | beta_def_812 | ΔS | 96.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (4.92, L, +inf) |

### `Yb^[3+]` + 2-Hydroxybenzoic acid (Salicylic acid) — 1 measurement(s)
metal_id: metal_206 | ligand_id: ligand_9257
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_160348 | *** | beta_def_194 | ΔS | 128.9 | 25 | 0.1 | `[M] + [HL]^2 <=> [M(HL)2]` | *** | [HL] | (-13.4, HL, 2.8) |

### `H^[+]` + Benzene-1,2-dicarboxylic acid (Phthalic acid) — 2 measurement(s)
metal_id: metal_68 | ligand_id: ligand_8938
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_154376 | *** | beta_def_79 | ΔS | 110.9 | 25 | 0 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (2.76, HL, 4.92, L, +inf) |
| vlm_154377 | *** | beta_def_79 | ΔS | 100 | 25 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (2.76, HL, 4.92, L, +inf) |

### `Lu^[3+]` + 2-Hydroxybenzoic acid (Salicylic acid) — 1 measurement(s)
metal_id: metal_81 | ligand_id: ligand_9257
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_160354 | *** | beta_def_194 | ΔS | 101.7 | 25 | 0.1 | `[M] + [HL]^2 <=> [M(HL)2]` | *** | [HL] | (-13.4, HL, 2.8) |

### `Zn^[2+]` + Benzene-1,2-dicarboxylic acid (Phthalic acid) — 1 measurement(s)
metal_id: metal_208 | ligand_id: ligand_8938
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_154494 | *** | beta_def_812 | ΔS | 100.8 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (4.92, L, +inf) |

### `Ho^[3+]` + 2-Hydroxybenzoic acid (Salicylic acid) — 1 measurement(s)
metal_id: metal_73 | ligand_id: ligand_9257
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_160330 | *** | beta_def_194 | ΔS | 96.7 | 25 | 0.1 | `[M] + [HL]^2 <=> [M(HL)2]` | *** | [HL] | (-13.4, HL, 2.8) |

### `Tm^[3+]` + 2-Hydroxybenzoic acid (Salicylic acid) — 1 measurement(s)
metal_id: metal_192 | ligand_id: ligand_9257
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_160342 | *** | beta_def_194 | ΔS | 96.2 | 25 | 0.1 | `[M] + [HL]^2 <=> [M(HL)2]` | *** | [HL] | (-13.4, HL, 2.8) |

---

### Step 42: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_9257 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K')",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 30
}
```

[summary]
## search_stability — 13 row(s)

### `Fe^[3+]` + 2-Hydroxybenzoic acid (Salicylic acid) — 11 measurement(s)
metal_id: metal_61 | ligand_id: ligand_9257
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_160412 | ref_eq_map_23105 | beta_def_779 | logK | 4.4 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (-13.4, HL, 2.8) |
| vlm_160398 | ref_eq_map_23105 | beta_def_821 | logK | 2.9 | 25 | 0.1 | `[M] + [HL] <=> [ML] + [H]` | *** | [HL] | (-13.4, HL, 2.8) |
| vlm_160400 | ref_eq_map_23108 | beta_def_821 | logK | 2.85 | 25 | 0.5 | `[M] + [HL] <=> [ML] + [H]` | *** | [HL] | (-13.4, HL, 2.8) |
| vlm_160402 | ref_eq_map_23110 | beta_def_821 | logK | 2.73 | 20 | 1 | `[M] + [HL] <=> [ML] + [H]` | *** | [HL] | (-13.4, HL, 2.8) |
| vlm_160401 | ref_eq_map_23109 | beta_def_821 | logK | 2.7 | 25 | 1 | `[M] + [HL] <=> [ML] + [H]` | *** | [HL] | (-13.4, HL, 2.8) |
| vlm_160403 | ref_eq_map_23107 | beta_def_821 | logK | 2.69 | 25 | 3 | `[M] + [HL] <=> [ML] + [H]` | *** | [HL] | (-13.4, HL, 2.8) |
| vlm_160411 | ref_eq_map_23107 | beta_def_846 | logK | -1.5 | 25 | 3 | `[ML] + [HL] <=> [ML2] + [H]` | *** | [HL] | (-13.4, HL, 2.8) |
| vlm_160409 | ref_eq_map_23105 | beta_def_846 | logK | -1.7 | 25 | 0.1 | `[ML] + [HL] <=> [ML2] + [H]` | *** | [HL] | (-13.4, HL, 2.8) |
| vlm_160410 | ref_eq_map_23106 | beta_def_846 | logK | -1.7 | 20 | 0.1 | `[ML] + [HL] <=> [ML2] + [H]` | *** | [HL] | (-13.4, HL, 2.8) |
| vlm_160399 | ref_eq_map_23106 | beta_def_821 | logK | -2.74 | 20 | 0.1 | `[M] + [HL] <=> [ML] + [H]` | *** | [HL] | (-13.4, HL, 2.8) |
| vlm_160404 | ref_eq_map_23111 | beta_def_821 | logK | -3.85 | 25 | 0 | `[M] + [HL] <=> [ML] + [H]` | *** | [HL] | (-13.4, HL, 2.8) |

### `Fe^[2+]` + 2-Hydroxybenzoic acid (Salicylic acid) — 2 measurement(s)
metal_id: metal_62 | ligand_id: ligand_9257
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_160374 | ref_eq_map_23094 | beta_def_821 | logK | -6.8 | 20 | 0.1 | `[M] + [HL] <=> [ML] + [H]` | *** | [HL] | (-13.4, HL, 2.8) |
| vlm_160375 | ref_eq_map_23094 | beta_def_846 | logK | -8.9 | 20 | 0.1 | `[ML] + [HL] <=> [ML2] + [H]` | *** | [HL] | (-13.4, HL, 2.8) |

---

### Step 43: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id = ligand_6165 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 14 row(s)

### `Fe^[3+]` + Nitrilotriacetic acid (NTA) — 14 measurement(s)
metal_id: metal_61 | ligand_id: ligand_6165
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CN(CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_105558 | ref_eq_map_3756 | beta_def_840 | logK | 24.3 | 20 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.46, L, +inf) |
| vlm_105557 | ref_eq_map_3754 | beta_def_840 | logK | 24 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.46, L, +inf) |
| vlm_105553 | ref_eq_map_3754 | beta_def_812 | logK | 15.9 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.46, L, +inf) |
| vlm_105554 | ref_eq_map_3755 | beta_def_812 | logK | 14.78 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.46, L, +inf) |
| vlm_105566 | ref_eq_map_3754 | beta_def_263 | logK | 10.72 | 25 | 0.1 | `[M(OH)3L] + [H] <=> [M(OH)2L] + [H2O]` | *** |  |  |
| vlm_105559 | ref_eq_map_3755 | beta_def_788 | logK | 0.9 | 25 | 1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_105568 | ref_eq_map_3755 | beta_def_423 | logK | 0 | 25 | 1 | `[ML]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2` | *** |  |  |
| vlm_105562 | ref_eq_map_3757 | beta_def_966 | logK | -3.98 | 25 | 0.5 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_105567 | ref_eq_map_3755 | beta_def_427 | logK | -4 | 25 | 1 | `[M(OH)L]^2 <=> [M2(OH)2L2]` | *** |  |  |
| vlm_105561 | ref_eq_map_3756 | beta_def_966 | logK | -4.1 | 20 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_105560 | ref_eq_map_3754 | beta_def_966 | logK | -4.36 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_105563 | ref_eq_map_3755 | beta_def_966 | logK | -5 | 25 | 1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_105564 | ref_eq_map_3754 | beta_def_238 | logK | -7.58 | 25 | 0.1 | `[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]` | *** |  |  |
| vlm_105565 | ref_eq_map_3756 | beta_def_238 | logK | -7.85 | 20 | 0.1 | `[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]` | *** |  |  |

---

### Step 44: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.ligand_id = ligand_6165 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 7 row(s)

### `Fe^[2+]` + Nitrilotriacetic acid (NTA) — 7 measurement(s)
metal_id: metal_62 | ligand_id: ligand_6165
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CN(CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_105498 | ref_eq_map_3742 | beta_def_840 | logK | 11.98 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.46, L, +inf) |
| vlm_105499 | ref_eq_map_3744 | beta_def_840 | logK | 11.53 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.46, L, +inf) |
| vlm_105500 | ref_eq_map_3742 | beta_def_966 | logK | 10.82 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_105501 | ref_eq_map_3743 | beta_def_966 | logK | 10.6 | 20 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_105495 | ref_eq_map_3742 | beta_def_812 | logK | 8.9 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.46, L, +inf) |
| vlm_105496 | ref_eq_map_3743 | beta_def_812 | logK | 8.83 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.46, L, +inf) |
| vlm_105497 | ref_eq_map_3744 | beta_def_812 | logK | 8.05 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.46, L, +inf) |

---

### Step 45: `search_ligands`
**Args:**
```json
{
  "name": "acetohydroxamic"
}
```

[summary]
## search_ligands — 25 result(s)

**stats:** 28 SQL matches · showing 25 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5938 | (Carboxymethylamino)acetohydroxamic acid | H2L | Amino Acids | 11 | `O=C(O)CNCC(=O)NO` | (-inf, H3L, -1.8, H2L, 6.99, HL, 9.09, L, +inf) |
| ligand_6020 | N-(Carboxymethyl)-N-(2-hydroxyethyl)aminoacetohyd… | H2L | Amino Acids | 9 | `O=C(O)CN(CCO)CC(=O)NO` | (-inf, H2L, 5.69, HL, 9.18, L, +inf) |
| ligand_6036 | N,N'-Bis(carboxymethyl)ethylenedinitrilo-N,N'-dia… | H4L | Amino Acids | 24 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)NO)CC(=O)NO` | (-inf, H5L, -1.6, H4L, 3.48, H3L, 6.67, H2L, 9, HL, 9.93, L, +inf) |
| ligand_6054 | N,N'-Bis(carboxymethyl)ethylenedinitrilobis(N-2-p… | H4L | Amino Acids | 8 | `CC(C)N(O)C(=O)CN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O` | (-inf, H4L, 4.2, H3L, 8.03, H2L, 9.67, HL, 10.56, L, +inf) |
| ligand_6057 | N,N',N''-Tris(carboxymethyl)diethylenetrinitrilob… | H5L | Amino Acids | 9 | `CC(C)N(O)C(=O)CN(CCN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O)CC(=O)O` | (-inf, H5L, 3.7, H4L, 5.94, H3L, 9.07, H2L, 10.1, HL, 10.85, L, +inf) |
| ligand_6203 | N,N-Bis(carboxymethyl)aminoacetohydroxamic acid | H3L | NTA and derivatives | 11 | `O=C(O)CN(CC(=O)O)CC(=O)NO` | (-inf, H3L, 2.44, H2L, 6.16, HL, 9.42, L, +inf) |
| ligand_6982 | Aminoacetohydroxamic acid (Glycinehydroxamic acid) | HL | Aliphatic amines | 51 | `NCC(=O)NO` | (-inf, H2L, 7.45, HL, 9.18, L, +inf) |
| ligand_6992 | Methylaminoacetohydrox… (Sarcosinehydroxamic acid) | HL | Aliphatic amines seconda… | 14 | `CNCC(=O)NO` | (-inf, H2L, 7.62, HL, 9.2, L, +inf) |
| ligand_7154 | Iminodiacetohydroxamic acid | H2L | Aliphatic amines seconda… | 9 | `O=C(CNCC(=O)NO)NO` | (-inf, H3L, 5.66, H2L, 7.23, HL, 10.8, L, +inf) |
| ligand_7282 | N,N-Bis(2-hydroxyethyl)aminoacetohydroxamic acid | HL | Aliphatic amines tertiar… | 8 | `O=C(CCN(CCO)CCO)NO` | (-inf, H2L, 5.37, HL, 8.97, L, +inf) |
| ligand_7295 | Nitrilotriacetohydroxamic acid | H3L | Aliphatic amines tertiar… | 49 | `O=C(CN(CC(=O)NO)CC(=O)NO)NO` | (-inf, H4L, 5.92, H3L, 6.81, H2L, 8.84, HL, 8.84, L, +inf) |
| ligand_7320 | Ethylenedinitrilotetraacetohydroxamic acid | H4L | Aliphatic amines tertiar… | 16 | `O=C(CN(CCN(CC(=O)NO)CC(=O)NO)CC(=O)NO)NO` | (-inf, H6L, 5.55, H5L, 6.05, H4L, 6.67, H3L, 7.23, H2L, 10.6, HL, 10.6, L, +inf) |
| ligand_7391 | Piperazine-N,N'-diacetohydroxamic acid | H2L | Cyclic amines  | 11 | `O=C(CN1CCN(C(=O)NO)CC1)NO` | (-inf, H4L, -1.5, H3L, 5.52, H2L, 8.4, HL, 9.8, L, +inf) |
| ligand_7709 | 5,7-Dioxo-1,4,8,11-tetraazacyclotetradecane-4,8-b… | H2L | Aza-oxo-macrocycles | 9 | `CN(O)C(=O)CN1CCNCCCNCCN(CC(=O)N(C)O)C(=O)CC1=O` | (-inf, H4L, 4.02, H3L, 6.67, H2L, 8.39, HL, 9.46, L, +inf) |
| ligand_9873 | Acetohydroxamic acid | HL | miscellaneous hydroxamic… | 66 | `CC(=O)NO` | (-inf, HL, 9.29, L, +inf) |
| ligand_9875 | N-Methylacetohydroxamic acid | HL | miscellaneous hydroxamic… | 6 | `CC(=O)N(C)O` | (-inf, HL, 8.63, L, +inf) |
| ligand_9876 | N-Phenylacetohydroxamic acid | HL | miscellaneous hydroxamic… | 7 | `CC(=O)N(O)c1ccccc1` | (-inf, HL, 8.33, L, +inf) |
| ligand_9877 | N-(4-Methylphenyl)acetohydroxamic acid | HL | miscellaneous hydroxamic… | 6 | `CC(=O)N(O)c1ccc(C)cc1` | (-inf, HL, 8.7, L, +inf) |
| ligand_9878 | N-(3-Cyanophenyl)acetohydroxamic acid | HL | miscellaneous hydroxamic… | 6 | `CC(=O)N(O)c1cccc(C#N)c1` | (-inf, HL, 8.15, L, +inf) |
| ligand_9879 | N-(4-Cyanophenyl)acetohydroxamic acid | HL | miscellaneous hydroxamic… | 6 | `CC(=O)N(O)c1ccc(C#N)cc1` | (-inf, HL, 8.14, L, +inf) |
| ligand_9880 | N-(4-Chlorophenyl)acetohydroxamic acid | HL | miscellaneous hydroxamic… | 6 | `CC(=O)N(O)c1ccc(Cl)cc1` | (-inf, HL, 8.26, L, +inf) |
| ligand_9881 | N-(3-Iodophenyl)acetohydroxamic acid | HL | miscellaneous hydroxamic… | 6 | `CC(=O)N(O)c1cccc(I)c1` | (-inf, HL, 8.2, L, +inf) |
| ligand_9882 | N-(4-Iodophenyl)acetohydroxamic acid | HL | miscellaneous hydroxamic… | 6 | `CC(=O)N(O)c1ccc(I)cc1` | (-inf, HL, 8.18, L, +inf) |
| ligand_9883 | N-(3-Acetylphenyl)acetohydroxamic acid | HL | miscellaneous hydroxamic… | 6 | `CC(=O)c1cccc(N(O)C(C)=O)c1` | (-inf, HL, 8.23, L, +inf) |
| ligand_11339 | Phenylacetohydroxamic acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (24 parseable SMILES)

| group | count | % |
|-------|-------|---|
| amide | 24 | 100% |
| hydroxyl | 24 | 100% |
| tertiary_amine | 9 | 38% |
| aromatic_ring | 8 | 33% |
| carboxyl | 6 | 25% |
| secondary_amine | 4 | 17% |
| halide | 3 | 12% |
| nitrile | 2 | 8% |
| ketone | 1 | 4% |
| primary_amine | 1 | 4% |

---

### Step 46: `search_ligands`
**Args:**
```json
{
  "name": "gluconic"
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8668 | D-gluco-Pentahydroxyhexanoic ac… (D-Gluconic acid) | HL | Carboxylic acids hydroxy | 62 | `O=C(O)[C@H](O)[C@@H](O)[C@H](O)[C@H](O)CO` | (-inf, HL, 3.46, L, +inf) |
| ligand_10317 | 6-[Bis(1-methylethyl)aminoacetyl]… (Pangamic acid) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| hydroxyl | 1 | 100% |

---

### Step 47: `search_ligands`
**Args:**
```json
{
  "name": "phosphoric"
}
```

[summary]
## search_ligands — 25 result(s)

**stats:** 43 SQL matches · showing 25 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9150 | Phosphoric acid methyl ester (Methyl phosphate) | H2L | Organophosphorus and ars… | 12 | `COP(=O)(O)O` | (-inf, HL, 6.25, L, +inf) |
| ligand_9151 | Phosphoric acid butyl ester (Butyl phosphate) | H2L | Organophosphorus and ars… | 11 | `CCCCOP(=O)(O)O` | (-inf, HL, 6.72, L, +inf) |
| ligand_9152 | Phosphoric acid phenyl ester (Phenyl phosphate) | H2L | Organophosphorus and ars… | 24 | `O=P(O)(O)Oc1ccccc1` | (-inf, H2L, -0.9, HL, 5.78, L, +inf) |
| ligand_9153 | Phosphoric acid 4-nitro… (4-Nitrophenyl phosphate) | H2L | Organophosphorus and ars… | 4 | `O=[N+]([O-])c1ccc(OP(=O)(O)O)cc1` | (-inf, HL, 5.01, L, +inf) |
| ligand_9154 | Phosphoric acid 1-naph… (alpha-Naphthyl phosphate) | H2L | Organophosphorus and ars… | 18 | `O=P(O)(O)Oc1cccc2ccccc12` | (-inf, H2L, -0.9, HL, 5.74, L, +inf) |
| ligand_9155 | Phosphoric acid 2-napht… (beta-Naphthyl phosphate) | H2L | Organophosphorus and ars… | 6 | `O=P(O)(O)Oc1ccc2ccccc2c1` | (-inf, H2L, -1.2, HL, 5.74, L, +inf) |
| ligand_9156 | Phosphoric acid 4-nitro… (p-Nitrophenyl phosphate) | H2L | Organophosphorus and ars… | 18 | `O=[N+]([O-])c1ccc(OP(=O)(O)O)cc1` | (-inf, HL, 5.02, L, +inf) |
| ligand_9163 | Phosphoric acid dibutyl ester (Dibutyl phosphate) | HL | Organophosphorus and ars… | 1 | `CCCCOP(=O)(O)OCCCC` | (-inf, HL, 1, L, +inf) |
| ligand_9165 | Diphosphoric acid methyl est… (Methyl diphosphate) | H3L | Organophosphorus and ars… | 9 | `COP(=O)(O)OP(=O)(O)O` | (-inf, H2L, -1.6, HL, 6.37, L, +inf) |
| ligand_9166 | Diphosphoric acid butyl ester (Butyl diphosphate) | H3L | Organophosphorus and ars… | 12 | `CCCCOP(=O)(O)OP(=O)(O)O` | (-inf, H2L, -1.3, HL, 6.65, L, +inf) |
| ligand_9167 | Diphosphoric acid phenyl est… (Phenyl diphosphate) | H3L | Organophosphorus and ars… | 12 | `O=P(O)(O)OP(=O)(O)Oc1ccccc1` | (-inf, H2L, -1.3, HL, 6.32, L, +inf) |
| ligand_9168 | Triphosphoric acid methyl e… (Methyl triphosphate) | H4L | Organophosphorus and ars… | 3 | `COP(=O)(O)OP(=O)(O)OP(=O)(O)O` | (-inf, HL, 6.45, L, +inf) |
| ligand_9173 | Phosphorodithioic … (Dibutyldithiophosphoric acid) | HL | Organophosphorus and ars… | 2 | `CCCCOP(=S)(S)OCCCC` | (-inf, HL, 0.08, L, +inf) |
| ligand_9174 | Phosphorodithio… (Diisobutyldithiophosphoric acid) | HL | Organophosphorus and ars… | 2 | `CC(C)COP(=S)(S)OCC(C)C` | (-inf, HL, -0.04, L, +inf) |
| ligand_10113 | Hydrogen phosphate (Phosphoric acid) | H3L | Inorganic ligands | 359 | `O=P(O)(O)O` | (-inf, H3L, 1.92, H2L, 6.71, HL, 11.52, L, +inf) |
| ligand_10114 | Hydrogen diphosphate (Pyrophosphoric acid) | H4L | Inorganic ligands | 211 | `O=P(O)(O)OP(=O)(O)O` | (-inf, H4L, -0.8, H3L, -0.8, H2L, 5.94, HL, 8.25, L, +inf) |
| ligand_10116 | Hydrogen hypophosphate (Hypophosphoric acid) | H4L | Inorganic ligands | 5 | `O=P(O)(O)P(=O)(O)O` | (-inf, H3L, 2.1, H2L, 6.77, HL, 9.48, L, +inf) |
| ligand_10117 | Hydrogen triphosphate (Triphosphoric acid) | H5L | Inorganic ligands | 176 | `O=P(O)(O)OP(=O)(O)OP(=O)(O)O` | (-inf, H5L, -0.5, H4L, -0.5, H3L, -0.9, H2L, 5.42, HL, 7.77, L, +inf) |
| ligand_10119 | Hydrogen tetraphosphate (Tetraphosphoric acid) | H6L | Inorganic ligands | 40 | `O=P(O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O` | (-inf, H2L, 5.84, HL, 7.43, L, +inf) |
| ligand_10120 | Hydrogen pentaphosphate (Pentaphosphoric acid) | H6L | Inorganic ligands | 2 | `O=P(O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O` | (-inf, H2L, 7.03, HL, 8.15, L, +inf) |
| ligand_10121 | Hydrogen hexaphosphate (Hexaphosphoric acid) | H7L | Inorganic ligands | 2 | `O=P(O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O[PH](O)(O)OP(=O)(O)O` | (-inf, H2L, 7.16, HL, 8.12, L, +inf) |
| ligand_10122 | Hydrogen heptaphosphate (Heptaphosphoric acid) | H8L | Inorganic ligands | 2 | `O=P(O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O[PH](O)(O)O[PH](O)(O)OP(=O)(O)O` | (-inf, H2L, 7.18, HL, 8.07, L, +inf) |
| ligand_10123 | Hydrogen trimetaphosphate (Trimetaphosphoric acid) | H3L | Inorganic ligands | 37 | `O=P1(O)OP(=O)(O)OP(=O)(O)O1` | (-inf, HL, 2.05, L, +inf) |
| ligand_10124 | Hydrogen tetrametaphos… (Tetrametaphosphoric acid) | H4L | Inorganic ligands | 37 | `O=P1(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O1` | (-inf, HL, -1.9, L, +inf) |
| ligand_10125 | Hydrogen hexametaphosph… (Hexametaphosphoric acid) | H6L | Inorganic ligands | 7 | `O=P1(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O1` | (-inf, HL, 3.7, L, +inf) |

### Functional groups across all SQL matches (28 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 26 | 93% |
| phosphate | 23 | 82% |
| aromatic_ring | 6 | 21% |
| secondary_amine | 2 | 7% |
| tertiary_amine | 2 | 7% |
| thiol | 2 | 7% |

---

### Step 48: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10113 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 14 row(s)

### `Fe^[3+]` + Hydrogen phosphate (Phosphoric acid) — 9 measurement(s)
metal_id: metal_61 | ligand_id: ligand_10113
ligand_HxL_def: H3L | ligand_SMILES: O=P(O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_174470 | ref_eq_map_28587 | beta_def_779 | logK | 8.3 | 25 | 0.5 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (6.71, HL, 11.52) |
| vlm_174475 | ref_eq_map_28586 | beta_def_172 | logK | 8.1 | 25 | 3 | `[M] + [H2L]^3 <=> [M(H2L)3]` | *** | [H2L] | (1.92, H2L, 6.71) |
| vlm_174471 | ref_eq_map_28586 | beta_def_779 | logK | 7.5 | 25 | 3 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (6.71, HL, 11.52) |
| vlm_174474 | ref_eq_map_28586 | beta_def_156 | logK | 6.03 | 25 | 3 | `[M] + [H2L]^2 <=> [M(H2L)2]` | *** | [H2L] | (1.92, H2L, 6.71) |
| vlm_174472 | ref_eq_map_28587 | beta_def_732 | logK | 3.47 | 25 | 0.5 | `[M] + [H2L] <=> [MH2L]` | *** | [H2L] | (1.92, H2L, 6.71) |
| vlm_174473 | ref_eq_map_28586 | beta_def_732 | logK | 3.47 | 25 | 3 | `[M] + [H2L] <=> [MH2L]` | *** | [H2L] | (1.92, H2L, 6.71) |
| vlm_174476 | ref_eq_map_28586 | beta_def_751 | logK | 0.6 | 25 | 3 | `[MH2L] + [H] <=> [MH3L]` | *** |  |  |
| vlm_174478 | ref_eq_map_28586 | beta_def_305 | logK | -21.76 | 25 | 3 | `[ML(H2O)2(s,am)] <=> [M] + [L] + [H2O]^2` | solid | [L] | (11.52, L, +inf) |
| vlm_174477 | ref_eq_map_28585 | beta_def_304 | logK | -26.4 | 25 | 0 | `[ML(H2O)2(s)] <=> [M] + [L] + [H2O]^2` | solid | [L] | (11.52, L, +inf) |

### `Fe^[2+]` + Hydrogen phosphate (Phosphoric acid) — 5 measurement(s)
metal_id: metal_62 | ligand_id: ligand_10113
ligand_HxL_def: H3L | ligand_SMILES: O=P(O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_174448 | ref_eq_map_28575 | beta_def_171 | logK | 5.29 | 25 | 3 | `[MH3L2] + [H] <=> [M(H2L)2]` | *** |  |  |
| vlm_174445 | ref_eq_map_28575 | beta_def_779 | logK | 2.46 | 25 | 3 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (6.71, HL, 11.52) |
| vlm_174447 | ref_eq_map_28575 | beta_def_156 | logK | 1.82 | 25 | 3 | `[M] + [H2L]^2 <=> [M(H2L)2]` | *** | [H2L] | (1.92, H2L, 6.71) |
| vlm_174446 | ref_eq_map_28575 | beta_def_732 | logK | 0.55 | 25 | 3 | `[M] + [H2L] <=> [MH2L]` | *** | [H2L] | (1.92, H2L, 6.71) |
| vlm_174449 | ref_eq_map_28574 | beta_def_623 | logK | -37.76 | 25 | 0 | `[M3L2(H2O)8(s,vivianite)] <=> [M]^3 + [L]^2 + [H2O]^8` | solid | [L] | (11.52, L, +inf) |

---

### Step 49: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_8668 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 5 row(s)

### `Fe^[3+]` + D-gluco-Pentahydroxyhexanoic acid (D-Gluconic acid) — 4 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8668
ligand_HxL_def: HL | ligand_SMILES: O=C(O)[C@H](O)[C@@H](O)[C@H](O)[C@H](O)CO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_149280 | ref_eq_map_18879 | beta_def_187 | logK | 13.3 | 25 | 1 | `[M(OH)(H-3L)] + [H] <=> [M(H-3L)] + [H2O]` | *** |  |  |
| vlm_149278 | ref_eq_map_18879 | beta_def_831 | logK | 4.6 | 25 | 1 | `[M(H-2L)] + [H]^2 <=> [ML]` | *** |  |  |
| vlm_149279 | ref_eq_map_18879 | beta_def_153 | logK | 4 | 25 | 1 | `[M(H-3L)] + [H] <=> [M(H-2L)]` | *** |  |  |
| vlm_149277 | ref_eq_map_18879 | beta_def_812 | logK | 3.1 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.46, L, +inf) |

### `Fe^[2+]` + D-gluco-Pentahydroxyhexanoic acid (D-Gluconic acid) — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8668
ligand_HxL_def: HL | ligand_SMILES: O=C(O)[C@H](O)[C@@H](O)[C@H](O)[C@H](O)CO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_149274 | ref_eq_map_18877 | beta_def_812 | logK | -1 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.46, L, +inf) |

---

### Step 50: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10114 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### `Ac^[3+]` + Hydrogen phosphate (Phosphoric acid) — 1 measurement(s)
metal_id: metal_1 | ligand_id: ligand_10113
ligand_HxL_def: H3L | ligand_SMILES: O=P(O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_174423 | ref_eq_map_28566 | beta_def_732 | logK | 1.59 | 25 | 0.5 | `[M] + [H2L] <=> [MH2L]` | *** | [H2L] | (1.92, H2L, 6.71) |

### `Ag^[+]` + Hydrogen phosphate (Phosphoric acid) — 5 measurement(s)
metal_id: metal_2 | ligand_id: ligand_10113
ligand_HxL_def: H3L | ligand_SMILES: O=P(O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_174492 | ref_eq_map_28594 | beta_def_739 | logK | 5.39 | 25 | 3 | `[MHL] + [H] <=> [MH2L]` | *** |  |  |
| vlm_174493 | ref_eq_map_28594 | beta_def_756 | logK | 4.45 | 25 | 3 | `[M(HL)2] + [H] <=> [MH3L2]` | *** |  |  |
| vlm_174491 | ref_eq_map_28594 | beta_def_156 | logK | -0.1 | 25 | 3 | `[M] + [H2L]^2 <=> [M(H2L)2]` | *** | [H2L] | (1.92, H2L, 6.71) |
| vlm_174490 | ref_eq_map_28594 | beta_def_732 | logK | -0.17 | 25 | 3 | `[M] + [H2L] <=> [MH2L]` | *** | [H2L] | (1.92, H2L, 6.71) |
| vlm_174494 | ref_eq_map_28593 | beta_def_621 | logK | -17.59 | 25 | 0 | `[M3L(s)] <=> [M]^3 + [L]` | solid | [L] | (11.52, L, +inf) |

### `Al^[3+]` + Hydrogen diphosphate (Pyrophosphoric acid) — 4 measurement(s)
metal_id: metal_5 | ligand_id: ligand_10114
ligand_HxL_def: H4L | ligand_SMILES: O=P(O)(O)OP(=O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_174772 | ref_eq_map_28683 | beta_def_840 | logK | 19.77 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (8.25, L, +inf) |
| vlm_174771 | ref_eq_map_28683 | beta_def_812 | logK | 13.74 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (8.25, L, +inf) |
| vlm_174773 | ref_eq_map_28683 | beta_def_779 | logK | 8.8 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (5.94, HL, 8.25) |
| vlm_174775 | ref_eq_map_28683 | beta_def_966 | logK | 6.33 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |

### `Al^[3+]` + Hydrogen triphosphate (Triphosphoric acid) — 4 measurement(s)
metal_id: metal_5 | ligand_id: ligand_10117
ligand_HxL_def: H5L | ligand_SMILES: O=P(O)(O)OP(=O)(O)OP(=O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_174984 | ref_eq_map_28754 | beta_def_840 | logK | 19.14 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (7.77, L, +inf) |
| vlm_174983 | ref_eq_map_28754 | beta_def_812 | logK | 13.15 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (7.77, L, +inf) |
| vlm_174985 | ref_eq_map_28754 | beta_def_779 | logK | 8.89 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (5.42, HL, 7.77) |
| vlm_174987 | ref_eq_map_28754 | beta_def_966 | logK | 6.62 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |

### `Al^[3+]` + Hydrogen phosphate (Phosphoric acid) — 6 measurement(s)
metal_id: metal_5 | ligand_id: ligand_10113
ligand_HxL_def: H3L | ligand_SMILES: O=P(O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_174530 | ref_eq_map_28610 | beta_def_502 | logK | 18.72 | 37 | 0.15 | `[M]^2 + [L] <=> [M2L]` | *** | [L] | (11.52, L, +inf) |
| vlm_174529 | ref_eq_map_28609 | beta_def_502 | logK | 16.7 | 25 | 0.1 | `[M]^2 + [L] <=> [M2L]` | *** | [L] | (11.52, L, +inf) |
| vlm_174528 | ref_eq_map_28610 | beta_def_812 | logK | 15.32 | 37 | 0.15 | `[M] + [L] <=> [ML]` | *** | [L] | (11.52, L, +inf) |
| vlm_174538 | ref_eq_map_28609 | beta_def_512 | logK | 6.79 | 25 | 0.1 | `[M2(OH)2L] + [H]^2 <=> [M2L] + [H2O]^2` | *** |  |  |
| vlm_174532 | ref_eq_map_28610 | beta_def_779 | logK | 6.25 | 37 | 0.15 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (6.71, HL, 11.52) |
| vlm_174537 | ref_eq_map_28610 | beta_def_512 | logK | 6.14 | 37 | 0.15 | `[M2(OH)2L] + [H]^2 <=> [M2L] + [H2O]^2` | *** |  |  |

---

### Step 51: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id = ligand_7295)",
  "order_by": "p.pKa ASC",
  "limit": 10
}
```

[summary]
## search_pka_values — 4 row(s)

### pKa -12.0–-11.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_127316 | ligand_7295 | Nitrilotriacetohydroxamic acid | H3L | O=C(CN(CC(=O)NO)CC(=O)NO)NO | -11.74 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_6 |

### pKa 5.5–6.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_127331 | ligand_7295 | Nitrilotriacetohydroxamic acid | H3L | O=C(CN(CC(=O)NO)CC(=O)NO)NO | 5.92 | 25 | 0.1 | H3L→H4L | M_tot_1 | M_tot_1 |

### pKa 6.5–7.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_127326 | ligand_7295 | Nitrilotriacetohydroxamic acid | H3L | O=C(CN(CC(=O)NO)CC(=O)NO)NO | 6.81 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |

### pKa 8.5–9.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_127321 | ligand_7295 | Nitrilotriacetohydroxamic acid | H3L | O=C(CN(CC(=O)NO)CC(=O)NO)NO | 8.84 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |

---

### Step 52: `search_ligands`
**Args:**
```json
{
  "name": "glycolic acid"
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8640 | Hydroxyacetic acid (Glycolic acid) | HL | Carboxylic acids hydroxy | 402 | `O=C(O)CO` | (-inf, HL, 3.62, L, +inf) |
| ligand_8766 | Mercaptoacetic acid (Thioglycolic acid) | H2L | Carboxylic acids thio | 148 | `O=C(O)CS` | (-inf, H2L, 3.48, HL, 10.11, L, +inf) |
| ligand_8974 | Oxydiacetic acid (Diglycolic acid) | H2L | Carboxylic acids diacids | 363 | `O=C(O)COCC(=O)O` | (-inf, H2L, 2.82, HL, 3.94, L, +inf) |
| ligand_10907 | Acrylamidoglycolic acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 3 | 100% |
| ether | 1 | 33% |
| hydroxyl | 1 | 33% |
| thiol | 1 | 33% |

---

### Step 53: `search_ligands`
**Args:**
```json
{
  "name": "lactic acid"
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8641 | D-2-Hydroxypropanoic acid (Lactic acid) | HL | Carboxylic acids hydroxy | 349 | `CC(O)C(=O)O` | (-inf, HL, 3.67, L, +inf) |
| ligand_8660 | DL-2-Phenyl-2-hydroxypropanoic … (Atrolactic acid) | HL | Carboxylic acids hydroxy | 34 | `CC(O)(C(=O)O)c1ccccc1` | (-inf, HL, 3.53, L, +inf) |
| ligand_8767 | DL-2-Mercaptopropanoic acid (Thiolactic acid) | H2L | Carboxylic acids thio | 71 | `CC(S)C(=O)O` | (-inf, H2L, 3.48, HL, 10.08, L, +inf) |
| ligand_8976 | DL-2,2'-Oxydipropanoic acid (Dilactic acid) | H2L | Carboxylic acids diacids | 30 | `CC(OC(C)C(=O)O)C(=O)O` | *** |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| hydroxyl | 2 | 50% |
| aromatic_ring | 1 | 25% |
| ether | 1 | 25% |
| thiol | 1 | 25% |

---

### Step 54: `search_ligands`
**Args:**
```json
{
  "name": "ascorbic acid"
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9601 | L-3,4-Dihydroxy-5-(1,2-dihydrox… (L-Ascorbic acid) | H2L | cyclic ketones | 118 | `O=C1O[C@H]([C@@H](O)CO)C(O)=C1O` | (-inf, H2L, 4.02, HL, 4.02, L, +inf) |
| ligand_11203 | Dehydroascorbic acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| ester | 1 | 100% |
| hydroxyl | 1 | 100% |

---

### Step 55: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_8640 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 5 row(s)

### `Fe^[3+]` + Hydroxyacetic acid (Glycolic acid) — 4 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8640
ligand_HxL_def: HL | ligand_SMILES: O=C(O)CO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_147409 | ref_eq_map_18185 | beta_def_812 | logK | 2.9 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.62, L, +inf) |
| vlm_147411 | ref_eq_map_18185 | beta_def_136 | logK | 2.41 | 25 | 1 | `[M(H-1L)] + [L] <=> [M(H-1L)L]` | *** | [L] | (3.62, L, +inf) |
| vlm_147412 | ref_eq_map_18185 | beta_def_140 | logK | 1.5 | 25 | 1 | `[M(H-1L)L] + [L] <=> [M(H-1L)L2]` | *** | [L] | (3.62, L, +inf) |
| vlm_147410 | ref_eq_map_18185 | beta_def_107 | logK | 1.31 | 25 | 1 | `[M(H-1L)] + [H] <=> [ML]` | *** |  |  |

### `Fe^[2+]` + Hydroxyacetic acid (Glycolic acid) — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8640
ligand_HxL_def: HL | ligand_SMILES: O=C(O)CO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_147386 | ref_eq_map_18174 | beta_def_812 | logK | 1.33 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.62, L, +inf) |

---

### Step 56: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_8641 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### `Ag^[+]` + L-2-Aminopropanoic acid (Alanine) — 3 measurement(s)
metal_id: metal_2 | ligand_id: ligand_5761
ligand_HxL_def: HL | ligand_SMILES: C[C@H](N)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_94297 | ref_eq_map_209 | beta_def_812 | logK | -3.64 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.71, L, +inf) |
| vlm_94298 | ref_eq_map_209 | beta_def_840 | logK | -7.02 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.71, L, +inf) |
| vlm_94299 | ref_eq_map_210 | beta_def_840 | logK | -7.18 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.71, L, +inf) |

### `Al^[3+]` + Ethane-1,1-dicarboxylic acid (Methylmalonic acid) — 3 measurement(s)
metal_id: metal_5 | ligand_id: ligand_8874
ligand_HxL_def: H2L | ligand_SMILES: CC(C(=O)O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_152506 | ref_eq_map_20166 | beta_def_872 | logK | 12.4 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (5.38, L, +inf) |
| vlm_152505 | ref_eq_map_20166 | beta_def_840 | logK | 10 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (5.38, L, +inf) |
| vlm_152504 | ref_eq_map_20166 | beta_def_812 | logK | 5.65 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (5.38, L, +inf) |

### `Al^[3+]` + D-2-Hydroxypropanoic acid (Lactic acid) — 14 measurement(s)
metal_id: metal_5 | ligand_id: ligand_8641
ligand_HxL_def: HL | ligand_SMILES: CC(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_147807 | ref_eq_map_18330 | beta_def_834 | logK | 10.55 | 25 | 0.2 | `[M(OH)2L] + [H]^2 <=> [ML] + [H2O]^2` | *** |  |  |
| vlm_147804 | ref_eq_map_18330 | beta_def_872 | logK | 5.9 | 25 | 0.2 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (3.67, L, +inf) |
| vlm_147805 | ref_eq_map_18331 | beta_def_872 | logK | 5.8 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (3.67, L, +inf) |
| vlm_147802 | ref_eq_map_18330 | beta_def_840 | logK | 4.55 | 25 | 0.2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (3.67, L, +inf) |
| vlm_147803 | ref_eq_map_18331 | beta_def_840 | logK | 4.42 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (3.67, L, +inf) |
| vlm_147806 | ref_eq_map_18330 | beta_def_839 | logK | 4.3 | 25 | 0.2 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_147808 | ref_eq_map_18330 | beta_def_984 | logK | 3.5 | 25 | 0.2 | `[M(OH)L2] + [H] <=> [ML2] + [H2O]` | *** |  |  |
| vlm_147809 | ref_eq_map_18331 | beta_def_984 | logK | 3.45 | 25 | 0.5 | `[M(OH)L2] + [H] <=> [ML2] + [H2O]` | *** |  |  |
| vlm_147800 | ref_eq_map_18330 | beta_def_812 | logK | 2.48 | 25 | 0.2 | `[M] + [L] <=> [ML]` | *** | [L] | (3.67, L, +inf) |
| vlm_147801 | ref_eq_map_18331 | beta_def_812 | logK | 2.36 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (3.67, L, +inf) |
| vlm_147811 | ref_eq_map_18331 | beta_def_415 | logK | -3.29 | 25 | 0.5 | `[M]^2 + [L] + [H2O]^2 <=> [M2(OH)2L] + [H]^2` | *** | [L] | (3.67, L, +inf) |
| vlm_147810 | ref_eq_map_18330 | beta_def_415 | logK | -3.43 | 25 | 0.2 | `[M]^2 + [L] + [H2O]^2 <=> [M2(OH)2L] + [H]^2` | *** | [L] | (3.67, L, +inf) |
| vlm_147812 | ref_eq_map_18330 | beta_def_411 | logK | -16.64 | 25 | 0.2 | `[M]^2 + [HL]^2 + [H2O]^2 <=> [M2(OH)2(H-1L)2] + [H]^6` | *** | [HL] | (-inf, HL, 3.67) |
| vlm_147813 | ref_eq_map_18331 | beta_def_411 | logK | -16.79 | 25 | 0.5 | `[M]^2 + [HL]^2 + [H2O]^2 <=> [M2(OH)2(H-1L)2] + [H]^6` | *** | [HL] | (-inf, HL, 3.67) |

---

### Step 57: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_9601 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 3 row(s)

### `Fe^[3+]` + L-3,4-Dihydroxy-5-(1,2-dihydroxyethyl)-2,5-H-oxole-2-one (L… — 1 measurement(s)
metal_id: metal_61 | ligand_id: ligand_9601
ligand_HxL_def: H2L | ligand_SMILES: O=C1O[C@H]([C@@H](O)CO)C(O)=C1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_166776 | ref_eq_map_25795 | beta_def_194 | logK | 6.36 | 25 | 0.1 | `[M] + [HL]^2 <=> [M(HL)2]` | *** | [HL] | (-11.35, HL, 4.02) |

### `Fe^[2+]` + L-3,4-Dihydroxy-5-(1,2-dihydroxyethyl)-2,5-H-oxole-2-one (L… — 2 measurement(s)
metal_id: metal_62 | ligand_id: ligand_9601
ligand_HxL_def: H2L | ligand_SMILES: O=C1O[C@H]([C@@H](O)CO)C(O)=C1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_166768 | ref_eq_map_25789 | beta_def_788 | logK | 2.6 | 25 | 3 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_166767 | ref_eq_map_25789 | beta_def_779 | logK | 0.21 | 25 | 3 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (-11.35, HL, 4.02) |

---

### Step 58: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_8641 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### `Ag^[+]` + L-2-Aminopropanoic acid (Alanine) — 3 measurement(s)
metal_id: metal_2 | ligand_id: ligand_5761
ligand_HxL_def: HL | ligand_SMILES: C[C@H](N)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_94297 | ref_eq_map_209 | beta_def_812 | logK | -3.64 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.71, L, +inf) |
| vlm_94298 | ref_eq_map_209 | beta_def_840 | logK | -7.02 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.71, L, +inf) |
| vlm_94299 | ref_eq_map_210 | beta_def_840 | logK | -7.18 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.71, L, +inf) |

### `Al^[3+]` + Ethane-1,1-dicarboxylic acid (Methylmalonic acid) — 3 measurement(s)
metal_id: metal_5 | ligand_id: ligand_8874
ligand_HxL_def: H2L | ligand_SMILES: CC(C(=O)O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_152506 | ref_eq_map_20166 | beta_def_872 | logK | 12.4 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (5.38, L, +inf) |
| vlm_152505 | ref_eq_map_20166 | beta_def_840 | logK | 10 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (5.38, L, +inf) |
| vlm_152504 | ref_eq_map_20166 | beta_def_812 | logK | 5.65 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (5.38, L, +inf) |

### `Al^[3+]` + D-2-Hydroxypropanoic acid (Lactic acid) — 14 measurement(s)
metal_id: metal_5 | ligand_id: ligand_8641
ligand_HxL_def: HL | ligand_SMILES: CC(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_147807 | ref_eq_map_18330 | beta_def_834 | logK | 10.55 | 25 | 0.2 | `[M(OH)2L] + [H]^2 <=> [ML] + [H2O]^2` | *** |  |  |
| vlm_147804 | ref_eq_map_18330 | beta_def_872 | logK | 5.9 | 25 | 0.2 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (3.67, L, +inf) |
| vlm_147805 | ref_eq_map_18331 | beta_def_872 | logK | 5.8 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (3.67, L, +inf) |
| vlm_147802 | ref_eq_map_18330 | beta_def_840 | logK | 4.55 | 25 | 0.2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (3.67, L, +inf) |
| vlm_147803 | ref_eq_map_18331 | beta_def_840 | logK | 4.42 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (3.67, L, +inf) |
| vlm_147806 | ref_eq_map_18330 | beta_def_839 | logK | 4.3 | 25 | 0.2 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_147808 | ref_eq_map_18330 | beta_def_984 | logK | 3.5 | 25 | 0.2 | `[M(OH)L2] + [H] <=> [ML2] + [H2O]` | *** |  |  |
| vlm_147809 | ref_eq_map_18331 | beta_def_984 | logK | 3.45 | 25 | 0.5 | `[M(OH)L2] + [H] <=> [ML2] + [H2O]` | *** |  |  |
| vlm_147800 | ref_eq_map_18330 | beta_def_812 | logK | 2.48 | 25 | 0.2 | `[M] + [L] <=> [ML]` | *** | [L] | (3.67, L, +inf) |
| vlm_147801 | ref_eq_map_18331 | beta_def_812 | logK | 2.36 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (3.67, L, +inf) |
| vlm_147811 | ref_eq_map_18331 | beta_def_415 | logK | -3.29 | 25 | 0.5 | `[M]^2 + [L] + [H2O]^2 <=> [M2(OH)2L] + [H]^2` | *** | [L] | (3.67, L, +inf) |
| vlm_147810 | ref_eq_map_18330 | beta_def_415 | logK | -3.43 | 25 | 0.2 | `[M]^2 + [L] + [H2O]^2 <=> [M2(OH)2L] + [H]^2` | *** | [L] | (3.67, L, +inf) |
| vlm_147812 | ref_eq_map_18330 | beta_def_411 | logK | -16.64 | 25 | 0.2 | `[M]^2 + [HL]^2 + [H2O]^2 <=> [M2(OH)2(H-1L)2] + [H]^6` | *** | [HL] | (-inf, HL, 3.67) |
| vlm_147813 | ref_eq_map_18331 | beta_def_411 | logK | -16.79 | 25 | 0.5 | `[M]^2 + [HL]^2 + [H2O]^2 <=> [M2(OH)2(H-1L)2] + [H]^6` | *** | [HL] | (-inf, HL, 3.67) |

---

### Step 59: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id = ligand_6277 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 6 row(s)

### `Fe^[3+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 6 measurement(s)
metal_id: metal_61 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108639 | ref_eq_map_5028 | beta_def_812 | logK | 25.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108640 | ref_eq_map_5029 | beta_def_812 | logK | 23.8 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108647 | ref_eq_map_5029 | beta_def_966 | logK | 7.53 | 25 | 1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_108646 | ref_eq_map_5028 | beta_def_966 | logK | 7.39 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_108650 | ref_eq_map_5029 | beta_def_427 | logK | 2.8 | 25 | 1 | `[M(OH)L]^2 <=> [M2(OH)2L2]` | *** |  |  |
| vlm_108643 | ref_eq_map_5028 | beta_def_788 | logK | -1.3 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |

---

### Step 60: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.ligand_id = ligand_6277 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 2 row(s)

### `Fe^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 2 measurement(s)
metal_id: metal_62 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108566 | ref_eq_map_5014 | beta_def_812 | logK | 14.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108569 | ref_eq_map_5014 | beta_def_786 | logK | 6.82 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (6.13, HL, 9.52) |

---

### Step 61: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id = ligand_8191 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 7 row(s)

### `Fe^[3+]` + 1,10-Phenanthroline (Dipyridino[a,c]benzene) — 7 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8191
ligand_HxL_def: L | ligand_SMILES: c1cnc2c(c1)ccc1cccnc12

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_139323 | ref_eq_map_15189 | beta_def_872 | logK | 14.6 | 25 | 1.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (4.92, L, +inf) |
| vlm_139322 | ref_eq_map_15188 | beta_def_872 | logK | 14.1 | 25 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (4.92, L, +inf) |
| vlm_139324 | ref_eq_map_15190 | beta_def_872 | logK | 13.8 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (4.92, L, +inf) |
| vlm_139321 | ref_eq_map_15188 | beta_def_840 | logK | 11.4 | 20 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (4.92, L, +inf) |
| vlm_139320 | ref_eq_map_15188 | beta_def_812 | logK | 6.5 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (4.92, L, +inf) |
| vlm_139327 | ref_eq_map_15188 | beta_def_587 | logK | 6.5 | 20 | 0.1 | `[M2(OH)L4] + [H] <=> [M2L4] + [H2O]` | *** |  |  |
| vlm_139328 | ref_eq_map_15188 | beta_def_588 | logK | 4.4 | 20 | 0.1 | `[M2(OH)2L4] + [H] <=> [M2(OH)L4] + [H2O]` | *** |  |  |

---

### Step 62: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.ligand_id = ligand_8191 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 5 row(s)

### `Fe^[2+]` + 1,10-Phenanthroline (Dipyridino[a,c]benzene) — 5 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8191
ligand_HxL_def: L | ligand_SMILES: c1cnc2c(c1)ccc1cccnc12

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_139269 | ref_eq_map_15178 | beta_def_872 | logK | 21 | 25 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (4.92, L, +inf) |
| vlm_139270 | ref_eq_map_15179 | beta_def_872 | logK | 21 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (4.92, L, +inf) |
| vlm_139268 | ref_eq_map_15178 | beta_def_840 | logK | 11.15 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (4.92, L, +inf) |
| vlm_139266 | ref_eq_map_15178 | beta_def_812 | logK | 5.85 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (4.92, L, +inf) |
| vlm_139267 | ref_eq_map_15179 | beta_def_812 | logK | -5.87 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (4.92, L, +inf) |

---

### Step 63: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id = ligand_5937 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 5 row(s)

### `Fe^[3+]` + N-(Phosphonomethyl)glycine (Glyphosate) — 5 measurement(s)
metal_id: metal_61 | ligand_id: ligand_5937
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CNCP(=O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_99818 | ref_eq_map_1596 | beta_def_840 | logK | 23 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (10.1, L, +inf) |
| vlm_99817 | ref_eq_map_1596 | beta_def_812 | logK | 16.09 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (10.1, L, +inf) |
| vlm_99821 | ref_eq_map_1596 | beta_def_238 | logK | 8.91 | 25 | 0.1 | `[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]` | *** |  |  |
| vlm_99820 | ref_eq_map_1596 | beta_def_966 | logK | 5.78 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_99819 | ref_eq_map_1596 | beta_def_788 | logK | 1.54 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |

---

### Step 64: `search_ligands`
**Args:**
```json
{
  "name": "malonic acid"
}
```

[summary]
## search_ligands — 25 result(s)

**stats:** 36 SQL matches · showing 25 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5801 | Aminopropanedioic acid (Aminomalonic acid) | H2L | Amino Acids | 14 | `NC(C(=O)O)C(=O)O` | (-inf, H3L, -1.8, H2L, 2.94, HL, 9.22, L, +inf) |
| ligand_5808 | (3-Aminopropyl)malonic acid | H2L | Amino Acids | 18 | `NCCCC(C(=O)O)C(=O)O` | (-inf, H3L, 2.52, H2L, 4.86, HL, 10.45, L, +inf) |
| ligand_8873 | Propanedioic acid (Malonic acid) | H2L | Carboxylic acids diacids | 505 | `O=C(O)CC(=O)O` | (-inf, H2L, 2.65, HL, 5.27, L, +inf) |
| ligand_8874 | Ethane-1,1-dicarboxylic acid (Methylmalonic acid) | H2L | Carboxylic acids diacids | 71 | `CC(C(=O)O)C(=O)O` | (-inf, H2L, 2.87, HL, 5.38, L, +inf) |
| ligand_8875 | Propane-1,1-dicarboxylic acid (Ethylmalonic acid) | H2L | Carboxylic acids diacids | 61 | `CCC(C(=O)O)C(=O)O` | (-inf, H2L, 2.77, HL, 5.46, L, +inf) |
| ligand_8876 | Butane-1,1-dicarboxylic acid (Propylmalonic acid) | H2L | Carboxylic acids diacids | 43 | `CCCC(C(=O)O)C(=O)O` | (-inf, H2L, 2.84, HL, 5.45, L, +inf) |
| ligand_8877 | Pentane-1,1-dicarboxylic acid (Butylmalonic acid) | H2L | Carboxylic acids diacids | 66 | `CCCCC(C(=O)O)C(=O)O` | (-inf, H2L, 2.81, HL, 5.49, L, +inf) |
| ligand_8878 | Hexane-1,1-dicarboxylic acid (Pentylmalonic acid) | H2L | Carboxylic acids diacids | 22 | `CCCCCC(C(=O)O)C(=O)O` | (-inf, H2L, 2.8, HL, 5.54, L, +inf) |
| ligand_8879 | 2-Methylpropane-1,1-dicar… (Isopropylmalonic acid) | H2L | Carboxylic acids diacids | 21 | `CC(C)C(C(=O)O)C(=O)O` | (-inf, H2L, 2.78, HL, 5.5, L, +inf) |
| ligand_8880 | 3-Methylbutane-1,1-dicarbo… (Isobutylmalonic acid) | H2L | Carboxylic acids diacids | 17 | `CC(C)CC(C(=O)O)C(=O)O` | (-inf, H2L, 2.87, HL, 5.36, L, +inf) |
| ligand_8881 | 2,2-Dimethylpropane-1,1-dic… (t-Butylmalonic acid) | H2L | Carboxylic acids diacids | 19 | `CC(C)(C)C(C(=O)O)C(=O)O` | (-inf, HL, 7.03, L, +inf) |
| ligand_8882 | But-3-ene-1,1-dicarboxylic ac… (Allylmalonic acid) | H2L | Carboxylic acids diacids | 8 | `C=CCC(C(=O)O)C(=O)O` | (-inf, H2L, 2.63, HL, 5.24, L, +inf) |
| ligand_8885 | 2-Phenylethane-1,1-dicarboxy… (Benzylmalonic acid) | H2L | Carboxylic acids diacids | 21 | `O=C(O)C(Cc1ccccc1)C(=O)O` | (-inf, H2L, 2.91, HL, 5.86, L, +inf) |
| ligand_8886 | Phenylmethanedicarboxylic ac… (Phenylmalonic acid) | H2L | Carboxylic acids diacids | 16 | `O=C(O)C(C(=O)O)c1ccccc1` | (-inf, H2L, 2.34, HL, 5.1, L, +inf) |
| ligand_8887 | Propane-2,2-dicarboxylic a… (Dimethylmalonic acid) | H2L | Carboxylic acids diacids | 71 | `CC(C)(C(=O)O)C(=O)O` | (-inf, H2L, 2.97, HL, 5.68, L, +inf) |
| ligand_8888 | Butane-2,2-dicarboxylic… (Ethylmethylmalonic acid) | H2L | Carboxylic acids diacids | 2 | `CCC(C)(C(=O)O)C(=O)O` | (-inf, H2L, 2.86, HL, 6.41, L, +inf) |
| ligand_8889 | Pentane-3,3-dicarboxylic ac… (Diethylmalonic acid) | H2L | Carboxylic acids diacids | 69 | `CCC(CC)(C(=O)O)C(=O)O` | (-inf, H2L, 2, HL, 6.96, L, +inf) |
| ligand_8890 | Hexane-3,3-dicarboxylic… (Ethylpropylmalonic acid) | H2L | Carboxylic acids diacids | 2 | `CCCC(CC)(C(=O)O)C(=O)O` | (-inf, H2L, 2.15, HL, 7.43, L, +inf) |
| ligand_8891 | 2-Methylpentane-3,3-… (Ethyl-2-propylmalonic acid) | H2L | Carboxylic acids diacids | 2 | `CCC(C(=O)O)(C(=O)O)C(C)C` | (-inf, H2L, 1.92, HL, 7.99, L, +inf) |
| ligand_8892 | Heptane-3,3-dicarboxylic… (Butylethylmalonic acid) | H2L | Carboxylic acids diacids | 13 | `CCCCC(CC)(C(=O)O)C(=O)O` | (-inf, H2L, 2.04, HL, 7.14, L, +inf) |
| ligand_8893 | Heptane-4,4-dicarboxylic a… (Dipropylmalonic acid) | H2L | Carboxylic acids diacids | 59 | `CCCC(CCC)(C(=O)O)C(=O)O` | (-inf, H2L, -1.84, HL, 7.18, L, +inf) |
| ligand_8894 | 4-Methylhexane-3,3-dic… (s-Butylethylmalonic acid) | H2L | Carboxylic acids diacids | 16 | `CCC(C)C(CC)(C(=O)O)C(=O)O` | (-inf, HL, 8.4, L, +inf) |
| ligand_8895 | 2,4-Dimethylpentane-3,3… (Di-2-propylmalonic acid) | H2L | Carboxylic acids diacids | 2 | `CC(C)C(C(=O)O)(C(=O)O)C(C)C` | (-inf, H2L, 2.07, HL, 8.49, L, +inf) |
| ligand_8896 | 6-Methylheptane-3,3-… (Ethylisopentylmalonic acid) | H2L | Carboxylic acids diacids | 2 | `CCC(CCC(C)C)(C(=O)O)C(=O)O` | (-inf, H2L, 2.04, HL, 7.2, L, +inf) |
| ligand_8897 | Nonane-5,5-dicarboxylic acid (Dibutylmalonic acid) | H2L | Carboxylic acids diacids | 42 | `CCCCC(CCCC)(C(=O)O)C(=O)O` | (-inf, H2L, -1.93, HL, 7.22, L, +inf) |

### Functional groups across all SQL matches (32 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 32 | 100% |
| aromatic_ring | 6 | 19% |
| primary_amine | 2 | 6% |
| hydroxyl | 1 | 3% |
| ketone | 1 | 3% |

---

### Step 65: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.ligand_id = ligand_5937 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 3 row(s)

### `Fe^[2+]` + N-(Phosphonomethyl)glycine (Glyphosate) — 3 measurement(s)
metal_id: metal_62 | ligand_id: ligand_5937
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CNCP(=O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_99791 | ref_eq_map_1591 | beta_def_840 | logK | 11.18 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (10.1, L, +inf) |
| vlm_99790 | ref_eq_map_1591 | beta_def_812 | logK | 6.87 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (10.1, L, +inf) |
| vlm_99792 | ref_eq_map_1591 | beta_def_788 | logK | 5.92 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |

---

### Step 66: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id = ligand_8873 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 8 row(s)

### `Fe^[3+]` + Propanedioic acid (Malonic acid) — 8 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8873
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_152347 | ref_eq_map_20112 | beta_def_872 | logK | 16.93 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (5.27, L, +inf) |
| vlm_152348 | ref_eq_map_20113 | beta_def_872 | logK | 16.6 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (5.27, L, +inf) |
| vlm_152342 | ref_eq_map_20111 | beta_def_840 | logK | 14 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (5.27, L, +inf) |
| vlm_152343 | ref_eq_map_20112 | beta_def_840 | logK | 13.29 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (5.27, L, +inf) |
| vlm_152344 | ref_eq_map_20113 | beta_def_840 | logK | 13.04 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (5.27, L, +inf) |
| vlm_152337 | ref_eq_map_20111 | beta_def_812 | logK | 8.12 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152338 | ref_eq_map_20112 | beta_def_812 | logK | 7.52 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152339 | ref_eq_map_20113 | beta_def_812 | logK | 7.5 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |

---

### Step 67: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.ligand_id = ligand_8873 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 3 row(s)

### `Fe^[2+]` + Propanedioic acid (Malonic acid) — 3 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8873
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_152298 | ref_eq_map_20097 | beta_def_840 | logK | 3.21 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (5.27, L, +inf) |
| vlm_152297 | ref_eq_map_20098 | beta_def_812 | logK | 2.24 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152296 | ref_eq_map_20097 | beta_def_812 | logK | 2.17 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |

---

### Step 68: `search_ligands`
**Args:**
```json
{
  "name": "tiron"
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9358 | 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron) | H4L | Catechols | 225 | `O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1` | (-inf, H2L, 7.62, HL, 7.62, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 1 | 100% |
| hydroxyl | 1 | 100% |
| phenol | 1 | 100% |
| sulfonate | 1 | 100% |

---

### Step 69: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id = ligand_5760 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 6 row(s)

### `Fe^[3+]` + Aminoacetic acid (Glycine) — 6 measurement(s)
metal_id: metal_61 | ligand_id: ligand_5760
ligand_HxL_def: HL | ligand_SMILES: NCC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_93885 | ref_eq_map_96 | beta_def_194 | logK | 3.7 | 25 | 3 | `[M] + [HL]^2 <=> [M(HL)2]` | *** | [HL] | (2.33, HL, 9.57) |
| vlm_93884 | ref_eq_map_96 | beta_def_779 | logK | 2.03 | 25 | 3 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (2.33, HL, 9.57) |
| vlm_93882 | ref_eq_map_97 | beta_def_779 | logK | 1.77 | 25 | 0.5 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (2.33, HL, 9.57) |
| vlm_93883 | ref_eq_map_98 | beta_def_779 | logK | 1.76 | 25 | 1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (2.33, HL, 9.57) |
| vlm_93880 | ref_eq_map_97 | beta_def_812 | logK | -8.57 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93881 | ref_eq_map_96 | beta_def_812 | logK | -9.25 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |

---

### Step 70: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_9358 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 25
}
```

[summary]
## search_stability — 16 row(s)

### `Fe^[3+]` + 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron) — 16 measurement(s)
metal_id: metal_61 | ligand_id: ligand_9358
ligand_HxL_def: H4L | ligand_SMILES: O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_162100 | ref_eq_map_23841 | beta_def_788 | logK | 1.8 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_162101 | ref_eq_map_23842 | beta_def_788 | logK | 1.8 | 20 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_162103 | ref_eq_map_23844 | beta_def_788 | logK | 1.8 | 25 | 1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_162102 | ref_eq_map_23843 | beta_def_788 | logK | 1.5 | 25 | 0.5 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_162089 | ref_eq_map_23842 | beta_def_823 | logK | 0.5 | 20 | 0.1 | `[M] + [H2L] <=> [ML] + [H]^2` | *** | [H2L] | (-inf, H2L, 7.62) |
| vlm_162088 | ref_eq_map_23841 | beta_def_823 | logK | 0.2 | 25 | 0.1 | `[M] + [H2L] <=> [ML] + [H]^2` | *** | [H2L] | (-inf, H2L, 7.62) |
| vlm_162090 | ref_eq_map_23843 | beta_def_823 | logK | 0 | 25 | 0.5 | `[M] + [H2L] <=> [ML] + [H]^2` | *** | [H2L] | (-inf, H2L, 7.62) |
| vlm_162091 | ref_eq_map_23844 | beta_def_823 | logK | -0.2 | 25 | 1 | `[M] + [H2L] <=> [ML] + [H]^2` | *** | [H2L] | (-inf, H2L, 7.62) |
| vlm_162095 | ref_eq_map_23844 | beta_def_853 | logK | -4.1 | 25 | 1 | `[ML] + [H2L] <=> [ML2] + [H]^2` | *** | [H2L] | (-inf, H2L, 7.62) |
| vlm_162094 | ref_eq_map_23843 | beta_def_853 | logK | -4.4 | 25 | 0.5 | `[ML] + [H2L] <=> [ML2] + [H]^2` | *** | [H2L] | (-inf, H2L, 7.62) |
| vlm_162093 | ref_eq_map_23842 | beta_def_853 | logK | -5 | 20 | 0.1 | `[ML] + [H2L] <=> [ML2] + [H]^2` | *** | [H2L] | (-inf, H2L, 7.62) |
| vlm_162092 | ref_eq_map_23841 | beta_def_853 | logK | -5.2 | 25 | 0.1 | `[ML] + [H2L] <=> [ML2] + [H]^2` | *** | [H2L] | (-inf, H2L, 7.62) |
| vlm_162099 | ref_eq_map_23844 | beta_def_876 | logK | -7.4 | 25 | 1 | `[ML2] + [H2L] <=> [ML3] + [H]^2` | *** | [H2L] | (-inf, H2L, 7.62) |
| vlm_162098 | ref_eq_map_23843 | beta_def_876 | logK | -8 | 25 | 0.5 | `[ML2] + [H2L] <=> [ML3] + [H]^2` | *** | [H2L] | (-inf, H2L, 7.62) |
| vlm_162097 | ref_eq_map_23842 | beta_def_876 | logK | -9.2 | 20 | 0.1 | `[ML2] + [H2L] <=> [ML3] + [H]^2` | *** | [H2L] | (-inf, H2L, 7.62) |
| vlm_162096 | ref_eq_map_23841 | beta_def_876 | logK | -9.3 | 25 | 0.1 | `[ML2] + [H2L] <=> [ML3] + [H]^2` | *** | [H2L] | (-inf, H2L, 7.62) |

---

### Step 71: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6770 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 12 row(s)

### `Fe^[3+]` + Pyridine-2-phosphonic-6-carboxylic acid (2PP6C) — 5 measurement(s)
metal_id: metal_61 | ligand_id: ligand_6770
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)c1cccc(P(=O)(O)O)n1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_119196 | ref_eq_map_8467 | beta_def_840 | logK | 25.47 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (7.11, L, +inf) |
| vlm_119195 | ref_eq_map_8467 | beta_def_812 | logK | 15.97 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (7.11, L, +inf) |
| vlm_119198 | ref_eq_map_8467 | beta_def_238 | logK | 8.53 | 25 | 0.1 | `[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]` | *** |  |  |
| vlm_119197 | ref_eq_map_8467 | beta_def_966 | logK | 3.25 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_119199 | ref_eq_map_8467 | beta_def_792 | logK | 2.6 | 25 | 0.1 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |

### `Fe^[2+]` + Pyridine-2-phosphonic-6-carboxylic acid (2PP6C) — 7 measurement(s)
metal_id: metal_62 | ligand_id: ligand_6770
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)c1cccc(P(=O)(O)O)n1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_119189 | ref_eq_map_8466 | beta_def_840 | logK | 13.8 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (7.11, L, +inf) |
| vlm_119192 | ref_eq_map_8466 | beta_def_238 | logK | 10.77 | 25 | 0.1 | `[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]` | *** |  |  |
| vlm_119191 | ref_eq_map_8466 | beta_def_966 | logK | 9.09 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_119188 | ref_eq_map_8466 | beta_def_812 | logK | 8.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (7.11, L, +inf) |
| vlm_119193 | ref_eq_map_8466 | beta_def_792 | logK | 5.13 | 25 | 0.1 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |
| vlm_119194 | ref_eq_map_8466 | beta_def_204 | logK | 3.83 | 25 | 0.1 | `[MHL2] + [H] <=> [M(HL)2]` | *** |  |  |
| vlm_119190 | ref_eq_map_8466 | beta_def_788 | logK | 3.46 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |

---

### Step 72: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_9358 AND c.metal_id = metal_62 AND s.constant_type = 'K')",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### `H^[+]` + 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron) — 4 measurement(s)
metal_id: metal_68 | ligand_id: ligand_9358
ligand_HxL_def: H4L | ligand_SMILES: O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_161963 | *** | beta_def_32 | ΔS | 75.7 | 25 | 0.1 | `[HL] + [H] <=> [H2L]` | *** | [HL]; [H2L] | (-inf, H2L, 7.62, HL, 7.62) |
| vlm_161953 | ref_eq_map_23787 | beta_def_79 | logK | 11.8 | 25 | 0.5 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-12.5, HL, 7.62, L, +inf) |
| vlm_161954 | ref_eq_map_23788 | beta_def_79 | logK | 11.7 | 25 | 1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-12.5, HL, 7.62, L, +inf) |
| vlm_161955 | ref_eq_map_23789 | beta_def_79 | logK | 11.6 | 25 | 2 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-12.5, HL, 7.62, L, +inf) |

### `H^[+]` + 1,8-Dihydroxynaphthalene-3,6-disulfonic acid (Chromotropic … — 1 measurement(s)
metal_id: metal_68 | ligand_id: ligand_9470
ligand_HxL_def: H4L | ligand_SMILES: O=S(=O)(O)c1cc(O)c2c(O)cc(S(=O)(=O)O)cc2c1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_164207 | *** | beta_def_32 | ΔS | 56.1 | 25 | 0.1 | `[HL] + [H] <=> [H2L]` | *** | [HL]; [H2L] | (-inf, H2L, 5.35, HL, +inf) |

### `Nb^[5+]` + 1,8-Dihydroxynaphthalene-3,6-disulfonic acid (Chromotropic … — 1 measurement(s)
metal_id: metal_108 | ligand_id: ligand_9470
ligand_HxL_def: H4L | ligand_SMILES: O=S(=O)(O)c1cc(O)c2c(O)cc(S(=O)(=O)O)cc2c1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_164249 | ref_eq_map_24759 | beta_def_891 | logK | 17.9 | 20 | 0.1 | `[MO2] + [H] + [HL]^3 <=> [ML3] + [H2O]^2` | *** | [HL] | (5.35, HL, +inf) |

### `Ti^[3+]` + 1,8-Dihydroxynaphthalene-3,6-disulfonic acid (Chromotropic … — 1 measurement(s)
metal_id: metal_187 | ligand_id: ligand_9470
ligand_HxL_def: H4L | ligand_SMILES: O=S(=O)(O)c1cc(O)c2c(O)cc(S(=O)(=O)O)cc2c1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_164242 | ref_eq_map_24756 | beta_def_874 | logK | 13.7 | 20 | 0.1 | `[MO] + [HL]^3 <=> [ML3] + [H] + [H2O]` | *** | [HL] | (5.35, HL, +inf) |

### `Th^[4+]` + 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron) — 2 measurement(s)
metal_id: metal_185 | ligand_id: ligand_9358
ligand_HxL_def: H4L | ligand_SMILES: O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_162043 | ref_eq_map_23823 | beta_def_546 | logK | 12.8 | 25 | 0.1 | `[M2(OH)2L3] + [H]^2 <=> [M2L3] + [H2O]^2` | *** |  |  |
| vlm_162042 | ref_eq_map_23823 | beta_def_5 | logK | 11.9 | 25 | 0.1 | `[M2(OH)2L3] + [H]^4 <=> [ML]^2 + [H2L] + [H2O]^2` | *** | [H2L] | (-inf, H2L, 7.62) |

### `H^[+]` + 1-Naphthol-3,8-disulfonic acid — 1 measurement(s)
metal_id: metal_68 | ligand_id: ligand_9426
ligand_HxL_def: H3L | ligand_SMILES: O=S(=O)(O)c1cc(O)c2c(S(=O)(=O)O)cccc2c1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_163235 | ref_eq_map_24212 | beta_def_79 | logK | 11.49 | 25 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-inf, HL, 11.49, L, +inf) |

---

### Step 73: `search_ligands`
**Args:**
```json
{
  "name": "catechol"
}
```

[summary]
## search_ligands — 17 result(s)

**stats:** 17 SQL matches · showing 17 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | H2L | Catechols | 126 | `Oc1ccccc1O` | (-inf, H2L, 9.26, HL, 9.26, L, +inf) |
| ligand_9340 | 1,2-Dihydroxy-4-methylbenzene (4-Methylcatechol) | H2L | Catechols | 8 | `Cc1ccc(O)c(O)c1` | (-inf, H2L, 9.4, HL, 9.4, L, +inf) |
| ligand_9341 | 1,2-Dihydroxy-4-(2-methyl-2-p… (4-t-Butylcatechol) | H2L | Catechols | 1 | `CC(C)(C)c1ccc(O)c(O)c1` | *** |
| ligand_9344 | 4-Cyano-1,2-dihydroxybenzene (4-Cyanocatechol) | H2L | Catechols | 1 | `N#Cc1ccc(O)c(O)c1` | *** |
| ligand_9346 | 4-Chloro-1,2-dihydroxybenzene (4-Chlorocatechol) | H2L | Catechols | 27 | `Oc1ccc(Cl)cc1O` | (-inf, H2L, 8.56, HL, 8.56, L, +inf) |
| ligand_9347 | 4,5-Dichloro-1,2-dihydroxy… (4,5-Dichlorocatechol) | H2L | Catechols | 2 | `Oc1cc(Cl)c(Cl)cc1O` | (-inf, HL, 7.46, L, +inf) |
| ligand_9349 | Tetrachloro-1,2-dihydroxybe… (Tetrachlorocatechol) | H2L | Catechols | 4 | `Oc1c(O)c(Cl)c(Cl)c(Cl)c1Cl` | (-inf, H2L, 5.8, HL, 10.1, L, +inf) |
| ligand_9350 | 4-Bromo-1,2-dihydroxybenzene (4-Bromocatechol) | H2L | Catechols | 2 | `Oc1ccc(Br)cc1O` | (-inf, H2L, 8.37, HL, 11.32, L, +inf) |
| ligand_9351 | 1,2-Dihydroxy-3-nitrobenzene (3-Nitrocatechol) | H2L | Catechols | 34 | `O=[N+]([O-])c1cccc(O)c1O` | (-inf, H2L, 6.48, HL, 6.48, L, +inf) |
| ligand_9352 | 1,2-Dihydroxy-4-nitrobenzene (4-Nitrocatechol) | H2L | Catechols | 63 | `O=[N+]([O-])c1ccc(O)c(O)c1` | (-inf, H2L, 6.69, HL, 10.83, L, +inf) |
| ligand_9353 | 1,2-Dihydroxy-3,4-dinitrobe… (3,4-Dinitrocatechol) | H2L | Catechols | 2 | `O=[N+]([O-])c1ccc(O)c(O)c1[N+](=O)[O-]` | (-inf, H2L, 4.02, HL, 8.24, L, +inf) |
| ligand_9354 | 1,2-Dihydroxy-3,5-Nitrobenz… (3,5-Dinitrocatechol) | H2L | Catechols | 23 | `O=[N+]([O-])c1cc(O)c(O)c([N+](=O)[O-])c1` | (-inf, H2L, 3.38, HL, 9.8, L, +inf) |
| ligand_9357 | 1,2-Dihydroxybenzene-4-sulfonic… (4-Sulfocatechol) | H3L | Catechols | 35 | `O=S(=O)(O)c1ccc(O)c(O)c1` | (-inf, H2L, 8.5, HL, 8.5, L, +inf) |
| ligand_9396 | 3,3',4'-Trihydroxyfuchson-2… (Pyrocatechol Violet) | H4L | Catechols fuchsons | 14 | `O=C1C=C/C(=C(\c2ccc(O)c(O)c2)c2ccccc2S(=O)(=O)O)C=C1O` | (-inf, H4L, -0.8, H3L, 7.8, H2L, 9.76, HL, 9.76, L, +inf) |
| ligand_11044 | 1,2-Dihydroxy-3-methylbenzene (3-Methylcatechol) | *** | Ligands not selected | 0 | *** | *** |
| ligand_11052 | 2,3-Dihydroxy-4'-nitro… (4-Nitrophenylazocatechol) | *** | Ligands not selected | 0 | *** | *** |
| ligand_11087 | 4,4'-Bis(catecholazo)biphenyl | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (14 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 14 | 100% |
| hydroxyl | 14 | 100% |
| phenol | 14 | 100% |
| halide | 4 | 29% |
| tertiary_amine | 4 | 29% |
| sulfonate | 2 | 14% |
| ketone | 1 | 7% |
| nitrile | 1 | 7% |

---

### Step 74: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_9337 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 8 row(s)

### `Fe^[3+]` + 1,2-Dihydroxybenzene (Catechol) — 4 measurement(s)
metal_id: metal_61 | ligand_id: ligand_9337
ligand_HxL_def: H2L | ligand_SMILES: Oc1ccccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_161602 | ref_eq_map_23636 | beta_def_823 | logK | -1.36 | 25 | 1 | `[M] + [H2L] <=> [ML] + [H]^2` | *** | [H2L] | (-inf, H2L, 9.26) |
| vlm_161601 | ref_eq_map_23635 | beta_def_823 | logK | -2.2 | 25 | 0.1 | `[M] + [H2L] <=> [ML] + [H]^2` | *** | [H2L] | (-inf, H2L, 9.26) |
| vlm_161605 | ref_eq_map_23635 | beta_def_853 | logK | -7.53 | 25 | 0.1 | `[ML] + [H2L] <=> [ML2] + [H]^2` | *** | [H2L] | (-inf, H2L, 9.26) |
| vlm_161606 | ref_eq_map_23635 | beta_def_876 | logK | -13.16 | 25 | 0.1 | `[ML2] + [H2L] <=> [ML3] + [H]^2` | *** | [H2L] | (-inf, H2L, 9.26) |

### `Fe^[2+]` + 1,2-Dihydroxybenzene (Catechol) — 4 measurement(s)
metal_id: metal_62 | ligand_id: ligand_9337
ligand_HxL_def: H2L | ligand_SMILES: Oc1ccccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_161570 | ref_eq_map_23622 | beta_def_497 | logK | 10.9 | 25 | 0.1 | `[M]^2 + [HL]^2 <=> [M2HL2] + [H]` | *** | [HL] | (-13.3, HL, 9.26) |
| vlm_161567 | ref_eq_map_23622 | beta_def_823 | logK | -14.3 | 25 | 0.1 | `[M] + [H2L] <=> [ML] + [H]^2` | *** | [H2L] | (-inf, H2L, 9.26) |
| vlm_161568 | ref_eq_map_23623 | beta_def_823 | logK | -14.33 | 25 | 1 | `[M] + [H2L] <=> [ML] + [H]^2` | *** | [H2L] | (-inf, H2L, 9.26) |
| vlm_161569 | ref_eq_map_23623 | beta_def_853 | logK | -16.7 | 25 | 1 | `[ML] + [H2L] <=> [ML2] + [H]^2` | *** | [H2L] | (-inf, H2L, 9.26) |

---

### Step 75: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_9352 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 2 row(s)

### `Fe^[3+]` + 1,2-Dihydroxy-4-nitrobenzene (4-Nitrocatechol) — 2 measurement(s)
metal_id: metal_61 | ligand_id: ligand_9352
ligand_HxL_def: H2L | ligand_SMILES: O=[N+]([O-])c1ccc(O)c(O)c1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_161832 | ref_eq_map_23725 | beta_def_823 | logK | -2 | 25 | 0.1 | `[M] + [H2L] <=> [ML] + [H]^2` | *** | [H2L] | (-inf, H2L, 6.69) |
| vlm_161833 | ref_eq_map_23725 | beta_def_853 | logK | -4.43 | 25 | 0.1 | `[ML] + [H2L] <=> [ML2] + [H]^2` | *** | [H2L] | (-inf, H2L, 6.69) |

---

### Step 76: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_9354 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### logK — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_5 | Al^[3+] | ligand_9283 | 2-Hydroxy-3,5-dinitrobenzoi… | H2L | O=C(O)c1cc([N+](=O)[O-])cc([N+](=O)[O-])c1O | 4 | 3 | 25~30 | 0.1 | *** | 2 |
| metal_5 | Al^[3+] | ligand_9352 | 1,2-Dihydroxy-4-nitrobenzen… | H2L | O=[N+]([O-])c1ccc(O)c(O)c1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_15 | B^[3+] | ligand_9352 | 1,2-Dihydroxy-4-nitrobenzen… | H2L | O=[N+]([O-])c1ccc(O)c(O)c1 | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_18 | Ba^[2+] | ligand_9352 | 1,2-Dihydroxy-4-nitrobenzen… | H2L | O=[N+]([O-])c1ccc(O)c(O)c1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_19 | Be^[2+] | ligand_9283 | 2-Hydroxy-3,5-dinitrobenzoi… | H2L | O=C(O)c1cc([N+](=O)[O-])cc([N+](=O)[O-])c1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_19 | Be^[2+] | ligand_9354 | 1,2-Dihydroxy-3,5-Nitrobenz… | H2L | O=[N+]([O-])c1cc(O)c(O)c([N+](=O)[O-])c1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_19 | Be^[2+] | ligand_9352 | 1,2-Dihydroxy-4-nitrobenzen… | H2L | O=[N+]([O-])c1ccc(O)c(O)c1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_9354 | 1,2-Dihydroxy-3,5-Nitrobenz… | H2L | O=[N+]([O-])c1cc(O)c(O)c([N+](=O)[O-])c1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_10 | As^[3+] | ligand_9352 | 1,2-Dihydroxy-4-nitrobenzen… | H2L | O=[N+]([O-])c1ccc(O)c(O)c1 | 1 | 1 | 22 | 0.1 | *** | 1 |

---

### Step 77: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_9351 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 2 row(s)

### `Fe^[3+]` + 1,2-Dihydroxy-3-nitrobenzene (3-Nitrocatechol) — 2 measurement(s)
metal_id: metal_61 | ligand_id: ligand_9351
ligand_HxL_def: H2L | ligand_SMILES: O=[N+]([O-])c1cccc(O)c1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_161777 | ref_eq_map_23703 | beta_def_823 | logK | -2.16 | 25 | 0.1 | `[M] + [H2L] <=> [ML] + [H]^2` | *** | [H2L] | (-inf, H2L, 6.48) |
| vlm_161778 | ref_eq_map_23703 | beta_def_853 | logK | -4.66 | 25 | 0.1 | `[ML] + [H2L] <=> [ML2] + [H]^2` | *** | [H2L] | (-inf, H2L, 6.48) |

---

### Step 78: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id = ligand_8434 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 6 row(s)

### `Fe^[3+]` + Pyridine-2,6-diphosphonic acid (2,6-PDPA) — 6 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8434
ligand_HxL_def: H4L | ligand_SMILES: O=P(O)(O)c1cccc(P(=O)(O)O)n1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_143993 | ref_eq_map_16775 | beta_def_840 | logK | 28.68 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.12, L, +inf) |
| vlm_143992 | ref_eq_map_16775 | beta_def_812 | logK | 20.87 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.12, L, +inf) |
| vlm_143996 | ref_eq_map_16775 | beta_def_238 | logK | 8.36 | 25 | 0.1 | `[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]` | *** |  |  |
| vlm_143995 | ref_eq_map_16775 | beta_def_966 | logK | 6.4 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_143994 | ref_eq_map_16775 | beta_def_788 | logK | 4.06 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_143997 | ref_eq_map_16775 | beta_def_792 | logK | 3.86 | 25 | 0.1 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |

---

### Step 79: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.ligand_id = ligand_8434 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 10 row(s)

### `Fe^[2+]` + Pyridine-2,6-diphosphonic acid (2,6-PDPA) — 10 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8434
ligand_HxL_def: H4L | ligand_SMILES: O=P(O)(O)c1cccc(P(=O)(O)O)n1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_143983 | ref_eq_map_16774 | beta_def_840 | logK | 15.45 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.12, L, +inf) |
| vlm_143982 | ref_eq_map_16774 | beta_def_812 | logK | 10.12 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.12, L, +inf) |
| vlm_143986 | ref_eq_map_16774 | beta_def_966 | logK | 9.81 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_143988 | ref_eq_map_16774 | beta_def_792 | logK | 6.51 | 25 | 0.1 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |
| vlm_143989 | ref_eq_map_16774 | beta_def_204 | logK | 4.78 | 25 | 0.1 | `[MHL2] + [H] <=> [M(HL)2]` | *** |  |  |
| vlm_143984 | ref_eq_map_16774 | beta_def_788 | logK | 4.5 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_143990 | ref_eq_map_16774 | beta_def_756 | logK | 4.18 | 25 | 0.1 | `[M(HL)2] + [H] <=> [MH3L2]` | *** |  |  |
| vlm_143991 | ref_eq_map_16774 | beta_def_171 | logK | 3.57 | 25 | 0.1 | `[MH3L2] + [H] <=> [M(H2L)2]` | *** |  |  |
| vlm_143985 | ref_eq_map_16774 | beta_def_739 | logK | 3.36 | 25 | 0.1 | `[MHL] + [H] <=> [MH2L]` | *** |  |  |
| vlm_143987 | ref_eq_map_16774 | beta_def_238 | logK | -11.38 | 25 | 0.1 | `[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]` | *** |  |  |

---

### Step 80: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_name_SRD LIKE '%hydroxide%' AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 15 row(s)

### `Fe^[3+]` + Hydroxide ion — 15 measurement(s)
metal_id: metal_61 | ligand_id: ligand_10076
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_170820 | ref_eq_map_27396 | beta_def_649 | logK | 51 | 25 | 3 | `[M]^3 + [L]^4 <=> [M3L4]` | *** | [L] | (13.78, L, +inf) |
| vlm_170819 | ref_eq_map_27391 | beta_def_649 | logK | 49.7 | 25 | 3 | `[M]^3 + [L]^4 <=> [M3L4]` | *** | [L] | (13.78, L, +inf) |
| vlm_170821 | ref_eq_map_27390 | beta_def_649 | logK | 49.7 | 25 | 0 | `[M]^3 + [L]^4 <=> [M3L4]` | *** | [L] | (13.78, L, +inf) |
| vlm_170808 | ref_eq_map_27390 | beta_def_894 | logK | 34.4 | 25 | 0 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (13.78, L, +inf) |
| vlm_170813 | ref_eq_map_27396 | beta_def_519 | logK | 25.5 | 25 | 3 | `[M]^2 + [L]^2 <=> [M2L2]` | *** | [L] | (13.78, L, +inf) |
| vlm_170812 | ref_eq_map_27391 | beta_def_519 | logK | 25.2 | 25 | 3 | `[M]^2 + [L]^2 <=> [M2L2]` | *** | [L] | (13.78, L, +inf) |
| vlm_170814 | ref_eq_map_27390 | beta_def_519 | logK | 25.14 | 25 | 0 | `[M]^2 + [L]^2 <=> [M2L2]` | *** | [L] | (13.78, L, +inf) |
| vlm_170811 | ref_eq_map_27394 | beta_def_519 | logK | 25.1 | 25 | 2 | `[M]^2 + [L]^2 <=> [M2L2]` | *** | [L] | (13.78, L, +inf) |
| vlm_170810 | ref_eq_map_27393 | beta_def_519 | logK | 25 | 25 | 1 | `[M]^2 + [L]^2 <=> [M2L2]` | *** | [L] | (13.78, L, +inf) |
| vlm_170809 | ref_eq_map_27392 | beta_def_519 | logK | 24.5 | 25 | 0.5 | `[M]^2 + [L]^2 <=> [M2L2]` | *** | [L] | (13.78, L, +inf) |
| vlm_170807 | ref_eq_map_27390 | beta_def_840 | logK | 23.4 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (13.78, L, +inf) |
| vlm_170806 | ref_eq_map_27391 | beta_def_840 | logK | 22.1 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (13.78, L, +inf) |
| vlm_170805 | ref_eq_map_27394 | beta_def_840 | logK | 21.9 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (13.78, L, +inf) |
| vlm_170802 | ref_eq_map_27392 | beta_def_840 | logK | 21.8 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (13.78, L, +inf) |
| vlm_170804 | ref_eq_map_27393 | beta_def_840 | logK | 21.8 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (13.78, L, +inf) |

---

### Step 81: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id = ligand_10076 AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 7 row(s)

### `Fe^[3+]` + Hydroxide ion — 7 measurement(s)
metal_id: metal_61 | ligand_id: ligand_10076
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_170797 | ref_eq_map_27397 | beta_def_812 | logK | 11.81 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (13.78, L, +inf) |
| vlm_170791 | ref_eq_map_27390 | beta_def_812 | logK | 11.27 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (13.78, L, +inf) |
| vlm_170796 | ref_eq_map_27391 | beta_def_812 | logK | 11.21 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (13.78, L, +inf) |
| vlm_170795 | ref_eq_map_27394 | beta_def_812 | logK | 11.14 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (13.78, L, +inf) |
| vlm_170792 | ref_eq_map_27392 | beta_def_812 | logK | 11.05 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (13.78, L, +inf) |
| vlm_170793 | ref_eq_map_27395 | beta_def_812 | logK | 11.05 | 25 | 0.7 | `[M] + [L] <=> [ML]` | *** | [L] | (13.78, L, +inf) |
| vlm_170794 | ref_eq_map_27393 | beta_def_812 | logK | 11.05 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (13.78, L, +inf) |

---

### Step 82: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_7295 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 3 row(s)

### `Fe^[3+]` + Nitrilotriacetohydroxamic acid — 3 measurement(s)
metal_id: metal_61 | ligand_id: ligand_7295
ligand_HxL_def: H3L | ligand_SMILES: O=C(CN(CC(=O)NO)CC(=O)NO)NO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_127357 | ref_eq_map_10986 | beta_def_812 | logK | 19.4 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-11.74, L, +inf) |
| vlm_127359 | ref_eq_map_10986 | beta_def_741 | logK | 10.58 | 20 | 0.1 | `[ML] + [H]^2 <=> [MH2L]` | *** |  |  |
| vlm_127358 | ref_eq_map_10986 | beta_def_966 | logK | 9.1 | 20 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |

---

### Step 83: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_7295 AND c.metal_id = metal_62 AND s.constant_type = 'K')",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### `Fe^[3+]` + Trimethylenedihydroxamic acid (Glutarodihydroxamic acid) — 2 measurement(s)
metal_id: metal_61 | ligand_id: ligand_9894
ligand_HxL_def: H2L | ligand_SMILES: O=C(CCCC(=O)NO)NO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_168650 | ref_eq_map_26606 | beta_def_408 | logK | 66.34 | 20 | 0.1 | `[M]^2 + [HL]^2 + [L]^2 <=> [M2(HL)2L2]` | *** | [HL]; [L] | (8.91, HL, 10.66, L, +inf) |
| vlm_168649 | ref_eq_map_26606 | beta_def_583 | logK | 56.74 | 20 | 0.1 | `[M]^2 + [OH] + [L]^2 <=> [M2(OH)L2]` | *** | [L] | (10.66, L, +inf) |

### `Fe^[3+]` + Iminodiacetohydroxamic acid — 1 measurement(s)
metal_id: metal_61 | ligand_id: ligand_7154
ligand_HxL_def: H2L | ligand_SMILES: O=C(CNCC(=O)NO)NO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_124725 | ref_eq_map_10255 | beta_def_540 | logK | 44 | 20 | 0.1 | `[M]^2 + [L]^3 <=> [M2L3]` | *** | [L] | (10.8, L, +inf) |

### `Fe^[3+]` + Aminoacetohydroxamic acid (Glycinehydroxamic acid) — 2 measurement(s)
metal_id: metal_61 | ligand_id: ligand_6982
ligand_HxL_def: HL | ligand_SMILES: NCC(=O)NO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_121461 | ref_eq_map_9344 | beta_def_872 | logK | 26.5 | 25 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.18, L, +inf) |
| vlm_121460 | ref_eq_map_9344 | beta_def_840 | logK | 21.87 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.18, L, +inf) |

### `Cu^[2+]` + Ethylenedinitrilotetraacetohydroxamic acid — 1 measurement(s)
metal_id: metal_41 | ligand_id: ligand_7320
ligand_HxL_def: H4L | ligand_SMILES: O=C(CN(CCN(CC(=O)NO)CC(=O)NO)CC(=O)NO)NO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_127783 | ref_eq_map_11152 | beta_def_812 | logK | 25.6 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-11.1, L, +inf) |

### `Fe^[3+]` + Ethylenedinitrilotetraacetohydroxamic acid — 1 measurement(s)
metal_id: metal_61 | ligand_id: ligand_7320
ligand_HxL_def: H4L | ligand_SMILES: O=C(CN(CCN(CC(=O)NO)CC(=O)NO)CC(=O)NO)NO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_127787 | ref_eq_map_11153 | beta_def_812 | logK | 25.6 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-11.1, L, +inf) |

### `Fe^[3+]` + N-(Carboxymethyl)-N-(2-hydroxyethyl)aminoacetohydroxamic ac… — 1 measurement(s)
metal_id: metal_61 | ligand_id: ligand_6020
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CN(CCO)CC(=O)NO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_101541 | ref_eq_map_2242 | beta_def_247 | logK | 22.55 | 20 | 0.1 | `[ML] + [OH]^2 <=> [M(OH)2L]` | *** |  |  |

### `Fe^[3+]` + N,N'-Bis(carboxymethyl)ethylenedinitrilo-N,N'-diacetohydrox… — 1 measurement(s)
metal_id: metal_61 | ligand_id: ligand_6036
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)NO)CC(=O)NO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_101953 | ref_eq_map_2399 | beta_def_812 | logK | 22.15 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.93, L, +inf) |

### `Ni^[2+]` + Nitrilotriacetohydroxamic acid — 1 measurement(s)
metal_id: metal_112 | ligand_id: ligand_7295
ligand_HxL_def: H3L | ligand_SMILES: O=C(CN(CC(=O)NO)CC(=O)NO)NO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_127352 | ref_eq_map_10984 | beta_def_581 | logK | 21.78 | 25 | 0.1 | `[M]^2 + [L]^2 + [H2O] <=> [M2(OH)L2] + [H]` | *** | [L] | (-11.74, L, +inf) |

---

### Step 84: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_8866 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 15 row(s)

### logK — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_2 | Ag^[+] | ligand_9034 | As-Phenylarsinodiacetic aci… | H2L | O=C(O)C[As](CC(=O)O)c1ccccc1 | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_8521 | Phenylacetic acid | HL | O=C(O)Cc1ccccc1 | 2 | 2 | 25 | 2 | *** | 1 |
| metal_2 | Ag^[+] | ligand_9019 | Benzene-1,2-bis(thioacetic … | H2L | O=C(O)CSc1ccccc1SCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_6731 | N-Phenyliminodiacetic acid | H2L | O=C(O)CN(CC(=O)O)c1ccccc1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6731 | N-Phenyliminodiacetic acid | H2L | O=C(O)CN(CC(=O)O)c1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_6731 | N-Phenyliminodiacetic acid | H2L | O=C(O)CN(CC(=O)O)c1ccccc1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_6723 | N-Phenylglycine | HL | O=C(O)CNc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔS — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_6731 | N-Phenyliminodiacetic acid | H2L | O=C(O)CN(CC(=O)O)c1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔH — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_6731 | N-Phenyliminodiacetic acid | H2L | O=C(O)CN(CC(=O)O)c1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 85: `search_ligands`
**Args:**
```json
{
  "name": "oxalic acid"
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | Carboxylic acids diacids | 394 | `O=C(O)C(=O)O` | (-inf, H2L, -1.2, HL, 3.8, L, +inf) |
| ligand_8960 | Oxopropanedioic acid (Ketomaloni… (Mesoxalic acid) | H2L | Carboxylic acids diacids… | 3 | `O=C(O)C(=O)C(=O)O` | (-inf, H2L, -1.82, HL, 3.52, L, +inf) |
| ligand_9763 | Dithiooxalic acid | H2L | miscellaneous mercaptans | 3 | `O=C(S)C(=O)S` | *** |
| ligand_11304 | Ethanedi(dithioic acid) (Tetrathiooxalic acid) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 67% |
| ketone | 1 | 33% |
| thiol | 1 | 33% |

---

### Step 86: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_8872 AND c.metal_id = metal_61 AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 3 row(s)

### `Fe^[3+]` + Ethanedioic acid (Oxalic acid) — 3 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8872
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_151795 | ref_eq_map_19978 | beta_def_812 | logK | 7.74 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |
| vlm_151794 | ref_eq_map_19976 | beta_def_812 | logK | 7.58 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |
| vlm_151793 | ref_eq_map_19977 | beta_def_812 | logK | 7.53 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |

---

### Step 87: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_8872 AND c.metal_id = metal_62 AND s.constant_type = 'K' AND c.beta_definition_name = '[ML]/[M][L]' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 1 row(s)

### `Fe^[2+]` + Ethanedioic acid (Oxalic acid) — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8872
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_151749 | ref_eq_map_19964 | beta_def_812 | logK | 3.05 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |

---

### Step 88: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_8872 AND c.metal_id = metal_61 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 5 row(s)

### `Fe^[3+]` + Ethanedioic acid (Oxalic acid) — 5 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8872
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_151801 | ref_eq_map_19976 | beta_def_872 | logK | 18.6 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (3.8, L, +inf) |
| vlm_151798 | ref_eq_map_19976 | beta_def_840 | logK | 13.81 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (3.8, L, +inf) |
| vlm_151795 | ref_eq_map_19978 | beta_def_812 | logK | 7.74 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |
| vlm_151794 | ref_eq_map_19976 | beta_def_812 | logK | 7.58 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |
| vlm_151793 | ref_eq_map_19977 | beta_def_812 | logK | 7.53 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |

---

### Step 89: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_8872 AND c.metal_id = metal_62 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 2 row(s)

### `Fe^[2+]` + Ethanedioic acid (Oxalic acid) — 2 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8872
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_151750 | ref_eq_map_19964 | beta_def_840 | logK | 5.08 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (3.8, L, +inf) |
| vlm_151749 | ref_eq_map_19964 | beta_def_812 | logK | 3.05 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |

---

### Step 90: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_8872 AND c.metal_id = metal_62 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30 AND s.equation_str LIKE '%solid%')",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### `UO_[2]^[2+]` + Hydrogen carbonate (Carbonic acid) — 2 measurement(s)
metal_id: metal_195 | ligand_id: ligand_10096
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172827 | *** | beta_def_653 | ΔS | 870.3 | 25 | 3 | `[M]^3 + [L]^6 <=> [M3L6]` | *** | [L] | (9.91, L, +inf) |
| vlm_172826 | *** | beta_def_653 | ΔS | 828.4 | 25 | 0 | `[M]^3 + [L]^6 <=> [M3L6]` | *** | [L] | (9.91, L, +inf) |

### `U^[4+]` + Hydrogen carbonate (Carbonic acid) — 1 measurement(s)
metal_id: metal_193 | ligand_id: ligand_10096
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172789 | *** | beta_def_903 | ΔS | 640.2 | 25 | 3 | `[M] + [L]^5 <=> [ML5]` | *** | [L] | (9.91, L, +inf) |

### `Fe^[3+]` + Ethanoic acid (Acetic acid) — 1 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8465
ligand_HxL_def: HL | ligand_SMILES: CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_144796 | *** | beta_def_597 | ΔS | 619.2 | 25 | 1 | `[M]^3 + [L]^6 + [H2O]^2 <=> [M3(OH)2L6] + [H]^2` | *** | [L] | (4.56, L, +inf) |

### `Th^[4+]` + Propanedioic acid (Malonic acid) — 1 measurement(s)
metal_id: metal_185 | ligand_id: ligand_8873
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_152275 | *** | beta_def_872 | ΔS | 376.6 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (5.27, L, +inf) |

### `Sc^[3+]` + Propanedioic acid (Malonic acid) — 1 measurement(s)
metal_id: metal_169 | ligand_id: ligand_8873
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_152035 | *** | beta_def_872 | ΔS | 360.2 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (5.27, L, +inf) |

### `Fe^[3+]` + Ethanedioic acid (Oxalic acid) — 1 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8872
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_151803 | *** | beta_def_872 | ΔS | 357.7 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (3.8, L, +inf) |

### `Fe^[3+]` + Propanedioic acid (Malonic acid) — 1 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8873
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_152350 | *** | beta_def_872 | ΔS | 341.8 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (5.27, L, +inf) |

### `Th^[4+]` + Ethanoic acid (Acetic acid) — 2 measurement(s)
metal_id: metal_185 | ligand_id: ligand_8465
ligand_HxL_def: HL | ligand_SMILES: CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_144672 | *** | beta_def_903 | ΔS | 340.2 | 25 | 1 | `[M] + [L]^5 <=> [ML5]` | *** | [L] | (4.56, L, +inf) |
| vlm_144669 | *** | beta_def_894 | ΔS | 314.2 | 25 | 1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (4.56, L, +inf) |

---

### Step 91: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_7320 AND c.metal_id IN (metal_61, metal_62) AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 6 row(s)

### `Fe^[3+]` + Ethylenedinitrilotetraacetohydroxamic acid — 6 measurement(s)
metal_id: metal_61 | ligand_id: ligand_7320
ligand_HxL_def: H4L | ligand_SMILES: O=C(CN(CCN(CC(=O)NO)CC(=O)NO)CC(=O)NO)NO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_127787 | ref_eq_map_11153 | beta_def_812 | logK | 25.6 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-11.1, L, +inf) |
| vlm_127789 | ref_eq_map_11153 | beta_def_754 | logK | 10 | 20 | 0.1 | `[MHL] + [H]^2 <=> [MH3L]` | *** |  |  |
| vlm_127788 | ref_eq_map_11153 | beta_def_788 | logK | 6.03 | 20 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_127791 | ref_eq_map_11153 | beta_def_981 | logK | 4.9 | 20 | 0.1 | `[ML] + [OH] <=> [M(OH)L]` | *** |  |  |
| vlm_127790 | ref_eq_map_11153 | beta_def_765 | logK | 3.92 | 20 | 0.1 | `[MH3L] + [H] <=> [MH4L]` | *** |  |  |
| vlm_127792 | ref_eq_map_11153 | beta_def_248 | logK | 3.3 | 20 | 0.1 | `[M(OH)L] + [OH] <=> [M(OH)2L]` | *** |  |  |

---

### Step 92: `search_ligands`
**Args:**
```json
{
  "name": "acetohydroxamic acid"
}
```

[summary]
## search_ligands — 25 result(s)

**stats:** 28 SQL matches · showing 25 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5938 | (Carboxymethylamino)acetohydroxamic acid | H2L | Amino Acids | 11 | `O=C(O)CNCC(=O)NO` | (-inf, H3L, -1.8, H2L, 6.99, HL, 9.09, L, +inf) |
| ligand_6020 | N-(Carboxymethyl)-N-(2-hydroxyethyl)aminoacetohyd… | H2L | Amino Acids | 9 | `O=C(O)CN(CCO)CC(=O)NO` | (-inf, H2L, 5.69, HL, 9.18, L, +inf) |
| ligand_6036 | N,N'-Bis(carboxymethyl)ethylenedinitrilo-N,N'-dia… | H4L | Amino Acids | 24 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)NO)CC(=O)NO` | (-inf, H5L, -1.6, H4L, 3.48, H3L, 6.67, H2L, 9, HL, 9.93, L, +inf) |
| ligand_6054 | N,N'-Bis(carboxymethyl)ethylenedinitrilobis(N-2-p… | H4L | Amino Acids | 8 | `CC(C)N(O)C(=O)CN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O` | (-inf, H4L, 4.2, H3L, 8.03, H2L, 9.67, HL, 10.56, L, +inf) |
| ligand_6057 | N,N',N''-Tris(carboxymethyl)diethylenetrinitrilob… | H5L | Amino Acids | 9 | `CC(C)N(O)C(=O)CN(CCN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O)CC(=O)O` | (-inf, H5L, 3.7, H4L, 5.94, H3L, 9.07, H2L, 10.1, HL, 10.85, L, +inf) |
| ligand_6203 | N,N-Bis(carboxymethyl)aminoacetohydroxamic acid | H3L | NTA and derivatives | 11 | `O=C(O)CN(CC(=O)O)CC(=O)NO` | (-inf, H3L, 2.44, H2L, 6.16, HL, 9.42, L, +inf) |
| ligand_6982 | Aminoacetohydroxamic acid (Glycinehydroxamic acid) | HL | Aliphatic amines | 51 | `NCC(=O)NO` | (-inf, H2L, 7.45, HL, 9.18, L, +inf) |
| ligand_6992 | Methylaminoacetohydrox… (Sarcosinehydroxamic acid) | HL | Aliphatic amines seconda… | 14 | `CNCC(=O)NO` | (-inf, H2L, 7.62, HL, 9.2, L, +inf) |
| ligand_7154 | Iminodiacetohydroxamic acid | H2L | Aliphatic amines seconda… | 9 | `O=C(CNCC(=O)NO)NO` | (-inf, H3L, 5.66, H2L, 7.23, HL, 10.8, L, +inf) |
| ligand_7282 | N,N-Bis(2-hydroxyethyl)aminoacetohydroxamic acid | HL | Aliphatic amines tertiar… | 8 | `O=C(CCN(CCO)CCO)NO` | (-inf, H2L, 5.37, HL, 8.97, L, +inf) |
| ligand_7295 | Nitrilotriacetohydroxamic acid | H3L | Aliphatic amines tertiar… | 49 | `O=C(CN(CC(=O)NO)CC(=O)NO)NO` | (-inf, H4L, 5.92, H3L, 6.81, H2L, 8.84, HL, 8.84, L, +inf) |
| ligand_7320 | Ethylenedinitrilotetraacetohydroxamic acid | H4L | Aliphatic amines tertiar… | 16 | `O=C(CN(CCN(CC(=O)NO)CC(=O)NO)CC(=O)NO)NO` | (-inf, H6L, 5.55, H5L, 6.05, H4L, 6.67, H3L, 7.23, H2L, 10.6, HL, 10.6, L, +inf) |
| ligand_7391 | Piperazine-N,N'-diacetohydroxamic acid | H2L | Cyclic amines  | 11 | `O=C(CN1CCN(C(=O)NO)CC1)NO` | (-inf, H4L, -1.5, H3L, 5.52, H2L, 8.4, HL, 9.8, L, +inf) |
| ligand_7709 | 5,7-Dioxo-1,4,8,11-tetraazacyclotetradecane-4,8-b… | H2L | Aza-oxo-macrocycles | 9 | `CN(O)C(=O)CN1CCNCCCNCCN(CC(=O)N(C)O)C(=O)CC1=O` | (-inf, H4L, 4.02, H3L, 6.67, H2L, 8.39, HL, 9.46, L, +inf) |
| ligand_9873 | Acetohydroxamic acid | HL | miscellaneous hydroxamic… | 66 | `CC(=O)NO` | (-inf, HL, 9.29, L, +inf) |
| ligand_9875 | N-Methylacetohydroxamic acid | HL | miscellaneous hydroxamic… | 6 | `CC(=O)N(C)O` | (-inf, HL, 8.63, L, +inf) |
| ligand_9876 | N-Phenylacetohydroxamic acid | HL | miscellaneous hydroxamic… | 7 | `CC(=O)N(O)c1ccccc1` | (-inf, HL, 8.33, L, +inf) |
| ligand_9877 | N-(4-Methylphenyl)acetohydroxamic acid | HL | miscellaneous hydroxamic… | 6 | `CC(=O)N(O)c1ccc(C)cc1` | (-inf, HL, 8.7, L, +inf) |
| ligand_9878 | N-(3-Cyanophenyl)acetohydroxamic acid | HL | miscellaneous hydroxamic… | 6 | `CC(=O)N(O)c1cccc(C#N)c1` | (-inf, HL, 8.15, L, +inf) |
| ligand_9879 | N-(4-Cyanophenyl)acetohydroxamic acid | HL | miscellaneous hydroxamic… | 6 | `CC(=O)N(O)c1ccc(C#N)cc1` | (-inf, HL, 8.14, L, +inf) |
| ligand_9880 | N-(4-Chlorophenyl)acetohydroxamic acid | HL | miscellaneous hydroxamic… | 6 | `CC(=O)N(O)c1ccc(Cl)cc1` | (-inf, HL, 8.26, L, +inf) |
| ligand_9881 | N-(3-Iodophenyl)acetohydroxamic acid | HL | miscellaneous hydroxamic… | 6 | `CC(=O)N(O)c1cccc(I)c1` | (-inf, HL, 8.2, L, +inf) |
| ligand_9882 | N-(4-Iodophenyl)acetohydroxamic acid | HL | miscellaneous hydroxamic… | 6 | `CC(=O)N(O)c1ccc(I)cc1` | (-inf, HL, 8.18, L, +inf) |
| ligand_9883 | N-(3-Acetylphenyl)acetohydroxamic acid | HL | miscellaneous hydroxamic… | 6 | `CC(=O)c1cccc(N(O)C(C)=O)c1` | (-inf, HL, 8.23, L, +inf) |
| ligand_11339 | Phenylacetohydroxamic acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (24 parseable SMILES)

| group | count | % |
|-------|-------|---|
| amide | 24 | 100% |
| hydroxyl | 24 | 100% |
| tertiary_amine | 9 | 38% |
| aromatic_ring | 8 | 33% |
| carboxyl | 6 | 25% |
| secondary_amine | 4 | 17% |
| halide | 3 | 12% |
| nitrile | 2 | 8% |
| ketone | 1 | 4% |
| primary_amine | 1 | 4% |

---

### Step 93: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_9873 AND c.metal_id = metal_61 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 8 row(s)

### `Fe^[3+]` + Acetohydroxamic acid — 8 measurement(s)
metal_id: metal_61 | ligand_id: ligand_9873
ligand_HxL_def: HL | ligand_SMILES: CC(=O)NO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_168455 | ref_eq_map_26541 | beta_def_872 | logK | 28.3 | 20 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.29, L, +inf) |
| vlm_168456 | ref_eq_map_26542 | beta_def_872 | logK | 26.9 | 25 | 2 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.29, L, +inf) |
| vlm_168453 | ref_eq_map_26541 | beta_def_840 | logK | 21.1 | 20 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.29, L, +inf) |
| vlm_168454 | ref_eq_map_26542 | beta_def_840 | logK | 19.8 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.29, L, +inf) |
| vlm_168448 | ref_eq_map_26543 | beta_def_812 | logK | 11.42 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.29, L, +inf) |
| vlm_168447 | ref_eq_map_26541 | beta_def_812 | logK | 11.38 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.29, L, +inf) |
| vlm_168449 | ref_eq_map_26544 | beta_def_812 | logK | 10.95 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.29, L, +inf) |
| vlm_168450 | ref_eq_map_26542 | beta_def_812 | logK | 10.84 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.29, L, +inf) |

---

### Step 94: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_9873 AND c.metal_id = metal_62 AND s.constant_type = 'K' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 15
}
```

[summary]
## search_stability — 2 row(s)

### `Fe^[2+]` + Acetohydroxamic acid — 2 measurement(s)
metal_id: metal_62 | ligand_id: ligand_9873
ligand_HxL_def: HL | ligand_SMILES: CC(=O)NO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_168433 | ref_eq_map_26534 | beta_def_840 | logK | 8.5 | 20 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.29, L, +inf) |
| vlm_168432 | ref_eq_map_26534 | beta_def_812 | logK | 4.8 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.29, L, +inf) |

---
