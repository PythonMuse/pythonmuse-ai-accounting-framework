# AI Permissions -- Understanding What AI Can Access

*You must understand what is happening and where your data goes. This is where accountants naturally excel (no pun intended).*

---

## Why This Matters

When you use an AI tool, you are not just typing into a chat box. Depending on the tool and how it is configured, the AI may:

- **Read files** on your computer
- **Execute code** (run Python scripts, terminal commands)
- **Send data** to a cloud server for processing
- **Store data** on external servers temporarily or permanently

As accountants, we already think about data access controls every day. We already ask: who has access to what? Where does information go? Is there an audit trail?

AI tools require the exact same scrutiny.

---

## Local vs Cloud: Where Does Your Data Go?

Think of it this way:

- **Local processing** = working at your desk. The data stays on your machine. Nothing leaves the building.
- **Cloud processing** = sending a copy of the document out of the building for someone else to process and return.

Both have valid use cases. But you need to know which one is happening.

### When Data Stays Local

- Running a Python script on your machine
- Using AI tools in fully offline mode
- Processing files with local-only libraries (pandas, openpyxl)

### When Data Leaves Your Machine

- Chat-based AI tools (Claude web, ChatGPT, Copilot Chat) typically send your prompts to cloud servers
- AI extensions in VS Code may send file contents as context for processing
- Any tool that requires an internet connection to function is likely processing data externally

### The Gray Area

Some tools operate in a hybrid mode. For example, Claude Code runs on your local machine but sends prompts to cloud APIs for processing. The code execution happens locally, but the reasoning happens in the cloud.

Understanding this distinction is critical for deciding which data you can use with which tools.

---

## Permission Models: What Can AI Do?

Different AI tools have different permission levels. Before using any tool, understand what it can:

| Permission | Question to Ask | Risk Level |
|-----------|----------------|------------|
| **Read** | Can it see my files? Which folders? | Medium |
| **Write** | Can it create or modify files? | High |
| **Execute** | Can it run scripts or terminal commands? | High |
| **Network** | Does it send data to external servers? | High |
| **Store** | Does the provider retain my data? For how long? | High |

Most AI tools allow you to configure these permissions. Use the principle of least privilege -- give the tool only the access it needs for the specific task.

### What a Permission Actually Looks Like

Permissions in most harnesses are a short configuration block you can read:

```yaml
permissions:
  allowed_folders:
    - data/raw
    - data/processed
    - outputs
```

Compare it with:

```yaml
permissions:
  allowed_folders:
    - /
```

The second grants the entire drive. Nothing errors. Nothing warns. This is the most common over-grant in practice, and reviewing for it takes about four seconds.

See [Module 16](../16-configuration-literacy/) for reading these files generally.

### The Three-Tier Folder Model

| Tier | Folders | Rule |
|---|---|---|
| Write / create / modify | `outputs/`, `data/processed/` | Allowed |
| Read-only | `data/raw/` | Never write -- source of truth |
| Forbidden | Everything else | No access |

### A Documented Placeholder Pattern

The module above names masking but does not yet show it. Here is the pattern:

| Field | Placeholder |
|---|---|
| Dollar amounts | `[AMT_1]` |
| Headcount | `[HC_1]` |
| Percentages | `[PCT_1]` |
| Employee names | `[EMP_1]` |
| Client / vendor names | `[CLIENT_1]` |
| Tax IDs, SSNs | `[ID_1]` |
| Bank / account numbers | `[ACCT_1]` |

Safe to leave unmasked: column headers, field names, dates and periods, GL account codes, and structural logic. The structure is usually what you need help with; the values are what you need to protect.

---

## Questions to Ask Before Using Any AI Tool

Before you use any AI tool with accounting data, work through these questions:

1. **Where does the processing happen?** Local, cloud, or hybrid?
2. **What data does the tool access?** Only what I paste, or does it read my project files?
3. **Is data sent to external servers?** If yes, where? What jurisdiction?
4. **Is there a data retention policy?** Does the provider store my prompts or data? Can I opt out?
5. **What permissions does the tool have?** Can it read, write, execute, or access the network?
6. **Is the tool compliant with my organization's policies?** Has IT reviewed and approved it?
7. **Am I using real or synthetic data?** For experimentation, always use synthetic data first.

---

## Practical Guidelines

### For Learning and Experimentation

- Use synthetic or sample data
- Cloud-based tools are fine for non-sensitive tasks
- Focus on learning the tool's capabilities before using real data

### For Internal Analysis (Non-Sensitive)

- Use organizational-approved AI tools
- Verify data retention policies
- Keep a log of what data was processed and where

### For Sensitive Financial Data

- Prefer local processing tools
- Never paste PII, SSNs, bank account numbers, or client data into cloud-based AI
- If cloud processing is required, ensure data masking first
- Document what data was used, where it was processed, and what controls were in place

---

## This Is Your Strength

If you are an accountant reading this and thinking "this sounds like internal controls for data access," you are exactly right. The same framework you use for:

- System access controls
- Segregation of duties
- Data classification policies
- Audit trail requirements

...applies directly to AI tool governance. You already think this way. You just need to apply it to a new set of tools.

---

*Next: [Hooks as Controls](../06-hooks-as-controls/) -- embedding internal controls into your AI workflows.*
