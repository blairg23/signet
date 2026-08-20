"""client-intake output contract -- see docs/signet-brief.md 3.1."""

from __future__ import annotations

from pydantic import BaseModel, Field


class Brief(BaseModel):
    client_id: str
    display_name: str
    what_they_do: str = ""
    audience: str = ""
    hard_requirements: list[str] = Field(default_factory=list)
    hard_exclusions: list[str] = Field(default_factory=list)
    existing_assets: list[str] = Field(default_factory=list)
    deliverable_scope: list[str] = Field(default_factory=list)
