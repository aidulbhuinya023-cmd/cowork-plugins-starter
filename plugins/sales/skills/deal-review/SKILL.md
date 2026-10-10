---
name: deal-review
description: >-
  This skill should be used when the user asks to "review this deal", "is this deal real", "deal health check", "will this close this quarter", or wants a candid assessment of an opportunity.
metadata:
  version: "0.1.0"
---

# Deal Review

Assess a single opportunity honestly. Do not inflate.

## Steps

1. Load the opportunity, its activity history, stakeholders, and notes from ~~CRM.
2. Read `sales-team-context` for the qualification framework. Score each element as **evidence**, **gap**, or **unknown**, with the source for each.
3. Check these basics: Is there a dated next step? Is the deal multi-threaded? Are the decision process and paper process known? Is there a champion? Does the close date follow from the evidence?

## Output

- **Verdict**: on track, at risk, or stalled
- **Evidence for**
- **Gaps**
- **Slip risk**: reasons, in order of likelihood
- **Three actions**: each with an owner and a date

Do not update the ~~CRM unless the user asks.
