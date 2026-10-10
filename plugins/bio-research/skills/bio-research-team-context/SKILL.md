---
name: bio-research-team-context
description: >-
  This skill should be used at the start of any bio research task for this team. It holds the team's own terminology, preferred workflows, tone, and guardrails that every other skill and command in the bio-research plugin relies on.
metadata:
  version: "0.1.0"
---

# Bio Research Team Context

> **Team lead:** this is the file to edit. Replace every `EDIT ME` with your team's real
> answer. Short and concrete beats long and complete. Claude reads this file (and the two
> reference files next to it) before doing any bio research work.

## Instructions for Claude

1. Read `references/glossary.md` and `references/ways-of-working.md` before starting.
2. Use the team's terms exactly as written there. Expand abbreviations the way the glossary does.
3. When this context conflicts with a default in another skill, this context wins.
4. If a value still says `EDIT ME`, proceed with a sensible default and say in one short line which default you used.
5. Never put secrets, passwords, or customer personal data in this file or its references.

## Snapshot

- Research areas and organisms: EDIT ME
- Preferred databases and date limits: EDIT ME
- Citation style: EDIT ME
- Gene and protein naming conventions: EDIT ME
- Internal programs and their code names: EDIT ME

## Defaults to apply

- Report the exact search strategy.
- Distinguish preprints from peer-reviewed work.
- Prefer primary sources over reviews for specific claims.
