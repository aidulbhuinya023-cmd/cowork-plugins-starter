---
name: enterprise-search-team-context
description: >-
  This skill should be used at the start of any enterprise search task for this team. It holds the team's own terminology, preferred workflows, tone, and guardrails that every other skill and command in the enterprise-search plugin relies on.
metadata:
  version: "0.1.0"
---

# Enterprise Search Team Context

> **Team lead:** this is the file to edit. Replace every `EDIT ME` with your team's real
> answer. Short and concrete beats long and complete. Claude reads this file (and the two
> reference files next to it) before doing any enterprise search work.

## Instructions for Claude

1. Read `references/glossary.md` and `references/ways-of-working.md` before starting.
2. Use the team's terms exactly as written there. Expand abbreviations the way the glossary does.
3. When this context conflicts with a default in another skill, this context wins.
4. If a value still says `EDIT ME`, proceed with a sensible default and say in one short line which default you used.
5. Never put secrets, passwords, or customer personal data in this file or its references.

## Snapshot

- Source of truth ranking (which tool wins when sources conflict): EDIT ME
- Freshness window (how old is too old): EDIT ME
- Project and system code names: EDIT ME
- Ownership table: topic to owner: EDIT ME
- Anything off-limits to search or summarize: EDIT ME

## Defaults to apply

- Always return links and dates.
- Prefer the official doc over a chat message.
- Say what was not searched.
