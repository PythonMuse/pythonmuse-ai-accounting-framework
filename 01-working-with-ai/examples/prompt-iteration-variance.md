# Prompt Iteration: Budget vs Actuals Variance Analysis

*Building a production-ready variance analysis prompt through progressive refinement.*

---

## The Scenario

You have a budget file and an actuals file for the current period. You need to calculate variances, flag exceptions, and produce a summary for management review.

---

## Iteration 1: The Starting Point

**Prompt:**
> "Compare my budget to actuals."

**What you get:** A general explanation of what variance analysis is. No actual calculations. The AI does not know your data, your thresholds, or your reporting format.

**Why it fails:** This is like handing a blank piece of paper to a new hire and saying "do the variance analysis." They need more than that.

---

## Iteration 2: Adding Data Structure

**Prompt:**
> "I have budget_2026.csv with columns: account_number, account_name, department, budget_amount. I also have actuals_march.csv with columns: account_number, account_name, department, actual_amount. Compare them."

**What you get:** A basic merge and subtraction. The AI will join on account_number and compute a simple difference. Better, but it will miss nuances.

**Why it is better:** The AI can now work with your specific data. But it does not know what matters to you.

---

## Iteration 3: Adding Accounting Context

**Prompt:**
> "Compare budget_2026.csv to actuals_march.csv by joining on account_number. Calculate:
> - Dollar variance (actual minus budget)
> - Percentage variance
> - For revenue accounts (4000-4999): favorable = actual > budget
> - For expense accounts (5000-9999): favorable = actual < budget
> Flag any variance where the absolute dollar amount exceeds $5,000 or the absolute percentage exceeds 10%."

**What you get:** A properly oriented variance analysis that understands the difference between revenue and expense accounts. Flagging logic is specific and useful.

**Why it is better:** Your accounting knowledge is now embedded in the instructions. The AI is not guessing about what "favorable" means.

---

## Iteration 4: Specifying the Deliverable

**Prompt:**
> "Output the results in two parts:
>
> 1. A CSV file called variance_report_march.csv saved to outputs/ with columns: account_number, account_name, department, budget_amount, actual_amount, dollar_variance, pct_variance, favorable_unfavorable, flag
>
> 2. A printed summary showing:
>    - Total budget vs total actual (revenue and expense separately)
>    - Number of accounts with unfavorable variances
>    - Top 5 largest unfavorable variances by dollar amount
>    - Top 5 largest unfavorable variances by percentage
>
> Sort the CSV by department, then account_number."

**What you get:** A formatted report and a concise summary for management review.

---

## Iteration 5: Production-Ready

**Prompt:**
> "Read budget_2026.csv and actuals_march.csv from data/raw/. Perform a variance analysis:
>
> 1. Join on account_number. If an account exists in actuals but not budget, flag as 'New Account.' If in budget but not actuals, flag as 'No Activity.'
> 2. Calculate dollar_variance = actual_amount - budget_amount.
> 3. Calculate pct_variance = dollar_variance / budget_amount. Handle division by zero (budget = 0) by noting 'N/A.'
> 4. Determine favorable/unfavorable:
>    - Revenue (accounts 4000-4999): favorable when actual exceeds budget
>    - Expense (accounts 5000-9999): favorable when actual is less than budget
> 5. Flag for review when: |dollar_variance| > $5,000 OR |pct_variance| > 10%.
>
> Output:
> - Save variance_report_march.csv to outputs/ with columns: account_number, account_name, department, budget_amount, actual_amount, dollar_variance, pct_variance, favorable_unfavorable, flag, notes. Sort by department then account_number.
> - Print a summary: total revenue budget vs actual, total expense budget vs actual, net income variance, count of flagged items, top 5 unfavorable variances by dollar and by percentage.
>
> Do not modify raw files."

**What you get:** A complete, audit-ready variance analysis with edge case handling, clear flagging logic, and a management-ready summary.

---

## The Pattern

Every iteration adds a layer of your professional judgment:

| Iteration | What You Added | What Improved |
|-----------|---------------|---------------|
| 1 | Nothing | Nothing useful |
| 2 | Data structure | AI can work with your files |
| 3 | Accounting rules | Correct orientation and flagging |
| 4 | Output format | Usable deliverable |
| 5 | Edge cases and full specification | Production-ready workflow |

The final prompt is not complicated. It is specific. That specificity comes from your expertise as an accountant, not from learning prompt tricks.

---

*Back to [Working With AI](../)*
