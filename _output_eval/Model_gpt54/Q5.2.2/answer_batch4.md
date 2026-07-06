SRD-46 appears to have **no direct entries for intact metal–protein systems such as transferrin**.

| Check | Result |
|---|---|
| Ligand search for transferrin / lactoferrin / albumin / ferritin / metallothionein and common variants | No matches |
| SQL text search of `ligand_name_SRD`, `synonym_iupac_name`, and `synonym_common_name` for those protein terms | No matches |
| Ligand-class distribution | Protein-like classes do exist, but as **small biomolecule classes** such as `Peptides` (157 entries) and `polypeptides` (98 entries), not named proteins like transferrin |

There were a few **citation hits** containing protein-related words, but they do **not** establish indexed transferrin-type ligand records:

| shortcut | citation evidence |
|---|---|
| 43Eaa | Contains “Proteins, Amino Acids and Peptides” |
| 72ESM | Contains “Membranes” symposium wording |
| 88CCI | Protein-related wording in citation metadata |

So the safest conclusion is:

| Conclusion | Interpretation |
|---|---|
| Direct transferrin data | Not found in SRD-46 |
| Intact protein metal binding coverage | Likely not a core SRD-46 focus |
| Related biological ligands | Yes — SRD-46 does include **amino acids, peptides, polypeptides**, and other smaller biologically relevant ligands |

Chemistry-wise, that makes sense: equilibrium databases like SRD-46 usually favor **well-defined small-molecule ligands** with standardized stoichiometry and conditional constants, whereas intact proteins such as transferrin have more heterogeneous binding behavior and assay-dependent conditions.

**Source:** NIST SRD-46 ligand index, citation search, and ligand-class distribution.

---