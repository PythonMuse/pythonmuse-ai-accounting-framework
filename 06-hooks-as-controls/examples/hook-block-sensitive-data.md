# Hook Example: Block Unmasked Sensitive Data

*A preventive control that stops AI from processing files containing unmasked PII.*

---

## Scenario

You are using AI to help analyze payroll data for a 401(k) match validation. The payroll export contains Social Security numbers and bank account numbers. Before the AI processes any file, you want to verify that sensitive data has been masked.

---

## The Risk

If unmasked PII is included in a file that gets sent to a cloud-based AI tool (or even processed in a local log that gets committed to version control), you have a data exposure incident.

---

## How the Hook Works

### Trigger
The hook runs **before** the AI reads or processes any file in the `data/` directory.

### Check
The hook scans the file contents for patterns that match:
- Social Security numbers: `XXX-XX-XXXX` or `XXXXXXXXX` (9 consecutive digits)
- Bank account numbers: sequences of 8-17 digits
- Email addresses in combination with financial data

### If Check Passes (No Sensitive Patterns Found)
The AI action proceeds normally.

### If Check Fails (Sensitive Patterns Detected)
1. The action is **blocked immediately**
2. A warning message is displayed: "Sensitive data pattern detected. Action blocked."
3. The attempt is logged with: timestamp, file name, pattern type detected, action that was attempted
4. The user is instructed to mask the data before retrying

---

## What the Logic Looks Like

```
BEFORE AI processes a file:
  1. Read the file contents
  2. Search for pattern: \d{3}-\d{2}-\d{4}     (SSN with dashes)
  3. Search for pattern: \b\d{9}\b              (SSN without dashes)
  4. Search for pattern: \b\d{8,17}\b           (potential bank account numbers)

  IF any pattern is found:
    BLOCK the action
    LOG: "Sensitive data detected in [filename] - [pattern type]"
    DISPLAY: "Action blocked. Mask sensitive data before processing."

  ELSE:
    ALLOW the action to proceed
```

---

## What Masked Data Looks Like

Before masking:
```
employee_name,ssn,bank_account,match_amount
John Smith,123-45-6789,9876543210,4500.00
Jane Doe,987-65-4321,1234567890,3200.00
```

After masking:
```
employee_name,ssn,bank_account,match_amount
John Smith,***-**-6789,******3210,4500.00
Jane Doe,***-**-4321,******7890,3200.00
```

The hook would pass the masked version and block the unmasked version.

---

## How to Implement This in Claude Code

In your project's `.claude/settings.json`, you can configure hooks that run shell commands before certain actions. For a detailed configuration example, see [sample-hooks-config.json](sample-hooks-config.json) and [hooks-config-explained.md](hooks-config-explained.md).

---

## Key Principle

This hook is a **preventive control** -- the same type you would implement to prevent unauthorized journal entries or payments above a threshold. The only difference is that it is applied to AI actions instead of ERP transactions.

---

*Back to [Hooks as Controls](../)*
