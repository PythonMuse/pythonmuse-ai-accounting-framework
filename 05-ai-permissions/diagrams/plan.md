# Diagram Plan: AI Permissions

*Visual guides to help accountants understand AI data flows, permission models, and decision frameworks.*

**Assigned to:** Patrick
**Status:** Not started
**Created:** 2026-03-22

---

## Purpose

Module 05 explains where data goes when using AI tools, what permissions different tools have, and how to decide what is safe to use with what data. These concepts are fundamentally visual — data flowing between your machine and the cloud, permission levels stacking up, decision trees branching. Diagrams will make the abstract concrete, especially for readers who are visual learners or who need to present this to their team or management.

---

## Diagram List

### 1. Data Flow: Local vs Cloud vs Hybrid

| Field | Detail |
|-------|--------|
| **Filename** | `data-flow-local-cloud-hybrid.png` |
| **README section** | "Local vs Cloud: Where Does Your Data Go?" |
| **What to show** | Three side-by-side flow diagrams: |
| | **Local:** Your Machine → Python/pandas → Results (all inside a "Your Computer" boundary box) |
| | **Cloud:** Your Machine → Internet → Cloud API → Response → Your Machine (data crosses a boundary) |
| | **Hybrid:** Your Machine runs code locally, but sends prompts to Cloud API for reasoning (split flow — code execution stays inside, reasoning crosses the boundary) |
| **Key visual elements** | Clear boundary line between "Your Environment" and "External." Use a lock icon inside the local boundary. Use arrows showing data direction. Label what crosses the boundary (prompts, file contents, metadata). |
| **Style** | Simple boxes and arrows. No need for fancy graphics — clarity over design. |
| **Insert after** | "Understanding this distinction is critical for deciding which data you can use with which tools." (README ~line 47) |

---

### 2. Permission Levels Pyramid

| Field | Detail |
|-------|--------|
| **Filename** | `permission-levels.png` |
| **README section** | "Permission Models: What Can AI Do?" |
| **What to show** | A layered pyramid or stacked bar showing permission escalation from least to most access: |
| | **Level 1 (bottom):** Read — AI can see your files |
| | **Level 2:** Write — AI can create or modify files |
| | **Level 3:** Execute — AI can run scripts and commands |
| | **Level 4:** Network — AI can send data externally |
| | **Level 5 (top):** Store — Provider retains your data |
| **Key visual elements** | Color gradient from green (low risk) at bottom to red (high risk) at top. Each level shows a one-line example. Arrow on the side labeled "Increasing Risk / Increasing Scrutiny." |
| **Style** | Clean, stacked blocks. Could be horizontal or vertical. |
| **Insert after** | "Use the principle of least privilege -- give the tool only the access it needs for the specific task." (README ~line 63) |

---

### 3. Decision Tree: Can I Use This Data With This Tool?

| Field | Detail |
|-------|--------|
| **Filename** | `decision-tree-data-tool.png` |
| **README section** | "Questions to Ask Before Using Any AI Tool" |
| **What to show** | A flowchart decision tree: |
| | **Start:** "What data are you working with?" |
| | → Branch: Public/Sample → "Any tool is fine" |
| | → Branch: Internal → "Is the tool approved by IT?" → Yes → "Proceed with logging" / No → "Get approval first" |
| | → Branch: Confidential → "Does the tool process locally?" → Yes → "Proceed with controls" / No → "Mask data first, then reassess" |
| | → Branch: Restricted (PII) → "Is processing fully local?" → Yes → "Proceed with full controls" / No → "Do not use" |
| **Key visual elements** | Diamond shapes for decisions, rounded boxes for outcomes. Green outcomes = proceed, yellow = proceed with conditions, red = stop. |
| **Style** | Standard flowchart. Flows top to bottom or left to right. |
| **Insert after** | The "Questions to Ask" section (README ~line 77), or at the top of `local-vs-cloud-checklist.md` |

---

### 4. Data Sensitivity Classification Grid

