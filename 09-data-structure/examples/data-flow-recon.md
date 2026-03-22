# Data Flow Example: Bank Reconciliation

*A step-by-step view of how data moves from raw source files to a final reconciliation report.*

---

## File Flow Diagram

```
data/raw/                          data/processed/                    outputs/
+--------------------------+       +--------------------------+       +---------------------------+
| bank_statement_march.csv |       | bank_clean.csv           |       | recon_march.csv           |
| (247 transactions)       | ----> | (standardized columns,   | ----> | (full reconciliation      |
| (original from bank)     |       |  YYYY-MM-DD dates,       |       |  with match status)       |
+--------------------------+       |  consistent signs)        |       +---------------------------+
                                   +--------------------------+
                                                                      +---------------------------+
+--------------------------+       +--------------------------+       | recon_summary_march.md    |
| gl_cash_1010_march.csv   |       | gl_clean.csv             |       | (totals, match rate,      |
| (312 entries)            | ----> | (standardized columns,   | ----> |  outstanding items)       |
| (original from ERP)      |       |  net amount calculated,  |       +---------------------------+
+--------------------------+       |  YYYY-MM-DD dates)        |
                                   +--------------------------+       +---------------------------+
                                                                      | unmatched_items_march.csv |
                                                                      | (items needing review)    |
                                                                      +---------------------------+
```

---

## Step-by-Step

### Step 1: Raw Data (data/raw/)

Place original exports in `data/raw/` without modification.

**bank_statement_march.csv** -- Downloaded directly from the bank portal.
- Columns: date, description, amount (negative = debit, positive = credit)
- 247 transactions

**gl_cash_1010_march.csv** -- Exported from the ERP system.
- Columns: posting_date, vendor_name, description, debit, credit, reference
- 312 entries

These files are never touched again.

### Step 2: Processed Data (data/processed/)

A cleaning script (`src/clean_data.py`) reads from raw and writes to processed:

**bank_clean.csv**
- Column names standardized: date -> transaction_date
- Date format: YYYY-MM-DD
- Amount sign: positive for debits (outflows), negative for credits (inflows) -- matching GL convention
- Empty descriptions filled with "No Description"

**gl_clean.csv**
- Column names standardized
- Net amount calculated: debit - credit
- Date format: YYYY-MM-DD
- 15 entries with April posting dates re-mapped to March based on GL period field

### Step 3: Output Data (outputs/)

The reconciliation script (`src/reconcile.py`) reads from processed and writes to outputs:

**recon_march.csv** -- Full detail with columns:
- bank_date, bank_description, bank_amount
- gl_date, gl_vendor, gl_amount
- match_status (Matched / Unmatched-Bank / Unmatched-GL)
- variance, notes

**recon_summary_march.md** -- Executive summary:
- Total bank transactions: 247
- Total GL entries: 312
- Matched: 243 (98.4%)
- Unmatched bank items: 4
- Unmatched GL items: 3
- Total reconciling difference: $2,525.00

**unmatched_items_march.csv** -- Items requiring investigation:
- 3 items with details and recommended action

---

## Key Principle

At any point, you can trace any output number back to its source:

Output number -> processed file -> raw file -> source system

If someone asks "Where did this $1,200 come from?", you can show the exact path.

---

*Back to [Data Structure](../)*
