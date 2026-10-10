# Data plugin

Write and check SQL, profile datasets, and turn results into clear stories for stakeholders using your warehouse and BI tools.

## Slash commands

| Command | What it does |
|---------|--------------|
| `/write-sql` | Write a checked SQL query |
| `/explore-data` | Profile a table or file |
| `/summarize-insights` | Turn results into a stakeholder summary |

## Skills

| Skill | What it covers |
|-------|----------------|
| `sql-query-writing` | Writes readable, checked SQL against your real schema |
| `data-exploration` | Profiles a table or file and ranks data quality issues |
| `insight-summary` | Turns results into a short, honest stakeholder narrative |
| `data-team-context` | **Edit this one.** Your terminology, workflows, tone, and guardrails |

## Connectors

Configured in `.mcp.json`: BigQuery, Hex, Amplitude, Atlassian (Jira, Confluence), Slack, Notion.
See `CONNECTORS.md` for categories, alternatives, and setup notes.

## Make it yours (5 minutes)

1. Open `skills/data-team-context/SKILL.md` and replace each `EDIT ME`.
2. Add your team's terms to `skills/data-team-context/references/glossary.md`.
3. Describe how your team works in `skills/data-team-context/references/ways-of-working.md`.
4. Delete servers you do not use from `.mcp.json`.
5. Bump `version` in `.claude-plugin/plugin.json` so teammates know it changed.
