# Bio Research plugin

Search the literature, look up targets and compounds, and map clinical trial landscapes using PubMed, bioRxiv, ChEMBL, Open Targets, and ClinicalTrials.gov. For research use only.

## Slash commands

| Command | What it does |
|---------|--------------|
| `/lit-search` | Search the literature on a question |
| `/target-profile` | Profile a target with disease and compound evidence |
| `/trial-landscape` | Map clinical trials for a condition or drug |

## Skills

| Skill | What it covers |
|-------|----------------|
| `literature-search` | Structured literature search with a reproducible query and ID-backed citations |
| `target-and-compound-lookup` | Target-disease evidence and compound activity summaries |
| `trial-landscape` | Maps trials for a condition or intervention |
| `bio-research-team-context` | **Edit this one.** Your terminology, workflows, tone, and guardrails |

## Connectors

Configured in `.mcp.json`: PubMed, bioRxiv, Consensus, Open Targets, ChEMBL, ClinicalTrials.gov, BioRender.
See `CONNECTORS.md` for categories, alternatives, and setup notes.

## Make it yours (5 minutes)

1. Open `skills/bio-research-team-context/SKILL.md` and replace each `EDIT ME`.
2. Add your team's terms to `skills/bio-research-team-context/references/glossary.md`.
3. Describe how your team works in `skills/bio-research-team-context/references/ways-of-working.md`.
4. Delete servers you do not use from `.mcp.json`.
5. Bump `version` in `.claude-plugin/plugin.json` so teammates know it changed.
