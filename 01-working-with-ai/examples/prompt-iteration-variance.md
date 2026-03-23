# Prompt Iteration: Budget vs Actuals Variance Analysis

*Building a production-ready variance analysis prompt through progressive refinement.*

---

> **Practice with sample data only.** The examples below use synthetic file names and data structures. When practicing these prompts, use the sample data provided with this framework or create your own masked test files. Never paste real company data — budget files, actuals exports, account details — into an AI tool without understanding your organization's data policies. For guidance, see [Safe AI Data Workflows](https://github.com/PythonMuse/ai-ledger/tree/main/articles/06-safe-ai-data-workflows). When you move toward production use, make sure each AI-assisted workflow is properly logged and governed — see [AI Governance for Controllers](https://github.com/PythonMuse/ai-ledger/tree/main/articles/07-ai-governance-for-controllers).

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

But here is the real question: if you run this analysis every month, do you really want to explain all of this again in April? And again in May? Iteration 5 is a great prompt — but it is still a prompt. It lives in a chat window, and next month you start from scratch.

Wouldn't it be better to drop in next month's actuals file, run the analysis, and watch it work — with one command, no re-explaining?

---

## Iteration 6: PythonMuse Accounting Framework

**Prompt:**
> "Let's move beyond a one-time variance analysis and build something I can trust and reuse every month — the way a strong accounting process should work.
>
> Apply PythonMuse principles:
>
> - structured, repeatable workflows
> - audit-ready outputs
> - and controlled, local-first data handling
>
> Think of this like documenting and training a new team member — the process should be clear enough that someone else (or future me) can run it without starting from scratch.
>
> Purpose:
> - Create a month-end budget vs actuals variance workflow that is:
>   - repeatable next month without rewriting instructions
>   - transparent enough for audit review
>   - protected so sensitive data never leaves the local environment
>
> What I need you to build:
>
> 1. **Variance Analysis SKILL**
>    - Clearly document:
>      - inputs (budget file, actuals file, structure, location)
>      - variance logic, account orientation rules, and flagging thresholds
>      - expected outputs (detail report and management summary)
>      - review checks and common exceptions (new accounts, zero budgets, missing activity)
>    - This should read like a procedure another accountant can follow
> 2. **Local-First Variance Agent**
>    - Explicitly restrict access to local files only
>    - Do not send source data outside the environment
>    - Treat data/raw/ as read-only source evidence
> 3. **Reusable Python Script**
>    - Allow parameters for period, file paths, and thresholds
>    - Ensure the same logic runs consistently each month
>    - No manual rework required
> 4. **Proof That It Works**
>    - Run on sample data
>    - Show results and explain how variances were calculated and flagged
>    - Highlight any edge cases or assumptions
> 5. **Audit-Ready Outputs**
>    - Save variance report, summary, and notes
>    - Include enough detail to support review without re-running the process
> 6. **Version-Control the Workflow**
>    - Stage everything in git
>    - So we can clearly see:
>      - what changed
>      - when it changed
>      - and why
>
> Controls to enforce:
>
> - Source data remains unchanged
> - All processing happens locally
> - Rules are documented and reusable
> - Results can be reproduced for any period
>
> End Result:
> I should walk away with:
>
> - a reusable variance analysis process
> - not just an answer for this month
> - something I can rely on, explain, and defend if asked
>
> Build this like you're helping me turn a manual task into a controlled accounting workflow — not just solving a one-time problem."

**What you get:** A workflow that no longer depends on re-explaining the task every month. Instead of a single prompt, you now have a reusable procedure, a controlled execution pattern, a reproducible script, and version history that supports audit review.


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
| 6 | Purpose, controls, reuse, and audit trail | Repeatable, reproducible, governed workflow |

The difference between iteration 1 and iteration 6 is not a better "prompt trick." It is the same thing that makes a good engagement letter better than a vague email: clarity, specificity, professional standards, and a process you can run again next month without starting from zero.

---

*Back to [Working With AI](../)*
