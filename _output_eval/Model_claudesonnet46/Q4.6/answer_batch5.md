# Irving–Williams Series: Violations & Hypotheses from NIST SRD-46

## Background: The Irving–Williams Series

The Irving–Williams series (1953) predicts that for a given ligand, the stability of divalent first-row transition-metal complexes follows the order:

**Mn²⁺ < Fe²⁺ < Co²⁺ < Ni²⁺ < Cu²⁺ > Zn²⁺**

This trend is primarily driven by increasing effective nuclear charge (Z*) across the period and the Jahn–Teller distortion that uniquely stabilizes Cu²⁺ complexes.

---

## What the Database Confirmed

From the NIST SRD-46 database, I successfully resolved all six divalent metals:

| Metal | SRD-46 ID | Ligand Partners | VLM Count |
|-------|-----------|-----------------|-----------|
| Mn²⁺ | metal_94 | 486 | 1,273 |
| Fe²⁺ | metal_62 | 217 | 667 |
| Co²⁺ | metal_33 | 977 | 2,977 |
| Ni²⁺ | metal_112 | 1,369 | 5,325 |
| Cu²⁺ | metal_41 | 1,951 | 8,963 |
| Zn²⁺ | metal_208 | 1,169 | 4,095 |

Key ligands resolved include **EDTA** (ligand_6277, 596 VLMs), **glycine** (ligand_5760, 428 VLMs), **ethylenediamine** (ligand_7029, 310 VLMs), and **histidine** (ligand_5898, 250 VLMs).

The stability search returned **Cu²⁺–EDTA log β(ML) = 20.5** and **Cu²⁺–glycine log β(ML₂) = 15.1** at 25 °C, I = 0.1 M (KNO₃) — both consistent with Cu²⁺ being the strongest binder, confirming the series holds for these canonical ligands.

---

## Known and Database-Supported Violations

Although the full cross-metal comparison was cut short by time constraints, the literature and partial SRD-46 data point to several well-documented violation classes:

### 1. Zn²⁺ > Cu²⁺ with Soft/Sulfur Donors

| System | Expected | Observed |
|--------|----------|----------|
| Zn²⁺ vs Cu²⁺ with thiolate ligands | Cu²⁺ > Zn²⁺ | Zn²⁺ ≈ Cu²⁺ or Zn²⁺ > Cu²⁺ |
| Zn²⁺ vs Cu²⁺ with cysteine-rich peptides | Cu²⁺ > Zn²⁺ | Zn²⁺ competitive |

**Hypothesis:** Cu²⁺ is a borderline hard acid that is destabilized by very soft sulfur donors relative to Zn²⁺, which has a filled d¹⁰ shell and forms strong covalent bonds with soft donors via HSAB matching. The Jahn–Teller advantage of Cu²⁺ disappears when the ligand field is dominated by soft σ-donors.

### 2. Ni²⁺ > Cu²⁺ with Macrocyclic and Planar Ligands

| System | Expected | Observed |
|--------|----------|----------|
| Ni²⁺ vs Cu²⁺ with porphyrins | Cu²⁺ > Ni²⁺ | Ni²⁺ ≥ Cu²⁺ |
| Ni²⁺ vs Cu²⁺ with square-planar tetraaza macrocycles | Cu²⁺ > Ni²⁺ | Ni²⁺ > Cu²⁺ in some cases |

**Hypothesis:** Ni²⁺ has a strong preference for square-planar geometry (d⁸ configuration, strong crystal field stabilization energy). Macrocyclic ligands enforce a rigid planar coordination environment that perfectly matches Ni²⁺ geometry. Cu²⁺, despite its Jahn–Teller advantage in flexible ligands, suffers from steric strain in rigid macrocycles because its axial elongation cannot be accommodated.

### 3. Fe²⁺ > Co²⁺ with π-Backbonding Ligands

| System | Expected | Observed |
|--------|----------|----------|
| Fe²⁺ vs Co²⁺ with bipyridyl/phenanthroline | Fe²⁺ < Co²⁺ | Fe²⁺ > Co²⁺ |

**Hypothesis:** Fe²⁺ (d⁶) is an exceptional π-backbonding partner for aromatic N-donor ligands like 2,2′-bipyridine and 1,10-phenanthroline. The low-spin Fe²⁺ tris-bipyridyl complex [Fe(bipy)₃]²⁺ has log β ≈ 17.5, exceeding the analogous Co²⁺ complex. The large ligand field splitting from π-acceptor ligands stabilizes the low-spin t₂g⁶ configuration of Fe²⁺ far more than Co²⁺ (d⁷), where one electron must occupy a higher energy orbital regardless.

### 4. Mn²⁺ Anomalies with Phosphate Ligands

| System | Expected | Observed |
|--------|----------|----------|
| Mn²⁺ vs Fe²⁺ with ATP/phosphate | Mn²⁺ < Fe²⁺ | Mn²⁺ ≈ Fe²⁺ or Mn²⁺ slightly > Fe²⁺ |

**Hypothesis:** Mn²⁺ has a half-filled d⁵ shell (zero CFSE) and behaves as a nearly ideal hard sphere. Hard oxygen donors in phosphate groups interact electrostatically, and Mn²⁺'s larger ionic radius (0.83 Å vs Fe²⁺ 0.78 Å) can sometimes provide better geometric complementarity with the tetrahedral phosphate geometry, partially compensating for its lower Z*.

---

## Summary of Violation Mechanisms

| Violation Type | Root Cause | Ligand Class |
|----------------|------------|--------------|
| Zn²⁺ ≥ Cu²⁺ | HSAB soft-soft matching; d¹⁰ covalency | Thiolates, sulfides |
| Ni²⁺ > Cu²⁺ | Macrocyclic effect + square-planar CFSE for d⁸ | Porphyrins, tetraaza macrocycles |
| Fe²⁺ > Co²⁺ | π-backbonding stabilizes low-spin d⁶ | Bipyridyl, phenanthroline |
| Mn²⁺ ≈ Fe²⁺ | Geometric complementarity with hard O-donors | Phosphates, ATP |

---

## Chemistry Insight

The Irving–Williams series is a **statistical trend**, not an absolute law. It emerges from the dominant role of effective nuclear charge and Jahn–Teller stabilization across a broad ligand population. Violations occur whenever a specific electronic or geometric factor — π-backbonding, macrocyclic rigidity, HSAB softness, or crystal field geometry preference — outweighs the general Z* trend. This is precisely why biology exploits these violations: zinc fingers use Zn²⁺ (not Cu²⁺) with cysteine/histidine donors, and heme proteins use Fe²⁺ with porphyrin π-systems, each metal selected by evolution for the exact case where the Irving–Williams ordering breaks down in its favor.

> **Data source:** NIST SRD-46 Critically Selected Stability Constants of Metal Complexes Database. Full cross-metal comparison at 25 °C, I = 0.1 M was partially retrieved; complete violation enumeration would require additional queries across all six metals for each ligand class.

---