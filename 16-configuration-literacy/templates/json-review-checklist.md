# JSON Review Checklist

*Use this checklist before you rely on a JSON (`.json`) or JSON Lines (`.jsonl`) file -- a settings file, a system export, or a log an AI workflow produced. Most of these files are drafted by AI. This is how you review one the way you would review a prepared journal entry.*

> **Practice on sample data first.** Work through this checklist using the fictional files in [examples/](../examples/) before applying it to real files. Never paste real financial data, credentials, or personal information into an AI tool to "check" a file for you. See [Safe AI Data Workflows](https://github.com/PythonMuse/ai-ledger/tree/main/articles/06-safe-ai-data-workflows).

---

## File Identification

| Field | Value |
|-------|-------|
| **File name** | [e.g., je_draft_2026-06.json] |
| **Location** | [e.g., outputs/] |
| **What it is** | [Settings file / export / log / draft entry] |
| **Who or what produced it** | [e.g., AI draft, ERP export, scheduled routine] |
| **Reviewed by** | [Name] |
| **Review date** | [YYYY-MM-DD] |

---

## 1. Can it be read?

- [ ] The file opens in a text editor (VS Code, Notepad) and the structure is followable
- [ ] VS Code shows no red error markers (a missing comma or quote breaks the whole file)
- [ ] For `.jsonl`: every line is one complete record

## 2. Do the values look right?

- [ ] Amounts are what you expect, with the right sign (no stray negatives, no missing decimals)
- [ ] Dates and periods are correct (`2026-06` is June, not the period you meant to close)
- [ ] Totals tie -- for an entry, debits equal credits
- [ ] `true` / `false` mean what was intended, especially on any field that grants access or approval
- [ ] Text values are spelled consistently (`"final"` vs `"Final"` can be treated as different values)

## 3. Is anything missing?

- [ ] Every required field is present
- [ ] No required field is `null` or blank (`""`) without an explanation
- [ ] Field names are spelled correctly (`"approved"` and `"aproved"` are two different fields to a program)
- [ ] There are no extra fields nobody asked for
- [ ] For a list: the count is right (number of lines, entries, or log events matches what you expected)

## 4. Does it contain anything sensitive?

- [ ] No bank, card, or full account numbers
- [ ] No personal data (names, addresses, tax IDs, employee details) unless the file is approved to hold it
- [ ] No passwords, API keys, or tokens -- settings files and logs are the usual place these leak
- [ ] No real client or vendor names in files meant for sharing, testing, or training
- [ ] Data classification is consistent with where the file is stored and who can see it

---

## Sign-off

| Result | Notes |
|--------|-------|
| [ ] Approved for use | |
| [ ] Returned for correction | [What needs to change] |

**Reviewer:** [Name] **Date:** [YYYY-MM-DD]

---

*Part of [Module 16: Configuration Literacy](../README.md) in the [PythonMuse AI Accounting Framework](https://github.com/PythonMuse/pythonmuse-ai-accounting-framework).*
