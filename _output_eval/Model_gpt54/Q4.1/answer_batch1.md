SRD-46 does **not contain direct Fe(II) or Fe(III) stability constants** for the four target neutral ligands/solvents:

| Ligand | Fe(II) direct SRD-46 result | Fe(III) direct SRD-46 result | Notes |
|---|---:|---:|---|
| DMF (N,N-dimethylformamide) | not found | not found | no matching stability records |
| Acetonitrile | not found | not found | no matching stability records |
| THF | not found | not found | no matching stability records |
| Ethylene glycol | not found | not found | no matching stability records |

I also checked likely analog names/classes in SRD-46 (amides, nitriles, ethers, simple polyols) and did **not** retrieve Fe(II)/Fe(III) stability entries for those either. So any numerical assessment beyond “not available” has to be an **estimate**, inferred from Fe hard/soft preferences and the database’s general pattern that Fe(III) binds O-donors much more strongly than Fe(II), while weak neutral monodentate donors are often too weak to be well represented in aqueous stability compilations.

## Reasoned estimates

These estimates are for **aqueous-type stability constants of simple 1:1 adducts** and should be treated as **order-of-magnitude log β₁ ranges**, not curated SRD-46 values.

| Ligand | Donor type | Fe(II) estimated log β₁ | Fe(III) estimated log β₁ | Confidence | Rationale |
|---|---|---:|---:|---|---|
| DMF | neutral O-donor amide | 0 to 1 | 1 to 3 | low | Carbonyl O can bind, but neutral amides are weak in water; Fe(III) should exceed Fe(II) because of higher charge density |
| Acetonitrile | neutral N-donor nitrile | ≤0 to 0.5 | 0 to 1.5 | low | Nitriles are weak donors to hydrated Fe ions; aqueous competition from water is strong |
| THF | neutral ether O-donor | ≤0 | 0 to 1 | very low | THF is a weak ether donor and especially poor competitor against hydration in water |
| Ethylene glycol (neutral) | neutral O,O donor diol | 0.5 to 2 | 1 to 4 | medium-low | Bidentate chelation helps relative to DMF/THF/MeCN, but neutral glycol is still much weaker than deprotonated glycolate/diolate forms |

## Likely strength ranking

For **Fe(II)**:
| Rank | Ligand | Expected relative strength |
|---|---|---|
| 1 | ethylene glycol | strongest of the four |
| 2 | DMF | weak |
| 3 | acetonitrile | very weak |
| 4 | THF | weakest or tied weakest |

For **Fe(III)**:
| Rank | Ligand | Expected relative strength |
|---|---|---|
| 1 | ethylene glycol | strongest, especially if partial deprotonation becomes possible |
| 2 | DMF | weak-moderate |
| 3 | acetonitrile | weak |
| 4 | THF | very weak |

## Important caveat for ethylene glycol

For ethylene glycol, the chemistry can change sharply if the ligand becomes **deprotonated**. Neutral ethylene glycol should bind only modestly, but **alkoxide-containing Fe(III) species** would be much stronger. Those would **not** be the same as the neutral glycol adduct and should not be conflated with a simple FeL β₁.

## Bottom line

| System | Best assessment |
|---|---|
| DMF–Fe(II) | no SRD-46 constant; probably very weak, log β₁ ~ 0–1 |
| DMF–Fe(III) | no SRD-46 constant; weak, log β₁ ~ 1–3 |
| MeCN–Fe(II) | no SRD-46 constant; extremely weak, log β₁ ≤ 0.5 |
| MeCN–Fe(III) | no SRD-46 constant; weak, log β₁ ~ 0–1.5 |
| THF–Fe(II) | no SRD-46 constant; essentially negligible in water, log β₁ ≤ 0 |
| THF–Fe(III) | no SRD-46 constant; very weak, log β₁ ~ 0–1 |
| ethylene glycol–Fe(II) | no SRD-46 constant; weak but aided by chelation, log β₁ ~ 0.5–2 |
| ethylene glycol–Fe(III) | no SRD-46 constant; modest as neutral glycol, log β₁ ~ 1–4 |

Source: **NIST SRD-46 searches returned no direct records for these target systems or close neutral analogs**. The estimates above are therefore reasoned extrapolations anchored to the SRD-46 pattern that weak neutral monodentate ligands are poorly represented and that Fe(III) generally binds O-donors more strongly than Fe(II).  

If you want, I can next do a **more quantitative analog-based bracket** using specific Fe(II)/Fe(III) ligands that *are* present in SRD-46 (e.g., halides, thiocyanate, carboxylates, oxalate) to put tighter upper/lower bounds on each estimated log β.

---