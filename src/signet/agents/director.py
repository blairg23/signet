"""Director: draws from decks minus registry-used tuples, proposes 3
territories. M2 (#17). Not implemented yet.
"""

from __future__ import annotations

from signet.agents.base import Agent
from signet.contracts import Brief, Territory


class Director(Agent):
    def run(self, *, brief: Brief) -> list[Territory]:  # type: ignore[override]
        raise NotImplementedError("Director is implemented in M2")
