---
name: journal-entry-prep
description: >-
  This skill should be used when the user asks to "draft a journal entry", "prepare accruals", "book this adjustment", "reclass these amounts", or needs entries prepared for accounting review.
metadata:
  version: "0.1.0"
---

# Journal Entry Preparation

Prepare entries for human review. Never post them.

## Steps

1. Read `finance-team-context` for the chart of accounts, entry format, and approval thresholds.
2. For each entry, list: date, accounts, debit, credit, amount, memo, and a reference to the supporting document.
3. Verify total debits equal total credits. Show the check.
4. Mark entries that auto-reverse next period.
5. Compare each amount to the approval thresholds and name the required approver.
6. List missing support documents.

Output a table that can be pasted into the ledger import template, followed by any open questions.
