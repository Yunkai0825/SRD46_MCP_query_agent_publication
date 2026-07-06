SRD-46 shows **two main inorganic mercury entries** with complexation data:

| Mercury form | SRD-46 ID | Coverage |
|---|---:|---:|
| Hg²⁺ | `metal_71` | 68 β definitions, 310 ligands, 1097 VLM entries |
| Hg⁺ | `metal_72` | 12 β definitions, 31 ligands, 83 VLM entries |

So the database is **much richer for Hg(II)** than for Hg(I). Hg(I) chemistry is present, but it is relatively sparse in SRD-46 compared with Hg(II). Source: **NIST SRD-46**.

## What kinds of mercury complexes show up?
For **Hg²⁺**, the retrieved network and stability data show a lot of emphasis on:
- **amino-acid / amino-carboxylate ligands**
- **macrocyclic ligands**
- equilibrium maps with multiple stoichiometries and protonation states

For **Hg⁺**, the retrieved systems are fewer and skew toward:
- **hydroxide**
- **oxo/phosphate-type ligands**
- **simple carboxylates**
- a few specialized macrocycles

## Representative Hg²⁺ systems found
From the retrieved Hg²⁺ stability entries:

| Ligand | Ligand ID | Constant type present | T (°C) | I (M) | Notes |
|---|---:|---|---:|---:|---|
| Aminoacetic acid (glycine) | `ligand_5760` | logK, ΔH, ΔS | 20–25 | 0–0.5 | 4 VLM, 4 β definitions |
| 3-Aminopropanoic acid (β-alanine) | `ligand_5788` | logK | 25 | 0.5 | 1 VLM |
| cis-2-Aminocyclopentane-1-carboxylic acid | `ligand_5790` | logK | 25 | 0.5 | 1 VLM |
| cis-2-Aminocyclohexane-1-carboxylic acid | `ligand_5792` | logK | 25 | 0.5 | 1 VLM |
| trans-2-Aminocyclohexane-1-carboxylic acid | `ligand_5793` | logK | 25 | 0.5 | 1 VLM |
| cis-2-Amino-4-cyclohexene-1-carboxylic acid | `ligand_5794` | logK | 25 | 0.5 | 1 VLM |
| trans-2-Amino-4-cyclohexene-1-carboxylic acid | `ligand_5795` | logK | 25 | 0.5 | 1 VLM |
| L-2-Amino-5-ureidopentanoic acid (citrulline) | `ligand_5852` | logK | 25 | 0.1 | 2 VLM |
| Tetramethyl macrocycle | `ligand_7655` | logK | 25 | 0.1 | 2 VLM |

## Representative Hg²⁺ logK values actually retrieved
The equilibrium-network output gave explicit Hg²⁺ logK ranges for several systems:

| Ligand | Network / definition context | Retrieved logK range |
|---|---|---:|
| Glycine | chloride-containing and ML₂-related network | 3.42–6.03 |
| Tetramethyl macrocycle (`ligand_7655`) | ML / MHL network | 4.2–26.1 |
| Citrulline | ML / ML₂ network | -10.95 to -6.02 |
| β-Alanine | single-node ML | 11.31 |
| cis-2-Aminocyclopentane-1-carboxylic acid | single-node ML | 11.17 |
| cis-2-Aminocyclohexane-1-carboxylic acid | single-node ML | 11.46 |
| trans-2-Aminocyclohexane-1-carboxylic acid | single-node ML | 11.29 |
| cis-2-Amino-4-cyclohexene-1-carboxylic acid | single-node ML | 15.9 |
| trans-2-Amino-4-cyclohexene-1-carboxylic acid | single-node ML | 25.18 |

## Representative Hg⁺ systems found
From the retrieved Hg⁺ stability search:

| Ligand | Ligand ID | Constant type present | T (°C) | I (M) |
|---|---:|---|---:|---:|
| Hydroxide ion | `ligand_10076` | logK | 25 | 0.5–3 |
| Hydrogen diphosphate (pyrophosphate-related entry) | `ligand_10114` | logK | 27 | 0.7 |
| Hydrogen triphosphate | `ligand_10117` | logK | 27 | 0.7 |
| Propane-2,2-dicarboxylic acid | `ligand_8887` | logK | 27 | 0.7 |
| Butanedioic acid (succinic acid) | `ligand_8907` | logK | 27 | 2.5 |
| Ethanedioic acid (oxalic acid) | `ligand_8872` | logK | 27 | 2.5 |
| Propanoic acid | `ligand_8467` | logK | 25 | 3 |
| Ethanoic acid (acetic acid) | `ligand_8465` | logK | 25 | 3 |
| Hydroxyacetic acid (glycolic acid) | `ligand_8640` | logK | 25 | 3 |
| Methanoic acid (formic acid) | `ligand_8464` | logK | 25 | 3 |
| Methoxyacetic acid | `ligand_8721` | logK | 25 | 3 |
| 3-Methoxypropanoic acid | `ligand_8724` | logK | 25 | 3 |

There are also **ΔH** and **ΔS** entries for:
- hydrazoic acid / azide-related ligand (`ligand_10106`)
- a specialized macrocycle (`ligand_9677`)

## Broad takeaways
| Observation | What SRD-46 data suggests |
|---|---|
| Hg²⁺ is far better characterized than Hg⁺ | Much larger ligand and measurement coverage for `metal_71` |
| Hg²⁺ shows very variable stability | Retrieved logK values span from strongly unfavorable cases (citrulline network) to very high values for certain constrained chelators/macrocycles |
| Ligand structure matters a lot | Closely related amino-carboxylates can differ substantially in Hg²⁺ logK |
| Hg⁺ data are narrower and often at higher ionic strength | Many Hg⁺ measurements were retrieved at I = 0.7–3 M, often with simpler oxy-donor ligands |

## Chemistry insight
Mercury is a **soft Lewis acid**, so in general its strongest complexes are often expected with **soft donor atoms**, especially sulfur donors. In the subset we retrieved here, the strongest explicit Hg²⁺ values were associated with certain **preorganized/macrocyclic or conformationally constrained ligands**, while Hg⁺ coverage was more limited and often focused on simpler oxygen-donor systems. That said, this particular pass did **not successfully retrieve the classic halide/cyanide/sulfur-ligand series**, so I’d avoid overgeneralizing beyond the records above.

If you want, I can next pull a more focused table for any one of these:
| Option | What I can fetch |
|---|---|
| **Hg(II) with halides** | chloride / bromide / iodide constants |
| **Hg(II) with sulfur ligands** | thiourea, cysteine, thiosulfate, thiocyanate |
| **Hg(I) complexes** | a cleaner summary of all Hg⁺ logK systems |
| **Biological ligands** | glycine, cysteine, glutathione, amino acids |
| **Strong chelators** | EDTA, cyanide, macrocycles |

---