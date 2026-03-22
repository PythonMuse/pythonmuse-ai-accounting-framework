# Prompt Iteration: Bank Reconciliation

*How refining your prompts transforms AI output from useless to audit-ready.*

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

---

## What Changed

| Iteration | Context Provided | Output Quality |
|-----------|-----------------|----------------|
| 1 | None | Generic explanation |
| 2 | File structure | Reasonable approach, wrong assumptions |
| 3 | Rules and constraints | Accurate logic |
| 4 | Output format | Usable deliverable |
| 5 | Full specification | Audit-ready workflow |

The difference between iteration 1 and iteration 5 is not a better "prompt trick." It is the same thing that makes a good engagement letter better than a vague email: clarity, specificity, and professional standards.

---

*Back to [Working With AI](../)*
