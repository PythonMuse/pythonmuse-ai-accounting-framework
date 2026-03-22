# Audit Workpaper Template

*A structured Markdown template for documenting accounting procedures and findings.*

---

## Workpaper Header

| Field | Value |
|-------|-------|
| **Entity** | [Company Name] |
| **Period** | [Month/Quarter/Year] |
| **Workpaper** | [Reference Number, e.g., A-101] |
| **Prepared By** | [Name] |
| **Date Prepared** | [YYYY-MM-DD] |
| **Reviewed By** | [Name] |
| **Date Reviewed** | [YYYY-MM-DD] |

---

## Objective

[State the purpose of this workpaper. What are you testing, verifying, or documenting?]

Example: *To reconcile the operating cash account (1010) to the bank statement for the period ending March 31, 2026, and to identify and resolve all reconciling items.*

---

## Procedures Performed

1. [Describe step 1]
2. [Describe step 2]
3. [Describe step 3]

Example:
1. Obtained bank statement for the period from Treasury
2. Exported GL detail for account 1010 from ERP system
3. Matched transactions by amount and date using AI-assisted reconciliation script
4. Investigated unmatched items exceeding $500 materiality threshold
5. Prepared reconciling items schedule

---

## Data Sources

| Source | File Name | Location | Date Obtained |
|--------|-----------|----------|---------------|
| [Source system] | [filename.csv] | [data/raw/] | [YYYY-MM-DD] |
| [Source system] | [filename.csv] | [data/raw/] | [YYYY-MM-DD] |

---

## Results and Findings

### Summary

| Metric | Value |
|--------|-------|
| Total bank transactions | [count] |
| Total GL transactions | [count] |
| Matched items | [count] |
| Unmatched items | [count] |
| Total reconciling difference | [$amount] |

### Reconciling Items

| # | Description | Amount | Status | Resolution |
|---|-------------|--------|--------|------------|
| 1 | [Description] | [$amount] | [Open/Resolved] | [How it was resolved] |
| 2 | [Description] | [$amount] | [Open/Resolved] | [How it was resolved] |

### Exceptions Noted

[Describe any exceptions, unusual items, or matters requiring follow-up.]

---

## Conclusions

[State your conclusion based on the work performed.]

Example: *The operating cash account reconciles to the bank statement within the materiality threshold of $500. Three reconciling items totaling $1,245 were identified and resolved. No exceptions were noted that require further investigation.*

---

## Output Files

| File | Description | Location |
|------|-------------|----------|
| [filename] | [what it contains] | [outputs/] |

---

## Sign-Off

- [ ] Workpaper prepared and self-reviewed
- [ ] Supporting documentation attached or referenced
- [ ] All reconciling items investigated and documented
- [ ] Conclusions supported by evidence
- [ ] Ready for reviewer

---

*Template from the [PythonMuse AI Accounting Framework](https://github.com/PythonMuse/pythonmuse-ai-accounting-framework)*
