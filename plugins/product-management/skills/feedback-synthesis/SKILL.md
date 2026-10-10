---
name: feedback-synthesis
description: >-
  This skill should be used when the user asks to "synthesize feedback", "what are customers saying", "themes from these interviews", "summarize feature requests", or has transcripts, tickets, or survey data to analyze.
metadata:
  version: "0.1.0"
---

# Feedback Synthesis

## Steps

1. Collect inputs from ~~customer feedback, call transcripts, support tickets, ~~chat channels, or files the user provides.
2. Cluster into themes. Separate **requests** (what they asked for) from **problems** (what they are trying to do).
3. Count **unique customers**, not mentions. Segment by plan or tier using the team context.
4. Use short paraphrases or quotes of fewer than 15 words as examples.

## Output

A table of themes: theme, number of customers, segments, example, suggested action. Then list contradictions in the data and gaps in coverage (who we did not hear from).