| Field | Detail |
|-------|--------|
| **Filename** | `data-sensitivity-grid.png` |
| **README section** | Maps to the Decision Matrix in `local-vs-cloud-checklist.md` |
| **What to show** | A 2D grid/matrix visualization of the existing decision matrix table: |
| | **X-axis:** Tool type (Local, Cloud No Retention, Cloud With Retention) |
| | **Y-axis:** Data sensitivity (Public, Internal, Confidential, Restricted) |
| | **Cells:** Color-coded — Green (OK), Yellow (Requires approval), Orange (Requires approval + masking), Red (Do not use) |
| **Key visual elements** | Traffic-light color scheme. Each cell has the action text from the existing table. Clear axis labels. |
| **Style** | Grid with colored cells. Simple and scannable. |
| **Insert after** | The Decision Matrix table in `local-vs-cloud-checklist.md` (~line 74) as a visual complement |

---

### 5. Accountant's Internal Controls → AI Controls Analogy

| Field | Detail |
|-------|--------|
| **Filename** | `controls-analogy.png` |
| **README section** | "This Is Your Strength" |
| **What to show** | A two-column comparison diagram: |
| | **Left column: Traditional Controls** — System access controls, Segregation of duties, Data classification, Audit trail |
| | **Right column: AI Controls** — Permission settings (read/write/execute), Hooks that block sensitive data, Data sensitivity assessment, Git version history + logging |
| | **Connecting arrows** between each pair showing the direct mapping |
| **Key visual elements** | Two parallel columns with connecting lines or arrows. Header on left: "Controls You Already Know." Header on right: "The Same Controls, Applied to AI." |
| **Style** | Clean two-column layout. Could use icons (lock, folder, clipboard) if available, but text-only is fine. |
| **Insert after** | "You already think this way. You just need to apply it to a new set of tools." (README ~line 113) |

---

## Diagram Guidelines

- **Tool:** PowerPoint, draw.io (free), Excalidraw, or any diagramming tool. Export as PNG.
- **Resolution:** At least 1200px wide for readability on GitHub.
- **Colors:** Use a consistent palette. Suggestion: green (#4CAF50) for safe/local, yellow (#FFC107) for caution, red (#F44336) for restricted. Blue (#2196F3) for neutral/informational.
- **Text:** Large enough to read without zooming. Minimum 14pt equivalent.
- **Branding:** Include "PythonMuse" in small text at bottom-right corner of each diagram (optional).
- **Format:** PNG. Filenames exactly as listed above (lowercase, hyphens, no spaces).
- **Source files:** If using draw.io or similar, save the editable source file (`.drawio`, `.pptx`) alongside the PNG so diagrams can be updated later. These will also be gitignored.

---

## Implementation Plan

Once diagrams are saved to this `diagrams/` folder:

| Step | Task | Files modified | Est. tokens |
|------|------|---------------|-------------|
| 1 | Insert image references into README.md (diagrams 1, 2, 3, 5) | `05-ai-permissions/README.md` | 4 edits, ~2,000 tokens |
| 2 | Insert image references into local-vs-cloud-checklist.md (diagram 4) | `05-ai-permissions/examples/local-vs-cloud-checklist.md` | 1 edit, ~500 tokens |
| 3 | Verify all images render in Markdown preview | Manual check | 5 minutes |
| 4 | Verify .gitignore excludes diagram images | Check `.gitignore` | Already done |
| **Total** | | **2 files, 5 edits** | **~2,500 tokens** |

### Priority Order

If time is limited, create diagrams in this order (highest impact first):

1. **Decision Tree** (#3) — most actionable, answers "what should I do?"
2. **Data Flow** (#1) — core concept of the entire module
3. **Sensitivity Grid** (#4) — visual version of the most-referenced table
4. **Permission Pyramid** (#2) — helpful but the table already communicates this well
5. **Controls Analogy** (#5) — nice-to-have, reinforces the PythonMuse message

---

## .gitignore

Diagram image files and editable source files are excluded from version control via the project `.gitignore` (patterns: `**/diagrams/*.png`, `**/diagrams/*.drawio`, etc.). This plan file (`plan.md`) is tracked so the diagram list is visible to collaborators.

---

*Part of the [PythonMuse AI Accounting Framework](https://github.com/PythonMuse/pythonmuse-ai-accounting-framework)*
