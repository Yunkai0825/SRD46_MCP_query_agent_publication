# Qfree_20260424_005101 -- Result (batch 1)

**Section:** freeform -- Fe(III)/Fe(II) ligand selection (corrected)

**Prompt:** I would like to find ligands that can complex Fe(III) to stabilize the acidic solution (pH<5), yet with limited complexation to Fe(II) so that it does not decrease the free Fe2+ concentration too much. This is for Fe electrodeposition since we also try to minimize the hydrogen evolution reaction when Fe electrodeposition happens. The expected concentration of Fe(II) is ~0.1M. Meanwhile, be cautious about ligand pH and its actual state, and be cautious about possible precipitations. If there are missing entries, try to observe similar metal-ligand systems with available data to estimate those with very robust reasons and explanations. You have unlimited time and unlimited turns.

**Tool calls:** 34  |  **Time:** 47s planning + 478s execution + 0s verdict = 525s total

---

Using SRD-46, the safest **direct-data shortlist** for your goal is:

| Tier | Ligand | SRD-46-based take for pH < 5 Fe bath |
|---|---|---|
| 1 | **Citrate** (`ligand_9058`) | Best overall practical balance found: **Fe(III) data present** and **Fe(II) data present**, with weaker/less aggressive behavior than EDTA/NTA-class chelators. Still substantially protonated at low pH, so use **modest dosage** only. |
| 2 | **5-Sulfosalicylate** (`ligand_9284`) | Promising **mild Fe(III)-leaning** acidic/water-compatible ligand with very limited Fe(II) coverage in SRD-46; likely safer than aminocarboxylates, but evidence is thinner. |
| 3 | **Salicylate** (`ligand_9257`) | Similar logic to 5-SSA but less ideal for solubility and low-pH reliability. Secondary option only. |
| 4 | **Acetate** (`ligand_8465`) | Weakest and safest for preserving free Fe²⁺, but probably **too weak** to meaningfully stabilize Fe(III) in strongly acidic media. Best as a baseline/comparator, not the main fix. |

**Deprioritize / avoid** for Fe electrodeposition baths aiming to keep free Fe²⁺ high:

| Ligand | Why |
|---|---|
| **EDTA (`ligand_6277`)** | Very strong, nonselective; likely captures Fe(II) too much. |
| **NTA (`ligand_6165`)** | Strong Fe(III) chelator but still appreciable Fe(II) binding. |
| **HEDTA (`ligand_6275`)** | Same concern as NTA/EDTA. |
| **IDA (`ligand_6127`)** | Weaker than NTA/EDTA but still not especially attractive in acid. |
| **2,6-PDPA (`ligand_8434`)** | Explicitly risky: strong Fe(II) network data, likely too much Fe²⁺ sequestration. |
| **Oxalate (`ligand_8872`)** | Binds both oxidation states and has precipitation risk. |
| **Tiron (`ligand_9358`)** | Very strong Fe(III), redox-active catechol chemistry; risky for plating bath behavior. |
| **SCN⁻ / HSCN (`ligand_10092`)** | Complicated speciation/side chemistry; not a clean selective stabilizer. |

### Key pKa/speciation cautions from SRD-46
| Ligand | pKa data noted from SRD-46 card | Low-pH implication |
|---|---:|---|
| Citrate | 2.90, 4.35, 5.65 | At pH 2–5 it is only partly deprotonated, so real binding is much weaker than raw logK suggests. |
| Acetate | 4.56 | Mostly protonated below ~4.5, so weak Fe binding. |
| 5-Sulfosalicylate | ~2.48, ~11.85 | Carboxylate available more than phenolate at pH < 5; Fe binding likely moderate, not extreme. |
| Salicylate | ~2.8 | Mainly monoanionic below pH 5; phenol mostly protonated, so limited chelation strength in strong acid. |
| Oxalate | ~−1.2, 3.8 | Active in acid, but also risky for Fe(II) binding and precipitation. |
| NTA | −1.81, −1.00, 2.52, 9.46 | Still protonated below pH 5, but once partly deprotonated can bind Fe strongly. |
| IDA | ~−1.77, 2.62, 9.34 | Similar caution. |
| HEDTA | ~2.62, 5.38, 9.70 | Still protonated in acid, but not Fe(II)-sparing enough. |
| EDTA | ~−1.5, 2.0, 2.69, 6.13, 9.52 | Strong even when protonated; too aggressive. |
| 2,6-PDPA | ~3.14, 4.67, 9.12 | Donor availability persists better in acid, but Fe(II) binding is too strong. |

### What the Fe coverage in SRD-46 supports
| Observation | SRD-46 evidence |
|---|---|
| Fe is encoded as **Fe^[3+]** and **Fe^[2+]** | `db_distribution` on `ligandmetal_card`: **1473 Fe^[3+]** rows, **667 Fe^[2+]** rows |
| Candidate pool is real but unevenly covered | `search_stability` returned pairs for citrate, acetate, salicylate, 5-SSA, oxalate, NTA, IDA, HEDTA, EDTA, 2,6-PDPA, thiocyanate |
| Direct Fe(II) concern is strongest for 2,6-PDPA and aminocarboxylates | Fe(II) networks/stability present for **2,6-PDPA, NTA, IDA, HEDTA, EDTA** |
| Mild ligands have thinner but more attractive profiles | Fe(III) records exist for **citrate, salicylate, 5-SSA, acetate** with less alarming Fe(II) coverage |

### My practical recommendation
| Priority | Recommendation |
|---|---|
| Best first experiment | **Citrate at substoichiometric concentration relative to total Fe impurities/Fe(III)** |
| Best lower-risk alternative | **5-Sulfosalicylate**, if you need more Fe(III) stabilization than acetate but less Fe(II) capture than EDTA/NTA-class ligands |
| Baseline control | **Acetate-only** bath as weak-ligand reference |
| Avoid as primary bath ligands | **EDTA, NTA, HEDTA, 2,6-PDPA, oxalate** |

### Chemistry interpretation
| Point | Meaning for your bath |
|---|---|
| Raw Fe(III) logK is not enough | At pH < 5, proton competition strongly reduces effective ligand availability. |
| Fe(III) stabilization vs Fe(II) sparing is a narrow window | Most ligands strong enough to hold Fe(III) also begin to tie up Fe(II). |
| Local cathode pH still matters | Even if bulk pH is <5, HER can raise interfacial pH and trigger Fe hydrolysis/precipitation; ligand helps but does not eliminate this. |

### Bottom line
If I stay strict to SRD-46 evidence, **citrate is the best-supported practical compromise**, with **5-sulfosalicylate** as the most interesting thinner-data alternative and **acetate** as the safest weak-binding baseline. **Do not start with EDTA/NTA/HEDTA/2,6-PDPA/oxalate** if your priority is preserving about **0.1 M free Fe²⁺** for deposition.

**Source:** NIST SRD-46.
