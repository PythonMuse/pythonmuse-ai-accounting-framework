# Skill Definition: Bank Reconciliation

*A reusable skill definition that can be given to an AI assistant for performing bank reconciliations.*

> **Validate with sample data first.** Before running this skill against real bank statements and GL exports, test it end-to-end with synthetic or masked data. This ensures the matching logic, thresholds, and outputs work as expected before real financial data is involved. See [Safe AI Data Workflows](https://github.com/PythonMuse/ai-ledger/tree/main/articles/06-safe-ai-data-workflows). Once validated, log the skill as part of your AI governance process — see [AI Governance for Controllers](https://github.com/PythonMuse/ai-ledger/tree/main/articles/07-ai-governance-for-controllers).

---

## Skill Name
Bank Account Reconciliation

## Description
Reconcile a bank statement against the general ledger cash account by matching transactions, identifying discrepancies, and producing a reconciliation report.

## When to Use
- Monthly close: reconcile each bank account to the corresponding GL cash account
- Ad hoc: when investigating cash discrepancies outside of regular close

---

## Input Requirements

| Input | Format | Location | Required |
|-------|--------|----------|----------|
| Bank statement | CSV with columns: date, description, amount | data/raw/ | Yes |
| GL cash detail | CSV with columns: posting_date, vendor, debit, credit, reference | data/raw/ | Yes |
| Prior month outstanding items | CSV (optional) | data/raw/ | No |

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| Date tolerance | 3 business days | Maximum date difference for a match |
| Materiality threshold | $500 | Unmatched items below this are grouped |
| Bank sign convention | Negative = debit | How the bank formats outflows |

---

## Steps

1. **Read source files** from data/raw/. Do not modify originals.
2. **Standardize data.** Clean column names, convert dates to YYYY-MM-DD, normalize amount signs.
3. **Save cleaned data** to data/processed/.
4. **Match transactions** by amount and date within the tolerance window.
5. **Identify unmatched items** on both sides (bank and GL).
6. **Compare against prior month outstanding** items (if provided). Mark items that cleared.
7. **Group immaterial items** below the materiality threshold.
8. **Flag items for review** that exceed thresholds or show unusual patterns.
9. **Generate outputs:**
   - Full reconciliation detail (CSV)
   - Executive summary (Markdown)
   - Unmatched items requiring investigation (CSV)
10. **Save all outputs** to outputs/.
11. **Update status_update.md** with session results.

---

## Output Format

### recon_[period].csv
| Column | Description |
|--------|-------------|
| bank_date | Transaction date from bank |
| bank_description | Bank transaction description |
| bank_amount | Bank transaction amount |
| gl_date | GL posting date |
| gl_vendor | GL vendor/description |
| gl_amount | GL entry amount |
| match_status | Matched / Unmatched-Bank / Unmatched-GL |
| variance | Difference if amounts are close but not exact |
| notes | Flags, observations, prior month carry-forward |

### recon_summary_[period].md
- Total bank transactions and GL entries
- Match count and rate
- Unmatched items by category
- Total reconciling difference
- Items flagged for review

---

## Review Checklist

Before accepting the reconciliation output:

- [ ] Total bank balance per statement agrees to the bank_amount column total
- [ ] Total GL balance agrees to the gl_amount column total
- [ ] Match count is reasonable (expect 90%+ for most accounts)
- [ ] Unmatched items are individually reviewed
- [ ] No items are double-matched
- [ ] Prior month outstanding items are properly resolved
- [ ] Summary totals reconcile to the detail file

---

*Back to [Skills, Agents, and Models](../)*
