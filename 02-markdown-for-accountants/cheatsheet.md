# Markdown Cheatsheet for Accounting Professionals

*A quick reference for the Markdown syntax you will use most often.*

---

## Headers

```markdown
# Level 1 -- Report Title
## Level 2 -- Section (e.g., Revenue Analysis)
### Level 3 -- Subsection (e.g., Product Revenue)
#### Level 4 -- Detail (e.g., Q1 Product Revenue)
```

---

## Text Formatting

```markdown
**Bold** -- use for key findings or important figures
*Italic* -- use for emphasis or references
~~Strikethrough~~ -- use for superseded information
`Inline code` -- use for file names, formulas, account numbers
```

**Rendered:**
**Material variance identified.** See *ASC 606 guidance* for reference. The prior estimate of ~~$42,000~~ has been revised. File: `variance_report.csv`

---

## Lists

### Unordered (Bullet Points)
```markdown
- Bank reconciliation
- Accounts receivable aging
- Intercompany balances
```

### Ordered (Numbered Steps)
```markdown
1. Export trial balance from ERP
2. Run variance analysis script
3. Review flagged items
4. Prepare management summary
```

### Nested
```markdown
- Cash accounts
  - Operating (1010)
  - Payroll (1020)
  - Savings (1030)
- Receivables
  - Trade AR (1200)
  - Other AR (1250)
```

---

## Checkboxes

```markdown
- [x] Bank reconciliation completed
- [x] Accruals posted
- [ ] Variance analysis pending
- [ ] Financial statements drafted
```

---

## Tables

```markdown
| Account | Description       | Debit      | Credit     |
|---------|-------------------|------------|------------|
| 1010    | Cash - Operating  | $125,430   |            |
| 2010    | Accounts Payable  |            | $42,300    |
| 3010    | Retained Earnings |            | $83,130    |
| **Total** |                 | **$125,430** | **$125,430** |
```

**Rendered:**

| Account | Description       | Debit      | Credit     |
|---------|-------------------|------------|------------|
| 1010    | Cash - Operating  | $125,430   |            |
| 2010    | Accounts Payable  |            | $42,300    |
| 3010    | Retained Earnings |            | $83,130    |
| **Total** |                 | **$125,430** | **$125,430** |

---

## Links

```markdown
[Variance Report](outputs/variance_report.csv)
[PythonMuse Article 09](https://github.com/PythonMuse/ai-ledger/tree/main/articles/09-how-accountants-learn-ai)
```

---

## Blockquotes (Great for Standards and Policy References)

```markdown
> Per ASC 842-20-25-1, a lessee shall recognize a right-of-use asset
> and a lease liability at the commencement date.
```

> Per ASC 842-20-25-1, a lessee shall recognize a right-of-use asset and a lease liability at the commencement date.

---

## Code Blocks

### Inline Formula
```markdown
Variance percentage: `(actual - budget) / budget * 100`
```

### Multi-Line Code
````markdown
```python
import pandas as pd
df = pd.read_csv("data/raw/trial_balance.csv")
print(df.head())
```
````

### Output or Data
````markdown
```
Total Revenue:    $1,245,000
Total Expenses:     $987,500
Net Income:         $257,500
```
````

---

## Horizontal Rules (Section Separators)

```markdown
---
```

---

## Images

```markdown
![Chart Description](visuals/variance_chart.png)
```

---

## Quick Reference Card

| What You Want | Syntax | Example |
|---------------|--------|---------|
| Bold | `**text**` | **Material** |
| Italic | `*text*` | *Immaterial* |
| Header | `# Title` | Section title |
| Bullet list | `- item` | Task list |
| Numbered list | `1. item` | Procedure steps |
| Checkbox | `- [ ] item` | Close checklist |
| Table | `\| col \| col \|` | Trial balance |
| Link | `[text](url)` | File reference |
| Code | `` `code` `` | Formula |
| Quote | `> text` | Policy citation |

---

*Keep this file bookmarked. You will use it more than you think.*
