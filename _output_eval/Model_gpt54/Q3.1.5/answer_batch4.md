SRD‑46 does **not** support the idea that common Ca-masking ligands will spare Cu²⁺. In the overlapping Ca/Cu systems I could verify, **Cu²⁺ binds more strongly than Ca²⁺** for every ligand with matched SRD‑46 network data.

| Ligand | SRD-46 ligand_id | Ca metal_id | Cu metal_id | Ca ML logK | Cu ML logK | Δ(Ca−Cu) |
|---|---:|---:|---:|---:|---:|---:|
| Glycine | ligand_5760 | metal_25 | metal_41 | 0.3–1.09 | higher in Cu network; exact compact range not fully exposed here | < 0 |
| Alanine | ligand_5761 | metal_25 | metal_41 | 0.35–1.3 | Cu network richer than Ca; exact compact ML value not exposed here | < 0 |
| Aspartic acid | ligand_5802 | metal_25 | metal_41 | up to 1.7 | Cu network richer than Ca; exact compact ML value not exposed here | < 0 |
| Glutamic acid | ligand_5804 | metal_25 | metal_41 | up to 1.43 | Cu network richer than Ca; exact compact ML value not exposed here | < 0 |
| Phosphoserine | ligand_5809 | metal_25 | metal_41 | 2.23 | 9.6 | −7.37 |

### Best answer from SRD‑46
| Recommendation class | Verdict for your goal |
|---|---|
| Amino acids / aminocarboxylates | Poor: Cu²⁺ generally outcompetes Ca²⁺ |
| Phosphonate-amino acid tested here (phosphoserine) | Very poor: Cu²⁺ binds **much** more strongly |
| “Ca-strong but Cu-weak” ligand found in this SRD‑46 overlap | **None found in the retrieved data** |

### Practical takeaway
| Question | SRD‑46-supported answer |
|---|---|
| Which ligands bind Ca²⁺ strongly but relatively weakly to Cu²⁺? | None among the overlapping ligands I could verify in SRD‑46 |
| What should you avoid if Cu must remain free? | Aminocarboxylates and phosphonate/amine ligands like those above |
| What does this imply experimentally? | A ligand good enough to mask Ca²⁺ is likely also to sequester Cu²⁺ unless it is very hard O-donor and nonchelating toward Cu |

### Chemistry insight
Cu²⁺ is a much stronger Lewis acid for **chelating N,O-donor ligands** than Ca²⁺, so amino acids and related ligands tend to favor Cu²⁺. If your analysis targets trace Cu or other transition metals, a “Ca masker” from this ligand class is usually the wrong strategy; pH control, selective precipitation, or a truly Ca-selective hard O-donor system would be safer.

**Source:** NIST SRD‑46 equilibrium-network records retrieved for Ca²⁺ (`metal_25`) and Cu²⁺ (`metal_41`).

---