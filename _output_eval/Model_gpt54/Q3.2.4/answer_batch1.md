## Fe(II) vs Fe(III) ligand-system survey from SRD-46

SRD-46 shows a clear oxidation-state split:

| Metal | SRD-46 system ID | Ligands represented | VLM entries | Overall coverage pattern |
|---|---:|---:|---:|---|
| Fe(III) | `metal_61` | 406 | 1473 | Strongly weighted toward hard O-donor and multidentate chelators |
| Fe(II) | `metal_62` | 217 | 667 | More mixed O/N-donor coverage; aromatic N-heterocycles appear more prominently |

## Coverage by ligand class

### Fe(III)
| Ligand-class coverage highlights | Approx. share of Fe(III) entries |
|---|---:|
| Inorganic ligands | 13% |
| Catechols | 9.5% |
| Hydroxamic acids | 8.4% |
| Amino acids | 7.9% |
| EDTA-like ligands | 7.2% |
| Aliphatic amines | 6.9% |
| Salicylate / phenol-carboxylates | 6.7% |
| Phenols | 4.6% |
| Simple carboxylates | 4.1% |
| Pyridines | 3.3% |
| NTA-like ligands | 3.1% |

### Fe(II)
| Ligand-class coverage highlights | Approx. share of Fe(II) entries |
|---|---:|
| Amino acids | 15% |
| EDTA-type aminopolycarboxylates | 12% |
| Inorganic ligands | 11% |
| Phenanthrolines | 3–5% |
| Aminophosphorus acids | 3–5% |
| Bipyridines | 3–5% |
| NTA-type ligands | 3–5% |
| Pyridines / pyridine-carboxylates | 3–5% |
| Polycarboxylates / IDA-type ligands | 3–5% |
| Aza/aza-oxa macrocycles, azoles, tripyridines, catechols, aliphatic amines | ~2–3% |

## Database-backed trend in stability ordering

The catalog summary and top-ranked retrieved systems support this broad ordering.

### Fe(III): strongest to weakest classes
| Approximate class ordering in SRD-46 | Interpretation |
|---|---|
| Multidentate hard O-donors: EDTA/CDTA/NTA, hydroxamates, Tiron-like systems | Strongest overall |
| Chelating aromatic O or O,N donors: oxine, salicylate-type ligands | Very strong, but generally below the best aminopolycarboxylates / hydroxamates |
| Small dicarboxylates: oxalate, malonate | Intermediate |
| Simple monocarboxylates: acetate and homologs | Lower |
| Fluoride | Strong among simple inorganic ligands |
| Thiocyanate, azide | Weak-to-moderate |
| Chloride | Weakest of the highlighted simple anions |

### Fe(II): strongest to weakest classes
| Approximate class ordering in SRD-46 | Interpretation |
|---|---|
| Multidentate aminopolycarboxylates and related chelators (EDTA-family, DTPA-like, CDTA-like) | Strongest among retrieved Fe(II) systems |
| Multidentate polyamines / aza-ligands / pyridyl-appended chelators | Strong |
| Aromatic N-heterocycles (phenanthroline, bipyridine families) | Prominent and often strong for Fe(II) |
| Amino acids and mixed O,N donors | Moderate |
| Simple inorganic ligands and weaker monodentates | Lower |
| Sparse S-donor entries exist, but coverage is too limited for a class-wide ranking | Edge-case territory |

## Representative systems actually retrieved

These are the named ligands returned directly by SRD-46 searches for each oxidation state.

### Fe(III) representatives
| Ligand | Class signal from SRD-46 context | Notes from retrieved records |
|---|---|---|
| EDTA (`ligand_6277`) | aminopolycarboxylate | 25 °C, I = 0.1 M |
| NTA (`ligand_6165`) | aminopolycarboxylate | 25 °C, I = 0.1 M |
| Oxalic acid (`ligand_8872`) | dicarboxylate | 25 °C |
| Malonic acid (`ligand_8873`) | dicarboxylate | 25 °C |
| Acetic acid (`ligand_8465`) and other monocarboxylates | simple carboxylates | 25 °C, often I = 1 M |
| HF / fluoride (`ligand_10162`) | inorganic hard donor | 25 °C, I = 0.5 M |
| Salicylaldehyde (`ligand_9300`) | aromatic O-donor / salicylate-type motif | 25 °C |
| Hydroxide (`ligand_10076`) | hydroxo chemistry present | important caveat: hydrolysis competes strongly for Fe(III) |

### Fe(II) representatives
| Ligand | Class signal from SRD-46 context | Notes from retrieved records |
|---|---|---|
| EDTA (`ligand_6277`) | aminopolycarboxylate | 25 °C, I = 0.1 M |
| trans-1,2-cyclohexylenediaminetetraacetic acid (`ligand_6301`) | rigid aminopolycarboxylate | 25 °C, I = 0.1 M |
| DTPA-like ligand (`ligand_6356`) | higher-denticity aminopolycarboxylate | 25 °C, I = 0.1 M |
| Polyamines such as tren / trien-like systems (`ligand_7345`, `ligand_7244`, `ligand_7224`) | aliphatic polyamines | 25 °C, I = 0.1 M |
| Pyridyl-appended amines (`ligand_8205`, `ligand_8174`, `ligand_8209`) | multidentate aromatic N-donors | 25 °C, I = 0.1 M |
| Histidine (`ligand_5898`) | amino acid / imidazole donor | 25 °C, I = 3 M |
| 5-methyl-1,10-phenanthroline (`ligand_8193`) | aromatic N-heterocycle | listed as logK entry |
| Cyanide (`ligand_10090`) | strong-field C/N donor | listed as logK entry |

