---
name: data-team-context
description: >-
  This skill should be used at the start of any data task for this team. It holds the team's own terminology, preferred workflows, tone, and guardrails that every other skill and command in the data plugin relies on.
metadata:
  version: "0.1.0"
---

# Data Team Context

> **Team lead:** this is the file to edit. Replace every `EDIT ME` with your team's real
> answer. Short and concrete beats long and complete. Claude reads this file (and the two
> reference files next to it) before doing any data work.

## Instructions for Claude

1. Read `references/glossary.md` and `references/ways-of-working.md` before starting.
2. Use the team's terms exactly as written there. Expand abbreviations the way the glossary does.
3. When this context conflicts with a default in another skill, this context wins.
4. If a value still says `EDIT ME`, proceed with a sensible default and say in one short line which default you used.
5. Never put secrets, passwords, or customer personal data in this file or its references.

## Snapshot

- Warehouse and SQL dialect: EDIT ME
- Most-used tables and what they mean: EDIT ME
- Official metric definitions (active user, revenue, churn): EDIT ME
- Time zone and fiscal calendar: EDIT ME
- Where dashboards and notebooks live: EDIT ME

## Defaults to apply

- Use official metric definitions; never invent a new one silently.
- State the time window and time zone on every result.
- Prefer CTEs over nested subqueries.
