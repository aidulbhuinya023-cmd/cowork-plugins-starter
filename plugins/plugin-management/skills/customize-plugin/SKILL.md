---
name: customize-plugin
description: >-
  This skill should be used when the user asks to "customize this plugin", "add our terminology", "make it use our tools", "change the tone", or wants an existing plugin adapted to their team.
metadata:
  version: "0.1.0"
---

# Customize Plugin

Keep changes small and reviewable.

## Steps

1. Ask which plugin. Read its `<name>-team-context` skill and both reference files.
2. Interview the user about terminology, workflows, tone, and tools. Skip anything already filled in.
3. Update, in this order of preference:
   1. `references/glossary.md` for new terms
   2. `references/ways-of-working.md` for workflows, tone, and guardrails
   3. The `EDIT ME` lines in the team context `SKILL.md`
   4. `.mcp.json` and `CONNECTORS.md` to add or remove connectors
   5. A domain skill, only when the workflow itself differs
4. If the team uses exactly one tool per category, offer to replace `~~category` placeholders with the tool name.
5. Bump `version` in `plugin.json`.
6. Show the user a summary of what changed and run `python3 scripts/validate.py`.

Never write secrets, API keys, or customer data into any plugin file.
