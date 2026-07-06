SRD-46 has substantial data on **zinc(II)** as **`metal_208`**.

| Item | Zn coverage |
|---|---:|
| Metal entry | `metal_208` |
| Name | Zn²⁺ |
| Symbol | Zn |
| Charge | +2 |
| Stability-definition count | 122 |
| Distinct ligand count | 1169 |
| VLM measurement count | 4095 |

A zinc-only catalog snapshot showed:

| Catalog metric | Value |
|---|---:|
| Zn–ligand pair systems in that catalog view | 20 |
| Total species in that view | 94 |

Examples of Zn²⁺ ligand systems present in that catalog include:

| Ligand | Ligand ID |
|---|---|
| Glycine | `ligand_5760` |
| Ethylenediamine | `ligand_7029` |
| Hydroxide | `ligand_10076` |
| Hydrogen cyanide | `ligand_10090` |
| Imidazole | `ligand_7795` |
| Histidine | `ligand_5898` |
| Cysteine | `ligand_5856` |
| Ammonia | `ligand_10103` |
| Citric acid | `ligand_9058` |
| EDTA | `ligand_6277` |
| 1,10-Phenanthroline | `ligand_8191` |
| 2,2'-Bipyridyl | `ligand_8156` |
| Acetic acid | `ligand_8465` |

Common Zn species/equilibrium definitions reported in that snapshot:

| Species type | Example IDs |
|---|---|
| Simple complexes | `beta_def_812` (ML), `beta_def_840` (ML2), `beta_def_872` (ML3), `beta_def_894` (ML4) |
| Protonated complexes | `beta_def_779`, `788`, `792`, `204`, `739`, `751`, `765` |
| Hydroxo complexes | `beta_def_966`, `984`, `238` |
| Polynuclear / mixed species | `beta_def_374`, `502`, `636`, `637`, `651`, `674` |
| Solids | `beta_def_334`, `337`, `340`, `341`, `343`, `344`, `345`, `347` |

One network example retrieved for **Zn²⁺ + glycine** shows room-temperature / low-ionic-strength reference data:

| System | Network ID | T range (°C) | I range (M) | Constants present |
|---|---|---:|---:|---|
| Zn²⁺ + glycine | `ref_eq_net_113` | 31–41 | 0–0.3 | ML, M(OH)L, ML2, ML3 |

Reference values from that network:

| Beta definition | Reaction | Type | Value |
|---|---|---|---:|
| `beta_def_812` | [M] + [L] ⇌ [ML] | logK | 4.87 |
| `beta_def_966` | [M(OH)L] + [H] ⇌ [ML] + [H2O] | logK | 8.9 |
| `beta_def_840` | [M] + [L]² ⇌ [ML2] | logK | 8.97 |
| `beta_def_872` | [M] + [L]³ ⇌ [ML3] | logK | 11.3 |

A top-ranked sample by **largest constant values** for Zn²⁺ highlights strong chelators measured at **25 °C, I = 0.1 M**:

| Ligand | Ligand ID | T (°C) | I (M) |
|---|---|---:|---:|
| trans-1,2-Cyclohexylenedinitrilotetraacetic acid | `ligand_6301` | 25 | 0.1 |
| Nitrilotris(methylenephosphonic acid) | `ligand_8412` | 25 | 0.1 |
| DOTA-like tetraaza polycarboxylates | `ligand_6109`, `6112`, `6104` | 25 | 0.1 |
| EDTA | `ligand_6277` | 25 | 0.1 |
| Triphosphate | `ligand_10117` | 25 | 0.1 |

Chemistry-wise, that pattern makes sense: **Zn²⁺ is strongly stabilized by multidentate N/O donor ligands**, while SRD-46 also captures its important **hydrolysis behavior** and biologically relevant binding to amino acids and imidazole-type donors. The presence of solids and hydroxo species suggests the database is useful not just for simple complexation, but also for **aqueous speciation and precipitation** questions involving zinc.

If you want, I can next give you either:

| Next option | What I’d return |
|---|---|
| **Top zinc ligands** | a ranked table of the most-studied Zn²⁺ ligands |
| **Zinc hydrolysis** | Zn–OH species and constants |
| **Biological ligands** | Zn with glycine, histidine, cysteine, imidazole, ammonia |
| **Strong chelators** | Zn with EDTA, NTA, IDA, citrate, phen, bpy |
| **Literature** | key SRD-46 references behind the zinc data |

*Source: NIST SRD-46.*

---