# Acceleration Machine — canon rules digest

Generated from `oklawsite-machine/ai-cloud-loader` `RULE_REGISTRY.json`. 40 rules: 4 enforced, 26 active, 10 proposed.

Signature: `dfef8cad8b3c533b45436d6b9f794d62ed88858ddd13f6091c7b23e908abe9ef`

This digest is generated. It is an index and a summary, never the rule text itself — when a rule decides something, open its canon file. Editing this file by hand does nothing except fail CI.

## Non-negotiables — these govern how you work here

1. **Source, not memory.** Do not state repo state, node state, file state or
   rule content as fact unless you read it this turn. Label anything else
   `MEMORY_ONLY` / `USER_STATED`. (GATE-S, RULE-D, bootloader enforcement gate)
2. **Branch and PR only.** Never push to the default branch. Work on
   `claude/<topic>-<YYYYMMDD>`. A PR that adds a rule or a script adds the check
   that enforces it in the same PR — a rule with no check does not count.
   (RULE-GITGATE sections 2 and 6)
3. **Build the mechanism, not the artifact.** A task is done when a mechanism
   exists, something that is not a human triggers it, it survived one unattended
   run, and its failure reaches a channel Ofer reads. Producing the output by
   hand and calling it done is the default failure mode. (RULE-MECH section 2)
4. **The model never decides control flow.** Timing, routing, retry and failure
   detection belong to the trigger and logic layers. (RULE-MECH section 4)
5. **Container writes are not node writes.** A real-drive target (`C:`, `D:`,
   `F:`, `G:`, any UNC path) is reached only by a direct-to-disk node tool, and
   every "saved" claim about a node carries a same-turn read-back.
   (RULE-DC-ONLY-WRITE)
6. **Know why the fence is there before you remove it.** `git log -S` and
   `git blame` are the evidence; an invented reason is not an origin. Verdict is
   one of: origin found and obsolete, origin found and live, origin not found.
   (RULE-CHESTERTON, with RULE-DESTRUCTIVE)
7. **Do not certify your own repair.** A session that caused or diagnosed a
   failure may record it and draft the fix, but must not mark that fix ENFORCED
   or canon. That is a separate reviewer's call. (RULE-NSRA)
8. **The user is not the operator.** Carry the loading, routing and filing
   burden yourself; do not hand back manual steps a tool you hold could perform.
   (RULE-A)
9. **Simple first.** Take the smallest execution path that actually solves it,
   and say so when you reject a bigger one. (RULE-OCC)
10. **No dead-end endings.** Diagnosis without a next action is not an answer.
    (RULE-N)

## Full registry

Tier is the coarse question — may I rely on this now? ENFORCED is binding, ACTIVE is canon in force, PROPOSED is drafted and awaiting review and must not be cited as binding.

### ENFORCED (4)

- **RULE-CHECK-BEFORE-MISSING** — `global-rules/check_local_clone_before_missing_rule_20260713.md`
  Before declaring any resource missing, lost, unavailable, or absent — a file, repo,
- **RULE-DC-ONLY-WRITE** — `global-rules/RULE-DC-ONLY-WRITE-20260705.md`
  Prevent the two coupled failures behind INCIDENT-SANDBOX-VS-NODE-WRITE-20260702: a
- **RULE-DISCOVERED-TRIAGE** — `global-rules/discovered_artifact_triage_one_touch_20260713.md`
  2026-07-13 home reconcile: gate.py (Rule Enforcement Kernel v0 — GOLD) sat UNTRACKED on
