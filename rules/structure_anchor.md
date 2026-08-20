# RULE-STRUCT anchor

Status: active repo anchor
Date: 2026-08-20
Canonical source: `oklawsite-machine/ai-cloud-loader/global-rules/RULE-STRUCT.md`
Design capture: `oklawsite-machine/ai-cloud-loader/architecture/acceleration-machine/structure-canon-and-obsidian-ui-20260820.md`
Status of the canon: PROPOSED / NOT SELF-CERTIFIED (RULE-NSRA) / PENDING_EXTERNAL_REVIEW
Scope: this repository

## Anchor

Every directory declares **which layer it is** and **who owns the truth in it**.

- Layers: `ROUTING` (`00_map/`), `INTAKE` (`10_intake/`), `REFINERY` (`20_refinery/`),
  `OUTPUTS` (`30_outputs/`), `ARCHIVE` (`90_archive/`), or `MIXED` for a directory that
  genuinely holds more than one.
- Authority: `SOURCE` (truth is born here, hand-edited) or `MIRROR` (generated elsewhere —
  regenerable, and hand-editing it is a defect, not a change).

A fact has exactly one SOURCE. This is RULE-CHANNELS applied to storage instead of messages.

## What this repository must do

1. Keep a root `CLAUDE.md` holding a map table: `| Directory | Layer | Authority | What lives here |`.
2. One row per top-level directory; every row resolves to a directory that exists.
3. A commit that adds a top-level directory adds its row **in the same commit**.

`CLAUDE.md` is a map, not a rulebook. Governance stays in the canonical `global-rules/`.

## What this anchor does not do

It does not restructure this repository. No file is moved by it. Physical migration to the five
layers is opt-in, one repository per PR, and needs its own justification per RULE-CHESTERTON.

The knowledge vault (`F:\lib\vault`, OFFICE) is never committed to this or any other repository.

## Check

`python3 scripts/structure_check.py <repo-root>` in `ai-cloud-loader` verifies the map is complete
and honest about the tree. It does not verify that a directory's contents belong to the layer it
claims — that is a review judgment (RULE-GOODHART).
