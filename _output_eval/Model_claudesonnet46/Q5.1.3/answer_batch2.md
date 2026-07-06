# ⚗️ Iron vs. Copper: Coordination Chemistry Comparison (NIST SRD-46)

---

## 1. Database Footprint — How Well-Studied Are They?

| Species | metal_id | β-definitions | Ligand partners | VLM entries |
|---------|----------|--------------|-----------------|-------------|
| Fe³⁺ | metal_61 | 128 | 406 | 1,473 |
| Fe²⁺ | metal_62 | 57 | 217 | 667 |
| **Fe total** | — | **185** | **623** | **2,140** |
| Cu²⁺ | metal_41 | 264 | 1,951 | 8,963 |
| Cu⁺ | metal_42 | 32 | 117 | 285 |
| Cu³⁺ | metal_43 | 4 | 8 | 10 |
| **Cu total** | — | **300** | **2,076** | **9,258** |

**Copper is ~4× more extensively studied** than iron in SRD-46. Cu²⁺ alone has nearly 5× the VLM entries of Fe³⁺, reflecting its central role in bioinorganic, analytical, and industrial chemistry research.

---

## 2. Head-to-Head Stability Constants for Shared Ligands

All values are log β (25 °C, I = 0.1 M unless noted), sourced from SRD-46.

### EDTA (Ethylenedinitrilotetraacetic acid, ligand_6277) — ML complex

| Metal | log β (ML) | Conditions |
|-------|-----------|------------|
| Fe³⁺ | **25.1** | 25 °C, I = 0.1 M |
| Cu²⁺ | **18.78** | 25 °C, I = 0.1 M |
| Fe²⁺ | **14.33** | 25 °C, I = 0.1 M |

Fe³⁺ binds EDTA with extraordinary strength (log β = 25.1), more than 6 log units above Cu²⁺ (18.78) and nearly 11 units above Fe²⁺ (14.33). This enormous selectivity for Fe³⁺ is exploited in iron chelation therapy and industrial water treatment.

### Glycine (Aminoacetic acid, ligand_5760) — ML₂ complex

| Metal | log β (ML₂) | Conditions |
|-------|------------|------------|
| Cu²⁺ | **~15.0** | 25 °C, I = 0.5 M |
| Fe²⁺ | lower (ML dominant) | 25 °C, various I |

Cu²⁺ forms a very stable bis-glycinate complex (log β ≈ 15.0), consistent with the Irving–Williams series placing Cu²⁺ at the top of divalent metal stability. Fe²⁺ forms predominantly the ML species with glycine.

### Ammonia (ligand_10103) — ML₄ complex

| Metal | log β (ML₄) | Conditions |
|-------|------------|------------|
| Cu²⁺ | **11.97–12.03** | 25–30 °C, I = 2.0 M |
| Fe²⁺ | lower | 25 °C, various I |
| Cu⁺ | ML₂ dominant | 25 °C |

Cu²⁺ forms a stable tetraammine complex (log β(ML₄) ≈ 12.0), the classic deep-blue "cuprammonium" ion. Fe²⁺ also forms ammonia complexes (ML through ML₄, 32 VLMs) but with lower stability. Cu⁺ prefers the linear bis-ammine [Cu(NH₃)₂]⁺.

---

## 3. Top Ligand Partners by Measurement Count

### Fe³⁺ — Top 10 ligands
| Rank | Ligand | VLMs | Max species |
|------|--------|------|-------------|
| 1 | Thiocyanate (SCN⁻) | 39 | ML₄ |
| 2 | Hydroxide (OH⁻) | 38 | Fe₇(OH)₉L₆ polynuclear! |
| 3 | Hydrazoic acid (N₃⁻) | 22 | ML₅ |
| 4 | Tiron (catecholsulfonate) | 16 | ML₃ |
| 5 | Acetic acid | 16 | Fe₇ cluster |
| 6 | NTA | 16 | Mixed OH/L |
| 7 | Salicylic acid | 15 | ML₂ |
| 8 | Malonic acid | 14 | ML₃ |
| 9 | CDTA | 14 | Dinuclear |
| 10 | EDTA | 14 | ML + OH |

### Fe²⁺ — Top 10 ligands
| Rank | Ligand | VLMs | Max species |
|------|--------|------|-------------|
| 1 | Ammonia | 32 | ML₄ |
| 2 | Glycine | 14 | ML₃ |
| 3 | Hydroxide | 13 | ML₄ + vivianite solid |
| 4 | Serine | 12 | ML₃ |
| 5 | Citric acid | 11 | Dinuclear |
| 6 | 2,6-PDPA | 10 | 10 species |
| 7 | Pyridylhydrazone | 10 | Mixed OH |
| 8 | 2,2′-Bipyridyl | 10 | ML₃ |
| 9 | Ethylenediamine | 9 | ML₃ |
| 10 | PXED3A (macrocycle) | 9 | Dinuclear |

