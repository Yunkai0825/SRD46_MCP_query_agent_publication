## Metal–Protein Binding in NIST SRD-46

**Short answer: SRD-46 does not contain stability constants for intact proteins such as transferrin, albumin, ferritin, or metallothionein.** No ligand entries or literature citations for these macromolecules were found. The database focuses on small-molecule ligands with well-defined stoichiometries.

### What SRD-46 *does* have: Polypeptide Ligands

The database includes **98 polypeptide ligands**, mostly di-, tri-, and tetrapeptides. The longest and most biologically relevant is **fibrinopeptide A** (ligand\_6692), a 16-residue peptide with stability data for Cu²⁺ and Zn²⁺.

#### Fibrinopeptide A — pKₐ Values (25 °C, I = 0.1 M)

| Equilibrium | log K |
|---|---|
| L + H ⇌ HL | 8.40 |
| HL + H ⇌ H₂L | 5.03 |
| H₂L + H ⇌ H₃L | 4.31 |
| H₃L + H ⇌ H₄L | 3.62 |
| H₄L + H ⇌ H₅L | 3.50 |
| H₅L + H ⇌ H₆L | 2.60 |

#### Fibrinopeptide A — Metal Binding Constants (25 °C, I = 0.1 M)

| Metal | Equilibrium | log K |
|---|---|---|
| Cu²⁺ | M + L ⇌ ML | 7.21 |
| Cu²⁺ | MH₋₁L + H ⇌ ML | 3.81 |
| Cu²⁺ | M(OH)(H₋₁L) + H ⇌ M(H₋₁L) + H₂O | 10.00 |
| Zn²⁺ | M + L ⇌ ML | 3.20 |
| Zn²⁺ | M(OH)L + H ⇌ ML + H₂O | 7.05 |
| Zn²⁺ | M(OH)₂L + H ⇌ M(OH)L + H₂O | 8.00 |

### Chemistry Insight

The Cu²⁺–fibrinopeptide A binding (log K = 7.21) is substantially stronger than Zn²⁺ (log K = 3.20), consistent with the Irving–Williams series and Cu²⁺'s preference for peptide amide nitrogen donors. These short-peptide constants serve as **model compound data** for understanding metal–backbone interactions in proteins, but they cannot capture the specialized binding sites of proteins like transferrin, which achieves log K ≈ 20–22 for Fe³⁺ through a precisely arranged Tyr/His/Asp/carbonate binding pocket.

For intact protein–metal binding data, consider resources such as **MetalPDB**, **BRENDA**, or primary literature reviews on metalloprotein thermodynamics.

*Source: NIST SRD-46 (Critically Selected Stability Constants of Metal Complexes)*

---