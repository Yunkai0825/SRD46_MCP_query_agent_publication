SRD-46 shows that **DTPA does not have one single binding constant**; the constant is **metal-specific**. The database does identify DTPA as:

| Ligand ID | Ligand name | Formula |
|---|---|---|
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | C14H23N3O10 |

From the retrieved SRD-46 data, I can confirm the **protonation constant(s)** for DTPA and the key point that a true “binding constant” must be tied to a metal ion:

| System | Reaction | Type | Value | T (°C) | I (M) |
|---|---|---:|---:|---:|---:|
| H⁺ + DTPA | [L] + [H] ⇌ [HL] | logK | 10.50 | 25 | 0.1 |
| H⁺ + DTPA | [L] + [H] ⇌ [HL] | logK | 10.79 | 25 | 0.1 |
| H⁺ + DTPA | [L] + [H] ⇌ [HL] | logK | 9.42 | 25 | 0.5 |
| H⁺ + DTPA | [L] + [H] ⇌ [HL] | logK | 9.98 | 25 | 1.0 |

So, if by “binding constant for DTPA” you meant **proton binding**, SRD-46 contains values around **logK ≈ 10–11** for the first protonation step, depending on medium.

If you meant **metal binding**, then the answer must be phrased as **metal–DTPA log β**. In the currently retrieved SRD-46 results, no metal-specific DTPA complex value was yet fetched for ligand_6356, so I should not invent one.  

| Interpretation of “binding constant” | SRD-46 status |
|---|---|
| Protonation of DTPA | Found |
| Metal–DTPA complex formation | Requires specifying the metal |

If you want, I can next pull the SRD-46 **metal-complex stability constant** for a specific ion such as **Ca²⁺, Cu²⁺, Fe³⁺, Zn²⁺, or Gd³⁺**.  
*Source: NIST SRD-46.*

---