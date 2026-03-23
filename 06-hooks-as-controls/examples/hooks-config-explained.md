# Hooks Configuration Explained

*A line-by-line explanation of the sample hooks configuration.*

> **This looks more technical than it is.** If the configuration below seems intimidating, take a breath. You do not need to write any of this from scratch. You describe the control you want — "block the AI from writing files with Social Security numbers" — and Claude builds the hook for you. What looks like a page of configuration is really a 15-20 minute conversation with your AI assistant. Your job is to know *what* control you need. The AI handles the *how*.

---

## Overview

The `sample-hooks-config.json` file shows how to configure automated checks (hooks) that run before and after AI tool actions. This is how you embed internal controls into your AI workflow.

---

## Hook 1: Block Writes Containing SSN Patterns

**Type:** PreToolUse (runs before the action)

**Trigger:** Activates whenever the AI tries to Edit or Write a file

**What it does:** Scans the content for patterns that look like Social Security numbers:
- `XXX-XX-XXXX` format (e.g., 123-45-6789)
- Nine consecutive digits (e.g., 123456789)

**If found:** The action is blocked (exit code 1). The AI cannot write the file.

**If not found:** The action proceeds (exit code 0).

**Accounting parallel:** This is like a system control that rejects a payment if the payee information is incomplete or malformed. It prevents data exposure before it happens.

> **PythonMuse Tip:** To create this hook, you would simply tell Claude: "I need a hook that blocks any file write if the content contains a Social Security number pattern." Claude writes the configuration. You review it, test it with sample data, and you are done. That is the whole process.

---

## Hook 2: Warn Before Modifying Raw Data

**Type:** PreToolUse (runs before the action)

**Trigger:** Activates whenever the AI tries to Edit or Write a file

**What it does:** Checks if the target file path includes `data/raw/`. If it does, the action is blocked.

**Why this matters:** In accounting data workflows, raw data is your source of truth. It should never be modified. This hook enforces that rule automatically.

**Accounting parallel:** This is like marking a workpaper as "original -- do not modify" and locking it from edits. The processed and output folders are where transformed data belongs.

> **PythonMuse Tip:** This is one of the most valuable hooks you can set up, and it takes about two minutes. Tell Claude: "Add a hook that blocks any writes to files in data/raw/." That one sentence protects your source data from accidental modification — permanently.

---

## Hook 3: Log Reminder After File Writes

**Type:** PostToolUse (runs after the action completes)

**Trigger:** Activates after the AI successfully writes a file

**What it does:** Prints a reminder message: "File written: check outputs for accuracy."

**Why this matters:** Even after the AI produces output, you should verify it. This hook serves as an automated reminder -- a nudge to apply your review process.

**Accounting parallel:** This is like an automated workflow that flags newly posted journal entries for review.

---

## How to Use This Configuration

> **You do not need to memorize any of this.** The steps below are here for reference, but in practice you would ask Claude to set up the hooks for you. Walk through the conversation: "I want three controls — block SSN patterns, protect my raw data folder, and remind me to review every output." Claude will generate the configuration, place it in the right directory, and test it. The whole setup takes less than 20 minutes.

1. Copy `sample-hooks-config.json` to your project's `.claude/` directory (or wherever your AI tool reads hook configurations)
2. Adjust the patterns and paths to match your specific project
3. Test each hook with sample data before relying on it with real workflows
4. Document your hooks in your project's plan.md or a dedicated controls document

---

## Customization Ideas

Every one of these is a single prompt to Claude. Describe the control; the AI builds it.

- Add a hook that checks for email addresses in output files
- Add a hook that enforces file naming conventions (e.g., outputs must include a date)
- Add a hook that blocks execution of certain terminal commands
- Add a hook that logs every file the AI creates to a `changes.log` file

---

*Back to [Hooks as Controls](../)*
