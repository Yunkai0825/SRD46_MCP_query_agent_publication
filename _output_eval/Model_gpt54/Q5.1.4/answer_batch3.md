SRD-46 has **substantial Zn(II) coverage**.

| Item | Zinc entry in SRD-46 |
|---|---|
| Metal ID | `metal_208` |
| Species | Zn²⁺ (`Zn^[2+]`) |
| Formula representation | simple ion |
| SMILES | `[Zn+2]` |
| InChI | `InChI=1S/Zn/q+2` |
| Distinct ligands linked | 1169 |
| Total measurements linked | 4095 |
| Beta-definition count | 122 |

Here’s the broad picture from the zinc card and stability survey:

| Data type | What is present for Zn(II) |
|---|---|
| Stability constants | Extensive `logK` data across many ligand classes |
| Thermodynamics | `ΔH` data for at least 20 Zn–ligand systems; `ΔS` data for at least 1 system in the sampled results |
| Ligand scope | Amino acids, iminodiacetates, nitrilotriacetates, polyaminocarboxylates, pyridinedicarboxylates, cyanide, phosphonates, catecholamine-like ligands, and more |
| Experimental conditions seen in sample | Mostly around **20 °C**, often **I = 0.1 M**, with some entries at **0, 0.5, 1, and 2 M** |
| Non-aqueous coverage | Present/flagged in the returned survey output, though I have not yet broken it down quantitatively |

Examples of Zn(II) ligand systems visible in the retrieved sample:

| Ligand ID | Ligand name | Data seen |
|---|---|---|
| `ligand_5760` | Glycine | `logK`, `ΔH` |
| `ligand_6127` | Iminodiacetic acid (IDA) | `ΔH` |
| `ligand_6165` | Nitrilotriacetic acid (NTA) | `ΔH` |
| `ligand_6277` | EDTA | `ΔH` |
| `ligand_6774` | Pyridine-2,6-dicarboxylic acid | `logK` |
| `ligand_10090` | Hydrogen cyanide / cyanide system | `logK`, `ΔH` |
| `ligand_9142` | 1-Hydroxyethane-1,1-diphosphonic acid | `ΔH` |

A few takeaways:

| Observation | Evidence from retrieved data |
|---|---|
| Zn(II) is one of the more broadly covered metals in the database | 1169 ligands and 4095 measurements |
| The dataset strongly features classic O/N donor chelators | Many iminodiacetate, nitrilotriacetate, and aminocarboxylate ligands appear in the sample |
| Conditions are often fairly standardized | Many returned Zn entries cluster near **20 °C** and **0.1 M ionic strength** |

If you want, I can next drill into one of these directions:

| Option | What I can show |
|---|---|
| Top Zn ligands | Most frequently studied zinc-binding ligands |
| Representative constants | Actual Zn `log β` values for glycine, IDA, NTA, EDTA, cyanide, etc. |
| Hydrolysis/speciation | Zinc hydroxo/chloro/speciation networks |
| Citations | Main literature sources behind the Zn data |

Source: **NIST SRD-46**.

---