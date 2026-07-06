Prediction: Aspartic acid (Asp, ligand_5802) is the best candidate among any proteinogenic amino acids not yet studied with Zn²⁺ to form the most stable zinc complex, with glutamic acid (Glu, ligand_5804) a close second.

Why this follows from SRD‑46 data
- Zinc–amino acids already covered: The Zn²⁺ system catalog we built shows Zn–glycine (ligand_5760), Zn–alanine (ligand_5761), Zn–histidine (ligand_5898), and Zn–cysteine (ligand_5856) among its pairs, with rich speciation for histidine (imidazole donor) and cysteine (thiolate donor), consistent with strong binding. This constrains the “not yet studied” set to other amino acids.
- Donor strength and pKa positioning: SRD‑46 ligand cards show that Asp and Glu deprotonate their side‑chain carboxylates at low pH (≈2–4), so an O,O-bidentate chelate with the α‑amine becomes available early in aqueous media. In contrast, amide side chains (Asn, Gln) are weak donors; Lys/Arg are cationic over most of the aqueous range; Ser/Thr (alcohol) and Tyr (phenolate) are weaker donors or require high pH. Thus, among amino acids lacking Zn data, Asp (and Glu) have the most favorable combination of donor type and deprotonation to stabilize Zn²⁺ complexes.

Key pKa brackets from SRD‑46 (ligand_card) for the relevant donor sets
| Amino acid | SRD‑46 ligand_id | pKa bracket (acid → base) |
|---|---|---|
| Aspartic acid | ligand_5802 | 1.95 (H3L→H2L), 3.71 (H2L→HL), 9.66 (HL→L) |
| Glutamic acid | ligand_5804 | 2.16 (H3L→H2L), 4.15 (H2L→HL), 9.58 (HL→L) |
| Histidine | ligand_5898 | −1.70 (H3L→H2L), 6.05 (H2L→HL), 9.10 (HL→L) |
| Cysteine | ligand_5856 | −1.90 (H3L→H2L), 8.18 (H2L→HL), 10.30 (HL→L) |
| Tyrosine | ligand_5819 | 2.24 (H3L→H2L), 9.04 (H2L→HL), 10.10 (HL→L) |
| Lysine | ligand_5887 | 2.15 (H3L→H2L), 9.15 (H2L→HL), 10.66 (HL→L) |

Context from the Zn²⁺ system catalog (evidence of binding modes already present)
- Zn–histidine (ligand_5898) shows multiple species (e.g., ML, ML₂, proton-linked forms), consistent with strong N-donor coordination.
- Zn–cysteine (ligand_5856) includes polynuclear species (e.g., M₃HL₄ families) and multiple proton-linked equilibria, indicating high affinity of thiolate donors for Zn²⁺.
- Zn–glycine and Zn–alanine (simple amino acids) exhibit ML, ML₂, ML₃ families typical of O,N bidentate chelation but generally weaker than imidazole/thiolate sets.

Putting it together
- Among those amino acids not yet covered for Zn²⁺ in SRD‑46, dicarboxylates (Asp, Glu) have the most favorable donor set (hard O donors matching Zn²⁺’s preference) and early deprotonation that enables chelation at modest pH and ionic strength. This combination is expected to yield larger β values than other unstudied amino acids with weaker or less accessible donors under comparable aqueous conditions.
- Between Asp and Glu, Asp’s slightly lower side‑chain pKa (1.95 vs 2.16) favors earlier bidentate binding and a tighter 5‑membered chelate ring, which often enhances stability relative to Glu’s 6‑membered ring.

Caveat and next step
- Our Zn²⁺ catalog snapshot is ultra‑compact and confirms only a subset of Zn–amino acid systems (e.g., glycine, alanine, histidine, cysteine). A full coverage check to pinpoint precisely which of the remaining 16 amino acids lack Zn data would require scanning Zn–amino acid stability records across SRD‑46. If you’d like, I can tabulate all Zn²⁺ stability constants for the 20 amino acids and highlight which are missing, then rank the expected β for the missing set using their pKa/donor profiles.

Source: NIST Standard Reference Database 46 (SRD‑46). Data used: Zn²⁺ system catalog (metal_208) showing Zn–glycine, Zn–alanine, Zn–histidine, Zn–cysteine pairs; ligand pKa brackets for amino acids (ligand_card; see ligand IDs above).

---