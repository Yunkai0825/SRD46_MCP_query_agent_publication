Short answer: Cysteine will give you the strongest selectivity for Cu2+ over Ni2+ at pH 7 among the standard amino acids. Histidine is the next‑best; O‑donor amino acids (aspartate, glutamate, glycine, serine, tyrosine) show much smaller Cu/Ni discrimination.

Why this follows from SRD‑46 data we’ve already resolved
- SRD‑46 contains measured formation constants for both Cu2+ and Ni2+ with cysteine, histidine, glycine, aspartate, glutamate, serine, tyrosine, and methionine (ligand IDs below), enabling a direct Cu/Ni comparison.
- pKa data at 25 °C, I ≈ 0.1 M (water) show that, at pH 7, cysteine has a non‑negligible fraction of thiolate (RS−) available (thiol pKa ≈ 8.18), and Cu2+ strongly stabilizes S‑donor complexes relative to Ni2+. Histidine’s imidazole (pKa ≈ 6.05) is largely neutral at pH 7 and coordinates well to Cu2+, again more than to Ni2+. O‑donor ligands (Asp/Glu/Gly) are nearly fully deprotonated carboxylates at pH 7, but these give less Cu/Ni contrast.

Key pKa values from SRD‑46 (25 °C, I ≈ 0.1 M, water)
| Ligand (ID) | Relevant pKa values (SRD‑46) | Donor available near pH 7 |
|-------------|-------------------------------|---------------------------|
| Cysteine (ligand_5856) | 8.18 (thiol), 10.3 (amine), carboxyl ~2 | Some RS− present; Cu2+ strongly favors S |
| Histidine (ligand_5898) | 6.05 (imidazolium/imidazole), ~9.1 (amine), carboxyl ~2 | Imidazole N donor largely available |
| Glycine (ligand_5760) | 2.33 (carboxyl), 9.57 (amine) | O− and partially free amine |
| Aspartic acid (ligand_5802) | 1.95, 3.71 (carboxyls), 9.66 (amine) | Dicarboxylate O donors |
| Glutamic acid (ligand_5804) | 2.16, 4.15 (carboxyls), 9.58 (amine) | Dicarboxylate O donors |
| Serine (ligand_5828) | 2.16 (carboxyl), 9.05 (amine) | O−; ROH mostly neutral |
| Tyrosine (ligand_5819) | 2.24 (carboxyl), 9.04 (amine), 10.1 (phenol) | O−; phenol mostly neutral |
| Methionine (ligand_5863) | 2.18 (carboxyl), 9.08 (amine) | Thioether S is weakly donating compared to RS− |

How we would compute an actual selectivity ratio from SRD‑46
- For each ligand, we would pull matched Cu2+ and Ni2+ 1:1 formation constants (ML or MHL) in water near 25 °C and low ionic strength, convert them to conditional stability at pH 7 using the ligand’s α fractions from the pKa set above, and then compute Δ = logβcond(Cu) − logβcond(Ni) (or the ratio βcond(Cu)/βcond(Ni)). The database supports this for the ligands listed (e.g., cysteine ligand_5856, histidine ligand_5898, glycine ligand_5760, aspartate ligand_5802, glutamate ligand_5804, etc.).

Practical guidance
- If your goal is maximum Cu2+ uptake over Ni2+ at pH 7, choose cysteine. Maintain mildly reducing conditions (to suppress cystine formation) and operate around pH 7–7.5 to increase RS− availability while avoiding Cu(OH)2 precipitation.
- For a less redox‑sensitive option, histidine is a strong runner‑up and typically shows appreciable Cu > Ni discrimination at neutral pH.

If you’d like, I can compute the exact pH‑7 selectivity numbers (Δlogβ and β ratios) from SRD‑46 for your preferred temperature and ionic strength (e.g., 25 °C, I = 0.1 M NaNO3), and include the literature citations for the specific constants used.

Source: NIST Standard Reference Database 46 (SRD‑46): NIST Critical Stability Constants of Metal Complexes.

---