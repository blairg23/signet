# ADR 0003: Authored SVG, never diffusion output, for the delivered mark

## Status

Accepted

## Context

Diffusion models are the obvious tool to reach for when generating visual
content, and Marquee (Signet's sibling) leans on one heavily for background
art. Logos are a fundamentally different kind of artifact: they must scale
from a favicon to a billboard, survive being flattened to one color,
color-separate cleanly for print, and remain pixel-stable forever once
delivered (see ADR 0002). Diffusion output is mushy at logo scale,
artifact-ridden on close inspection, unreproducible run to run, and cannot
be scaled or color-separated the way a logo needs to be.

## Decision

The delivered mark is always authored SVG -- vector paths, produced directly
by the Mark-maker stage, never diffusion output. Constraints on that SVG are
not negotiable: a single compound path or a small number of named paths, no
gradients/filters/blend modes/embedded raster in the primary mark, a
normalized viewBox with centered geometry, and the mark must survive being
flattened to one color, because that is how it will be used a good fraction
of the time.

Diffusion is not banned outright -- it has a real, narrow role in
moodboarding during territory exploration (M5, #31), clearly separated from
the mark pipeline and never touching the delivered artifact. If a raster
input must come back into the vector pipeline (e.g. an existing logo being
redrawn), it goes through `vtracer`/`potrace` and then gets cleaned, with
the Critic checking the resulting geometry same as any authored mark.

## Consequences

- A one-shot "generate me a logo" flow is explicitly not the product. The
  realistic pipeline is an agent authoring SVG paths directly for geometric
  marks, which is a harder problem than prompting a diffusion model, and
  that difficulty is accepted as the cost of a mark that actually works as
  a logo.
- The registry's fingerprinting and similarity screen (ADR 0001) can rely on
  clean vector geometry rather than needing to handle raster artifacts as a
  first-class case.
- No diffusion-generated delivered marks, ever -- this is a non-goal listed
  explicitly in the brief and enforced by construction: the export pipeline
  only ever reads from `mark.svg`, which is never diffusion output.
