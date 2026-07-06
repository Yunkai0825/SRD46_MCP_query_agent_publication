Below is a short list of Ca‑selective masking agents (stronger interaction with Ca2+ than with Cu2+) distilled from the NIST SRD‑46 ligand/metal entries we resolved in this session. I include SRD‑46 ligand IDs for traceability and brief practical notes; entries in the “Avoid” table are ligands that complex Cu2+ strongly and thus are unsuitable when you want to leave Cu2+ uncomplexed.

Recommended (Ca2+ binds strongly; Cu2+ only weakly)
| Ligand (SRD‑46 ID) | Donor type | Ca2+ behavior in SRD‑46 | Cu2+ behavior in SRD‑46 | Practical notes |
|---|---|---|---|---|
| Carbonate / bicarbonate (ligand_10096) | Hard O donor | Strong interaction; CaCO3(s) precipitation favored in alkaline media | Much weaker interaction than with Ca2+ | From SRD‑46 summary: “Hard O; forms CaCO3(s). Ca≫Cu.” Use moderately alkaline pH (bicarbonate/carbonate region; SRD‑46 pKa ~6.13, 9.91) to remove Ca2+ with minimal Cu2+ complexation. |
| Hydrogen sulfate / sulfate (ligand_10148) | Hard O donor | Forms CaSO4(s); suppresses Ca2+ | Weak Cu2+ binding | SRD‑46 notes: “forms CaSO4(s); weak Cu binding.” Useful when sulfate addition is compatible with the matrix. |
| Aminodisulfonic acid (ligand_10153) | Two sulfonate O donors | Favors hard Ca2+ | Poor Cu2+ chelation | SRD‑46 notes: “two sulfonates; favors hard Ca2+, poor Cu chelation.” Becomes more anionic near pH ~8.5 (SRD‑46 note) which enhances Ca2+ binding. |
| 18‑crown‑6 (ligand_9676) | Polyether O donors | Crown ethers commonly used to bind alkaline‑earths (Ca2+) | Typically weaker for Cu2+ | SRD‑46 lists the 18‑crown‑6 family and notes their usefulness for Ca2+ masking with weaker Cu2+ binding. Aqueous constants can be sparse; often more effective in mixed solvents—check your matrix. |
| Acetate (ethanoate) (ligand_8465) | Monocarboxylate O donor | Weak chelation; can modestly engage Ca2+ | Weak for Cu2+ | Very mild/second‑tier “mask”; useful mainly for ionic strength/pH control rather than strong Ca masking. |
| Malonate (ligand_8873) | Dicarboxylate O donors | Moderate Ca2+ binding | Cu2+ interaction present but generally weaker than with N‑donor chelators | A softer option than polyaminocarboxylates; if used, keep pH where one/two carboxylates are deprotonated to favor Ca2+ over Cu2+. |

Avoid for Ca‑only masking (bind Cu2+ strongly)
| Ligand (SRD‑46 ID) | Reason to avoid (from SRD‑46 notes) |
|---|---|
| EDTA (ligand_6277) and derivatives HEDTA (ligand_6275), EEDTA (ligand_6335), TEDTA (ligand_6348), aza‑macrocycle 24edtaen (ligand_6118) | SRD‑46 explicitly flags these polyaminopolycarboxylate/aza‑macrocycle N,O donors as very strong for Cu2+ (≫Ca2+). Not suitable when Cu2+ must remain uncomplexed. |
| Thiosulfate (ligand_10149) | SRD‑46: forms strong Cu–thiosulfate complexes [Cu(S2O3)x]; dissolves Cu salts. |
| Sulfamate (ligand_10151) | SRD‑46: Cu–sulfamate complexes are used in plating → binds Cu2+. |
| Trithiocarbonate (ligand_10097), perthiocarbonate (ligand_10098), triselenocarbonate (ligand_10099) | SRD‑46: soft S/Se donors bind Cu2+ much more strongly than Ca2+. |

How to apply this in practice
- For robust Ca removal with minimal Cu2+ complexation, carbonate/bicarbonate or sulfate additions (where compatible) are effective because they preferentially remove Ca2+ by precipitation (CaCO3, CaSO4) while leaving Cu2+ largely in solution.
- If a chelating (non‑precipitating) mask is needed, consider aminodisulfonic acid or, where your solvent system allows, 18‑crown‑6. Both are O‑donor systems that favor hard Ca2+ and show weaker affinity for Cu2+ in the SRD‑46 profiles.
- Avoid polyaminocarboxylate chelators (EDTA family, aza‑macrocycles) and soft‑donor anions (thiosulfate, thio/seleno‑carbonates), which strongly complex Cu2+ and will defeat the purpose.

Notes and next steps
- I attempted to pull matched‑condition log β (ML, ML2; ~25 °C, I ≈ 0.1 M, aqueous) for a quantitative Δlogβ ranking, but no records surfaced under the strict filters within the time budget. If you share your actual ionic medium and pH window, I can relax the filters (e.g., accept I ≈ 0.0 or a single medium like NaClO4) and extract specific constants and citations from SRD‑46 to numerically rank these masks for your conditions.

Source: NIST Standard Reference Database 46 (SRD‑46): Critical Stability Constants of Metal Complexes (ligand and system entries cited above by SRD‑46 ligand IDs).

---