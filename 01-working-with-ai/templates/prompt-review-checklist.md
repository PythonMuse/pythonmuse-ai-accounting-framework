# AI Output Review Checklist

*Use this checklist every time you receive output from an AI tool. Treat it the same way you would treat a workpaper prepared by a staff accountant.*

*If you find yourself running the same checks month after month, that is a signal: the context behind those checks — what you are verifying, what thresholds matter, what the source data looks like — should be captured in a reusable [SKILL](../../13-skills-agents-models/templates/skill-template.md). A skill turns a one-time review habit into a documented, repeatable procedure.*

---

> **Use sample or masked data when practicing.** If you are working through these checks for the first time, use the synthetic data provided with this framework — not real company files. For guidance on handling sensitive data with AI tools, see [Safe AI Data Workflows](https://github.com/PythonMuse/ai-ledger/tree/main/articles/06-safe-ai-data-workflows). When you apply this checklist to production workflows, ensure each AI-assisted process is logged — see [AI Governance for Controllers](https://github.com/PythonMuse/ai-ledger/tree/main/articles/07-ai-governance-for-controllers).

## Before You Accept the Output

### Data Accuracy
- [ ] Do the totals in the output match the totals in the source data?
- [ ] Are row counts consistent? (e.g., if the source has 150 transactions, does the output account for all 150?)
- [ ] Spot-check at least 3-5 individual values against the source file
- [ ] Are dates, account numbers, and descriptions accurate (not reformatted or truncated)?

> **PythonMuse Tip:** If you are specifying expected totals, row counts, or source file details each time you run this analysis, capture them as inputs in a `skill.md`. Next month, the SKILL already knows what to expect and what to check.

### Calculation Integrity
- [ ] Are calculations correct? (Manually verify at least 2-3 key figures)
- [ ] Are formulas or logic applied consistently across all rows?
- [ ] Are percentages calculated correctly (correct numerator and denominator)?
- [ ] Are signs correct? (Debits vs credits, positive vs negative)

> **PythonMuse Tip:** Calculation rules — how signs work, which accounts are revenue vs expense, what thresholds trigger flags — are exactly the kind of logic that belongs in a SKILL's Steps section. Document them once rather than re-explaining them in every prompt.

### Completeness
- [ ] Are all expected accounts, transactions, or records present?
- [ ] Are there any missing rows, gaps in sequences, or unexplained exclusions?
- [ ] Does the output include all columns you requested?

### Fabrication Check
- [ ] Are there any numbers in the output that do not exist in the source data?
- [ ] Do descriptions match the source exactly (AI can paraphrase or "improve" text)?
- [ ] Are there any account names or vendor names that look plausible but are not in your data?

> **PythonMuse Tip:** If you keep catching the same fabrication patterns — invented vendor names, rounded dollar amounts, plausible but fake account numbers — add them as explicit review checks in your SKILL's Review Checklist section so the AI and future reviewers know what to watch for.

### Logic Transparency
- [ ] Can you explain how each output value was derived?
- [ ] Did the AI document its assumptions?
- [ ] If you asked for filtering or flagging, are the criteria applied correctly?
- [ ] Could a colleague follow the logic without additional explanation?

### Reproducibility
- [ ] Could you re-run this process and get the same result?
- [ ] Are the instructions specific enough that a different AI session would produce identical output?
- [ ] Are source files preserved (nothing modified in raw data)?

> **PythonMuse Tip:** If the answer to "could I re-run this?" is "yes, but I would need to type the same prompt again" — that is a SKILL waiting to be written. Save the prompt, inputs, and expected outputs as a `skill.md` so next month you run it instead of rebuilding it. See the [Skill Template](../../13-skills-agents-models/templates/skill-template.md).

### Professional Standards
- [ ] Would you sign off on this as a workpaper?
- [ ] Is the output organized and clearly labeled?
- [ ] Could this withstand questions during an audit or review?
- [ ] Is sensitive data appropriately handled (no PII in outputs that will be shared)?

---

## If Something Fails

If any item above does not pass:

1. **Identify the issue.** Which check failed? What specifically is wrong?
2. **Ask the AI to explain.** "Show me how you calculated the variance for account 5100."
3. **Provide correction.** "The total should be $42,350, not $42,530. Recheck the calculation."
4. **Re-verify after correction.** Do not assume the fix is correct. Check again.
5. **Update the SKILL and Agent.** Ask the AI to update the applicable SKILL definition (inputs, logic, thresholds, edge cases) to reflect what you learned. If the workflow uses an Agent, update its instructions as well. This ensures the fix is documented and the same issue does not repeat next month.

---

## Quick Version (For Daily Use)

After you have built the habit, use this shortened version:

- [ ] Totals match source?
- [ ] Spot-checked 3 values?
- [ ] No fabricated data?
- [ ] Logic is clear?
- [ ] Would I sign off on this?

> **PythonMuse Tip:** When this quick version feels routine, your workflow has matured. Formalize it: capture the full context — data sources, logic, output format, and these review checks — in a [`skill.md`](../../13-skills-agents-models/templates/skill-template.md). The SKILL becomes the documented procedure; this checklist becomes the quality gate.
>
> Now think about what happens next. You have a SKILL that knows the inputs, the rules, and the expected outputs. You have a checklist that validates the results. Pair that SKILL with an [Agent](../../13-skills-agents-models/) — a set of instructions that tells the AI how to execute the SKILL, where to find the data, and what controls to follow — and you have something remarkable: your first AI team member.
>
> Not a chatbot you have to re-explain things to every month. A documented, governed, repeatable process that you can hand off the way you would hand off a procedure to a trained staff accountant — with clear instructions, defined boundaries, and a review step before anything is final.
>
> That is the path from checklist to SKILL to Agent. And it starts right here, with the work you are already doing.

---

*Back to [Working With AI](../)*
