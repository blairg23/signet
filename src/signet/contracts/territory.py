"""Director output contract -- one line per territory in territories.jsonl."""

from __future__ import annotations

from pydantic import BaseModel


class IdentityTuple(BaseModel):
    construction: str
    mark_type: str
    era_reference: str
    feeling: str
    color_logic: str


class Territory(BaseModel):
    idea: str
    why_this_client: str
    tuple: IdentityTuple
