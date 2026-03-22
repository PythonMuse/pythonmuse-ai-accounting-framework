# Git for Accountants -- Version Control as Your Audit Trail

*Git is not just for developers. It is the most powerful audit trail tool you have never used.*

---

## You Already Think in Versions

Every accountant has done this:

```
report_draft.xlsx
report_draft_v2.xlsx
report_final.xlsx
report_final_v2.xlsx
report_FINAL_ACTUAL.xlsx
report_FINAL_ACTUAL_revised.xlsx
```

This is version control. It is just bad version control.

Git does the same thing, but properly: every version is tracked, every change is documented, and you can go back to any point in history without keeping fifteen copies of the same file.

---

## The Accounting Analogy

Git concepts map directly to accounting concepts:

| Git | Accounting | What It Does |
|-----|-----------|-------------|
| **Commit** | Journal entry | Records a specific change with a description of what was done |
| **History (log)** | Audit trail | Chronological record of every change ever made |
| **Branch** | Scenario / what-if analysis | Work on an alternative version without affecting the main copy |
| **Pull request** | Review and approval | Someone else reviews your changes before they are accepted |
| **Revert** | Correcting / adjusting entry | Undo a specific change while preserving the record that it happened |
| **Repository** | Workpaper binder | The complete collection of files and their full history |

---

## How This Supports COSO Principles

The COSO framework for internal controls maps naturally to Git:

- **Change tracking:** Every commit records what changed, when, and who made the change
- **Control:** Branches and pull requests enforce review before changes are accepted
- **Accountability:** Every action is attributed to a specific person
- **Documentation:** Commit messages explain why changes were made
- **Reversibility:** Any change can be undone without losing the record

---

## The Only Three Commands You Need to Start

You do not need to learn Git comprehensively. Start with three commands.

### 1. Stage your changes
```bash
git add .
```
This tells Git: "These are the files I want to save."

### 2. Commit (save a checkpoint)
```bash
git commit -m "Complete March bank reconciliation"
```
This creates a permanent record of the current state of your project with a description.

### 3. Push to remote
```bash
git push
```
This sends your saved checkpoints to GitHub (or Azure DevOps), creating an off-site backup and making your work available to your team.

---

## GitHub vs Azure DevOps

| Feature | GitHub | Azure DevOps |
|---------|--------|-------------|
| Best for | Learning, open collaboration, personal projects | Enterprise control, IT alignment, security governance |
| Ease of use | Very easy to get started | More complex, more features |
| Cost | Free for public repos; reasonable for private | Free tier available; enterprise licensing |
| Integration | Excellent with AI tools, open source | Excellent with Microsoft ecosystem |
| Security | Strong; fine-grained permissions | Enterprise-grade; AD integration |

**Start with GitHub.** It is simpler to learn and has better integration with AI tools. When your organization needs enterprise controls, Azure DevOps is there.

---

## Examples

| File | What It Covers |
|------|---------------|
| [git-accounting-analogy.md](examples/git-accounting-analogy.md) | Full side-by-side comparison of Git and accounting concepts |
| [gitignore-finance.md](examples/gitignore-finance.md) | Complete .gitignore guide for finance projects |
| [first-repo-walkthrough.md](examples/first-repo-walkthrough.md) | Step-by-step guide to creating your first repository |

## Templates

| File | What It Is |
|------|-----------|
| [.gitignore-template](templates/.gitignore-template) | Ready-to-use .gitignore for accounting AI projects |
| [pr-review-checklist.md](templates/pr-review-checklist.md) | Pull request review checklist for accounting teams |

---

## Key Takeaway

You do not need to become a Git expert. You need to understand three things:

1. **Git tracks changes.** Every save (commit) is recorded permanently.
2. **Git is your audit trail.** You can see who changed what, when, and why.
3. **Git protects your work.** You can always go back to a previous version.

The accountants who adopt Git early will have better documentation, better collaboration, and better control over their AI workflows than those who rely on file naming conventions.

---

*Next: [SQL Access](../12-sql-access/) -- working with IT for direct database access.*
