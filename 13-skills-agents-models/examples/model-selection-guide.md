# Model Selection Guide

*A practical decision matrix for choosing the right AI model for your accounting task.*

---

## Quick Decision Tree

```
Is the data sensitive (PII, payroll, client data)?
    YES --> Use local processing or a secure/private model
    NO  --> Continue below

Is the task complex (analysis, interpretation, judgment)?
    YES --> Use a reasoning model (e.g., Claude Opus, GPT-4)
    NO  --> Continue below

Is the task simple (formatting, cleaning, summarizing)?
    YES --> Use a fast model (e.g., Claude Haiku, GPT-3.5)
    NO  --> Use a balanced model (e.g., Claude Sonnet, GPT-4o)
```

---

## Decision Matrix

| Factor | Fast Model | Balanced Model | Reasoning Model | Local/Secure |
|--------|-----------|----------------|-----------------|-------------|
| **Data sensitivity** | Non-sensitive only | Non-sensitive to internal | Internal with controls | Sensitive and restricted |
| **Task complexity** | Simple, mechanical | Moderate analysis | Complex, multi-step | Varies |
| **Speed** | Very fast | Fast | Slower | Varies |
| **Cost per task** | Lowest | Medium | Highest | Infrastructure cost |
| **Output quality** | Good for simple tasks | Good for most tasks | Best for complex tasks | Depends on model |

---

## Mapping Common Accounting Tasks

### Fast Model Tasks
Low complexity, non-sensitive, high volume.

| Task | Why Fast Model Works |
|------|---------------------|
| Cleaning CSV column names | Mechanical text transformation |
| Formatting a Markdown report | Structural, not analytical |
| Summarizing meeting notes | Simple text processing |
| Converting dates between formats | Pattern-based transformation |
| Generating boilerplate text | Template-based output |

### Balanced Model Tasks
Moderate complexity, general analysis.

| Task | Why Balanced Model Works |
|------|-------------------------|
| Bank reconciliation matching logic | Requires rules but well-defined |
| Budget vs actuals variance analysis | Calculation plus classification |
| Generating Python scripts for data analysis | Code generation with accounting context |
| Drafting variance commentary | Requires understanding of financial context |
| Creating workpaper documentation | Structured output with professional judgment |

### Reasoning Model Tasks
High complexity, requires interpretation or judgment.

| Task | Why Reasoning Model Works |
|------|--------------------------|
| Analyzing complex lease agreements | Multi-factor interpretation of contract terms |
| Evaluating accounting treatment options | Requires knowledge of standards and judgment |
| Designing a new workflow from scratch | Creative problem-solving with constraints |
| Investigating unusual transactions | Pattern recognition and anomaly analysis |
| Reviewing and critiquing existing analysis | Meta-analysis requiring deep understanding |

### Local/Secure Model Tasks
Sensitive data that should not leave your machine.

| Task | Why Local Processing |
|------|---------------------|
| Processing payroll data | Contains SSNs, bank accounts |
| Analyzing employee compensation | Personal financial information |
| Working with client tax returns | Privileged client data |
| Processing HIPAA-covered data | Regulatory requirements |
| Pre-audit analysis of sensitive accounts | Confidential pending findings |

---

## Cost Awareness

AI processing is not free. Each interaction uses tokens (units of text), and more tokens = more cost.

**Ways to reduce cost without reducing quality:**
- Use fast models for simple tasks (do not use a reasoning model to clean CSV headers)
- Provide clean, focused input (fewer tokens in = fewer tokens out)
- Use CSV instead of Excel (smaller, cleaner data)
- Break complex tasks into steps (use different model tiers for different steps)
- Cache results (do not re-analyze data that has not changed)

---

## Key Takeaway

The right model is the one that matches the task. Using the most powerful model for every task is like using a senior partner to file invoices -- technically capable but wasteful. Match the model to the complexity, sensitivity, and speed requirements of each specific task.

---

*Back to [Skills, Agents, and Models](../)*
