# ADR 0001: The two-axis uniqueness rule -- Signet must remember while Marquee must forget

## Status

Accepted

## Context

Signet and Marquee share a core bet: separate judgment from execution. It
would be tempting to also share their memory policy, especially since they
are sibling tools in the same product family with the same pipeline shape.
That temptation is wrong, and getting it backwards produces a portfolio
where every client's logo is visibly from the same generator.

## Decision

Signet's uniqueness requirement runs on two independent axes, and they point
in opposite directions from Marquee:

- **Across runs for the same subject:** a brand must be identical every time
  it is produced. A logo that changes each run is not a brand.
- **Across different subjects:** every client's mark must differ from every
  other client's mark, and from every mark Signet has ever produced.

This is the exact inversion of Marquee's statelessness contract, which
forbids reading past runs and enforces it in the file layer. Signet does the
opposite on purpose: it **must** read every mark it has ever produced via an
append-only registry, and the deck draw for a new client mechanically
excludes constraint tuples already claimed in that registry. Asking an LLM
to "be original" is not a mechanism; excluding the tuple from the available
pool is.

Permanence within a client is a separate mechanism (sealing, see ADR 0002)
from divergence across clients (the registry, this ADR). Both are required
and neither substitutes for the other.

## Consequences

- Do not import Marquee's statelessness contract or its run-isolation guard
  into this repo. They solve the opposite problem.
- The registry is not an optimization or a cache -- it is the entire
  mechanism that makes cross-client divergence a guarantee rather than a
  hope. Losing it is losing the product's core promise.
- One codebase cannot hold both Marquee's and Signet's memory rules without
  violating one of them by accident, which is also why they are separate
  repos with a data-only handoff contract rather than a shared library.
