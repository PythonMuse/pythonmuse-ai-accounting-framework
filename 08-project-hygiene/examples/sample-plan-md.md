# Project Plan: March 2026 Bank Reconciliation

---

## Project Objective

Reconcile the operating cash account (GL 1010) to the March 2026 bank statement. Identify and resolve all reconciling items. Produce a final reconciliation report suitable for month-end close workpapers.

---

## Data Sources

| Source | File | Location | Format |
|--------|------|----------|--------|
| Bank statement | bank_statement_march.csv | data/raw/ | CSV |
| GL detail | gl_cash_1010_march.csv | data/raw/ | CSV |
| Prior month recon | recon_february.csv | data/raw/ | CSV |

---

## Rules and Constraints

- Match transactions by amount and date (3 business day tolerance)
- Materiality threshold: $500 (items below this can be grouped)
- Bank statement uses negative amounts for debits, positive for credits
- GL uses separate debit and credit columns
- Never modify files in data/raw/
- All outputs saved to outputs/

---

## Steps

1. Import bank statement and GL detail into pandas DataFrames
2. Standardize column names and date formats
3. Convert bank amounts to match GL sign convention
4. Match transactions by amount and date
5. Identify unmatched items on both sides
6. Investigate unmatched items over $500
7. Check against prior month's outstanding items
8. Generate reconciliation report (CSV)
9. Generate summary (Markdown)
10. Update status_update.md

---

## Expected Outputs

| File | Description | Location |
|------|-------------|----------|
| recon_march.csv | Full reconciliation detail | outputs/ |
| recon_summary_march.md | Executive summary with totals | outputs/ |
| unmatched_items_march.csv | Items requiring investigation | outputs/ |

---

## Assumptions

- Bank statement is complete for the full month (3/1 - 3/31)
- GL is posted through 3/31 with no pending entries
- Prior month reconciliation was completed and is available for outstanding item comparison
