Here’s what I could extract directly from SRD‑46 (grouping ligands by ligand_class_name, excluding NULL/blank labels). The five classes with the most ligands are:

| Rank | Ligand class | Ligand count | Share |
|---:|---|---:|---:|
| 1 | Ligands not selected | 1339 | 23.29% |
| 2 | Amino Acids | 297 | 5.17% |
| 3 | Aliphatic amines | 250 | 4.35% |
| 4 | Pyridines (azines) | 248 | 4.31% |
| 5 | Carboxylic acids | 182 | 3.17% |

Note: “Ligands not selected” is an explicit class label in SRD‑46 and was included; NULL/blank entries were excluded. The relatively large “Ligands not selected” category suggests many ligands lack a specific class assignment, with the next largest groups reflecting common donor sets (amino acids, aliphatic amines, azines).

Total number of distinct ligand classes: I wasn’t able to finalize this count within the time budget. It’s a single distinct-count over the same field (COUNT DISTINCT TRIM(ligand_class_name) with NULL/blank excluded). I can provide the exact number immediately on your go-ahead.

Source: NIST Standard Reference Database 46 (SRD‑46), ligand_card class distribution.

---