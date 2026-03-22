# =============================================================================
# aging_buckets.py
# PythonMuse AI Accounting Framework
#
# Accounts receivable aging bucket analysis.
# Reads AR data, calculates days outstanding, assigns aging buckets,
# and prints a summary report.
# =============================================================================

import pandas as pd
from datetime import datetime

# Step 1: Read the AR aging data
df = pd.read_csv("data/sample_ar_aging.csv")

# Step 2: Define "today" for calculating days outstanding
# In practice, this would be your reporting date (e.g., month-end)
report_date = datetime(2026, 3, 31)

# Step 3: Convert date columns from text to actual dates
# This is like formatting a column as Date in Excel
df["invoice_date"] = pd.to_datetime(df["invoice_date"])
df["due_date"] = pd.to_datetime(df["due_date"])

# Step 4: Handle payment dates (some invoices are unpaid, so this column has blanks)
df["payment_date"] = pd.to_datetime(df["payment_date"], errors="coerce")

# Step 5: Identify unpaid invoices
# If payment_date is blank (NaT = Not a Time), the invoice is still open
df["is_open"] = df["payment_date"].isna()

# Step 6: Calculate days outstanding for open invoices
# This is the number of days between the due date and the report date
df["days_outstanding"] = (report_date - df["due_date"]).dt.days

# Step 7: Assign aging buckets based on days outstanding
# This is the same logic as a nested IF statement in Excel
def assign_bucket(days):
    """Assign an aging bucket based on days past due."""
    if days <= 0:
        return "Current"
    elif days <= 30:
        return "1-30 Days"
    elif days <= 60:
        return "31-60 Days"
    elif days <= 90:
        return "61-90 Days"
    else:
        return "Over 90 Days"

df["aging_bucket"] = df["days_outstanding"].apply(assign_bucket)

# Step 8: Filter to only open (unpaid) invoices
open_invoices = df[df["is_open"]].copy()

# Step 9: Summarize by aging bucket
# This is like a pivot table grouped by aging bucket, summing the amounts
summary = open_invoices.groupby("aging_bucket")["amount"].agg(["count", "sum"])
summary.columns = ["Invoice Count", "Total Amount"]

# Sort buckets in logical order
bucket_order = ["Current", "1-30 Days", "31-60 Days", "61-90 Days", "Over 90 Days"]
summary = summary.reindex(bucket_order)

# Step 10: Print the report
print("=" * 60)
print("ACCOUNTS RECEIVABLE AGING REPORT")
print(f"As of: {report_date.strftime('%B %d, %Y')}")
print("=" * 60)
print()

for bucket in bucket_order:
    if bucket in summary.index:
        count = summary.loc[bucket, "Invoice Count"]
        total = summary.loc[bucket, "Total Amount"]
        print(f"  {bucket:<15}  {int(count):>5} invoices   ${total:>12,.2f}")

print()
print("-" * 60)
total_open = open_invoices["amount"].sum()
total_count = len(open_invoices)
print(f"  {'TOTAL':<15}  {total_count:>5} invoices   ${total_open:>12,.2f}")
print()

# Step 11: Show the largest overdue items (over 90 days)
overdue = open_invoices[open_invoices["aging_bucket"] == "Over 90 Days"]
if len(overdue) > 0:
    print("TOP OVERDUE ITEMS (Over 90 Days):")
    print("-" * 60)
    for _, row in overdue.nlargest(5, "amount").iterrows():
        print(f"  {row['customer_name']:<25} Invoice #{row['invoice_number']:<8} ${row['amount']:>10,.2f}  ({row['days_outstanding']} days)")
