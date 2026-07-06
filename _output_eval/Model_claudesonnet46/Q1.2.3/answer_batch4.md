# 🔬 Zinc–Citrate Equilibrium Network (NIST SRD-46)

## System Overview

**Metal:** Zn²⁺ (`metal_208`) | **Ligand:** Citric acid — 2-Hydroxypropane-1,2,3-tricarboxylic acid (`ligand_9058`)  
**Best network:** `ref_eq_net_22198` | **Conditions:** ~25 °C, ionic strength 0–0.25 M  
**Nodes:** 4 | **Edges:** 6 (the most connected Zn network found in SRD-46 across citrate, NTA, and EDTA systems)

---

## Species in the Network

| Node | Formula | Chemical Meaning |
|---|---|---|
| **Free metal** | Zn²⁺ | Aquated zinc(II) ion — the central reference node |
| **ZnL⁻** | Zn(cit)⁻ | 1:1 complex with fully deprotonated citrate (L³⁻) |
| **ZnHL** | Zn(Hcit) | 1:1 complex with singly protonated citrate (HL²⁻) |
| **ZnL₂⁴⁻** | Zn(cit)₂⁴⁻ | 1:2 complex — one Zn²⁺ chelated by two citrate ligands |
| **Zn₂(H₋₁L)₂²⁻** | Zn₂(cit-OH)₂²⁻ | Dinuclear complex: two Zn²⁺ bridged by two alkoxide-citrate ligands |

---

## Equilibrium Reactions and Stability Constants

| Equilibrium Reaction | β Definition | log β (~25 °C) |
|---|---|---|
| Zn²⁺ + L³⁻ ⇌ ZnL⁻ | [ML]/[M][L] | **4.98** |
| Zn²⁺ + 2 L³⁻ ⇌ ZnL₂⁴⁻ | [ML₂]/[M][L]² | **8.32** |
| Zn²⁺ + HL²⁻ ⇌ ZnHL | [MHL]/[M][HL] | **3.19** |
| 2 Zn²⁺ + 2 L³⁻ ⇌ Zn₂(H₋₁L)₂²⁻ + 2 H⁺ | [M₂(H₋₁L)₂]/[M]²[L]² | **5.33** |

---

## Network Topology

The 6 edges connect the 4 species nodes in a rich web:

- **Zn²⁺ ↔ ZnL⁻** (direct 1:1 complexation, log β = 4.98)
- **Zn²⁺ ↔ ZnHL** (complexation with protonated citrate, log β = 3.19)
- **Zn²⁺ ↔ ZnL₂⁴⁻** (bis-citrate, log β = 8.32)
- **ZnL⁻ ↔ ZnHL** (protonation step on the complex)
- **ZnL⁻ ↔ ZnL₂⁴⁻** (addition of second citrate)
- **Zn²⁺ ↔ Zn₂(H₋₁L)₂²⁻** (dinuclear formation with hydroxyl deprotonation)

---

## Chemistry Insights

1. **pH-driven speciation:** Citric acid is triprotic (pKa ≈ 2.9, 4.35, 5.65). At mildly acidic pH the ZnHL species dominates; near neutral pH (e.g., blood plasma at 7.4) ZnL⁻ takes over; at high citrate concentrations the bis-complex ZnL₂⁴⁻ (log β = 8.32) becomes significant.

2. **Remarkable dinuclear species:** The Zn₂(H₋₁L)₂²⁻ complex carries the H₋₁ notation, meaning citrate's *hydroxyl group* has been deprotonated by metal coordination — a process that normally requires pH > 13 for free citric acid, but is dramatically facilitated by Zn²⁺ binding. Two zinc centers are bridged by two alkoxide-citrate ligands in a symmetric dinuclear cage, a motif that has been confirmed by X-ray crystallography in related systems.

3. **Real-world relevance:** Zinc–citrate equilibria matter in multiple practical contexts: citrate-buffered pharmaceutical formulations (e.g., zinc lozenges for cold treatment), plant root exudate chemistry where citrate mobilizes zinc from soil minerals, and food science where zinc bioavailability is modulated by citrate in dairy products and infant formula.

---

*Source: NIST SRD-46 Standard Reference Database 46, network `ref_eq_net_22198`.*

---