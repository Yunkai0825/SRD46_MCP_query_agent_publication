I’m missing the actual SRD-46 stability constants needed to do the Cu²⁺/Ni²⁺/Zn²⁺ comparison quantitatively.

From the SRD-46 queries so far, I could **not retrieve explicit NH₃ or ethylenediamine stability data** for those three metals, so I should not invent values. The only literature hits found by citation text were:

| shortcut | citation |
|---|---|
| 49NT | R. Nasanen and V. Tamminen, *J. Amer. Chem. Soc.*, 1949, **71**, 1994 |
| 76ML | O. Makitie, L. H. J. Lajunen and P. Tamminen, *Finn. Chem. Lett.*, 1976, 3 |
| 88LT | O. Lukkari and J. Tamminen, *Finn. Chem. Lett.*, 1988, 15, 13 |

And the stability search that did return rows was for **other aminocarboxylate ligands**, not NH₃ or en, so it is not valid for your requested calculation.

## What can be concluded safely

The intended comparison is:

| metal | target quantity |
|---|---|
| Cu²⁺ | Δ = log K(en) − 2·log K(NH₃) |
| Ni²⁺ | Δ = log K(en) − 2·log K(NH₃) |
| Zn²⁺ | Δ = log K(en) − 2·log K(NH₃) |

But with the current SRD-46 retrieval, **Δ cannot yet be computed** for any of the three metals.

## Best chemistry hypothesis

Even without the missing numbers, the most defensible hypothesis is:

| question | hypothesis |
|---|---|
| Is the chelate effect magnitude consistent across Cu²⁺, Ni²⁺, and Zn²⁺? | **Probably not exactly; it should vary across metals.** |
| Why might it vary? | Differences in **metal–ligand bonding strength**, **preferred coordination geometry**, **ligand-field stabilization**, and for Cu²⁺ especially **Jahn–Teller distortion** can change how much extra stabilization en gains over two NH₃ ligands. |

A chemically reasonable expectation is:

| metal factor | likely consequence for Δ |
|---|---|
| Ni²⁺ (octahedral LFSE important) | en may gain relatively strong stabilization if it fits the preferred geometry well |
| Cu²⁺ (d⁹, Jahn–Teller active) | NH₃ vs en comparison may be less regular because stepwise ammine constants can be uneven |
| Zn²⁺ (d¹⁰, no LFSE) | chelate advantage may be more dominated by entropy/preorganization than ligand-field effects |

So the **chelate effect should not be assumed constant across metals**.

## Status

| item | result |
|---|---|
| SRD-46 NH₃ constants for Cu²⁺/Ni²⁺/Zn²⁺ | not retrieved |
| SRD-46 en constants for Cu²⁺/Ni²⁺/Zn²⁺ | not retrieved |
| Quantitative Δ values | not available from current search |
| Qualitative interpretation | varies across metals, likely due to geometry/LFSE/Jahn–Teller/solvation effects |

If you want, I can continue with a more targeted SRD-46 retrieval strategy to try to extract the actual Cu/Ni/Zn ammine and ethylenediamine constants from the database.

---