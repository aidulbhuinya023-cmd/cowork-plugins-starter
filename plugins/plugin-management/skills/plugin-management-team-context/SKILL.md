---
name: plugin-management-team-context
description: >-
  This skill should be used at the start of any plugin management task for this team. It holds the team's own terminology, preferred workflows, tone, and guardrails that every other skill and command in the plugin-management plugin relies on.
metadata:
  version: "0.1.0"
---

# Plugin Management Team Context

> **Team lead:** this is the file to edit. Replace every `EDIT ME` with your team's real
> answer. Short and concrete beats long and complete. Claude reads this file (and the two
> reference files next to it) before doing any plugin management work.

## Instructions for Claude

1. Read `references/glossary.md` and `references/ways-of-working.md` before starting.
2. Use the team's terms exactly as written there. Expand abbreviations the way the glossary does.
3. When this context conflicts with a default in another skill, this context wins.
4. If a value still says `EDIT ME`, proceed with a sensible default and say in one short line which default you used.
5. Never put secrets, passwords, or customer personal data in this file or its references.

## Snapshot

- Plugin owners (who approves changes): EDIT ME
- Naming convention for new plugins: EDIT ME
- Review process before a plugin is shared: EDIT ME
- Where the repo lives: EDIT ME
- Approved connectors list: EDIT ME

## Defaults to apply

- Prefer editing the team context over editing domain skills.
- Keep every change small enough to review in a few minutes.
- Run the validator after every change.
