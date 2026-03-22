# Screenshot Plan: VS Code as Your Workspace

*Shot list and implementation plan for adding visual guides to Module 04.*

**Assigned to:** Patrick
**Status:** Not started
**Created:** 2026-03-22

---

## Purpose

The README for this module describes the VS Code layout, setup steps, and key concepts in text. Screenshots will make these descriptions concrete -- especially for readers who have never opened VS Code before. Each screenshot maps directly to a section in the README.

---

## Shot List

### 1. VS Code Layout Overview

| Field | Detail |
|-------|--------|
| **Filename** | `vscode-layout-overview.png` |
| **README section** | "The VS Code Layout" |
| **What to capture** | Full VS Code window with a project folder open. All four areas should be visible: sidebar (file explorer open), editor (a Markdown or Python file open), terminal (at the bottom, can be empty), and the left activity bar (icons for explorer, search, git, extensions). |
| **Suggested annotations** | Label the four areas: "Sidebar," "Editor," "Terminal," "Extensions Bar." Use simple arrows or numbered callouts. |
| **Image reference** | `![VS Code layout with sidebar, editor, terminal, and extensions bar labeled](screenshots/vscode-layout-overview.png)` |
| **Insert after line** | "**Extensions (left bar icons):** Add-ons that extend VS Code's capabilities." (README ~line 31) |

---

### 2. Open Folder Dialog

| Field | Detail |
|-------|--------|
| **Filename** | `open-folder.png` |
| **README section** | "Step 2: Open a Project Folder" |
| **What to capture** | File > Open Folder menu selected, or the "Open Folder" dialog box with a project folder (e.g., `bank-recon-march/`) highlighted. |
| **Suggested annotations** | None needed -- the dialog is self-explanatory. |
| **Image reference** | `![File > Open Folder dialog in VS Code](screenshots/open-folder.png)` |
| **Insert after line** | "This is important: VS Code works with folders, not individual files." (README ~line 45) |

---

### 3. Sidebar Project Structure

| Field | Detail |
|-------|--------|
| **Filename** | `sidebar-project-structure.png` |
| **README section** | "Files and Folders = Your Organizational Structure" |
| **What to capture** | Sidebar showing a project folder expanded with the standard structure: `CLAUDE.md`, `plan.md`, `status_update.md`, `data/raw/`, `data/processed/`, `outputs/`, `src/`. Use a framework example project if available. |
| **Suggested annotations** | Optional: label `data/raw/` as "Source files (read-only)" and `outputs/` as "Results go here." |
| **Image reference** | `![Project folder structure in the VS Code sidebar](screenshots/sidebar-project-structure.png)` |
| **Insert after line** | "You can create, rename, move, and delete files directly in the sidebar." (README ~line 112) |

---

### 4. Terminal Running a Script

| Field | Detail |
|-------|--------|
| **Filename** | `terminal-run-script.png` |
| **README section** | "Step 6: Run a Script" |
| **What to capture** | Terminal panel at the bottom of VS Code showing `python examples/read_csv_basics.py` being run, with output visible (totals, row counts from the sample bank transactions CSV). The editor above can show the script source. |
| **Suggested annotations** | Optional: arrow pointing to the terminal prompt with "Type your command here." |
| **Image reference** | `![Running a Python script in the VS Code terminal](screenshots/terminal-run-script.png)` |
| **Insert after line** | "Or type `python your_script.py` in the terminal." (README ~line 61) |

---

### 5. Extensions Panel

| Field | Detail |
|-------|--------|
| **Filename** | `extensions-panel.png` |
| **README section** | "Step 5: Install Python Extension" |
| **What to capture** | Extensions sidebar open with "Python" searched and the Microsoft Python extension visible (installed or ready to install). Bonus: also show GitHub Copilot and Markdown Preview Enhanced if they are installed. |
| **Suggested annotations** | None needed. |
| **Image reference** | `![Extensions panel showing the Python extension](screenshots/extensions-panel.png)` |
| **Insert after line** | "This enables Python support, syntax highlighting, and the ability to run scripts directly." (README ~line 57) |

---

### 6. Markdown Preview Split View

| Field | Detail |
|-------|--------|
| **Filename** | `markdown-preview-split.png` |
| **README section** | "Tips for Getting Comfortable" -- item 2 |
| **What to capture** | Split view: Markdown source on the left, formatted preview on the right. Use a file like `plan.md` or `status_update.md` from the framework so the content looks relevant to accountants. |
| **Suggested annotations** | Optional: label left panel "Source (what you type)" and right panel "Preview (what others see)." |
| **Image reference** | `![Markdown source and preview side by side](screenshots/markdown-preview-split.png)` |
| **Insert after line** | "You can see the formatted version side by side with the source." (README ~line 120) |

---

### 7. GitHub Copilot Chat with Claude Model

| Field | Detail |
|-------|--------|
| **Filename** | `copilot-chat-claude.png` |
| **README section** | recommended-extensions.md -- PythonMuse note under "AI Extensions" |
| **What to capture** | GitHub Copilot Chat panel open in VS Code, with the model selector showing Claude selected (or the model dropdown visible). If possible, show a brief exchange related to accounting (e.g., asking about a reconciliation). |
| **Suggested annotations** | Arrow or circle around the model selector showing "Claude" is chosen. |
| **Image reference** | `![GitHub Copilot Chat with Claude model selected](screenshots/copilot-chat-claude.png)` |
| **Insert in** | `recommended-extensions.md` after the PythonMuse note (~line 41) |

---

## Capture Guidelines

- **Resolution:** Use your normal screen resolution. Crop to the VS Code window only -- no desktop or taskbar visible.
- **Theme:** Use the default VS Code theme (Dark+ or Light+). Either is fine, just be consistent across all 7 screenshots.
- **Sensitive data:** Do not capture any real company data, file paths with personal info, or credentials. Use framework sample files or generic project names.
- **File format:** PNG. Keep filenames exactly as listed above (lowercase, hyphens, no spaces).
- **Annotations:** If adding labels or arrows, use a simple tool (Snagit, PowerPoint, or even Paint). Keep annotations clean -- solid arrows, readable font, no clutter.

---

## Implementation Plan (for whoever inserts the images into the articles)

Once screenshots are saved to this `screenshots/` folder:

| Step | Task | Files modified | Est. effort |
|------|------|---------------|-------------|
| 1 | Insert image references into README.md (shots 1-6) | `04-vscode-as-workspace/README.md` | 6 edits, ~3,000 tokens |
| 2 | Insert image reference into recommended-extensions.md (shot 7) | `04-vscode-as-workspace/examples/recommended-extensions.md` | 1 edit, ~500 tokens |
| 3 | Verify all images render in Markdown preview | Manual check | 5 minutes |
| 4 | Verify .gitignore excludes screenshot PNGs | Check `.gitignore` | Already done |
| **Total** | | **2 files, 7 edits** | **~3,500 tokens** |

The image insertion is a quick session -- all the reference text and insert locations are documented above. Ask the AI to read this plan and execute steps 1-2.

---

## .gitignore

Screenshot image files are excluded from version control via the project `.gitignore` (pattern: `**/screenshots/*.png`). This plan file (`plan.md`) is tracked so the shot list is visible to collaborators.

---

*Part of the [PythonMuse AI Accounting Framework](https://github.com/PythonMuse/pythonmuse-ai-accounting-framework)*
