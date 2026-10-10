# Finance plugin

Explain variances, prepare journal entries for review, and track month-end close using your data warehouse and spreadsheets.

## Slash commands

| Command | What it does |
|---------|--------------|
| `/variance` | Explain variances for a period |
| `/draft-je` | Draft journal entries for review |
| `/close-status` | Summarize month-end close status |

## Skills

| Skill | What it covers |
|-------|----------------|
| `variance-analysis` | Explains actual vs budget or prior period, above materiality |
| `journal-entry-prep` | Drafts balanced journal entries with support, for review |
| `month-end-close` | Tracks close tasks, owners, blockers, and status updates |
| `finance-team-context` | **Edit this one.** Your terminology, workflows, tone, and guardrails |

## Connectors

Configured in `.mcp.json`: BigQuery, Slack, Google Drive, Gmail, Microsoft 365 (Outlook, Teams, SharePoint).
See `CONNECTORS.md` for categories, alternatives, and setup notes.

## Make it yours (5 minutes)

1. Open `skills/finance-team-context/SKILL.md` and replace each `EDIT ME`.
2. Add your team's terms to `skills/finance-team-context/references/glossary.md`.
3. Describe how your team works in `skills/finance-team-context/references/ways-of-working.md`.
4. Delete servers you do not use from `.mcp.json`.
5. Bump `version` in `.claude-plugin/plugin.json` so teammates know it changed.
