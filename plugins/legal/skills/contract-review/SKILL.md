---
name: contract-review
description: >-
  This skill should be used when the user asks to "review this contract", "redline this agreement", "check this MSA against our playbook", "what are the risks in this contract", or uploads a contract for analysis.
metadata:
  version: "0.1.0"
---

# Contract Review

Assistive analysis only. A licensed attorney makes the final call.

## Steps

1. Read `legal-team-context` for the playbook (standard, fallback, and walk-away positions), the approval matrix, and approved templates.
2. Identify contract type, parties, and which side the company is on.
3. Read the whole document before judging any clause.
4. Compare each clause the playbook covers. Rate it **Green** (acceptable), **Yellow** (negotiate), or **Red** (escalate).
5. For Yellow and Red, propose redline language starting with the fallback position.
6. List clauses the playbook expects that are missing.

## Output

- **Summary up top**: term, renewal, fees, liability cap, indemnities, termination, governing law
- **Issues table**: clause, rating, why, proposed language
- **Escalations**: what needs a named approver, per the approval matrix

End with: "Assistive analysis for attorney review. Not legal advice." Never send anything to a counterparty.
