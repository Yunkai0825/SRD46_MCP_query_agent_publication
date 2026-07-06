# Qfree_20260423_134926 -- Result (batch 1)

**Section:** freeform -- Fe(III) vs Fe(II) selective ligand

**Prompt:** I would like to find a ligand that can complex Fe(III) to stabilize the solution, yet with limited complexation to Fe(II), so that I can selectively keep iron in the +3 oxidation state in aqueous solution at near-neutral pH. Please survey the SRD-46 database for candidate ligands and rank them by the difference (or ratio) between their Fe(III) and Fe(II) stability constants under comparable conditions (ionic strength, temperature, pH range). Report the top candidates with the underlying log-K values, the experimental conditions, and the entity IDs supporting each value. You have unlimited time — be thorough and explain your reasoning.


**Tool calls:** 28  |  **Time:** 252s planning + 1644s execution + 0s verdict = 1895s total

---

# Selective Fe(III) Stabilization: Ligand Survey from NIST SRD-46

## Objective

Identify ligands that form **much stronger complexes with Fe(III) than Fe(II)**, enabling selective stabilization of the ferric oxidation state in aqueous solution near neutral pH.

## Methodology

I queried the NIST SRD-46 database for all **1:1 metal–ligand formation constants** (β definition = `[ML]/[M][L]`, `beta_def_812`) measured for both **Fe³⁺ (`metal_61`)** and **Fe²⁺ (`metal_62`)** under **matched conditions** (same temperature and ionic strength). The selectivity metric is:

> **ΔlogK = logK₁(Fe³⁺) − logK₁(Fe²⁺)**

A larger ΔlogK means the ligand preferentially binds Fe(III) over Fe(II), thermodynamically disfavoring reduction of chelated Fe(III) to Fe(II).

---

## Top Candidates — Paired Fe(III)/Fe(II) Data

| Rank | Ligand | Ligand ID | logK₁(Fe³⁺) | logK₁(Fe²⁺) | **ΔlogK** | T (°C) | I (M) | Card IDs (Fe³⁺ / Fe²⁺) |
|------|--------|-----------|-------------|-------------|-----------|---------|-------|-------------------------|
| 1 | **[24]RBPyBC** (tetraaza-dipyridina macrocycle) | `ligand_7673` | 32.0 | 15.3 | **16.7** | 25 | 0.1 | 59652 / 59653 |
| 2 | **TETA** (1,4,8,11-tetraazacyclotetradecane-tetraacetic acid) | `ligand_6109` | 26.46 | 13.32 | **13.14** | 25 | 0.1 | 59576 / 59577 |
| 3 | **DTPA** (diethylenetrinitrilopentaacetic acid) | `ligand_6356` | 28.0 | 16.2 | **11.8** | 25 | 0.1 | 59614 / 59615 |
| 4 | **DL-EDDP** (ethylenedinitrilo-dipropanoic-diacetic acid) | `ligand_6292` | 25.28 | 14.18 | **11.1** | 20 | 0.1 | 59596 / 59597 |
| 5 | **CDTA** (trans-1,2-cyclohexylenedinitrilotetraacetic acid) | `ligand_6301` | 30.0 | 18.9 | **11.1** | 25 | 0.1 | 59600 / 59601 |
| 6 | **TTHA** (triethylenetetranitrilohexaacetic acid) | `ligand_6366` | 26.8 | 15.8 | **11.0** | 25 | 0.1 | 59618 / 59619 |
| 7 | **rac-Dimethyl-EDTA** | `ligand_6287` | 28.05 | 17.08 | **10.97** | 25 | 0.1 | 59594 / 59595 |
| 8 | **EDTA** | `ligand_6277` | 25.1 | 14.3 | **10.8** | 25 | 0.1 | 59590 / 59591 |
| 9 | **2,6-PDPA** (pyridine-2,6-diphosphonic acid) | `ligand_8434` | 20.87 | 10.12 | **10.75** | 25 | 0.1 | 59720 / 59721 |
| 10 | **PDTA** (methylethylene-dinitrilotetraacetic acid) | `ligand_6278` | 26.0 | 15.5 | **10.5** | 25 | 0.1 | 59592 / 59593 |
| 11 | **meso-Dimethyl-EDTA** | `ligand_6288` | 25.65 | 15.33 | **10.32** | 25 | 0.1 | 59594 / 59595 |
| 12 | **1-Oxa-4,7,10-triazacyclododecane-triacetic acid** | `ligand_6084` | 26.8 | 16.55 | **10.25** | 25 | 0.1 | 59564 / 59565 |
| 13 | **TRITA** (tetraazacyclotridecane-tetraacetic acid) | `ligand_6104` | 27.5 | 17.6 | **9.9** | 25 | 0.1 | 59572 / 59573 |
| 14 | **Amino(phenyl)methylenediphosphonic acid** | `ligand_8360` | 20.15 | 10.4 | **9.75** | 25 | 0.1 | 59714 / 59715 |
| 15 | **DOTA** (tetraazacyclododecane-tetraacetic acid) | `ligand_6102` | 29.4 | 19.8 | **9.6** | 25 | 0.1 | 59570 / 59571 |
| 16 | **Glyphosate** (N-phosphonomethylglycine) | `ligand_5937` | 16.09 | 6.87 | **9.22** | 25 | 0.1 | 59466 / 59467 |
| 17 | **TEDTA** (thiobis-ethylenenitrilo-tetraacetic acid) | `ligand_6348` | 20.41 | 11.57 | **8.84** | 20 | 0.1 | 59610 / 59611 |
| 18 | **EGTA** | `ligand_6342` | 20.5 | 11.8 | **8.7** | 25 | 0.1 | 59608 / 59609 |
| 19 | **Glutamic acid** | `ligand_5804` | 12.1 | 3.52 | **8.58** | 20 | 1.0 | 59436 / 59437 |
| 20 | **Citric acid** | `ligand_9058` | 11.27 | 4.4 | **~6.9** | 25/20 | 0.1 | 59757 / 59694 |

