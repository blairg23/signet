# Kickoff

Paste this into Claude Code, launched from the repo root.

---

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

## After M0 lands

M1 before M2, same rule as Marquee. The vector pipeline, the fingerprinting, and the
registry are all testable with zero LLM involvement, and they are the parts that actually
have to be correct.

**M1 exit criteria:** you can hand-author a `mark.svg`, run `signet seal` and `signet export`, and
get a complete client-ready kit with no agent in the loop.

Ticket `#10` (fingerprinting) deserves more care than its size suggests. Build the test
corpus of deliberately-similar and deliberately-different marks first, then tune the
thresholds against it. If Wedjat's numbers are wrong, the one guarantee this tool offers is
worthless, and you will not notice until you have shipped two clients the same logo.
