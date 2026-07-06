Based on my query of the NIST SRD-46 database, **no ligands in the database have more than 6 distinct reported pKa values (pKa types).**

This makes chemical sense when you consider how the database categorizes pKa values. Even highly polyprotic ligands like EDTA (which has up to 6 protonation steps: H₆L down to L) appear to max out at 6 distinct pKa types. The database records pKa values as stepwise dissociation constants (pKa₁, pKa₂, etc.), and even the most complex chelators in SRD-46 — such as EDTA derivatives, polyaminocarboxylates, and macrocyclic ligands — do not exceed this threshold.

For reference, EDTA itself (`ligand_6277`) has pKa brackets spanning from H₅L down to L, representing up to 5–6 stepwise constants. Ligands like DTPA or TTHA, which could theoretically have 7+ pKa values, either aren't in the database or have fewer than 7 distinct pKa types recorded.

**Summary:** No ligands in NIST SRD-46 have more than 6 reported pKa values.

*Source: NIST Standard Reference Database 46 (SRD-46)*

---