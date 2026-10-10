---
name: task-management
description: >-
  This skill should be used when the user asks to "add a task", "remind me to", "what am I waiting on", "triage my to-dos", "clean up my task list", or "weekly review".
metadata:
  version: "0.1.0"
---

# Task Management

Capture, organize, and review the user's tasks.

## Where tasks live

- If ~~project tracker is connected, treat it as the source of truth for the tasks it owns.
- Otherwise keep a `TASKS.md` file in the working folder with this layout:

```
## Today
- [ ] Task - due Fri - link or context
## This week
## Waiting on
- [ ] Item - person - asked on 2025-01-06
## Later
## Done
```

## Rules

- When the user says "add a task", create it immediately with a clear verb-first title. Add an owner and due date only if stated or obvious. Ask a question only if the task is ambiguous.
- For a weekly review: move finished items to Done, flag anything overdue, surface "Waiting on" items older than the follow-up window in the team context, and propose the next week's top 5.
- Never delete tasks. Move them to Done or Later.
