"""Provider-agnostic agent interface. No vendor SDK belongs in business logic.

M2 (#15). Not implemented yet.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Agent(ABC):
    """Base class every judgment stage (director, markmaker, critic) implements."""

    @abstractmethod
    def run(self, **inputs: Any) -> Any:
        """Execute this agent's judgment step and return its structured output."""
        raise NotImplementedError
