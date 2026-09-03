# lk-law

Public-facing law office site.

<!-- BEGIN ACCELERATION-MACHINE RULES BLOCK (generated - do not edit by hand) -->

## Rules layer

This repository carries the Acceleration Machine canon rule set as a vendored
bundle. It is loaded by reading this block; nothing else is required.

- **Read `.rules/RULES.md` before doing substantive work here.** It holds the
  non-negotiables and indexes all 40 registered rules by tier
  (4 enforced, 26 active, 10 proposed).
- **Canon rule text lives in `oklawsite-machine/ai-cloud-loader`** under `global-rules/` and `rules/`.
  This repo carries the index and the hashes, never a second copy of the text —
  a second copy would become a second source of truth (CF-05).
- **`.rules/` is generated.** Hand edits fail CI and are overwritten on the next
  sync. Change a rule at canon, then re-sync.

Rule-set signature: `6051c0160d4e4f48b431acc7aa66f31150cec2eceeb85517daf237a99c9b34db`

A session starting in this repo also runs `.claude/hooks/rules-boot.sh`, which
prints the non-negotiables and warns when this bundle has drifted from a canon
clone found on the same disk.

<!-- END ACCELERATION-MACHINE RULES BLOCK -->
