# Cowork Plugins Starter

A copy-and-customize marketplace of role-based plugins for Claude Code and Claude Cowork.

Everything here is plain markdown and JSON. There is no backend, no build step, and nothing to
compile. A team lead can open a file, add the company's own terminology and ways of working,
and every teammate who installs the plugin gets Claude behaving the way your team actually works.

## What's inside

| Plugin | For | Slash commands | Main connectors |
|--------|-----|----------------|-----------------|
| [`productivity`](plugins/productivity) | Anyone | `/plan-day` `/weekly-review` `/capture` | Slack, Notion, Asana, Linear, Jira, Google Calendar, Gmail, Microsoft 365 |
| [`sales`](plugins/sales) | Sales reps and managers | `/call-prep` `/deal-review` `/draft-follow-up` | HubSpot, Salesforce, Gong, Fireflies, Apollo, ZoomInfo, Slack |
| [`customer-support`](plugins/customer-support) | Support agents and leads | `/triage` `/draft-reply` `/escalate` | Intercom, HubSpot, Guru, Jira, Notion, Slack |
| [`product-management`](plugins/product-management) | Product managers | `/write-prd` `/prioritize` `/synthesize-feedback` | Linear, Jira, Figma, Amplitude, Pendo, Intercom, Notion |
| [`marketing`](plugins/marketing) | Marketers | `/campaign-brief` `/draft-content` `/performance-report` | HubSpot, Canva, Figma, Klaviyo, Ahrefs, Amplitude, Supermetrics |
| [`legal`](plugins/legal) | In-house legal | `/review-contract` `/triage-nda` `/explain-clause` | Box, DocuSign, Google Drive, Microsoft 365, Slack |
| [`finance`](plugins/finance) | Finance and accounting | `/variance` `/draft-je` `/close-status` | BigQuery, Google Drive, Microsoft 365, Slack |
| [`data`](plugins/data) | Analysts | `/write-sql` `/explore-data` `/summarize-insights` | BigQuery, Hex, Amplitude, Jira, Notion, Slack |
| [`enterprise-search`](plugins/enterprise-search) | Everyone | `/find` `/digest` `/who-knows` | Slack, Notion, Guru, Jira, Asana, Google Drive, Box, Microsoft 365 |
| [`bio-research`](plugins/bio-research) | Life science researchers | `/lit-search` `/target-profile` `/trial-landscape` | PubMed, bioRxiv, ChEMBL, Open Targets, ClinicalTrials.gov, Consensus |
| [`plugin-management`](plugins/plugin-management) | Team leads and admins | `/new-plugin` `/customize-plugin` `/audit-plugins` | None |

## What is a plugin?

A plugin is a folder that teaches Claude how to do a specific kind of work for your team. It bundles four things:

| Piece | What it is | Who it's for |
|-------|-----------|--------------|
| **Skills** | Markdown files describing a workflow ("how we prep for a sales call"). Claude loads one automatically when your request matches its description. | Claude |
| **Slash commands** | Short markdown files that give a workflow a name you can type, like `/call-prep Acme`. | You |
| **Connectors** | A `.mcp.json` file listing the tools Claude may connect to (Slack, Notion, Jira, HubSpot and so on). | Claude, after you sign in |
| **Manifest** | `plugin.json`: the plugin's name, version, and description. | The installer |

Plugins can also include agents and hooks. This starter leaves them out on purpose, to keep everything readable by non-engineers.

## Install a plugin

### In Claude Code

Add this repo as a marketplace, then install the plugins you want:

```
/plugin marketplace add YOUR-ORG/cowork-plugins-starter
/plugin install sales@cowork-plugins-starter
```

To try it from a local copy first, point at the folder instead:

```
/plugin marketplace add ./cowork-plugins-starter
```

Then run a command. Claude Code namespaces commands with the plugin name:

```
/sales:call-prep Acme Corp
```

### In Cowork

Cowork installs a plugin from a `.plugin` file, which is just a zip of the plugin folder. Create one:

```bash
cd plugins/sales
zip -r ../../sales.plugin . -x "*.DS_Store"
```

Then add the file from the plugins area in Cowork. Menu names change between releases, so look for
"Plugins" or "Customize". If your organization manages plugins centrally, ask your admin whether the
repo can be added as a shared marketplace. See Anthropic's current Cowork documentation for specifics.

### First run

The first time a plugin uses a connector, Claude asks you to sign in to that service. No passwords or API keys are stored in these files.

## How the folders work

```
cowork-plugins-starter/
├── .claude-plugin/
│   └── marketplace.json         # The catalog: lists every plugin in this repo
├── plugins/
│   └── sales/                   # One folder per plugin (all 11 look like this)
│       ├── .claude-plugin/
│       │   └── plugin.json      # Manifest: name, version, description
│       ├── .mcp.json            # Connector settings (which tools to connect)
│       ├── CONNECTORS.md        # Plain-English map of tool categories and alternatives
│       ├── README.md            # What this plugin does
│       ├── commands/            # Slash commands, one markdown file each
│       │   └── call-prep.md
│       └── skills/              # Skills, one folder each
│           ├── call-prep/
│           │   └── SKILL.md
│           └── sales-team-context/       # <- the folder a team lead edits
│               ├── SKILL.md
│               └── references/
│                   ├── glossary.md
│                   └── ways-of-working.md
├── templates/
│   └── plugin-template/         # Copy this to start a new plugin
└── scripts/
    └── validate.py              # Optional checker (standard library only)
```

### What each file does

