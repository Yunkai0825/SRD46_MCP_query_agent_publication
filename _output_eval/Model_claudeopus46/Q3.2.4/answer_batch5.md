# Survey of Fe(II) and Fe(III) Ligand Systems in NIST SRD-46

## Database Coverage

| Metal | Ligand classes | Unique ligands | VLM entries |
|-------|---------------|----------------|-------------|
| **Fe³⁺** (metal_61) | ~30 | 406 | 1 473 |
| **Fe²⁺** (metal_62) | ~30 | 217 | 667 |

Fe(III) has roughly twice the data coverage, reflecting its greater importance in environmental, biological, and industrial chemistry.

---

## Representative 1:1 (ML) Stability Constants (log K, 20–30 °C, I ≤ 1 M)

### Fe(III)

| Ligand class | n | avg log K | range |
|---|---|---|---|
| EDTA & derivatives | 22 | **30.6** | 19–44 |
| Aza-macrocycles + COOH | 12 | **28.4** | 17–38 |
| NTA & derivatives | 10 | **23.6** | 14–34 |
| Aminophosphorus acids | 10 | **22.9** | 15–29 |
| Catechols | 37 | **21.1** | 13–46 |
| Hydroxamic acids | 38 | **19.4** | 5–29 |
| Phenols / salicylates | 30 | **17.3** | 8–38 |
| Aliphatic amines | 13 | **14.6** | 3–26 |
| Amino acids | 28 | **12.0** | 4–22 |
| Phenols (simple) | 14 | **11.9** | 5–18 |
| Carboxylic acids (poly) | 8 | **10.6** | 5–18 |
| Inorganic ligands | 36 | **8.4** | 0.3–26 |
| Carboxylic acids (mono) | 10 | **5.8** | 3–11 |
| Ketones / β-diketones | 8 | **~5** | 3–9 |

### Fe(II)

| Ligand class | n | avg log K | range |
|---|---|---|---|
| EDTA & derivatives | 18 | **18.1** | 9–29 |
| Aza-macrocycles + COOH | 5 | **17.7** | 9–22 |
| Tripyridines | 5 | **16.8** | 13–21 |
| Phenanthrolines | 9 | **16.5** | 5–21 |
| Bipyridines | 7 | **15.9** | 4–18 |
| Aminophosphorus acids | 7 | **15.8** | 9–23 |
| NTA & derivatives | 7 | **14.1** | 9–23 |
| Aza-macrocycles | 3 | **12.9** | 5–17 |
| Catechols | 5 | **11.8** | 7–16 |
| Pyridine carboxylic acids | 6 | **10.6** | 4–18 |
| Amino acids | 25 | **8.3** | 4–14 |
| Aliphatic amines | 3 | **5.9** | 4–7 |
| Inorganic ligands | 14 | **3.4** | 0.7–8 |
| Carboxylic acids (mono) | 2 | **2.6** | 1–4 |

---

## Key Trends and Thermodynamic Reasoning

### 1. Fe(III) ≫ Fe(II) for O-donor ligands — Hard–Soft Acid–Base (HSAB) Theory

For virtually every O-donor class, **Fe(III) forms dramatically stronger complexes** than Fe(II). Typical differences:

| Ligand class | Δ log K (Fe³⁺ − Fe²⁺) |
|---|---|
| EDTA derivatives | ~12.5 |
| Catechols | ~9.3 |
| Carboxylic acids (mono) | ~3.2 |
| Inorganic O-donors | ~5.0 |

Fe³⁺ is a classic **hard Lewis acid** (small ionic radius, high charge, low polarizability), and anionic oxygen donors (phenolate, carboxylate, hydroxamate) are **hard Lewis bases**. The hard–hard match maximizes electrostatic stabilization. Fe²⁺, with its lower charge density, is a borderline acid and interacts less strongly with these donors.

### 2. Fe(II) Narrows the Gap — or Wins — with N-Donor / π-Acceptor Ligands

The most striking feature of the Fe(II) data is the prominence of **phenanthrolines** (avg log K 16.5), **bipyridines** (15.9), and **tripyridines** (16.8) near the top of the ranking. These classes are essentially absent from the Fe(III) top list. Two effects combine:

