I couldn’t make a same-ligand, same-database numeric Co²⁺/Co³⁺ comparison from the SRD-46 records retrieved here, because the overlapping set was empty.

| Finding | Result from SRD-46 search |
|---|---|
| Co²⁺ ID | `metal_33` |
| Co³⁺ ID | `metal_34` |
| Ligands found with cobalt in the retrieved stability set | `ligand_5958`, `ligand_5975`, `ligand_6003` |
| Ligands with both Co²⁺ and Co³⁺ stability data in the retrieved set | None |

The cobalt-containing ligand entries actually returned were all **Co²⁺ only**:

| Ligand | Ligand type | Oxidation states present | Conditions noted |
|---|---|---|---|
| Diethylenetriamine-N(1)-acetic acid (`ligand_5958`) | polydentate amine + carboxylate | Co²⁺ only | 25 °C, I = 0.1 M |
| Ethylenediiminodiacetic acid / EDDA-like (`ligand_5975`) | diamine + 2 carboxylates | Co²⁺ only | 25 °C, I = 0.1 M |
| 6-Oxa-3,9-diazaundecanedioic acid (`ligand_6003`) | diamine + ether + 2 carboxylates | Co²⁺ only | 25 °C, I = 0.1 M |

So, strictly from the retrieved SRD-46 data, I **cannot report numeric Δlogβ = logβ(Co³⁺) − logβ(Co²⁺)** for shared ligands, because no such pair appeared.

That said, the **prediction** for a new polydentate amine ligand is still clear from crystal-field and charge-density arguments:

| Metal ion | Electronic picture | Expected behavior with a polydentate amine |
|---|---|---|
| Co²⁺ | usually high-spin d⁷ | Should form complexes readily, but with more modest thermodynamic stability |
| Co³⁺ | typically low-spin d⁶ in octahedral amine fields | Expected to bind much more strongly and often become very inert kinetically |

**Prediction:** a new multidentate amine ligand should bind **Co³⁺ much more strongly than Co²⁺**, likely by a large margin if it enforces an octahedral N-donor environment. The effect should be strongest for **preorganized, higher-denticity, all-nitrogen ligands** because Co³⁺ gains substantially more ligand-field stabilization and also has higher charge density.

A practical nuance is that **Co³⁺ amine complexes are often kinetically inert**, so experimentally they may form via oxidation of a Co²⁺ complex rather than by rapid direct equilibration.

Source: **NIST SRD-46** retrieved stability-constant records.

---