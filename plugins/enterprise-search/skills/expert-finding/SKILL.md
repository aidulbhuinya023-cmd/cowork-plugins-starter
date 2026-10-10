---
name: expert-finding
description: >-
  This skill should be used when the user asks "who knows about", "who owns", "who should I ask about", or needs the right person for a question.
metadata:
  version: "0.1.0"
---

# Expert Finding

## Steps

1. Check the ownership table in `enterprise-search-team-context` first.
2. Look for evidence in connected sources: document authorship and edits, ticket assignees, active chat participants, meeting organizers.
3. Return the top three people.

## Output

For each person: name, role if known, the specific evidence, and a suggested first question. Prefer people with recent activity. Say plainly when evidence is thin.
