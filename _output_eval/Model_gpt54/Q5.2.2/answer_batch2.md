I checked SRD-46 for protein-type ligands, including **transferrin**, **lactoferrin**, **conalbumin**, **albumin**, and **metallothionein**.

## What I found

| Check | Result |
|---|---|
| Direct ligand search for transferrin / albumin / metallothionein names | No hits |
| Broader ligand search for “protein” / “peptide” / protein-family names | No protein-name hits |
| Stability search for protein-like ligand names | No transferrin/albumin/etc. hits |
| Citation search for protein-related terms | A few generic literature hits mentioning proteins/peptides, but not verified transferrin ligand entries |

## What *is* present

SRD-46 does contain some **small peptide ligands**, not full protein entries. For example, I found one peptide-like ligand with Cu(II) and Zn(II) stability data:

| Metal | Ligand (truncated SRD name) | Constant type | logK | T (°C) | I (M) |
|---|---|---:|---:|---:|---:|
| Cu(II) | L-Alanyl-L-aspartyl-L-serylglycyl-L-glutamylglycyl-L-aspart… | ML | 7.21 | 25 | 0.1 |
| Zn(II) | L-Alanyl-L-aspartyl-L-serylglycyl-L-glutamylglycyl-L-aspart… | ML | 3.2 | 25 | 0.1 |

There were also protonation constants for that peptide ligand.

## Bottom line

| Question | Answer |
|---|---|
| Does SRD-46 appear to contain transferrin binding data? | I did **not** find evidence of it |
| Does SRD-46 contain metal–protein binding data in general? | Not obvious for full proteins; it seems to include at least some **peptides**, but I did not find clear **macromolecular protein** entries |

So the safest conclusion is: **SRD-46 does not appear to have explicit transferrin (or similar full protein) metal-binding entries, based on the searchable ligand and stability records I checked.** It seems more focused on small-molecule ligands and some peptides rather than large proteins.

A chemistry note: that pattern is plausible, because equilibrium-constant databases often emphasize well-defined solution complexes with small ligands; full proteins like transferrin introduce site heterogeneity, conformational effects, and conditional binding behavior that are harder to store as simple β values.

Source: **NIST SRD-46**.

---