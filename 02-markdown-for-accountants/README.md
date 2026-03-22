# Markdown for Accountants

*The simplest documentation tool you will ever use -- and the one AI understands best.*

---

## Why Markdown Matters

If there is one tool change that pays for itself immediately when working with AI, it is Markdown.

Markdown is a lightweight way to write structured text using plain characters. No special software required. No formatting menus. No compatibility issues. Just text that is organized, readable, and -- crucially -- understood perfectly by AI tools.

Here is what Markdown gives you:

- **Structure.** Headers, lists, tables, and sections that organize your thoughts
- **Repeatability.** The same file reads the same way everywhere -- VS Code, GitHub, email, AI tools
- **Clarity.** No hidden formatting. What you see is what there is
- **Version control.** Plain text works perfectly with Git (your audit trail)

Markdown replaces scattered notes, undocumented Word files, and email chains with organized, searchable, version-controlled logic.

---

## My Recommendation

Move as much as you can to Markdown. It is the best documented way to interact with AI.

If you work with many PDFs, one of the first useful skills you should build is converting a specific PDF report to Markdown. That PDF becomes interactive with AI -- and more importantly, you may not need to convert all of it. Often you only need specific sections, which saves tokens and produces better results.

---

## When to Use Markdown

| Use Case | Why Markdown Works |
|----------|-------------------|
| Project plans and notes | Structured, easy to update, AI-readable |
| Checklists | Checkbox syntax built in |
| Workpapers | Consistent format, version controlled |
| AI instructions (CLAUDE.md) | AI reads Markdown natively |
| Process documentation | Searchable plain text |
| Meeting notes | Quick to write, easy to share |
| Status updates | Structured format, consistent layout |

---

## Markdown vs Word: A Comparison

**Word document for a process memo:**
- Requires Microsoft Word or compatible software
- Formatting can break when shared
- Cannot be tracked meaningfully in version control
- AI tools need to parse complex file formats
- Hidden formatting can cause unexpected behavior

**Markdown file for a process memo:**
- Opens in any text editor
- Looks the same everywhere
- Perfect for version control (every change is tracked)
- AI tools read it natively with zero overhead
- What you see is exactly what is in the file

---

## Basic Syntax (With Accounting Examples)

### Headers

```markdown
# Month-End Close Process
## Pre-Close Tasks
### Bank Reconciliation
```

### Bold and Italic

```markdown
**Material variance** requires investigation.
*Immaterial* items can be grouped.
```

### Lists

```markdown
- Review bank reconciliation
- Post accrual entries
- Reconcile intercompany balances

1. Export trial balance
2. Run variance analysis
3. Prepare financial statements
```

### Tables

```markdown
| Account | Description    | Debit      | Credit     |
|---------|----------------|------------|------------|
| 1010    | Cash - Operating | $125,430 |            |
| 2010    | Accounts Payable |          | $42,300    |
| 3010    | Retained Earnings |         | $83,130    |
```

### Checkboxes

```markdown
- [x] Bank reconciliation completed
- [x] Accruals posted
- [ ] Intercompany reconciliation
- [ ] Financial statements drafted
```

### Code Blocks

```markdown
The formula for the variance percentage:

    variance_pct = (actual - budget) / budget * 100
```

### Blockquotes (Great for Policy References)

```markdown
> Per ASC 842, lessees must recognize a right-of-use asset
> and a lease liability for all leases with terms greater
> than 12 months.
```

---

## Try This

1. Open VS Code (or any text editor)
2. Create a new file called `close-notes.md`
3. Write a simple month-end close checklist using the syntax above
4. Preview it (in VS Code: Ctrl+Shift+V)

You will have a clean, structured document in under five minutes.

---

## Key Takeaway

Markdown is not a developer tool. It is a documentation tool that happens to be the native language of AI interactions. The sooner you adopt it, the better your AI workflows will be -- and the easier it will be to maintain, share, and audit your work.

---

*Next: [Python Without Intimidation](../03-python-without-intimidation/) -- reading code is easier than you think.*
