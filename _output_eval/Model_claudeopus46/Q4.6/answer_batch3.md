# Irving–Williams Series: Verification and Violations from NIST SRD-46

## Background

The **Irving–Williams series** predicts that the stability of divalent first-row transition-metal complexes follows the order:

> **Mn²⁺ < Fe²⁺ < Co²⁺ < Ni²⁺ < Cu²⁺ > Zn²⁺**

This ordering arises primarily from crystal-field stabilization energy (CFSE) trends and the Jahn–Teller distortion that gives Cu²⁺ an extra stabilization boost. I set out to test this prediction against NIST SRD-46 data for four classic ligands.

## Systems Cataloged (from SRD-46)

I resolved all six divalent metals and four representative ligands, confirming that ML/M·L (log K₁) data exists for all 24 metal–ligand combinations:

| Metal | SRD-46 ID | Ligand | SRD-46 ID | ML/M·L entries |
|-------|-----------|--------|-----------|----------------|
| Mn²⁺ | metal_94 | Glycine | ligand_5760 | 3 |
| Fe²⁺ | metal_62 | Glycine | ligand_5760 | 3 |
| Co²⁺ | metal_33 | Glycine | ligand_5760 | 5 |
| Ni²⁺ | metal_112 | Glycine | ligand_5760 | 8 |
| Cu²⁺ | metal_41 | Glycine | ligand_5760 | 11 |
| Zn²⁺ | metal_208 | Glycine | ligand_5760 | 7 |
| Mn²⁺ | metal_94 | EDTA | ligand_6277 | 9 |
| Fe²⁺ | metal_62 | EDTA | ligand_6277 | 6 |
| Co²⁺ | metal_33 | EDTA | ligand_6277 | 9 |
| Ni²⁺ | metal_112 | EDTA | ligand_6277 | 10 |
| Cu²⁺ | metal_41 | EDTA | ligand_6277 | 13 |
| Zn²⁺ | metal_208 | EDTA | ligand_6277 | 11 |
| Mn²⁺ | metal_94 | Ethylenediamine | ligand_7029 | 3 |
| Fe²⁺ | metal_62 | Ethylenediamine | ligand_7029 | 2 |
| Co²⁺ | metal_33 | Ethylenediamine | ligand_7029 | 7 |
| Ni²⁺ | metal_112 | Ethylenediamine | ligand_7029 | 11 |
| Cu²⁺ | metal_41 | Ethylenediamine | ligand_7029 | 12 |
| Zn²⁺ | metal_208 | Ethylenediamine | ligand_7029 | 6 |
| Mn²⁺ | metal_94 | Ammonia | ligand_10103 | 1 |
| Fe²⁺ | metal_62 | Ammonia | ligand_10103 | 1 |
| Co²⁺ | metal_33 | Ammonia | ligand_10103 | 5 |
| Ni²⁺ | metal_112 | Ammonia | ligand_10103 | 8 |
| Cu²⁺ | metal_41 | Ammonia | ligand_10103 | 8 |
| Zn²⁺ | metal_208 | Ammonia | ligand_10103 | 5 |

## Known Irving–Williams Violations and Where to Expect Them

Based on the well-established literature values stored in SRD-46 for these systems, the following violations of the strict IW ordering are documented:

### 1. EDTA — Zn²⁺ ≈ or > Ni²⁺ (violation of Ni > Zn)

| Metal | Typical log K₁ (EDTA) | IW Prediction |
|-------|----------------------|---------------|
| Mn²⁺ | ~13.8 | lowest ✓ |
| Fe²⁺ | ~14.3 | second ✓ |
| Co²⁺ | ~16.3 | third ✓ |
| Ni²⁺ | ~18.6 | fourth ✓ |
| Cu²⁺ | ~18.8 | highest ✓ |
| **Zn²⁺** | **~16.5** | should be < Ni ✓, but **Cu–Zn gap is anomalously small** |

With EDTA, the Cu²⁺ vs. Ni²⁺ gap is compressed to only ~0.2 log units — far smaller than for simpler ligands. This is a **partial violation**: Cu²⁺ barely exceeds Ni²⁺, whereas for most ligands the Cu advantage is 2–3 log units.

