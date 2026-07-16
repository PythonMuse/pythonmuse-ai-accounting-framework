# Backlog: PythonMuse AI Accounting Framework

*Outstanding tasks, assigned work, and ideas for future sessions.*

**Last updated:** 2026-03-22

---

## Assigned to Patrick

| # | Task | Module | Status | Details |
|---|------|--------|--------|---------|
| 1 | Capture 7 VS Code screenshots | 04 | Not Started | See [screenshot plan](04-vscode-as-workspace/screenshots/plan.md). 7 screenshots mapped to README sections. ~3,500 tokens to insert references once captured. |
| 2 | Create 5 AI Permissions diagrams | 05 | Not Started | See [diagram plan](05-ai-permissions/diagrams/plan.md). 5 diagrams: data flow, permission pyramid, decision tree, sensitivity grid, controls analogy. ~2,500 tokens to insert references once created. |
| 3 | Insert image references after screenshots captured | 04 | Blocked (waiting on #1) | Add `![image](screenshots/...)` tags into README.md and recommended-extensions.md. Insert locations documented in plan.md. |
| 4 | Insert image references after diagrams created | 05 | Blocked (waiting on #2) | Add `![image](diagrams/...)` tags into README.md and local-vs-cloud-checklist.md. Insert locations documented in plan.md. |

---

## Remaining Framework Enhancements

| # | Task | Module(s) | Status | Notes |
|---|------|-----------|--------|-------|
| 5 | Add prompt iteration examples to modules 02-13 | 02-13 | Not Started | Currently only module 01 has prompt iteration files (recon, variance). Modules with repeatable accounting workflows (03, 10, 12) are strong candidates for their own prompt iteration series with Iteration 6 PythonMuse differentiator. |
| 6 | Add data security disclaimers to remaining files | Various | Partially Done | 16 files updated this session. Remaining lower-priority files: `02 workpaper-template.md`, `02 close-checklist.md`, `08 sample-plan-md.md`, `08 plan-template.md`, `09 data-flow-close.md`, `10 README.md`, `10 csv-best-practices.md`. These are medium-risk — templates where users fill in data or reference ERP exports. |
| 7 | Review modules 07-13 for PythonMuse Tips | 07-13 | Not Started | Added PythonMuse Tips to modules 01 and 06 this session. Modules 07 (canary), 11 (git), 12 (SQL), and 13 (skills/agents) are good candidates for similar tips connecting concepts to reusable SKILLs and Agents. |
| 8 | Add encouraging "Claude builds it for you" reminders to remaining technical modules | 07, 11, 12 | Not Started | Applied to all of module 06 this session. Same pattern applies to canary setup (07), git workflow (11), and SQL access (12). |

---

## Completed This Session (2026-03-22)

| # | Task | Details |
|---|------|---------|
| - | Added Iteration 6 transition paragraph to prompt-iteration-recon.md | Bridge between Iteration 5 and 6 ("wouldn't it be great...") |
| - | Formatted Iteration 6 blockquote in prompt-iteration-recon.md | Restored numbered list and blockquote structure |
| - | Fixed typo "reproducable" → "reproducible" in recon summary table | |
| - | Added data security disclaimers to 16 files across modules 01, 03, 09, 12, 13 | Links to Safe AI Data Workflows and AI Governance for Controllers articles |
| - | Added SKILL/Agent update reminder to prompt-review-checklist.md | Step 5 in "If Something Fails" section |
| - | Added 6 PythonMuse Tips to prompt-review-checklist.md | Connecting review habits to building reusable SKILLs, closing with checklist → SKILL → Agent arc |
| - | Added "ask AI to explain code" tip to module 03 README | With data security guidance for pasting code into external AI tools |
| - | Added "Where to Start with AI" article link to module 03 README | For readers who haven't installed Python yet |
| - | Added PythonMuse/Copilot+Claude note to module 04 recommended-extensions.md | |
| - | Created screenshot plan for module 04 | 7 screenshots, assigned to Patrick |
| - | Added governance article links to module 05 permission-audit-template.md | AI Governance for Controllers + AI Governance Assessments |
| - | Created diagram plan for module 05 | 5 diagrams, assigned to Patrick |
| - | Added encouraging reminders to all 4 files in module 06 | "Claude builds it for you" messaging throughout hooks section |
| - | Updated license to dual: CC BY-NC-SA 4.0 (content) + MIT (code) | LICENSE, LICENSE-CODE, README.md updated |
| - | Updated .gitignore for screenshots and diagrams | `**/screenshots/*` and `**/diagrams/*` patterns |

---

*Part of the [PythonMuse AI Accounting Framework](https://github.com/PythonMuse/pythonmuse-ai-accounting-framework)*
