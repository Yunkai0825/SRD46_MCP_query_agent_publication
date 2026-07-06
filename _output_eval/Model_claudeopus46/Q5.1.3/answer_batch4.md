# Iron vs. Copper — A Comparison in NIST SRD-46

## Overview: Database Coverage

| Metal Ion | ID | β-Definitions | Ligand Partners | Measurements (VLMs) |
|-----------|-----------|----------------|-----------------|----------------------|
| **Cu²⁺** | metal_41 | 264 | 1,951 | 8,963 |
| **Fe³⁺** | metal_61 | 128 | 406 | 1,473 |
| **Fe²⁺** | metal_62 | 57 | 217 | 667 |
| **Cu⁺** | metal_42 | 32 | 117 | 285 |
| **Cu³⁺** | metal_43 | 4 | 8 | 10 |

Cu²⁺ is by far the most extensively studied metal ion of the group — and indeed one of the most studied in all of coordination chemistry — with nearly **9,000 measurements** spanning almost 2,000 different ligands. Fe³⁺ comes next, followed by Fe²⁺, then Cu⁺, while Cu³⁺ data is extremely sparse.

---

## Key Comparison Points

### 1. Breadth of Coordination Chemistry
- **Cu²⁺** forms stable complexes with an enormous variety of ligands (N-donors, O-donors, S-donors, mixed-donor chelates). Its d⁹ configuration and Jahn–Teller distortion give it flexible coordination geometries (4-, 5-, 6-coordinate).
- **Fe³⁺** is a hard Lewis acid (d⁵ high-spin) that strongly favours O-donor ligands (carboxylates, hydroxamates, catecholates, phosphonates). It has roughly **twice** the ligand coverage of Fe²⁺.
- **Fe²⁺** (d⁶) is softer than Fe³⁺ and binds well to N-donor ligands (bipyridine, phenanthroline, imidazoles), reflected in its 217 ligand partners.
- **Cu⁺** (d¹⁰) is a soft Lewis acid preferring S- and N-donors (thioethers, nitriles, phosphines), with a more limited but distinct ligand set (117 partners).

### 2. Stability Constant Trends (Irving–Williams Series)
Cu²⁺ sits at the peak of the **Irving–Williams series** for divalent first-row transition metals:

> Mn²⁺ < Fe²⁺ < Co²⁺ < Ni²⁺ < **Cu²⁺** > Zn²⁺

This means that for virtually any given ligand measured under the same conditions, **Cu²⁺ forms more stable complexes than Fe²⁺**. The database's massive Cu²⁺ dataset (8,963 VLMs vs. 667 for Fe²⁺) is partly a consequence of this rich and strong coordination chemistry.

### 3. Fe³⁺ vs. Cu²⁺ — Hard vs. Borderline
Fe³⁺ (hard acid) and Cu²⁺ (borderline acid) show complementary selectivity:

| Feature | Fe³⁺ | Cu²⁺ |
|---------|-------|-------|
| HSAB class | Hard | Borderline |
| Preferred donors | O (carboxylate, hydroxamate, catecholate) | N, O, S (amines, imidazoles, thiolates) |
| Hydrolysis tendency | Very strong (low pH onset) | Moderate |
| Typical log β₁ with EDTA (25 °C) | ~25 | ~18–19 |
| Biological role | O₂ transport (hemoglobin), electron transfer | Electron transfer (blue Cu proteins), O₂ activation |

Fe³⁺ often exceeds Cu²⁺ in stability with hard O-donor chelators (e.g., siderophores, EDTA, DTPA), while Cu²⁺ dominates with softer N/S-donor ligands.

### 4. Redox Accessibility
Both elements are biologically important precisely because they access multiple oxidation states:
- **Fe³⁺/Fe²⁺** — the workhorse redox couple in cytochromes, iron–sulfur clusters, and Fenton chemistry.
- **Cu²⁺/Cu⁺** — central to oxidases (laccase, cytochrome c oxidase) and superoxide dismutase.

The database reflects this: both oxidation states of each metal have significant, independent datasets.

### 5. Data Richness Summary

| Metric | Iron (all) | Copper (all) |
|--------|-----------|-------------|
| Total ligand partners | ~620* | ~2,070* |
| Total measurements | ~2,140 | ~9,258 |
| Oxidation states covered | 2 (Fe²⁺, Fe³⁺) | 3 (Cu⁺, Cu²⁺, Cu³⁺) |

*\*Approximate; some ligands may overlap between oxidation states.*

---

## Summary

**Copper** — especially Cu²⁺ — is the single most data-rich metal in SRD-46, reflecting its position at the top of the Irving–Williams series and its extraordinarily versatile coordination chemistry. **Iron** is split between a hard, strongly hydrolyzing Fe³⁺ (favouring O-donors) and a softer Fe²⁺ (favouring N-donors), together covering ~2,100 measurements. For any head-to-head ligand comparison, Cu²⁺ will generally outbind Fe²⁺ with the same ligand, while Fe³⁺ can surpass Cu²⁺ for hard oxygen-donor chelators. Both metals owe their biological prominence to accessible redox couples (Fe³⁺/Fe²⁺ and Cu²⁺/Cu⁺).

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes).*

---