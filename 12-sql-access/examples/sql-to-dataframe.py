# =============================================================================
# sql-to-dataframe.py
# PythonMuse AI Accounting Framework
#
# Demonstrates querying a database and loading results into a pandas DataFrame.
# Uses SQLite for the example so it runs without an external database server.
#
# DATA NOTICE: This script creates a temporary SQLite database with synthetic
# data for learning purposes. When adapting this pattern for real databases,
# do not connect to production systems until you have reviewed your
# organization's data handling and access policies.
# See: https://github.com/PythonMuse/ai-ledger/tree/main/articles/06-safe-ai-data-workflows
# =============================================================================

import pandas as pd
import sqlite3
import os

# =============================================================================
# Step 1: Create a sample database (simulating your ERP/GL system)
# In real life, you would connect to an existing database instead.
# =============================================================================

db_path = "sample_accounting.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a general ledger detail table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS gl_detail (
        entry_id INTEGER PRIMARY KEY,
        posting_date TEXT,
        account_number TEXT,
        account_name TEXT,
        department TEXT,
        description TEXT,
        debit REAL,
        credit REAL,
        reference TEXT
    )
""")

# Insert sample data (synthetic -- not real financial data)
sample_entries = [
    (1, '2026-03-01', '5100', 'Salaries and Wages', 'Operations', 'March payroll - week 1', 22600.00, 0.00, 'PAY-0301'),
    (2, '2026-03-01', '1010', 'Cash - Operating', 'Treasury', 'March payroll - week 1', 0.00, 22600.00, 'PAY-0301'),
    (3, '2026-03-05', '6200', 'Software Subscriptions', 'Admin', 'Monthly SaaS licenses', 1875.00, 0.00, 'AP-0305'),
    (4, '2026-03-05', '2010', 'Accounts Payable', 'Admin', 'Monthly SaaS licenses', 0.00, 1875.00, 'AP-0305'),
    (5, '2026-03-10', '1010', 'Cash - Operating', 'Treasury', 'Customer payment - Riverside', 12500.00, 0.00, 'CR-0310'),
    (6, '2026-03-10', '1200', 'Accounts Receivable', 'Revenue', 'Customer payment - Riverside', 0.00, 12500.00, 'CR-0310'),
    (7, '2026-03-15', '5100', 'Salaries and Wages', 'Operations', 'March payroll - week 2', 22600.00, 0.00, 'PAY-0315'),
    (8, '2026-03-15', '1010', 'Cash - Operating', 'Treasury', 'March payroll - week 2', 0.00, 22600.00, 'PAY-0315'),
    (9, '2026-03-20', '7100', 'Marketing Expense', 'Marketing', 'Ad campaign - Q1', 4500.00, 0.00, 'AP-0320'),
    (10, '2026-03-20', '2010', 'Accounts Payable', 'Marketing', 'Ad campaign - Q1', 0.00, 4500.00, 'AP-0320'),
    (11, '2026-03-25', '4100', 'Product Revenue', 'Sales', 'March product sales', 0.00, 47250.00, 'REV-0325'),
    (12, '2026-03-25', '1200', 'Accounts Receivable', 'Sales', 'March product sales', 47250.00, 0.00, 'REV-0325'),
    (13, '2026-03-31', '8100', 'Depreciation', 'Finance', 'Monthly depreciation', 2200.00, 0.00, 'JE-DEP-03'),
    (14, '2026-03-31', '1510', 'Accumulated Depreciation', 'Finance', 'Monthly depreciation', 0.00, 2200.00, 'JE-DEP-03'),
]

cursor.executemany("""
    INSERT OR REPLACE INTO gl_detail
    (entry_id, posting_date, account_number, account_name, department, description, debit, credit, reference)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", sample_entries)

conn.commit()

# =============================================================================
# Step 2: Query the database (this is what you would do in practice)
# =============================================================================

# Simple query: Get all GL entries for March 2026
query = """
    SELECT *
    FROM gl_detail
    WHERE posting_date BETWEEN '2026-03-01' AND '2026-03-31'
    ORDER BY posting_date, entry_id
"""

# Load results into a pandas DataFrame
# This is the key step: SQL data becomes a programmable table
df = pd.read_sql_query(query, conn)

print("=== GL Detail for March 2026 ===")
print(f"Total entries: {len(df)}")
print()
print(df.to_string(index=False))
print()

# =============================================================================
# Step 3: Analyze the data (same operations you'd do in Excel)
# =============================================================================

# Summarize by account
account_summary = df.groupby(['account_number', 'account_name']).agg(
    total_debit=('debit', 'sum'),
    total_credit=('credit', 'sum'),
    entry_count=('entry_id', 'count')
).reset_index()

print("=== Account Summary ===")
print(account_summary.to_string(index=False))
print()

# Verify debits = credits
total_debits = df['debit'].sum()
total_credits = df['credit'].sum()
print(f"Total Debits:  ${total_debits:,.2f}")
print(f"Total Credits: ${total_credits:,.2f}")
print(f"Difference:    ${total_debits - total_credits:,.2f}")

# =============================================================================
# Step 4: Save results to CSV
# =============================================================================

output_path = "gl_detail_march.csv"
df.to_csv(output_path, index=False)
print(f"\nResults saved to: {output_path}")

# =============================================================================
# Clean up
# =============================================================================
conn.close()
os.remove(db_path)  # Remove the sample database (you would not do this with a real DB)
