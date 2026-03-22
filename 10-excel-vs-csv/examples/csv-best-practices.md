# CSV Best Practices for AI Consumption

*How to format CSV files so they work cleanly with Python and AI tools.*

---

## Date Format: YYYY-MM-DD

Use ISO 8601 format: `2026-03-15`

Avoid: `3/15/2026`, `03-15-2026`, `March 15, 2026`, `15/03/2026`

Why: YYYY-MM-DD sorts correctly, is unambiguous, and is the default for pandas.

---

## Column Headers

**Do:**
- Use lowercase: `account_number`
- Use underscores, not spaces: `invoice_date`
- Be descriptive: `total_debit_amount`
- Keep headers in the first row only

**Do not:**
- Use spaces: `Account Number`
- Use special characters: `Account #`, `Amount ($)`
- Use duplicate column names
- Include units in the header: `amount_usd` is okay, `amount ($)` is not

---

## Null and Empty Values

Choose one convention and be consistent:

| Convention | Example | When to Use |
|------------|---------|-------------|
| Empty string | `,,` | Default. Most common. |
| Explicit null | `,N/A,` or `,NULL,` | When you need to distinguish "no data" from "zero" |
| Zero | `,0,` | When zero is a valid numeric value |

Do not mix conventions in the same file.

---

## Numbers

- No currency symbols: `42300.00` not `$42,300.00`
- No thousand separators: `42300` not `42,300`
- Use period as decimal separator: `42300.50`
- Negative numbers: use a leading minus sign: `-42300.00`

Formatting with dollar signs and commas is for presentation (Excel). Processing (CSV) uses raw numbers.

---

## Text Fields

- If a text field contains commas, it must be quoted: `"Smith, John"`
- If a text field contains quotes, escape them: `"He said ""hello"""`
- UTF-8 encoding is standard
- Be consistent with case (all uppercase, all lowercase, or title case -- pick one per column)

---

## Leading Zeros

Account numbers like `00451` will lose their leading zeros if opened in Excel. To preserve them:

- Keep the file as CSV and open it in VS Code or a text editor for verification
- If you must open in Excel, import using "Text" column type for those fields
- When generating CSV from Python, account numbers should be stored as strings, not integers

---

## File Encoding

Always use UTF-8. This handles special characters correctly across all platforms.

Check for and remove BOM (Byte Order Mark) characters. Some Windows tools add a hidden BOM at the start of UTF-8 files, which can cause issues with Python parsing.

---

## Structure Rules

- Exactly one header row (the first row)
- No summary or total rows at the bottom
- No blank rows between data rows
- No merged concepts (every row should be a complete record)
- Consistent number of columns across all rows
- No trailing commas at the end of rows

---

## Pre-Processing Validation

Before feeding a CSV to AI or a Python script, check:

- [ ] File opens correctly in a text editor
- [ ] Header row has clean, descriptive column names
- [ ] Dates are in YYYY-MM-DD format
- [ ] Numbers are plain (no currency symbols or commas)
- [ ] No summary rows at the bottom
- [ ] No blank rows in the middle
- [ ] Row count matches expected data volume
- [ ] Encoding is UTF-8

---

*Back to [Excel vs CSV](../)*
