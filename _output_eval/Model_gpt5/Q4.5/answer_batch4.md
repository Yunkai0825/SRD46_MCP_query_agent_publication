Below is a data snapshot of ligand acid dissociation constants (pKa) relevant to Ca2+ complexation, drawn from NIST SRD‑46. Because the stability constants (log β) for Ca2+ could not be retrieved within the time budget, I summarize trends and give a testable hypothesis rather than compute a correlation coefficient.

Representative ligand pKa values (near 25 °C; brackets copied from SRD‑46 entries)
| Ligand (SRD‑46 name) | ID | Class | Key pKa values (from pKa brackets) | Notes on donors |
|---|---|---|---|---|
| Ethanedioic acid (Oxalic acid) | ligand_8872 | Diacid | pKa1 = −1.2, pKa2 = 3.8 | 2×COOH (bidentate carboxylates possible) |
| 2‑Hydroxypropane‑1,2,3‑tricarboxylic acid (Citric acid) | ligand_9058 | Triacid | pKa1 = 2.9, pKa2 = 4.35, pKa3 = 5.65 | 3×COOH + OH (multidentate) |
| D‑2‑Hydroxypropanoic acid (Lactic acid) | ligand_8641 | Monoacid | pKa ≈ 3.67 | 1×COOH + OH |
| L‑Hydroxybutanedioic acid (Malic acid) | ligand_8953 | Diacid | pKa1 = 3.24, pKa2 = 4.68 | 2×COOH + OH |
| Butanedioic acid (Succinic acid) | ligand_8907 | Diacid | pKa1 = 3.99, pKa2 = 5.24 | 2×COOH |
| D‑Tartaric acid | ligand_8955 | Diacid | pKa1 = 2.82, pKa2 = 3.97 | 2×COOH + 2×OH |
| Aminoacetic acid (Glycine) | ligand_5760 | Zwitterionic | pKaCOOH ≈ 2.33, pKaNH3+ ≈ 9.57 | COOH + NH2 (can chelate via O and N) |
| Ethylenedinitrilotetraacetic acid (EDTA) | ligand_6277 | Aminopolycarboxylate | sequence: −1.5, 2.00, 2.69, 6.13, 9.52 | 4×COOH + 2×N (high denticity) |
| EGTA | ligand_6342 | Aminopolycarboxylate | sequence: −1.9, 2.70, 8.71, 9.32 | 4×COOH + 2×N (preorganized O‑rich) |
| Hydrogen phosphate (Phosphoric acid) | ligand_10113 | Inorganic oxyanion | pKa1 = 1.92, pKa2 = 6.71, pKa3 = 11.52 | PO4 tetra‑O donor; multiple deprotonations |
| Hydrogen carbonate (Carbonic acid) | ligand_10096 | Inorganic oxyanion | pKa1 = 6.13, pKa2 = 9.91 | CO3 oxyanion family |

Interpretation and hypothesis
- Within a given donor family (e.g., monocarboxylates or closely related dicarboxylates), higher pKa of the coordinating group(s) generally implies stronger basicity and hence stronger Ca2+ binding (higher log β), because Ca2+ is a hard cation that favors deprotonated oxygen donors.
- However, pKa alone does not set binding strength across different ligand classes. Denticity (number of donor atoms), charge, and preorganization produce large upward shifts in stability constants. For example, aminopolycarboxylates (EDTA/EGTA) have multiple deprotonation steps and high denticity, which typically lead to much larger Ca2+ log β values than simple mono‑ or di‑carboxylates, independent of modest pKa differences.
- In inorganic oxyanions, higher pKa2 (e.g., HPO4^2− at pKa2 ≈ 6.71) indicates substantial deprotonation near neutral pH, favoring Ca–O binding. Bicarbonate (HCO3−, pKa1 ≈ 6.13) is also deprotonated near neutral pH, but geometric and charge distribution differences likely make phosphate competitive or stronger within comparable conditions.

Testable statement for alkaline‑earth metals
- At fixed ligand framework and denticity, Ca2+ stability constants increase with the ligand basicity (higher pKa of the coordinating group), yielding a positive within‑class correlation between pKa and log β.
- Across the Mg2+ → Ca2+ → Sr2+ → Ba2+ series, absolute binding often increases with ionic radius for oxygen donors due to lower hydration penalties and larger coordination numbers, but size matching and ligand preorganization can create selectivity peaks (e.g., Ca2+ preference in EGTA‑like ligands). Thus, pKa is a good predictor within a class; denticity/geometry/charge control cross‑class comparisons.

What remains to quantify (next step)
- Retrieve Ca2+ stability constants (log βn) at 25 °C and controlled ionic strength for the ligands listed above and pair them with the pKa values already extracted. Plot log β versus the relevant pKa within each ligand family (mono‑, di‑, tri‑carboxylates; aminopolycarboxylates; oxyanions) to measure slopes and goodness‑of‑fit. This will confirm or refine the positive correlation hypothesis and highlight denticity‑driven offsets.

Source: NIST Standard Reference Database 46 (SRD‑46): Critical Stability Constants of Metal Complexes (ligand pKa and Ca2+ complexation literature records).

---