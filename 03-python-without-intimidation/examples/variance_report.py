# =============================================================================
# variance_report.py
# PythonMuse AI Accounting Framework
#
# Budget vs actuals variance analysis.
# Reads budget and actuals data, calculates variances, flags exceptions,
# and prints a management-ready summary.
#
# DATA NOTICE: This script uses synthetic sample data. When learning or
# experimenting, use the sample files provided or create your own masked
# test data. Do not use real company data (budget figures, account balances)
# until you have reviewed your organization's data policies.
# See: https://github.com/PythonMuse/ai-ledger/tree/main/articles/06-safe-ai-data-workflows
# =============================================================================

import pandas as pd

# Step 1: Read the budget and actuals data
df = pd.read_csv("data/sample_budget_actuals.csv")

# Step 2: Calculate dollar variance
# Variance = Actual - Budget
df["dollar_variance"] = df["actual_amount"] - df["budget_amount"]

# Step 3: Calculate percentage variance
# Handle division by zero (accounts with zero budget)
df["pct_variance"] = df.apply(
    lambda row: (row["dollar_variance"] / row["budget_amount"] * 100)
    if row["budget_amount"] != 0
    else None,
    axis=1,
)

# Step 4: Determine favorable vs unfavorable
# Revenue (accounts 4000-4999): favorable when actual > budget (more revenue)
# Expense (accounts 5000-9999): favorable when actual < budget (less spending)
def classify_variance(row):
    """Determine if a variance is favorable or unfavorable."""
    acct = row["account_number"]
    variance = row["dollar_variance"]

    if variance == 0:
        return "On Budget"
    elif 4000 <= acct <= 4999:
        # Revenue account: more actual = favorable
        return "Favorable" if variance > 0 else "Unfavorable"
    else:
        # Expense account: less actual = favorable
        return "Favorable" if variance < 0 else "Unfavorable"

df["status"] = df.apply(classify_variance, axis=1)

# Step 5: Flag items that exceed thresholds
# Flag if: absolute dollar variance > $5,000 OR absolute percentage > 10%
def should_flag(row):
    """Determine if a variance needs review."""
    dollar_threshold = 5000
    pct_threshold = 10

    if abs(row["dollar_variance"]) > dollar_threshold:
        return "Review Required"
    if row["pct_variance"] is not None and abs(row["pct_variance"]) > pct_threshold:
        return "Review Required"
    return ""

df["flag"] = df.apply(should_flag, axis=1)

# Step 6: Print the report
print("=" * 70)
print("BUDGET VS ACTUALS VARIANCE REPORT")
print("=" * 70)
print()

# Revenue section
revenue = df[(df["account_number"] >= 4000) & (df["account_number"] <= 4999)]
print("REVENUE")
print("-" * 70)
for _, row in revenue.iterrows():
    flag = " ***" if row["flag"] else ""
    pct = f"{row['pct_variance']:>6.1f}%" if row["pct_variance"] is not None else "   N/A"
    print(
        f"  {row['account_number']}  {row['account_name']:<25} "
        f"Budget: ${row['budget_amount']:>10,.2f}  "
        f"Actual: ${row['actual_amount']:>10,.2f}  "
        f"Var: ${row['dollar_variance']:>10,.2f}  "
        f"{pct}  {row['status']}{flag}"
    )

print()
rev_budget = revenue["budget_amount"].sum()
rev_actual = revenue["actual_amount"].sum()
print(f"  Total Revenue  Budget: ${rev_budget:>10,.2f}  Actual: ${rev_actual:>10,.2f}  Var: ${rev_actual - rev_budget:>10,.2f}")

# Expense section
print()
expenses = df[(df["account_number"] >= 5000)]
print("EXPENSES")
print("-" * 70)
for _, row in expenses.iterrows():
    flag = " ***" if row["flag"] else ""
    pct = f"{row['pct_variance']:>6.1f}%" if row["pct_variance"] is not None else "   N/A"
    print(
        f"  {row['account_number']}  {row['account_name']:<25} "
        f"Budget: ${row['budget_amount']:>10,.2f}  "
        f"Actual: ${row['actual_amount']:>10,.2f}  "
        f"Var: ${row['dollar_variance']:>10,.2f}  "
        f"{pct}  {row['status']}{flag}"
    )

print()
exp_budget = expenses["budget_amount"].sum()
exp_actual = expenses["actual_amount"].sum()
print(f"  Total Expenses Budget: ${exp_budget:>10,.2f}  Actual: ${exp_actual:>10,.2f}  Var: ${exp_actual - exp_budget:>10,.2f}")

# Summary
print()
print("=" * 70)
print("SUMMARY")
print("-" * 70)
print(f"  Net Income (Budget):  ${rev_budget - exp_budget:>10,.2f}")
print(f"  Net Income (Actual):  ${rev_actual - exp_actual:>10,.2f}")
print(f"  Net Income Variance:  ${(rev_actual - exp_actual) - (rev_budget - exp_budget):>10,.2f}")
print()

flagged = df[df["flag"] != ""]
print(f"  Items Flagged for Review: {len(flagged)}")
if len(flagged) > 0:
    print()
    print("  FLAGGED ITEMS:")
    for _, row in flagged.iterrows():
        print(f"    {row['account_number']} {row['account_name']:<25} ${row['dollar_variance']:>10,.2f}  {row['status']}")
