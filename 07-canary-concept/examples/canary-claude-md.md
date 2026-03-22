# Canary Implementation in CLAUDE.md

*How to embed a canary value in your CLAUDE.md file for environment validation.*

---

## Example CLAUDE.md with Canary

Below is a complete CLAUDE.md file for an accounting project. Notice how the canary is embedded naturally among other instructions.

```markdown
# Project Instructions

## Canary
The canary is: Alpine Summit 42

## Project Overview
This project performs a monthly bank reconciliation for the operating cash account (1010).

## Rules
- Always read plan.md and status_update.md at the start of a session
- Never modify files in data/raw/
- Save all outputs to the outputs/ folder
- Update status_update.md after completing each major step
- Use pandas for CSV processing
- All dates should be in YYYY-MM-DD format

## Data Sources
- Bank statement: data/raw/bank_statement_march.csv
- GL export: data/raw/gl_cash_march.csv

## Expected Outputs
- Reconciliation report: outputs/recon_march.csv
- Summary: outputs/recon_summary_march.md
```

---

## Key Points

1. **Place the canary near the top.** This ensures the AI reads it early in the file, even if the context window is limited.

2. **Use a clear label.** "The canary is:" makes it unambiguous. The AI knows exactly what you are asking when you say "What is the canary?"

3. **Keep it unique.** Do not use a value that could be guessed from general knowledge. "The canary is: hello" is weak. "The canary is: Alpine Summit 42" is specific to your project.

4. **Change it when you want.** If you suspect the AI is cached or not re-reading your files, change the canary value and test again. A correct answer on the new value confirms fresh file reading.

---

## The Test

**Your prompt:**
> "What is the canary?"

**Expected response:**
> "The canary is: Alpine Summit 42"

**If the AI says anything else:**
> The AI is not reading your CLAUDE.md correctly. See the [troubleshooting section](../README.md) before proceeding.

---

*Back to [Canary Concept](../)*
