# Folder Structure Template for Accounting AI Projects

*Copy this structure to start any new accounting AI project. Every folder has a purpose.*

---

## The Structure

```
project-name/
│
├── CLAUDE.md                 # AI instructions and canary value
├── plan.md                   # Project scope and blueprint
├── status_update.md          # Rolling progress tracker
├── backlog.md                # Future tasks and improvement ideas
│
├── data/
│   ├── raw/                  # Original source files -- NEVER modify
│   │   ├── .gitkeep
│   │   └── (your source CSVs, exports, statements)
│   │
│   └── processed/            # Cleaned and transformed data
│       ├── .gitkeep
│       └── (standardized, merged, or filtered files)
│
├── src/                      # Scripts and logic files
│   ├── .gitkeep
│   └── (Python scripts, analysis code)
│
├── outputs/                  # Generated reports and results
│   ├── .gitkeep
│   └── (final CSVs, summaries, charts)
│
└── docs/                     # Notes, memos, reference material
    ├── .gitkeep
    └── (process documentation, meeting notes, research)
```

---

## What Goes Where

### CLAUDE.md (Project Root)
Instructions that the AI reads automatically at the start of every session. Includes your canary value, project rules, and behavioral instructions.

### plan.md (Project Root)
Defines what you are doing, what data you are using, and what the expected outputs are. Think of it as your engagement letter.

### status_update.md (Project Root)
Rolling log of what has been completed, issues encountered, and next steps. Updated after every session milestone.

### data/raw/
**The golden rule: never modify files in this folder.**

This is where original source files go -- bank statements, GL exports, reports from your ERP. If you need to clean or transform the data, save the result to `data/processed/`.

### data/processed/
Cleaned, standardized, or transformed data. This is where your scripts save intermediate files that are ready for analysis.

### src/
Python scripts, analysis code, and any logic files. If the AI generates a script, it goes here.

### outputs/
Final deliverables -- reconciliation reports, variance summaries, charts, formatted Excel files. These are what you would include in your workpapers or share with management.

### docs/
Supporting documentation -- process notes, research, meeting summaries, policy references. Anything that provides context but is not part of the active workflow.

---

## Quick Setup Commands

To create this structure from the terminal:

```bash
mkdir -p project-name/{data/raw,data/processed,src,outputs,docs}
touch project-name/{CLAUDE.md,plan.md,status_update.md,backlog.md}
touch project-name/data/raw/.gitkeep
touch project-name/data/processed/.gitkeep
touch project-name/src/.gitkeep
touch project-name/outputs/.gitkeep
touch project-name/docs/.gitkeep
```

---

*Template from the [PythonMuse AI Accounting Framework](https://github.com/PythonMuse/pythonmuse-ai-accounting-framework)*
