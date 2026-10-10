---
name: create-plugin
description: >-
  This skill should be used when the user asks to "create a plugin", "make a new plugin", "add a plugin for our team", "scaffold a plugin", or wants to turn a repeated workflow into a plugin.
metadata:
  version: "0.1.0"
---

# Create Plugin

## Steps

1. Interview the user, at most five questions: the role, who will use it, the three workflows that matter most, the tools involved, and the terms newcomers get wrong.
2. Copy `templates/plugin-template/` to `plugins/<kebab-case-name>/`.
3. Edit `.claude-plugin/plugin.json`: name, description, author, version `0.1.0`.
4. Write one skill per workflow:
   - Frontmatter `description` in third person with real trigger phrases in quotes
   - Body in imperative voice, under 2,000 words, detail moved to `references/`
5. Add one thin slash command per skill in `commands/`. A command only points at its skill.
6. Keep only the servers the team needs in `.mcp.json`. Fill `CONNECTORS.md` to match, using `~~category` placeholders in the skills.
7. Fill the team context skill with the terms and rules the user gave you.
8. Add the plugin to `.claude-plugin/marketplace.json`.
9. Run `python3 scripts/validate.py` and fix every error.

Show the user the list of files created and how to try each command.
