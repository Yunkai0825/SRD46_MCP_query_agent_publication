Short answer: SRD‑46 currently contains no stability-constant measurements with supercritical CO2 (scCO2) as the solvent.

What I checked in SRD‑46 and what turned up
| Dataset/Field checked | Filter for scCO2 context | Matches |
|---|---|---|
| ligandmetal_stability_measured | solvent_name, electrolyte_composition, reaction_type containing “supercritical” AND (“CO2”/“CO₂”/“carbon dioxide”) | 0 |
| ligandmetal_stability_measured | notes/raw_definition/normalized_definition containing “supercritical” AND (“CO2”/“CO₂”/“carbon dioxide”) | 0 |
| ligand_pka_measured | solvent_name/electrolyte containing “supercritical” AND (“CO2”/“CO₂”/“carbon dioxide”) | 0 |
| ref_literature_alt | citation containing “supercritical” AND (“CO2”/“CO₂”/“carbon dioxide”) | 0 |
| ligandmetal_stability_measured | notes mentioning “CO2” (any context) | 1 record, but only about CO2 gas evolution in a reaction; not scCO2 as solvent |

Interpretation and next steps
- Within SRD‑46’s curated stability and pKa datasets, there are no equilibrium constants explicitly measured in supercritical CO2 as the bulk solvent.
- If you’d like, I can broaden the search to: (a) near‑critical CO2 or CO2‑expanded liquids (CO2 + organic modifiers), (b) specific metals/ligands you’re interested in, or (c) track down external literature beyond SRD‑46 where scCO2 equilibria might have been reported.

Source: NIST SRD‑46 (searches over ligandmetal_stability_measured, ligand_pka_measured, and ref_literature_alt).

---