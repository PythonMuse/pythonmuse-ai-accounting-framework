# Project Hygiene -- Managing AI Like a Team Member

*Structure your AI projects the same way you structure an accounting engagement: with clear scope, documented progress, and organized deliverables.*

---

## Why Hygiene Matters

The accountants who get the most from AI are not the ones with the best prompts. They are the ones with the best project structure.

Think about how you manage a new engagement or a month-end close:

- You define the scope (what are we doing?)
- You track progress (what have we done? what is left?)
- You organize deliverables (where do outputs go?)
- You document decisions (why did we do it this way?)

AI projects need the same discipline. Without it, you end up with scattered files, lost context, and workflows that cannot be repeated.

---

## The Three Key Files

AI models work inside a **context window** -- a fixed budget of text covering your instructions, the files opened, and the conversation so far. Two things follow. When the session ends, that context is gone. When the window fills up, the earliest material gets squeezed out, silently.

That is the entire reason for the three files below. They are external memory for a system that has none.

Every AI project should have these three files at the project root. Together, they form a persistent memory system that survives session resets.

### 1. plan.md -- The Engagement Letter

Your plan.md defines what you are building. It includes:

- Project objective
- Key rules and requirements
- Steps to complete
- Input files and expected outputs
- Constraints and assumptions

When a session ends and you start a new one, the AI reads this file and immediately understands the full scope of the project.

See: [sample-plan-md.md](examples/sample-plan-md.md) | [plan-template.md](templates/plan-template.md)

### 2. status_update.md -- The Rolling Checkpoint

This file tracks progress. It answers:

- What has been completed so far?
- What outputs have been generated?
- Were there any issues or errors?
- What are the next steps?

Update this file after every meaningful milestone. It is your Ctrl+S for AI work.

See: [sample-status-update.md](examples/sample-status-update.md) | [status-update-template.md](templates/status-update-template.md)

### 3. backlog.md -- The To-Do List

A running list of future tasks, improvements, and ideas. Prioritized so you always know what to work on next.

See: [sample-backlog.md](examples/sample-backlog.md)

---

## The Before, During, After Framework

### Before a Session

> "Read plan.md and status_update.md. Summarize where we left off and what the next steps are."

This brings the AI up to speed in seconds.

### During a Session

> "We just finished the matching logic. Update status_update.md with what was completed, any issues, and what comes next."

Do this after every milestone. It takes seconds and saves hours.

### After a Session

> "Before we stop, update status_update.md with a full summary of today's work. Include completed steps, output files, open issues, and next steps."

This is your end-of-session save. If the session crashes tomorrow, everything is documented.

---

## Folder Organization

A well-organized project structure should be clear from the file tree alone:

```
project/
  CLAUDE.md             AI instructions and canary
  plan.md               Project scope and blueprint
  status_update.md      Rolling progress tracker
  backlog.md            Future tasks and ideas

  data/
    raw/                Original source files (NEVER modify)
    processed/          Cleaned and transformed data

  src/                  Scripts and logic files

  outputs/              Generated reports and results

  evidence/             What ran, what tied out, what the reviewer concluded
  validation/           Checks the workflow runs against itself

  docs/                 Notes, memos, reference material
```

See: [folder-structure-template.md](templates/folder-structure-template.md)

---

## When You Cannot Restructure the Files

Most accounting files cannot be reorganised. They have been used for three closes, several people touch them, they have linked cells, and they work.

You do not fight that. You layer on top of it: create a `workings/` folder alongside the legacy files, with `data/`, `scripts/`, and `outputs/` inside. Legacy files stay untouched. Git runs inside `workings/` only. Your agent file lives inside `workings/`, not above it -- placement defines scope.

Keeping `workings/` as a template repository you clone each year also gives you something useful: year over year, "did we run the same process?" becomes a `git diff` rather than a memory test.

---

## The Engagement Analogy

| Accounting Engagement | AI Project |
|----------------------|------------|
| Engagement letter | plan.md |
| Workpaper index | Folder structure |
| Progress tracking | status_update.md |
| Open items list | backlog.md |
| Workpaper binder | outputs/ folder |
| Source documents | data/raw/ folder |
| Instructions for the team | CLAUDE.md |

If you have ever managed an audit engagement or a month-end close, you already know how to structure an AI project. The tools are different. The discipline is the same.

---

## Key Takeaway

Project hygiene is not extra work. It is the work that makes everything else work. The difference between a chaotic AI experiment and a reliable AI workflow is three Markdown files and a folder structure.

---

*Next: [Data Structure](../09-data-structure/) -- the raw, processed, output discipline.*
