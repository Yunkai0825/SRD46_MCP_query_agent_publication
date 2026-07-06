SRD-46 does **not appear to contain direct Fe(II)/Fe(III) stability constants** for the four target neutral solvent ligands:

| Ligand | Direct SRD-46 Fe(II)/Fe(III) hit? |
|---|---|
| DMF | No |
| Acetonitrile | No |
| THF | No |
| Ethylene glycol | No |

The direct ligand-name searches and Fe-specific stability searches returned no matches for these ligands. Fe coverage in SRD-46 is concentrated in **stronger classical ligands** such as hydroxide, thiocyanate, ammonia, pyridines, amino acids, hydroxy acids, EDTA/NTA-type ligands, catechols, and hydroxamates, rather than weak neutral solvent donors.

## What the database does support

For Fe(II)/Fe(III), the populated ligand space includes:

| Example ligands/classes present for Fe | Implication |
|---|---|
| Ammonia, pyridines, bipyridyl, phenanthroline | Neutral N-donor ligands are represented, but mostly stronger than MeCN |
| Hydroxy acids, catechols, hydroxamates, carboxylates | Hard O-donors and chelators dominate Fe(III) data |
| No obvious DMF / MeCN / THF / ethylene glycol entries | Target systems are likely absent, so estimation must rely on donor-type trends |

## Reasoned estimates

Using Fe coordination chemistry trends and the SRD-46 coverage pattern as anchors:

- **Fe(III)** strongly prefers **hard, anionic O-donors** and binds weakly to neutral solvent ligands unless no better ligands are available.
- **Fe(II)** binds neutral donors somewhat more permissively than Fe(III), but these particular solvents are still weak ligands relative to NH3, pyridines, or chelating N/O donors.
- Expected donor-strength order here is roughly:

| Ligand | Donor type | Expected relative binding to Fe |
|---|---|---|
| Acetonitrile | weak neutral N donor | weak |
| THF | weak neutral ether O donor | very weak |
| DMF | neutral amide O donor | weak to modest |
| Ethylene glycol | neutral O,O donor, potentially chelating | weak to modest, strongest of the four because of chelate effect |

### Estimated log β1 values

These are **reasoned ranges**, not database values:

| Ligand | Fe(II) estimated logβ1 | Fe(III) estimated logβ1 | Rationale |
|---|---:|---:|---|
| Acetonitrile | ~0 to 1 | ~0 to 0.5 | Weak monodentate nitrile donor; Fe(III) disfavors soft/neutral N donors |
| THF | ~0 to 0.5 | ~0 to 0.5 | Very weak neutral ether donor; likely only outer-sphere or highly labile inner-sphere binding |
| DMF | ~0.5 to 1.5 | ~0.5 to 1.5 | Amide O donor stronger than THF/MeCN, but still much weaker than anionic O ligands |
| Ethylene glycol | ~1 to 2 | ~1.5 to 3 | Neutral O,O chelation gives some stabilization; still far below glycolate/polyolato or carboxylate complexes |

## Best interpretation by system

| System | Assessment |
|---|---|
| DMF–Fe(II) | Plausible weak adduct formation; likely measurable only in donor solvents or under low-competition conditions |
| DMF–Fe(III) | Also possible, but strongly outcompeted by hydrolysis and harder anionic ligands in aqueous systems |
| MeCN–Fe(II) | Weak but chemically plausible; likely labile solvato complexes rather than strongly defined aqueous stability constants |
| MeCN–Fe(III) | Probably very weak in water; hydrolysis/anion coordination should dominate |
| THF–Fe(II) | Very weak; mostly relevant in nonaqueous solvation chemistry |
| THF–Fe(III) | Extremely weak as a discrete competitive ligand |
| Ethylene glycol–Fe(II) | Most credible of the four for a real measurable β1 because it can chelate |
| Ethylene glycol–Fe(III) | Stronger than with Fe(II), but still much weaker than deprotonated O-donor chelators |

## Practical conclusion

If you need a single working ranking for **Fe²⁺ complexation strength** among these solvents, I would use:

| Ligand | Relative Fe(II) affinity |
|---|---|
| THF | lowest |
| Acetonitrile | low |
| DMF | low-to-moderate |
| Ethylene glycol | highest |

and for **Fe³⁺**:

| Ligand | Relative Fe(III) affinity |
|---|---|
| THF | lowest |
| Acetonitrile | very low |
| DMF | low |
| Ethylene glycol | modest but still weak vs classical Fe(III) ligands |

So the most defensible summary is:

| Ligand | Fe(II) logβ1 estimate | Fe(III) logβ1 estimate |
|---|---:|---:|
| DMF | 0.5–1.5 | 0.5–1.5 |
| Acetonitrile | 0–1 | 0–0.5 |
| THF | 0–0.5 | 0–0.5 |
| Ethylene glycol | 1–2 | 1.5–3 |

Source: **NIST SRD-46** search results showed no direct constants for these target ligand systems; estimates are inferred from the Fe ligand classes present in SRD-46 and standard donor-type/chelate-effect trends.

If you want, I can do one more pass in SRD-46 focused specifically on **closest Fe²⁺ analog ligands** for each class:
- amides for DMF,
- nitriles / pyridines for MeCN,
- ethers for THF,
- diols / hydroxy alcohols for ethylene glycol.

---