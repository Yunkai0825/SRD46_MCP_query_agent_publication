## Ni²⁺–EDTA Equilibrium Networks (NIST SRD-46)

### Number of distinct networks: **2**

Both networks contain **3 nodes and 3 edges** each, so they are tied in size. By convention I select **ref_eq_net_5023** (the lower-ionic-strength, reference-state network) as the "largest."

---

### Largest network: `ref_eq_net_5023`

| VLM Node ID | Equilibrium | log K |
|-------------|-------------|------:|
| `vlm_108585` | [M] + [L] ⇌ [ML] | 18.4 |
| `vlm_108590` | [ML] + [H] ⇌ [MHL] | 3.1 |
| `vlm_108596` | [M(OH)L] + [H] ⇌ [ML] + H₂O | −11.9 |

**Conditions:** T 20–30 °C, I ≈ 0–0.25 M

---

### Second network: `ref_eq_net_5024`

| VLM Node ID | Equilibrium | log K |
|-------------|-------------|------:|
| `vlm_108591` | [ML] + [H] ⇌ [MHL] | 3.0 |
| `vlm_108601` | [M(OH)L] + [H] ⇌ [ML] + H₂O | −12.9 |
| `vlm_108603` | [MHL] + [H] ⇌ [MH₂L] | 2.4 |

**Conditions:** T 19–29 °C, I ≈ 0.85–1.15 M

---

### Chemistry insight

The two networks partition the 19 total Ni²⁺–EDTA measurements by ionic strength. Network 5023 anchors at low ionic strength and includes the classic overall formation constant log K₁ = 18.4, consistent with EDTA's well-known role as one of the strongest hexadentate chelators for divalent transition metals. Network 5024, measured at ~1 M ionic strength, omits the overall formation step but adds the doubly protonated species MH₂L, reflecting the greater importance of proton competition at higher electrolyte concentrations. The slight decrease in the hydroxo-complex equilibrium (from −11.9 to −12.9) at higher I is consistent with typical ionic-strength effects on charged-species equilibria.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes).*

---