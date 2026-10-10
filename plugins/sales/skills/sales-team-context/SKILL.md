---
name: sales-team-context
description: >-
  This skill should be used at the start of any sales task for this team. It holds the team's own terminology, preferred workflows, tone, and guardrails that every other skill and command in the sales plugin relies on.
metadata:
  version: "0.1.0"
---

# Sales Team Context

> **Team lead:** this is the file to edit. Replace every `EDIT ME` with your team's real
> answer. Short and concrete beats long and complete. Claude reads this file (and the two
> reference files next to it) before doing any sales work.

## Instructions for Claude

1. Read `references/glossary.md` and `references/ways-of-working.md` before starting.
2. Use the team's terms exactly as written there. Expand abbreviations the way the glossary does.
3. When this context conflicts with a default in another skill, this context wins.
4. If a value still says `EDIT ME`, proceed with a sensible default and say in one short line which default you used.
5. Never put secrets, passwords, or customer personal data in this file or its references.

## Snapshot

- What we sell, in one sentence: EDIT ME
- Ideal customer profile: EDIT ME
- Qualification framework (for example MEDDPICC, BANT): EDIT ME
- Sales stages and exit criteria: EDIT ME
- Quarter-end date and forecast categories: EDIT ME

## Defaults to apply

- Cite the source for every claim about an account.
- Prefer the customer's own words over our paraphrase.
- Keep emails under 150 words unless asked.
