---
name: sql-query-writing
description: >-
  This skill should be used when the user asks to "write a query", "SQL for", "pull the number of", "optimize this query", "why is this query slow", or needs data retrieved from a warehouse.
metadata:
  version: "0.1.0"
---

# SQL Query Writing

## Steps

1. Read `data-team-context` for the SQL dialect, naming conventions, key tables, and metric definitions.
2. Restate the question as: metric, grain, filters, and time window. Ask only if one of these is genuinely ambiguous.
3. Inspect real schemas in ~~data warehouse before writing. Do not guess column names.
4. Write the query with CTEs, short comments, and explicit date ranges.
5. Sanity-check: row counts at each join, duplicate keys, null handling, and time zone.
6. For large tables, add partition or date filters and mention likely cost.

## Output

The query, the assumptions behind it, and two or three ways to validate the result.

Run read-only statements only. Never run DROP, DELETE, UPDATE, or TRUNCATE unless the user explicitly asks.
