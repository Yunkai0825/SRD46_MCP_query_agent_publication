# Packaged database files

The current checkout contains two database files larger than GitHub's **100 MiB per-file limit**. They are distributed as ordinary ZIP archives below 95 MiB, with no Git LFS pointers. The original SQLite files are restored locally before use; none of their contents are regenerated or omitted. GitHub's limit applies to the stored archive file, not its expanded contents ([GitHub documentation](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)).

## What is included

| Installed database | Original bytes | Distribution in `SRD46_db/` | Archive size |
|---|---:|---|---:|
| `srd46_cards.db` | 197,775,360 | `srd46_cards.db.zip` | 22.11 MiB |
| `srd46_ligand_fingerprints.db` | 763,731,968 | `srd46_ligand_fingerprints.db.part001-of-002.zip` | 88.73 MiB |
| Same fingerprints database, continued | — | `srd46_ligand_fingerprints.db.part002-of-002.zip` | 61.51 MiB |
| `srd46_equilibrium_maps.db` | 29,376,512 | Original SQLite file | — |
| `srd46_literature.db` | 46,178,304 | Original SQLite file | — |

The cards ZIP contains the complete `srd46_cards.db`. The fingerprint ZIPs contain twelve ordered byte chunks in `srd46_ligand_fingerprints.db.__chunks__/`: chunks 1–7 in the first archive and 8–12 in the second. Each archive opens independently in Windows File Explorer. Individual chunks are not usable SQLite files; startup joins them into the original database.

[packaged_files.json](./packaged_files.json) records the target paths, exact original sizes, SHA-256 hashes, and chunk order. These packages preserve the databases supplied in the current workspace. They do not establish which database revision was used for older benchmark results. Saved results in `_output/` and `_output_eval/` were left in their existing layout; none exceeded the size limit.

## First launch

After installing the locked dependencies, run the application normally:

```sh
uv run --locked python API_SRD46_Query_UI.py
# Or start the MCP server:
uv run --locked python main.py
```

The application restores missing packaged files, verifies every chunk and the reconstructed file, then continues startup. This also covers the direct browser entry point, query command, terminal runtime, and database-tool connections. A browser configured with a complete external `SRD46_DB_DIR` uses that directory directly.

Keep all three ZIPs in `SRD46_db/` and keep the manifest at the repository root. Allow about **1 GiB of additional disk space** for the restored files. Installation uses only Python's standard library. It needs no model request, database generation, or additional download.

To restore without starting a service, or to hash-check the installed files:

```sh
python workspace_setup.py --verify
```

Normal launches check existing file sizes and reuse them. `--verify` also checks their hashes. A real file with a wrong size or hash is preserved and reported; inspect or back it up before moving it aside to reinstall. Missing/corrupt ZIP parts stop startup with a diagnostic naming the affected asset. New files are installed atomically only after verification; simultaneous launches coordinate their restoration. Diagnostics go to stderr so MCP stdout remains a valid protocol stream.

## Publication checks

The installed cards and fingerprint databases are ignored by their exact paths. Their ZIPs and manifest are publication files. Smaller databases and all other retained files are ordinary Git blobs. `.gitattributes` disables Git LFS filtering for new content; this does not rewrite older Git history.

Run the read-only audit before staging:

```sh
python scripts/check_publication.py --verify-packages
```

It checks every tracked or nonignored untracked file, including saved outputs, for the size limit and pointer placeholders. Package verification streams and hashes every part without extracting files. Ignored virtual environments, scratch files, and restored large databases are local assets and are not publication candidates.

After reviewing and staging the intended changes, also run:

```sh
python scripts/check_publication.py --staged
```

This checks the actual staged contents; old pointer entries must be replaced by their original file bytes or by the packaged representation. These commands do not commit or push anything. When updating a packaged database, replace the matching ZIPs and manifest together and rerun both the package and environment checks; do not simply edit the recorded checksum.
