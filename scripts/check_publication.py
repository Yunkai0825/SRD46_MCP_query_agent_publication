"""Read-only checks of publication file sizes, original contents, and packages."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import stat
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 100 * 1024 * 1024
LFS_HEADER = b"version https://git-lfs.github.com/spec/v1"
MANIFEST = "packaged_files.json"


def git(root: Path, *args: str, data: bytes | None = None) -> bytes:
    result = subprocess.run(["git", *args], cwd=root, input=data,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace").strip())
    return result.stdout


def io_path(path: Path) -> Path:
    """Support long Windows paths while preserving Git's ordinary cwd."""
    value = str(path.absolute())
    if os.name != "nt" or value.startswith("\\\\?\\"):
        return Path(value)
    if value.startswith("\\\\"):
        return Path("\\\\?\\UNC\\" + value[2:])
    return Path("\\\\?\\" + value)


def relative_name(value: object) -> str:
    if not isinstance(value, str) or not value or "\\" in value or ":" in value:
        raise ValueError(f"Invalid relative path: {value!r}")
    if PurePosixPath(value).is_absolute() or any(p in {"", ".", ".."} for p in value.split("/")):
        raise ValueError(f"Invalid relative path: {value!r}")
    return value


def byte_size(value: object) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f"Invalid byte size: {value!r}")
    return value


def sha256(value: object) -> str:
    if not isinstance(value, str) or len(value) != 64:
        raise ValueError(f"Invalid SHA-256: {value!r}")
    if any(c not in "0123456789abcdefABCDEF" for c in value):
        raise ValueError(f"Invalid SHA-256: {value!r}")
    return value.lower()


def inspect_file(root: Path, name: str) -> tuple[str, int | None, list[str]]:
    try:
        path = io_path(root / name)
        info = path.lstat()
        if stat.S_ISLNK(info.st_mode):
            return name, None, [f"Symbolic link instead of original file: {name}"]
        if not stat.S_ISREG(info.st_mode):
            return name, None, []
        errors = []
        if info.st_size > MAX_BYTES:
            errors.append(f"File exceeds 100 MiB ({info.st_size:,} bytes): {name}")
        with path.open("rb") as stream:
            if stream.read(len(LFS_HEADER)) == LFS_HEADER:
                errors.append(f"Git LFS pointer instead of original file: {name}")
        return name, info.st_size, errors
    except FileNotFoundError:
        return name, None, []  # Deleted tracked files are absent from the next tree.
    except OSError as exc:
        return name, None, [f"Cannot inspect {name}: {exc}"]


def worktree(root: Path) -> tuple[dict[str, int], list[str], bytes | None]:
    raw = git(root, "ls-files", "--cached", "--others", "--exclude-standard", "-z")
    names = sorted({os.fsdecode(n) for n in raw.split(b"\0") if n})
    files, errors = {}, []
    with ThreadPoolExecutor(max_workers=min(16, os.cpu_count() or 4)) as pool:
        for name, size, issues in pool.map(lambda name: inspect_file(root, name), names):
            errors.extend(issues)
            if size is not None:
                files[name] = size
    for row in git(root, "ls-files", "--stage", "-z").split(b"\0"):
        if row.startswith(b"160000 "):
            name = os.fsdecode(row.split(b"\t", 1)[1])
            errors.append(f"Git submodule instead of original files: {name}")
    path = io_path(root / MANIFEST)
    manifest = path.read_bytes() if path.is_file() else None
    if manifest is not None and MANIFEST not in files:
        errors.append(f"Package manifest excluded from publication: {MANIFEST}")
    return files, errors, manifest


def staged(root: Path) -> tuple[dict[str, int], list[str], bytes | None]:
    errors, by_oid = [], {}
    manifest_oid = None
    for row in git(root, "ls-files", "--stage", "-z").split(b"\0"):
        if not row:
            continue
        metadata, raw_name = row.split(b"\t", 1)
        mode, raw_oid, stage = metadata.split()
        name = os.fsdecode(raw_name)
        if stage != b"0":
            errors.append(f"Unresolved merge entry: {name}")
            continue
        if mode in {b"120000", b"160000"}:
            errors.append(f"Symbolic link or submodule instead of original files: {name}")
            continue
        oid = raw_oid.decode("ascii")
        by_oid.setdefault(oid, []).append(name)
        if name == MANIFEST:
            manifest_oid = oid
    files = {}
    if by_oid:
        metadata = git(root, "cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize)",
                       data=("\n".join(by_oid) + "\n").encode("ascii"))
        candidates = []
        for row in metadata.splitlines():
            fields = row.decode("ascii").split()
            if len(fields) != 3 or fields[1] != "blob":
                errors.append(f"Cannot inspect staged object: {row!r}")
                continue
            oid, _, raw_size = fields
            size = int(raw_size)
            for name in by_oid[oid]:
                files[name] = size
                if size > MAX_BYTES:
                    errors.append(f"Staged file exceeds 100 MiB ({size:,} bytes): {name}")
            # Standard Git LFS pointers are at most 1 KiB; allow extra metadata.
            if len(LFS_HEADER) <= size <= 4096:
                candidates.append(oid)
        if candidates:
            payload = git(root, "cat-file", "--batch", data=("\n".join(candidates) + "\n").encode("ascii"))
            offset = 0
            for oid in candidates:
                end = payload.index(b"\n", offset)
                size = int(payload[offset:end].split()[-1])
                content = payload[end + 1:end + 1 + size]
                if content.startswith(LFS_HEADER):
                    errors.extend(f"Staged Git LFS pointer: {name}" for name in by_oid[oid])
                offset = end + 1 + size + 1
    manifest = git(root, "cat-file", "blob", manifest_oid) if manifest_oid else None
    return files, errors, manifest


