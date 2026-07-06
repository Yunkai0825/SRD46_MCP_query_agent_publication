Short answer: I wasn’t able to complete the Co(II)–bipyridine join within this turn, so I can’t yet report the Co(II)-specific measurement count or log K range from SRD‑46.

What I did confirm in SRD‑46
- Cobalt(II) is present as metal_33 (Co2+), with broad coverage overall (ligand_count 977; vlm_count 2977).
- Multiple bipyridyl ligands are present and data-rich overall (counts below are total measurements across all metals, not Co(II)-specific):

| Ligand ID | Ligand name | Class | Total VLM measurements (all metals) |
|---|---|---|---|
| ligand_8156 | 2,2'-Bipyridyl | Bipyridines | 178 |
| ligand_8161 | 4,4'-Bipyridyl | Bipyridines | 3 |
| ligand_8157 | 2,3'-Bipyridyl | Bipyridines | 1 |
| ligand_8158 | 2,4'-Bipyridyl | Bipyridines | 1 |
| ligand_8159 | 3,3'-Bipyridyl | Bipyridines | 1 |
| ligand_8160 | 3,4'-Bipyridyl | Bipyridines | 1 |
| ligand_8162 | 4,4'-Dimethyl-2,2'-bipyridyl | Bipyridines | 4 |
| ligand_8172 | 6,6'-Bis(aminomethyl)-2,2'-bipyridyl | Bipyridines | 20 |

Given the substantial overall coverage for 2,2'-bipyridyl, Co(II) entries are very likely present, but I have not yet verified this directly or aggregated the Co(II)-only log K values.

What I still need to do (1 quick step)
- Run the system catalog and stability query scoped to Co(II) (metal_33) and the bipyridyl isomers (ligand_8156, 8157, 8158, 8159, 8160, 8161) to:
  - count independent measurements (distinct VLM IDs) for Co(II)–bipyridine complexes, and
  - extract the minimum and maximum reported log K values (and note temperature/ionic strength ranges if helpful).

If you’d like, I can run that single query next and return a compact table with:
- ligand,
- species stoichiometry (MLx),
- number of independent measurements, and
- min–max log K (with conditions).

Source: NIST Standard Reference Database 46 (SRD‑46), Thermodynamics of Metal Complexes.

---