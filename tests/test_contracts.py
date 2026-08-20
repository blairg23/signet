from __future__ import annotations

from signet.contracts import Brief, Critique, CritiqueFinding, RegistryEntry, Territory
from signet.contracts.registry import StructuralDescriptors
from signet.contracts.territory import IdentityTuple


def test_brief_defaults() -> None:
    brief = Brief(client_id="club-moon", display_name="Club Moon")
    assert brief.hard_requirements == []
    assert brief.deliverable_scope == []


def test_territory_round_trip() -> None:
    territory = Territory(
        idea="a crescent built from negative space",
        why_this_client="the venue's whole identity is a moon phase",
        tuple=IdentityTuple(
            construction="negative space",
            mark_type="lettermark",
            era_reference="art deco",
            feeling="mythic",
            color_logic="monochrome plus one accent",
        ),
    )
    assert territory.model_dump()["tuple"]["mark_type"] == "lettermark"


def test_critique_may_be_empty() -> None:
    critique = Critique()
    assert critique.findings == []


def test_critique_finding_shape() -> None:
    finding = CritiqueFinding(
        finding="mark does not survive single-color flatten",
        proposed_fix="remove the gradient fill on the crescent",
    )
    assert "gradient" in finding.proposed_fix


def test_registry_entry_shape() -> None:
    entry = RegistryEntry(
        client="club-moon",
        version=1,
        sealed="",
        tuple=IdentityTuple(
            construction="negative space",
            mark_type="lettermark",
            era_reference="art deco",
            feeling="mythic",
            color_logic="monochrome plus one accent",
        ),
        svg="clients/club-moon/kit/logo/mark.svg",
        phash="deadbeef",
        descriptors=StructuralDescriptors(
            aspect=1.0, compactness=0.61, counters=2, symmetry="vertical"
        ),
        content_hash="sha256:abc",
    )
    assert entry.superseded_by is None
    assert entry.descriptors.counters == 2
