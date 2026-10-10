# Connectors

## How tool references work

Skills and commands in this plugin refer to tools by **category**, written as `~~category`
(for example `~~chat`). A category means "whatever tool your team connects for this job".
That keeps the markdown readable and lets you swap tools without rewriting every skill.

The `.mcp.json` file pre-configures one or more servers per category. Any MCP server in the
same category works. If your team only ever uses one tool, you can find-and-replace the
placeholder with its name (for example `~~chat` becomes `Slack`).

Every skill also works with nothing connected: paste text or upload a file and it works from that.

## Connectors for this plugin

| Category | Placeholder | Included in `.mcp.json` | Other options |
|----------|-------------|-------------------------|---------------|
| Support platform | `~~support platform` | Intercom, HubSpot | Zendesk, Freshdesk, Help Scout |
| Knowledge base | `~~knowledge base` | Guru, Notion, Atlassian (Confluence) | Document360, Help Center exports |
| Project tracker | `~~project tracker` | Atlassian (Jira) | Linear, Asana |
| Chat | `~~chat` | Slack, Microsoft 365 (Teams) |  |
| Email | `~~email` | Gmail, Microsoft 365 (Outlook) |  |

## Setup notes

- Each server asks you to sign in (OAuth) the first time it is used. No API keys live in these files.
- Remove any server your team does not use from `.mcp.json`. Fewer connectors means less noise.
- Control what a connector may do (allow, ask, or block per tool) in the connector's own settings.
- Zendesk and Freshdesk are not pre-configured. Add their MCP server URL to `.mcp.json` if your vendor provides one.
