# Skill Definition: Variance Analysis

*A reusable skill for performing budget vs actuals variance analysis.*

> **Validate with sample data first.** Before running this skill against real budget and actuals files, test it end-to-end with synthetic or masked data. This ensures the variance logic, thresholds, and outputs work as expected before real financial data is involved. See [Safe AI Data Workflows](https://github.com/PythonMuse/ai-ledger/tree/main/articles/06-safe-ai-data-workflows). Once validated, log the skill as part of your AI governance process — see [AI Governance for Controllers](https://github.com/PythonMuse/ai-ledger/tree/main/articles/07-ai-governance-for-controllers).

---

## Skill Name
Budget vs Actuals Variance Analysis

## Description
Compare budget to actuals for a reporting period. Calculate dollar and percentage variances, classify as favorable or unfavorable, flag exceptions, and produce a management-ready summary.

## When to Use
- Monthly close: management reporting and variance commentary
- Quarterly review: board and executive reporting
- Ad hoc: investigating specific cost center or account variances

---

## Input Requirements

| Input | Format | Location | Required |
|-------|--------|----------|----------|
| Budget data | CSV with columns: account_number, account_name, department, budget_amount | data/raw/ | Yes |
| Actuals data | CSV with columns: account_number, account_name, department, actual_amount | data/raw/ | Yes |
| Prior period actuals | CSV (optional, for trend analysis) | data/raw/ | No |

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| Dollar threshold | $5,000 | Flag variances exceeding this amount |
| Percentage threshold | 10% | Flag variances exceeding this percentage |
| Revenue account range | 4000-4999 | Accounts classified as revenue |
| Expense account range | 5000-9999 | Accounts classified as expenses |

---

## Steps

1. **Read source files** from data/raw/. Do not modify originals.
2. **Join budget and actuals** on account_number. Flag accounts that exist in one file but not the other.
3. **Calculate dollar variance:** actual_amount - budget_amount.
4. **Calculate percentage variance:** dollar_variance / budget_amount. Handle zero-budget accounts.
5. **Classify variances:**
   - Revenue: favorable when actual > budget
   - Expense: favorable when actual < budget
6. **Flag for review** when |dollar_variance| > threshold OR |pct_variance| > threshold.
7. **Generate outputs:**
   - Full variance detail (CSV)
   - Management summary (Markdown) with totals and top variances
8. **Save all outputs** to outputs/.
9. **Update status_update.md.**

---

## Output Format

### variance_report_[period].csv
| Column | Description |
|--------|-------------|
| account_number | GL account number |
| account_name | Account description |
| department | Department or cost center |
| budget_amount | Budget for the period |
| actual_amount | Actual for the period |
| dollar_variance | Actual minus budget |
| pct_variance | Dollar variance / budget (percentage) |
| favorable_unfavorable | Favorable / Unfavorable / On Budget |
| flag | "Review Required" or blank |
| notes | New account, no activity, or other observations |

### variance_summary_[period].md
- Total revenue: budget vs actual
- Total expenses: budget vs actual
- Net income variance
- Count of flagged items
- Top 5 unfavorable variances by dollar amount
- Top 5 unfavorable variances by percentage

---

## Review Checklist

- [ ] Budget totals match the approved budget
- [ ] Actual totals match the trial balance for the period
- [ ] Revenue and expense classifications are correct
- [ ] Favorable/unfavorable designations make sense
- [ ] Flagged items have reasonable explanations or are escalated
- [ ] No accounts are missing from either side
- [ ] Summary totals reconcile to detail

---

*Back to [Skills, Agents, and Models](../)*
