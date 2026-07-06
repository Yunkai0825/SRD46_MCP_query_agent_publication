## Metal–Protein Binding in NIST SRD-46

**NIST SRD-46 does not contain stability constant data for intact proteins such as transferrin, albumin, lactoferrin, or any other macromolecular ligands.** The database is focused on small-molecule equilibrium constants.

### What the database covers

SRD-46 contains **12,417 ligands** across 18 classes. Here is the full landscape:

| Ligand Class | Number of Ligands |
|---|---|
| Carboxylic acids | 2,024 |
| Amines | 1,469 |
| Nitrogen heterocycles | 1,302 |
| Other | 1,247 |
| Macrocyclic ligands | 1,117 |
| Phenols | 1,019 |
| Miscellaneous | 1,006 |
| Schiff bases | 604 |
| Phosphorus ligands | 589 |
| Alcohols | 404 |
| Sulfur ligands | 373 |
| **Peptides** | **321** |
| **Amino Acids** | **297** |
| Ethers | 224 |
| Ketones | 149 |
| Nucleotides | 119 |
| **Polypeptides** | **98** |
| Aldehydes | 55 |

The largest biomolecule present is **fibrinopeptide A** (a 16-residue polypeptide, `ligand_6692` with 12 measurements), but no intact proteins appear in the database.

### What SRD-46 *can* offer: amino acid & peptide–metal constants

While transferrin itself is absent, the **building blocks** of protein metal-binding sites are extensively covered. For example, here are Fe³⁺–histidine stability constants — directly relevant to the histidine residues that coordinate iron in transferrin:

| System | β Definition | Constant Type | Value | T (°C) | I (mol/L) | Electrolyte |
|---|---|---|---|---|---|---|
| Fe³⁺ + L-Histidine | ML/M·L | log K | **10.07** | 25 | 0.2 | KCl |
| Fe³⁺ + L-Histidine | ML/M·L | log K | **10.0** | 25 | 0.15 | NaClO₄ |
| Fe³⁺ + L-Histidine | ML₂/M·L₂ | log β | **18.5** | 25 | 0.2 | KCl |
| Fe³⁺ + L-Histidine | ML₃/M·L₃ | log β | **25.3** | 25 | 0.2 | KCl |
| Fe³⁺ + L-Histidine | MHL/M·HL | log K | **3.3** | 25 | 0.15 | NaClO₄ |
| Fe³⁺ + L-His methyl ester | ML/M·L | log K | **5.5** | 25 | 0.15 | NaClO₄ |
| Fe³⁺ + L-His methyl ester | ML₂/M·L₂ | log β | **10.2** | 25 | 0.15 | NaClO₄ |
| Fe³⁺ + L-His methyl ester | ML₃/M·L₃ | log β | **13.3** | 25 | 0.15 | NaClO₄ |

### Chemistry insight

The very high log K ≈ 10 for Fe³⁺–histidine reflects the strong affinity of ferric iron for imidazole nitrogen donors — the same interaction that anchors Fe³⁺ in transferrin's binding cleft (where two histidine residues, one aspartate, one tyrosine, and a synergistic carbonate coordinate the metal). The ~4.5 log-unit drop for the histidine methyl ester highlights the critical role of the free carboxylate as a secondary donor group. These small-molecule constants provide a thermodynamic foundation for understanding why nature selected these particular amino acid side chains for iron transport proteins.

### Recommendations for protein-level data

For intact metal–protein binding constants (e.g., Fe³⁺–transferrin, K_d ~ 10⁻²² M), consider:
- **Primary literature** (e.g., Aisen & Leibman, *Biochim. Biophys. Acta*, 1972)
- **PDB** (Protein Data Bank) for structural metalloprotein data
- **MetalPDB** or **BioLiP** for metalloprotein binding-site databases

If you're interested, I can explore stability constants for other biologically relevant amino acids (cysteine, tyrosine, aspartate, glutamic acid) or short peptides with specific metals — SRD-46 has extensive data in those areas that can illuminate the coordination chemistry underlying protein metal-binding sites.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes)*

---