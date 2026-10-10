# Customer Support plugin

Triage tickets, draft consistent replies, and package clean escalations using your support platform and knowledge base.

## Slash commands

| Command | What it does |
|---------|--------------|
| `/triage` | Triage a ticket: category, severity, owner |
| `/draft-reply` | Draft a customer reply from the knowledge base |
| `/escalate` | Write an escalation brief for another team |

## Skills

| Skill | What it covers |
|-------|----------------|
| `ticket-triage` | Categorize, rate severity, and route a ticket |
| `response-drafting` | Drafts an accurate, on-tone customer reply |
| `escalation-brief` | Packages a case for engineering or a specialist team |
| `customer-support-team-context` | **Edit this one.** Your terminology, workflows, tone, and guardrails |

## Connectors

Configured in `.mcp.json`: Slack, Intercom, HubSpot, Guru, Atlassian (Jira, Confluence), Notion, Gmail, Microsoft 365 (Outlook, Teams, SharePoint).
See `CONNECTORS.md` for categories, alternatives, and setup notes.

## Make it yours (5 minutes)

1. Open `skills/customer-support-team-context/SKILL.md` and replace each `EDIT ME`.
2. Add your team's terms to `skills/customer-support-team-context/references/glossary.md`.
3. Describe how your team works in `skills/customer-support-team-context/references/ways-of-working.md`.
4. Delete servers you do not use from `.mcp.json`.
5. Bump `version` in `.claude-plugin/plugin.json` so teammates know it changed.
