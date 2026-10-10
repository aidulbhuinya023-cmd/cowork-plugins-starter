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
| CRM / marketing automation | `~~CRM` | HubSpot | Salesforce, Marketo |
| Email marketing | `~~email marketing` | Klaviyo, HubSpot | Mailchimp, Customer.io |
| Design | `~~design` | Canva, Figma | Adobe Express |
| Product analytics | `~~product analytics` | Amplitude | Mixpanel, GA4 |
| SEO | `~~SEO tool` | Ahrefs | Semrush, Similarweb |
| Marketing analytics | `~~marketing analytics` | Supermetrics | Funnel, Windsor |
| Knowledge base | `~~knowledge base` | Notion, Google Drive | Confluence |
| Chat | `~~chat` | Slack | Microsoft 365 (Teams) |

## Setup notes

- Each server asks you to sign in (OAuth) the first time it is used. No API keys live in these files.
- Remove any server your team does not use from `.mcp.json`. Fewer connectors means less noise.
- Control what a connector may do (allow, ask, or block per tool) in the connector's own settings.
