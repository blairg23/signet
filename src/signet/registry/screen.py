"""Wedjat-role mechanical similarity screen. M1 (#12). Not implemented yet.

Not a trademark search -- must never be described as one. See
docs/signet-brief.md 3.4.
"""

from __future__ import annotations

from pathlib import Path

from signet.contracts import Critique, RegistryEntry


def screen(candidate_svg: Path, *, registry: list[RegistryEntry]) -> Critique:
    """Compare candidate_svg against every registry entry mechanically."""
    raise NotImplementedError("similarity screen is implemented in M1")
