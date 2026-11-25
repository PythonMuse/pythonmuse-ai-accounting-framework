# Worked Example: Year-over-Year Variance Analysis, Step by Step

*A fictional monthly variance review, classified one step at a time. All figures and names are synthetic.*

It is tempting to call the whole review "an AI use case." Break it into steps and a better design appears: AI helps build most of it, runs almost none of it, and a person owns the explanation.

---

## The Steps

| # | Step | Kind of work | Method | Why | Evidence kept |
|---|------|--------------|--------|-----|---------------|
| 1 | Confirm the expected trial balance files and columns are present | Rule | Script | The expected file names and headers can be listed exactly | Schema-check log |
| 2 | Confirm the reporting period and that totals tie to the general ledger | Rule | Script | Period must equal the reporting period; totals must tie | Control-total report |
| 3 | Calculate dollar and percent change by account | Rule | Script | Change = current minus prior; percent = change divided by the absolute prior balance | Variance file and script version |
| 4 | Apply the approved materiality threshold | Rule | Script, with the threshold in one labeled setting | Approved policy (for example, over a stated dollar amount and a stated percent) | Threshold value and approval reference in the run log |
| 5 | Draft questions for the account owners on flagged accounts | Language | LLM, only if policy allows, on summarized figures | Turning a flagged line into a sensible question is language work | Draft questions, marked as AI-drafted |
| 6 | Find and support the reason for each material change | Judgment | Accountant | The explanation needs facts, support, and accountability | Support attached to each explanation |
| 7 | Approve the final variance commentary | Judgment | Controller | Sign-off cannot be delegated to a tool | Signed review note |

---

## What to Notice

- **Five of seven steps are rules.** AI can help write and test that script. At run time, none of those steps needs a model, and none of the data needs to leave the machine.
- **The one language step is optional.** If policy rules out an LLM, the process loses a convenience, not a control.
- **The model never supplies the reason.** It can ask "what drove the 27 percent increase in travel expense?" It must not answer.
- **Step 3 has a built-in failure to test for.** If the prior-year balance is zero, the percentage change divides by zero. A script that handles this silently, rather than flagging it, can hide a new account. Test with a zero-balance account on purpose.
- **Step 4 can go stale.** A threshold hard-coded last year and never reviewed is a consistent, deterministic, wrong rule.

---

*Part of [Module 19: Decision Models](../README.md).*
