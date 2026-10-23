# Signet: Project Brief

> Drop this whole file into Claude Code at the root of a new working directory.
> Ask it to register/generate the repo with RepoScaffold, then generate the backlog
> from the Roadmap section. Do not invent RepoScaffold flags. Read RepoScaffold's
> own docs/CLI help first and use the real ones.
>
> **Companion tool:** `Marquee` (inside name `Ptah`) makes event posters. Signet is
> upstream of it and does not make posters. See Section 11.

---

## 0. Names

Two layers, per ET convention: plain names outward, mythology inward.

### Naming discipline (binding)

**Internal names appear ONLY in planning docs under `/docs`.** They must never appear in
`/src`, in CLI commands, in config keys, in trace stage ids, in skill names, in file names,
or in anything a user or another tool sees.

| Surface | Uses |
|---|---|
| `/docs` planning docs | mythology names, freely. That is what they are for. |
| CLI | `signet <verb>`. Always. |
| `/src` modules | role names: `director.py`, `designer.py`, `critic.py` |
| trace stage ids | `director`, `designer`, `renderer`, `critic`, `gate` |
| `.claude/skills/` | role names: `director/`, `designer/`, `critic/` |

The mythology is a thinking tool and a naming convention for humans. It is not an API.

**Outside name: Signet.** A signet ring stamps a mark that says whose this is. That is the
entire product.

**Inside name: Ren** (planning docs only; the CLI is `signet`). In Egyptian thought the *ren* is the name, one of
the parts of the soul, and a thing only truly exists while its name is spoken and
preserved. A tool that creates an identity and then guards it unchanged forever is exactly
that idea. Three letters on a command line.

| Stage | Name | Why |
|---|---|---|
| Intake | **client-intake** | Collects client facts. No mythology, it does no judging. |
| Director | **Hu** | The divine utterance, the spoken word that brings a thing into being. Pairs with Marquee's Sia (perception) by design. |
| Mark-maker | **Sokar** | Patron of the Memphite craftsmen and metalworkers. Cuts the actual form. |
| Registry check | **Wedjat** | The Eye. Recognizes what it has seen before. |
| Critic | **Anubis** | Weighs the heart against the feather. Distinct from Ma'at, who *is* the standard rather than the one who weighs. |
| Human gate | **Meat Gate** | You. Same name as in Marquee, deliberately. It is one pattern across the ecosystem, not a per-repo joke. |

---

## 1. What Signet is

A **client-scoped identity system generator**. It produces three things, which are really
one thing at increasing levels of completeness:

1. A **mark** (logo) as vector artwork
2. A **lockup set** (mark plus wordmark, in the arrangements a client actually needs)
3. A **brand kit** (the above, plus palette, type, usage rules, exports, and a machine
   record downstream tools consume)

Clients are DJs, venues, and anything else. Today that is FFXIV in-game venues paid in gil.
The architecture should not care.

**The core bet, same as Marquee:** separate judgment from execution. Judgment stages are
LLM agents. Execution stages are deterministic tools with no creative latitude.

**The core constraint, unlike Marquee:** see the next section, because getting this
backwards will produce a portfolio where every client's logo is visibly from the same
generator.

---

## 2. The two-axis uniqueness rule

This is the single most important idea in this document.

|  | Marquee | Signet |
|---|---|---|
| Across runs for the same subject | must differ | **must be identical** |
| Across different subjects | (n/a) | **must differ** |
| Memory of prior work | **forbidden** | **required** |

Marquee solves sameness by *forgetting*. Signet cannot. A brand that changes every time you
run the tool is not a brand. So Signet needs two separate mechanisms:

### 2.1 Divergence across clients: the registry, not good intentions

Signet **must** read every mark it has ever produced, and is required to avoid resembling
them. This is the exact inversion of Marquee's Section 4 statelessness contract. Do not
copy that contract into this repo.

The strong version, which is mechanical rather than aspirational: **the deck draw excludes
constraint tuples already present in the registry.** Hu cannot propose a territory built on
a tuple another client already owns, because the tuple is not in the available pool. That is
a guarantee. Asking an LLM to "be original" is not.

### 2.2 Permanence within a client: sealing

Once a kit is approved, `signet seal <client>` freezes it: content-hashes every artifact and
writes the hash into the registry. After sealing, the kit is immutable.

Changing a sealed kit requires `signet revise <client> --reason "<why>"`, which creates
`v2` as a **new** registry entry rather than mutating `v1`. Version history is append-only.
There is no path that silently changes a delivered mark.

---

