#!/usr/bin/env python3
"""Rules-bundle integrity check — vendored, self-contained, no canon needed.

Runs in the consumer repo's CI and locally. It answers one question: is this
repo's self-loading rules layer intact and internally consistent? It cannot see
the canon repo, so it does not judge freshness — staleness against canon is the
session-start hook's job (it compares signatures when a canon clone is present).

Exit 0 = intact, 1 = broken.
"""

import hashlib
import json
import sys
from pathlib import Path

BEGIN_MARK = "<!-- BEGIN ACCELERATION-MACHINE RULES BLOCK (generated - do not edit by hand) -->"
END_MARK = "<!-- END ACCELERATION-MACHINE RULES BLOCK -->"

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
errors = []


def sha256_text(data):
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


lock_path = HERE / "rules.lock.json"
digest_path = HERE / "RULES.md"

if not lock_path.is_file():
    errors.append("missing .rules/rules.lock.json")
if not digest_path.is_file():
    errors.append("missing .rules/RULES.md")

lock = {}
if lock_path.is_file():
    try:
        lock = json.loads(lock_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append("rules.lock.json does not parse: %s" % exc)

if lock:
    for field in ("schema", "registry_signature", "digest_sha256", "rules", "rule_count"):
        if field not in lock:
            errors.append("rules.lock.json missing field: %s" % field)
    if lock.get("rule_count") != len(lock.get("rules", [])):
        errors.append(
            "rule_count=%s but rules array has %s"
            % (lock.get("rule_count"), len(lock.get("rules", [])))
        )
    if digest_path.is_file():
        actual = sha256_text(digest_path.read_bytes())
        if lock.get("digest_sha256") != actual:
            errors.append(
                "RULES.md does not match its lock: lock=%s actual=%s"
                % (lock.get("digest_sha256"), actual)
            )
    payload = "\n".join(
        "%s:%s" % (r.get("id"), r.get("sha256"))
        for r in sorted(lock.get("rules", []), key=lambda x: x.get("id") or "")
    )
    recomputed = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    if lock.get("registry_signature") != recomputed:
        errors.append(
            "registry_signature does not match the rules array: lock=%s recomputed=%s"
            % (lock.get("registry_signature"), recomputed)
        )

claude_md = REPO / "CLAUDE.md"
if not claude_md.is_file():
    errors.append("missing CLAUDE.md - the rules layer has no auto-load point in this repo")
else:
    text = claude_md.read_text(encoding="utf-8")
    if BEGIN_MARK not in text or END_MARK not in text:
        errors.append("CLAUDE.md is missing the managed rules block markers")
    elif lock.get("registry_signature") and lock["registry_signature"] not in text:
        errors.append("CLAUDE.md managed block signature does not match rules.lock.json")

for extra in (".claude/settings.json",):
    p = REPO / extra
    if not p.is_file():
        errors.append("missing %s" % extra)
    elif extra.endswith(".json"):
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append("%s does not parse: %s" % (extra, exc))

hook = REPO / ".claude" / "hooks" / "rules-boot.sh"
if not hook.is_file():
    errors.append("missing .claude/hooks/rules-boot.sh")

for e in errors:
    print("ERROR %s" % e)
print("check_rules_bundle: %d error(s)" % len(errors))
sys.exit(1 if errors else 0)
