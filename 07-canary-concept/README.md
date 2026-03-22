# The Canary Concept -- A Simple Environment Validation

*A quick smoke test to confirm your AI is reading your project files correctly. And yes, you can have fun with it.*

---

## What Is a Canary?

A canary is a simple known-answer test. You embed a specific, unique value in your project files. At the start of a session, you ask the AI: "What is the canary?" If the answer is correct, your environment is working. If the answer is wrong -- or the AI does not know -- something is off.

The name comes from the old mining practice of bringing a canary into a coal mine. If the canary was fine, the air was safe. If it was not, the miners knew there was a problem before it affected them.

---

## The Accounting Parallel

When you start a new month-end close, you do not just dive into reconciliations. First, you check:

- Is the prior period closed?
- Are subledgers posted to the GL?
- Is the trial balance pulling correctly?

These are validation checks. You confirm the environment is in the expected state before you begin work.

The canary does the same thing for your AI workspace. Before you start working, you confirm:

- The AI is reading your project files (CLAUDE.md)
- Your workspace is loaded correctly
- You are in the right project

---

## How It Works

### Step 1: Choose a Canary Value

Pick something specific and memorable -- but not something the AI could guess from general knowledge. It should be unique to your project.

Examples:
- `The canary is: Alpine Summit 42`
- `The canary is: Blue Ledger 7`
- `The canary is: Coffee Mug Protocol`

Have fun with this one. Come up with the silliest question or the silliest answer and leave an easter egg in your workflow. It is your project -- make it yours.

### Step 2: Add It to CLAUDE.md

Place the canary value in your project's CLAUDE.md file alongside your other instructions. See [canary-claude-md.md](examples/canary-claude-md.md) for a complete example.

### Step 3: Test It

At the start of every new session, ask: "What is the canary?"

If the AI gives you the correct answer, you are good to go. If it does not, troubleshoot before proceeding.

---

## When Your Canary Fails

If the AI cannot answer the canary question correctly, check the following:

1. **Are you in the right project folder?** The AI may have opened a different workspace.
2. **Does CLAUDE.md exist in the project root?** The AI looks for this file automatically.
3. **Is CLAUDE.md readable?** Open it yourself and verify the canary value is there.
4. **Did the session load properly?** Some AI tools need a moment to index project files after opening.
5. **Are there multiple CLAUDE.md files?** The AI may be reading a different one.

A failed canary does not mean something catastrophic happened. It means you should investigate before trusting the AI's outputs in this session.

---

## Why Bother?

It takes five seconds to ask "What is the canary?" at the start of a session. The cost of not asking -- and discovering halfway through a reconciliation that the AI was not reading your project instructions -- is much higher.

This is the simplest control you can implement. And it is the one that prevents the most confusion.

---

*Next: [Project Hygiene](../08-project-hygiene/) -- managing your AI projects like a team member.*
