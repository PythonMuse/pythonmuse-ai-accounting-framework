# Data Flow Example: Month-End Close

*How data moves through the three tiers during a month-end close process.*

---

## File Flow Diagram

```
data/raw/                          data/processed/                    outputs/
+--------------------------+       +--------------------------+       +---------------------------+
| trial_balance_march.csv  |       | tb_normalized.csv        |       | close_package_march.xlsx  |
| (from ERP)               | ----> | (standardized accounts,  | ----> | (formatted financials)    |
+--------------------------+       |  mapped to reporting)    |       +---------------------------+
                                   +--------------------------+
+--------------------------+       +--------------------------+       +---------------------------+
| ar_subledger_march.csv   |       | flux_analysis.csv        |       | variance_summary.md       |
| (from AR module)         | ----> | (MoM and budget          | ----> | (flagged items for        |
+--------------------------+       |  comparisons)            |       |  management review)       |
                                   +--------------------------+       +---------------------------+
+--------------------------+       +--------------------------+       +---------------------------+
| ap_subledger_march.csv   |       | accrual_calculations.csv |       | journal_entries.csv       |
| (from AP module)         | ----> | (estimated accruals      | ----> | (recommended JEs with     |
+--------------------------+       |  based on rules)         |       |  accounts and amounts)    |
                                   +--------------------------+       +---------------------------+
+--------------------------+
| tb_february.csv          |
| (prior period for flux)  |
+--------------------------+
+--------------------------+
| budget_2026.csv          |
| (annual budget)          |
+--------------------------+
```

---

## Step-by-Step

### Step 1: Raw Data (data/raw/)

Exports collected from source systems at period end:

| File | Source | Contents |
|------|--------|----------|
| trial_balance_march.csv | ERP GL module | Full TB with account, description, debit, credit |
| ar_subledger_march.csv | AR module | Invoice detail with aging |
| ap_subledger_march.csv | AP module | Open payables with aging |
| tb_february.csv | Prior close | February TB for comparison |
| budget_2026.csv | Budget system | Annual budget by account and department |

### Step 2: Processed Data (data/processed/)

Cleaning and calculation scripts transform raw data:

**tb_normalized.csv** -- Trial balance with standardized account mapping, department allocation, and reporting categories.

**flux_analysis.csv** -- Month-over-month comparison (March vs February) and budget-to-actual comparison. Includes dollar and percentage variances, favorable/unfavorable classification.

**accrual_calculations.csv** -- Estimated accruals for recurring items (rent, insurance, utilities) based on defined rules and prior period patterns.

### Step 3: Output Data (outputs/)

Final deliverables for review and distribution:

**close_package_march.xlsx** -- Formatted Excel workbook with:
- Income statement
- Balance sheet
- Department-level P&L
- Supporting schedules

**variance_summary.md** -- Markdown summary of material variances:
- Items exceeding $5,000 or 10% threshold
- Explanation placeholders for each flagged item
- Sorted by magnitude

**journal_entries.csv** -- Recommended adjusting entries:
- Account, description, debit, credit, reference
- Ready for import or manual posting

---

## Traceability

Every number in the close package traces back through the three tiers:

```
Close package balance -> tb_normalized.csv -> trial_balance_march.csv -> ERP
Variance flag         -> flux_analysis.csv -> tb_march + tb_february   -> ERP
Accrual entry         -> accrual_calcs.csv -> business rules + priors  -> Documented assumptions
```

---

*Back to [Data Structure](../)*
