I picked the **zinc–hydroxide** reference equilibrium network, which has **11 nodes** in SRD-46.

| Chosen network | Metal | Ligand | Node count | Edge count | Temperature range (°C) | Ionic strength range (M) |
|---|---|---:|---:|---:|---:|---:|
| ref_eq_net_27522 | Zn²⁺ | Hydroxide ion | 11 | 55 | 20–30 | -0.05–0.25 |

### Species involved
From the network equations, the species/forms represented are:

| Network species label | Interpreted zinc species/form |
|---|---|
| [M] | free **Zn²⁺** |
| [L] | **OH⁻** |
| [ML] | **ZnOH⁺** |
| [ML2] | **Zn(OH)2(aq)** |
| [ML3] | **Zn(OH)3⁻** |
| [ML4] | **Zn(OH)4²⁻** |
| [ML2(s,am)] | amorphous **Zn(OH)2(s)** |
| [ML2(s,beta1)] | solid **Zn(OH)2(s)** polymorph |
| [ML2(s,beta2)] | solid **Zn(OH)2(s)** polymorph |
| [ML2(s,gamma)] | solid **Zn(OH)2(s)** polymorph |
| [ML2(s,delta)] | solid **Zn(OH)2(s)** polymorph |
| [ML2(s,epsilon)] | solid **Zn(OH)2(s)** polymorph |
| [MO(s)] + H2O | **ZnO(s)** / zinc oxide solid equilibrium with water |

### Constants listed in this network
| Beta definition | Equation | logK |
|---|---|---:|
| beta_def_347 | [MO(s)] + [H2O] ⇌ [M] + [OH]² | -15.96 |
| beta_def_344 | [ML2(s,epsilon)] ⇌ [M] + [L]² | -15.77 |
| beta_def_345 | [ML2(s,gamma)] ⇌ [M] + [L]² | -15.56 |
| beta_def_340 | [ML2(s,beta1)] ⇌ [M] + [L]² | -15.54 |
| beta_def_341 | [ML2(s,beta2)] ⇌ [M] + [L]² | -15.50 |
| beta_def_343 | [ML2(s,delta)] ⇌ [M] + [L]² | -15.45 |
| beta_def_337 | [ML2(s,am)] ⇌ [M] + [L]² | -14.82 |
| beta_def_840 | [M] + [L]² ⇌ [ML2] | -10.2 |
| beta_def_812 | [M] + [L] ⇌ [ML] | 4.7 |
| beta_def_872 | [M] + [L]³ ⇌ [ML3] | 13.9 |
| beta_def_894 | [M] + [L]⁴ ⇌ [ML4] | 15.5 |

A nice chemistry takeaway is that this network shows the classic **stepwise hydrolysis of Zn²⁺** from **ZnOH⁺** through **Zn(OH)4²⁻**, while also including **solid Zn(OH)2 polymorphs** and **ZnO(s)**. That makes it a rich speciation network rather than just a simple aqueous-complex set.

**Source:** NIST SRD-46 equilibrium network search, network `ref_eq_net_27522`.

---