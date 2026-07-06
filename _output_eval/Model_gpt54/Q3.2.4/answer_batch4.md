Using the SRD-46 survey results, the strongest supported pattern is:

| Metal | Database coverage pattern | Qualitative stability trend across ligand classes |
|---|---|---|
| Fe(III) | Rich in hard, multidentate O-donor systems | small O,N donors < IDA-type < NTA < EDTA-like/polyaminocarboxylates < macrocyclic aminocarboxylates ≲ strongly Fe(III)-selective hard-O ligands such as hydroxamates, catecholates/phenolates, hydroxypyridyls, and phosphonate-rich ligands |
| Fe(II) | Broader spread across common aminocarboxylates, amino acids, and some softer/N-donor space | stability still rises with denticity/preorganization, but Fe(II) is less selectively driven toward the hardest O-donor classes than Fe(III) |

### What is actually available in SRD-46
The database inventory shows:

| Coverage finding | SRD-46 observation |
|---|---|
| Iron ions present | Fe(II) = `metal_62`; Fe(III) = `metal_61` |
| Fe(III)-rich classes | hydroxamates, catecholate/phenolate/salicylate systems, hydroxypyridyl ligands, phosphonate-rich ligands, siderophore-like O-donor chelators |
| Shared Fe(II)/Fe(III) space | amino acids, small O,N donors, IDA/NTA/EDTA families, macrocyclic aminocarboxylates, glyphosate, bicine |
| Fe(II) edge space | some S-containing / softer-donor ligands such as cysteine, methionine-related ligands, mercaptoethyl-IDA, methylthioethyl-IDA |

### Numeric support available
The network dump was mainly inventory-level, and direct `search_stability` queries did not return a broad numeric table under matched aqueous conditions. Only one explicit anchor constant was surfaced in the retrieved material:

| System | Reported constant |
|---|---|
| Fe(III)–`ligand_6047` | logK = 32.7 for ML |

That ligand was described in the retrieved summary as a multidentate mixed N/O ligand with aromatic hard O donors, which is fully consistent with the “very strong Fe(III) binding” end of the trend.

### Thermodynamic interpretation
The ordering is well explained by standard coordination thermodynamics:

| Factor | Effect on Fe(III) vs Fe(II) |
|---|---|
| HSAB | Fe(III) is smaller, more highly charged, and harder than Fe(II), so deprotonated O donors bind especially strongly to Fe(III): carboxylate, phenolate/catecholate, hydroxamate, phosphonate |
| Chelate effect | Stability generally increases with denticity: IDA < NTA < EDTA-like < higher-denticity / preorganized systems |
| Preorganization / macrocyclic effect | Rigid, preorganized ligands often gain extra stability from lower entropic and reorganization penalties |
| Ligand-field effects | Fe(III) is commonly high-spin d5, so LFSE discrimination is often modest; electrostatics, donor hardness, and chelation dominate. Fe(II) (d6) can gain more from stronger-field and N-donor environments, helping explain some Fe(II)-favoring edge cases |
| Ligand charge / deprotonation | Highly anionic ligands strongly stabilize Fe(III); this is why hydroxamates, catecholates, and phosphonates are standout classes |

### Edge cases worth noting
| Edge case | Why it matters |
|---|---|
| Hydroxamates / catecholates / hydroxypyridyls | These are classic Fe(III)-selective outliers because they combine hard O donors, often high denticity, and substantial ligand charge |
| S-donor ligands | Softer donors are less favored by Fe(III), so when they appear they are more plausible in Fe(II) chemistry |
| Aminocarboxylates vs aromatic O-donors | EDTA-like systems are strong because of chelation and charge, but some Fe(III)-selective aromatic hard-O ligands can compete with or exceed them because they are exceptionally well matched to Fe(III) hardness |
| Macrocycles | May outperform open-chain analogues through preorganization even when donor types are similar |

### Bottom line
SRD-46 supports a clear qualitative conclusion: **Fe(III) systems in the database are concentrated in the strongest hard-O, multidentate ligand classes, whereas Fe(II) is represented more broadly in common aminocarboxylate and some softer/N-donor chemistry.** The main ordering is driven by **HSAB matching + chelate/preorganization effects**, while **ligand-field effects matter more for Fe(II) edge cases than for Fe(III)**.

If you want, I can do a second pass focused just on **named exemplar ligands** for each class (e.g., acetate, oxalate, NTA, EDTA, hydroxamates, salicylates, phosphonates) and tabulate the specific Fe(III)/Fe(II) systems present in SRD-46.

---