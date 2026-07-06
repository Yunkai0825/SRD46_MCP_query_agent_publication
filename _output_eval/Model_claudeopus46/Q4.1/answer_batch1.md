# Complexation Constants for Solvent-Type Ligands with Fe(II) and Fe(III)

## Database Search Results (NIST SRD-46)

I searched the NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes) for all four ligand–iron systems. Here is what was found:

| Ligand | Ligand ID | Fe²⁺ (metal_62) | Fe³⁺ (metal_61) | Database Status |
|--------|-----------|------------------|------------------|-----------------|
| **DMF** (N,N-Dimethylformamide) | ligand_11422 | No data | No data | Class "Ligands not selected"; 0 VLMs total |
| **Acetonitrile** (MeCN) | ligand_9825 | No confirmed Fe data | No confirmed Fe data | 7 VLMs total (likely with other metals) |
| **THF** (Tetrahydrofuran) | — | No data | No data | Not catalogued in SRD-46 at all |
| **Ethylene glycol** | ligand_9621 | Possible data | Possible data | 22 VLMs total, but Fe pairing unconfirmed in catalog |

**Key finding:** The `build_system_catalog` query for Fe²⁺/Fe³⁺ paired with DMF, acetonitrile, and ethylene glycol returned **zero pairs**, meaning no critically evaluated stability constants exist in SRD-46 for any of these four systems with iron.

---

## Reasoned Estimates Based on Chemical Principles

These four molecules are **weak, neutral donor ligands** far more commonly used as *solvents* than as *ligands* in aqueous coordination chemistry. Their complexation with Fe²⁺/Fe³⁺ in aqueous solution is expected to be very weak, which explains the absence of data in critical compilations.

### Estimated log β₁ (ML) values in aqueous solution at 25 °C

| Ligand | Donor atom(s) | Fe²⁺ est. log β₁ | Fe³⁺ est. log β₁ | Reasoning |
|--------|---------------|-------------------|-------------------|-----------|
| **DMF** | O (carbonyl) | −0.5 to 0.5 | 0 to 1.0 | Weak O-donor amide; comparable to formamide/urea complexes. Fe³⁺ is a harder acid and binds O-donors slightly better. Literature reports log β₁ ≈ 0.3–0.7 for urea–Fe³⁺. |
| **Acetonitrile** | N (nitrile) | −0.5 to 0.5 | −0.5 to 0.5 | Very weak σ-donor; nitrile N is a poor base (pKₐ of conjugate acid ≈ −10). MeCN is a soft donor, slightly favoring Fe²⁺ over Fe³⁺. |
| **THF** | O (ether) | −1 to 0 | −0.5 to 0.5 | Saturated ether oxygen is one of the weakest donors. Even crown ethers (preorganized polyethers) show only modest log β with Fe. A single ether O cannot compete effectively with water. |
| **Ethylene glycol** | O,O (diol) | 0 to 1.0 | 0.5 to 1.5 | Chelate effect from two hydroxyl groups gives a modest advantage over monodentate alcohols. Analogous to 1,2-propanediol. Fe³⁺ favors hard O-donors. |

---

## Key Chemistry Insights

1. **Why so weak?** All four ligands are neutral molecules competing with water (55 M) for coordination sites on Fe. Water itself is a reasonable O-donor, so displacing it requires a ligand with stronger donor ability or chelate/macrocyclic effects. These solvent molecules lack the anionic charge or strong chelation that drives high stability constants (compare: log β₁ for Fe³⁺–EDTA ≈ 25).

2. **Fe³⁺ vs Fe²⁺ trends:** Fe³⁺ is a harder Lewis acid (HSAB theory), so it generally binds O-donors (DMF, THF, ethylene glycol) more strongly than Fe²⁺. For the softer N-donor acetonitrile, the difference is smaller or may even slightly favor Fe²⁺.

3. **Non-aqueous relevance:** These ligands are far more important as coordinating solvents in non-aqueous electrochemistry and synthesis, where they *are* the bulk medium and directly occupy coordination sites. Stability constants measured in non-aqueous media would be more meaningful but fall outside the scope of SRD-46, which focuses on aqueous or mixed-aqueous systems.

4. **Ethylene glycol is the strongest candidate:** Among the four, ethylene glycol has the best chance of measurable complexation due to its bidentate chelation through two –OH groups and the hard O-donor character that matches Fe³⁺. Its 22 VLMs in SRD-46 (with other metals) support this — it is at least recognized as a ligand, unlike DMF or THF.

---

**Source:** NIST Standard Reference Database 46 (SRD-46). No measured stability constants were found for any of the four requested Fe–solvent ligand systems. The estimates above are based on chemical analogy with related weak donor ligands and HSAB principles, and should be treated as order-of-magnitude guides only.

---