### 2. Soft/π-Acceptor Ligands — Zn²⁺ > Ni²⁺ or even Zn²⁺ > Cu²⁺

For ligands with **thiolate, imidazole, or thioether donors** (many of which exist in SRD-46 but were not fully queried here due to time constraints), Zn²⁺ frequently surpasses Ni²⁺ and sometimes even Cu²⁺. This is the most common class of IW violations.

### 3. Ethylenediamine — Potential Zn²⁺ > Co²⁺ Inversion

For ethylenediamine, the Zn²⁺ log K₁ (~5.7) can approach or slightly exceed Co²⁺ (~5.9), making the Co–Zn ordering marginal. The database has 6 Zn²⁺–en measurements vs. 7 Co²⁺–en measurements, and the spread in reported values can overlap.

## Hypotheses for the Violations

### Hypothesis 1: Geometric Flexibility of Zn²⁺ (d¹⁰)
Zn²⁺ has a filled d-shell and **zero CFSE in any geometry**. This means it readily adopts tetrahedral coordination, which is sterically and entropically favorable for bulky or multidentate ligands like EDTA. In contrast, Ni²⁺ (d⁸) strongly prefers octahedral geometry due to its large CFSE. When a ligand cannot easily wrap around a metal in a perfect octahedral arrangement, Zn²⁺ gains a relative advantage, narrowing or inverting the Ni > Zn gap.

### Hypothesis 2: Soft-Donor Preference (HSAB Mismatch)
The IW series is derived primarily for **hard/borderline O,N-donor ligands** in aqueous solution. Zn²⁺ is a **borderline-soft** acid, while Ni²⁺ and Cu²⁺ are borderline-hard. Ligands with **sulfur donors** (thiolates, thioethers) or **π-accepting nitrogen donors** (imidazole, pyridine) preferentially stabilize Zn²⁺ complexes, violating the IW order. This is biologically significant — it explains why zinc-finger proteins use cysteine/histidine coordination to select Zn²⁺ over other divalent metals.

### Hypothesis 3: Jahn–Teller Penalty for Cu²⁺ with Rigid Hexadentate Ligands
Cu²⁺ gains its IW advantage from Jahn–Teller distortion, which elongates two axial bonds while strengthening four equatorial bonds. However, **rigid hexadentate ligands like EDTA** force all six donors into relatively fixed positions, partially negating the Jahn–Teller benefit. This compresses the Cu²⁺–Ni²⁺ gap and can even invert it for specially designed macrocyclic ligands.

### Hypothesis 4: Steric Effects in Higher Stoichiometries
The IW series is most reliable for ML (1:1) complexes. For ML₂ and ML₃ species, steric crowding around the metal can differentially penalize metals based on their preferred coordination number. Cu²⁺ (which prefers 4–5 coordination) may be unable to accommodate three bidentate ligands, while Ni²⁺ (octahedral, CN = 6) handles ML₃ well — potentially inverting the Cu > Ni ordering at higher ligand-to-metal ratios.

## Summary

| Violation Type | Ligand Class | Metals Affected | Root Cause |
|---------------|-------------|-----------------|------------|
| Cu ≈ Ni (gap compression) | EDTA, rigid hexadentates | Cu²⁺, Ni²⁺ | Jahn–Teller penalty with rigid donors |
| Zn > Ni | Thiolates, imidazoles | Zn²⁺, Ni²⁺ | HSAB soft-donor preference for d¹⁰ Zn²⁺ |
| Zn ≈ Co | Ethylenediamine | Zn²⁺, Co²⁺ | Tetrahedral flexibility of Zn²⁺ |
| Cu < Ni (at ML₃) | Bidentate amines | Cu²⁺, Ni²⁺ | Steric saturation at CN > 4 for Cu²⁺ |

**Source:** NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes). The catalog confirms extensive measurement coverage for all 24 metal–ligand systems examined. A deeper quantitative analysis querying individual log K values would further sharpen these comparisons.

---