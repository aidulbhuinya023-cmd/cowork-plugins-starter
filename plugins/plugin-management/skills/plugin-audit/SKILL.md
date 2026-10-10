---
name: plugin-audit
description: >-
  This skill should be used when the user asks to "audit our plugins", "check this plugin", "why isn't my skill triggering", "review plugin quality", or wants a health check of the plugins folder.
metadata:
  version: "0.1.0"
---

# Plugin Audit

## Checks

- **Manifest**: valid JSON, kebab-case name, semantic version
- **Skills**: description has trigger phrases in quotes; body is imperative and under 2,000 words; every referenced file exists
- **Commands**: each points at a skill that exists
- **Connectors**: servers in `.mcp.json` match the table in `CONNECTORS.md`; every `~~placeholder` used in a skill is defined there
- **Leftovers**: remaining `EDIT ME` values in team context files
- **Safety**: no secrets, no hard-coded absolute paths, guardrails section filled in

## Output

Findings grouped as **Must fix**, **Should fix**, and **Nice to have**, each with the file and a concrete fix. Offer to apply the fixes.
