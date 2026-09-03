#!/bin/sh
# SessionStart orientation for this repo — READ-ONLY, fast, non-interactive.
#
# Prints the non-negotiables and the canon pointers so no session starts blind,
# then compares this repo's vendored rules signature against a canon clone if
# one is on disk. Drift is printed loudly; it is never repaired here, because a
# hook that silently rewrites canon is worse than drift.

set -u

ROOT="${CLAUDE_PROJECT_DIR:-.}"
RULES_DIR="$ROOT/.rules"
LOCK="$RULES_DIR/rules.lock.json"

echo "===== RULES LAYER — READ BEFORE ACTING ====="
echo

if [ -f "$RULES_DIR/RULES.md" ]; then
  sed -n '/^## Non-negotiables/,/^## Full registry/p' "$RULES_DIR/RULES.md" | sed '$d'
else
  echo "WARNING: .rules/RULES.md is missing. This repo's rules layer is not installed."
fi

echo "Full registry index: .rules/RULES.md"
echo "Canon rule text:     oklawsite-machine/ai-cloud-loader (global-rules/ and rules/)"
echo

# Drift check against a canon clone sitting beside this repo, when there is one.
SIG=""
if [ -f "$LOCK" ]; then
  SIG=$(sed -n 's/.*"registry_signature"[[:space:]]*:[[:space:]]*"\([0-9a-f]*\)".*/\1/p' "$LOCK" | head -1)
fi

CANON=""
for candidate in "$ROOT/../ai-cloud-loader" "$HOME/ai-cloud-loader" "/home/user/ai-cloud-loader" "D:/AI/ai-cloud-loader" "F:/lib/Ai/ai-cloud-loader"; do
  if [ -f "$candidate/RULE_REGISTRY.json" ]; then CANON="$candidate"; break; fi
done

if [ -n "$CANON" ] && [ -n "$SIG" ] && [ -f "$CANON/.rules/rules.lock.json" ]; then
  CANON_SIG=$(sed -n 's/.*"registry_signature"[[:space:]]*:[[:space:]]*"\([0-9a-f]*\)".*/\1/p' "$CANON/.rules/rules.lock.json" | head -1)
  if [ -n "$CANON_SIG" ] && [ "$CANON_SIG" != "$SIG" ]; then
    echo "!!! RULES DRIFT — this repo's bundle does not match the canon clone at $CANON"
    echo "    here:  $SIG"
    echo "    canon: $CANON_SIG"
    echo "    Refresh with: python3 $CANON/tools/rules/rules_bundle.py sync --targets $ROOT"
    echo "    Do not hand-edit .rules/ — it is generated."
    echo
  fi
fi

echo "===== END RULES LAYER ====="
exit 0
