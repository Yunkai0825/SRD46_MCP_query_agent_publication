Yes. Aggregating the SRD‑46 pKa table by ligand shows 33 ligands with more than 6 reported pKa entries (across all studies and conditions). Below are the ones visible in the retrieved page of results, with their per‑ligand entry counts.

| Ligand ID | Ligand name (SRD) | pKa entries (>6) |
|-----------|--------------------|------------------|
| ligand_7541 | 1,4,7,10,13,16,19,22,25,28,31,34-Dodecaazacyclohexatriacontane ([36]aneN12) | 11 |
| ligand_7540 | 1,4,7,10,13,16,19,22,25,28,31-Undecaazacyclotritriacontane ([33]aneN11) | 11 |
| ligand_7539 | 1,4,7,10,13,16,19,22,25,28-Decaazacyclotriacontane ([30]aneN10) | 10 |
| ligand_7253 | 2,5,8,11,14,17,20,23,26,29-Decaazatriacontane (Me2nonaen) | 10 |
| ligand_6368 | Pentaethylenehexanitrilooctaacetic acid (PHOA) | 10 |
| ligand_7538 | 1,4,7,10,13,16,19,22,25-Nonaazacycloheptacosane ([27]aneN9) | 9 |
| ligand_7252 | 2,5,8,11,14,17,20,23,26-Nonaazaheptacosane (Me2octaen) | 9 |
| ligand_6367 | Tetraethylenepentanitriloheptaacetic acid (TPHA) | 9 |
| ligand_7254 | 1,3-Bis(2,5,8,11-tetraazaundecyl)benzene (MXTRIEN) | 8 |
| ligand_7534 | 1,4,7,10,13,16,19,22-Octaazacyclotetracosane ([24]aneN8) | 8 |
| ligand_7535 | 1,5,9,13,17,21,25,32-Octaazacyclodotriacontane ([32]aneN8) | 8 |
| ligand_7543 | 1,5,9,13,17,21,28,32-Octaazabicyclo[11.11.11]pentatriacontane | 8 |
| ligand_7251 | 2,5,8,11,14,17,20,23-Octaazatetracosane (Me2heptaen) | 8 |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | 8 |
| ligand_8433 | Diethylenetrinitrilopentakis(methylenephosphonic acid) (DTPP) | 8 |
| ligand_6047 | N,N''-Bis(3-hydroxy-6-methyl-2-pyridinylmethyl)diethylenetrinitrilotriacetic ac... | 8 |
| ligand_6041 | N,N'-Bis(3-hydroxy-5-phosphomethyl-2-methyl-4-pyridylmethyl)ethylenedinitrilodi... | 8 |
| ligand_8431 | Oxybis[ethylenenitrilobis(methylenephosphonic acid)] | 8 |
| ligand_6366 | Triethylenetetranitrilohexaacetic acid (TTHA) | 8 |
| ligand_9171 | myo-Inositol-hexa(dihydrogenphosphate) (Phytic acid) | 8 |
| ligand_8432 | (2-Hydroxytrimethylene)dinitrilotetrakis(methylenephosphonic acid) | 7 |
| ligand_7649 | 1,4,16,19-Tetraoxa-7,10,13,22,25,28,31-heptaazacyclotritriacotane ([33]aneN7O4) | 7 |
| ligand_7530 | 1,4,7,10,13,16,19-Heptaazacycloheneicosane ([21]aneN7) | 7 |
| ligand_8403 | 1,4,7,10-Tetraazacyclododecane-1,4,7,10-tetrakis(methylenephosphonic acid) (DOT...) | 7 |
| ligand_7422 | 1,4,7-Tris(3-hydroxy-6-methyl-2-pyridylmethyl)-1,4,7-triazacyclononane | 7 |

Notes:
- This count reflects the number of reported pKa entries in SRD‑46 for each ligand (i.e., across studies and conditions), not the number of distinct stepwise protonation constants. If you want only unique steps per ligand, we can deduplicate by pKa_type in a follow‑up.
- The full query returned 33 ligands; 8 additional ligands (not shown above due to output truncation) also exceed 6 pKa entries.

Chemistry insight: The list is dominated by highly polyfunctional ligands—macrocyclic polyamines (e.g., [24]aneN8 to [36]aneN12), polyaminopolycarboxylates (TTHA, PHOA, TPHA, DTPA), and polyphosphonates (e.g., DTPP). Their many donor sites give rise to numerous protonation steps and extensive literature, hence high pKa entry counts.

Source: NIST Standard Reference Database 46 (IUPAC Stability Constants Database), aggregate over ligand_pka_measured joined to ligand_card (GROUP BY ligand_id; HAVING COUNT(*) > 6).

---