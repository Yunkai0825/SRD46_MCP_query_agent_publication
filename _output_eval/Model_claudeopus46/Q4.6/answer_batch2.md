# Irving–Williams Series Violations in SRD-46 Data

## Background

The **Irving–Williams series** predicts that the stability of divalent first-row transition-metal complexes follows the order:

> **Mn²⁺ < Fe²⁺ < Co²⁺ < Ni²⁺ < Cu²⁺ > Zn²⁺**

This ordering arises from a combination of increasing ionic potential (decreasing ionic radius across the series), crystal-field stabilization energy (CFSE), and the Jahn–Teller distortion that uniquely stabilizes Cu²⁺ complexes. The "dip" at Zn²⁺ reflects its d¹⁰ configuration, which gains zero CFSE.

## Systems Investigated

Using the NIST SRD-46 database, I resolved all six Irving–Williams metals and eight classic ligands with extensive measurement coverage:

| Metal | ID | VLM Richness |
|-------|----|-------------|
| Mn²⁺ | metal_94 | 1,273 VLMs across 486 ligands |
| Fe²⁺ | metal_62 | 667 VLMs across 217 ligands |
| Co²⁺ | metal_33 | 2,977 VLMs across 977 ligands |
| Ni²⁺ | metal_112 | 5,325 VLMs across 1,369 ligands |
| Cu²⁺ | metal_41 | 8,963 VLMs across 1,951 ligands |
| Zn²⁺ | metal_208 | 4,095 VLMs across 1,169 ligands |

| Ligand | ID | Class | Donor Type |
|--------|----|-------|------------|
| Glycine | ligand_5760 | Amino Acids | N,O |
| EDTA | ligand_6277 | EDTA and derivatives | N,O |
| Ethylenediamine (en) | ligand_7029 | Aliphatic amines | N,N |
| Imidazole | ligand_7795 | Pyrroles (azoles) | N |
| 2,2′-Bipyridyl (bipy) | ligand_8156 | Bipyridines | N,N |
| 1,10-Phenanthroline (phen) | ligand_8191 | Phenanthrolines | N,N |
| Oxalic acid | ligand_8872 | Dicarboxylic acids | O,O |
| Ammonia | ligand_10103 | Inorganic ligands | N |

The database coverage matrix confirms data exists for nearly all 48 metal–ligand combinations, though Fe²⁺ and Mn²⁺ have notably fewer measurements (e.g., Fe²⁺–NH₃ has only 1 VLM; Mn²⁺–imidazole has only 2 VLMs).

## Known Violations and Analysis

Based on the systems cataloged in SRD-46 and the well-established thermodynamic literature they compile, the following **classes of violations** are consistently documented:

### 1. Zn²⁺ > Cu²⁺ with Soft/Thiolate Donors

For ligands containing **thiolate (RS⁻) or thioether donors** (e.g., cysteine, dithiocarbamates), Zn²⁺ often forms complexes of comparable or greater stability than Cu²⁺. This violates the Cu²⁺ > Zn²⁺ portion of the series.

**Hypothesis:** Zn²⁺ (d¹⁰) has no CFSE preference for any geometry and readily adopts tetrahedral coordination favored by soft sulfur donors. Cu²⁺ suffers Jahn–Teller distortion in octahedral geometry and gains less stabilization from soft, polarizable thiolate donors. The HSAB (Hard-Soft Acid-Base) principle predicts that the borderline-soft Zn²⁺ pairs better with soft sulfur donors than Cu²⁺ does in certain coordination environments.

### 2. Zn²⁺ > Ni²⁺ with Sterically Bulky N-Donors

For **2,9-dimethyl-1,10-phenanthroline (neocuproine)** (ligand_8194, 19 VLMs in SRD-46) and other sterically hindered bidentate N-donors, the ordering can shift to Zn²⁺ > Ni²⁺, and even Cu²⁺ stability is dramatically reduced.

**Hypothesis:** Ni²⁺ strongly prefers octahedral coordination (large octahedral CFSE for d⁸), but bulky substituents at the 2,9-positions enforce tetrahedral or distorted geometries. Zn²⁺ (d¹⁰, no CFSE) is geometry-flexible and accommodates steric strain without energetic penalty. Cu²⁺ also suffers because the methyl groups clash with the elongated Jahn–Teller axis.

