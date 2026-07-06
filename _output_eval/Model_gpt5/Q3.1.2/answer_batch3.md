Short answer: I can’t rank amino‑acid ligands by Cu2+/Ni2+ selectivity at pH 7 from SRD‑46 yet. In this session the L0 name lookups for “copper/nickel” and common amino acids returned no hits and I was blocked from running the stability/pKa queries needed to compute conditional selectivity; so I don’t have any SRD‑46 constants to report.

How I’ll answer this rigorously from NIST SRD‑46 (and what I’ll return):
- Pull aqueous stability constants (20–30 °C, I ≤ 0.5 M when available) for Cu2+ and Ni2+ with each amino acid under their SRD‑46 names (e.g., glycinate, histidinate, cysteinate, aspartate, glutamate, etc.).
- Pull ligand pKa values to get the fraction of the binding form at pH 7 (αL), correcting for stoichiometry (e.g., ML, ML2).
- Compute conditional log β at pH 7 for each metal–ligand pair and the selectivity: log S = log βcond(Cu2+) − log βcond(Ni2+).
- Return a ranked table of ligands with log βcond(Cu2+), log βcond(Ni2+), and log S at pH 7 under the stated conditions.

Practical note while I run the data: amino‑acid naming in SRD‑46 often uses anionic forms (e.g., “glycinate”, “histidinate”) and specific protonation/stoichiometries; I’ll query by those synonyms and by ligand class to avoid the earlier name‑match miss.

If you confirm the conditions I should use (e.g., 25 °C, ionic strength ~0.1 M in water, no added buffer/electrolyte preference), I’ll return the ranked selectivity table from NIST SRD‑46 in my next message.

Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes).

---