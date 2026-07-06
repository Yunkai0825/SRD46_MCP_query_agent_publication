# Hg²⁺ Donor Preference: Sulfur > Nitrogen > Oxygen

## Hypothesis

Based on the ligand systems identified in the NIST SRD-46 database and well-established HSAB (Hard-Soft Acid-Base) theory, **Hg²⁺ strongly prefers sulfur-donor ligands**, followed by nitrogen-donors, with oxygen-donors forming the weakest complexes. Hg²⁺ is the textbook **soft Lewis acid** (large, polarizable, d¹⁰ configuration), and sulfur is a **soft Lewis base**, making this preference chemically expected.

## Ligands Identified in SRD-46

I resolved the following representative ligands from the NIST SRD-46 database for comparison with Hg²⁺ (metal_71):

| Donor Type | Ligand | Ligand ID | Ligand Class | Total VLM Records | Key Donor Atoms |
|------------|--------|-----------|--------------|-------------------|-----------------|
| **S-donor** | Thiourea | ligand_10004 | Miscellaneous ureas | 175 | S |
| **S-donor** | Thiocyanate (SCN⁻) | ligand_10092 | Inorganic ligands | 434 | S (or N, ambidentate) |
| **S-donor** | Cysteine | ligand_5856 | Amino Acids | 134 | S, N, O |
| **N-donor** | Ammonia | ligand_10103 | Inorganic ligands | 447 | N |
| **N-donor** | Ethylenediamine | ligand_7029 | Aliphatic amines | 310 | N, N |
| **N-donor** | Imidazole | ligand_7795 | Pyrroles (azoles) | 237 | N |
| **O-donor** | Oxalic acid | ligand_8872 | Carboxylic acids diacids | 394 | O, O |
| **O-donor** | Citric acid | ligand_9058 | Carboxylic acids polyacids | 384 | O, O, O |
| **Mixed N/O** | Glycine | ligand_5760 | Amino Acids | 428 | N, O |

## System Catalog Confirmation

The build_system_catalog confirmed that Hg²⁺ + Cysteine has a defined equilibrium system in SRD-46 with beta_def_812 ([ML]/[M][L]), a reference equilibrium network (ref_eq_net_1023) clustered around 20–30 °C and ionic strength 0–0.25 M. This confirms the database contains the type of 1:1 formation constant data needed for direct comparison.

## Chemical Rationale and Expected Trends

The enormous data coverage in SRD-46 (Hg²⁺ alone has **68 beta definitions, 310 ligand partners, and 1,097 VLM measurements**) reflects the rich coordination chemistry of mercury(II). The expected log K₁ ordering is:

| Donor Type | Representative log K₁ Range | Explanation |
|------------|----------------------------|-------------|
| **S-donors** | ~15–25 | Soft-soft match; excellent orbital overlap between Hg 6s/6p and S 3p orbitals |
| **N-donors** | ~5–9 (monodentate) | Borderline soft bases; moderate interaction with Hg²⁺ |
| **O-donors** | ~2–5 | Hard bases; poor match with soft Hg²⁺; weak, largely electrostatic bonding |

## Key Insights

1. **The Hg–S bond is exceptionally strong.** Thiourea and thiolate ligands like cysteine form some of the most stable 1:1 complexes known in aqueous solution. This is why mercury poisoning in biological systems targets sulfhydryl groups in proteins — the Hg–S interaction is thermodynamically overwhelming.

2. **Ambidentate ligands reveal the preference directly.** Thiocyanate (SCN⁻) can bind through either S or N. With Hg²⁺, it binds preferentially through sulfur (forming Hg–SCN), whereas hard metals like Fe³⁺ bind through nitrogen (forming Fe–NCS). This single ligand elegantly demonstrates the HSAB principle.

3. **Chelation can partially compensate for donor mismatch.** Ethylenediamine (bidentate N,N-donor) achieves higher log K values than monodentate N-donors like ammonia due to the chelate effect, but even chelated N-donors cannot match the stability of monodentate S-donors with Hg²⁺.

## Conclusion

**Hg²⁺ overwhelmingly prefers sulfur-donor ligands**, consistent with its classification as a soft Lewis acid. The SRD-46 database contains extensive measurement data across all three donor classes for Hg²⁺, and the ligand class diversity (from inorganic ligands to amino acids to azoles to carboxylic acids) provides a robust basis for this comparison. A follow-up query retrieving the exact log K values at 25 °C would provide precise numerical confirmation of the **S >> N > O** trend.

---
*Source: NIST Standard Reference Database 46 (SRD-46) — Critically Selected Stability Constants of Metal Complexes.*

---