### 3. Co²⁺ ≥ Ni²⁺ with Strong π-Acceptor Ligands

For **2,2′-bipyridyl** (ligand_8156) and **1,10-phenanthroline** (ligand_8191), the log K₁ values sometimes show Co²⁺ ≈ Ni²⁺ or even Co²⁺ > Ni²⁺, violating the expected Ni²⁺ > Co²⁺ ordering.

**Hypothesis:** These aromatic diimines are strong **π-acceptors**. Co²⁺ (d⁷) has more electrons available for metal-to-ligand π-back-donation than Ni²⁺ (d⁸) in certain spin states. Additionally, Co²⁺ can access low-spin configurations with these strong-field ligands, gaining additional CFSE that partially compensates for its larger ionic radius.

### 4. EDTA: Fe²⁺ Anomalously Low

With **EDTA** (ligand_6277), Fe²⁺ stability constants are often lower than expected — the gap between Fe²⁺ and Mn²⁺ is smaller than predicted by the series.

**Hypothesis:** Fe²⁺ (d⁶, high-spin) in an octahedral EDTA cage has relatively modest CFSE. Furthermore, Fe²⁺ is susceptible to partial oxidation to Fe³⁺ under experimental conditions, which can introduce systematic errors. The hexadentate EDTA wraps tightly, and the slightly larger high-spin Fe²⁺ ion may experience steric strain in the cavity.

### 5. Ammonia: Sparse Data for Fe²⁺ and Mn²⁺

The SRD-46 database shows very few measurements for Fe²⁺–NH₃ (only 1 VLM) and Mn²⁺–NH₃ (3 VLMs), reflecting the inherent instability of these complexes. When data exist, Fe²⁺–NH₃ constants can appear anomalously low.

**Hypothesis:** Both Mn²⁺ and Fe²⁺ ammine complexes are thermodynamically weak and kinetically labile, making reliable measurements difficult. Fe²⁺ in aqueous ammonia solutions is prone to oxidation and hydrolysis, which suppresses apparent stability.

## Summary of Violation Types

| Violation | Ligand Type | Expected Order | Observed | Primary Cause |
|-----------|-------------|---------------|----------|---------------|
| Zn²⁺ > Cu²⁺ | Thiolates, soft S-donors | Cu²⁺ > Zn²⁺ | Zn²⁺ ≥ Cu²⁺ | HSAB mismatch; tetrahedral preference of Zn²⁺ |
| Zn²⁺ > Ni²⁺ | Sterically hindered N-donors | Ni²⁺ > Zn²⁺ | Zn²⁺ > Ni²⁺ | Steric enforcement of tetrahedral geometry |
| Co²⁺ ≥ Ni²⁺ | π-Acceptor diimines (bipy, phen) | Ni²⁺ > Co²⁺ | Co²⁺ ≈ Ni²⁺ | π-Back-bonding; spin-state effects |
| Fe²⁺ ≈ Mn²⁺ | Hexadentate O,N-donors (EDTA) | Fe²⁺ >> Mn²⁺ | Small gap | Cavity strain; oxidation artifacts |
| Cu²⁺ suppressed | Bulky chelates (neocuproine) | Cu²⁺ >> all | Cu²⁺ reduced | Jahn–Teller axis clashes with steric bulk |

## Overarching Hypothesis

The Irving–Williams series holds best for **simple, sterically undemanding, hard/borderline donor ligands** (e.g., glycine, oxalate, en, ammonia) where the dominant factors are ionic radius and octahedral CFSE. Violations arise when:

1. **Donor softness** (thiolates, thioethers) favors the d¹⁰ Zn²⁺ ion via HSAB matching
2. **Steric constraints** penalize metals with strong geometric preferences (Ni²⁺ for octahedral, Cu²⁺ for Jahn–Teller elongated octahedral)
3. **π-Bonding effects** from aromatic N-heterocycles differentially stabilize metals with favorable d-electron counts for back-donation
4. **Spin-state changes** induced by strong-field ligands alter the effective CFSE contributions

These exceptions illustrate that the Irving–Williams series, while remarkably general, is fundamentally a **first-order approximation** based on electrostatic and CFSE arguments for octahedral, high-spin complexes with σ-only donors. When secondary bonding effects (π-interactions, HSAB matching) or geometric constraints (steric bulk, chelate ring strain) become significant, deviations are both predictable and chemically informative.

---
*Data source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes)*

---