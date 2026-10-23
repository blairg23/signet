"""Brand-record contract -- the `signet export <client> --to-venue` handoff.

Matches Marquee's Venue contract field-for-field (docs/signet-brief.md 5.3)
so a Marquee repo can consume it directly, with no code shared between the
two projects.
"""

from __future__ import annotations

from pydantic import BaseModel


class BrandRecord(BaseModel):
    id: str
    name: str
    world: str = ""
    datacenter: str = ""
    location: str = ""
    carrd: str = ""
    discord: str = ""
    logo: str = ""
    logo_lock: bool = True
    regular_night: str = ""
    brand_notes: str = ""
    safe_margin_pct: float = 5.0
