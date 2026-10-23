# Architecture

Signet is a client-scoped identity system generator. It produces a mark
(logo), a lockup set, and a brand kit -- three levels of completeness of the
same underlying identity.

## The two-axis uniqueness rule

The single most important idea in this codebase:

|  | Across runs, same subject | Across different subjects |
|---|---|---|
| Marquee | must differ | n/a |
| Signet | **must be identical** | **must differ** |

Marquee solves sameness by forgetting. Signet cannot -- a brand that changes
every time you run the tool is not a brand. So Signet needs two separate,
independent mechanisms. See ADR 0001.

### Divergence across clients: the registry, not good intentions

Signet reads every mark it has ever produced and is required to avoid
resembling them. The deck draw mechanically **excludes constraint tuples
already present in the registry** -- the Director cannot propose a territory
built on a tuple another client already owns, because the tuple is not in the
available pool. That is a guarantee, not an instruction to "be original."

### Permanence within a client: sealing

Once a kit is approved, `signet seal <client>` freezes it: content-hashes
every artifact and writes the hash into the registry. After sealing, the kit
is immutable. Changing a sealed kit requires `signet revise <client> --reason
"<why>"`, which creates a new version as a **new** registry entry rather than
mutating the old one. See ADR 0002.

## The pipeline

```
  client discovery (interactive)
        |
        v
  client-intake .......... facts, constraints, hard requirements --> brief.json
        |
        v
  Director ......... draws from decks MINUS registry-used tuples
        |                  --> 3 identity territories
        v
  Registry check .............. territory-level similarity screen (cheap, pre-work)
        |
        v
  MEAT GATE ........... you pick a territory
        |
        v
  Mark-maker .... authors SVG paths directly --> mark.svg
        |
        v
  Registry check .............. mark-level similarity screen against the full registry
        |
        v
  Critic ....... 16px, mono, reversed, on-noise --> critique.jsonl
        |                                                    |
        +----------------- revise loop (cheap, vector) ------+
        |
        v
  MEAT GATE ........... approve
        |
        v
  signet seal .............. hash, register, export the kit
```

### client-intake: facts only

Produces `clients/<id>/brief.json`. Collects legal/display name, audience,
hard requirements and exclusions, existing assets, and deliverable scope.
Does not propose visual ideas -- its opinions would anchor the Director.

### Director: judgment

Reads `decks/identity.jsonl` minus every tuple already claimed in the
registry, draws a tuple, proposes exactly 3 identity territories, genuinely
different from each other. Emits `clients/<id>/territories.jsonl`. Does not
draw the mark, does not pick.

### Mark-maker: judgment expressed as vector

Authors `mark.svg` directly as SVG source -- paths, not prompts. Constraints:
single compound path or a small number of named paths, no gradients/filters/
blend modes/embedded raster, normalized viewBox, must survive being flattened
to one color. Diffusion is used for moodboarding only, never for the
delivered mark. See ADR 0003.

### Registry check: deterministic plus judgment

Runs twice (territory-level, cheap; mark-level, thorough). Mechanical
signals: perceptual hash at 256px flattened to one color, structural
descriptors (aspect ratio, compactness, counter count, stroke-count,
symmetry, corner-vs-curve ratio), declared tuple overlap, palette distance,
type-stack overlap. Then a judgment pass over anything the numbers flag.
This is a check against the registry, not a trademark search, and must never
be described as one.

### Critic: judgment

Weighs the mark against the standard: 16px legibility, single-color
survival, reversal on brand colors, noise (busy photograph), geometry
hygiene, territory delivery, and drift toward generic-logo defaults. Emits
`clients/<id>/critique.jsonl`. May not praise.

### Meat Gate: the human

`signet gate <client>` presents the current state and blocks. Decisions
append to `clients/<id>/decisions.jsonl`:

| Decision | Effect |
|---|---|
| `approve` | Proceeds to seal. |
| `revise` | Back to Mark-maker with selected findings. Cheap, vector only. |
| `redirect` | Back to Director for new territories. Discards the mark. |
| `reject` | Kills the run. Nothing enters the registry. |

Nothing is sealed, exported, or registered without an `approve` on record.

## Data contracts

JSONL for pipeline I/O, JSON/TOML for hand-edited config.

- `clients/<id>/brief.json` -- intake output
- `clients/<id>/territories.jsonl` -- Director output, one territory per line
- `clients/<id>/similarity.jsonl` -- registry-check findings; any `blocker`
  stops the run at the Meat Gate
- `clients/<id>/critique.jsonl` -- Critic findings, one per line
- `clients/<id>/decisions.jsonl` -- Meat Gate decisions
- `registry/marks.jsonl` -- append-only, one line per sealed mark version.
  Never rewritten; `signet revise` adds a line and sets `superseded_by` on
  the old one, never deletes.
- `decks/identity.jsonl` -- axes for the Director, tuples already claimed in
  the registry removed from the pool before the draw
- `brand.json` -- the handoff to Marquee: `signet export <client> --to-venue`
  emits a record matching Marquee's venue schema, so a Marquee repo can
  consume it with zero shared code

## The brand kit deliverable

`signet export <client>` produces `clients/<id>/kit/`: `logo/` (mark, mono
variants, wordmark, lockups, all SVG), `raster/` (PNG at multiple sizes plus
favicons), `print/` (vector PDF), `color/` (palette JSON, swatches), `type/`
(the actual OFL font files plus license text), `brand.json` (the machine
record), `GUIDE.pdf` (clear space, min size, misuse), and `MANIFEST.json`
(content hashes of everything above). Every font shipped is SIL OFL.

## See also

- `docs/signet-brief.md` -- the full project brief (source of truth)
- `docs/ADR/0001-two-axis-uniqueness.md`
- `docs/ADR/0002-sealing-and-versioning.md`
- `docs/ADR/0003-authored-svg-not-diffusion.md`
- `docs/ADR/0004-vector-before-agents.md`