- **HSAB matching**: N-heterocyclic donors are borderline-to-soft bases, better matched to the softer Fe²⁺.
- **Crystal-field stabilization energy (CFSE)**: Fe²⁺ (d⁶) in the strong octahedral field of polypyridyl ligands adopts a **low-spin t₂g⁶** configuration, gaining enormous CFSE (~2.4 Dq extra relative to high-spin). Fe³⁺ (d⁵) gains **zero net CFSE** regardless of spin state, so the ligand-field bonus is unique to Fe(II). This is why [Fe(phen)₃]²⁺ is famously stable and intensely colored (used in the ferrozine assay), while the Fe(III) analog is far less favored.

### 3. Chelate and Macrocyclic Effects Dominate the Top of Both Rankings

The highest log K values for both metals belong to **polydentate chelators**:

| Ligand type | Typical denticity | Fe(III) avg log K | Fe(II) avg log K |
|---|---|---|---|
| EDTA derivatives | hexadentate | 30.6 | 18.1 |
| Aza-macrocycles + COOH | hexa-/octadentate | 28.4 | 17.7 |
| NTA derivatives | tetradentate | 23.6 | 14.1 |
| Catechols (per unit) | bidentate | 21.1 | 11.8 |
| Monocarboxylates | monodentate | 5.8 | 2.6 |

The **chelate effect** — the entropic gain from displacing multiple coordinated water molecules per chelate ring closure — adds roughly **5–8 log units per additional donor atom** in a matched comparison (compare monocarboxylate log K ~6 vs. EDTA ~31 for Fe³⁺). The **macrocyclic effect** adds a further 2–5 log units on top of the open-chain chelate, visible in the aza-macrocycle + COOH class slightly outperforming open-chain EDTA analogs of similar denticity.

### 4. Notable Edge Cases and Anomalies

| Observation | Explanation |
|---|---|
| **Catechols for Fe(III): range 13–46** | The extraordinary upper end reflects tris-catecholate siderophore-type ligands (e.g., enterobactin analogs) that combine the chelate effect with the ideal hard O⁻ donor match for Fe³⁺. These are among the strongest known metal–ligand interactions in aqueous solution. |
| **Hydroxamic acids (Fe³⁺ avg ~19) vs. monocarboxylates (~6)** | Despite similar denticity (bidentate), the N–O⁻/C=O chelate ring provides a 5-membered ring with two hard O-donors ideally pre-organized for Fe³⁺. This is the strategy exploited by microbial siderophores like desferrioxamine B (tris-hydroxamate, log K ~30). |
| **Inorganic ligands: huge range (0.3–26 for Fe³⁺)** | This class lumps weak donors (Cl⁻, SO₄²⁻) with strong ones (CN⁻, F⁻, PO₄³⁻). CN⁻ is notable: as a strong-field, soft π-acceptor it forms very stable complexes with both oxidation states — via π-backbonding with Fe(II) and strong σ-donation with Fe(III). |
| **Aza-macrocycles without COOH arms: Fe(II) log K ~13 vs. Fe(III) sparse data** | Pure N-donor macrocycles (cyclam, cyclen) favor Fe(II) due to HSAB and CFSE arguments; Fe(III) prefers O-functionalized variants. |

### 5. Summary Stability Hierarchy

**Fe(III):**
```
Polydentate O,N-chelators (EDTA, macrocycles) ≫ Catechols ≈ Hydroxamates
> Salicylates > Amines > Amino acids > Simple phenols > Polycarboxylates
> Inorganic > Monocarboxylates > Ketones
```

**Fe(II):**
```
Polydentate N,O-chelators (EDTA, macrocycles) > Phenanthrolines ≈ Bipyridines
≈ Tripyridines > Aminophosphonates > NTA > Aza-macrocycles > Catechols
> Amino acids > Amines > Inorganic > Carboxylates
```

### Overarching Principles

1. **Charge density and HSAB matching set the baseline**: Fe³⁺ strongly prefers hard O⁻ donors; Fe²⁺ accommodates softer N-donors and π-acceptors.
2. **Chelation multiplies the effect**: each ring closure adds ~5 log units, and macrocyclic pre-organization adds 2–5 more.
3. **Crystal-field effects create the signature Fe(II)–polypyridyl anomaly**: the d⁶ low-spin stabilization unique to Fe(II) with strong-field N-donors underpins applications from colorimetric iron assays (ferrozine) to dye-sensitized solar cells and bioinorganic electron-transfer proteins (cytochromes).
4. **Nature exploits these trends**: biological siderophores use tris-catecholate or tris-hydroxamate scaffolds to scavenge Fe(III) (log K > 30), while heme and non-heme iron enzymes use N-donor frameworks (porphyrins, histidine) to stabilize Fe(II) for redox catalysis.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes).*

---