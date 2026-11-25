# Decision Models -- Choosing the Method for Each Step

*Before you ask which AI model to use, ask what kind of work the step actually is.*

---

## Why This Module Exists

"Can we use AI for this?" is the wrong question. A bank reconciliation, a variance analysis, or a month-end close is not one kind of work. It is a sequence of steps, and the steps are different from each other: a calculation, a match, a piece of reading, a judgment call, an approval.

Each step can use a different method. Some should never involve a language model at all. Choosing the method step by step is a control decision, the same as deciding who may approve a journal entry and who may only prepare one.

This module gives you a way to make that choice on purpose. It builds on [Skills, Agents, and Models](../13-skills-agents-models/), which covers model tiers and cost, and goes one question earlier: does this step need a model at all?

> The ideas here come from the PythonMuse articles [AI Helped Me Build It. AI Does Not Have to Run It.](https://github.com/PythonMuse/ai-ledger/tree/main/articles/42-ai-helped-me-build-it), [Does This Decision Actually Need a Large Language Model?](https://github.com/PythonMuse/ai-ledger/tree/main/articles/43-does-this-decision-need-an-llm), and [Model Selection Is an Accounting Control](https://github.com/PythonMuse/ai-ledger/tree/main/articles/36-model-selection-is-a-control). Read them for the full argument and the working demos.

---

## "Deterministic" in Plain English

Accountants have used deterministic processes for decades.

> **Same inputs + same rules = same outputs.**

A SUM formula is deterministic. An aging calculation is deterministic. A rule that sends every payment over $25,000 for second approval is deterministic: the system does not wake up on Tuesday and decide that $24,750 feels suspicious.

A large language model (LLM) works differently. It generates its answer from probabilities. Give it substantially the same instructions and data twice, and the wording, the classification, or the conclusion can change.

That flexibility is why an LLM is good at reading messy language. It is also why its output needs validation. Neither approach is better in general. They are built for different kinds of work.

---

## Build-Time AI vs Run-Time AI

Take duplicate-payment testing. There are two ways to do it.

**Option one:** upload the AP payment data to an LLM every month and ask which payments look like duplicates. It may find useful items. Next month it may read the request differently, skip a record, or flag two payments that only resemble each other.

**Option two:** ask AI to help you *build* a script that applies the criteria your team approved -- same vendor, same invoice, same amount, paid within 30 days -- and hands every match to an accountant. The script decides nothing. It finds what meets the rule, the same way, every month.

The difference is **build-time AI** and **run-time AI**:

| | Build-time AI | Run-time AI |
|---|---|---|
| **When** | While you design and test the workflow | Every time the workflow runs |
| **Does what** | Writes the script, explains it, makes test data, suggests test cases | Processes the real data and makes or recommends the call |
| **Your data** | Stays out of it (use synthetic samples) | Goes to the model, so privacy, contract, and cost questions apply every run |
| **Accounting analogy** | The consultant who designs your close checklist | The staff accountant who works it every month |

AI at build time is almost always a good idea. AI at run time is a design decision, not a default. Once the script is tested, the model can go home. The script keeps working.

---

## Classify Each Step, Not the Whole Process

Four kinds of work cover most steps:

| Kind of work | The test | Typical home |
|---|---|---|
| **Rules** | Can we state exactly how the result is calculated or classified? | Formula, Power Query, SQL, Python |
| **Patterns** | Do past examples hold a relationship we cannot write down? | A model trained on your own history |
| **Language** | Does the work require reading or writing free text? | An LLM, with validation and review |
| **Judgment** | Does it need professional accountability? | A qualified person |

Aging buckets, thresholds, and matching criteria are rules. Estimating which receivables are likely to go delinquent is a pattern. Summarizing a long dispute email thread is language. Approving a write-off is judgment, and AI should not quietly inherit that authority because it helped automate the steps before it.

Before classifying anything, ask whether the step is still needed. Automating a process nobody understands is just an efficient way to produce confusion on a schedule.

The one-page version is in [step-classification-worksheet.md](templates/step-classification-worksheet.md). A worked example is in [variance-analysis-step-breakdown.md](examples/variance-analysis-step-breakdown.md).

---

## The Missing Middle: the Decision Model

Between "write a rule" and "let an LLM write an essay" there is a third option. A **decision model** does not generate text. It *chooses* from a list of answers you supply, usually with a probability attached. "Pick the reason code for this late payment: incorrect PO, pricing dispute, short pay, other." "Rate the urgency from 1 to 4."

The way to tell which method fits is to look at the shape of the answer the step needs:

| What the step needs | Start with | Example |
|---|---|---|
| A known calculation, threshold, or match | Deterministic automation | Remittance advice goes to cash application |
| A choice among known answers, or a score | Decision model | Pick the late-payment reason code |
| Reading or writing open-ended language | LLM | Summarize a dispute thread and draft questions |
| Professional judgment or accountability | A person | Approve a credit memo |

The underlying question is: **do I need the model to generate an answer, or to choose among answers I already understand?** If it is the second, a smaller, cheaper, more testable tool may do the job.

---

## One Workflow, Several Methods

Real processes use more than one method, layered like a review chain:

```
Rules clear the items they can settle.
A decision model sorts what the rules cannot.
An LLM summarizes the hard ones, if policy allows it.
A person decides and owns the call.
```

In an AP exception queue, rules clear most invoices without any model. A decision model routes the exceptions. An LLM reads the few long email threads. The accountant keeps approval and the accounting treatment. That is not an "LLM workflow." It is a controlled process with several kinds of work inside it.

In a year-over-year variance review: **Python calculates the 27 percent. AI suggests questions for the account owner. The accountant finds, supports, and owns the explanation.** The model should never invent the reason travel expense went up.

---

## A Probability Is Only Useful With a Plan

Most decision models return a probability, and that creates a natural control. Decide in advance what happens at each level of certainty, the same way an expense policy decides what happens at each dollar amount.

| Model output (example) | Band | What happens |
|---|---|---|
| Incorrect PO -- 96% | High | Route automatically, log it |
| Incorrect PO -- 78% | Middle | A person confirms before routing |
| Incorrect PO 47%, Pricing dispute 42%, Other 11% | Low or split | A person decides |

Three rules go with this table:

- **Set the thresholds from your own results.** Never copy 96 percent from an article, including this one. Test the model on your own labeled history and choose the bands from what you see and from your risk tolerance.
- **A "confidence" number is not proof of accuracy.** It does not tell you the model is right that often on *your* work. Only your own examples can.
- **Freeze the wording.** Scores can shift when the question or the list of answers changes. Treat the prompt and the answer list like a control setting: change it only through review.

The model recommends. Deterministic logic decides what authority the recommendation gets. A person stays responsible for the consequential call.

---

## The Cheapest Model Is Not the Cheapest Process

When a workflow makes the same decision thousands of times, per-decision cost matters. But the price per call is the wrong measure. A better one is **cost per acceptable decision**:

```
(model cost + review time + cost of wrong routing and missed exceptions)
        divided by the share of decisions that came out right
```

A model that costs almost nothing but sends half the items to an accountant has not improved the process. It has moved the cost from the invoice to the payroll line.

The script [cost_per_acceptable_decision.py](examples/cost_per_acceptable_decision.py) compares five approaches on synthetic numbers. Change the inputs in [decision_scenarios.csv](examples/data/decision_scenarios.csv) to see which one actually moves the answer. In the sample data, the cheapest model produces the most expensive process.

---

## Deterministic Does Not Mean Correct

Deterministic automation has real control advantages. The logic can be inspected, tested against known answers, version-controlled, and approved. A run log shows what was processed.

But a script can apply the wrong rule perfectly, every month, forever.

Suppose the duplicate-payment script compares vendor names exactly. "ABC Corp" and "ABC Corporation" are not the same string, so the script misses a pair with the same invoice number and the same amount, paid a week apart. A person would spot it in a second. The script misses it consistently, on every run. The rule is not broken. It is exactly what was approved. It is just incomplete, and the consistency makes that invisible until someone tests for it.

Consistency makes a process testable. It does not make testing optional. Test against known answers, control totals, and documented exceptions, and treat a change to the logic as you would a change to an important spreadsheet or a system configuration. That is what it is.

---

## Model Selection Is a Control

Once a step does need a model, the choice of model is part of the control environment, not a personal preference. Ask these in order:

1. **Is it permitted?** Permission comes before capability. The most capable model is irrelevant if the data cannot go to it.
2. **What happens if the model is wrong?** A wrong reason code on an internal queue is not a wrong accrual.
3. **How hard is the output to check?** A number you can tie to the ledger is easy to verify. A paragraph of reasoning is not.
4. **What is the minimum evidence the model needs?** If the step needs one of five reason codes, it does not need the whole email chain. The safest confidential field is the one never sent.
5. **What happens when the model changes?** A vendor update can change results with no change on your side. Record which model is approved, and retest when it moves.

Two cautions:

- **A decision model is not a loophole.** A customer contract may restrict machine learning, automated decision-making, or external processing. Swapping the type of model does not remove the obligation. Treat the restriction as a reason to talk to the contract owner, not as a puzzle.
- **Being allowed to classify is not being allowed to approve.** The model can propose a reason code. It does not decide the credit memo.

Record the answers in the [model-selection-record.md](templates/model-selection-record.md) template. A reviewer's first question should be "why this method?" before it is "which vendor?"

---

## Try This

1. Pick one process you own. List its steps and classify each as rule, pattern, language, or judgment, using the [worksheet](templates/step-classification-worksheet.md).
2. Find one step currently done by pasting data into a chat window every month. Ask: is this a rule you could write down? If yes, that step is a candidate for a tested script that AI helps you build and never has to run.
3. Open [cost_per_acceptable_decision.py](examples/cost_per_acceptable_decision.py) with Claude, change the error cost and the review time, and find the point where the ranking flips.
4. For one step that uses a model, fill in a [model selection record](templates/model-selection-record.md).

---

## Key Takeaway

Do not label a whole process an "AI use case." Classify each step by the kind of work it is, use the simplest method that is safe and testable, and keep a person accountable for every consequential call. AI can help you build almost any of it. It does not have to run all of it.

Pick the method the way you would pick a control: for the risk, not for the novelty.

---

*Next: Run Evidence and Telemetry -- how a run proves what it did, and how you notice when it starts to drift (coming soon). Return to the [Table of Contents](../README.md).*
