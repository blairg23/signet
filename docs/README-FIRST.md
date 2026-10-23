# Read this first

Starter kit, not a repo. Unzip into an empty folder and point Claude Code at it. Spec, data
files, and agent skills only. The code is what Claude Code writes.

**This is the companion to `marquee`. Separate repo, separate spec, no shared code.**

## What is in here

```
signet-brief.md               the spec. everything is in here.
KICKOFF.md                    the prompt to paste into Claude Code
.claude/skills/
  client-intake/SKILL.md           client discovery, proposes nothing
  director/SKILL.md          draws an unclaimed tuple, proposes 3 territories
  markmaker/SKILL.md      authors the SVG by hand, no diffusion
  critic/SKILL.md        weighs it at 16px / mono / reversed / on noise
decks/
  identity.jsonl              the territory deck. tuples get consumed permanently.
  typefaces.jsonl             OFL-only, same deck Marquee uses
$SIGNET_HOME/registry/
  marks.jsonl                 empty, append-only. THIS IS THE ASSET. commit it.
clients/                      per-client work
docs/                         empty. Claude Code writes ARCHITECTURE.md and the ADRs here.
```

## The one idea that makes this work

**Marquee forgets. Signet remembers.**

Marquee guarantees every poster is different by having no memory at all. Signet cannot do
that, because a brand that changes every run is not a brand. So it runs two mechanisms
instead:

1. **Across clients: the deck draw excludes tuples already in the registry.** Hu literally
   cannot propose a direction another client owns, because it is not in the pool. That is a
   guarantee, not an instruction.
2. **Within a client: sealing.** Once approved, the kit is content-hashed and frozen.
   Changing it requires an explicit `signet revise` that creates a new version and states why.
   Nothing silently mutates a delivered mark.

If you ever find yourself letting Hu reuse a tuple because it "fits this client better,"
you have thrown away the only structural guarantee the tool provides.

## Before the first real run

1. **Backfill the registry.** Ticket `#29`. Your existing marks need to be in
   `$SIGNET_HOME/registry/marks.jsonl` or Wedjat will happily let you redraw one of them.
2. **Build the fingerprint test corpus early.** Ticket `#10`. Pairs of marks you know are
   too similar, pairs you know are fine. Tune thresholds against it. Untested thresholds
   mean the guarantee is decorative.
3. **Decide where `clients/` lives.** It holds client work. Gitignore it or keep the repo
   private. `$SIGNET_HOME/registry/marks.jsonl` should be committed either way.

## One thing to be clear about with clients

Wedjat checks a mark against **your own registry**. It is not a trademark search and must
never be described as one. If this ever moves past gil and into real money, that gap is
someone else's job to close, not this tool's.
