# Enterprise Search plugin

Ask one question and search chat, docs, email, and tickets together, with sources, dates, and honest confidence.

## Slash commands

| Command | What it does |
|---------|--------------|
| `/find` | Search all connected tools for an answer |
| `/digest` | Catch up on a topic across tools |
| `/who-knows` | Find the right person for a topic |

## Skills

| Skill | What it covers |
|-------|----------------|
| `cross-source-search` | Searches all connected sources and returns a sourced answer |
| `knowledge-digest` | Catch-up on a topic: timeline, decisions, open questions |
| `expert-finding` | Finds who owns or knows a topic, with evidence |
| `enterprise-search-team-context` | **Edit this one.** Your terminology, workflows, tone, and guardrails |

## Connectors

Configured in `.mcp.json`: Slack, Notion, Guru, Atlassian (Jira, Confluence), Asana, Google Drive, Microsoft 365 (Outlook, Teams, SharePoint), Gmail, Google Calendar, Box.
See `CONNECTORS.md` for categories, alternatives, and setup notes.

## Make it yours (5 minutes)

1. Open `skills/enterprise-search-team-context/SKILL.md` and replace each `EDIT ME`.
2. Add your team's terms to `skills/enterprise-search-team-context/references/glossary.md`.
3. Describe how your team works in `skills/enterprise-search-team-context/references/ways-of-working.md`.
4. Delete servers you do not use from `.mcp.json`.
5. Bump `version` in `.claude-plugin/plugin.json` so teammates know it changed.
