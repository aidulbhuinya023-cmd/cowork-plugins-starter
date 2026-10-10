---
name: customer-support-team-context
description: >-
  This skill should be used at the start of any customer support task for this team. It holds the team's own terminology, preferred workflows, tone, and guardrails that every other skill and command in the customer-support plugin relies on.
metadata:
  version: "0.1.0"
---

# Customer Support Team Context

> **Team lead:** this is the file to edit. Replace every `EDIT ME` with your team's real
> answer. Short and concrete beats long and complete. Claude reads this file (and the two
> reference files next to it) before doing any customer support work.

## Instructions for Claude

1. Read `references/glossary.md` and `references/ways-of-working.md` before starting.
2. Use the team's terms exactly as written there. Expand abbreviations the way the glossary does.
3. When this context conflicts with a default in another skill, this context wins.
4. If a value still says `EDIT ME`, proceed with a sensible default and say in one short line which default you used.
5. Never put secrets, passwords, or customer personal data in this file or its references.

## Snapshot

- Product names and plans: EDIT ME
- Severity levels and what each means: EDIT ME
- First-response and resolution SLAs by tier: EDIT ME
- Escalation paths (who, which channel): EDIT ME
- What agents may offer without approval (refunds, credits): EDIT ME

## Defaults to apply

- Answer first, then explain.
- Link to the help article instead of pasting long instructions.
- Use the customer's name and the product name they use.
