"""Critic (Anubis role): the 7 checks against a mark. M2 (#19).

May not praise -- findings or an empty file only. Not implemented yet.
"""

from __future__ import annotations

from pathlib import Path

from signet.agents.base import Agent
from signet.contracts import Critique, Territory


class Critic(Agent):
    def run(  # type: ignore[override]
        self, *, mark_svg: Path, territory: Territory
    ) -> Critique:
        raise NotImplementedError("Critic is implemented in M2")
