---
name: month-end-close
description: >-
  This skill should be used when the user asks for "close status", "month-end checklist", "what's blocking the close", "close update", or wants close tasks tracked and summarized.
metadata:
  version: "0.1.0"
---

# Month-End Close

## Steps

1. Read the close calendar in `finance-team-context`.
2. Build or update a task table: task, owner, due date, status (not started, in progress, blocked, done), and dependency. Use the team's own close tracker if one is named in the team context; otherwise keep the table in `CLOSE-STATUS.md` in the working folder.
3. Highlight blockers and the tasks they hold up.
4. List open reconciliations and accruals still to review.
5. Write a short status update suitable for ~~chat: percent complete, risks, and what is needed from whom.

Do not mark a task done without the owner's confirmation.
