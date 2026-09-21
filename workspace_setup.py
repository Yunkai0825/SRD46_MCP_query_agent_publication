"""Restore missing, Git-sized packaged files without regenerating their contents.

Run ``python workspace_setup.py --verify`` to install missing assets and check
all installed assets. ZIP parts are ordinary independent archives; the manifest
records the order, sizes, and SHA-256 digests of the contained file chunks.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import errno
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import tempfile
import threading
import time
from zipfile import BadZipFile, ZipFile
from zlib import error as ZlibError

ROOT = Path(__file__).absolute().parent
MANIFEST_NAME = "packaged_files.json"
_BUFFER_SIZE = 1024 * 1024
_THREAD_LOCK = threading.RLock()


class AssetRestoreError(RuntimeError):
    """A packaged asset is unavailable or failed validation."""


def _safe_relative(root: Path, value: object, label: str) -> Path:
    if not isinstance(value, str) or not value or any(c in value for c in ("\\", ":", "\0")):
        raise AssetRestoreError(f"Invalid {label} in {MANIFEST_NAME}: {value!r}")
    relative = PurePosixPath(value)
    if relative.is_absolute() or any(part in ("", ".", "..") for part in value.split("/")):
        raise AssetRestoreError(f"Invalid {label} in {MANIFEST_NAME}: {value!r}")
    path = root.joinpath(*relative.parts)
    if not path.resolve().is_relative_to(root.resolve()):
        raise AssetRestoreError(f"Packaged {label} escapes the workspace: {value!r}")
    return path


def _size_digest(record: dict, label: str) -> tuple[int, str]:
    size, digest = record.get("size"), record.get("sha256")
    if isinstance(size, bool) or not isinstance(size, int) or size < 0:
        raise AssetRestoreError(f"Invalid byte count for {label}")
    if not isinstance(digest, str) or re.fullmatch(r"[0-9a-fA-F]{64}", digest) is None:
        raise AssetRestoreError(f"Invalid SHA-256 digest for {label}")
    return size, digest.lower()


def _entries(root: Path) -> list[dict]:
    manifest = root / MANIFEST_NAME
    try:
        data = json.loads(manifest.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as exc:
        raise AssetRestoreError(f"Cannot read {manifest}: {exc}") from exc
    if not isinstance(data, dict) or data.get("version") != 1 or not isinstance(data.get("files"), list):
        raise AssetRestoreError(f"Unsupported or invalid packaged asset manifest: {manifest}")
    entries, targets = [], set()
    for record in data["files"]:
        if not isinstance(record, dict):
            raise AssetRestoreError(f"Invalid asset entry in {manifest}")
        entry = dict(record)
        target = _safe_relative(root, entry.get("path"), "path")
        size, digest = _size_digest(entry, str(target))
        key = os.path.normcase(str(target.resolve()))
        if key in targets:
            raise AssetRestoreError(f"Duplicate packaged target: {target}")
        targets.add(key)
        raw_parts = entry.get("parts")
        if raw_parts is None:
            raw_parts = [{"archive": entry.get("archive"), "member": entry.get("member", target.name),
                          "size": size, "sha256": digest}]
        if not isinstance(raw_parts, list) or not raw_parts:
            raise AssetRestoreError(f"Expected one or more ZIP parts for {target}")
        parts, members = [], set()
        for raw_part in raw_parts:
            if not isinstance(raw_part, dict):
                raise AssetRestoreError(f"Invalid ZIP part for {target}")
            part = dict(raw_part)
            source = _safe_relative(root, part.get("archive"), "archive")
            member = part.get("member")
            _safe_relative(root, member, "member")
            part_size, part_digest = _size_digest(part, f"{source}:{member}")
            if source == target or source.suffix.lower() != ".zip":
                raise AssetRestoreError(f"Invalid ZIP archive for {target}: {source}")
            member_key = (os.path.normcase(str(source.resolve())), member)
            if member_key in members:
                raise AssetRestoreError(f"Repeated ZIP part for {target}: {source}:{member}")
            members.add(member_key)
            part.update(source=source, member=member, size=part_size, sha256=part_digest)
            parts.append(part)
        if sum(part["size"] for part in parts) != size:
            raise AssetRestoreError(f"ZIP part sizes do not sum to the original byte count for {target}")
        entry.update(target=target, size=size, sha256=digest, parts=parts)
        entries.append(entry)
    return entries


def _is_pointer(contents: bytes) -> bool:
    return re.fullmatch(
        rb"version https://git-lfs.github.com/spec/v1\r?\n"
        rb"oid sha256:[0-9a-fA-F]{64}\r?\nsize [0-9]+\r?\n?", contents
    ) is not None


def _existing_state(entry: dict, *, inspect_pointer: bool = True) -> str:
    target = entry["target"]
    if target.is_symlink():
        raise AssetRestoreError(f"Cannot restore over a symbolic link: {target}")
    try:
        metadata = target.stat()
    except FileNotFoundError:
        return "missing"
    if not stat.S_ISREG(metadata.st_mode):
        raise AssetRestoreError(f"Cannot restore over a non-file: {target}")
    if metadata.st_size <= 200:
        if not inspect_pointer:
            return "small"
        # Another restorer may replace a pointer between stat and open. Inspect
        # the opened file and bound the read even if it is now a large database.
        with target.open("rb") as source:
            metadata = os.fstat(source.fileno())
            if _is_pointer(source.read(201)):
                return "pointer"
    if metadata.st_size != entry["size"]:
        raise AssetRestoreError(
            f"Size mismatch for {target}: expected {entry['size']} bytes, found {metadata.st_size}. "
            "The existing file was preserved. Move it aside after checking it, then rerun "
            "python workspace_setup.py."
        )
    return "ready"


def _verify_file(path: Path, entry: dict) -> None:
    digest, size = hashlib.sha256(), 0
    with path.open("rb") as source:
        while chunk := source.read(_BUFFER_SIZE):
            size += len(chunk)
            digest.update(chunk)
    if size != entry["size"] or digest.hexdigest() != entry["sha256"]:
        raise AssetRestoreError(
            f"Size/SHA-256 mismatch for {path}. The existing file was preserved. "
            "Move it aside after checking it, then rerun python workspace_setup.py."
        )


@contextmanager
def _asset_lock(root: Path, entry: dict):
    # Keep the lock filename: removing it could let two waiters lock different
    # inodes. The OS releases the lock even when a process exits unexpectedly.
    lock_dir = _safe_relative(root, "__tmp__/workspace_restore_locks", "lock directory")
    lock_dir.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha256(entry["path"].casefold().encode("utf-8")).hexdigest()
    with (lock_dir / f"{key}.lock").open("a+b") as handle:
        handle.seek(0, os.SEEK_END)
        if handle.tell() == 0:
            handle.write(b"\0")
            handle.flush()
        deadline = time.monotonic() + 1800
        locked = False
        try:
            while not locked:
                try:
                    handle.seek(0)
                    if os.name == "nt":
                        import msvcrt
                        msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
                    else:
                        import fcntl
                        fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                    locked = True
                except OSError as exc:
                    if exc.errno not in (errno.EACCES, errno.EAGAIN, errno.EDEADLK):
                        raise
                    if time.monotonic() >= deadline:
                        raise AssetRestoreError(f"Timed out waiting for another process to restore {entry['path']}") from exc
                    time.sleep(0.1)
            yield
        finally:
            if locked:
                handle.seek(0)
                if os.name == "nt":
                    import msvcrt
                    msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def _publish_missing(temporary: Path, target: Path) -> bool:
    try:
        if os.name == "nt":
            # Windows rename refuses an existing destination.
            os.rename(temporary, target)
        else:
            os.link(temporary, target)
    except FileExistsError:
        return False
    return True


def _restore(root: Path, entry: dict, *, verify: bool = False) -> bool:
    target = entry["target"]
    state = _existing_state(entry, inspect_pointer=False)
    if state == "ready":
        if verify:
            _verify_file(target, entry)
        return False
    with _asset_lock(root, entry):
        state = _existing_state(entry)
        if state == "ready":
            if verify:
                _verify_file(target, entry)
            return False
        for part in entry["parts"]:
            if not part["source"].is_file():
                raise AssetRestoreError(
                    f"Cannot restore {entry['path']}: missing ZIP part {part['archive']}. "
                    "Obtain the complete repository archive set and rerun python workspace_setup.py."
                )
        temporary = None
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            print(f"Restoring packaged file: {entry['path']}", file=sys.stderr)
            digest, count = hashlib.sha256(), 0
            with tempfile.NamedTemporaryFile(
                mode="wb", prefix="." + target.name + ".", suffix=".restore-tmp",
                dir=target.parent, delete=False,
            ) as writer:
                temporary = Path(writer.name)
                for part in entry["parts"]:
                    with ZipFile(part["source"], "r") as archive:
                        matches = [info for info in archive.infolist() if info.filename == part["member"]]
                        if len(matches) != 1:
                            raise AssetRestoreError(f"Expected one {part['member']!r} in {part['source']}; found {len(matches)}")
                        info = matches[0]
                        if (info.is_dir() or stat.S_ISLNK(info.external_attr >> 16)
                                or info.file_size != part["size"] or info.flag_bits & 1):
                            raise AssetRestoreError(f"Invalid ZIP member type, encryption, or size: {part['source']}:{part['member']}")
                        part_digest, part_count = hashlib.sha256(), 0
                        with archive.open(info) as reader:
                            while chunk := reader.read(_BUFFER_SIZE):
                                part_count += len(chunk)
                                count += len(chunk)
                                if part_count > part["size"] or count > entry["size"]:
                                    raise AssetRestoreError(f"Expanded size exceeds the manifest for {entry['path']}")
                                part_digest.update(chunk)
                                digest.update(chunk)
                                writer.write(chunk)
                        if part_count != part["size"] or part_digest.hexdigest() != part["sha256"]:
                            raise AssetRestoreError(f"ZIP part failed size/SHA-256 verification: {part['source']}:{part['member']}")
                writer.flush()
                os.fsync(writer.fileno())
            if count != entry["size"] or digest.hexdigest() != entry["sha256"]:
                raise AssetRestoreError(f"Packaged contents failed size/SHA-256 verification for {entry['path']}")
            # Check again before publication, preserving any independently created
            # real file. Cooperative restorers are serialized by the OS lock.
            state = _existing_state(entry)
            if state == "ready":
                _verify_file(target, entry)
                return False
            if state == "pointer":
                os.replace(temporary, target)
                return True
            installed = _publish_missing(temporary, target)
            if not installed:
                _verify_file(target, entry)
            return installed
        except AssetRestoreError:
            raise
        except (OSError, BadZipFile, EOFError, RuntimeError, ValueError, ZlibError) as exc:
            raise AssetRestoreError(f"Cannot restore {entry['path']}: {exc}") from exc
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)


def ensure_packaged_file(path: str | Path, *, root: str | Path | None = None) -> bool:
    """Restore one manifest asset; custom paths outside the repository are untouched.

    Relative paths are interpreted from the repository root. An unlisted file is
    left to the caller's normal handling. Existing files are size-checked, and
    only missing files or Git LFS pointer placeholders are installed.
    """
    base = Path(root).absolute() if root is not None else ROOT
    target = Path(path)
    if not target.is_absolute():
        target = base / target
    resolved = target.resolve()
    if not resolved.is_relative_to(base.resolve()):
        return False
    with _THREAD_LOCK:
        for entry in _entries(base):
            if entry["target"].resolve() == resolved:
                try:
                    return _restore(base, entry)
                except OSError as exc:
                    raise AssetRestoreError(f"Cannot check packaged file {entry['path']}: {exc}") from exc
    return False


def ensure_packaged_files(*, root: str | Path | None = None, verify: bool = False) -> list[Path]:
    """Restore all missing manifest assets; optionally hash existing assets too.

    Diagnostics go to stderr, preserving stdout for MCP JSON-RPC. Files that
    already have the expected size are untouched unless ``verify`` detects a
    mismatch, which is reported without replacing the existing data.
    """
    base = Path(root).absolute() if root is not None else ROOT
    restored = []
    with _THREAD_LOCK:
        for entry in _entries(base):
            try:
                if _restore(base, entry, verify=verify):
                    restored.append(entry["target"])
            except OSError as exc:
                raise AssetRestoreError(f"Cannot check packaged file {entry['path']}: {exc}") from exc
    return restored


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="also verify SHA-256 of existing packaged assets")
    parser.add_argument("--root", type=Path, help="repository root (defaults to this script's directory)")
    args = parser.parse_args(argv)
    try:
        restored = ensure_packaged_files(root=args.root, verify=args.verify)
    except AssetRestoreError as exc:
        print(f"Workspace self-check failed: {exc}", file=sys.stderr)
        return 1
    print(f"Workspace self-check passed: {len(restored)} file(s) restored" +
          ("; all packaged assets verified." if args.verify else "."))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
