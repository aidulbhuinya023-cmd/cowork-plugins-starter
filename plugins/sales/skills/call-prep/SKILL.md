---
name: call-prep
description: >-
  This skill should be used when the user asks to "prep for a call", "call prep", "brief me on this account", "get me ready for my meeting with", or needs background on a prospect before a conversation.
metadata:
  version: "0.1.0"
---

# Call Prep

Produce a one-page brief the rep can read in two minutes.

## Steps

1. Identify the account, the contact, and the call time. Ask if any is missing.
2. Read `sales-team-context` for the qualification framework, ideal customer profile, and product names.
3. Gather, from whatever is connected:
   - ~~CRM: account record, open opportunities, last five activities, contacts and roles
   - ~~conversation intelligence: summaries of previous calls
   - ~~email and ~~chat: recent threads with this account
   - ~~data enrichment: company news, funding, headcount
4. Write the brief.

## Output

- **Snapshot**: who they are, size, stage, owner
- **Where we left off**: last interaction and any commitments
- **Stakeholders**: name, role, stance, last contact
- **Goals for this call**: what a good outcome looks like
- **Suggested agenda**: three to five items
- **Discovery questions**: at most five, aimed at gaps in the qualification framework
- **Likely objections**: with a short response for each
- **Next step to ask for**

Write "unknown" for anything not found. Do not guess.
