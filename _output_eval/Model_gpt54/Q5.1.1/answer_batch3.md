SRD-46 shows that **mercury complexation is dominated by Hg(II)**, with a smaller but distinct **Hg(I)** set.

| Mercury form | SRD-46 ID | Ligand count | Measurement count | Notes |
|---|---:|---:|---:|---|
| Hg(II) | `metal_71` | 310 | 1097 | Main mercury entry; broad coordination chemistry |
| Hg(I) | `metal_72` | 31 | 83 | Much smaller coverage; often treated separately from Hg(II) |

## Big-picture picture of mercury complexes

From the Hg(II) system catalog, SRD-46 contains about **20 ligand pairings and 92 species** in a reusable overview, with recurring stoichiometries such as:

| Beta definition | Meaning |
|---|---|
| `beta_def_812` | ML |
| `beta_def_840` | ML2 |
| `beta_def_872` | ML3 |
| `beta_def_894` | ML4 |

There are also **hydroxo**, **protonated**, **polynuclear**, and some **solid-phase** mercury species.

## What ligands show up most for mercury?

The cataloged Hg(II) systems span several chemically important ligand families:

| Ligand family | Examples in SRD-46 |
|---|---|
| Halides | chloride (`ligand_10163`), bromide (`ligand_10168`), iodide (`ligand_10171`) |
| Pseudohalides | HCN (`ligand_10090`), hydrazoic acid (`ligand_10106`), thiocyanic acid (`ligand_10092`) |
| Hydroxo / inorganic | hydroxide (`ligand_10076`), carbonate (`ligand_10096`) |
| N-donor ligands | ammonia (`ligand_10103`), methylamine, pyridine, imidazole, ethylenediamine |
| Soft S/Se donors | thiourea, thiodiglycol, thiosemicarbazide, selenourea, H2S, TDS |
| Strong multidentate chelators | EDTA (`ligand_6277`) and related aminopolycarboxylates |

## What kinds of complexes are typical?

The retrieved network data show Hg(II) participating in:

| Pattern | Evidence from SRD-46 |
|---|---|
| Simple mononuclear complexes | ML and ML2 are common recurring forms |
| Protonated complexes | MHL and MHL2 appear in several amino-acid systems |
| Hydrolyzed species | hydroxide-containing mercury species are explicitly cataloged |
| Polynuclear species / solids | present for hydroxo, sulfide/thiocyanate/iodide-related systems |
| Strong binding to soft donors | sulfur-containing ligands are heavily represented in the catalog |

That last point matches standard chemistry intuition: **Hg(II) is a soft Lewis acid**, so sulfur donors and heavier halides are especially important.

## Example Hg(II) speciation networks

The network search returned mostly **Hg(II)** reference networks at roughly **20–25 °C** and **low ionic strength**, especially for amino acids and sulfur-containing amino acids.

A representative highest-node network was for **L-2,3-diaminopropanoic acid** (`ligand_5883`):

| Species / beta definition | Equation | Type | Value |
|---|---|---:|---:|
| ML2 (`beta_def_840`) | [M] + [L]^2 ⇌ [ML2] | logK | -15.9 |
| MHL2 (`beta_def_792`) | [ML2] + [H] ⇌ [MHL2] | logK | -6.04 |
| MHL (`beta_def_779`) | [M] + [HL] ⇌ [MHL] | logK | 4.78 |
| MHL (`beta_def_788`) | [ML] + [H] ⇌ [MHL] | logK | 5.81 |
| ML (`beta_def_812`) | [M] + [L] ⇌ [ML] | logK | 8.37 |

Other Hg(II) network ligands returned included:

| Ligand type | Examples |
|---|---|
| Simple amino acids | glycine, β-alanine, ornithine |
| Sulfur amino acids | cysteine, methionine analogs, mercaptoimidazole-containing amino acid |
| Diamino acids | 2,3-diaminopropanoic acid |
| Macrocycles | aza/oxa macrocyclic ligands |

## Hg(I) versus Hg(II)

Hg(I) has much less coverage in SRD-46, but the database still shows some characteristic behavior:

| Mercury form | Observed data types |
|---|---|
| Hg(II) | broad stability coverage, especially with chelators, hydroxide, halides, sulfur donors |
| Hg(I) | narrower set: azide, hydroxide, pyrophosphate/triphosphate, dicarboxylates and simple carboxylates, one macrocycle |

For Hg(I), SRD-46 specifically notes thermodynamic data for:

| Hg(I) ligand examples | Notes |
|---|---|
| hydrogen azide / azide | ΔS and ΔH reported |
| hydroxide | logK reported |
| pyrophosphate / triphosphate | logK reported |
| oxalic, succinic, propane-2,2-dicarboxylic acids | logK reported |
| acetic and propionic acids | logK reported |
| one macrocyclic ligand (`ligand_9677`) | ΔS and ΔH reported |

So, **Hg(I) appears as a more specialized, smaller thermodynamic subset**, whereas **Hg(II) is the main oxidation state for rich coordination chemistry in SRD-46**.

## Thermodynamic coverage

The stability search results available here were more thermodynamic-summary-like than a ranked logβ table, but they still show where SRD-46 has depth:

| Mercury form | Thermodynamic coverage noted |
|---|---|
| Hg(II) | ΔS for ~15 Hg-ligand pairs, mainly hydroxide, hydrogen sulfite, EDTA-family chelators, pyridyl iminodiacetates, and some macrocycles |
| Hg(II) | ΔH sparse; explicitly noted for iodide at 25 °C, I = 0.5 |
| Hg(I) | ΔS and ΔH for azide and one macrocycle; logK for hydroxide, phosphate-derived ligands, and simple carboxylates |

## Practical chemistry takeaway

| Theme | Interpretation |
|---|---|
| Soft-donor preference | Hg(II) strongly favors sulfur-containing ligands; this is reflected by many thiourea/thioether/thiol-related entries |
| Halide richness | chloride, bromide, and especially iodide systems are prominent |
| Hydrolysis matters | hydroxo and polynuclear species mean mercury speciation can shift strongly with pH |
| Chelation matters | EDTA-family and macrocyclic ligands are well represented, showing strong sequestration chemistry |

In short: **SRD-46 portrays mercury as a metal with very broad Hg(II) complex chemistry, especially with halides, soft sulfur donors, hydroxo species, and multidentate chelators, while Hg(I) is much less extensively covered and more specialized.**

If you want, I can next pull a **table of specific mercury ligands and their reported stability constants** from SRD-46, or focus on a subset like **Hg–chloride**, **Hg–iodide**, **Hg–thiol/thiourea**, or **Hg–EDTA**.

---