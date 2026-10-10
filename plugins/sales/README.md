# Sales plugin

Prep calls, review deals, and draft follow-ups using your CRM, email, calendar, and call recordings, or uploaded notes.

## Slash commands

| Command | What it does |
|---------|--------------|
| `/call-prep` | Prep a one-page brief for a call |
| `/deal-review` | Candid health check on a deal |
| `/draft-follow-up` | Draft a follow-up email and CRM note |

## Skills

| Skill | What it covers |
|-------|----------------|
| `call-prep` | One-page brief before a customer or prospect call |
| `deal-review` | Honest health check on one opportunity |
| `follow-up-drafting` | Recap email and CRM note after a meeting |
| `sales-team-context` | **Edit this one.** Your terminology, workflows, tone, and guardrails |

## Connectors

Configured in `.mcp.json`: HubSpot, Salesforce, Slack, Gmail, Google Calendar, Microsoft 365 (Outlook, Teams, SharePoint), Notion, Gong, Fireflies, Apollo, ZoomInfo.
See `CONNECTORS.md` for categories, alternatives, and setup notes.

## Make it yours (5 minutes)

1. Open `skills/sales-team-context/SKILL.md` and replace each `EDIT ME`.
2. Add your team's terms to `skills/sales-team-context/references/glossary.md`.
3. Describe how your team works in `skills/sales-team-context/references/ways-of-working.md`.
4. Delete servers you do not use from `.mcp.json`.
5. Bump `version` in `.claude-plugin/plugin.json` so teammates know it changed.
