---
name: variance-analysis
description: >-
  This skill should be used when the user asks for "variance analysis", "actual vs budget", "why is revenue down", "explain the P&L movement", or wants financial results compared to a plan or prior period.
metadata:
  version: "0.1.0"
---

# Variance Analysis

## Steps

1. Read `finance-team-context` for the chart of accounts, materiality thresholds, and fiscal calendar.
2. Get actuals and the comparison (budget, forecast, or prior period) from ~~data warehouse or an uploaded spreadsheet.
3. Compute dollar and percent variance for every line.
4. Explain only variances above the materiality thresholds. Decompose into price, volume, mix, and timing where the data allows. Separate one-time items from run-rate.

## Output

- A variance table sorted by absolute size
- Three to five bullets of narrative
- **Questions for budget owners** where the data cannot explain a movement

Show the formulas or SQL used so a reviewer can reproduce every number. Write "needs owner input" instead of guessing at causes.
