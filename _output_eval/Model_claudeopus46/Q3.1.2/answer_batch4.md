## Best Amino Acid for Selective Cu²⁺ Complexation over Ni²⁺ at pH 7

### **Winner: L-Histidine (ligand_5898)**

Based on the SRD-46 database, histidine is the optimal amino acid ligand for selectively complexing Cu²⁺ in the presence of Ni²⁺ at pH 7. The database confirms rich data coverage for both systems: **24 VLM entries for Cu²⁺–histidine** and **18 VLM entries for Ni²⁺–histidine**, with multiple stoichiometries (ML, ML₂, ML₃, MHL, MHL₂, etc.).

### Why Histidine Wins at pH 7

**1. The Imidazole Advantage**

Histidine is unique among the 20 common amino acids: it offers **tridentate** coordination (α-amino N, carboxylate O, imidazole N). The critical factor is the imidazole pKₐ ≈ 6.05 (from SRD-46 pKₐ data), meaning at pH 7 the imidazole is **~90% deprotonated and available for metal binding**. No other standard amino acid has a side-chain donor with a pKₐ so perfectly positioned for pH 7.

**2. Protonation Kills the Competition**

| Ligand | Key pKₐ values (SRD-46) | Status at pH 7 |
|--------|------------------------|----------------|
| **Histidine** | 6.05 (imidazole), 9.1 (NH₃⁺) | Imidazole ~90% free; tridentate binding available |
| Glycine | 2.33 (COOH), 9.57 (NH₃⁺) | NH₂ >99% protonated; only bidentate, weak conditional K |
| Alanine | 2.33 (COOH), 9.71 (NH₃⁺) | NH₂ >99% protonated; same problem as glycine |
| Cysteine | 8.18 (SH), 10.3 (NH₃⁺) | Thiol ~94% protonated; also oxidises readily with Cu²⁺ |
| Aspartic acid | 1.95, 3.71, 9.66 | Carboxylates free but NH₂ protonated; weaker N-donor effect |
| Serine | 2.16 (COOH), 9.05 (NH₃⁺) | NH₂ >99% protonated; hydroxyl is a poor donor |
| Proline | 1.89 (COOH), 10.46 (NH) | NH >99.9% protonated at pH 7 |
| Lysine | 2.15, 9.15, 10.66 | Both amines protonated; very weak conditional binding |

For simple α-amino acids like glycine and alanine, the α-amino group (pKₐ ≈ 9.5–10.5) is overwhelmingly protonated at pH 7, so the **conditional (effective) stability constants** collapse for both Cu²⁺ and Ni²⁺. The raw Δlog K may be large, but the absolute binding is too weak to be useful.

**3. Irving-Williams Amplification with Nitrogen Donors**

The Irving-Williams series guarantees Cu²⁺ > Ni²⁺ for all these ligands, but the Cu/Ni selectivity gap is **amplified by nitrogen-rich coordination**. Cu²⁺ with its d⁹ Jahn-Teller distortion has an outsized preference for planar N-donor arrangements. Histidine's tridentate N₂O donor set plays directly into this preference.

### Estimated Selectivity

| Complex | log K (Cu²⁺) | log K (Ni²⁺) | Selectivity ratio K_Cu/K_Ni |
|---------|-------------|-------------|---------------------------|
| M–Histidine (ML) | ~10.2 | ~8.7 | ~30× |
| M–(Histidine)₂ (ML₂) | ~18.3 | ~15.5 | ~600× |
| M–Glycine (ML) | ~8.2 | ~5.8 | ~250× (but conditional K is tiny at pH 7) |

While glycine shows a larger *intrinsic* Δlog K, its conditional stability at pH 7 is orders of magnitude lower than histidine's because the amino group is protonated. Histidine maintains **both high absolute binding AND good selectivity** at pH 7.

### Practical Considerations

- **Cysteine** might seem attractive (very high Cu²⁺ affinity via thiolate), but Cu²⁺ catalyses cysteine oxidation to cystine, making it impractical and leading to reduction of Cu²⁺ to Cu⁺.
- **Histidine** is air-stable, water-soluble, commercially available, and biologically benign — exactly why nature uses histidine residues as the primary Cu²⁺-binding motif in proteins (e.g., albumin's ATCUN motif).

### Conclusion

**L-Histidine** provides the best selectivity for Cu²⁺ over Ni²⁺ at pH 7 among amino acid ligands. Its imidazole side chain (pKₐ ≈ 6.05) is uniquely positioned to be deprotonated and coordination-ready at physiological pH, giving Cu²⁺ a ~30-fold advantage over Ni²⁺ for ML and ~600-fold for ML₂ complexes under practical conditions.

*Source: NIST Standard Reference Database 46 (SRD-46) — Critically Selected Stability Constants of Metal Complexes*

---