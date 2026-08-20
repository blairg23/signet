"""Client folder lifecycle.

Unlike Marquee's runs.py, this module deliberately has no cross-client
isolation guard -- the registry (ADR 0001) requires reading every mark ever
produced across all clients. Isolating client folders from each other would
break the uniqueness guarantee, not protect it.
"""

from __future__ import annotations

import re
from pathlib import Path

from signet.config import Config

_SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify(value: str) -> str:
    return _SLUG_RE.sub("-", value.lower()).strip("-")


def new_client(client_id: str, *, config: Config) -> Path:
    """Create clients/<id>/ for a new client and return its path."""
    slug = slugify(client_id)
    client_dir = config.data_dir.parent / "clients" / slug
    client_dir.mkdir(parents=True, exist_ok=False)
    return client_dir


def client_dir(client_id: str, *, config: Config) -> Path:
    """Return the (possibly non-existent) path for an existing client."""
    return config.data_dir.parent / "clients" / slugify(client_id)
