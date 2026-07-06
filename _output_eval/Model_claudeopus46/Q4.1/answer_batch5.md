Based on my extensive search of the NIST SRD-46 database, here is a comprehensive assessment:

---

# Complexation Constants for DMF, Acetonitrile, THF, and Ethylene Glycol with Fe(II)/Fe(III)

## Direct Data Availability

**None of the eight target metal–ligand pairs (4 ligands × 2 iron oxidation states) have stability constant data in NIST SRD-46.**

| Ligand | Ligand ID | Fe²⁺ (metal_62) | Fe³⁺ (metal_61) |
|--------|-----------|------------------|------------------|
| DMF (N,N-dimethylformamide) | ligand_11422 | ❌ No data | ❌ No data |
| Acetonitrile (MeCN) | ligand_9825 | ❌ No data | ❌ No data |
| THF (tetrahydrofuran) | — | ❌ Not in database | ❌ Not in database |
| Ethylene glycol | ligand_9621 | ❌ No data | ❌ No data |

This is not surprising — these are all **weak, neutral donor solvents** that are far more commonly used as *bulk solvents* than as discrete ligands in aqueous coordination chemistry, which is the focus of SRD-46.

---

## Available Data for These Ligands with Other Metals

### Acetonitrile (ligand_9825) — 3 metals found

| Metal | log K₁ (ML) | log β₂ (ML₂) | T (°C) | I (M) |
|-------|-------------|---------------|---------|--------|
| Cu⁺ | — | 4.35 | 25 | 0.1 |
| Ag⁺ | 0.42 | 0.78 | 25 | 0.1 |
| Pd²⁺ | 1.19 | 1.53 | 25 | 1.0 |

### Ethylene glycol (ligand_9621) — 17 metals found
Primarily lanthanides (La³⁺ through Lu³⁺), plus B³⁺ and Pb²⁺. No transition metal data at all.

### DMF & THF — No data with any metal

---

## Reasoned Estimates

Given the absence of direct data, I can provide estimates based on chemical reasoning and the available SRD-46 data:

| System | Estimated log K₁ (aq, 25 °C) | Reasoning |
|--------|-------------------------------|-----------|
| **MeCN–Fe²⁺** | **≈ −0.5 to 0.5** | MeCN is a weak σ-donor nitrile. Ag⁺ gives log K₁ = 0.42; Fe²⁺ is a harder, less π-accepting ion than Ag⁺ and binds nitriles more weakly. |
| **MeCN–Fe³⁺** | **≈ 0 to 1.0** | Fe³⁺ is harder and more electrophilic than Fe²⁺, so slightly stronger binding to the nitrile N lone pair, but still very weak. |
| **DMF–Fe²⁺** | **≈ −0.5 to 0.5** | DMF coordinates through the carbonyl O. As a neutral amide, it is a moderate σ-donor but competes poorly with water. Comparable to or slightly weaker than MeCN binding. |
| **DMF–Fe³⁺** | **≈ 0.5 to 1.5** | Fe³⁺ is a harder acid; the C=O oxygen of DMF is a harder donor than the nitrile N, so DMF–Fe³⁺ should be modestly stronger than MeCN–Fe³⁺. |
| **THF–Fe²⁺** | **≈ −1 to 0** | THF is a very weak ether O-donor. Ethers are among the weakest ligands in aqueous solution; water easily outcompetes THF for Fe²⁺. |
| **THF–Fe³⁺** | **≈ −0.5 to 0.5** | Slightly stronger than Fe²⁺ due to higher charge density, but still negligible in water. |
| **Ethylene glycol–Fe²⁺** | **≈ 0 to 1.0** | Two hydroxyl O-donors provide chelation, but neutral –OH is a weak donor. Lanthanide data show very weak binding; Fe²⁺ should be comparable. |
| **Ethylene glycol–Fe³⁺** | **≈ 1.0 to 2.5** | Fe³⁺ is a strong Lewis acid; the chelate effect of the 5-membered ring with two O-donors gives a modest boost. If deprotonation occurs (glycolate-like), log K could be significantly higher (>4). |

---

## Key Chemistry Insights

1. **All four ligands are neutral, weak donors** that are primarily used as solvents rather than ligands. In aqueous solution, water (itself a good O-donor) competes effectively, keeping log K values near zero or even negative.

2. **Fe³⁺ vs Fe²⁺ trend:** Fe³⁺ (d⁵, high-spin, hard acid) consistently binds harder O/N donors more strongly than Fe²⁺ (d⁶, borderline). Expect Fe³⁺ constants to be ~0.5–1.5 log units higher across all four ligands.

3. **Donor strength ranking** (estimated, in aqueous media): **Ethylene glycol > DMF ≈ MeCN > THF**. Ethylene glycol benefits from the chelate effect; DMF and MeCN are comparable single-site donors; THF is the weakest due to the poor donor ability of ether oxygen.

4. **Caution:** Literature values for these systems often come from *nonaqueous* media (e.g., MeCN as solvent with Fe salts), where the "stability constants" reflect a fundamentally different reference state. The estimates above assume *aqueous* conditions consistent with SRD-46 conventions.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes). Direct Fe data unavailable; estimates based on available data for other metals and chemical reasoning.*

---