- **RULE-PF** — `global-rules/project_files_not_source_of_truth_rule_20260701.md`
  Prevent content auto-loaded from **claude.ai Project Files** (files attached to a

### ACTIVE (26)

- **RULE-ASK** — `global-rules/RULE-ASK.md`
  Authored by Ofer 16.07.26, formulated by Claude. Extends the standing "if you don't understand, ask" principle. Staged by claude.ai [HOME] 19.07.26, unmerged...
- **RULE-CHESTERTON** — `global-rules/RULE-CHESTERTON.md`
  Canon (Ofer, 2026-07-17). Companion gate to RULE-DESTRUCTIVE. RULE-DESTRUCTIVE
- **RULE-CLOSEOUT** — `rules/closeout_20260513.md`
  id: RULE-CLOSEOUT
- **RULE-CODEX-WINDOW** — `rules/codex-operating-window-rule-2026-05-12.md`
  id: RULE-CODEX-WINDOW
- **RULE-CONTINUATION-ROUTING** — `rules/continuation-routing-identity-rule-2026-05-12.md`
  id: RULE-CONTINUATION-ROUTING
- **RULE-CONV-HOOK** — `rules/conversation-hook-rule-2026-05-12.md`
  id: RULE-CONV-HOOK
- **RULE-DESTRUCTIVE** — `global-rules/RULE-DESTRUCTIVE.md`
  Authored by Ofer 15.07.26, refined by Claude. REPLACES the old blanket prohibition ('Claude never permanently deletes a file, even with explicit approval'). ...
- **RULE-DRAFT-LOCK** — `rules/draft-lock.md`
  id: RULE-DRAFT-LOCK
- **RULE-DRIFT-MATTER** — `rules/drift_to_matter_and_slow_wide_scan_rule_20260517.md`
  id: RULE-DRIFT-MATTER
- **RULE-ENFORCEMENT-LAYER** — `rules/enforcement-vs-behavior-layer-2026-05-15.md`
  id: RULE-ENFORCEMENT-LAYER
- **RULE-GITGATE** — `global-rules/RULE-GITGATE.md`
  `master` is the only good version. Nothing is canon until merged to master.
- **RULE-GITPUSH-NODEBRIDGE** — `global-rules/RULE-GITPUSH-NODEBRIDGE.md`
  Confirmed by Ofer 19.07.26 (node-bridge, full scope) and extended 10.08.26
- **RULE-GOODHART** — `global-rules/RULE-GOODHART.md`
  Canon (Ofer, 2026-07-17). When a measure becomes the target it stops being a
- **RULE-HANDOFF** — `rules/handoff.md`
  id: RULE-HANDOFF
- **RULE-HANDOFF-PROTOCOL** — `global-rules/RULE-HANDOFF-PROTOCOL.md`
  Authored by Ofer 18.07.26 ("almost the most important"). Two parts: how a HANDOFF gets written, and what that writing moment is for. Staged by claude.ai [HOM...
- **RULE-HRW** — `rules/human_natural_rewrite_prompts_20260605.md`
  id: RULE-HRW
- **RULE-INSTRUCTION-SOURCE** — `global-rules/RULE-INSTRUCTION-SOURCE.md`
  Clarified by Ofer 18.07.26. VOIDS an earlier broken framing. Staged by claude.ai [HOME] 19.07.26, unmerged — see RULE-GITGATE for PR requirement before this ...
- **RULE-LOCAL-WORKER** — `rules/local-worker-vscode-claude-codex-workflow-2026-05-12.md`
  id: RULE-LOCAL-WORKER
- **RULE-MECH** — `global-rules/RULE-MECH.md`
  On EVERY task, before any design, the first question is:
- **RULE-NAMES** — `rules/names.md`
  id: RULE-NAMES
- **RULE-NULL** — `global-rules/RULE-NULL.md`
  Authored by Ofer 16.07.26, formulated by Claude. Staged by claude.ai [HOME] 19.07.26, unmerged — see RULE-GITGATE for PR requirement before this is canon.
- **RULE-OCC** — `global-rules/RULE-OCC_OCCAM_CHECK_SIMPLE_FIRST_EXECUTION_V0.md`
  `RULE-OCC` — Occam Check / Simple-First Execution
- **RULE-PRESERVATION-ANCHOR** — `rules/preservation_vs_execution_anchor.md`
  id: RULE-PRESERVATION-ANCHOR
- **RULE-PSC** — `rules/production-sprint-checkpoint-rule-2026-05-15.md`
  id: RULE-PSC
- **RULE-RELAY** — `global-rules/RULE-RELAY.md`
  Pinned by Ofer 17.07.26, explicit and firm requirement. Staged by claude.ai [HOME] 19.07.26; merged to main 21.07.26 in commit `0e66344` (six HOME-staged rul...
- **RULE-RESEARCH-SYNTHESIS** — `global-rules/RULE-RESEARCH-SYNTHESIS.md`
  turns them into a decision. All executors.

### PROPOSED (10)

- **BOOTLOADER_GITHUB_FIRST_RULE** — `rules/bootloader_github_first.md`
  Status: PENDING_EXTERNAL_REVIEW
- **GATE-S** — `rules/SOURCE_TRUTH_GATE_20260610.md`
  id: GATE-S
- **RULE-CHANNELS** — `global-rules/RULE-CHANNELS.md`
  Proposed by Claude Code [HOME] 27.07.26 (git-archaeology of ai-cloud-loader); GO on all five points from claude.ai the same day, which added the consultation...
- **RULE-CHANNELS-WORKROUTING** — `global-rules/RULE-CHANNELS-WORKROUTING.md`
  Written 2026-08-09 by cowork@office (cloud session, Desktop Commander bound to OfficeNode).
- **RULE-FEEPOA-PREP** — `global-rules/client_fee_agreement_poa_prep_rule_20260730.md`
  תיעודיים: נעמה ברגר (09.07 — הולידה את קיום התבניות), נרקיס (21.07+23.07 — חשפה
- **RULE-R** — `rules/REFINERY_PROTOCOL_20260610.md`
  id: RULE-R
- **RULE-RULESLOAD** — `global-rules/RULE-RULESLOAD.md`
  A rule that is written but never loaded is not a rule. It is a document about a
- **RULE-SCANINDEX** — `global-rules/scan_residue_index_rule_20260730.md`
  `sig: inbox recbShXPFGPclVFjk | node: OFFICE | agent: claude-code+claude-opus-4-8 | ts: 2026-07-30`
- **RULE-SELFRESUME** — `global-rules/RULE-SELFRESUME.md`
  Spec authored by claude.ai [OFFICE] 29.07.26 in PINNED_TASK `rec1D1vbLbvxsOs0U` (HIGH); rule text authored and staged by Claude Code [OFFICE] 29.07.26 on bra...
- **RULE-SESSION-SIGNATURE** — `global-rules/RULE-SESSION-SIGNATURE.md`
  Name pinned by Ofer 27.07.26; content formulated by Claude — PROPOSED, not yet user-approved. Staged by Claude Code [OFFICE] 27.07.26 on branch `claude/rule-...
