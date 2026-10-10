---
name: ticket-triage
description: >-
  This skill should be used when the user asks to "triage this ticket", "what priority is this", "route this issue", "is this a duplicate", or needs a ticket categorized and assigned.
metadata:
  version: "0.1.0"
---

# Ticket Triage

## Steps

1. Read `customer-support-team-context` for categories, severity definitions, SLAs, and routing rules.
2. Fetch the ticket from ~~support platform, plus the customer's recent history and similar tickets from the last 30 days.
3. Search ~~knowledge base for a matching known issue or article.

## Output

- **Category** and **severity**, with the reason tied to the severity definitions
- **Customer tier and impact**: who is affected and how badly
- **Duplicates or related tickets**, with links
- **Suggested owner or queue**
- **First-response deadline** from the SLA
- **Missing information** to request from the customer

If several similar tickets arrived in a short window, flag a possible incident and say so at the top.
