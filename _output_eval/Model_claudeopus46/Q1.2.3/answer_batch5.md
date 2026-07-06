I have a great network to describe. Let me present the **Zn²⁺ + Cysteine** system, which has **7 nodes** — the richest zinc network returned.

---

# Equilibrium Network: Zn²⁺ + L-Cysteine (7 Nodes)

**Source:** NIST SRD-46, network `ref_eq_net_1017`
**Ligand:** L-2-Amino-3-mercaptopropanoic acid (L-Cysteine), defined as H₂L
**SMILES:** `N[C@@H](CS)C(=O)O`
**Conditions:** T ≈ 20–30 °C, I ≈ 0–0.25 M

## Species in the Network

Cysteine is a tridentate amino acid with thiol (–SH), amino (–NH₂), and carboxylate (–COO⁻) donor groups. The fully deprotonated form is **L²⁻**, and the singly protonated form is **HL⁻**. The network contains **7 distinct equilibrium species**:

| # | Species | Formula | Description | logK | Equilibrium |
|---|---------|---------|-------------|------|-------------|
| 1 | **ZnL** | ZnL | 1:1 complex, fully deprotonated ligand | 9.11 | Zn²⁺ + L²⁻ ⇌ ZnL |
| 2 | **ZnL₂²⁻** | ZnL₂²⁻ | 1:2 complex (bis-cysteinato zinc) | 18.12 | Zn²⁺ + 2L²⁻ ⇌ ZnL₂²⁻ |
| 3 | **ZnHL⁺** | Zn(HL)⁺ | 1:1 complex with one protonated ligand | 4.6 | Zn²⁺ + HL⁻ ⇌ Zn(HL)⁺ |
| 4 | **ZnHL₂⁻** | Zn(HL)L⁻ | 1:2 complex, one ligand protonated | 6.3 | ZnL₂²⁻ + H⁺ ⇌ Zn(HL)L⁻ |
| 5 | **Zn(HL)₂** | Zn(HL)₂ | 1:2 complex, both ligands protonated | 5.5 | Zn(HL)L⁻ + H⁺ ⇌ Zn(HL)₂ |
| 6 | **Zn₃HL₄⁵⁻** | Zn₃(HL)L₃⁵⁻ | Trinuclear cluster with 3 Zn, 4 cysteinates, 1 proton | 49 | 3Zn²⁺ + H⁺ + 4L²⁻ ⇌ Zn₃HL₄⁵⁻ |
| 7 | **Zn₃L₄⁶⁻** | Zn₃L₄⁶⁻ | Fully deprotonated trinuclear cluster (precursor to #6) | 6.9 | Zn₃L₄⁶⁻ + H⁺ ⇌ Zn₃HL₄⁵⁻ |

## Species Grouped by Type

### Mononuclear Zn–Cys Complexes (4 species)
- **ZnL** and **ZnL₂²⁻**: Fully deprotonated 1:1 and 1:2 complexes. The large cumulative log β₂ = 18.12 reflects strong thiolate–Zn²⁺ binding.
- **Zn(HL)⁺**: A protonated 1:1 complex — likely the thiol remains protonated while the amino/carboxylate groups coordinate.
- **Zn(HL)L⁻** and **Zn(HL)₂**: Stepwise protonation of the bis complex, showing how pH controls speciation.

### Polynuclear Zn–Cys Clusters (2 species)
- **Zn₃L₄⁶⁻** and **Zn₃HL₄⁵⁻**: Remarkable trinuclear zinc-cysteine clusters bridged by thiolate sulfurs. The enormous cumulative log β = 49 for Zn₃HL₄ formation highlights the cooperative stability of multi-metal thiolate assemblies — reminiscent of zinc-finger protein motifs where cysteine residues bridge or chelate multiple zinc ions.

### Free Ligand Protonation States
The network implicitly includes **Zn²⁺ (free metal)**, **L²⁻**, and **HL⁻** as reactant nodes connecting the equilibria.

## Chemistry Insight

This network beautifully illustrates how cysteine's versatile donor set (S, N, O) supports a rich speciation landscape for Zn²⁺. The thiolate sulfur is the dominant anchor — consistent with the biological preference of zinc for cysteine-rich binding sites (e.g., zinc fingers, metallothioneins). The presence of **trinuclear Zn₃L₄** clusters is particularly noteworthy: such polynuclear thiolate-bridged species are models for the Zn–S cores found in metallothionein proteins, where up to 7 zinc ions are coordinated by 20 cysteine residues in clustered domains.

---