SRD-46 contains **297 ligands** in the **Amino Acids** class.

| Ligand class | Count |
|---|---:|
| Amino Acids | 297 |

This was confirmed two ways in SRD-46:
| Check | Result |
|---|---:|
| `db_count_records` on `ligand_card` where `ligand_class_name = 'Amino Acids'` | 297 |
| `db_distribution` on `ligand_card` grouped by `ligand_class_name` with the same filter | 297 |

Source: **NIST SRD-46**.

---