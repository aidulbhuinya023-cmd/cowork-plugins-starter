---
name: knowledge-digest
description: >-
  This skill should be used when the user asks to "catch me up on", "what's happened with", "summarize the history of", "status of this project across teams", or needs a digest of a topic over time.
metadata:
  version: "0.1.0"
---

# Knowledge Digest

## Steps

1. Default the window to the last 30 days unless the user gives one.
2. Run the search procedure in `cross-source-search` for the topic.
3. Assemble a digest.

## Output

- **Timeline**: dated events, oldest first
- **Decisions made**: with who decided and where it is recorded
- **Open questions**
- **Owners** and **upcoming dates**
- **Where to read more**: five links at most
