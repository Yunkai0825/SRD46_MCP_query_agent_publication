# Q2.2.4 — Tool Results (batch 5)

### Step 2: `db_distribution`
**Args:**
```json
{
  "table": "ligand_card",
  "group_column": "ligand_class_name",
  "limit": 100
}
```

[PHASE ERROR] Tool 'db_distribution' is not available yet. Complete PHASE 1 first: call search_ligands, then call 0_plan_search_strategy.

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "%",
  "limit": 1
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 5750 SQL matches · showing 1 · limit 1

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |

### Functional groups across all SQL matches (4054 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 1903 | 47% |
| carboxyl | 1693 | 42% |
| hydroxyl | 1430 | 35% |
| primary_amine | 1101 | 27% |
| tertiary_amine | 820 | 20% |
| amide | 756 | 19% |
| secondary_amine | 724 | 18% |
| phenol | 462 | 11% |
| pyridine | 428 | 11% |
| ether | 291 | 7% |
| halide | 268 | 7% |
| thioether | 261 | 6% |
| sulfonate | 203 | 5% |
| phosphonate | 181 | 4% |
| thiol | 119 | 3% |
| imine | 109 | 3% |
| phosphate | 99 | 2% |
| ester | 92 | 2% |
| ketone | 90 | 2% |
| oxime | 48 | 1% |
| aldehyde | 44 | 1% |
| nitrile | 39 | 1% |
| thiazole | 10 | 0% |
| imidazole | 8 | 0% |
| pyrazole | 8 | 0% |
| carboxylate | 1 | 0% |

---

### Step 5: `db_distribution`
**Args:**
```json
{
  "table": "ligand_card",
  "group_column": "ligand_class_name",
  "limit": 100
}
```

[summary]
## db_distribution - ligand_card by ligand_class_name

**total_rows:** 5750

| value | count | pct |
|-------|-------|-----|
| Ligands not selected | 1339 | 23.29% |
| Amino Acids | 297 | 5.17% |
| Aliphatic amines | 250 | 4.35% |
| Pyridines (azines) | 248 | 4.31% |
| Carboxylic acids | 182 | 3.17% |
| Aza-macrocycles | 165 | 2.87% |
| Peptides | 157 | 2.73% |
| Aliphatic amines secondary N | 139 | 2.42% |
| Pyrroles (azoles) | 134 | 2.33% |
| Aminophosphorus acids | 132 | 2.3% |
| EDTA and derivatives | 115 | 2.0% |
| Aza-oxa-macrocycles | 112 | 1.95% |
| Carboxylic acids diacids | 103 | 1.79% |
| Inorganic ligands | 101 | 1.76% |
| Naphtols | 100 | 1.74% |
| polypeptides | 98 | 1.7% |
| Organophosphorus and arsenic acids | 95 | 1.65% |
| Aliphatic amines tertiary N | 95 | 1.65% |
| Phenols | 92 | 1.6% |
| NTA and derivatives | 91 | 1.58% |
| miscellaneous hydrocarbons | 84 | 1.46% |
| miscellaneous hydroxamic acids | 74 | 1.29% |
| Aniline | 72 | 1.25% |
| Carboxylic acids thio | 71 | 1.23% |
| miscellaneous ureas, hadrazides, amidines | 70 | 1.22% |
| Aza macrocycles with carboxylic acids | 70 | 1.22% |
| miscellaneous alcohols and sugar | 68 | 1.18% |
| tripeptides | 66 | 1.15% |
| Catechols | 66 | 1.15% |
| Aniline carboxylic acids | 66 | 1.15% |
| Aza-oxo-macrocycles | 58 | 1.01% |
| cyclic ketones | 57 | 0.99% |
| miscellaneous amides | 54 | 0.94% |
| Carboxylic acids diacids S-Se-Te-P-As | 53 | 0.92% |
| Purines | 52 | 0.9% |
| Carboxylic acids hydroxy | 52 | 0.9% |
| Cyclic amines  | 51 | 0.89% |
| Phenols salicylic acids | 49 | 0.85% |
| Carboxylic acids polyacids | 49 | 0.85% |
| miscellaneous mercaptans | 46 | 0.8% |
| Carboxylic acids oxy | 45 | 0.78% |
| Ketones (oxo ligands) | 43 | 0.75% |
| Iminodiacetic acid and derivatives | 38 | 0.66% |
| Carboxylic acids keto | 36 | 0.63% |
| Pyrimidines | 35 | 0.61% |
| Pyridine carboxylic acids | 35 | 0.61% |
| Bipyridines | 35 | 0.61% |
| Quinolines | 32 | 0.56% |
| miscellaneous sulfides | 25 | 0.43% |
| miscellaneous crown ether | 24 | 0.42% |
| Carboxylic acids seleno | 22 | 0.38% |
| Purines phosphates | 21 | 0.37% |
| Aza-thia-macrocycles | 20 | 0.35% |
| Catechols fuchsons | 15 | 0.26% |
| Carboxylic acids diacids hydroxy | 15 | 0.26% |
| Phenanthrolines | 13 | 0.23% |
| miscellaneous sulfonic acids | 12 | 0.21% |
| Tripyridines | 6 | 0.1% |
| Carboxylic acids diacids keto | 5 | 0.09% |

---
