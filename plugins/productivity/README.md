# Productivity plugin

Plan your day, keep a clean task list, and run a weekly review using your calendar, email, chat, and project tracker, or plain pasted text.

## Slash commands

| Command | What it does |
|---------|--------------|
| `/plan-day` | Build today's prioritized plan |
| `/weekly-review` | Run a weekly review of tasks and commitments |
| `/capture` | Add a task from free text |

## Skills

| Skill | What it covers |
|-------|----------------|
| `daily-planning` | Builds a prioritized plan for today from calendar, tasks, and messages |
| `task-management` | Captures tasks and keeps a clean Today / Waiting On / Later list |
| `productivity-team-context` | **Edit this one.** Your terminology, workflows, tone, and guardrails |

## Connectors

Configured in `.mcp.json`: Slack, Notion, Asana, Linear, Atlassian (Jira, Confluence), Google Calendar, Gmail, Microsoft 365 (Outlook, Teams, SharePoint).
See `CONNECTORS.md` for categories, alternatives, and setup notes.

## Make it yours (5 minutes)

1. Open `skills/productivity-team-context/SKILL.md` and replace each `EDIT ME`.
2. Add your team's terms to `skills/productivity-team-context/references/glossary.md`.
3. Describe how your team works in `skills/productivity-team-context/references/ways-of-working.md`.
4. Delete servers you do not use from `.mcp.json`.
5. Bump `version` in `.claude-plugin/plugin.json` so teammates know it changed.