| File | Purpose | Edit it to... |
|------|---------|---------------|
| `marketplace.json` | Lists plugins so they can be browsed and installed | Add or remove a plugin |
| `plugin.json` | Names and versions one plugin | Rename it or bump the version |
| `skills/<name>/SKILL.md` | Instructions for one workflow, with a `description` that tells Claude when to use it | Change how a workflow runs |
| `skills/<role>-team-context/` | Your terminology, tone, and rules, read before every task | **Make the plugin yours (start here)** |
| `commands/<name>.md` | A named shortcut that points at a skill | Rename or add shortcuts |
| `.mcp.json` | The connectors to offer | Add or remove tools |
| `CONNECTORS.md` | Explains the `~~category` placeholders used in skills | Keep in sync with `.mcp.json` |

### Skills and commands

Both are markdown. They differ in how they start.

- A **skill** loads on its own when what you type matches its `description` (for example "prep me for my call with Acme"). The description is the most important line in the file, so write it the way people actually talk.
- A **command** is an explicit shortcut you type, like `/call-prep`. In this repo each command is one or two lines that say "use the `call-prep` skill". The real instructions live in the skill, so there is one place to edit.

### The `~~category` placeholders

Skills say `~~chat` or `~~CRM` instead of naming a product. `CONNECTORS.md` explains what each placeholder
means and which tools are pre-configured. This lets one skill serve a Slack team and a Teams team.
If your company only uses one tool per category, find-and-replace the placeholder with the tool's name.

## Customize a plugin (for managers and team leads)

You do not need to be technical. Each plugin has one folder built for you: `skills/<role>-team-context/`.
Claude reads it before doing any work in that plugin.

1. **Open** `plugins/<name>/skills/<name>-team-context/SKILL.md`. Replace each `EDIT ME` with your answer ("Quarter ends March 31", "We use MEDDPICC").
2. **Add your vocabulary** in `references/glossary.md`. One row per term:
   ```
   | Term              | What it means here                              |
   |-------------------|-------------------------------------------------|
   | Atlas             | Our 2026 platform rebuild                       |
   | Green-lit         | Approved by the VP, not yet scheduled           |
   ```
3. **Describe how you work** in `references/ways-of-working.md`: tools of record, standard workflows, tone, and guardrails. Write it like you would brief a new hire.
4. **Trim connectors.** Delete any server in `.mcp.json` your team does not use, and remove its row from `CONNECTORS.md`.
5. **Bump the version** in `.claude-plugin/plugin.json` so teammates know to update.
6. **Test it.** Run one command and see whether Claude used your terms.

When a workflow itself should change (not just the vocabulary), edit the matching `skills/<name>/SKILL.md`.
Keep instructions short, concrete, and in the imperative: "Ask for the renewal date" works better than "It would be good to know the renewal date."

You can also ask Claude to do this with you. Run `/plugin-management:customize-plugin sales` and it will interview you and make the edits.

## Create a new plugin

1. Copy `templates/plugin-template/` to `plugins/<your-plugin-name>/` (kebab-case, for example `hr-onboarding`).
2. Edit `.claude-plugin/plugin.json`: name, description, author.
3. Replace `example-skill` with one skill per workflow. Rename the folder, update `name:` in the frontmatter, and write a `description` that includes phrases people really say.
4. Add a command in `commands/` for each skill you want a shortcut for.
5. Edit `.mcp.json` and `CONNECTORS.md` to list only the tools you use.
6. Fill in the team context skill.
7. Register the plugin in `.claude-plugin/marketplace.json`.
8. Run `python3 scripts/validate.py` and fix anything it reports.

Or run `/plugin-management:new-plugin hr onboarding` and let Claude walk through it.

### Tips for good skills

- **One workflow per skill.** "Contract review" and "NDA triage" are separate skills.
- **Write the description for matching.** Include 3 to 5 quoted phrases a person might say.
- **Say what the output looks like.** Sections, length, and format.
- **Say what to do when information is missing.** "Write 'unknown'. Do not guess."
- **Draft, then ask.** Anything that sends, posts, or changes a record should require a yes.
- **Keep it short.** Under about 2,000 words. Move long reference material into `references/`.

## Connectors and permissions

- Connectors use each service's official MCP server and sign-in. Claude only sees what the signed-in person can already see.
- Some services (Microsoft 365, Salesforce) need an admin to enable the connector for your organization before individuals can sign in.
- Warehouses and lab systems with account-specific URLs (Snowflake, Databricks, Benchling) are not pre-configured. Add yours as another `http` entry in `.mcp.json`.
- You control what each connector may do (allow, ask, or block per tool) in the connector's settings. Start restrictive, especially for finance, legal, and HR data.
- Connector URLs were checked against Anthropic's public knowledge-work-plugins repository when this starter was built. Vendors do change endpoints, so if a connector fails to load, check the vendor's current MCP documentation first.

Every skill also works with nothing connected. Paste text or upload a file and Claude works from that.

## Safety notes

- The legal, finance, and bio-research plugins produce **assistive analysis for expert review**. They are not legal, accounting, or medical advice, and each says so.
- Skills are written to draft first and ask before sending, posting, or editing records. Keep that habit when you customize them.
- Never put passwords, API keys, or customer personal data in any file in this repo.

## Validate (optional)

```bash
python3 scripts/validate.py          # check everything
python3 scripts/validate.py sales    # check one plugin
```

The script needs only Python 3. It checks manifests, skill and command frontmatter, connector JSON,
that every `~~placeholder` is defined, and that each plugin is listed in the marketplace. It also counts
how many `EDIT ME` placeholders are left in each plugin.

## Share with your team

1. Fork or copy this repo into your organization.
2. Customize the plugins your teams need. Delete the rest from `plugins/` and `marketplace.json`.
3. Share the install commands from the section above.
4. Change plugins through pull requests, with one reviewer and a version bump.

## License

MIT. See `LICENSE`. Replace the copyright line with your own.
