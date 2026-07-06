Based on my thorough search of the NIST SRD-46 database, here is the finding:

---

## Uranium(VI) + Crown Ethers — Stability Constants

**No stability constant data found in NIST SRD-46.**

I searched for all uranium species in the database:

| Metal | ID | Description |
|-------|-----|-------------|
| UO₂²⁺ | metal_195 | Uranyl ion (U(VI)) — 163 ligand partners, 748 measurements |
| U⁴⁺ | metal_193 | Uranium(IV) — 18 ligand partners, 102 measurements |
| UO₂⁺ | metal_196 | Uranyl(V) — 1 ligand partner, 1 measurement |

And all crown ether ligands available (12-crown-4, 15-crown-5, 18-crown-6, benzo-15-crown-5, benzo-18-crown-6, dibenzo-18-crown-6, dicyclohexyl-18-crown-6 variants, etc.). The system catalog returned **zero pairs** for any uranium species with any crown ether ligand.

### Why might this be?

This absence is chemically understandable:

1. **SRD-46 focuses on aqueous-phase equilibrium constants.** Most uranyl–crown ether interaction studies have been conducted in **non-aqueous or mixed solvents** (e.g., extraction/distribution studies in organic phases), which fall outside the scope of this database.

2. **Weak aqueous complexation.** The uranyl ion (UO₂²⁺) is a hard, linear dioxo cation that preferentially coordinates hard oxygen donors in its equatorial plane. Crown ethers, while offering oxygen donors, have a cyclic geometry that is not well-suited to the equatorial coordination preference of uranyl, leading to relatively weak or poorly characterized aqueous-phase complexation.

3. **Crown ether data in SRD-46 is limited overall** — even the most data-rich crown ether (18-crown-6, ligand_9676) has only 76 total measurements across all metals, mostly with alkali and alkaline earth cations where size-selectivity is well established.

For uranyl–crown ether interaction data, you may want to consult extraction chemistry literature or databases focused on non-aqueous/solvent extraction equilibria.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes)*

---