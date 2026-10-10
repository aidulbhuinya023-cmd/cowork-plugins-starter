# Plugin Management plugin

Create, customize, and audit plugins in this repo. Helps team leads add company terminology, swap connectors, and keep plugins healthy.

## Slash commands

| Command | What it does |
|---------|--------------|
| `/new-plugin` | Create a new plugin from the template |
| `/customize-plugin` | Add company terms and tools to a plugin |
| `/audit-plugins` | Health-check the plugins in this repo |

## Skills

| Skill | What it covers |
|-------|----------------|
| `create-plugin` | Guides a new plugin from idea to a validated folder |
| `customize-plugin` | Adapts an existing plugin to your company's language and tools |
| `plugin-audit` | Reviews plugins for quality, drift, and leftover placeholders |
| `plugin-management-team-context` | **Edit this one.** Your terminology, workflows, tone, and guardrails |

## Connectors

Configured in `.mcp.json`: none.
See `CONNECTORS.md` for categories, alternatives, and setup notes.

## Make it yours (5 minutes)

1. Open `skills/plugin-management-team-context/SKILL.md` and replace each `EDIT ME`.
2. Add your team's terms to `skills/plugin-management-team-context/references/glossary.md`.
3. Describe how your team works in `skills/plugin-management-team-context/references/ways-of-working.md`.
4. Delete servers you do not use from `.mcp.json`.
5. Bump `version` in `.claude-plugin/plugin.json` so teammates know it changed.
