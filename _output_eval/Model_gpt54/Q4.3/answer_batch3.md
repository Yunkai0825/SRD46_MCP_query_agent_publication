I’m sorry, but I can’t complete a reliable comparison from the SRD-46 data retrieved so far.

| Issue | What happened |
|---|---|
| Ligand resolution | I could identify **Cu²⁺ (metal_41)**, **Ni²⁺ (metal_112)**, **Zn²⁺ (metal_208)** and **ammonia (ligand_10103)**, but I did **not successfully resolve the SRD-46 ligand ID for unsubstituted ethylenediamine (en)**. |
| Stability retrieval | The direct **ammonia** stability search returned **no results** under the attempted filters. |
| en search quality | A broader “ethylenediamine”-text stability search returned many **false positives** (IDA, substituted diamines, etc.), not the unsubstituted en system needed for your comparison. |

So I would be inventing or guessing if I gave numerical values for  
\(\Delta = \log K_{\mathrm{en}} - 2\log K_{\mathrm{NH_3}}\).

What I *can* say, cautiously, is the expected chemistry hypothesis:

| Metal ion | Expected qualitative chelate effect trend | Plausible reason |
|---|---|---|
| Ni²⁺ | likely relatively strong | octahedral **d⁸** ion often gains substantial stabilization with bidentate N donors; favorable preorganization and LFSE contributions |
| Cu²⁺ | may differ from Ni²⁺, sometimes enhanced or irregular | **Jahn–Teller distortion** in **d⁹** Cu²⁺ changes the balance between stepwise monodentate binding and chelation |
| Zn²⁺ | often somewhat smaller/less distinctive | **d¹⁰** ion has no LFSE, so differences are more dominated by entropy, size match, and donor-field effects |

So the magnitude of the chelate effect is **not expected to be perfectly constant across metals**; it likely **varies**, because the chelate effect is not purely entropic in practice. It also reflects metal-dependent factors such as **LFSE, Jahn–Teller distortion, ionic radius/geometry, and metal–nitrogen bond covalency**.

If you want, I can continue with a fresh SRD-46 workflow aimed specifically at:
1. resolving the exact **ethylenediamine** ligand entry,
2. finding matched **25 °C aqueous** constants for **Cu²⁺/Ni²⁺/Zn²⁺** with **NH₃** and **en**,
3. and then computing the chelate-effect values in a table.

---