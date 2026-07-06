## Ni²⁺–EDTA Equilibrium Networks (SRD-46)

### How many distinct networks?

There are **2** distinct equilibrium networks for the Ni²⁺–EDTA system:

| Network ID | Nodes | Edges | T range (°C) | I range (M) |
|------------|-------|-------|---------------|-------------|
| ref_eq_net_5023 | 3 | 3 | 20–30 | 0–0.25 |
| ref_eq_net_5024 | 3 | 3 | 19–29 | 0.85–1.15 |

Both networks have the same node count (3), so they are tied in size. Selecting **ref_eq_net_5023** (lower ID, standard reference conditions near zero ionic strength):

### Largest Network: ref_eq_net_5023 — VLM Node IDs

| VLM ID | Beta Definition | Equilibrium | log K |
|--------|----------------|-------------|-------|
| **vlm_108585** | beta_def_812 | [M] + [L] ⇌ [ML] | 18.4 |
| **vlm_108590** | beta_def_966 | [M(OH)L] + [H] ⇌ [ML] + H₂O | −11.9 |
| **vlm_108591** | beta_def_788 | [ML] + [H] ⇌ [MHL] | 3.1 |

### Chemistry Insight

The very large formation constant (log K = 18.4) for Ni²⁺–EDTA reflects the classic hexadentate chelation of EDTA, making it one of the most thermodynamically stable EDTA complexes among first-row transition metals. The protonated species MHL (log K = 3.1) and the hydroxo species M(OH)L (derived from log K = −11.9) show that EDTA can remain coordinated even under moderately acidic or basic conditions — a key reason EDTA is widely used as a titrant and masking agent in analytical chemistry.

*Source: NIST Standard Reference Database 46 (SRD-46)*

---