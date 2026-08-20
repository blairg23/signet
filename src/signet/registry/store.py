"""Append-only registry store: registry/marks.jsonl. M1 (#11).

Never rewritten. `revise` adds a line and sets `superseded_by` on the old
entry -- it does not delete. Not implemented yet. See ADR 0002.
"""

from __future__ import annotations

from pathlib import Path

from signet.contracts import RegistryEntry


def append(entry: RegistryEntry, *, registry_path: Path) -> None:
    """Append a new entry to the registry. Never rewrites an existing line."""
    raise NotImplementedError("registry store is implemented in M1")


def load_all(*, registry_path: Path) -> list[RegistryEntry]:
    """Load every entry ever written to the registry."""
    raise NotImplementedError("registry store is implemented in M1")
