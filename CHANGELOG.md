# Release notes

## v1.0.0(R) â€” 21 September 2026

This revision makes the SRD-46 query workspace reproducible to install and supplies its current database snapshot without Git LFS pointers.

- Added a Python 3.13.13 environment specification, exact direct and transitive dependency versions in `uv.lock`, one root hash-pinned `requirements.txt`, and an installed-version snapshot and validation report.
- Packaged the current cards database into one ordinary ZIP and fingerprints database into two ordinary ZIPs, all below 95 MiB. The smaller databases remain original SQLite files in Git.
- Added automatic, atomic startup restoration with part and full-file SHA-256 verification before browser, query, or MCP database access. Existing original files are preserved.
- Added publication checks for oversized files, pointer placeholders, staged Git content, and lossless package contents.
- Ported maintenance fixes for empty API replies, non-retryable authentication failures, environment-based API identity/endpoint configuration, and MCP startup with redirected stderr.
- Corrected ligand-similarity input validation and filtering, and retained citation/evidence identifiers during result compaction.
- Corrected evaluation database overrides and custom-root claims-cache isolation; standalone evaluation also restores missing packaged databases.
- Refreshed the README, installation instructions, database inventory/counts, citation metadata, and environment provenance documentation.

Validation included restoration from absent database files followed by a real MCP copper query; all 18 MCP tools registered. The locked environment check, 33 focused offline regression checks, browser database-override tests, and archive size/pointer checks passed. All scientific output artifacts are retained.

The environment was newly validated on 21 September 2026. Its lock and version snapshot do not establish the package versions used for the original experiments. The supplied database snapshot may differ from historical runs; benchmark outputs were not regenerated.

The public release name is `v1.0.0(R)`; Python environment metadata uses `1.0.0.post1` for PEP 440 compatibility.

## v1.0.0 â€” July 2026

Initial publication of the SRD-46 MCP query agent, browser, databases, and saved evaluation artifacts. Superseded by `v1.0.0(R)`.
