# =============================================================================
# read_csv_basics.py
# PythonMuse AI Accounting Framework
#
# A beginner-friendly script that reads a CSV file and prints basic summaries.
# Every line is commented so you can follow the logic step by step.
# =============================================================================

# Step 1: Import the pandas library
# pandas is a data analysis tool -- think of it as a programmable spreadsheet
import pandas as pd

# Step 2: Read the CSV file into a DataFrame
# A DataFrame is like an Excel table: rows and columns of data
df = pd.read_csv("data/sample_bank_transactions.csv")

# Step 3: Print the column names
# This is like looking at the header row in Excel
print("=== Column Names ===")
print(df.columns.tolist())
print()

# Step 4: Print how many rows are in the file
# Same as checking the row count in the bottom-left corner of Excel
print("=== Row Count ===")
print(f"Total transactions: {len(df)}")
print()

# Step 5: Print the first 5 rows
# This gives you a quick look at the data, like scrolling to the top of a spreadsheet
print("=== First 5 Rows ===")
print(df.head())
print()

# Step 6: Calculate the total debits and credits
# .sum() adds up all values in a column -- same as SUM() in Excel
total_debits = df["debit"].sum()
total_credits = df["credit"].sum()

print("=== Totals ===")
print(f"Total Debits:  ${total_debits:,.2f}")
print(f"Total Credits: ${total_credits:,.2f}")
print(f"Net Movement:  ${total_debits - total_credits:,.2f}")
print()

# Step 7: Find the largest single transaction
# .max() finds the highest value -- same as MAX() in Excel
max_debit = df["debit"].max()
max_credit = df["credit"].max()

print("=== Largest Transactions ===")
print(f"Largest Debit:  ${max_debit:,.2f}")
print(f"Largest Credit: ${max_credit:,.2f}")
print()

# Step 8: Count transactions by type (based on description keywords)
# This is like using COUNTIF in Excel
print("=== Transaction Summary ===")
print(f"Total rows in file: {len(df)}")
print(f"Rows with debits:   {df['debit'].gt(0).sum()}")
print(f"Rows with credits:  {df['credit'].gt(0).sum()}")
