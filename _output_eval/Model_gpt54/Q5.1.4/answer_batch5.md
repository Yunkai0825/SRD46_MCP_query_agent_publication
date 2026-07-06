SRD-46 has substantial **Zn²⁺** coverage.

| Metric | Zn²⁺ coverage |
|---|---:|
| Metal ID | `metal_208` |
| Distinct β-definition entries | 122 |
| Distinct ligands linked to Zn²⁺ | 1169 |
| Value/measurement rows | 4095 |
| Zn²⁺–ligand pairs in built catalog | 20 |
| Distinct species in catalog | 94 |

### Main Zn²⁺ ligand systems present
| Ligand/system | Notes from SRD-46 |
|---|---|
| Glycine | 37 entries; species include `ML`, `ML2`, `ML3`, hydroxo form |
| Ethylenediamine | 36 entries; stepwise `ML`, `ML2`, `ML3` |
| Hydroxide | 33 entries; soluble hydroxo species plus multinuclear and solid Zn(OH)₂ / ZnO-type forms |
| HCN / CN⁻ | 30 entries; `ML` to `ML4` plus solid cyanide-related form |
| Imidazole | 30 entries; `ML` to `ML4` |
| Histidine | 29 entries; protonated, `ML`, `ML2`, hydroxo species |
| Cysteine | sulfur-donor system with protonated and multinuclear complexes |
| Penicillamine | sulfur-donor system with protonated and multinuclear complexes |
| Ammonia | stepwise ammine complexes |
| IDA / HIDA / EDTA / citrate / NTP | chelator systems with protonated and/or hydroxo forms |
| 1,10-Phenanthroline / 2,2'-bipyridyl | aromatic N-donor complexes |
| Alanine / acetate / propylenediamine | additional amino acid / amine systems |

### Species types represented
| Category | Examples in Zn²⁺ data |
|---|---|
| Simple complexes | `ML`, `ML2`, `ML3`, `ML4` |
| Protonated complexes | `MHL`, `MH2L`, `MHL2` |
| Hydroxo complexes | `M(OH)L`, `M(OH)L2`, `M(OH)2L` |
| Multinuclear species | `M2L`, `M2(OH)L` and related forms |
| Solids | Zn hydroxide / oxide-type and cyanide-related solid definitions |

### Condition coverage
| Condition | Coverage seen in catalog/network summaries |
|---|---|
| Temperature | about **5–45 °C** overall |
| Ionic strength | about **-0.15 to 5.15 M** overall |
| Common reference-network region | often near **20–25 °C** and **low ionic strength** |

### Example Zn²⁺ equilibrium-network data found
| Zn²⁺ + ligand | Max nodes | T range (°C) | I range (M) | Example logK range |
|---|---:|---|---|---|
| Glycine (`ligand_5760`) | 4 | 31–41 | 0–0.3 | 4.87–11.3 |
| Macrocycle `ligand_7653` | 6 | 20–30 | -0.05–0.25 | 3.8–11 |
| Macrocycle `ligand_7654` | 6 | 20–30 | -0.05–0.25 | 3.9–9.7 |
| Macrocycle `ligand_7655` | 2 | 20–30 | -0.05–0.25 | 6.6–6.8 |

### Example species in one Zn²⁺ network
| β definition | Reaction | logK |
|---|---|---:|
| `beta_def_812` | `[M] + [L] <=> [ML]` | 8.89 |
| `beta_def_788` | `[ML] + [H] <=> [MHL]` | 7.45 |
| `beta_def_839` | `[M(OH)L] + [H] <=> [ML] + [H2O]` | 9.52 |
| `beta_def_975` | `[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]` | 11 |
| `beta_def_516` | `[ML] + [M] <=> [M2L]` | 3.8 |
| `beta_def_515` | `[M2(OH)L] + [H] <=> [M2L] + [H2O]` | 7.07 |

Zn²⁺ in SRD-46 is therefore covered across **amino acids, amines, N-donor aromatics, sulfur ligands, cyanide, hydroxide, and strong chelators**, with data spanning **simple, protonated, hydrolyzed, multinuclear, and solid** species. Chemically, that fits Zn²⁺’s broad borderline-Lewis-acid behavior: it binds well to **N/O donors**, but the database also captures especially interesting **S-donor** and **hydrolysis** chemistry.

If you want, I can next give you either:
| Option | What I can pull |
|---|---|
| Top Zn ligands | most data-rich Zn systems |
| Specific ligand | all Zn²⁺ constants for, say, EDTA, glycine, ammonia, histidine, cyanide, etc. |
| Hydrolysis only | Zn–OH species and solid phases |
| pKa context | ligand pKa data for Zn-relevant ligands |

*Source: NIST SRD-46*

---