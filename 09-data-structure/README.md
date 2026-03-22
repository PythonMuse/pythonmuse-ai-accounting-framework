# Data Structure -- Raw vs Processed vs Output

*One of the first things we learn in accounting: never overwrite source data. Apply the same discipline to AI projects.*

---

## The Three-Tier Structure

Every accounting AI project should separate data into three tiers:

```
data/
├── raw/          Source of truth. Never modify.
├── processed/    Cleaned, transformed, standardized.
└── outputs/      Final reports and deliverables.
```

This is not a developer convention. It is an accounting convention applied to data workflows.

---

## The Accounting Analogy

| Data Tier | Accounting Equivalent | Rule |
|-----------|----------------------|------|
| **raw/** | Original bank statement, source document | Never alter the original |
| **processed/** | Reconciliation worksheet, working papers | Transform and analyze here |
| **outputs/** | Final reconciliation report, financial statements | Deliverable to stakeholders |

You would never write adjustments directly on an original bank statement. You work on a copy, track your changes on a worksheet, and produce a final report. AI data workflows follow the same principle.

---

## Why This Matters

### Auditability

When someone asks "How was this number calculated?", you can trace the path:

1. Raw data came from [source system], unchanged in `data/raw/`
2. It was cleaned and standardized in `data/processed/`
3. The final report in `outputs/` was generated from the processed data

Every step is documented. Every file is preserved.

### Reproducibility

If you need to re-run the analysis -- next month, next quarter, or because an assumption changed -- you start from `data/raw/` and run the same process. The result should be identical (or you can explain exactly why it changed).

### Traceability

If an output number looks wrong, you can trace backward: output file to processed file to raw file. If the raw file is intact, the issue is in your transformation logic. If the raw file was modified, you have a bigger problem -- which is exactly why you do not modify it.

---

## Common Mistakes

### Modifying Raw Data
Resist the urge to "fix" a CSV in `data/raw/`. If dates need reformatting or columns need renaming, do it in a script that reads from `raw/` and writes to `processed/`.

### Saving Outputs Over Inputs
Never save your analysis results back into `data/raw/`. If your script accidentally overwrites source data, you cannot recover or reproduce your work.

### Mixing Tiers
Keep processed files in `processed/` and outputs in `outputs/`. If intermediate working files are mixed with final deliverables, it is hard to tell what is draft and what is final.

### No Clear Naming
Use file names that indicate the tier, date, or version:
- `data/raw/bank_statement_march_2026.csv` (clear source)
- `data/processed/bank_clean_march_2026.csv` (clearly processed)
- `outputs/recon_report_march_2026.csv` (clearly final)

---

## Setting Up Your First Data Pipeline

A data pipeline is just a fancy name for the flow from raw data to final output. Here is the simplest version:

1. **Place source files in `data/raw/`.** Do not rename or modify them.
2. **Write a script that reads from `raw/` and writes to `processed/`.** This script cleans column names, standardizes dates, and handles data quality issues.
3. **Write a script that reads from `processed/` and writes to `outputs/`.** This script performs the analysis and generates the final report.

That is it. Two scripts, three folders, complete traceability.

---

## Examples

| Pipeline | Raw | Processed | Output |
|----------|-----|-----------|--------|
| [Bank Reconciliation](examples/data-flow-recon.md) | Bank CSV + GL CSV | Cleaned, standardized files | Recon report + summary |
| [Month-End Close](examples/data-flow-close.md) | TB export + subledgers | Normalized TB + flux calcs | Close package + variance report |

---

*Next: [Excel vs CSV](../10-excel-vs-csv/) -- a small decision with big impact.*
