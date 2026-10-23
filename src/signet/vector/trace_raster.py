"""vtracer/potrace: raster input to vector, for raster inputs only.

Never used for a delivered mark -- see ADR 0003. Not implemented yet.
"""

from __future__ import annotations

from pathlib import Path


def trace_raster(raster_path: Path, out_path: Path) -> Path:
    """Trace a raster image to SVG for cleanup, not delivery."""
    raise NotImplementedError("trace_raster is implemented in M1")