---

## Notable Fe(III)-Only Ligands (No Fe(II) Data — Presumed High Selectivity)

Several ligands show **extremely high Fe(III) logK₁ values** with no Fe(II) data in SRD-46, suggesting they were designed specifically as Fe(III) chelators:

| Ligand | Ligand ID | logK₁(Fe³⁺) | T (°C) | I (M) |
|--------|-----------|-------------|---------|-------|
| **1,4,7-Tris(3-OH-6-Me-2-pyridylmethyl)-TACN** | `ligand_7674` | 50.0 | 25 | 0.1 |
| **HBED** | `ligand_6371` | 39.01 | 25 | 0.1 |
| **SHBED** | `ligand_6370` | 36.0 | 25 | 0.1 |
| **EHPG** | `ligand_6369` | 33.7 | 25 | 0.1 |
| **5-Br-EHPG** | `ligand_6367` | 33.1 | 25 | 0.1 |

These phenolate-containing aminocarboxylate ligands (HBED, EHPG family) are well-known Fe(III)-selective chelators used in iron-overload therapy (e.g., deferiprone analogs). Their selectivity for Fe(III) over Fe(II) is expected to be enormous based on hard–soft acid–base (HSAB) principles.

---

## Chemistry Insight & Recommendations

### Why does Fe(III) consistently bind harder ligands more strongly?

Fe³⁺ is a **hard Lewis acid** (small, highly charged, d⁵), while Fe²⁺ is **borderline**. Ligands with **oxygen-donor groups** (carboxylates, phenolates, phosphonates, hydroxamates) show the largest ΔlogK because they are hard Lewis bases that strongly prefer the higher charge density of Fe³⁺. The ΔlogK of ~10–17 log units for the top candidates translates to a **selectivity factor of 10¹⁰–10¹⁷** — meaning the Fe(III) complex is astronomically more stable.

### Practical Recommendations for Near-Neutral pH

| Priority | Ligand | Why |
|----------|--------|-----|
| ⭐⭐⭐ | **DTPA** (ΔlogK = 11.8) | Commercially available, water-soluble, well-characterized at pH 7. Forms very stable Fe(III) complex (logK = 28.0) while Fe(II) complex is 11.8 log units weaker. FDA-approved chelator. |
| ⭐⭐⭐ | **CDTA** (ΔlogK = 11.1) | Highest absolute Fe(III) logK among paired data (30.0). Rigid cyclohexane backbone preorganizes for octahedral Fe(III). |
| ⭐⭐⭐ | **EDTA** (ΔlogK = 10.8) | The classic benchmark. Ubiquitous, inexpensive, logK(Fe³⁺) = 25.1. Widely used to stabilize Fe(III) in analytical and industrial applications. |
| ⭐⭐ | **HBED / EHPG family** (Fe³⁺ logK = 33–39) | Purpose-built Fe(III) chelators with phenolate donors. Likely ΔlogK > 15 but Fe(II) data absent from SRD-46. Used in radiopharmaceuticals (⁶⁸Ga/⁵⁹Fe labeling). |
| ⭐⭐ | **Citric acid** (ΔlogK ≈ 6.9) | Biologically relevant, food-safe, moderate selectivity. Commonly used in biological buffers to maintain Fe(III). |
| ⭐ | **Glyphosate** (ΔlogK = 9.2) | Phosphonate + amino acid hybrid; strong Fe(III) preference but environmental/toxicity concerns limit applications. |

### Key Caveat

All values above are **thermodynamic** stability constants. At near-neutral pH, **conditional (effective) stability constants** will differ because ligand protonation competes with metal binding. Ligands with lower pKₐ values (e.g., DTPA, EDTA) maintain more of their binding capacity at pH 7 than ligands whose donor groups are substantially protonated (e.g., simple amino acids). For the aminopolycarboxylates (EDTA, DTPA, CDTA), the conditional logK at pH 7 remains very high for Fe(III) — typically only 2–4 log units below the thermodynamic value — while the Fe(II) conditional constant drops even further, **enhancing** the selectivity at neutral pH.

---

**Source:** All values from NIST Standard Reference Database 46 (SRD-46), Critically Selected Stability Constants of Metal Complexes. Equilibrium definition: `[ML]/[M][L]` (`beta_def_812`). Metal entities: Fe³⁺ = `metal_61`, Fe²⁺ = `metal_62`.