## 3. The pipeline

```
  client discovery (interactive)
        |
        v
  [client-intake] .......... facts, constraints, hard requirements --> brief.json
        |
        v
  [Hu] Director ......... draws from decks MINUS registry-used tuples
        |                  --> 3 identity territories
        v
  [Wedjat] .............. territory-level similarity screen (cheap, pre-work)
        |
        v
  [MEAT GATE] ........... you pick a territory
        |
        v
  [Sokar] Mark-maker .... authors SVG paths directly --> mark.svg
        |
        v
  [Wedjat] .............. mark-level similarity screen against the full registry
        |
        v
  [Anubis] Critic ....... 16px, mono, reversed, on-noise --> critique.jsonl
        |                                                    |
        +----------------- revise loop (cheap, vector) ------+
        |
        v
  [MEAT GATE] ........... approve
        |
        v
  signet seal .............. hash, register, export the kit
```

### 3.1 client-intake: facts only

Produces `clients/<id>/brief.json`. Collects: legal/display name, what they do, who the
audience is, hard requirements (must contain a crescent, must work on a dark Discord
banner, must read at Twitch avatar size), hard exclusions, existing assets to honor or
replace, and deliverable scope.

Does not propose visual ideas. Its opinions would anchor Hu.

### 3.2 Hu: Director, judgment

- Reads `decks/identity.jsonl`, **minus every tuple already claimed in the registry**.
- Draws a tuple. Proposes exactly **3 identity territories**, genuinely different from each
  other, not three variations.
