# Configuration Literacy -- YAML, Front Matter, and Manifests

*A configuration file is a written procedure that a computer can read. You already write procedures.*

---

## Why This Module Exists

Once AI starts doing repeatable work, you stop reading only prose and start encountering short structured files: a workflow configuration, a header block at the top of a skill file, a spreadsheet listing which inputs are approved.

None of them are code. All of them are reviewable. And every one of them can quietly change what a workflow does.

You do not need to write these from scratch -- AI will draft them. You need to be able to **read one and say whether it is right**, the same way you review a journal entry someone else prepared.

---

## The Four Layers

A working AI workflow usually has four kinds of file in it. Knowing which is which tells you where to look when something goes wrong.

| Layer | File type | What it handles | Accounting analogy |
|-------|----------|----------------|-------------------|
| **Logic** | Python `.py` | Calculations, transformations, steps | The associate running the process |
| **Configuration** | YAML `.yaml` | Structure, triggers, permissions, sequence | The written SOP the associate follows |
| **Data** | SQL `.sql` | Pulling records from a database | The query that runs against your ERP |
| **Instructions** | Markdown `.md` | Agent guidance, controls, documentation | The policy memo governing the whole thing |

Python is the worker doing the activity. YAML is the instruction sheet. Confusing the two is how people end up reviewing the wrong file.

---

## Reading YAML Without Fear

YAML is a structured configuration format. It is deliberately plain -- if you can read a nested checklist, you can read YAML.

There are only three patterns.

**A setting is `key: value`.**
```yaml
owner: controller
frequency: monthly
approval_required: true
```

**A list uses a dash per item.**
```yaml
allowed_folders:
  - data/raw
  - data/processed
  - outputs
```

**Indentation shows what belongs to what.**
```yaml
retry:
  attempts: 3
  delay_seconds: 60
```
Here `attempts` and `delay_seconds` belong to `retry`. Indentation is not decoration in YAML -- it is the structure. Two spaces in the wrong place changes meaning.

That is genuinely most of it. `true`/`false` for yes and no, `#` to start a comment.

### Review it like a control document

```yaml
permissions:
  allowed_folders:
    - /
```

That reads harmlessly. It grants access to the entire drive. The difference between that and `- data/raw` is one character, and no error will be raised -- the workflow will simply be able to reach everything.

This is why configuration literacy is a control skill rather than a technical one. The file is short, plain English, and load-bearing.

---

## Front Matter

**Front matter** is a small YAML block at the very top of a Markdown file, fenced by three dashes above and below. It carries information *about* the file, separate from the file's content.

```markdown
---
name: bank-rec-review
description: Reviews a completed bank reconciliation for exceptions
process_area: treasury
owner: controller
data_classification: confidential
ai_allowed: true
cloud_ai_allowed: false
review_required: true
---

# Bank Reconciliation Review

(the actual instructions start here)
```

Everything above the closing `---` is metadata. Everything below is the procedure.

Why it matters: a human reading this sees an ordinary document. A script reading it can check `cloud_ai_allowed: false` and refuse to send the contents to a cloud service. **The same file serves the reader and the control.**

Every `SKILL.md` should carry front matter. Without it, a skill is a document. With it, a skill is a document a control can act on.

### README.md vs SKILL.md

They look similar and serve different audiences:

| File | Written for | Answers |
|------|------------|---------|
| `README.md` | The human | What is this folder, why does it exist, where do I start |
| `SKILL.md` | The AI | What is the procedure, what inputs, what output, what checks |

Writing one and expecting it to do both jobs is the most common structural mistake in a new project.

---

## The Manifest

A **manifest** is a plain list of the files a workflow is allowed to use, and what each one is. Usually a CSV, because a CSV opens in Excel.

```
file_name,folder,period,status,approved_for_ai,data_classification,purpose
gl_detail_2026-06.csv,data/raw,2026-06,final,yes,internal,GL activity for the month
budget_fy26.csv,data/raw,FY26,approved,yes,internal,Approved operating budget
headcount_draft.xlsx,data/raw,2026-06,draft,no,confidential,Not yet approved
```

It looks like a control log because it is one.

Three columns carry most of the weight:

- **`status`** -- `final` and `approved` are usable; `draft`, `superseded`, and `do_not_use` are not. This is the column that stops last month's file from being picked up this month.
- **`approved_for_ai`** -- an explicit decision, made by a person, recorded before the run.
- **`data_classification`** -- what handling this file requires, which determines whether it can leave the machine.

### Who does what

The division of labor is the point:

```
Python does the boring inventory.
The accountant applies judgment.
AI follows the instructions.
Hooks enforce the controls.
Evidence proves what happened.
```

A script can scan a folder and list every file it finds, defaulting each to `needs_review`. It cannot decide whether the November headcount file is appropriate for a June analysis. That is your call, and the manifest is where you record it.

---

## Where to Put Metadata, Where to Put Controls

Two placement rules:

> **Put metadata where the work happens. Put controls where the risk happens.**

Metadata belongs next to the thing it describes -- front matter at the top of the skill, a manifest in the folder it inventories. It is easiest to keep current when it lives where someone is already looking.

Controls belong at the point of exposure. A rule about not sending data to the cloud belongs where the call is made, not in a document three folders away.

When deciding whether something needs its own configuration file, ask: **who needs to read this, and what decision depends on it?** If the answer is "a person, for orientation," it is documentation. If it is "a script, to decide whether to proceed," it is configuration.

### What this is not

This is deliberately low-tech. It is not a search index, a vector database, embeddings, or enterprise document management. It is labeling -- the same discipline as naming a workpaper properly and marking it reviewed, applied to files an AI will read.

Metadata is boring right up until your AI grabs the wrong file.

---

## Try This

1. Open any `.yaml` you can find and identify the settings, the lists, and the nesting. Do not change anything.
2. Add front matter to one skill file, with `data_classification` and `cloud_ai_allowed` filled in honestly.
3. Build a manifest for one real project folder. Default everything to `needs_review`, then go through and make the calls.
4. Find one rule currently living in prose that a script could check instead.

---

## Key Takeaway

Configuration files are short, plain, and consequential. You do not have to write them -- you have to review them, because a permission line or a status column can change what a workflow reaches and which data it picks up.

Read the YAML. Fill in the front matter. Keep the manifest current. This is the "metadata informs" rung of the ladder, and it is the cheapest control in the framework.

---

*Next: [Routines](../17-routines/) -- what happens when the workflow starts running without you.*
