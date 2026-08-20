# ADR 0002: Sealing and append-only versioning

## Status

Accepted

## Context

Once a client has a delivered brand mark, that mark needs to stay exactly
what it was delivered as. Software tools that let their own output drift --
even with good intentions, like "cleaning up" a mark's SVG later -- create a
real risk: a client's printed materials, signage, and social presence can
silently diverge from what the tool now considers canonical.

## Decision

`signet seal <client>` freezes an approved kit: every artifact is
content-hashed and the hash is written into the append-only registry
(`registry/marks.jsonl`). After sealing, the kit is immutable in the sense
that matters -- nothing in the tool will silently rewrite it.

Changing a sealed kit requires an explicit `signet revise <client> --reason
"<why>"`. This creates a **new** registry entry (`v2`, `v3`, ...) rather than
mutating the sealed one. The registry itself is append-only: `revise` adds a
new line and sets `superseded_by` on the old entry, and never deletes or
rewrites a prior line.

There is no code path that changes a delivered mark without an explicit,
reasoned `revise` call on record.

## Consequences

- A client's brand history is fully auditable: every version that ever
  existed is still in the registry, with an explicit reason for each
  revision and a clear supersession chain.
- The registry's similarity-screening mechanism (ADR 0001) automatically
  benefits from this: it can distinguish "this client's mark evolved" from
  "this looks like someone else's mark," because versions are chained by
  client rather than silently overwritten.
- The cost is that `revise` is the only path to change anything -- there is
  no quick in-place fix for a typo or a minor tweak. That is deliberate:
  cheap in-place edits are exactly the mechanism that would make "sealed"
  meaningless.
