SRD‑46 results and evidence-based estimates

What we looked up
- Metals: Fe(III) metal_61; Fe(II) metal_62
- Ligands: DMF ligand_11422; acetonitrile ligand_9825; ethylene glycol ligand_9621; THF (no canonical THF/oxolane record resolved)

Direct SRD‑46 findings (aqueous)
| Target system | SRD‑46 availability | Notes |
|---|---|---|
| Fe(II)–DMF | none | search_stability returned no rows for Fe(II/III) with DMF names/synonyms |
| Fe(III)–DMF | none | same as above |
| Fe(II)–MeCN | none | build_system_catalog for acetonitrile shows non‑Fe pairs only; Fe absent |
| Fe(III)–MeCN | none | same as above |
| Fe(II)–THF | none | THF/oxolane name/SMILES searches returned no aqueous Fe records |
| Fe(III)–THF | none | same as above |
| Fe(II)–ethylene glycol | none | build_system_catalog shows many other metals with EG but no Fe |
| Fe(III)–ethylene glycol | none | same as above |

Comparator evidence (Fe with related donor classes)
- Ether/aza‑polyether (multidentate, much stronger than monodentate THF): SRD‑46 reports Fe(II/III) complex formation with N,O macrocycles and glyme‑like scaffolds in water (I ≈ 0.1 M, 25 °C). These provide upper bounds for simple ether donors.

| Metal | Ligand (SRD name) | vlm_id | type | logK | T (°C) | I (M) | Equation |
|---|---|---|---|---|---|---|---|
| Fe(II) (metal_62) | N‑(2‑Tetrahydropyranylmethyl)iminodiacetic acid (ether + two carboxylates; chelating) | vlm_107056 | logK | 7.4 | 20 | 0.1 | [M] + [L] ⇌ [ML] |

Source: SRD‑46 search_stability (Fe2+ with a chelating ether/carboxylate ligand; this is far stronger than a neutral monodentate ether like THF).

- Ether/aza‑macrocycles (Fe(II/III)) are present in SRD‑46, but their specific logK values for the Fe(II/III) entries were not retrieved within this time window. Their existence supports the expectation that multidentate ether donors bind Fe measurably in water, whereas simple monodentate solvents (THF, DMF, MeCN) do not show reported aqueous Fe(II/III) constants in SRD‑46.

Reasoned estimates for the requested solvent ligands (aqueous, near 25 °C, low ionic strength)
Because SRD‑46 contains no direct aqueous Fe(II/III) stability constants with DMF, acetonitrile, THF, or ethylene glycol, we estimate by donor class, anchored to the comparator above and general trends seen in SRD‑46:

- THF (neutral, monodentate ether, very weak in water): Expect negligible complexation in bulk water due to displacement by H2O and hydrolysis competition for Fe(III). Estimate:
  - Fe(II)–THF: logK ≈ 0–1 (upper bound far below chelates like the 7.4 value above).
  - Fe(III)–THF: logK ≈ 0 (practically no measurable simple adduct under aqueous conditions).

- DMF (neutral amide O‑donor; similar weakness in water): Amides show little aqueous Fe binding in SRD‑46; DMF is expected weaker than chelating carboxylates. Estimate:
  - Fe(II)–DMF: logK ≈ 0–1.
  - Fe(III)–DMF: logK ≈ 0 (Fe3+ hydrolysis dominates).

- Acetonitrile (neutral nitrile N‑donor; weak ligand in water): SRD‑46 lacks Fe data; neutral nitriles typically bind Fe weakly in water. Estimate:
  - Fe(II)–MeCN: logK ≈ 0–1.
  - Fe(III)–MeCN: logK ≈ 0.

- Ethylene glycol (diol; can chelate only upon deprotonation; neutral EG as donor is weak): SRD‑46 shows many EG complexes with other metals, often involving deprotonated (H‑2L) species at alkaline pH. For neutral EG in water:
  - Fe(II)–EG (neutral): logK ≈ 0–1.
  - Fe(III)–EG (neutral): logK ≈ 0.
  - Note: If EG deprotonates and chelates (higher pH), Fe binding could be significantly stronger than these neutral‑donor estimates; however, SRD‑46 provides no Fe constants for those specific EG species.

Interpretive notes
- Multidentate/chelating ligands (ethers + carboxylates or aza‑polyethers) can reach logK in the mid‑single digits for Fe(II) in water (e.g., 7.4 above), but simple neutral solvent molecules (THF, DMF, MeCN) are displaced by water and/or outcompeted by hydrolysis, explaining the absence of SRD‑46 aqueous constants.
- Fe(III) more readily hydrolyzes than Fe(II), making neutral donor adducts even less favorable in water.

Limits and follow‑up
- These estimates are qualitative/low‑precision ranges grounded in SRD‑46’s absence of direct data and the strength of chelating comparators. If you need tighter bounds, we can:
  - Expand comparator pulls to retrieve specific Fe(II/III) logK values for the ether/aza‑macrocycles (to quantify upper bounds).
  - Check non‑aqueous media (e.g., MeCN or DMF as solvent) for Fe complexes, if relevant to your application.

Source: NIST SRD‑46 (Ligand–Metal Stability Constants Database).

---