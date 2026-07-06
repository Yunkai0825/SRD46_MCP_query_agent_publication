# Irving–Williams Series Violations in SRD-46 Data

## The Expected Ordering

The Irving–Williams series predicts that for a given ligand, the stability of divalent first-row transition-metal complexes follows:

**Mn²⁺ < Fe²⁺ < Co²⁺ < Ni²⁺ < Cu²⁺ > Zn²⁺**

## Summary of log K₁ (ML, ~25 °C) Across Six Ligands

| Metal | EDTA | Glycine | Oxalate | Imidazole | 1,10-Phen | Cysteine |
|-------|------|---------|---------|-----------|-----------|----------|
| Mn²⁺ | ~13.9 | ~3.0 | ~3.9 | ~2.0 | ~4.0 | — |
| Fe²⁺ | ~14.3 | ~4.2 | **~3.2** | — | ~6.2 | — |
| Co²⁺ | ~16.3 | ~5.1 | ~4.7 | ~2.7 | ~7.1 | ~9.3 |
| Ni²⁺ | ~18.5 | ~6.0 | ~5.3 | ~3.1 | ~8.7 | ~10.8 |
| Cu²⁺ | ~18.8 | ~8.4 | ~6.3 | ~4.3 | ~9.1 | ~19.5 |
| Zn²⁺ | ~16.5 | ~5.2 | ~4.9 | ~2.6 | ~6.5 | **~10.0** |

*(Source: NIST SRD-46. Values are representative medians; ranges exist across ionic-strength and temperature conditions.)*

## Ligands That Obey the Series Well

**Glycine, imidazole, and 1,10-phenanthroline** all follow the Irving–Williams ordering faithfully. These ligands feature hard or intermediate N/O donors and do not impose unusual geometric constraints — exactly the regime where crystal-field stabilization energy (CFSE) arguments work best.

## Identified Violations

### 1. Oxalate: Fe²⁺ < Mn²⁺ (log K ~3.2 vs ~3.9)
The Irving–Williams series requires Fe²⁺ > Mn²⁺, yet **Fe²⁺–oxalate is less stable than Mn²⁺–oxalate** in the database. This is a clear inversion of the first step in the series.

### 2. EDTA: Ni²⁺ ≈ Cu²⁺ (log K ~18.5 vs ~18.8)
While Cu²⁺ nominally remains higher, the gap is remarkably small (~0.3 log units), and **some individual measurements show Ni²⁺ ≥ Cu²⁺**. The expected Cu²⁺ dominance is nearly erased.

### 3. Cysteine: Zn²⁺ ≈ Ni²⁺ (log K ~10.0 vs ~10.8)
For this thiol-containing amino acid, **Zn²⁺ approaches or matches Ni²⁺**, violating the expected Ni²⁺ > Zn²⁺ ordering. Some measurements show Zn²⁺ > Ni²⁺.

---

## Hypotheses for the Exceptions

| Violation | Proposed Explanation |
|-----------|---------------------|
| **Fe²⁺ < Mn²⁺ (oxalate)** | Oxalate is a hard, oxygen-only donor ligand. Fe²⁺ (d⁶, high-spin) gains minimal CFSE from weak-field O-donors, and its slightly larger effective ionic radius compared to high-spin Mn²⁺ can reduce electrostatic stabilization. Furthermore, Fe²⁺ is redox-labile and may partially oxidize to Fe³⁺ during measurement, leading to artificially low apparent log K values for the divalent state. |
| **Ni²⁺ ≈ Cu²⁺ (EDTA)** | EDTA is a hexadentate ligand that enforces a roughly octahedral coordination geometry. Cu²⁺ (d⁹) normally gains extra stability from Jahn–Teller distortion in tetragonal or square-planar fields, but a **rigid hexadentate cage suppresses this distortion**, reducing Cu²⁺'s usual thermodynamic advantage. Meanwhile, Ni²⁺ (d⁸) achieves maximum octahedral CFSE with all six donors, closing the gap substantially. |
| **Zn²⁺ ≈ Ni²⁺ (cysteine)** | Cysteine provides a soft thiolate sulfur donor. According to **HSAB (Hard–Soft Acid–Base) theory**, Zn²⁺ — a borderline-soft acid — has a much stronger affinity for soft S-donors than Ni²⁺, which behaves as a borderline-hard acid. This soft–soft interaction elevates Zn²⁺ stability beyond what the Irving–Williams series predicts. This is biologically significant: Zn²⁺ preferentially binds cysteine-rich sites in zinc-finger proteins precisely because of this thermodynamic preference. |

---

## Key Takeaway

The Irving–Williams series is an excellent general rule for **hard, monodentate or small chelating ligands** — glycine, imidazole, and 1,10-phenanthroline all obey it faithfully in the SRD-46 data. Violations arise systematically when:

1. **HSAB mismatch** — Soft donors (thiolate S in cysteine) preferentially stabilize Zn²⁺ over Ni²⁺, inverting the tail of the series.
2. **Geometric constraints** — Rigid polydentate ligands like EDTA suppress the Jahn–Teller distortion advantage of Cu²⁺ (d⁹), allowing Ni²⁺ to nearly match it.
3. **Redox complications** — Fe²⁺ is easily oxidized, and with purely hard O-donor ligands like oxalate, its CFSE advantage over Mn²⁺ vanishes, sometimes yielding an apparent inversion.

These exceptions underscore that crystal-field stabilization energy alone does not determine complex stability — ligand geometry, donor-atom softness, and metal redox chemistry all play critical and sometimes dominant roles.

---