"""SVG parse, normalize, validate: viewBox, centering, transform flattening,
and geometry hygiene checks. M1 (#6, #7). Not implemented yet.
"""

from __future__ import annotations

from pathlib import Path


def normalize(svg_path: Path) -> Path:
    """Normalize viewBox, center geometry, flatten transforms."""
    raise NotImplementedError("svg normalize is implemented in M1")


def hygiene_check(svg_path: Path) -> list[str]:
    """Return a list of geometry hygiene problems (empty if clean)."""
    raise NotImplementedError("svg hygiene_check is implemented in M1")
