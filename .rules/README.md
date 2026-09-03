# .rules — vendored canon rules layer

Generated. Do not edit anything in this directory by hand; CI fails when the
contents stop matching their own lock, and the next sync overwrites edits.

| File | What it is |
|---|---|
| `RULES.md` | The digest a session reads: non-negotiables plus the full registry index by tier. |
| `rules.lock.json` | Machine-readable lock — rule ids, statuses, canon paths, per-file hashes, and the one signature that identifies this rule set. |
| `check_rules_bundle.py` | Self-contained integrity check. Runs in CI and locally, needs no network and no canon clone. |

Canon lives in `oklawsite-machine/ai-cloud-loader`. Rule *text* is never copied
here — only the index, the statuses and the hashes. To read what a rule actually
says, open its canon file.

Refresh this bundle from a canon clone:

    python3 <canon>/tools/rules/rules_bundle.py sync --targets <this repo>
