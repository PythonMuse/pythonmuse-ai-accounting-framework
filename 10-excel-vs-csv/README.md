# Excel vs CSV -- A Small Decision with Big Impact

*Before working with AI, always ask: "Is this Excel or CSV?" The answer affects everything downstream.*

---

## Why This Matters

It seems like a minor question. But the choice between Excel and CSV affects:

- **Which Python libraries you need.** CSV uses pandas only. Excel requires openpyxl or xlrd.
- **Processing speed.** CSV files are plain text -- fast to read, fast to process. Excel files are complex archives that take longer to parse.
- **Error likelihood.** Excel files carry hidden formatting, merged cells, multiple sheets, and formula dependencies. CSV files are flat and predictable.
- **AI token usage.** A CSV file is compact. An Excel file with formatting metadata can be significantly larger. More tokens = more cost, slower processing.

**Best practice: CSV for processing, Excel for presentation.**

---

## CSV: When to Use It

CSV (Comma-Separated Values) is the format AI tools work with best.

**Strengths:**
- Simple and lightweight -- just text and commas
- Opens in any tool (Excel, VS Code, Python, AI tools)
- Fast to read and process
- Version-control friendly (Git can track changes)
- No hidden formatting surprises

**Best for:**
- Data analysis and processing
- Input to Python scripts
- AI tool consumption
- Intermediate working files
- Data exchange between systems

---

## Excel: When to Use It

Excel is the format stakeholders expect for final deliverables.

**Strengths:**
- Familiar to every finance professional
- Supports formatting, formulas, charts, and multiple sheets
- Suitable for presentation and distribution

**Best for:**
- Final reports for management
- Formatted workpapers
- Files that need specific cell formatting, colors, or charts
- Deliverables that will be opened in Excel by others

---

## Common Gotchas When Converting

### Dates
Excel often reformats dates silently. `2026-03-15` might become `3/15/2026` or even a serial number like `46100`. Always verify date columns after conversion.

### Leading Zeros
Account numbers like `00451` become `451` in Excel. ZIP codes lose their leading zeros. When exporting to CSV, verify that leading zeros are preserved.

### Merged Cells
Excel supports merged cells. CSV does not. Merged cells become blank cells in CSV, which can break your data structure.

### Multiple Sheets
A CSV file is a single table. An Excel workbook can have dozens of sheets. When converting, you need to handle each sheet separately.

### Formulas
CSV files store values only. Excel files can contain formulas. When you export to CSV, formulas are resolved to their current values -- which is usually what you want, but verify.

### Encoding
Excel files can contain special characters that cause issues in CSV. Always save CSV files in UTF-8 encoding.

---

## How to Export Clean CSV from Your ERP

Most ERP systems offer export options. When exporting for AI processing:

1. **Choose CSV format** (not .xlsx or .xls)
2. **Select UTF-8 encoding** if the option is available
3. **Verify date format** -- YYYY-MM-DD is the most reliable
4. **Check for header rows** -- ensure there is exactly one header row
5. **Remove summary rows** -- totals at the bottom of reports will confuse analysis
6. **Verify column consistency** -- every row should have the same number of columns

---

## Examples

| File | What It Does |
|------|-------------|
| [convert-excel-to-csv.py](examples/convert-excel-to-csv.py) | Python script to batch convert Excel files to clean CSV |
| [csv-best-practices.md](examples/csv-best-practices.md) | Formatting guidelines for AI-ready CSV files |

---

## Sample Data

| File | Description |
|------|-------------|
| [sample_clean.csv](data/sample_clean.csv) | A well-formatted trial balance CSV |

---

## Key Takeaway

Clean CSV = lower cost + better results. Save yourself hours of debugging by converting to clean CSV before starting any AI workflow. Use Excel for the final deliverable.

---

*Next: [Git for Accountants](../11-git-for-accountants/) -- version control as your audit trail.*
