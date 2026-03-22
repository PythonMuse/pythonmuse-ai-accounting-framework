# Contributing to the PythonMuse AI Accounting Framework

Thank you for your interest in contributing. This framework is built by and for accounting professionals, and every contribution makes it more useful for the community.

---

## Who Can Contribute

You do not need to be a developer. The most valuable contributions often come from accountants who understand the real workflows.

**We welcome:**

- **Use cases** -- Real examples of how AI can help with accounting tasks
- **Templates** -- Markdown templates, checklists, and project structures
- **Code examples** -- Python scripts for common accounting operations
- **Corrections** -- Typos, inaccuracies, or outdated information
- **Reviews** -- Feedback on whether examples are accurate and practical
- **Ideas** -- Suggestions for new sections, topics, or examples

---

## How to Contribute

### Step 1: Fork This Repository

Click the "Fork" button at the top right of this page to create your own copy.

### Step 2: Create a Branch

```bash
git checkout -b your-branch-name
```

Use a descriptive branch name. Examples:

- `add-ar-aging-example`
- `fix-typo-section-03`
- `add-month-end-template`

### Step 3: Make Your Changes

Follow the content guidelines below. Place your files in the correct section folder.

### Step 4: Commit Your Changes

```bash
git add .
git commit -m "Add AR aging bucket example to section 03"
```

Write clear commit messages that describe what you changed and why.

### Step 5: Push and Open a Pull Request

```bash
git push origin your-branch-name
```

Then open a Pull Request on GitHub. In your PR description, include:

- **What** you added or changed
- **Why** it is useful for accountants
- **Which section** it belongs to

### Step 6: Add Yourself to CONTRIBUTORS.md

Add your name to the [CONTRIBUTORS.md](CONTRIBUTORS.md) file as part of your PR. See the format in that file.

---

## Content Guidelines

### Writing Style

- **Practical over theoretical.** Show real accounting scenarios.
- **Clear over clever.** Write for someone who has never used Python or an AI tool.
- **Concise.** Respect the reader's time. Get to the point.
- **Accounting-first.** Frame everything in terms of accounting workflows, not developer workflows. Use terms like "reconciliation," "variance analysis," and "audit trail" -- not "deployment" or "CI/CD."

### Code Examples

- **Include comments** that explain what each section does
- **Use sample data** that looks like real accounting data (but is synthetic)
- **Never include real financial data**, API keys, passwords, or sensitive information
- **Keep examples self-contained** -- a reader should be able to run the script without external dependencies beyond what is listed
- **List required libraries** at the top of each script or in the section README

### Templates

- Use Markdown format
- Include placeholder text that shows how to fill it in
- Add a brief explanation of when and why to use the template

### Folder Structure

Each section follows this pattern:

```
XX-section-name/
├── README.md           Main explanation and walkthrough
├── examples/           Practical examples (scripts, prompts, guides)
├── templates/          Reusable templates
└── data/               Sample data files (if applicable)
```

Place your contributions in the correct subfolder. If you are unsure where something belongs, mention it in your PR and we will help.

---

## What Makes a Good Contribution

### Good Examples

- A Python script that reads a CSV of journal entries and flags entries over a threshold
- A Markdown template for documenting a reconciliation workflow
- A prompt progression showing how to refine AI instructions for variance analysis
- A .gitignore template specifically for finance projects

### Less Helpful

- Generic AI tutorials not tied to accounting
- Overly complex code that requires advanced developer knowledge
- Content that duplicates what already exists in the repository

---

## Review Process

1. A maintainer will review your PR within a few days
2. We may suggest changes to align with the content guidelines
3. Once approved, your contribution will be merged and you will be credited in CONTRIBUTORS.md

---

## Questions?

If you are not sure whether your idea fits, open a GitHub Issue and describe what you have in mind. We would rather hear your idea than have you spend time on something that does not align.

---

## Code of Conduct

All contributors are expected to follow our [Code of Conduct](CODE_OF_CONDUCT.md). We are building a professional, supportive community for accounting professionals learning AI.

---

*Thank you for helping build the future of AI in accounting.*
