---
name: legal-team-context
description: >-
  This skill should be used at the start of any legal task for this team. It holds the team's own terminology, preferred workflows, tone, and guardrails that every other skill and command in the legal plugin relies on.
metadata:
  version: "0.1.0"
---

# Legal Team Context

> **Team lead:** this is the file to edit. Replace every `EDIT ME` with your team's real
> answer. Short and concrete beats long and complete. Claude reads this file (and the two
> reference files next to it) before doing any legal work.

## Instructions for Claude

1. Read `references/glossary.md` and `references/ways-of-working.md` before starting.
2. Use the team's terms exactly as written there. Expand abbreviations the way the glossary does.
3. When this context conflicts with a default in another skill, this context wins.
4. If a value still says `EDIT ME`, proceed with a sensible default and say in one short line which default you used.
5. Never put secrets, passwords, or customer personal data in this file or its references.

## Snapshot

- Company legal entity names: EDIT ME
- Jurisdictions we usually contract under: EDIT ME
- Approved templates (NDA, MSA, DPA): EDIT ME
- Approval matrix (who signs off on what): EDIT ME
- Escalation contact for urgent matters: EDIT ME

## Defaults to apply

- Always label output as assistive analysis for attorney review.
- Quote the clause you are discussing.
- Never guess at facts not in the document.
