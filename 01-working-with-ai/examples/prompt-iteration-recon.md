# Prompt Iteration: Bank Reconciliation

*How refining your prompts transforms AI output from useless to audit-ready.*

---

> **Practice with sample data only.** The examples below use synthetic file names and data structures. When practicing these prompts, use the sample data provided with this framework or create your own masked test files. Never paste real company data — bank statements, GL exports, vendor details — into an AI tool without understanding your organization's data policies. For guidance, see [Safe AI Data Workflows](https://github.com/PythonMuse/ai-ledger/tree/main/articles/06-safe-ai-data-workflows). When you move toward production use, make sure each AI-assisted workflow is properly logged and governed — see [AI Governance for Controllers](https://github.com/PythonMuse/ai-ledger/tree/main/articles/07-ai-governance-for-controllers).

---

## The Scenario

You have a bank statement export (CSV) and a general ledger cash account export (CSV). You need to reconcile the two and identify unmatched items.

---

## Iteration 1: The Vague Start

**Prompt:**
> "Reconcile my bank data."

**What you get:** A generic explanation of what bank reconciliation is. No actual analysis. The AI has no idea what your data looks like, where it is, or what you expect.

**Why it fails:** No context. No data. No format. No goal.

---

## Iteration 2: Adding Data Context

**Prompt:**
> "I have two CSV files. bank_statement.csv has columns: date, description, amount. gl_export.csv has columns: posting_date, vendor_name, debit, credit. Help me reconcile these."

**What you get:** A reasonable starting point. The AI might suggest a matching approach based on amounts and dates. But it will make assumptions about your matching rules.

**Why it is better:** The AI now knows the file structure. But it still does not know your rules.

---

## Iteration 3: Adding Rules and Constraints

**Prompt:**
> "Match transactions between bank_statement.csv and gl_export.csv using the following rules:
> - Match by amount (bank amount should equal GL debit or credit)
> - Allow a date tolerance of 3 business days between bank date and GL posting date
> - Flag any unmatched items over $500
> - Ignore bank fees under $25
> - The bank statement uses negative amounts for debits and positive for credits"

**What you get:** A structured matching script with your specific rules applied. The output is much closer to what you actually need.

**Why it is better:** Your domain knowledge is now embedded in the instructions.

---

## Iteration 4: Specifying Output Format

**Prompt:**
> "Output the results as a CSV file called recon_results.csv with these columns:
> - bank_date, bank_description, bank_amount
> - gl_date, gl_vendor, gl_amount
> - match_status (Matched, Unmatched-Bank, Unmatched-GL)
> - variance (if amounts differ slightly)
> - notes (any flags or observations)
>
> Save to the outputs/ folder. At the top of the output, include a summary: total bank transactions, total GL transactions, matched count, unmatched count, total variance."

**What you get:** A complete, formatted reconciliation output that you can review, share with your team, or include in your workpapers.

**Why it is better:** The output is now defined precisely. No guessing, no reformatting.

---

## Iteration 5: Production-Ready Prompt

**Prompt:**
> "Read bank_statement.csv from data/raw/ and gl_export.csv from data/raw/. Reconcile using these rules:
>
> 1. Match by exact amount. Bank uses negative for debits, positive for credits. GL uses separate debit/credit columns.
> 2. Date tolerance: 3 business days.
> 3. Flag unmatched items over $500 as 'Review Required.'
> 4. Exclude bank fees under $25 from the reconciliation.
> 5. If multiple GL entries could match a single bank transaction, match to the closest date.
>
> Output:
> - Save recon_results.csv to outputs/ with columns: bank_date, bank_description, bank_amount, gl_date, gl_vendor, gl_amount, match_status, variance, notes.
> - Print a summary with: total bank items, total GL items, matched count, unmatched count, total unmatched dollar value, items flagged for review.
>
> Do not modify any files in data/raw/."

**What you get:** A complete, audit-ready reconciliation workflow that protects source data, applies your specific rules, and produces a documented output.

But here is the real question: if you run this reconciliation every month, do you really want to explain all of this again in February? And again in March? Iteration 5 is a great prompt — but it is still a prompt. It lives in a chat window, and next month you start from scratch.

Wouldn't it be better to drop in next month's bank statement and GL export, run the reconciliation, and watch it work — with one command, no re-explaining?

---

## Iteration 6: PythonMuse Accounting Framework

**Prompt:**
> "Let’s move beyond a one-time reconciliation and build something I can trust and reuse every month — the way a strong accounting process should work.

> Apply PythonMuse principles:

> - structured, repeatable workflows
> - audit-ready outputs
> - and controlled, local-first data handling

> Think of this like documenting and training a new team member — the process should be clear enough that someone else (or future me) can run it without starting from scratch.
>
> Purpose:
> - Create a month-end bank reconciliation workflow that is:
>   - repeatable next month without rewriting instructions
>   - transparent enough for audit review
>   - protected so sensitive data never leaves the local environment
>
> What I need you to build:
>
> 1. **Bank Reconciliation SKILL**
>    - Clearly document:
>      - inputs (files, structure, location)
>      - matching logic and thresholds
>      - expected outputs
>      - review checks and common exceptions
>    - This should read like a procedure another accountant can follow
> 2. **Local-First Reconciliation Agent**
>    - Explicitly restrict access to local files only
>    - Do not send source data outside the environment
>    - Treat data/raw/ as read-only source evidence
> 3. **Reusable Python Script**
>    - Allow parameters for period and file paths
>    - Ensure the same logic runs consistently each month
>    - No manual rework required
> 4. **Proof That It Works**
>    - Run on sample data
>    - Show results and explain how matches/unmatched items were determined
>    - Highlight any edge cases or assumptions
> 5. **Audit-Ready Outputs**
>    - Save reconciliation results, summaries, and notes
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
> - a reusable reconciliation process
> - not just an answer for this month
> - something I can rely on, explain, and defend if asked
>
> Build this like you’re helping me turn a manual task into a controlled accounting workflow — not just solving a one-time problem."

**What you get:** A workflow that no longer depends on re-explaining the task every month. Instead of a single prompt, you now have a reusable procedure, a controlled execution pattern, a reproducible script, and version history that supports audit review.


---

## What Changed

| Iteration | Context Provided | Output Quality |
|-----------|-----------------|----------------|
| 1 | None | Generic explanation |
| 2 | File structure | Reasonable approach, wrong assumptions |
| 3 | Rules and constraints | Accurate logic |
| 4 | Output format | Usable deliverable |
| 5 | Full specification | Audit-ready workflow |
| 6 | Purpose, controls, reuse, and audit trail | Repeatable, reproducible, governed workflow |

The difference between iteration 1 and iteration 6 is not a better "prompt trick." It is the same thing that makes a good engagement letter better than a vague email: clarity, specificity, professional standards, and a process you can run again next month without starting from zero.

---

*Back to [Working With AI](../)*
