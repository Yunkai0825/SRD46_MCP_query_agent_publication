SRD-46 contains **297 ligands** in the **“Amino Acids”** class.

| ligand_class | count |
|---|---:|
| Amino Acids | 297 |

This was confirmed two ways in **NIST SRD-46**:

| check | result |
|---|---:|
| `db_count_records` on `ligand_card` with `ligand_class_name = 'Amino Acids'` | 297 |
| `db_distribution` on `ligand_card` grouped by `ligand_class_name` with the same filter | 297 |

---