SRD-46 does **not provide enough Cu/Ni stability-constant data here to calculate a defensible pH-7 selectivity ratio** for the amino acids in your list.

From the retrievable SRD-46 records in this session:

| Finding | Result |
|---|---|
| Amino-acid ligands resolved | glycine, alanine, aspartic acid, glutamic acid, tyrosine, serine, threonine, cysteine, penicillamine |
| Cu/Ni numerical stability data successfully retrieved | none |
| pKa data retrieved | yes, for the ligands above |
| Catalog evidence for both Cu and Ni complexes | only glycine was explicitly retained in the catalog subset |

So the **strict SRD-46 answer** is:

| Question | Answer |
|---|---|
| Which amino acid gives the best Cu²⁺/Ni²⁺ selectivity ratio at pH 7? | **Cannot be determined conclusively from the retrieved SRD-46 numerical stability data in this session** |

That said, using the **available SRD-46 pKa data plus standard coordination-chemistry expectations**, the **best practical candidate is penicillamine**, with **cysteine** as the next-best choice:

| Ligand | Relevant pKa values from SRD-46 | Qualitative Cu²⁺ vs Ni²⁺ expectation at pH 7 |
|---|---:|---|
| Penicillamine | 7.96, 10.67 | Best expected Cu preference |
| Cysteine | 8.18, 10.3 | Strong Cu preference, likely slightly below penicillamine |
| Glycine / alanine / serine / threonine | carboxyl ~2.2–2.3; amine ~8.9–9.7 | Much weaker Cu/Ni discrimination |
| Aspartic / glutamic acid | extra carboxyl pKa 3.71 / 4.15; amine ~9.6 | O-rich donors, not ideal for maximizing Cu over Ni |
| Tyrosine | 2.24, 9.04, 10.1 | Less compelling than thiol-containing ligands |

## Bottom line

| Recommendation | Confidence |
|---|---|
| **Penicillamine** is the best amino-acid ligand to try for selective Cu²⁺ complexation over Ni²⁺ at pH 7 | **Qualitative only; not numerically validated from retrieved SRD-46 stability constants** |

Chemistry insight: at pH 7, **thiol-containing amino acids** are the most promising because Cu²⁺ is typically favored over Ni²⁺ by softer **S,N,O donor sets**. Penicillamine should edge out cysteine because its donor environment and substitution pattern usually enhance Cu selectivity while disfavoring Ni somewhat more.

If you want, I can next do a **broader SRD-46 search focused only on cysteine vs penicillamine vs glycine** and try to extract any hidden Cu/Ni stability records for a more quantitative comparison.

---