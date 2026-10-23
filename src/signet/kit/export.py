"""Kit exporter: all variants, all formats, MANIFEST hashes. M1 (#13).

See docs/signet-brief.md Section 4 for the full kit/ layout. Not implemented
yet.
"""

from __future__ import annotations

from pathlib import Path


def export_kit(client_dir: Path, out_dir: Path) -> Path:
    """Build the complete client-ready kit/ deliverable."""
    raise NotImplementedError("kit export is implemented in M1")
