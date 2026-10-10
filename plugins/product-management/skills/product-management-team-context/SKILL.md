---
name: product-management-team-context
description: >-
  This skill should be used at the start of any product management task for this team. It holds the team's own terminology, preferred workflows, tone, and guardrails that every other skill and command in the product-management plugin relies on.
metadata:
  version: "0.1.0"
---

# Product Management Team Context

> **Team lead:** this is the file to edit. Replace every `EDIT ME` with your team's real
> answer. Short and concrete beats long and complete. Claude reads this file (and the two
> reference files next to it) before doing any product management work.

## Instructions for Claude

1. Read `references/glossary.md` and `references/ways-of-working.md` before starting.
2. Use the team's terms exactly as written there. Expand abbreviations the way the glossary does.
3. When this context conflicts with a default in another skill, this context wins.
4. If a value still says `EDIT ME`, proceed with a sensible default and say in one short line which default you used.
5. Never put secrets, passwords, or customer personal data in this file or its references.

## Snapshot

- Product areas and owners: EDIT ME
- PRD template or link: EDIT ME
- Prioritization framework and scoring scale: EDIT ME
- North-star and guardrail metrics: EDIT ME
- Planning cadence (quarterly, six-week cycles): EDIT ME

## Defaults to apply

- Lead with the problem and evidence, not the solution.
- Every metric needs a baseline and a measurement method.
- List non-goals explicitly.
