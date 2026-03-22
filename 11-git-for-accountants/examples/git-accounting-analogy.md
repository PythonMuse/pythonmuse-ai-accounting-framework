# Git and Accounting: The Full Analogy

*A detailed side-by-side comparison showing how Git concepts map directly to accounting practices.*

---

## The Journal Entry = The Commit

A journal entry records: **what changed, when, who, and why.**

```
Date: 2026-03-31
Account 5100 - Salaries Expense    DR  $45,200
Account 1010 - Cash                CR  $45,200
Memo: March payroll - second biweekly cycle
Prepared by: S. Toohey
```

A git commit records the same information:

```bash
git commit -m "Add March payroll reconciliation logic

- Added matching for biweekly payroll transactions
- Handles split between salary and tax withholding entries
- Tested against March bank statement data"
```

**What changed:** The files that were modified (Git tracks every line)
**When:** Timestamp is automatic
**Who:** Git records the author
**Why:** The commit message explains the purpose

---

## The General Ledger = The Git Log

The GL is a chronological record of all journal entries. You can drill into any entry to see what happened.

```bash
git log --oneline
a3b8f21  Complete March bank reconciliation (2026-03-20)
7c4e912  Fix date tolerance matching logic (2026-03-19)
b1d5a88  Add initial reconciliation script (2026-03-19)
e2f1c34  Import raw bank and GL data (2026-03-18)
9a8d7b6  Initialize project structure (2026-03-18)
```

Just like you can drill into any GL entry, you can drill into any commit:

```bash
git show a3b8f21
```

This shows every line that was added, removed, or changed in that commit.

---

## The Adjusting Entry = The Revert

When you find an error in accounting, you do not go back and erase the original entry. You post a correcting entry:

```
Date: 2026-04-02
Account 6200 - Software Expense    DR  $1,500
Account 6100 - Office Supplies     CR  $1,500
Memo: Correct misclassification from March posting
```

Git works the same way:

```bash
git revert 7c4e912
```

This does not delete the original commit. It creates a new commit that undoes the changes, preserving the full history. The original entry is still in the log. The correction is documented alongside it.

---

## The Branch = The Scenario Analysis

When a controller asks "What would our numbers look like if we capitalized this cost instead of expensing it?", you do not change the real books. You work on a copy.

Git branches work the same way:

```bash
git checkout -b scenario-capitalize-lease
```

Now you are working on a separate copy. You can make changes, test assumptions, and analyze results. The main version is untouched.

When you are done:
- If the scenario is approved, merge it back into the main branch
- If it is rejected, delete the branch. No harm done.

---

## The Pull Request = The Review Process

Before a senior accountant's work is accepted, it is reviewed. A pull request (PR) is the same thing in Git:

1. You complete your work on a branch
2. You open a pull request: "Please review my March reconciliation"
3. A reviewer examines every change
4. They approve, request modifications, or reject
5. Once approved, the changes are merged into the main branch

This is maker-checker for code and data workflows.

---

## Side-by-Side Summary

| Action | Accounting | Git Command |
|--------|-----------|-------------|
| Record a change | Post a journal entry | `git commit -m "description"` |
| Review the history | Pull the GL detail | `git log` |
| See what changed | Drill into an entry | `git show <commit>` |
| Correct an error | Post an adjusting entry | `git revert <commit>` |
| Test a scenario | Work on a copy | `git checkout -b branch-name` |
| Get approval | Submit for review | Open a pull request |
| Accept the changes | Approve and post | Merge the pull request |
| Back up your work | Off-site document storage | `git push` |

---

*Back to [Git for Accountants](../)*
