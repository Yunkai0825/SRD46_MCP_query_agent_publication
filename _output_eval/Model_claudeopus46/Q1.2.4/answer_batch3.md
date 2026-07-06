## Ni²⁺–EDTA Equilibrium Networks (NIST SRD-46)

### Number of distinct networks: **2**

The Ni²⁺–EDTA system has two reference equilibrium networks, both containing **3 nodes and 3 edges**:

| Network ID | Nodes | Edges | T range (°C) | I range (M) | Species covered |
|------------|-------|-------|-------------|-------------|-----------------|
| ref_eq_net_5023 | 3 | 3 | 20–30 | 0–0.25 | ML, MHL, M(OH)L |
| ref_eq_net_5024 | 3 | 3 | 19–29 | 0.85–1.15 | ML, MHL, MH₂L |

Since both networks are the same size (3 nodes each), I selected **ref_eq_net_5023** (lowest ID as tiebreaker). Its VLM node IDs are:

| VLM ID | Equilibrium | log K |
|--------|-------------|-------|
| **vlm_108590** | [M(OH)L] + [H] ⇌ [ML] + H₂O | −11.9 |
| **vlm_108591** | [ML] + [H] ⇌ [MHL] | 3.1 |
| **vlm_108592** | [M] + [L] ⇌ [ML] | 18.4 |

**Chemistry insight:** The dominant formation constant (log K = 18.4 for ML) confirms EDTA's well-known exceptionally strong chelation of Ni²⁺, driven by its hexadentate coordination wrapping around the metal center. The two networks differ in ionic strength regime—the low-I network (ref_eq_net_5023) includes the hydroxo species M(OH)L, while the high-I network (ref_eq_net_5024) instead resolves the doubly protonated MH₂L adduct, reflecting how the ionic medium shifts the accessible speciation window.

*Source: NIST Standard Reference Database 46 (SRD-46).*

---