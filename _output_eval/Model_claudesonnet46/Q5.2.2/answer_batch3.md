## Metal–Protein Binding in NIST SRD-46: Complete Answer

### Direct Finding: Protein Macromolecules Are Not in SRD-46

After a thorough search, **no protein macromolecules** appear as ligands in NIST SRD-46. The database is scoped to small, well-defined ligands for which thermodynamically rigorous, critically evaluated stability constants (log β) can be reported and reproduced across laboratories.

| Protein Searched | Found in SRD-46? |
|---|---|
| Transferrin | ❌ Not found |
| Albumin | ❌ Not found |
| Metallothionein | ❌ Not found |
| Hemoglobin / Myoglobin | ❌ Not found |
| Ferritin | ❌ Not found |
| Hematoporphyrin / TPPS (porphyrins) | ⚠️ Listed, but 0 measurements |

---

### Why Proteins Are Excluded

Macromolecular proteins present fundamental challenges for the SRD-46 critical evaluation framework:

1. **Multiple non-equivalent binding sites** — A single log β cannot capture heterogeneous coordination environments.
2. **Conformational coupling** — Metal binding induces protein folding/unfolding, violating simple equilibrium assumptions.
3. **Synergistic anion requirements** — Transferrin, for example, requires carbonate as a synergistic anion alongside Fe³⁺, making the system too complex for a standard stability constant.
4. **Reproducibility** — Batch-to-batch protein variability prevents the critical evaluation that SRD-46 demands.

---

### What SRD-46 *Does* Have: Protein-Site Surrogate Ligands

SRD-46 is rich in the **amino acids, peptides, and heterocycles** that form the actual metal-coordinating residues inside proteins — the chemist's toolkit for modeling metalloprotein active sites:

| Ligand | SRD-46 ID | Class | # Measurements | Key pKa Values |
|---|---|---|---|---|
| Glycine | ligand_5760 | Amino Acids | 428 | 2.33 (COOH), 9.57 (NH₃⁺) |
| L-Histidine | ligand_5898 | Amino Acids | 250 | 6.05 (imidazolium), 9.10 (NH₃⁺) |
| L-Cysteine | ligand_5856 | Amino Acids | 134 | 8.18 (SH), 10.30 (NH₃⁺) |
| Imidazole | ligand_7795 | Pyrroles/Azoles | 237 | 7.00 |
| Glutathione (γ-Glu-Cys-Gly) | ligand_6592 | Tripeptides | 106 | 2.08, 3.49, 8.64, 9.51 |
| Glutathione disulfide (GSSG) | ligand_6682 | Polypeptides | 53 | 6 protonation steps |

---

### Representative Stability Constants: Fe(III)–Cysteine (25 °C, I = 0.1 M)

The most biologically striking data retrieved are for **Fe(III) + L-Cysteine**, directly relevant to iron–sulfur protein chemistry:

| Metal | Ligand | Complex | log β | Temp (°C) | Ionic Str. (M) |
|---|---|---|---|---|---|
| Fe(III) | L-Cysteine | ML (1:1) | **11.60** | 25 | 0.1 |
| Fe(III) | L-Cysteine | ML₂ (1:2) | **22.70** | 25 | 0.1 |
| Fe(III) | L-Cysteine | ML₃ (1:3) | **33.86** | 25 | 0.1 |

The stepwise increment is remarkably consistent (~11 log units per cysteine ligand), reflecting the powerful thiolate–Fe(III) interaction that underpins iron–sulfur cluster assembly and cysteine-rich metalloprotein sites such as rubredoxin and ferredoxin.

---

### Chemistry Insight

> **Connecting small-molecule data to proteins:** Transferrin binds Fe³⁺ with log K ~ 20–22 per site, arising from a synergistic tetradentate pocket (Tyr + His + Asp residues + carbonate). The SRD-46 cysteine data (log β₃ = 33.86 for three thiolates) illustrates *why* metallothionein — with ~20 Cys residues — sequesters toxic metals like Cd²⁺ and Hg²⁺ so effectively. Similarly, histidine's imidazole pKa of 6.05 explains why the His₃ motif is ubiquitous in zinc finger proteins and carbonic anhydrase: at physiological pH, imidazole is predominantly neutral and an excellent σ-donor to Zn²⁺. Glutathione (106 measurements in SRD-46) is the cell's primary low-molecular-weight metal buffer, and its stability constants with Cu, Zn, and Fe are directly relevant to intracellular metal homeostasis.

---

### Recommended Resources for Direct Protein–Metal Binding Data

| Resource | Focus |
|---|---|
| **MetalPDB** | Metal coordination geometries in PDB crystal structures |
| **BRENDA** | Enzyme metal cofactor affinities (Kd, Km) |
| **BioLiP** | Biologically relevant ligand–protein interactions |
| **SC-Database (Protonic Software)** | Broader stability constants, including some macromolecular entries |

*All data sourced from NIST SRD-46 Critically Selected Stability Constants of Metal Complexes Database.*

---