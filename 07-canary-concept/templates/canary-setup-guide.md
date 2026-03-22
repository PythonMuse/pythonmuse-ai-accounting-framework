# Canary Setup Guide

*Step-by-step instructions for adding a canary to your project.*

---

## Step 1: Choose Your Canary Value

Pick a unique phrase that:
- Cannot be guessed from general knowledge
- Is memorable to you
- Is specific to this project

**Examples:**
- `Alpine Summit 42`
- `Blue Ledger 7`
- `Coffee Mug Protocol`
- `Penguin Audit 2026`

Have fun with it. The sillier, the more memorable.

---

## Step 2: Add to CLAUDE.md

Open (or create) the CLAUDE.md file in your project root. Add the canary near the top:

```markdown
# Project Instructions

## Canary
The canary is: [YOUR VALUE HERE]

## Project Overview
[rest of your instructions...]
```

**Copy-paste snippet:**

```markdown
## Canary
The canary is: Alpine Summit 42
```

---

## Step 3: Test

Start a new session (or restart your current one) and ask:

> "What is the canary?"

Verify the response matches exactly.

---

## Step 4: Use It Every Session

Make this your first prompt in every new session:

> "What is the canary?"

If correct, proceed with confidence.
If incorrect, troubleshoot before doing any work.

---

## Step 5: Change When Needed

If you:
- Suspect the AI is using cached context instead of fresh file reads
- Want to verify that a new session is truly starting fresh
- Just want to update your easter egg

Change the canary value in CLAUDE.md and test again.

---

## Checklist

- [ ] Canary value chosen
- [ ] Added to CLAUDE.md near the top
- [ ] Tested in a session
- [ ] Correct response confirmed
- [ ] Added to session startup routine

---

*Template from the [PythonMuse AI Accounting Framework](https://github.com/PythonMuse/pythonmuse-ai-accounting-framework)*
