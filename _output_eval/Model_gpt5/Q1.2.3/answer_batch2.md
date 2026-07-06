Selected Zn–histidine equilibrium network (>5 nodes)

Metadata
- Metal: Zn2+ (metal_208)
- Ligand: L‑Histidine (ligand_5898)
- Network size: 10 nodes
- Beta definitions present in this network: beta_def_812, 840, 788, 792, 204, 984
- Reported condition span in the catalog: T ≈ 19–41 °C; ionic strength ≈ 0.05–3.15 M

Species (nodes)
| Species | Description |
|---|---|
| M | Zn2+ (free metal) |
| H | Proton |
| L | Histidinate (deprotonated histidine donor form) |
| ML | ZnL (1:1 complex) |
| ML2 | ZnL2 (1:2 complex) |
| MHL | ZnHL (protonated 1:1 complex) |
| MHL2 | ZnHL2 (protonated 1:2 complex) |
| M(HL)2 | Zn(HL)2 (1:2 complex with protonated ligand) |
| M(OH)L2 | Zn(OH)L2 (hydroxo–ligand complex) |
| H2O | Water |

Equilibrium definitions (edges) in the network
| beta_def_id | Reaction |
|---|---|
| beta_def_812 | [M] + [L] ⇌ [ML] |
| beta_def_840 | [M] + [L]^2 ⇌ [ML2] |
| beta_def_788 | [ML] + [H] ⇌ [MHL] |
| beta_def_792 | [ML2] + [H] ⇌ [MHL2] |
| beta_def_204 | [MHL2] + [H] ⇌ [M(HL)2] |
| beta_def_984 | [M(OH)L2] + [H] ⇌ [ML2] + [H2O] |

Notes
- This Zn–histidine network captures ligand protonation and stepwise complex formation (ML → ML2), plus hydroxo competition via M(OH)L2. As pH increases, deprotonated ligand forms (L) and hydroxo species become more relevant; at higher ligand-to-metal ratios, ML2-type nodes are favored.

Source: NIST SRD‑46 (IUPAC Stability Constants Database).

---