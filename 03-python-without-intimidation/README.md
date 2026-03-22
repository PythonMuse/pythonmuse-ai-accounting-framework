# Python Without Intimidation

*You do not need to become a developer. You need to understand what the code is doing -- the same way you follow a complex Excel formula.*

---

## The Excel Analogy

Think about how you work with Excel formulas today.

You do not necessarily need to write `=INDEX(MATCH(...))` from scratch every time. But when you see it in a workbook, you can break it apart: this piece looks up a value, this piece finds the row, this piece returns the result. You follow the logic in chunks.

Python works the same way.

The difference is that Python is written in something closer to plain English, which makes it -- in many cases -- easier to follow than nested Excel formulas.

---

## What Python Looks Like

Here is a Python script that reads a CSV file and prints a summary:

```python
import pandas as pd

# Read the trial balance file
df = pd.read_csv("data/raw/trial_balance.csv")

# Show the first 5 rows
print(df.head())

# Print the total debits and credits
total_debits = df["debit_balance"].sum()
total_credits = df["credit_balance"].sum()

print(f"Total Debits:  ${total_debits:,.2f}")
print(f"Total Credits: ${total_credits:,.2f}")
print(f"Difference:    ${total_debits - total_credits:,.2f}")
```

Read it line by line. Even without any Python experience, you can follow what this does:

1. Import a library called pandas (a data analysis tool)
2. Read a CSV file into a table
3. Show the first 5 rows
4. Add up the debit column and the credit column
5. Print the totals and the difference

That is it. No magic. No intimidation required.

---

## Why Python Matters for Accountants

Python is valuable in accounting because it is:

- **Readable.** The syntax is close to English. You can follow the logic.
- **Transparent.** Every step is visible. No hidden calculations buried in cell references.
- **Audit-friendly.** The script is the documentation. Anyone can read it and understand what was done.
- **Repeatable.** Run the same script next month with new data. Same process, same controls, no manual steps.

And here is the key insight:

**You do not need to write it. You need to understand it.**

When you work with AI tools like Claude, the AI writes the Python. Your job is to review it -- the same way you review a staff accountant's work. You check the logic, verify the output, and make sure it does what you intended.

Trust me -- I am not a developer. But I can follow the logic, and that is all due to the amazing people who have contributed to open-source libraries that make Python readable and practical for non-developers.

---

## Key Libraries for Accounting

These are the tools that make Python useful for finance work. Think of them as add-ons -- each one gives Python a specific capability.

| Library | What It Does | Accounting Use Case |
|---------|-------------|---------------------|
| pandas | Data analysis and manipulation | Your programmable spreadsheet |
| openpyxl | Read and write Excel files | Generate formatted Excel reports |
| pdfplumber | Extract text and tables from PDFs | Pull data from bank statements, invoices |
| matplotlib | Create charts and graphs | Trend analysis, variance visuals |
| plotly | Interactive visualizations | Dashboard-style reporting |
| sqlalchemy | Connect to databases | Query GL, AR, AP directly |

For a deeper dive into each library, see [libraries.md](libraries.md).

---

## Reading Python: A Line-by-Line Guide

When you encounter a Python script, read it the same way you would read a complex Excel formula -- break it into pieces.

**Common patterns you will see:**

```python
import pandas as pd          # "I need the pandas tool, call it pd for short"
df = pd.read_csv("file.csv") # "Read this file into a table called df"
df["column"].sum()            # "Add up everything in this column"
df[df["amount"] > 1000]       # "Show me only rows where amount is over 1000"
df.to_csv("output.csv")      # "Save this table as a new CSV file"
```

Every one of these lines maps to something you already do in Excel:
- `import` = opening a workbook with specific add-ins
- `read_csv` = File > Open
- `.sum()` = SUM()
- `df[condition]` = Filter
- `.to_csv()` = Save As

---

## Examples in This Section

| File | What It Does |
|------|-------------|
| [read_csv_basics.py](examples/read_csv_basics.py) | Read a CSV, print summary statistics |
| [aging_buckets.py](examples/aging_buckets.py) | AR aging bucket analysis |
| [variance_report.py](examples/variance_report.py) | Budget vs actuals variance report |

Each script is heavily commented so you can follow every step.

---

## Sample Data

| File | Description |
|------|-------------|
| [sample_ar_aging.csv](data/sample_ar_aging.csv) | Accounts receivable aging data |
| [sample_budget_actuals.csv](data/sample_budget_actuals.csv) | Budget and actuals by account |
| [sample_bank_transactions.csv](data/sample_bank_transactions.csv) | Bank statement transactions |

All data is synthetic. No real financial information is included.

---

## Try This

1. Open one of the example scripts in VS Code
2. Read through the comments before looking at the code
3. Try to predict what each line does before reading the comment
4. Run the script: open the terminal in VS Code and type `python examples/read_csv_basics.py`
5. Compare the output to the source CSV file

You will be surprised how quickly it starts to make sense.

---

## Key Takeaway

Python is not about becoming a programmer. It is about being able to follow the logic when AI generates a script, verify that it does what you intended, and trust the process because every step is visible.

The same professional judgment you use to review a staff accountant's workpapers applies directly to reviewing Python code.

---

*Next: [VS Code as Your Workspace](../04-vscode-as-workspace/) -- your AI-ready work environment.*
