SRD-46 shows **2 distinct equilibrium networks** for the **Ni²⁺–EDTA** system.

Both networks have **3 nodes** and **3 edges**, so the largest network is tied. Using the returned ordering from `search_networks`, the selected largest network is **`ref_eq_net_5023`**.

| system | network_count | selected_largest_network | node_count | edge_count |
|---|---:|---|---:|---:|
| Ni²⁺–EDTA | 2 | ref_eq_net_5023 | 3 | 3 |

The VLM node IDs in **`ref_eq_net_5023`** are the three measurements attached to its node definitions:

| network_id | VLM node IDs |
|---|---|
| ref_eq_net_5023 | `vlm_108596`, `vlm_108590`, `vlm_108585` |

For reference, these correspond to the three node constants in that network:

| network_id | beta_definition_id | equation | VLM ID |
|---|---|---|---|
| ref_eq_net_5023 | `beta_def_966` | [M(OH)L] + [H] ⇌ [ML] + [H2O] | `vlm_108596` |
| ref_eq_net_5023 | `beta_def_788` | [ML] + [H] ⇌ [MHL] | `vlm_108590` |
| ref_eq_net_5023 | `beta_def_812` | [M] + [L] ⇌ [ML] | `vlm_108585` |

Source: **NIST SRD-46**.

---