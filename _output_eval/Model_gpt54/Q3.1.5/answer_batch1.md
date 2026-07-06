I’m sorry, but I can’t reliably answer this from the SRD-46 data retrieved so far.

| Issue | What happened |
|---|---|
| Metal resolution failed | `search_metals` returned no resolved Ca/Cu entities |
| Ligand resolution failed | `search_ligands` returned no resolved candidate ligands |
| Catalog step failed | `build_system_catalog` needs valid resolved IDs; guessed IDs were not validated |
| Execution blocked | I don’t yet have trustworthy resolved entity IDs to run the comparison properly |

Because of that, I’d risk inventing rankings if I named “best” Ca-selective ligands from SRD-46 now.

What I *can* say chemically, at a high level, is that ligands with mostly oxygen donors and lower soft/borderline-metal affinity are more likely to favor Ca²⁺ over Cu²⁺, whereas aminopolycarboxylates like NTA/EGTA typically bind Cu²⁺ very strongly and are usually poor choices if you want weak Cu²⁺ affinity.

| Likely more Ca-favoring class | Likely poor choice for weak Cu affinity |
|---|---|
| carboxylates / hydroxycarboxylates / some hard oxygen-donor anions | NTA, EGTA, and related aminopolycarboxylates |

If you want, I can continue and try a different SRD-46 discovery route to resolve the canonical Ca/Cu and ligand names, then produce a proper ranked table with matched-condition log β values and citations from SRD-46.

---