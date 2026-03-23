# Working With AI -- Not Just Prompting It

*AI is not Google. It is more like a new staff accountant who needs context, direction, and review.*

---

## The Difference Between Searching and Working

When you Google something, you type a few keywords and scan the results. The interaction is one-directional. You ask, you get a list, you pick.

Working with AI is fundamentally different.

You are not searching for an answer. You are building one -- iteratively, through conversation.

The process looks like this:

1. **Give context.** What are you working on? What does the data look like? What is the goal?
2. **Refine instructions.** The first response is rarely the final answer. Clarify, narrow, redirect.
3. **Review outputs.** Check the work against your source data. Verify the logic.
4. **Iterate.** Adjust and continue until the output meets your standards.

This is not a new skill for accountants. It is exactly how you work with a junior team member.

---

## Prompting vs Working With AI

| Prompting | Working With AI |
|-----------|-----------------|
| One question, one answer | Ongoing conversation |
| Generic input | Context-rich input |
| Accept the first response | Refine through iteration |
| No verification | Review against source data |
| Disposable interaction | Documented workflow |

Most "prompt engineering" advice focuses on the left column. What actually produces reliable results in accounting is the right column.

---

## Why Context Changes Everything

Consider these two approaches to the same task:

**Without context:**
> "Reconcile this data."

**With context:**
> "I have a bank statement export (CSV, columns: date, description, amount) and a general ledger export (CSV, columns: posting_date, vendor, debit, credit). I need to match transactions by amount and date within a 3-day window. Flag anything over $500 that does not match. Output the results as a CSV with columns for bank_amount, gl_amount, match_status, and notes."

The second version gives the AI everything it needs to produce useful output on the first attempt. The first version will require five rounds of clarification.

Think of it this way: if you emailed that first instruction to a new hire, you would expect follow-up questions. AI is the same.

---

## The Review Mindset

Every output from AI should be treated the same way you treat work from a staff accountant:

- **Does the math check out?** Verify totals, subtotals, and calculations against your source data.
- **Are the assumptions reasonable?** Did the AI make decisions you did not explicitly approve?
- **Is anything fabricated?** AI can generate plausible-looking numbers that have no basis in your data. Always trace outputs back to inputs.
- **Is the logic transparent?** Can you explain how the output was produced? If not, ask the AI to show its work.

This is not about distrusting the tool. It is about applying the same professional skepticism you already use every day.

---

## Try This: Starter Exercises

### Exercise 1: The Context Experiment

Take a simple task you do regularly (reviewing an expense report, checking a bank balance, summarizing a trial balance).

1. Ask your AI tool to help with the task using a one-sentence prompt
2. Note what is missing from the response
3. Add context: file format, column names, what "done" looks like
4. Compare the two responses

You will see immediately why context matters.

### Exercise 2: The Iteration Loop

Pick a small data file (a CSV with 20-30 rows). Use the sample data provided with this framework or create a masked test file — do not use real company data while learning. (See [Safe AI Data Workflows](https://github.com/PythonMuse/ai-ledger/tree/main/articles/06-safe-ai-data-workflows) for guidance.) Ask the AI to analyze it. Then:

1. Ask it to change the output format
2. Ask it to add a filter
3. Ask it to explain its logic
4. Ask it to save the results

Notice how each step builds on the previous one. This is working with AI.

### Exercise 3: The Verification Check

Ask the AI to calculate something you already know the answer to. A column total, an average, a count. Compare the AI output to your manual check.

This exercise builds the habit of verification and shows you where AI is reliable and where it needs supervision.

---

## Key Takeaway

AI is most useful when you treat it like a capable but unseasoned team member. Give it clear instructions, provide the context it needs, review its work, and iterate until the output meets your professional standards.

The accountants who get the most from AI are not the ones who write the cleverest prompts. They are the ones who bring the same discipline to AI interactions that they bring to every other part of their work.

---

*Next: [Markdown for Accountants](../02-markdown-for-accountants/) -- the simplest documentation tool you will use with AI.*
