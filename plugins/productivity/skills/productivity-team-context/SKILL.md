---
name: productivity-team-context
description: >-
  This skill should be used at the start of any productivity task for this team. It holds the team's own terminology, preferred workflows, tone, and guardrails that every other skill and command in the productivity plugin relies on.
metadata:
  version: "0.1.0"
---

# Productivity Team Context

> **Team lead:** this is the file to edit. Replace every `EDIT ME` with your team's real
> answer. Short and concrete beats long and complete. Claude reads this file (and the two
> reference files next to it) before doing any productivity work.

## Instructions for Claude

1. Read `references/glossary.md` and `references/ways-of-working.md` before starting.
2. Use the team's terms exactly as written there. Expand abbreviations the way the glossary does.
3. When this context conflicts with a default in another skill, this context wins.
4. If a value still says `EDIT ME`, proceed with a sensible default and say in one short line which default you used.
5. Never put secrets, passwords, or customer personal data in this file or its references.

## Snapshot

- Role and team: EDIT ME
- Working hours and time zone: EDIT ME
- Focus-time rules (for example no meetings before 11): EDIT ME
- Priority labels in use (for example P0-P3): EDIT ME
- Follow-up window for Waiting On items (days): EDIT ME

## Defaults to apply

- Keep plans to one screen.
- Protect focus blocks before scheduling anything else.
- Use verb-first task titles.
