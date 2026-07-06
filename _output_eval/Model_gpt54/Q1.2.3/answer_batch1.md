I found a qualifying Zn(II) equilibrium network in SRD-46 and selected one actual network with **6 nodes**.

## Selected equilibrium network

| Property | Value |
|---|---|
| Metal | Zn^[2+] |
| Ligand | 6,16-Dioxa-3,9,13,19-tetraaza-1,11(2,6)-dipyridinacycloeicosane |
| Ligand ID | ligand_7653 |
| Network ID | ref_eq_net_171 |
| Node count | 6 |
| Edge count | 12 |
| Temperature range | 20–30 °C |
| Ionic strength range | -0.05–0.25 M |
| Constant type | logK |

## Species involved

From the network equations, the node species are:

| Species | How it appears in the network |
|---|---|
| [M] | free Zn(II) |
| [L] | free ligand |
| [ML] | 1:1 zinc–ligand complex |
| [MHL] | protonated zinc–ligand complex |
| [M(OH)L] | hydroxo zinc–ligand complex |
| [M(OH)2L] | dihydroxo zinc–ligand complex |
| [M2L] | dinuclear zinc complex |
| [M2(OH)L] | hydroxo-bridged dinuclear zinc complex |
| [H] | proton |
| [H2O] | water |

Because SRD-46 defines the network through equilibrium equations, the chemically distinct complex species centered on zinc here are the zinc-containing forms: **[ML]**, **[MHL]**, **[M(OH)L]**, **[M(OH)2L]**, **[M2L]**, and **[M2(OH)L]**, together with free **Zn(II)** and free ligand.

## Equilibria that define this network

| Beta definition | Equation | logK |
|---|---|---:|
| beta_def_812 | [M] + [L] <=> [ML] | 8.89 |
| beta_def_788 | [ML] + [H] <=> [MHL] | 7.45 |
| beta_def_839 | [M(OH)L] + [H] <=> [ML] + [H2O] | 9.52 |
| beta_def_975 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] | 11 |
| beta_def_516 | [ML] + [M] <=> [M2L] | 3.8 |
| beta_def_515 | [M2(OH)L] + [H] <=> [M2L] + [H2O] | 7.07 |

## Plain-language description

This network shows that Zn(II) with this polyaza polyether ligand forms not just a simple **1:1 complex**, but also **protonated**, **hydrolyzed**, and **dinuclear** species. In other words, the system captures competition between ligand binding, protonation, and metal hydrolysis, which is why the network is richer than a basic ZnL-only system.

**Source:** NIST SRD-46 equilibrium network data (`search_networks`, network `ref_eq_net_171`).

---