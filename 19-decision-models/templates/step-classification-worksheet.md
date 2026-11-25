# Step Classification Worksheet

*Use this worksheet to break one process into steps and choose a method for each, before you build or buy anything. Ask the questions of each step, not once for the whole process.*

> **Practice on a synthetic process first.** Work through a fictional process, or the [variance example](../examples/variance-analysis-step-breakdown.md), before applying this to real workflows. Do not paste real company data into an AI tool to fill this in. See [Safe AI Data Workflows](https://github.com/PythonMuse/ai-ledger/tree/main/articles/06-safe-ai-data-workflows).

---

## Process Overview

| Field | Value |
|-------|-------|
| **Process** | [e.g., Monthly duplicate-payment test] |
| **Owner** | [Name or role] |
| **Date** | [YYYY-MM-DD] |
| **Is the process still necessary?** | [Yes / No / Needs redesign first] |

---

## The Six Questions

Ask these of every step.

| # | Question | If yes | If no |
|---|----------|--------|-------|
| 1 | Is the step necessary and understood? | Go to 2 | Simplify, document, or redesign first |
| 2 | Can we write the rule, and should the same input always give the same result? | Start with deterministic automation | Go to 3 |
| 3 | Does it require interpreting language or context? | Consider an LLM, subject to data limits, validation, and review | Go to 4 |
| 4 | Do reliable past examples hold a pattern we cannot write as rules? | Consider a decision model trained or tested on your history | Keep it with a person, or redesign |
| 5 | Does it involve judgment, approval, restricted data, or contract limits? | A qualified person stays responsible, whatever prepared the work | Note it and move on |
| 6 | What evidence will show it worked? | Define validation, logging, and sign-off before you build | -- |

---

## Step Table

One row per step.

| Step # | Step | Input | Expected output | Written rule? | Kind of work (rule / pattern / language / judgment) | Proposed method | Data restrictions | Evidence kept | Accountable person |
|--------|------|-------|-----------------|---------------|------------------------------------------------------|-----------------|-------------------|---------------|--------------------|
| 1 | [e.g., Confirm expected files and columns are present] | [Files] | [Pass/fail list] | [Yes: list of expected names and headers] | [Rule] | [Deterministic script] | [Internal; no AI at run time] | [Check log saved with run] | [Role] |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |

---

## Review Notes

- **Steps where AI helps build but never runs:** [List]
- **Steps where a model runs, and why a rule is not enough:** [List]
- **Steps that stay with a person:** [List]
- **What could a rule get consistently wrong?** [e.g., exact-match vendor names miss "ABC Corp" vs "ABC Corporation"]

---

*Part of [Module 19: Decision Models](../README.md) in the [PythonMuse AI Accounting Framework](https://github.com/PythonMuse/pythonmuse-ai-accounting-framework).*
