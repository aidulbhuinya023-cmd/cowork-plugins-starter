---
name: cross-source-search
description: >-
  This skill should be used when the user asks "where is", "find the doc about", "what did we decide about", "search everything for", or any question whose answer may live across chat, docs, email, or tickets.
metadata:
  version: "0.1.0"
---

# Cross-Source Search

## Steps

1. Read `enterprise-search-team-context` for the source-of-truth ranking and internal terminology.
2. Restate the question. Break it into two to four searches using synonyms and internal terms from the glossary.
3. Query every connected source in parallel: ~~chat, ~~knowledge base, ~~file storage, ~~email, ~~project tracker.
4. Remove duplicates. Rank results by source-of-truth order, then recency, then author authority.

## Output

- **Answer first**, in plain language
- **Evidence**: a list of sources with title, link, date, and author
- **Conflicts**: where two sources disagree, and which one the ranking favors
- **Staleness**: any source older than the freshness window in the team context
- **Confidence**: high, medium, or low, and why
- **Not searched**: sources that were not connected or returned nothing

Only surface content the signed-in user can already access. Do not quote private direct messages into shared outputs.
