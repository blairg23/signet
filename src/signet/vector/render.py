"""resvg/cairosvg -> PNG at arbitrary size, mono flattening, reversal,
over-noise composite. M1 (#8). Not implemented yet.
"""

from __future__ import annotations

from pathlib import Path


def render(svg_path: Path, out_path: Path, *, size: int) -> Path:
    """Render an SVG to a PNG at `size` x `size`."""
    raise NotImplementedError("render is implemented in M1")


def flatten_mono(png_path: Path, *, color: str) -> Path:
    """Flatten a rendered PNG to a single color."""
    raise NotImplementedError("flatten_mono is implemented in M1")
