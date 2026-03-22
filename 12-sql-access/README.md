# SQL Access -- Working With IT for Direct Database Access

*Instead of manual exports, ask for read-only SQL access. It changes everything.*

---

## The Problem with Manual Exports

Every month, the process looks the same:

1. Log into the ERP
2. Navigate to the report
3. Set the date range
4. Export to Excel
5. Clean up the export (remove headers, fix formatting)
6. Save as CSV
7. Import into your analysis

That is seven steps of manual work -- every single time. And if you need to adjust the date range or add a filter? Start over.

---

## The Better Way: Read-Only SQL Access

Ask IT for read-only access to the database behind your ERP system. With that access, you can:

- Pull exactly the data you need with a single query
- Automate the extraction (run the same query every month)
- Skip the export-clean-import cycle entirely
- Work with live data instead of stale exports

**The data flow becomes:**

```
SQL Database --> Python --> DataFrame --> Analysis --> Output
```

No manual exports. No cleaning steps. Repeatable every time.

---

## How to Frame the Request

IT departments are understandably cautious about database access. Frame your request around safety and specificity:

**Key points:**
- Read-only access (SELECT statements only -- no ability to modify data)
- Specific databases and tables (not blanket access to everything)
- For analysis purposes only (not replacing any system functions)
- You can discuss specific queries you plan to run

See [sample-it-request.md](examples/sample-it-request.md) for an email template.

---

## What Is a DataFrame?

When you pull data from SQL into Python, it lands in something called a **DataFrame**.

The simplest definition: **a DataFrame is an Excel table, but programmable and repeatable.**

It has rows and columns. You can filter, sort, group, and calculate -- just like Excel. The difference is that every operation is a line of code, which means it can be repeated, documented, and audited.

---

## Common Scenarios for SQL Access

| Scenario | What You Query | Why It Helps |
|----------|---------------|-------------|
| GL detail for analysis | General ledger transactions table | Faster than exporting reports |
| Trial balance | GL balances by account and period | Real-time balance verification |
| AR aging | Open invoices with dates | Automated aging calculations |
| AP aging | Open payables with due dates | Cash flow analysis |
| Journal entries by source | JE header and detail tables | Audit trail and review |
| Cash receipts | Cash receipt transactions | Bank reconciliation |

---

## Security Considerations

- **Read-only only.** Never request write access unless absolutely necessary and approved.
- **Parameterized queries.** Use parameters instead of string formatting to prevent SQL injection.
- **No hardcoded credentials.** Store connection strings in environment variables, not in your scripts.
- **Close connections.** Always close your database connection after you are done.

---

## Start Small

Do not ask for access to every database on day one. Start with:

1. **One database** (the one behind your primary ERP or GL)
2. **One table** (GL detail or trial balance)
3. **One query** (a simple SELECT for a specific period)
4. **One report** (replace one manual export with an automated query)

Demonstrate the value. Then expand.

---

## Examples

| File | What It Covers |
|------|---------------|
| [sql-to-dataframe.py](examples/sql-to-dataframe.py) | Complete example: SQL query to pandas DataFrame |
| [sample-it-request.md](examples/sample-it-request.md) | Email template for requesting SQL access |
| [common-accounting-queries.md](examples/common-accounting-queries.md) | Common SQL patterns for accounting |

---

*Next: [Skills, Agents, and Models](../13-skills-agents-models/) -- reusable logic and choosing the right AI.*
