Based on the SRD-46 data retrieved so far for **Pb²⁺ (metal_125)**, the clinically relevant ligands that are explicitly present are **penicillamine** and **citrate**; the Pb catalog slice also contains high-interest thiol ligands such as **cysteine** and **glutathione**, plus two unnamed macrocycles, but I do **not** yet have extracted numerical log β values for all of them. The catalog specifically did **not** show **EDTA, DTPA, or DMSA** in this Pb²⁺ slice, so I cannot rank those from the retrieved SRD-46 records.

| Ligand | SRD-46 ID | Present with Pb²⁺ in retrieved catalog? | Clinical relevance for lead chelation |
|---|---:|---|---|
| Penicillamine | ligand_5857 | Yes | Historically used clinically |
| Citric acid | ligand_9058 | Yes | Not a standard clinical lead chelator |
| Cysteine | not resolved here | Yes | Biochemical thiol; not standard clinical chelator |
| Glutathione | not resolved here | Yes | Biochemical thiol; not standard clinical chelator |
| EDTA | — | Not in retrieved Pb catalog slice | Yes, clinically used |
| DMSA (succimer) | — | Not in retrieved Pb catalog slice | Yes, clinically used |
| Dimercaprol (BAL) | — | Not in retrieved Pb catalog slice | Yes, clinically used |
| D-penicillamine | ligand_5857 | Yes | Yes, clinically used |

Two explicit ligand identities confirmed from SRD-46 are:

| Ligand | Name in SRD-46 | Ligand class | Pb²⁺ measurements in card |
|---|---|---|---:|
| Penicillamine | D-2-Amino-3-mercapto-3-methylbutanoic acid | Amino Acids | 13 |
| Citric acid | 2-Hydroxypropane-1,2,3-tricarboxylic acid | Carboxylic acids polyacids | Pb²⁺ included among 57 metal partners |

### What this means
| Conclusion | SRD-46 support |
|---|---|
| **Penicillamine is the strongest clinically relevant candidate currently confirmed in the retrieved Pb²⁺ dataset** | It is explicitly present as a Pb²⁺ ligand and is a known clinical chelator |
| **Citrate binds Pb²⁺ but is not a frontline clinical chelator** | Present in SRD-46 Pb²⁺ data, but not standard therapy |
| **EDTA/DMSA/BAL are clinically important, but not rankable from the records retrieved here** | They were not found in the Pb²⁺ catalog slice we built |

### Practical chemistry note
Thiol-containing ligands often bind **Pb²⁺** strongly because lead is a **soft Lewis acid**, so sulfur donors such as those in **penicillamine**, **cysteine**, and **glutathione** are chemically plausible high-affinity binders. Clinically, however, choice of chelator depends on far more than raw affinity: toxicity, oral availability, redistribution risk, and renal handling matter just as much.

If you want, I can continue the SRD-46 search to extract an actual **ranked log β table for Pb²⁺ ligands** under matched aqueous conditions and then compare the top binders against the clinically used chelators.

---