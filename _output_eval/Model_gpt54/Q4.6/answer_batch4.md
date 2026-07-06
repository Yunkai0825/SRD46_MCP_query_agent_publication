I could not rigorously identify true Irving–Williams violations from the SRD-46 data retrieved so far.

What the database work supports:

| Finding | Evidence from SRD-46 |
|---|---|
| The relevant divalent metals are present | Mn²⁺ = `metal_94`, Fe²⁺ = `metal_62`, Co²⁺ = `metal_33`, Cu²⁺ = `metal_41`, Ni²⁺ = `metal_112`; Zn²⁺ is also present in the DB but its ID was not resolved in the completed run |
| A usable shared ligand was found | Glycine = `ligand_5760` |
| Glycine has broad cross-metal coverage | Retrieved summaries show glycine has data for Mn²⁺, Fe²⁺, Co²⁺, Cu²⁺, and Ni²⁺ in the database |
| Preliminary trend | The retrieved summary states the current signal is broadly consistent with `Mn < Fe < Co < Cu`; no inversion was confirmed |

So, based on the retrieved SRD-46 evidence, **no confirmed exception has yet been demonstrated**.

Why I’m stopping short of claiming violations:
- The workflow did **not recover the actual matched numeric logK/β values** for a full six-metal, like-for-like comparison.
- Zn²⁺ was not fully resolved into the same matched dataset.
- For Irving–Williams, apparent “violations” are only meaningful if the constants are compared for the **same ligand, same stoichiometry/beta definition, same protonation model, same solvent, same temperature, and same ionic strength**.

Most likely sources of apparent exceptions if they appear on follow-up:

| Likely cause | Why it can invert the expected order |
|---|---|
| Condition mismatch | Different ionic strengths, electrolytes, or temperatures can shift measured logK enough to make neighboring metals swap order |
| Proton-linked/speciation differences | Amino-acid ligands like glycine have multiple protonation states, so non-identical equilibrium definitions can look like stability anomalies |
| Fe²⁺ redox instability | Partial oxidation to Fe³⁺ or hydrolysis can distort the reported Fe²⁺ constants |
| Ni²⁺ kinetic effects | Slow ligand-exchange can lead to underestimated equilibrium constants if equilibration is incomplete |
| Ligand-specific donor effects | Soft/π-accepting ligands, constrained chelates, or unusual steric/preorganization effects can favor Zn²⁺ or suppress Ni²⁺/Cu²⁺ relative to the textbook trend |

Chemically, the most plausible real exceptions would come from **ligand-specific structural effects**, not from a breakdown of the Irving–Williams idea itself. In practice, many “violations” in curated databases turn out to be **comparison artifacts** caused by mismatched equilibrium definitions or experimental media.

If you want, I can do a focused follow-up on **glycine (`ligand_5760`)** or on a stronger shared ligand such as **EDTA/NTA/ammonia/imidazole** once the exact SRD-46 names/IDs are resolved, and extract the matched numeric constants to test for genuine violations.  

*Source: NIST SRD-46 / IUPAC Stability Constants Database tool results retrieved in this session.*

---