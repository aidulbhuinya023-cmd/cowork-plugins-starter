---
name: response-drafting
description: >-
  This skill should be used when the user asks to "draft a reply", "write a response to this customer", "answer this ticket", or needs a customer-facing message grounded in the knowledge base.
metadata:
  version: "0.1.0"
---

# Response Drafting

## Steps

1. Read the ticket and the thread so far. Identify what the customer actually asked.
2. Search ~~knowledge base for the official answer. Link the article when one exists.
3. Draft the reply using the tone guide in `customer-support-team-context`:
   - Acknowledge the specific problem in one sentence
   - Give the answer first, then numbered steps
   - Set a realistic expectation for timing
   - Close with what happens next
4. Offer a shorter version suitable for live chat.

## Guardrails

- Do not promise refunds, credits, roadmap dates, or timelines unless the team context says agents may.
- If the reply needs approval, say so at the top and explain why.
- Never include internal notes or other customers' details in the draft.
