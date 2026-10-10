# Legal plugin

Review contracts against your playbook, triage NDAs, and explain clauses in plain language. Assistive analysis for attorney review, not legal advice.

## Slash commands

| Command | What it does |
|---------|--------------|
| `/review-contract` | Review a contract against the playbook |
| `/triage-nda` | Screen an NDA green, yellow, or red |
| `/explain-clause` | Explain a clause in plain language |

## Skills

| Skill | What it covers |
|-------|----------------|
| `contract-review` | Clause-by-clause review against your playbook with proposed redlines |
| `nda-triage` | Fast green / yellow / red screen for incoming NDAs |
| `clause-explainer` | Plain-language explanation of a clause for non-lawyers |
| `legal-team-context` | **Edit this one.** Your terminology, workflows, tone, and guardrails |

## Connectors

Configured in `.mcp.json`: Slack, Box, DocuSign, Atlassian (Jira, Confluence), Google Drive, Gmail, Microsoft 365 (Outlook, Teams, SharePoint).
See `CONNECTORS.md` for categories, alternatives, and setup notes.

## Make it yours (5 minutes)

1. Open `skills/legal-team-context/SKILL.md` and replace each `EDIT ME`.
2. Add your team's terms to `skills/legal-team-context/references/glossary.md`.
3. Describe how your team works in `skills/legal-team-context/references/ways-of-working.md`.
4. Delete servers you do not use from `.mcp.json`.
5. Bump `version` in `.claude-plugin/plugin.json` so teammates know it changed.
