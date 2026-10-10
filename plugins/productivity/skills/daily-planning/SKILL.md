---
name: daily-planning
description: >-
  This skill should be used when the user asks to "plan my day", "what's on my plate", "morning briefing", "prioritize my tasks", or wants a prioritized agenda built from their calendar, tasks, and messages.
metadata:
  version: "0.1.0"
---

# Daily Planning

Build a realistic, prioritized plan for the user's day.

## Steps

1. Read `productivity-team-context` for priority labels, working hours, and focus-time rules.
2. Gather inputs from whatever is connected:
   - ~~calendar: today's meetings and the gaps between them
   - ~~project tracker: tasks assigned to the user that are due today, overdue, or flagged high priority
   - ~~chat and ~~email: direct mentions and unanswered questions from the last 24 hours
3. If a source is not connected, ask the user to paste it or skip it. Never invent meetings or tasks.
4. Rank work by deadline, impact, and who is waiting. Protect the focus blocks defined in the team context.

## Output

- **Top 3 priorities**: one line each, with why it matters today
- **Schedule**: meetings and proposed focus blocks in time order
- **Needs a reply**: people waiting on the user, oldest first
- **Can wait or be delegated**: with a suggested owner

Keep it to one screen. Offer to create tasks or draft replies. Do not send or create anything unless asked.
