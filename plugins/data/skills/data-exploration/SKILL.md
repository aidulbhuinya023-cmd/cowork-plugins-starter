---
name: data-exploration
description: >-
  This skill should be used when the user asks to "explore this dataset", "profile this table", "what's in this data", "check data quality", or uploads a CSV to understand before analysis.
metadata:
  version: "0.1.0"
---

# Data Exploration

## Steps

1. Identify the table, file, or query to profile. Sample if it is very large and say that you did.
2. Report: row count, grain and key uniqueness, null rate per column, distinct counts, min and max, value distributions, date coverage, and outliers.
3. Flag suspicious values: placeholders, impossible dates, duplicates, and sudden shifts in volume.

## Output

- A one-screen profile table
- Data quality issues ranked by how much they could distort analysis
- Three suggested questions the data can answer well, and one it cannot
