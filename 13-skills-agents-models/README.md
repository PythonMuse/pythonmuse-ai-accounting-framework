# Skills, Agents, and Models -- What Most People Miss

*Reusable logic, AI assistants that follow instructions, and choosing the right model for the job.*

---

## Skills: Reusable Logic

A skill is a set of reusable instructions that you can apply to the same type of task every time. Think of it as a macro -- but for AI workflows.

You already have skills in accounting. You just call them procedures:

- The bank reconciliation procedure
- The month-end close checklist
- The variance analysis process

AI skills work the same way. You define the inputs, the steps, and the expected outputs once. Then you reuse that definition every time you perform that task.

**Why reusability matters:** For the same reason you template your workpapers. Consistency, efficiency, and reduced error.

---

## How to Define a Skill

A skill definition includes:

1. **Name and description** -- What does this skill do?
2. **When to use it** -- Under what conditions?
3. **Input requirements** -- What data and format?
4. **Steps** -- What the AI should do, in order
5. **Output format** -- What the result should look like
6. **Review checklist** -- How to verify the output

See the examples:
- [Bank Reconciliation Skill](examples/skill-bank-recon.md)
- [Variance Analysis Skill](examples/skill-variance-analysis.md)
- [Skill Template](templates/skill-template.md) (blank, ready to copy)

---

## Agents: AI Interns That Follow Instructions

An agent is an AI assistant configured to perform specific tasks within defined boundaries. Think of it as a well-briefed intern:

- You give it clear instructions
- You define what it can and cannot do
- You review its work before accepting it
- You adjust its instructions based on results

### What Agents Can Do

- Process data files according to your rules
- Generate reports in specific formats
- Flag anomalies or exceptions
- Draft documentation based on templates

### What Agents Need

- **Clear instructions.** Vague instructions produce vague results.
- **Defined scope.** What files can it access? What actions can it take?
- **Review process.** Every output is reviewed before use.
- **Feedback loop.** If the output is wrong, refine the instructions.

### The Intern Analogy

You would not give a new intern access to everything on day one. You would:

1. Start with a specific, well-defined task
2. Provide clear written instructions
3. Review their work carefully
4. Expand their responsibilities as they prove reliable

Do the same with AI agents.

---

## Models: Choosing the Right Tool

Not all AI models are the same. Different models have different strengths, and the right choice depends on your task.

### Model Tiers

| Tier | Strengths | Best For | Cost |
|------|-----------|----------|------|
| **Reasoning** (Opus-level) | Deep analysis, complex logic, nuanced judgment | Financial analysis, complex reconciliations, interpretation | Higher |
| **Fast** (Haiku-level) | Speed, simple tasks, high volume | Formatting, summaries, data cleaning, simple queries | Lower |
| **Balanced** (Sonnet-level) | Good all-around performance | Most daily tasks, code generation, general analysis | Medium |

### How to Choose

Ask yourself:

1. **How sensitive is the data?** Sensitive data may require local processing models.
2. **How complex is the task?** Complex analysis benefits from reasoning models. Simple formatting does not.
3. **How fast do I need results?** For batch processing, fast models save time and money.
4. **What is the cost tolerance?** More capable models cost more per token.

### Mapping Tasks to Models

| Task | Recommended Tier | Why |
|------|-----------------|-----|
| Summarizing meeting notes | Fast | Simple text processing |
| Formatting a report | Fast | Structural task, not analytical |
| Bank reconciliation logic | Balanced/Reasoning | Requires matching rules and judgment |
| Complex lease analysis | Reasoning | Requires interpretation of contract terms |
| Variance analysis with commentary | Balanced | Combines calculation with explanation |
| Processing payroll data | Local/Secure | Sensitive data; minimize exposure |
| Data cleaning (column names, dates) | Fast | Mechanical transformation |

See [model-selection-guide.md](examples/model-selection-guide.md) for a detailed decision matrix.

---

## The Controller's Framework for AI Tool Selection

If you are a controller evaluating AI tools for your team, consider these dimensions:

| Dimension | Question | Impact |
|-----------|----------|--------|
| **Data sensitivity** | What data will this tool process? | Determines local vs cloud, model restrictions |
| **Task complexity** | How much judgment is required? | Determines model tier |
| **Frequency** | How often will this task run? | Cost and automation considerations |
| **Auditability** | Can we document and reproduce the process? | Governance and compliance |
| **Team readiness** | Does the team have the skills to use and review AI output? | Training and adoption planning |

---

## Key Takeaway

Skills give you consistency. Agents give you capacity. Models give you flexibility. Together, they turn AI from a chat tool into a operational capability for your accounting team.

Start with one skill (your most repetitive task), use it with one agent (a well-configured AI session), and choose the right model for the job. Scale from there.

---

*This is the final section of the framework. Return to the [Table of Contents](../README.md).*
