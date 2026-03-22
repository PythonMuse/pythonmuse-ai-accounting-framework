# Project Folder Scaffold

*Copy-paste ready structure for starting any accounting AI project.*

---

## Full Structure

```
project-name/
│
├── CLAUDE.md
├── plan.md
├── status_update.md
├── backlog.md
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── .gitkeep
│   └── processed/
│       └── .gitkeep
│
├── src/
│   └── .gitkeep
│
├── outputs/
│   └── .gitkeep
│
└── docs/
    └── .gitkeep
```

---

## Starter CLAUDE.md

```markdown
# Project Instructions

## Canary
The canary is: [YOUR UNIQUE VALUE]

## Rules
- Always read plan.md and status_update.md at the start of a session
- Never modify files in data/raw/
- Save all outputs to the outputs/ folder
- Update status_update.md after completing each major step
- All dates in YYYY-MM-DD format
```

---

## Starter plan.md

```markdown
# Project Plan

## Objective
[What are you building or analyzing?]

## Data Sources
| Source | File | Location |
|--------|------|----------|
| [source] | [file] | data/raw/ |

## Steps
1. [Step 1]
2. [Step 2]

## Expected Outputs
| File | Description | Location |
|------|-------------|----------|
| [file] | [description] | outputs/ |
```

---

## Starter status_update.md

```markdown
# Status Update

## Session 1 -- [Date]
**Summary:** Project initialized.
**Completed:** Created project structure.
**Next Steps:** [First task]
```

---

## Setup Command

Run this in your terminal to create the entire structure:

```bash
mkdir -p my-project/{data/raw,data/processed,src,outputs,docs}
touch my-project/{CLAUDE.md,plan.md,status_update.md,backlog.md,.gitignore}
touch my-project/{data/raw,data/processed,src,outputs,docs}/.gitkeep
cd my-project && git init
```

---

*Template from the [PythonMuse AI Accounting Framework](https://github.com/PythonMuse/pythonmuse-ai-accounting-framework)*
