"""
Database connection helpers for the four SRD-46 SQLite databases.
"""

import sqlite3
from pathlib import Path
from contextlib import contextmanager
from functools import lru_cache

from workspace_setup import ensure_packaged_file

# Resolve the SRD46_db directory relative to this repo.
_DB_DIR = Path(__file__).absolute().parent.parent.parent / "SRD46_db"

CARDS_DB = _DB_DIR / "srd46_cards.db"
EQUILIBRIUM_DB = _DB_DIR / "srd46_equilibrium_maps.db"
LITERATURE_DB = _DB_DIR / "srd46_literature.db"
FINGERPRINT_DB = _DB_DIR / "srd46_ligand_fingerprints.db"


@lru_cache(maxsize=8)
def _prepare_database(path: Path) -> None:
    """Restore a packaged database once per process before its first use."""
    ensure_packaged_file(path)


def _verify(path: Path) -> str:
    """Restore a packaged database, then return its verified path."""
    if not path.is_file():
        # Permit recovery if a database was removed after an earlier query.
        _prepare_database.cache_clear()
    _prepare_database(path)
    if not path.is_file():
        raise FileNotFoundError(f"Database not found: {path}")
    return str(path)


@contextmanager
def get_cards_db():
    """Context manager for the primary cards database."""
    conn = sqlite3.connect(_verify(CARDS_DB))
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


@contextmanager
def get_equilibrium_db():
    """Context manager for the equilibrium maps database."""
    conn = sqlite3.connect(_verify(EQUILIBRIUM_DB))
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


@contextmanager
def get_literature_db():
    """Context manager for the full literature catalog database."""
    conn = sqlite3.connect(_verify(LITERATURE_DB))
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


@contextmanager
def attach_all_dbs():
    """
    Open the cards database as the primary connection and ATTACH
    the equilibrium and literature databases for cross-DB queries.
    """
    conn = sqlite3.connect(_verify(CARDS_DB))
    conn.row_factory = sqlite3.Row
    try:
        conn.execute("ATTACH DATABASE ? AS eqdb", (_verify(EQUILIBRIUM_DB),))
        conn.execute("ATTACH DATABASE ? AS litdb", (_verify(LITERATURE_DB),))
        yield conn
    finally:
        conn.close()
