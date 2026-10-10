---
name: target-and-compound-lookup
description: >-
  This skill should be used when the user asks about "target profile for", "is this gene associated with", "known inhibitors of", "compound activity", "tractability", or needs target, disease, or compound evidence.
metadata:
  version: "0.1.0"
---

# Target and Compound Lookup

## Steps

1. Use ~~target database to retrieve target-disease associations, evidence types, and tractability.
2. Use ~~compound database to retrieve known compounds, activity values with units and assay type, and clinical phase.
3. Cross-check key claims against ~~literature database.

## Output

- **Target summary**: identifiers, function, strongest disease associations, evidence type for each
- **Compounds**: ID, activity value and unit, assay, clinical phase
- **Evidence strength**: strong, moderate, or weak, with the reason
- **Gaps and caveats**: assay context, species, data age

Copy identifiers (Ensembl, ChEMBL, and similar) exactly from tool results. Do not fill in from memory.
