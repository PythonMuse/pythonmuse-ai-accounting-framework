# Hooks as Controls -- Your Internal Control Layer for AI

*Hooks are how you embed the same approval workflows and checks you already use for journal entries into your AI workflows.*

---

## What Is a Hook?

A hook is a simple check that runs automatically before or after an AI action. It is a gate: if the condition passes, the action proceeds. If it fails, the action is blocked or paused for review.

If you work in accounting, you already use hooks every day. You just call them something else:

| In Accounting | In AI Workflows |
|--------------|-----------------|
| Journal entry approval threshold | Hook that flags outputs over a dollar limit |
| Segregation of duties review | Hook that pauses for human review before writing |
| Data access restrictions | Hook that blocks processing of sensitive data |
| Payment authorization limits | Hook that requires confirmation before execution |

Hooks are the same concept applied to AI: "Before this action runs, check this condition."

---

## Why Hooks Matter

Without hooks, your AI workflow is like a general ledger with no approval controls. Anyone (or anything) can post entries, modify data, and generate outputs without oversight.

Hooks give you:

- **Prevention.** Block risky actions before they happen.
- **Detection.** Log actions for review and audit trail.
- **Documentation.** Every hook trigger creates a record.
- **Compliance.** Directly supports COSO principles of control activities and monitoring.

---

## Types of Hooks

### Pre-Execution Hooks

Run *before* an AI action. Act as gatekeepers.

**Examples:**
- Check if a file contains SSN patterns before allowing AI to process it
- Verify that the AI is not about to modify files in the `data/raw/` folder
- Confirm that data masking has been applied before sending to a cloud tool

### Post-Execution Hooks

Run *after* an AI action completes. Act as validators.

**Examples:**
- Log every file the AI created or modified
- Verify output totals match input totals
- Flag if an output file contains unexpected data patterns

### Approval Hooks

Pause execution and require human confirmation before proceeding.

**Examples:**
- "The AI is about to write 15 journal entries. Review and approve?"
- "This script will modify 3 files. Confirm?"
- "Output contains dollar amounts over your review threshold. Approve for distribution?"

---

## Real Examples

### Example 1: Block Unmasked Sensitive Data

Before the AI processes a payroll file, a hook checks for SSN patterns (XXX-XX-XXXX) and bank account numbers. If found unmasked, the action is blocked.

See: [hook-block-sensitive-data.md](examples/hook-block-sensitive-data.md)

### Example 2: Require Human Approval Before Writing

After the AI generates a financial summary, a hook pauses execution and displays the output for review before writing it to the outputs folder.

See: [hook-require-approval.md](examples/hook-require-approval.md)

### Example 3: Protect Raw Data Folder

A hook that warns or blocks any attempt to modify files in the `data/raw/` directory. Source data should never be changed.

See: [sample-hooks-config.json](examples/sample-hooks-config.json) and [hooks-config-explained.md](examples/hooks-config-explained.md)

---

## Designing Your First Hook

Start with the question every internal control starts with: **What could go wrong?**

1. **Identify the risk.** What is the worst-case scenario? (e.g., AI processes unmasked PII)
2. **Define the trigger.** What action should be checked? (e.g., before processing any file in the payroll folder)
3. **Define the check.** What condition must be met? (e.g., no SSN patterns found in file contents)
4. **Define the response.** What happens if the check fails? (e.g., block the action and log the attempt)
5. **Document it.** Record the hook, its purpose, and how it works.

Use the [Hook Design Worksheet](templates/hook-design-worksheet.md) to plan your hooks.

---

## Connection to SOX and COSO

For organizations subject to SOX or following COSO frameworks, hooks map directly to control activities:

| COSO Principle | Hook Implementation |
|---------------|-------------------|
| Control Activities | Pre-execution checks that enforce policies |
| Information and Communication | Logging and alerting on hook triggers |
| Monitoring Activities | Post-execution validation and review |

Hooks are not a replacement for your existing control framework. They are an extension of it into AI-assisted workflows.

---

## Key Takeaway

You would not let a staff accountant post journal entries without review. You would not let anyone modify source data without documentation. Hooks apply the same discipline to AI.

They are simple, configurable, and -- for accountants -- conceptually familiar. Start with one hook that protects your most sensitive data, and build from there.

---

*Next: [Canary Concept](../07-canary-concept/) -- a simple environment validation for your AI workspace.*
