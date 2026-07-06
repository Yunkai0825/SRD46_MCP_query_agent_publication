SRD-46 has enough data to compare **iron and copper by oxidation state**, but not as a single element-only property. In this database, the relevant cation entries are:

| Metal state | SRD-46 metal_id | Cards |
|---|---:|---:|
| Cu(I) | metal_42 | 285 |
| Cu(II) | metal_41 | 8963 |
| Fe(II) | metal_62 | 667 |
| Fe(III) | metal_61 | 1473 |

A few immediate takeaways:

| Observation | Evidence from SRD-46 |
|---|---|
| Copper is much more heavily represented than iron overall | Cu(II) alone has 8963 cards vs Fe(III) 1473 and Fe(II) 667 |
| Cu(II) is the dominant copper oxidation state in the database | Cu(II): 8963 cards vs Cu(I): 285 |
| Fe(III) is better represented than Fe(II) | Fe(III): 1473 vs Fe(II): 667 |
| Cu(I) data are relatively sparse | Only 285 cards |

The Fe/Cu distribution in `ligandmetal_card` is:

| Metal name in SRD-46 | Count | Percent of Fe/Cu rows |
|---|---:|---:|
| Cu^[2+] | 8963 | 78.64% |
| Fe^[3+] | 1473 | 12.92% |
| Fe^[2+] | 667 | 5.85% |
| Cu^[+] | 285 | 2.50% |
| Cu^[3+] | 10 | 0.09% |

There are also ligands for which **all four common oxidation states** appear, enabling fairer side-by-side comparison later. Examples include:

| Ligand | ligand_id | Fe(III) cards | Fe(II) cards | Cu(II) cards | Cu(I) cards |
|---|---:|---:|---:|---:|---:|
| Hydroxide ion | ligand_10076 | 38 | 13 | 34 | 3 |
| Thiocyanate | ligand_10092 | 39 | 2 | 21 | 4 |
| Histidine | ligand_5898 | 1 | 6 | 50 | 3 |
| Glycine | ligand_5760 | 6 | 14 | 30 | 1 |
| Chloride ion | ligand_10163 | 13 | 2 | 19 | 14 |
| 2,2'-Bipyridyl | ligand_8156 | 1 | 10 | 33 | 2 |
| 1,10-Phenanthroline | ligand_8191 | 9 | 7 | 22 | 1 |

## Bottom line

| Metal | Practical SRD-46 comparison summary |
|---|---|
| Iron | Mostly represented as Fe(III), with moderate Fe(II) coverage |
| Copper | Overwhelmingly represented as Cu(II), with limited Cu(I) coverage |

So, **within SRD-46, copper has far broader stability-constant coverage than iron**, especially for **Cu(II)** complexes. Iron is represented mainly as **Fe(III)**, while **Cu(I)** is much less documented than **Cu(II)**. Chemically, that pattern is sensible: Cu(II) and Fe(III) are both common, relatively robust aqueous states, whereas Cu(I) and Fe(II) are more condition-sensitive.

If you want, I can now do a **true apples-to-apples comparison** by pulling matched stability constants for a shared ligand set such as **glycine, chloride, thiocyanate, bipyridyl, or phenanthroline** from SRD-46.

---