# Hook Example: Require Human Approval Before Writing

*A maker-checker control that pauses AI execution for human review.*

---

## Scenario

The AI has just generated a variance analysis summary and is about to write the results to `outputs/variance_report.csv`. Before the file is created, you want to review the output and confirm it is accurate.

---

## The Accounting Parallel

This is the maker-checker principle:

- **Maker:** The AI generates the report (preparer role)
- **Checker:** You review and approve before it is finalized (reviewer role)

No output should be considered final until a human has reviewed it. This hook enforces that discipline.

---

## How the Hook Works

### Trigger
The hook activates **before** the AI writes any file to the `outputs/` directory.

### What Happens
1. The AI pauses execution
2. A preview of the content is displayed to the user
3. The user sees a prompt: "The AI is about to write the following file. Review and approve?"
4. Options:
   - **Approve:** The file is written as shown
   - **Reject:** The action is cancelled and the AI is notified
   - **Modify:** The user provides feedback and the AI revises before trying again

### Logging
Every approval or rejection is logged with:
- Timestamp
- File name and path
- Action taken (approved / rejected / modified)
- User who reviewed

---

## What the Logic Looks Like

```
BEFORE AI writes a file to outputs/:
  1. Capture the file contents that will be written
  2. DISPLAY to user:
     "AI wants to write: outputs/variance_report.csv"
     [Preview of first 20 rows]
     "Total rows: 45 | Total columns: 8"

  3. PROMPT: "Approve this output? [Yes / No / Revise]"

  IF approved:
    WRITE the file
    LOG: "Output approved by [user] at [timestamp]"

  IF rejected:
    CANCEL the write
    LOG: "Output rejected by [user] at [timestamp]"
    NOTIFY AI: "Output was rejected. Ask the user what needs to change."

  IF revise:
    CAPTURE user feedback
    CANCEL the write
    PASS feedback to AI for revision
```

---

## Practical Benefits

- **No accidental overwrites.** You see exactly what will be written before it happens.
- **Catches errors early.** If the AI produced incorrect calculations, you catch it before the file exists.
- **Creates an audit trail.** Every approval or rejection is documented.
- **Builds trust.** You stay in control of every output.

---

## When to Use This Hook

This hook is most valuable when:

- The output will be shared with others (management reports, audit workpapers)
- The output contains financial figures that need verification
- You are still building confidence in a new AI workflow
- The project involves sensitive or high-stakes data

For routine, well-tested workflows, you may choose to relax this hook to a post-execution log instead of a pre-execution gate.

---

*Back to [Hooks as Controls](../)*
