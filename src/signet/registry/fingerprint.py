"""phash plus structural descriptors. M1 (#10). Not implemented yet."""

from __future__ import annotations

from pathlib import Path

from signet.contracts.registry import StructuralDescriptors


def phash(png_path: Path) -> str:
    """Perceptual hash of a mark rendered at 256px, flattened to one color."""
    raise NotImplementedError("phash is implemented in M1")


def structural_descriptors(svg_path: Path) -> StructuralDescriptors:
    """Aspect ratio, compactness, counter count, symmetry axis, etc."""
    raise NotImplementedError("structural_descriptors is implemented in M1")