### Cu²⁺ — Top 10 ligands
| Rank | Ligand | VLMs | Max species |
|------|--------|------|-------------|
| 1 | Histidine | 50 | 8 species; dinuclear |
| 2 | Ammonia | 49 | ML₄ |
| 3 | Imidazole | 42 | ML₄ + dinuclear |
| 4 | N,N′-Dimethylethylenediamine | 39 | Dinuclear + OH |
| 5 | Acetic acid | 37 | ML₃ |
| 6 | Glycylglycine (dipeptide) | 36 | Deprotonated amide |
| 7 | Hydroxide | 34 | 9 species; CuO solid |
| 8 | Ethylenediamine | 34 | ML₂ |
| 9 | 2,2′-Bipyridyl | 33 | ML₃ + OH |
| 10 | Phenylalanine | 33 | ML₂ |

### Cu⁺ — Top ligands
| Rank | Ligand | VLMs | Max species |
|------|--------|------|-------------|
| 1 | Cyanide (CN⁻) | 15 | ML₄ + CuCN(s) |
| 2 | Chloride | 14 | ML₄ + CuCl(s) |
| 3 | Iodide | 8 | ML₄ + CuI(s) |
| 4 | Bromide | 7 | ML₃ + CuBr(s) |
| 5 | Ammonia | 6 | ML₂ |

---

## 4. Speciation Complexity

| Species | Max nuclearity | Max species per system | Richest system |
|---------|---------------|----------------------|----------------|
| Fe³⁺ | **Fe₇** (with acetate) | 12 (hydroxamates) | Threoninehydroxamic acid |
| Fe²⁺ | Fe₂ | 10 (2,6-PDPA) | Pyridine-2,6-diphosphonic acid |
| Cu²⁺ | Cu₃ | 9 (hydroxide) | Hydroxide system |
| Cu⁺ | Cu₂ | 6 (iodide) | Iodide system |

Fe³⁺ shows the most exotic polynuclear chemistry — the **Fe₇(OH)₉(acetate)₆** cluster is a remarkable molecular-scale precursor to iron oxide minerals (ferrihydrite, goethite, hematite).

---

## 5. Key Chemical Contrasts

| Feature | Iron | Copper |
|---------|------|--------|
| **Oxidation states (SRD-46)** | +2, +3 | +1, +2, +3 |
| **Dominant state** | Fe³⁺ (2.2× more ligands than Fe²⁺) | Cu²⁺ (overwhelmingly dominant) |
| **Preferred geometry** | Octahedral | Square planar/distorted octahedral (Cu²⁺); tetrahedral (Cu⁺) |
| **HSAB character** | Hard (Fe³⁺), borderline (Fe²⁺) | Borderline (Cu²⁺), soft (Cu⁺) |
| **Preferred donors** | Fe³⁺: O-donors (catecholates, hydroxamates, carboxylates); Fe²⁺: N-donors (bipy, phen) | Cu²⁺: N-donors (amines, imidazole, histidine); Cu⁺: soft donors (CN⁻, halides, phosphines) |
| **Hydrolysis** | Fe³⁺ hydrolyzes strongly → Fe₂, Fe₃, Fe₇ clusters | Cu²⁺ hydrolyzes moderately → Cu₂, Cu₃ dimers/trimers |
| **Peptide chemistry** | Rare deprotonated amide species | Cu²⁺ routinely deprotonates peptide NH groups (glycylglycine, glycyl-Ala) |
| **Solid phases** | α-Fe₂O₃, FeOOH, Fe(OH)₂, vivianite | CuO, CuCl, CuCN, CuBr, CuI |
| **Irving–Williams position** | Fe²⁺ below Cu²⁺ | Cu²⁺ at the top of the series |
| **Bioinorganic role** | O₂ transport (hemoglobin), electron transfer (cytochromes), iron storage (ferritin) | Electron transfer (blue copper proteins), oxidase enzymes (laccase, ceruloplasmin), SOD |

---

## 6. Chemistry Insights

1. **Irving–Williams series:** The EDTA data perfectly illustrates this fundamental trend — Fe²⁺ (log β = 14.33) < Cu²⁺ (18.78) ≪ Fe³⁺ (25.1). The Fe³⁺ value is anomalously high because charge density, not just the Irving–Williams order, dominates for trivalent ions.

2. **Siderophore selectivity:** Fe³⁺'s extreme affinity for oxygen donors (catecholates, hydroxamates) is the chemical basis of siderophore-mediated iron acquisition in bacteria. Tiron (a catecholate model) and acetohydroxamic acid both appear in Fe³⁺'s top ligand list, with up to ML₃ stoichiometry — exactly the tris-bidentate coordination seen in enterobactin.

3. **Cu⁺ soft-donor preference:** Cu⁺ is almost exclusively found with soft donors — CN⁻, Cl⁻, Br⁻, I⁻, and phosphines — consistent with HSAB theory. The [Cu(CN)₄]³⁻ complex (log β up to ML₄) is the basis of cyanide-based copper electroplating baths, while CuCl, CuBr, and CuI solids reflect the low solubility of cuprous halides exploited in analytical precipitation reactions.

---

*Source: NIST SRD-46 — NIST Critically Selected Stability Constants of Metal Complexes Database*

---