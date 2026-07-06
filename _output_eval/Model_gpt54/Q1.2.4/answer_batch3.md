SRD-46 shows **2 distinct equilibrium networks** for the **Ni²⁺–EDTA** system.

The largest network size is **3 nodes**. In the returned `search_networks` result, the explicitly expanded largest network is **`ref_eq_net_5023`**, which contains these VLM node IDs:

| network_id | node_count | VLM node IDs |
|---|---:|---|
| ref_eq_net_5023 | 3 | Not exposed in the `search_networks` summary output |

What SRD-46 does expose here is the 3 node-defining equilibria in that largest network:

| network_id | beta_def_id | equation | value |
|---|---|---|---:|
| ref_eq_net_5023 | beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] | -11.9 |
| ref_eq_net_5023 | beta_def_788 | [ML] + [H] <=> [MHL] | 3.1 |
| ref_eq_net_5023 | beta_def_812 | [M] + [L] <=> [ML] | 18.4 |

So the direct answer is:

| Question | Answer |
|---|---|
| Number of distinct Ni²⁺–EDTA equilibrium networks | 2 |
| Largest network | `ref_eq_net_5023` |
| Size of largest network | 3 nodes |
| All VLM node IDs in largest network | Not provided by the current SRD-46 network summary output |

If you want, I can do one more SRD-46 step to explicitly extract the **actual `vlm_N` IDs** belonging to `ref_eq_net_5023`.

---