- Each territory states: `construction`, `mark_type`, `era_reference`, `feeling`,
  `color_logic`, the idea in one sentence, and `why_this_client` (one sentence tying it to
  the brief, not to Hu's taste).
- Emits `clients/<id>/territories.jsonl`.
- Does not draw. Does not write SVG. Does not pick.

### 3.3 Sokar: Mark-maker, judgment expressed as vector

- Authors `mark.svg` **directly as SVG source**. Paths, not prompts.
- Constraints that are not negotiable:
  - single compound path or a small number of named paths, no stray groups
  - no gradients, no filters, no blend modes, no embedded raster, in the primary mark
  - `viewBox` normalized, geometry centered, no transform soup
  - the mark must survive being flattened to one color, because that is how it will be
    used half the time
- Also produces the lockups, the wordmark, and the reversed variants.
- **Diffusion is used for moodboarding only, never for the delivered mark.** See Section 7.

### 3.4 Wedjat: Registry check, deterministic plus judgment

Runs twice. Cheap at territory level, thorough at mark level.

Mechanical signals, all computed, no LLM required:

- perceptual hash of the mark rendered at 256px, flattened to one color
- structural descriptors: aspect ratio, silhouette compactness, counter count, stroke-count
  estimate, symmetry axis, corner-vs-curve ratio
- declared tuple overlap with existing registry entries
- palette distance and type-stack overlap

Then a judgment pass over anything the numbers flag, because two marks can share a hash and
read completely differently, and vice versa.

Emits `clients/<id>/similarity.jsonl`. Any `blocker` finding stops the run at the Meat Gate.

**This is a check against your own registry. It is not a trademark search and must never be
described as one, in the code, the docs, or the output.**

### 3.5 Anubis: Critic, judgment

Weighs the mark against the standard. Checks, in order:

1. **16px legibility.** Render at favicon size. Is it still the same shape?
2. **Single-color survival.** Flatten to black. Then to white on black. Does it hold?
3. **Reversal.** On the client's darkest and lightest brand colors.
4. **Noise.** Over a busy photograph, which is what a Discord banner actually is.
5. **Geometry hygiene.** Stray nodes, unclosed paths, near-duplicate points, off-grid
   anchors, non-uniform scaling baked into a transform.
6. **Territory delivery.** Does the mark deliver its chosen territory's `feeling` and
   `construction`, or did it drift to a default?
7. **Drift.** Has this converged on generic-logo defaults? Circle containing an abstract
   swoosh, geometric sans in all caps with wide tracking, a gradient doing the work the
   form should be doing.

Emits `clients/<id>/critique.jsonl`, one finding per line, each with a concrete proposed
fix. **Anubis may not praise.**

### 3.6 Meat Gate: the human

Same pattern as Marquee. `signet gate <client>` presents the current state and blocks.
Decisions append to `clients/<id>/decisions.jsonl`:

| Decision | Effect |
|---|---|
| `approve` | Proceeds to seal. |
| `revise` | Back to Sokar with selected critique findings. Cheap, vector only. |
| `redirect` | Back to Hu for new territories. Discards the current mark. |
| `reject` | Kills the run. Nothing enters the registry. |

Nothing is sealed, exported, or registered without an `approve` on record.

---

## 4. The brand kit deliverable

`signet export <client>` produces `clients/<id>/kit/`:

```
kit/
  logo/
    mark.svg                    primary, full color
    mark-mono-black.svg
    mark-mono-white.svg
    wordmark.svg
    lockup-horizontal.svg
    lockup-stacked.svg
  raster/
    mark-{2048,1024,512,256}.png    transparent
    mark-favicon-{32,16}.png
    lockup-horizontal-2048.png
  print/
    marks.pdf                   vector PDF, all variants
  color/
    palette.json                roles, hex, RGB, contrast pairs
    swatches.svg
  type/
    fonts/                      the actual OFL font files
    OFL.txt                     per family
    type-spec.json              families, axes, roles, sizes, tracking
  brand.json                    the machine record. see 5.3.
  GUIDE.pdf                     one page: clear space, min size, misuse
  MANIFEST.json                 content hashes of everything above
```

**Every font shipped in a kit is SIL OFL.** This is why that decision was made, and it is
what makes handing a client a folder legally uncomplicated. Nothing else enters `type/`.

---

## 5. Data contracts

JSONL for all pipeline I/O, per the ET standard. JSON/TOML for hand-edited config.

### 5.1 `$SIGNET_HOME/registry/marks.jsonl`: append-only, the heart of the tool

One line per sealed mark version:

```json
{"client":"club-moon","version":1,"sealed":"2026-08-27","tuple":{"construction":"negative space","mark_type":"lettermark","era_reference":"art deco","feeling":"mythic","color_logic":"monochrome plus one accent"},"svg":"clients/club-moon/kit/logo/mark.svg","phash":"...","descriptors":{"aspect":1.0,"compactness":0.61,"counters":2,"symmetry":"vertical"},"palette":["#..."],"type_stack":["Fraunces","IBM Plex Sans"],"content_hash":"sha256:...","superseded_by":null}
```

Append-only. Never rewritten. `signet revise` adds a line and sets `superseded_by` on the old
one; it does not delete.

### 5.2 `decks/identity.jsonl`

Axes for Hu. Tuples already claimed in the registry are removed from the pool before the
draw.

### 5.3 `brand.json`: the handoff to Marquee

Signet's output is Marquee's input. `signet export <client> --to-venue` emits a record matching
Marquee's venue schema (its Section 5.1), so a Marquee repo can consume it directly with no
code shared between the two projects.

---

## 6. Repo layout

```
signet/
  pyproject.toml
  signet.toml               # config: providers, export presets, thresholds
  CLAUDE.md                 # RepoScaffold-managed
  AGENTS.md                 # RepoScaffold-managed
  docs/                     # single source of truth
    QUICKSTART.md
    ARCHITECTURE.md
    ADR/
  src/signet/
    cli.py
    config.py
    trace.py                # zoom-tagged JSONL events
    clients.py              # client folder lifecycle
    contracts/              # pydantic: brief, territory, critique, registry entry
    agents/
      base.py               # provider-agnostic
      director.py
      markmaker.py
      critic.py
    vector/
      svg.py                # parse, normalize, validate, hygiene checks
      render.py             # resvg/cairosvg -> PNG for inspection
      trace_raster.py       # vtracer/potrace, for raster inputs only
    $SIGNET_HOME/registry/
      store.py              # append-only jsonl
      fingerprint.py        # phash + structural descriptors
      screen.py             # similarity screen
    kit/
      export.py             # the kit builder
      guide.py              # GUIDE.pdf
  decks/
    identity.jsonl
    typefaces.jsonl
  clients/                  # per-client work. gitignored or private.
  $SIGNET_HOME/registry/
    marks.jsonl             # committed. this is the asset.
  .claude/skills/
    client-intake/SKILL.md
    director/SKILL.md
    markmaker/SKILL.md
    critic/SKILL.md
  tests/
```

---

## 7. Non-goals and invariants

1. **No diffusion-generated delivered marks.** Diffusion output is mushy, artifact-ridden,
   unreproducible, not scalable, and cannot be color-separated. Use it for moodboards only.
   The delivered mark is authored SVG.
2. **No raster-only deliverable.** Ever. If something must come back from raster, it goes
   through `vtracer`/`potrace` and then gets cleaned, and Anubis checks the geometry.
3. **No silent revision of a sealed kit.** `signet revise` creates a new version with a stated
   reason, or nothing changes.
4. **No mark ships without a Wedjat pass and an `approve` decision on record.**
5. **Wedjat is not a trademark search.** Do not imply otherwise anywhere in the product.
6. **Signet does not make posters.** That is Marquee. See Section 11.
7. **Anubis does not compliment.** Findings only.
8. **Only OFL fonts enter a kit.**

---

## 8. Roadmap

### M0: Skeleton
- `#1` Poetry project, typer CLI shell, `signet --version`, `signet doctor`
- `#2` Config layer: `signet.toml`
- `#3` Pydantic contracts: brief, territory, critique, registry entry, brand record
- `#4` Client lifecycle: `signet new <client>` creates `clients/<id>/`
- `#5` `trace.py` zoom-tagged JSONL emitter

### M1: Vector before intelligence
Build the deterministic half first, exactly as in Marquee. All testable with no LLM.
- `#6` SVG parse, normalize, validate: viewBox, centering, transform flattening
- `#7` SVG geometry hygiene checks: stray nodes, unclosed paths, duplicate points
- `#8` Render pipeline: resvg or cairosvg to PNG at arbitrary size, mono flattening,
  reversal, over-noise composite
- `#9` Font stack: `decks/typefaces.jsonl`, `signet fonts sync`, OFL manifest, and a test
  asserting every bundled font is OFL
- `#10` Fingerprinting: phash plus structural descriptors, with a test corpus of
  deliberately similar and deliberately different marks
- `#11` Append-only registry store, `signet registry list|show`
- `#12` Wedjat mechanical screen (no LLM), threshold config
- `#13` Kit exporter: all variants, all formats, MANIFEST hashes
- `#14` `signet seal` and `signet revise` with version chaining
- **M1 exit criteria:** you can hand-author a `mark.svg`, run `signet seal` and `signet export`,
  and get a complete client-ready kit with zero LLM involvement.

### M2: Judgment
- `#15` Provider-agnostic agent base
- `#16` `decks/identity.jsonl` plus the registry-excluding draw
- `#17` Hu: 3 territories, `territories.jsonl`, `signet direct`
- `#18` Sokar: territory to `mark.svg` plus lockups, `signet draw`
- `#19` Anubis: the 7 checks, `critique.jsonl`, `signet critique`
- `#20` Wedjat judgment pass over mechanically-flagged pairs
- `#21` `signet revise-loop`: critique to Sokar to render, until clean or max iterations

### M3: Intake and gate
- `#22` `signet intake`: conversational client discovery to `brief.json`
- `#23` Meat Gate: `signet gate`, four decisions, `decisions.jsonl`, and a test asserting no
  seal or export path exists without an `approve`
- `#24` The four Claude Code skill files in `.claude/skills/`

### M4: Ship a real kit
- `#25` End-to-end run producing a complete kit for one real client
- `#26` `GUIDE.pdf` generator: clear space, min size, misuse examples
- `#27` `signet export --to-venue` handoff, verified by a Marquee repo consuming it
- `#28` `docs/QUICKSTART.md` verified from scratch on a clean box

### M5: Scale
- `#29` Backfill the registry with your existing marks so Wedjat knows about them
- `#30` `signet audit`: re-screen the whole registry for collisions after threshold changes
- `#31` Moodboard mode: diffusion for territory exploration only, clearly separated from
  the mark pipeline
- `#32` Optional local preview panel

---

## 9. Kickoff prompt for Claude Code

```
Read signet-brief.md in full before doing anything else.

1. Read RepoScaffold's own docs and CLI help. Use its real commands, do not invent flags.
   Create or register this repo with RepoScaffold under the name "signet".
2. Generate the backlog from the Roadmap section, one ticket per line item, grouped by
   milestone. 32 tickets, M0 through M5.
3. Write /docs/ARCHITECTURE.md from Sections 2, 3, 4 and 5. Write ADRs for:
   - the two-axis uniqueness rule and why Signet must remember while Marquee must forget
   - sealing and append-only versioning
   - authored SVG rather than diffusion for delivered marks
   - vector pipeline before the agent layer
4. Scaffold the repo layout in Section 6. Empty modules with docstrings and signatures
   are fine at this stage.
5. Implement M0 only. Stop and check in before starting M1.

The skill files in .claude/skills/ and the decks in decks/ are already written.
Do not regenerate them. Wire the code to read them.

Do not start on the agent layer. M1 is the deterministic vector and registry work.
Do not import Marquee, CueQueue, or any other component. This repo stands alone.
```

---

## 10. Settled decisions

| Question | Decision |
|---|---|
| Outside name | Signet |
| Inside name / CLI | Ren / `signet` |
| ET integration | Standalone always. Composition from outside via CLI |
| Relationship to Marquee | Upstream. Data contract only, no shared code |
| Shared plumbing | A RepoScaffold-managed standard, not a shared library |
| Delivered mark format | Authored SVG. Never diffusion output |
| Memory | Required and append-only. The opposite of Marquee |
| Fonts | SIL OFL only, shipped inside the kit |
| Build order | Vector and registry (M1) before agents (M2) |

---

## 11. Scope boundary: Signet does not make posters

Marquee (inside name `Ptah`) owns event posters, fliers, and per-event promo assets. It is
a **separate repo** with a separate spec.

Why they are split, recorded so it does not get relitigated:

- **Opposite memory architecture.** Marquee forbids reading past runs and enforces it in the
  file layer. Signet requires reading every mark ever made. One codebase cannot hold both
  rules without violating one by accident.
- **Opposite output format.** Signet is vector SVG. Marquee is raster Pillow compositing.
  The renderers share nothing.
- **Different cadence.** Marquee runs weekly. Signet runs a few times a year per client.

**The handoff.** Signet is upstream:

```
signet export club-moon --to-venue > ../marquee/venues/club-moon.json
```

Marquee then places the mark and never regenerates, redraws, recolors, or restyles it. Its
`logo_lock` invariant exists specifically to protect what Signet produced.

**Shared plumbing** (config layer, trace JSONL, agent provider interface, run lifecycle,
font deck) is duplicated *by RepoScaffold template*, not by a shared library. Fix it once in
RepoScaffold, propagate to both repos, keep zero runtime coupling. That is what RepoScaffold
is for.

### M3 additions: the interview layer

- `#33` `<cli> init`: create the home dir, seed defaults, first-run questions
- `#34` Config resolution: shipped defaults, user overrides, CLI flags. `decks show`
  prints the merged view with provenance per value
- `#35` `venue new` / `client new` interview skill, writes a validated record
- `#36` `venue edit <id>`: re-interview named fields only
- `#37` `decks extend`: propose-only, with redundancy checking against existing axis values
- `#38` Gate approval required before any proposed deck value is written

---

## Data layer

`data/` sits beside `src/`, and its location comes from config. Nothing in `src/` ever
hardcodes a path.

```
Signet/
  src/signet/
  data/
    decks/      constraints.jsonl, typefaces.jsonl   COMMITTED
    registry/   your marks. THE asset.                          not committed
    assets/     logos, wordmarks                      not committed
  signet.toml
```

```toml
[paths]
data_dir = "./data"
work_dir = "~/.local/state/signet/work"
```

**Why the config indirection matters.** `data_dir` defaults to `./data` for a dev checkout,
but it is just a value. Point it at a shared drive, a synced folder, or a per-machine
location and nothing in the code changes. That is also what keeps this working when the
package is installed rather than run from a checkout, and it is the reason `data/` is a
sibling of `src/` rather than living inside the package.

**What is committed and what is not.** `data/decks/` is committed: those are the shipped
defaults that make a fresh install work, and they define tool behavior. Everything else
under `data/` is user data. Someone doing logos for a bakery ships with working decks and none of your marks.

**Durability.** Uncommitted does not mean unprotected. Whatever syncs this folder versions
those files. The only real hazard is `git clean -x`, which deletes ignored files. Plain
`git clean -fd` respects `.gitignore` and leaves them alone.

### User data is generated, not hand-authored

Hand-editing stays possible. It is not the expected path.

```
<cli> init              first run. creates data_dir, seeds decks, asks a few questions
<cli> venue new         interviews you, writes a venue record
<cli> venue edit <id>   re-asks only the fields you name
<cli> decks extend      proposes new axis values for your kind of events
```

The park organizer answers "Riverside Park", "no website", "no logo" and has a working venue
record without ever seeing JSON. You answer with a Goblet plot number. Same interview, same
schema, different outcome.

Each interview is a separate single-purpose skill.

**One hard rule on `decks extend`.** The deck is the entire anti-sameness mechanism, and an
LLM asked to invent creative axes produces clustered, overlapping values. "Art deco" and
"1920s glamour" as two entries silently halves your real variety. So it may only propose,
never append; every proposal is checked for redundancy against existing values on that axis;
and you approve each one at the gate. A tool that helpfully extends its own deck will
helpfully destroy the thing that makes it work.