## Overall trend

The simplest summary is:

| Trend | What SRD-46 suggests |
|---|---|
| Fe(III) prefers | hard, highly charged, deprotonated O-donor ligands, especially multidentate ones |
| Fe(II) prefers | still benefits from chelation, but shows relatively stronger representation and competitiveness for N-donor ligands, especially aromatic N-heterocycles and polyamines |
| For both ions | denticity and preorganization strongly raise stability |
| Biggest oxidation-state contrast | Fe(III) is much more dominated by hard O-donor chemistry than Fe(II) |

## Thermodynamic reasoning behind the ordering

### 1. HSAB: Fe(III) is harder than Fe(II)
| Ion | HSAB character | Consequence |
|---|---|---|
| Fe(III) | harder, higher charge density | Strong preference for hard bases: carboxylate O, phenolate O, hydroxamate O, fluoride |
| Fe(II) | less hard / more borderline | Better relative compatibility with N donors such as bipyridine, phenanthroline, pyridines, polyamines |

This explains why Fe(III) is so enriched in catechols, hydroxamates, salicylates, EDTA/NTA-type O-rich ligands, and why fluoride outranks chloride among simple inorganic ligands.

### 2. Chelate effect and macro/preorganization effects
| Ligand type | Effect on stability |
|---|---|
| Monodentate carboxylates | modest stability |
| Dicarboxylates | stronger due to chelation |
| Aminopolycarboxylates (NTA, EDTA, CDTA, DTPA-like) | much stronger because of multidentate binding and favorable entropy |
| Rigid / preorganized ligands | often stronger still because less conformational penalty is paid on binding |

This is one of the clearest trends in the database: simple acetate-type ligands are much weaker than oxalate/malonate, which are in turn weaker than EDTA-family ligands.

### 3. Crystal-field / ligand-field effects
| Ion | d count | Ligand-field implication |
|---|---:|---|
| Fe(III) | high-spin d5 in many aqueous complexes | CFSE contribution is modest, so electrostatics + desolvation + chelation dominate |
| Fe(II) | d6 | ligand-field stabilization can matter more, especially with stronger-field N donors |

That helps explain why Fe(II) is comparatively competitive with phenanthroline/bipyridine-type ligands: beyond chelation, these ligands can give favorable ligand-field stabilization and sometimes low-spin character, boosting stability.

### 4. Solvation/desolvation
| Feature | Thermodynamic consequence |
|---|---|
| Fe(III) is more strongly hydrated | A ligand must compensate a larger desolvation penalty |
| Highly charged, hard, multidentate O-donors | best able to pay that penalty |
| Weak soft/neutral monodentates | often cannot compete well with Fe(III) hydration |

This is why Fe(III) especially rewards strongly anionic, multidentate oxygen donors.

## Edge cases and why they happen

| Edge case | Explanation |
|---|---|
| Fluoride stronger than chloride for Fe(III) | Classic HSAB: F⁻ is hard, compact, and much better matched to Fe(III) than Cl⁻ |
| Oxine / salicylate-type ligands stronger than simple monodentates | Chelation and partial preorganization overcome the fact that they are not the hardest pure O-donor systems |
| Aromatic N-donors appear especially important for Fe(II) | Fe(II) is more borderline and gains more from ligand-field stabilization with phenanthroline/bipyridine-type ligands |
| Sparse S-donor data | Coverage is limited, so class-wide conclusions are weak; but in general Fe(III) should disfavor soft S donors more than Fe(II) does |
| Hydroxo chemistry for Fe(III) | Fe(III) hydrolyzes strongly; apparent stability patterns can be distorted if hydrolysis/speciation is not separated from simple ML binding |

## Bottom-line ordering

| Metal | Practical class ordering inferred from SRD-46 |
|---|---|
| Fe(III) | hydroxamates / catecholates / EDTA-family hard multidentate O-donors > salicylate/oxine-type chelators > dicarboxylates > simple carboxylates > F⁻ > SCN⁻/N₃⁻ > Cl⁻ |
| Fe(II) | high-denticity aminopolycarboxylates and polyamines ≳ strong aromatic N-heterocycle chelators > amino-acid and mixed O,N ligands > weaker inorganic/monodentate ligands |

## Interpretation in one sentence

Fe(III) stability is governed mainly by **hard-acid preference plus strong gains from anionic O-donor chelation**, whereas Fe(II) shows a **more balanced competition between chelation and ligand-field stabilization**, allowing **N-donor aromatic chelators** to become much more competitive.

Source: **NIST SRD-46**.

---