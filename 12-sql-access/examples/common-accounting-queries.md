# Common SQL Query Patterns for Accounting

*Practical SQL queries for the most common accounting data needs. Adapt these to your database schema.*

---

## Important Notes

- These queries use standard SQL syntax. Your database may require slight adjustments.
- Replace table and column names with your actual database schema.
- Always test queries on a small date range first.
- Use parameterized queries in Python to prevent SQL injection.

---

## 1. GL Detail for a Date Range

**What it does:** Pulls all general ledger entries for a specific period.

```sql
SELECT
    posting_date,
    account_number,
    account_name,
    description,
    debit,
    credit,
    reference,
    source,
    created_by
FROM gl_detail
WHERE posting_date BETWEEN '2026-03-01' AND '2026-03-31'
ORDER BY posting_date, account_number
```

**Expected output:** Every GL transaction for the period, sorted chronologically.

---

## 2. Trial Balance Summary

**What it does:** Summarizes GL balances by account for a period.

```sql
SELECT
    account_number,
    account_name,
    SUM(debit) AS total_debit,
    SUM(credit) AS total_credit,
    SUM(debit) - SUM(credit) AS net_balance
FROM gl_detail
WHERE posting_date BETWEEN '2026-03-01' AND '2026-03-31'
GROUP BY account_number, account_name
ORDER BY account_number
```

**Expected output:** One row per account with total debits, credits, and net balance.

---

## 3. AR Aging

**What it does:** Lists open (unpaid) invoices with days outstanding.

```sql
SELECT
    invoice_number,
    customer_name,
    invoice_date,
    due_date,
    amount,
    DATEDIFF(day, due_date, GETDATE()) AS days_past_due,
    CASE
        WHEN DATEDIFF(day, due_date, GETDATE()) <= 0 THEN 'Current'
        WHEN DATEDIFF(day, due_date, GETDATE()) <= 30 THEN '1-30 Days'
        WHEN DATEDIFF(day, due_date, GETDATE()) <= 60 THEN '31-60 Days'
        WHEN DATEDIFF(day, due_date, GETDATE()) <= 90 THEN '61-90 Days'
        ELSE 'Over 90 Days'
    END AS aging_bucket
FROM ar_invoices
WHERE payment_date IS NULL
ORDER BY days_past_due DESC
```

**Note:** `DATEDIFF` and `GETDATE()` are SQL Server syntax. For PostgreSQL, use `CURRENT_DATE - due_date`.

---

## 4. AP Aging

**What it does:** Lists open payables with days until due.

```sql
SELECT
    invoice_number,
    vendor_name,
    invoice_date,
    due_date,
    amount,
    DATEDIFF(day, GETDATE(), due_date) AS days_until_due,
    CASE
        WHEN DATEDIFF(day, GETDATE(), due_date) > 30 THEN 'Not Yet Due (30+)'
        WHEN DATEDIFF(day, GETDATE(), due_date) > 0 THEN 'Due Within 30 Days'
        WHEN DATEDIFF(day, GETDATE(), due_date) >= -30 THEN 'Past Due 1-30'
        ELSE 'Past Due 30+'
    END AS status
FROM ap_invoices
WHERE payment_date IS NULL
ORDER BY due_date
```

**Expected output:** Open payables with urgency classification for cash management.

---

## 5. Journal Entries by Source

**What it does:** Lists journal entries filtered by source (manual, system, payroll, etc.)

```sql
SELECT
    je_number,
    posting_date,
    source,
    description,
    created_by,
    approved_by,
    total_debit,
    total_credit
FROM je_header
WHERE posting_date BETWEEN '2026-03-01' AND '2026-03-31'
    AND source = 'Manual'
ORDER BY posting_date
```

**Expected output:** All manual journal entries for the period -- useful for audit review.

---

## 6. Cash Receipts for a Period

**What it does:** Lists all cash received during a period.

```sql
SELECT
    receipt_date,
    customer_name,
    invoice_number,
    receipt_amount,
    payment_method,
    bank_account,
    reference
FROM cash_receipts
WHERE receipt_date BETWEEN '2026-03-01' AND '2026-03-31'
ORDER BY receipt_date
```

**Expected output:** Cash receipt detail for bank reconciliation.

---

## Using These Queries in Python

```python
import pandas as pd
from sqlalchemy import create_engine

# Connect to database
engine = create_engine("your_connection_string")

# Run query and load into DataFrame
query = """
    SELECT account_number, account_name,
           SUM(debit) as total_debit, SUM(credit) as total_credit
    FROM gl_detail
    WHERE posting_date BETWEEN '2026-03-01' AND '2026-03-31'
    GROUP BY account_number, account_name
"""
df = pd.read_sql(query, engine)

# Now you have a programmable trial balance
print(df.head())
```

---

*Back to [SQL Access](../)*
