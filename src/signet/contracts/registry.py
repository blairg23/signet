"""Registry entry contract -- one line per sealed mark version in
registry/marks.jsonl. Append-only; see docs/signet-brief.md 5.1 and ADR 0002.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from signet.contracts.territory import IdentityTuple

__all__ = ["IdentityTuple", "RegistryEntry", "StructuralDescriptors"]


class StructuralDescriptors(BaseModel):
    aspect: float
    compactness: float
    counters: int
    symmetry: str


class RegistryEntry(BaseModel):
    client: str
    version: int
    sealed: str
    tuple: IdentityTuple
    svg: str
    phash: str
    descriptors: StructuralDescriptors
    palette: list[str] = Field(default_factory=list)
    type_stack: list[str] = Field(default_factory=list)
    content_hash: str
    superseded_by: int | None = None
