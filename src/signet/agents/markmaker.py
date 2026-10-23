"""Mark-maker: territory to mark.svg plus lockups, authored directly as SVG
source. M2 (#18). Not implemented yet.
"""

from __future__ import annotations

from pathlib import Path

from signet.agents.base import Agent
from signet.contracts import Territory


class MarkMaker(Agent):
    def run(self, *, territory: Territory, out_dir: Path) -> Path:  # type: ignore[override]
        raise NotImplementedError("MarkMaker is implemented in M2")