def packages(root: Path, files: dict[str, int], raw: bytes | None,
             verify: bool) -> tuple[int, list[str]]:
    if raw is None:
        return 0, [f"Missing {MANIFEST}; cannot verify packages."] if verify else []
    try:
        manifest = json.loads(raw)
        if not isinstance(manifest, dict) or manifest.get("version") != 1:
            raise ValueError("Expected version 1 manifest")
        entries = manifest.get("files")
        if not isinstance(entries, list):
            raise ValueError("Manifest 'files' must be a list")
    except (ValueError, UnicodeError) as exc:
        return 0, [f"Invalid {MANIFEST}: {exc}"]
    errors, seen = [], set()
    for entry in entries:
        name = "<invalid entry>"
        try:
            if not isinstance(entry, dict):
                raise ValueError("File entry must be an object")
            name = relative_name(entry.get("path"))
            if name in seen:
                raise ValueError("Duplicate installation path")
            seen.add(name)
            size, digest = byte_size(entry.get("size")), sha256(entry.get("sha256"))
            parts = entry.get("parts") if "parts" in entry else [{
                "archive": entry.get("archive"),
                "member": entry.get("member", PurePosixPath(name).name),
                "size": size, "sha256": digest,
            }]
            if not isinstance(parts, list) or not parts:
                raise ValueError("Expected at least one package part")
            total_hash, total_size, seen_parts = hashlib.sha256(), 0, set()
            for part in parts:
                if not isinstance(part, dict):
                    raise ValueError("Package part must be an object")
                archive, member = relative_name(part.get("archive")), relative_name(part.get("member"))
                part_size, part_digest = byte_size(part.get("size")), sha256(part.get("sha256"))
                if (archive, member) in seen_parts:
                    raise ValueError(f"Duplicate member: {archive}:{member}")
                seen_parts.add((archive, member))
                if not archive.lower().endswith(".zip"):
                    raise ValueError(f"Package must be an ordinary .zip file: {archive}")
                if archive not in files:
                    raise ValueError(f"Package missing or excluded from publication: {archive}")
                if files[archive] > MAX_BYTES:
                    raise ValueError(f"Package exceeds 100 MiB: {archive}")
                total_size += part_size
                if verify:
                    with zipfile.ZipFile(io_path(root / archive)) as zipped:
                        matches = [info for info in zipped.infolist() if info.filename == member]
                        if len(matches) != 1:
                            raise ValueError(f"Expected exactly one {member!r} in {archive}")
                        info = matches[0]
                        if info.file_size != part_size:
                            raise ValueError(f"Member size differs from manifest: {archive}:{member}")
                        read_size, part_hash = 0, hashlib.sha256()
                        with zipped.open(info) as stream:
                            while chunk := stream.read(1024 * 1024):
                                read_size += len(chunk)
                                part_hash.update(chunk)
                                total_hash.update(chunk)
                        if read_size != part_size or part_hash.hexdigest() != part_digest:
                            raise ValueError(f"Member content differs from manifest: {archive}:{member}")
            if total_size != size:
                raise ValueError(f"Parts total {total_size:,} bytes; expected {size:,}")
            if verify and total_hash.hexdigest() != digest:
                raise ValueError("Reconstructed SHA-256 differs from manifest")
        except (OSError, ValueError, KeyError, RuntimeError, zipfile.BadZipFile) as exc:
            errors.append(f"Package {name}: {exc}")
    return len(entries), errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT,
                        help="Repository directory (default: this script's repository).")
    parser.add_argument("--staged", action="store_true",
                        help="Check the complete staged tree, including actual Git blob contents.")
    parser.add_argument("--verify-packages", action="store_true",
                        help="Stream worktree ZIP members to check part and reconstructed SHA-256; never extract.")
    args = parser.parse_args(argv)
    if args.staged and args.verify_packages:
        parser.error("--verify-packages checks worktree archives; run it separately from --staged")
    try:
        root = args.root.resolve()
        files, errors, manifest = staged(root) if args.staged else worktree(root)
        count, package_errors = packages(root, files, manifest, args.verify_packages)
        errors.extend(package_errors)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"Publication check failed: {exc}", file=sys.stderr)
        return 1
    if errors:
        for error in sorted(set(errors)):
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    scope = "staged" if args.staged else "worktree"
    verified = "; package contents verified" if args.verify_packages else ""
    print(f"Publication check passed: {len(files):,} {scope} files, {count} packaged assets; "
          f"no pointers or files over 100 MiB{verified}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
