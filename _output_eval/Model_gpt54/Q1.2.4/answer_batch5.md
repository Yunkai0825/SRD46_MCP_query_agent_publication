SRD-46 shows **2 distinct equilibrium networks** for the **Ni²⁺–EDTA** system.

The largest network size is **3 nodes**. Both networks have 3 nodes, and the returned ranking shows **`ref_eq_net_5023`** first, so that is the selected largest network.

| network_id | node_count | edge_count | T range (°C) | I range (M) |
|---|---:|---:|---|---|
| ref_eq_net_5023 | 3 | 3 | 20–30 | -0.05–0.25 |
| ref_eq_net_5024 | 3 | 3 | 19–29 | 0.85–1.15 |

For **`ref_eq_net_5023`**, the VLM node count is **3**. The returned network summary does **not expose the individual `vlm_N` node IDs**, only the count and included beta definitions. To list the exact VLM node IDs, I’d need one more SRD-46 query against the underlying network-node mapping.

| selected largest network | VLM node IDs available directly? |
|---|---|
| ref_eq_net_5023 | No — only `vlm_count = 3` returned |

If you want, I can do that follow-up query and extract the exact **three `vlm_N` IDs** from SRD-46.

---