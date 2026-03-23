# Skill Template

*Copy this template to define a new reusable AI skill for your accounting workflows.*

> **Validate with sample data first.** Before running any new skill against real company data, test it end-to-end with synthetic or masked files. This confirms the logic, thresholds, and outputs work as expected before real financial data is involved. See [Safe AI Data Workflows](https://github.com/PythonMuse/ai-ledger/tree/main/articles/06-safe-ai-data-workflows). Once validated, log the skill as part of your AI governance process — see [AI Governance for Controllers](https://github.com/PythonMuse/ai-ledger/tree/main/articles/07-ai-governance-for-controllers).

---

## Skill Name
[Name of the skill]

## Description
[One or two sentences describing what this skill does.]

## When to Use
- [Scenario 1]
- [Scenario 2]

---

## Input Requirements

| Input | Format | Location | Required |
|-------|--------|----------|----------|
| [Data file 1] | [CSV/Excel/PDF] | [data/raw/] | [Yes/No] |
| [Data file 2] | [CSV/Excel/PDF] | [data/raw/] | [Yes/No] |

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| [Parameter 1] | [value] | [what it controls] |
| [Parameter 2] | [value] | [what it controls] |

---

## Steps

1. [Step 1]
2. [Step 2]
3. [Step 3]
4. [Step 4]
5. [Step 5]
6. Save all outputs to outputs/
7. Update status_update.md

---

## Output Format

### [output_filename]
| Column | Description |
|--------|-------------|
| [column 1] | [what it contains] |
| [column 2] | [what it contains] |

---

## Review Checklist

Before accepting the output:

- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]
- [ ] [Check 4]

---

## Notes and Constraints

- [Any special considerations]
- [Known limitations]
- [Dependencies on other skills or processes]

---

*Template from the [PythonMuse AI Accounting Framework](https://github.com/PythonMuse/pythonmuse-ai-accounting-framework)*
