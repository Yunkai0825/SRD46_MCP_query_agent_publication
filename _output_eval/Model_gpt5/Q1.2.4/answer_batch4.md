Below is what SRD‑46 reports for Ni²⁺–EDTA (metal_112 with ligand_6277):

How many distinct equilibrium networks?
- Two distinct reference equilibrium networks are present for Ni²⁺–EDTA under the cataloged conditions.

| network_id | node_count | edge_count | T_range (°C) | I_range (M) | beta_def_ids in network |
|---|---:|---:|---|---|---|
| ref_eq_net_5023 | 3 | 3 | 20–30 | −0.05–0.25 | beta_def_966; beta_def_788; beta_def_812 |
| ref_eq_net_5024 | 3 | 3 | 19–29 | 0.85–1.15 | beta_def_966; beta_def_739; beta_def_788 |

Largest network and its contents
- Both networks have the same node count (3). Choosing ref_eq_net_5023 (tie by node_count):
  - Reactions present in ref_eq_net_5023 and example logK values at its reference anchor:
  
    | beta_def_id | equation | logK (example) |
    |---|---|---:|
    | beta_def_966 | [M(OH)L] + [H] ⇌ [ML] + [H₂O] | −11.9 |
    | beta_def_788 | [ML] + [H] ⇌ [MHL] | 3.1 |
    | beta_def_812 | [M] + [L] ⇌ [ML] | 18.4 |

- The network’s VLM node membership count is 3, but the specific VLM node IDs (vlm_N) were not returned in the current tool results. To list them, we need to run a VLM‑to‑network mapping query (group by network_id for metal_112 + ligand_6277) and extract the vlm_N identifiers for ref_eq_net_5023.

Notes and context
- The Ni²⁺–EDTA system in the catalog includes 4 beta definitions overall (ML formation, protonation to MHL and MH₂L, and hydroxo coupling via M(OH)L). The two reference networks differ by including either MH₂L (beta_def_739) or M(OH)L (beta_def_966) alongside ML/MHL, which is typical of acid–base and hydrolysis coupling in EDTA chelation chemistry.

Source: NIST Standard Reference Database 46 (SRD‑46).

---