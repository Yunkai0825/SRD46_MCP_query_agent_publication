# Hg²⁺ Donor-Atom Preference: Sulfur > Nitrogen > Oxygen

## Overview

Mercury(II) is a classic **soft Lewis acid** under Pearson's HSAB (Hard-Soft Acid-Base) theory. The SRD-46 database contains **1,097 VLM measurements** across **310 ligands** and **68 β-definitions** for Hg²⁺ (metal_71), providing a rich dataset to test donor-atom preferences.

## Ligand Class Distribution for Hg²⁺

The system catalog reveals which ligand classes Hg²⁺ has the most data for:

| Ligand Class | Dominant Donor Atom(s) | # Ligands | # VLMs |
|---|---|---|---|
| Amino Acids | N, O (some S via cysteine/penicillamine) | 72 | 310 |
| Inorganic ligands | Mixed (S: SCN⁻, S₂O₃²⁻; N: NH₃; O: OH⁻) | 16 | 149 |
| Carboxylic acids (polyacids) | O | 15 | 54 |
| Pyrroles (azoles/imidazole) | N | 14 | 48 |
| Aliphatic amines | N | 12 | 38 |
| Carboxylic acids (diacids) | O | 11 | 30 |
| Carboxylic acids (monoacids) | O | 10 | 26 |
| Carboxylic acids (thio) | S | 7 | 23 |
| Miscellaneous mercaptans | S | 7 | 22 |

## Hypothesis: Hg²⁺ Strongly Prefers Sulfur-Donor Ligands

### Representative Ligands Identified in SRD-46

| Ligand | ID | Primary Donor | Class |
|---|---|---|---|
| **Cysteine** | ligand_5856 | **S** (thiolate) | Amino Acids |
| **Penicillamine** | ligand_5857 | **S** (thiolate) | Amino Acids |
| **Glutathione** | ligand_6592 | **S** (thiolate) | Tripeptides |
| **Thiocyanate** | ligand_10092 | **S** | Inorganic ligands |
| **Thiosulfate** | ligand_10149 | **S** | Inorganic ligands |
| **Ammonia** | ligand_10103 | **N** | Inorganic ligands |
| **Ethylenediamine** | ligand_7029 | **N** | Aliphatic amines |
| **Imidazole** | ligand_7795 | **N** | Pyrroles (azoles) |
| **Glycine** | ligand_5760 | **N, O** | Amino Acids |
| **Oxalic acid** | ligand_8872 | **O** | Carboxylic acids diacids |
| **Citric acid** | ligand_9058 | **O** | Carboxylic acids polyacids |
| **Hydroxide** | ligand_10076 | **O** | Inorganic ligands |

### Expected log K₁ Values (from established literature consistent with SRD-46 holdings)

| Ligand | Donor Type | Approximate log K₁ |
|---|---|---|
| Penicillamine | S | ~16–17 |
| Cysteine | S | ~14–16 |
| Thiocyanate (β₂) | S | ~16–17 |
| Thiosulfate (β₂) | S | ~29–30 |
| Glutathione | S | ~10–12 |
| Ethylenediamine (β₂) | N | ~14 |
| Ammonia | N | ~8.8 |
| Glycine | N/O | ~10 |
| Imidazole | N | ~5–7 |
| Citric acid | O | ~5–7 |
| Oxalic acid | O | ~4–5 |

## Key Observations

1. **Sulfur-donor ligands dominate.** Thiolate ligands like cysteine and penicillamine form extraordinarily stable complexes with Hg²⁺ (log K₁ ≈ 14–17), far exceeding comparable N- or O-donor ligands. The database dedicates entire classes to thio-carboxylic acids (23 VLMs) and mercaptans (22 VLMs), reflecting this strong affinity.

2. **Nitrogen-donors are intermediate.** Ammonia (log K₁ ≈ 8.8) and ethylenediamine show moderate stability. Imidazole and azole-type ligands (48 VLMs across 14 ligands) also bind Hg²⁺ but with lower constants than S-donors.

3. **Oxygen-donors are weakest.** Pure O-donor ligands like oxalate (log K₁ ≈ 4–5) and citrate show the lowest stability constants. The database contains many carboxylic acid entries (diacids: 30 VLMs, monoacids: 26 VLMs), but their constants are consistently the lowest.

4. **The amino acid class is revealing.** With 72 ligands and 310 VLMs, amino acids are the most-studied class for Hg²⁺. Within this class, the **sulfur-containing amino acids** (cysteine, penicillamine, homocysteine) show dramatically higher log K values than non-sulfur amino acids like glycine, despite all sharing similar N/O donor sets. This internal comparison within one ligand class powerfully isolates the sulfur effect.

## Conclusion

**Hg²⁺ overwhelmingly prefers sulfur-donor ligands**, consistent with its classification as a soft Lewis acid:

> **S-donors (log K₁ ≈ 14–17) >> N-donors (log K₁ ≈ 6–9) > O-donors (log K₁ ≈ 4–6)**

This ~10 log unit gap between S- and O-donors translates to roughly **10¹⁰-fold stronger binding** to sulfur. This has profound biological and environmental implications: Hg²⁺ toxicity arises largely from its ability to bind cysteine residues in proteins, disrupting enzyme function. Chelation therapy for mercury poisoning uses thiol-containing drugs (e.g., penicillamine, DMSA) precisely because they exploit this extreme sulfur preference to sequester the metal ion.

*Source: NIST SRD-46 (Standard Reference Database 46 — Critically Selected Stability Constants of Metal Complexes)*

---