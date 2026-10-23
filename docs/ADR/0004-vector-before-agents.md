# ADR 0004: Vector and registry pipeline before the agent layer

## Status

Accepted

## Context

Signet's judgment stages (Director, Mark-maker, Critic) depend on
infrastructure that has nothing to do with LLMs: SVG parsing and hygiene
checks, a rendering pipeline for inspection, perceptual-hash fingerprinting,
an append-only registry store, a similarity screen, a kit exporter, and
sealing/versioning. None of that requires a model call to build or to test.

## Decision

M1 builds the entire deterministic half first -- SVG parse/normalize/
validate, geometry hygiene checks, the render pipeline (resvg/cairosvg to
PNG, mono flattening, reversal, over-noise composite), the font stack, phash
plus structural-descriptor fingerprinting, the append-only registry store,
the mechanical similarity screen, the kit exporter, and `seal`/`revise` with
version chaining. M1's exit criteria: hand-author a `mark.svg`, run `signet
seal` and `signet export`, and get a complete client-ready kit with zero LLM
involvement. Only after that does M2 add the Director, Mark-maker, and
Critic agents on top.

## Consequences

- Every M1 component is fully testable without a model in the loop, which
  is both faster to build and far more reliable to test than anything
  depending on LLM output.
- The registry and similarity-screening mechanism that ADR 0001's uniqueness
  guarantee depends on exists and is proven correct before any agent ever
  writes to it, so the core promise of the product is verified independently
  of agent behavior.
- The agent layer becomes optional in the same sense Marquee's is after its
  own M1: a human can hand-author a mark and get a complete, sealed,
  exported kit through the tool with no LLM involved at all. The agents make
  the workflow faster and less manual, not load-bearing for correctness.
