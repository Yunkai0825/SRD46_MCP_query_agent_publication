I now have sufficient data to deliver a comprehensive final answer.

---

## Metal–Protein Binding in NIST SRD-46

### Direct Answer: Proteins Are Not in SRD-46

NIST SRD-46 does **not** contain entries for intact proteins as ligands. Searches for **transferrin, lactoferrin, ovotransferrin, serum albumin,** and **metallothionein** all returned **zero results**. The database is scoped to small molecules and defined macrocyclic/oligomeric ligands — not folded proteins.

---

### What SRD-46 *Does* Cover: Biologically Relevant Ligand Classes

The database contains **5,750 ligand entries** across classes that directly model the metal-binding chemistry found in proteins:

| Ligand Class | # Entries | Protein Relevance |
|---|---|---|
| Amino Acids | 297 | His, Cys, Asp, Glu, Met side chains |
| Peptides | 157 | Short backbone fragments |
| Polypeptides | 98 | Longer chain models |
| Hydroxamic acids | 74 | Siderophores; transferrin mimics |
| Catechols | 66 | Enterobactin-type Fe³⁺ binders |
| Pyrroles / Porphyrins | 134 | Heme analogs |
| Mercaptans (thiols) | 46 | Cys-type metal binding |
| Inorganic ligands | 101 | Carbonate (transferrin synergist) |

---

### Closest Analog to Transferrin: Desferriferrioxamine B (DFO)

Transferrin sequesters Fe³⁺ using hydroxamate-like oxygen donors. **Desferriferrioxamine B** (DFO, `ligand_9910`) is the canonical small-molecule analog — a trihydroxamic acid siderophore with 53 VLM measurements in SRD-46.

**Stability constants (logK, [M] + [HL] ⇌ [MHL]):**

| Metal | logK | T (°C) | I (M) |
|---|---|---|---|
| **Fe³⁺** | **30.7** | 25 | 0.1 |
| **Fe³⁺** | 30.6 | 20 | 0.1 |
| Ga³⁺ | 28.17 | 25 | 0.1 |
| Ga³⁺ | 27.56 | 25 | 1.0 |
| Al³⁺ | 24.14 | 25 | 0.1 |
| In³⁺ | 20.6 | 25 | 0.1 |
| Yb³⁺ | 16.0 | 20 | 0.1 |
| Cu²⁺ | 14.12 | 20 | 0.1 |

> *Source: NIST SRD-46, ligand_9910 (Desferriferrioxamine B)*

The extraordinary selectivity of DFO for Fe³⁺ (logK ≈ 30.7) over Cu²⁺ (logK ≈ 14.1) mirrors transferrin's own iron specificity — a difference of ~16 log units! This is why DFO (Desferal®) is used clinically to treat iron overload: it competes effectively even against protein-bound iron.

---

### Histidine — The Key Metal-Binding Amino Acid

L-Histidine (`ligand_5898`) has **250 VLM measurements** — the richest amino acid dataset in SRD-46. Its pKa profile (imidazole pKa = 6.05, α-NH₂ pKa = 9.1) makes it the dominant metal-binding residue in proteins like carbonic anhydrase (Zn²⁺), hemocyanin (Cu²⁺), and many metalloenzymes.

---

### Chemistry Insight

The SRD-46 data on DFO, histidine, cysteine, and catecholates collectively tell the story of **metal selectivity in biology**:
- **Fe³⁺** is captured by hard oxygen donors (hydroxamates, catecholates, carboxylates) — as in transferrin and ferritin
- **Cu²⁺ and Zn²⁺** prefer nitrogen/sulfur donors (imidazole, thiolate) — as in metallothionein and Cu chaperones
- **Zn²⁺** in enzymes is often coordinated by 2–3 His + 1 Asp/Glu, all well-represented in SRD-46

For full protein–metal binding data, complementary resources include **MetalPDB**, **PDB**, and **UniProt** metal-binding annotations.

---