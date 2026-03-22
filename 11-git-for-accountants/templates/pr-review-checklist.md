# Pull Request Review Checklist for Accounting Teams

*Use this checklist when reviewing a colleague's pull request for an accounting AI project.*

---

## Before You Start

- [ ] Read the PR description to understand what was changed and why
- [ ] Check the branch name -- does it describe the work?

---

## Code and Logic Review

- [ ] Does the change match the stated objective?
- [ ] Are data transformations documented (in comments or in the PR description)?
- [ ] Is the logic correct? (Spot-check calculations, matching rules, thresholds)
- [ ] Are edge cases handled? (Division by zero, missing data, unexpected values)
- [ ] Are outputs saved to the correct folder? (outputs/, not data/raw/)

---

## Data Safety

- [ ] Is sensitive data excluded from the commit? (No PII, SSNs, bank accounts)
- [ ] Does the .gitignore properly exclude data files and credentials?
- [ ] Are raw data files in data/raw/ left unmodified?
- [ ] No hardcoded passwords, API keys, or connection strings?

---

## Documentation

- [ ] Are commit messages clear and descriptive?
- [ ] Is status_update.md updated with the current session's progress?
- [ ] Are new scripts or templates commented for clarity?
- [ ] Would a new team member understand this change without verbal explanation?

---

## Quality

- [ ] Does the code run without errors?
- [ ] Were results verified against sample data?
- [ ] Is the output format correct and consistent?
- [ ] Are file names descriptive and following project conventions?

---

## Approval

- [ ] All checks above pass
- [ ] Approved for merge

**Reviewer:** _______________  **Date:** _______________

---

*Template from the [PythonMuse AI Accounting Framework](https://github.com/PythonMuse/pythonmuse-ai-accounting-framework)*
