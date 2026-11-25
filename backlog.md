# Backlog: PythonMuse AI Accounting Framework

*Outstanding tasks, assigned work, and ideas for future sessions.*

**Last updated:** 2026-11-25

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

## Framework Enhancements from ai-ledger Articles 10-46 (2026-11-25)

*Gap review of the ai-ledger series against modules 01-18. Telemetry content: run evidence comes from Article 46; monitoring over time is original framework content and should be marked as going beyond the articles.*

### New modules (priority order)

| # | Module | Topic | Source articles | Status |
|---|--------|-------|-----------------|--------|
| 9 | 19 Decision Models | Choose the method per step (rules, decision model, LLM, person); build-time vs run-time AI; probability bands; cost per acceptable decision; model selection as a control | 42, 43, 36 | Drafted on branch add-decision-models-module |
| 10 | 20 Run Evidence and Telemetry | Run ID, input and rules fingerprints, code version, explicit run status, append-only JSONL log, no silent overwrites, rollback; original content on monitoring over time (exception rate, review overrides, cost, confidence drift, model-change notices) | 46, 40, 39, 37 | Not Started |
| 11 | 21 Operator Handoff | Five roles, front door, input contract (block/warn), operator acceptance test, lifecycle from Build to Retire, Unavailable Tomorrow Test, ONBOARD sequence | 46, 40, 35 | Not Started |
| 12 | 22 Untrusted Content and Boundaries | Prompt injection ("evidence informs, policy instructs"), read/recommend/act ladder, instruction-integrity canary, research boundaries and source register, customer-contract check, Zero Trust and Four Levels of AI Control | 37, 44, 38, 13 | Not Started |

### Expansions to existing modules

| # | Module(s) | Enhancement | Source articles | Status |
|---|-----------|-------------|-----------------|--------|
| 13 | 03, 10 | Accounting-formatted numbers such as ($1,234.56); convert PDF to Markdown once; a skill that documents a workbook layout | 24, 16, 15 | Not Started |
| 14 | 05, 06 | Schema-driven sanitization (schema inventory, synthetic data, sanitize and restore with a local mapping); local models and licence checks | 23, 41 | Not Started |
| 15 | 08, 09 | Workings-layer starter kit; prompts/ and evidence/ folders in scaffolds; checkpoint habit for long sessions | 22, 20c, 26 | Not Started |
| 16 | 11 | Close-period tags and the reproducibility test; branch protection; "which prompt produced it" in the PR checklist; SharePoint vs Git | 20f, 20e, 20d | Not Started |
| 17 | 13 | Multi-agent orchestration; MCP; Copilot-only environments; vendor acceptance and exit test; model-per-step | 19, 34, 33, 39, 14 | Not Started |
| 18 | 15 | Upgrade the run-log template to the Article 46 fields (ties to module 20); Trust but Verify six-gate checklist | 46, 13 | Not Started |
| 19 | 01, 14 | Exploratory vs repeatable vs audit-ready decision; headers-only planning; the three mindsets of AI adoption | 10, 11, 21 | Not Started |
| 20 | 17 | Routine folder structure and proposed-change template | 30 | Not Started |

### Housekeeping

| # | Task | Status |
|---|------|--------|
| 21 | Add module 18 to the root README index once 18-governance-agents is committed | Blocked (18 uncommitted) |
| 22 | Add the module 18 to 19 Next link in 18-governance-agents/README.md, and chain Next links for 19-22 as they are built | Blocked (18 uncommitted) |

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
