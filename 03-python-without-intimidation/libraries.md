# Python Libraries for Accounting

*The tools that make Python practical for finance professionals. Start with the problem, not the library.*

---

## pandas -- Your Programmable Spreadsheet

**What it does:** Reads, manipulates, and analyzes tabular data. If you use Excel for data analysis, pandas does the same thing -- but repeatably and at scale.

**When you use it:** Every time you work with CSV or Excel data. This is the library you will use most.

**Install:**
```bash
pip install pandas
```

**Quick example:**
```python
import pandas as pd

# Read a CSV (like opening a file in Excel)
df = pd.read_csv("trial_balance.csv")

# Filter to expense accounts (like applying a filter in Excel)
expenses = df[df["account_number"] >= 5000]

# Sum a column (like SUM() in Excel)
total = expenses["amount"].sum()

# Group and summarize (like a pivot table)
by_dept = df.groupby("department")["amount"].sum()
```

---

## openpyxl -- Read and Write Excel Files

**What it does:** Reads and writes .xlsx files, including formatting, formulas, and multiple sheets.

**When you use it:** When you need to generate formatted Excel output for stakeholders, or when your source data is in Excel format.

**Install:**
```bash
pip install openpyxl
```

**Quick example:**
```python
import pandas as pd

# Read an Excel file with multiple sheets
df = pd.read_excel("workbook.xlsx", sheet_name="Trial Balance", engine="openpyxl")

# Write results to a formatted Excel file
df.to_excel("outputs/report.xlsx", index=False, sheet_name="Summary")
```

---

## pdfplumber -- Extract Data from PDFs

**What it does:** Pulls text, tables, and structured data out of PDF files. This is enormous for accounting, where so many documents arrive as PDFs.

**When you use it:** Bank statements, vendor invoices, lease agreements, audit reports -- any time you need to get data out of a PDF and into a usable format.

**Install:**
```bash
pip install pdfplumber
```

**Quick example:**
```python
import pdfplumber

# Open a PDF and extract text from the first page
with pdfplumber.open("bank_statement.pdf") as pdf:
    first_page = pdf.pages[0]
    text = first_page.extract_text()
    print(text)

    # Extract tables (if the PDF has structured tables)
    tables = first_page.extract_tables()
    for table in tables:
        for row in table:
            print(row)
```

---

## matplotlib -- Charts and Visualizations

**What it does:** Creates static charts and graphs -- bar charts, line charts, scatter plots, and more.

**When you use it:** Trend analysis, variance visuals, budget comparisons, any time you need a chart for a report or presentation.

**Install:**
```bash
pip install matplotlib
```

**Quick example:**
```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/sample_budget_actuals.csv")

# Create a simple bar chart comparing budget vs actuals
fig, ax = plt.subplots(figsize=(10, 6))
x = range(len(df))
ax.bar(x, df["budget_amount"], width=0.4, label="Budget", align="center")
ax.bar([i + 0.4 for i in x], df["actual_amount"], width=0.4, label="Actual", align="center")
ax.set_xlabel("Account")
ax.set_ylabel("Amount ($)")
ax.set_title("Budget vs Actuals")
ax.legend()
plt.tight_layout()
plt.savefig("outputs/budget_vs_actuals.png")
```

---

## plotly -- Interactive Visualizations

**What it does:** Creates interactive, web-based charts that users can hover over, zoom, and filter. Great for dashboards.

**When you use it:** When you want stakeholders to explore the data themselves, or when you are building a dashboard-style report.

**Install:**
```bash
pip install plotly
```

**Quick example:**
```python
import plotly.express as px
import pandas as pd

df = pd.read_csv("data/sample_budget_actuals.csv")
df["variance"] = df["actual_amount"] - df["budget_amount"]

fig = px.bar(df, x="account_name", y="variance", color="department",
             title="Variance by Account")
fig.write_html("outputs/variance_dashboard.html")
```

---

## sqlalchemy -- Database Connections

**What it does:** Connects Python to databases (SQL Server, PostgreSQL, MySQL, SQLite) so you can query data directly instead of exporting manually.

**When you use it:** When you have read-only SQL access to your ERP or GL system and want to pull data directly into Python for analysis.

**Install:**
```bash
pip install sqlalchemy
```

**Quick example:**
```python
from sqlalchemy import create_engine
import pandas as pd

# Connect to a database
engine = create_engine("sqlite:///accounting.db")

# Run a query and load results into a DataFrame
query = "SELECT * FROM gl_detail WHERE period = '2026-03'"
df = pd.read_sql(query, engine)

print(f"Rows returned: {len(df)}")
print(df.head())
```

---

## pyodbc -- SQL Server Connections

**What it does:** Connects Python to Microsoft SQL Server specifically. Many ERP systems (Dynamics, SAP) use SQL Server.

**When you use it:** When your IT team gives you read-only access to a SQL Server database.

**Install:**
```bash
pip install pyodbc
```

**Quick example:**
```python
import pyodbc
import pandas as pd

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=your-server;"
    "DATABASE=your-database;"
    "Trusted_Connection=yes;"
)

df = pd.read_sql("SELECT TOP 100 * FROM GL_Detail", conn)
conn.close()
```

---

## Which Library Do I Start With?

| Your Task | Start Here |
|-----------|------------|
| Read and analyze CSV files | pandas |
| Generate Excel reports | pandas + openpyxl |
| Extract data from PDFs | pdfplumber |
| Create charts for reports | matplotlib |
| Build interactive dashboards | plotly |
| Query databases directly | sqlalchemy or pyodbc |

Start with pandas. It is the foundation for almost everything else.

---

*Back to [Python Without Intimidation](../)*
