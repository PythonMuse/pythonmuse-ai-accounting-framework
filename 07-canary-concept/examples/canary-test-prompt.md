# Canary Test Prompts

*Use these prompts at the start of every AI session to verify your environment.*

---

## Primary Test Prompt

> "What is the canary?"

**Expected response:** The AI should respond with the exact canary value from your CLAUDE.md file.

**Example correct response:** "The canary is: Alpine Summit 42"

---

## Alternative Test Prompts

### Confirmation Style
> "Before we begin, confirm the canary value."

**Why this is useful:** It sets the tone that you are going to verify the environment before starting work. It signals to the AI that you expect it to have read your project files.

### Explicit File Reference
> "Read CLAUDE.md and tell me the canary."

**Why this is useful:** If the primary prompt fails, this forces the AI to explicitly read the file. If it still cannot answer, the file may be missing or in the wrong location.

### Combined with Status Check
> "Read CLAUDE.md and status_update.md. Tell me the canary value and summarize where we left off."

**Why this is useful:** This combines the canary check with a session resumption. One prompt, two verifications.

---

## Interpreting Results

### Correct Answer
The AI responds with your exact canary value.

**Action:** Proceed with your session. The environment is working correctly.

### "I don't have a canary value" or Similar
The AI does not recognize the canary concept.

**Action:**
1. Check that CLAUDE.md exists in your project root
2. Check that you opened the correct folder in VS Code
3. Try the explicit file reference prompt: "Read CLAUDE.md and tell me the canary."

### Wrong Answer
The AI gives a canary value, but it is incorrect or from a different project.

**Action:**
1. You may be in the wrong workspace
2. There may be multiple CLAUDE.md files causing confusion
3. Open CLAUDE.md yourself and verify the value
4. Restart the session in the correct project folder

### Generic Response About Canaries
The AI starts explaining what a canary is (the bird, the mining practice, etc.) instead of giving you the specific value.

**Action:** The AI is not reading your project files. It is responding from general knowledge. Follow the troubleshooting steps above.

---

## Best Practice

Make the canary check the first thing you do in every session. It takes five seconds and prevents wasted time in the wrong environment.

Some people make their canary values fun -- inside jokes, silly phrases, or references that make them smile. If checking the canary brings a moment of levity to the start of your work session, that is a feature, not a bug.

---

*Back to [Canary Concept](../)*
