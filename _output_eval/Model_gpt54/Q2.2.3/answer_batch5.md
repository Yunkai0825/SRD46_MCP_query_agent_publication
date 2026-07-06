Yes. Using SRD-46 pKa records, there are ligands with more than 6 reported pKa values.

| ligand_id | ligand_name | reported pKa steps | total pKa rows |
|---|---|---:|---:|
| ligand_7541 | 1,4,7,10,13,16,19,22,25,28,31,34-Dodecaazacyclohexatriacontane ([36]aneN12) | 11 | 11 |
| ligand_7540 | 1,4,7,10,13,16,19,22,25,28,31-Undecaazacyclotritriacontane ([33]aneN11) | 11 | 11 |
| ligand_7539 | 1,4,7,10,13,16,19,22,25,28-Decaazacyclotriacontane ([30]aneN10) | 10 | 10 |
| ligand_7253 | 2,5,8,11,14,17,20,23,26,29-Decaazatriacontane (Me2nonaen) | 10 | 10 |
| ligand_6368 | Pentaethylenehexanitrilooctaacetic acid (PHOA) | 10 | 10 |
| ligand_7538 | 1,4,7,10,13,16,19,22,25-Nonaazacycloheptacosane ([27]aneN9) | 9 | 9 |
| ligand_7252 | 2,5,8,11,14,17,20,23,26-Nonaazaheptacosane (Me2octaen) | 9 | 9 |
| ligand_6367 | Tetraethylenepentanitriloheptaacetic acid (TPHA) | 9 | 9 |
| ligand_7254 | 1,3-Bis(2,5,8,11-tetraazaundecyl)benzene (MXTRIEN) | 8 | 8 |
| ligand_7534 | 1,4,7,10,13,16,19,22-Octaazacyclotetracosane ([24]aneN8) | 8 | 8 |
| ligand_7535 | 1,5,9,13,17,21,25,32-Octaazacyclodotriacontane ([32]aneN8) | 8 | 8 |
| ligand_7543 | 1,5,9,13,17,21,28,32-Octaazabicyclo[11.11.11]pentatriacontane | 8 | 8 |
| ligand_7251 | 2,5,8,11,14,17,20,23-Octaazatetracosane (Me2heptaen) | 8 | 8 |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | 8 | 8 |
| ligand_8433 | Diethylenetrinitrilopentakis(methylenephosphonic acid) (DTPP) | 8 | 8 |
| ligand_6047 | N,N''-Bis(3-hydroxy-6-methyl-2-pyridinylmethyl)diethylenetrinitrilotriacetic acid... | 8 | 8 |
| ligand_6041 | N,N'-Bis(3-hydroxy-5-phosphomethyl-2-methyl-4-pyridylmethyl)ethylenedinitrilodi... | 8 | 8 |
| ligand_8431 | Oxybis[ethylenenitrilobis(methylenephosphonic acid)] | 8 | 8 |
| ligand_6366 | Triethylenetetranitrilohexaacetic acid (TTHA) | 8 | 8 |
| ligand_9171 | myo-Inositol-hexa(dihydrogenphosphate) (Phytic acid) | 8 | 8 |
| ligand_8432 | (2-Hydroxytrimethylene)dinitrilotetrakis(methylenephosphonic acid) | 7 | 7 |
| ligand_7649 | 1,4,16,19-Tetraoxa-7,10,13,22,25,28,31-heptaazacyclotritriacotane ([33]aneN7O4) | 7 | 7 |
| ligand_7530 | 1,4,7,10,13,16,19-Heptaazacycloheneicosane ([21]aneN7) | 7 | 7 |
| ligand_8403 | 1,4,7,10-Tetraazacyclododecane-1,4,7,10-tetrakis(methylenephosphonic acid) (DOT...) | 7 | 7 |
| ligand_7422 | 1,4,7-Tris(3-hydroxy-6-methyl-2-pyridylmethyl)-1,4,7-triazacyclononane | 7 | 7 |

The SQL result reported **33 ligands total** with more than 6 distinct pKa steps; the tool output exposed **25 rows explicitly** and noted **8 additional rows omitted**.

A clear chemistry pattern is that the hits are mostly **highly polybasic polyamines** and **highly polyacidic aminopolycarboxylate/phosphonate ligands**, which is exactly what you’d expect: more protonatable/deprotonatable sites usually means more stepwise pKa values can be measured and tabulated.

Source: **NIST SRD-46** pKa tables (`ligand_pka_measured` joined to `ligand_card`).

---