---
name: literature-search
description: >-
  This skill should be used when the user asks to "search PubMed", "find papers on", "literature review of", "what's known about", "latest research on", or needs evidence from biomedical literature.
metadata:
  version: "0.1.0"
---

# Literature Search

## Steps

1. Read `bio-research-team-context` for preferred databases, organisms, date limits, and citation style.
2. Build the query with controlled vocabulary (MeSH terms) plus free-text synonyms. Report the exact query used so the search can be repeated.
3. Search ~~literature database. Add ~~preprints and ~~evidence search when connected or relevant.

## Output

A table with: citation, year, study type, key finding, sample size, and PMID or DOI. Then a short synthesis that notes agreement, conflict, and gaps.

## Rules

- Cite only identifiers returned by the tools. **Never invent PMIDs, DOIs, authors, or findings.**
- Label preprints as not peer reviewed.
- State when results are limited to abstracts.
- For research use only. Not medical advice.
