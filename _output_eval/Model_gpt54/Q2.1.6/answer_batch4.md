Thiocyanic acid is present in SRD-46 as **Hydrogen thiocyanate (Thiocyanic acid), ligand_10092**, with acid dissociation to **SCN⁻**. However, in the retrieved SRD-46 data so far, I do **not** yet have the corresponding **Cd(II), Pb(II), and Hg(II) stability constants with SCN⁻**, so I cannot give a database-backed numeric ranking without another stability lookup.

From the SRD-46 results currently retrieved, I can state:

| Ligand in SRD-46 | ligand_id | HxL form | pKa-related entry |
|---|---:|---|---:|
| Hydrogen thiocyanate (Thiocyanic acid) | ligand_10092 | HL | -1.1 |

To answer your ranking question rigorously, the needed next SRD-46 step is to query **search_stability** for **Cd²⁺, Pb²⁺, and Hg²⁺ with ligand_10092/SCN⁻**, restricted to **1:1 ML log K** at matched conditions.

Chemically, for a soft donor like **SCN⁻**, you would generally expect **Hg²⁺** to show the strongest affinity among these soft/borderline-soft metals, but I’m **not labeling that as the SRD-46 ranking yet** because the actual log K values have not been retrieved.  
**Source:** NIST SRD-46.

---