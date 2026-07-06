Here’s what the NIST SRD‑46 database shows for Fe2+/Fe3+ with the four neutral “solvent‑type” ligands you asked about, and what can be inferred from closely related systems.

Summary of SRD‑46 findings and reasoned estimates (25 °C, aqueous media)
| Ligand (synonyms) | Fe(II) data in SRD‑46? | Fe(III) data in SRD‑46? | Closest SRD‑46 analog evidence (Fe-centered or donor‑class) | Qualitative estimate of Fe binding (neutral ligand, aqueous) |
|---|---|---|---|---|
| N,N‑Dimethylformamide (DMF) | No hits found for Fe2+ (metal_62) with DMF by name | No hits found for Fe3+ (metal_61) with DMF by name | No Fe entries found for simple amides (formamide, acetamide, N‑methylformamide, dimethylacetamide) under matched conditions | Very weak; amide carbonyl O is a poor donor to aqueous Fe2+/Fe3+. Any DMF–Fe adducts are likely too weak to compete with water; negligible under typical aqueous conditions |
| Acetonitrile (MeCN; cyanomethane; ligand_9825) | No Fe2+ entries; searches return MeCN complexes for Pd2+, Ag+, Cu+ at 25 °C and I ≈ 0.1–1 M, but none for Fe | No Fe3+ entries | SRD‑46 shows MeCN complexes for Pd2+, Ag+, Cu+ (not Fe), consistent with nitriles favoring softer cations | Very weak; nitrile N is a poor donor for aqueous Fe2+/Fe3+. Expect negligible complexation in water |
| Tetrahydrofuran (THF; oxolane) | No hits found for Fe2+ with “tetrahydrofuran/oxolane” by name | No hits found for Fe3+ with “tetrahydrofuran/oxolane” by name | No Fe data for common simple ethers (1,4‑dioxane, 1,2‑dimethoxyethane, diglyme) in water; only multidentate poly(oxa/aza) macrocycles show measurable Fe binding | Very weak; ether O donors bind Fe2+/Fe3+ poorly in water; THF adducts are unlikely to be competitive with hydration |
| Ethylene glycol (EG; ethane‑1,2‑diol; ligand_9621) | No hits found for Fe2+ with EG by name | No hits found for Fe3+ with EG by name | For comparison, Fe complexes are reported with multidentate O,N polyether macrocycles (e.g., ligand_7614; ligand_7579; ligand_7582) at 25 °C and I ≈ 0.1 M, indicating Fe can bind strongly to chelating poly(oxa/aza) ligands. However, no entries for simple neutral glycols | Weak to at most modest via neutral chelation; chelate effect (two OH donors) makes EG stronger than monodentate DMF/MeCN/THF, but in water neutral EG adducts are still expected to be easily outcompeted by hydration (and for Fe3+, by hydrolysis). Overall small effect under typical aqueous conditions |

How this was determined (SRD‑46 queries)
- Direct lookups for Fe2+ (metal_62) and Fe3+ (metal_61) with “dimethylformamide/DMF”, “acetonitrile/cyanomethane”, “tetrahydrofuran/oxolane”, and “ethylene glycol/ethane‑1,2‑diol” returned no aqueous stability‑constant records near 25 °C.
- For acetonitrile specifically, SRD‑46 reports logK data at 25 °C for soft/softer metals (e.g., Pd2+, Ag+), but none for Fe — consistent with nitriles binding weakly to Fe in water.
- For ether/glycol donor classes, no Fe data were found for simple ethers/glycols under the same conditions. SRD‑46 does include measurable Fe2+/Fe3+ complexes with multidentate O,N polyether macrocycles (e.g., ligand_7614; ligand_7579; ligand_7582) at 25 °C, I ≈ 0.1 M, illustrating that Fe binds when strong chelation is present; this contrasts with the absence of Fe data for simple neutral diols like ethylene glycol.

Reasoned estimates (no invented numbers)
- In aqueous solution at ~25 °C and moderate ionic strength, neutral adduct formation of Fe2+/Fe3+ with DMF, MeCN, or THF is expected to be extremely weak and practically negligible compared with hydration (and, for Fe3+, hydrolysis). Their conditional logβ1 values would be very small if measured.
- Ethylene glycol can chelate through two neutral OH donors and should bind Fe2+ somewhat more than the strictly monodentate DMF/MeCN/THF, but still weak under neutral aqueous conditions; for Fe3+, extensive hydrolysis and inner‑sphere aquo complexes dominate, suppressing neutral EG binding.
- Qualitative ordering expected in water (Fe2+): EG (weak but strongest of the four due to chelation) > DMF ≈ MeCN > THF (weakest). For Fe3+, all four remain very weak; EG may be slightly favored by chelation, but hydrolysis dominates.

Notes and caveats
- SRD‑46 focuses on aqueous complexation data; many DMF/MeCN/THF “complexes” in the literature are in non‑aqueous solvents or involve solvation equilibria rather than true aqueous ligand addition. The queries here specifically filtered for aqueous conditions near 25 °C.
- For practical modeling in water, you can usually neglect these neutral donors for Fe2+/Fe3+. If you require measurable complexation with oxygen donors, consider deprotonated species (e.g., glycolates) or strongly chelating multidentate ligands; those classes do show Fe data in SRD‑46.

Source
NIST Standard Reference Database 46 (SRD‑46): searches over ligandmetal_stability_measured joined to ligandmetal_card at 25 °C for Fe2+ (metal_62) and Fe3+ (metal_61) with the named ligands and close analogs (see observations above).

---