# Validation and Evidence

*A correct answer is great. A reviewable answer is better.*

---

## The Question That Does the Work

One question separates AI output you can put in a workpaper from AI output you cannot:

> **Based on what?**

Ask an AI why travel expense rose and you will get a fluent, confident, plausible paragraph about post-pandemic travel normalization and expanded client coverage. It reads like something a competent senior wrote.

It may also be entirely invented. The model was not given headcount data, travel policy changes, or client roster movement. It produced an explanation shaped like the explanations it has seen, because that is what it was asked for.

The paragraph is not wrong because the model is bad. It is unsupported because nothing in the request required support.

---

## Why Every Model Does This

Worth understanding once, because it explains the whole module:

**The training reward is not accuracy. It is response quality.**

Models are trained toward answers that read well -- complete, confident, well-organized. Accuracy correlates with that most of the time, which is exactly what makes the exceptions dangerous. An unsupported answer and a supported one look identical on the page.

This is not a flaw that the next model release fixes. Expect it from every model, indefinitely, and design around it.

---

## "Are You Sure?" Is Not a Control

The instinctive check is to ask the model whether it is confident. Sometimes it will apologize and revise. Often it will simply reassert, more smoothly.

Asking a model whether it is sure is the same as asking the intern who made the mistake whether they are confident. You are querying the same source that produced the problem. That is not a second look -- it is the first look, repeated.

A real control looks outward: to the source data, to the totals, to something that can disagree.

---

## Separate Facts From Assumptions

The most useful single prompt in this module:

> Separate what you calculated from the source data from what you inferred or assumed. List them in two columns.

Then push it into a support table:

| Statement made | Source data supporting it | Fully / partially / unsupported | What to verify manually |
|---|---|---|---|
| Travel rose $32.5K over prior year | `gl_detail_2026-06.csv`, account 7200 | Fully supported | Tie to trial balance |
| Driven by expanded client coverage | None | **Unsupported** | Confirm with FP&A |

The moment the middle column is empty, you know exactly what you are dealing with. Nothing about the sentence changed -- only whether it can be defended.

**Keep the conclusion separate from the support.** They are two documents, not one. A conclusion mixed into its own evidence cannot be reviewed independently, and a reviewer who has to disentangle them will skim instead.

---

## The Tie-Out Report

For any recurring workflow, require a tie-out report alongside the answer:

- Source files used, with filenames
- Row counts: read, processed, excluded
- Control totals on both sides of the process
- Reconciling differences, if any
- Accounts or records excluded, and why
- Errors, missing values, unmapped items

This is not new work. It is the tie-out you would perform on a workpaper prepared by a person, written down. Requiring it from AI is the same standard, applied consistently.

---

## Ask AI to Self-Validate Before You Review

You can put a substantial amount of this on the AI itself -- not as a substitute for review, but so review starts from a better place. Add to your agent file:

> Before saving any output, produce a self-validation section covering: (1) which files you read, (2) row counts in and out with any difference explained, (3) whether totals tie to source and by how much if not, (4) every assumption made, (5) anything you could not determine and had to leave open.

Save it to `evidence/self_validation.md`. The model is much better at reporting what it did than at judging whether what it did was right -- so use it for the first and keep the second.

---

## Where the Evidence Lives

Give evidence a folder, the same way you give raw data a folder:

```
evidence/
  run-logs/          What ran, when, against which inputs
  tie-outs/          Control totals and reconciliations
  self_validation.md What the AI reported about its own run
  review-notes/      What the human reviewer checked and concluded
```

The test is simple: **six months from now, could someone reconstruct what happened without you?** If the answer depends on your memory, the evidence folder is not doing its job.

---

## Two Checklists

Match the checklist to where the work is happening.

### Working in chat

- [ ] Did I state the source data, or did the model infer it?
- [ ] Have I asked it to separate facts from assumptions?
- [ ] Did I tie at least one total back to the source myself?
- [ ] Have I removed unsupported confidence from the narrative?
- [ ] Do I know which statements would fail a reviewer's "based on what?"
- [ ] Have I saved the prompt, so next month is not improvised?

### Working in a harness

- [ ] Is `data/raw/` unmodified?
- [ ] Did a script perform the calculations, rather than the model?
- [ ] Do row counts reconcile between input and output?
- [ ] Do control totals tie, and is any difference explained?
- [ ] Is the output file dated and saved outside the raw folder?
- [ ] Does `evidence/` contain something a reviewer could follow?
- [ ] Can this be re-run next month without re-explaining it?

---

## Let the Code Calculate

A rule worth adopting series-wide:

```
Let the code calculate.
Let the model explain.
Let the accountant review.
```

Models are good at language and unreliable at arithmetic under pressure. Scripts are the reverse. A script that computes a variance produces the same number every time, is readable line by line, and -- unlike a conversation -- is not influenced by which model wrote it. When the vendor changes the model next quarter, the script does not care.

Put the numbers in the script. Put the narrative in the model. Put the judgment in the human.

---

## The Control Ladder

Everything in this framework sits on one of four rungs:

```
Metadata informs.
Scripts validate.
Hooks enforce.
Evidence proves.
```

| Rung | What it does | Where it lives |
|------|-------------|---------------|
| **Metadata informs** | Labels the file so the right one gets picked up | [Module 16](../16-configuration-literacy/) |
| **Scripts validate** | Recalculates and checks -- and can fail loudly | This module |
| **Hooks enforce** | Stops an action before it happens | [Module 06](../06-hooks-as-controls/) |
| **Evidence proves** | Records what actually occurred | This module |

They are not alternatives. A workflow with metadata but no enforcement is a workflow with good intentions. One with enforcement but no evidence cannot demonstrate that the control operated.

---

## Try This

1. Take an AI answer you found convincing and ask it to build the support table. Note how much lands in the unsupported column.
2. Add a tie-out requirement to one recurring workflow.
3. Create `evidence/` in a real project and put one thing in it.
4. Pick your riskiest workflow step and decide which rung it needs -- and whether it is currently on a lower one.

---

## Key Takeaway

Validation is not distrust of AI. It is the same professional skepticism you already apply to work prepared by anyone else, applied to a preparer that is fluent, fast, tireless, and occasionally confidently wrong.

Ask "based on what?" Separate facts from assumptions. Make the code do the arithmetic. Keep the evidence. Those four habits make AI output reviewable -- and reviewable is the standard that matters.

---

*Next: [Configuration Literacy](../16-configuration-literacy/) -- reading the files that tell your workflow what to do.*
