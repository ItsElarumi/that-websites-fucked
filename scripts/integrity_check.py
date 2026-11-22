#!/usr/bin/env python3

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

MANIFEST = Path("integrity/SHA256SUMS.json")


def repository_root():
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=True,
    )
    return Path(result.stdout.strip())


def tracked_files(root):
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=root,
        capture_output=True,
        check=True,
    )

    paths = [
        Path(path.decode())
        for path in result.stdout.split(b"\0")
        if path
    ]

    return sorted(
        path for path in paths
        if path != MANIFEST
    )


def sha256_file(path):
    digest = hashlib.sha256()

    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)

    return digest.hexdigest()


def create_manifest(root):
    entries = {}

    for relative_path in tracked_files(root):
        full_path = root / relative_path

        if not full_path.is_file():
            print(f"ERROR: Cannot read tracked file: {relative_path}")
            return 1

        entries[relative_path.as_posix()] = sha256_file(full_path)

    manifest = {
        "algorithm": "SHA-256",
        "files": entries,
    }

    destination = root / MANIFEST
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Integrity manifest written: {MANIFEST}")
    print(f"Files fingerprinted: {len(entries)}")
    print("Keep the manifest committed alongside the files it records.")
    return 0


def check_manifest(root):
    manifest_path = root / MANIFEST

    if not manifest_path.is_file():
        print("ERROR: No integrity manifest found.")
        print("Create one first with: python scripts/integrity_check.py write")
        return 1

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"ERROR: Cannot read manifest: {error}")
        return 1

    if manifest.get("algorithm") != "SHA-256":
        print("ERROR: Unsupported or invalid hash algorithm.")
        return 1

    expected = manifest.get("files")

    if not isinstance(expected, dict):
        print("ERROR: Invalid manifest file list.")
        return 1

    actual = {}
    missing = []

    for relative_path in tracked_files(root):
        full_path = root / relative_path

        if not full_path.is_file():
            missing.append(relative_path.as_posix())
            continue

        actual[relative_path.as_posix()] = sha256_file(full_path)

    modified = sorted(
        name for name in expected.keys() & actual.keys()
        if expected[name] != actual[name]
    )

    unrecorded = sorted(actual.keys() - expected.keys())
    no_longer_tracked = sorted(expected.keys() - actual.keys())

    if not (modified or missing or unrecorded or no_longer_tracked):
        print("PASS: All recorded file hashes match.")
        print(f"Verified files: {len(actual)}")
        return 0

    print("INTEGRITY CHECK FAILED")

    for name in modified:
        print(f"MODIFIED: {name}")

    for name in missing:
        print(f"MISSING: {name}")

    for name in unrecorded:
        print(f"UNRECORDED TRACKED FILE: {name}")

    for name in no_longer_tracked:
        print(f"NO LONGER TRACKED: {name}")

    print("\nReview every change before updating the manifest.")
    return 1


def main():
    parser = argparse.ArgumentParser(
        description="Check SHA-256 fingerprints of tracked investigation files."
    )
    parser.add_argument(
        "action",
        choices=["write", "check"],
        help="Write a new manifest or verify existing fingerprints.",
    )
    args = parser.parse_args()

    try:
        root = repository_root()
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("ERROR: Run this script inside the Git repository.")
        return 1

    if args.action == "write":
        return create_manifest(root)

    return check_manifest(root)


if __name__ == "__main__":
    sys.exit(main())
