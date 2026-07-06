Excluding **H⁺**, the metal ion with the largest number of different ligands studied in **NIST SRD-46** is **Cu²⁺** (`metal_41`).

| Rank | Metal ion | SRD-46 ID | Distinct ligands studied |
|---|---|---:|---:|
| 1 | Cu²⁺ | `metal_41` | 1951 |
| 2 | Ni²⁺ | `metal_112` | 1369 |
| 3 | Zn²⁺ | `metal_208` | 1169 |
| 4 | Co²⁺ | `metal_33` | 977 |
| 5 | Cd²⁺ | `metal_26` | 818 |
| 6 | Ag⁺ | `metal_2` | 649 |
| 7 | Ca²⁺ | `metal_25` | 644 |
| 8 | Mg²⁺ | `metal_92` | 508 |
| 9 | Mn²⁺ | `metal_94` | 486 |
| 10 | Pb²⁺ | `metal_125` | 470 |

If you include **H⁺**, it is larger still, but it is usually excluded for this kind of “metal ion” comparison.

| Species | SRD-46 ID | Distinct ligands studied |
|---|---|---:|
| H⁺ | `metal_68` | 4081 |

SRD-46 also directly confirms `metal_41` as **Cu²⁺**, with **1951 ligand partners**. Chemically, that makes sense: Cu²⁺ is one of the most extensively studied coordination ions because of its importance in analytical, bioinorganic, and environmental chemistry.

**Source:** NIST SRD-46, computed from `ligandmetal_card` by counting distinct `ligand_id` per `metal_id`, with confirmation from `inspect_card(metal_41)`.

---