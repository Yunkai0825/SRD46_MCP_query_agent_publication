Excluding the proton entry **H⁺** (which is encoded as a “metal” in SRD-46 for acid–base systems), the **metal ion with the largest number of different ligands studied is Cu²⁺**.

| Rank | Metal ion | Metal ID | Distinct ligands studied |
|---|---|---:|---:|
| 1 | Cu²⁺ | metal_41 | 1951 |
| 2 | Ni²⁺ | metal_112 | 1369 |
| 3 | Zn²⁺ | metal_208 | 1169 |
| 4 | Co²⁺ | metal_33 | 977 |
| 5 | Cd²⁺ | metal_26 | 818 |
| 6 | Ag⁺ | metal_2 | 649 |
| 7 | Ca²⁺ | metal_25 | 644 |
| 8 | Mg²⁺ | metal_92 | 508 |
| 9 | Mn²⁺ | metal_94 | 486 |

For completeness, the raw top row in SRD-46 is actually **H⁺** with **4081** ligands, but that reflects protonation/pKa coverage rather than a conventional metal-ion coordination dataset.

Copper(II) being first is chemically plausible: it is one of the most extensively studied coordination ions because it forms stable complexes with a very broad range of donor atoms and is important in analytical, bioinorganic, and environmental chemistry.

**Source:** NIST SRD-46, aggregated from `ligandmetal_card` using `COUNT(DISTINCT ligand_id)` per `metal_id`.

---