# Your AI Work Harness and the Agent File

*The tooling is a harness. The governance is yours.*

---

## What Is a Harness?

You will see the word "harness" throughout the PythonMuse series, usually without a definition. Here is one.

**An AI work harness is a structured environment where AI can work with files, folders, scripts, instructions, outputs, and evidence.**

A chat window is not a harness. A chat window can listen and respond. It cannot open your `data/raw/` folder, run a reconciliation script, write an output file with today's date on it, or leave a record of what it did. A harness can do all four.

The clearest way to think about it:

| Piece | What it is | Who controls it |
|-------|-----------|----------------|
| **The harness** | The kitchen -- files, folders, permissions, the ability to run things | You |
| **The instructions** | The recipe -- your accounting rules, written down | You |
| **The model** | The chef -- Claude, GPT, Gemini, whichever | The vendor |

The point of separating them is that you can swap chefs without redesigning the process. When a vendor updates their model, rebrands their product, or replaces the underlying AI entirely, your recipe still works. **The AI environment changes. The accounting control logic does not.**

This is why the series teaches the framework and not the software. VS Code with an AI extension is a harness. Claude Code is a harness. Codex is a harness. So is whatever ships next year.

---

## Why Chat Alone Runs Out of Road

Chat is genuinely fine for a lot of work: understanding a new standard, drafting an email, sanity-checking a formula, exploring a question before you know what you are looking for.

It runs out of road at a predictable point -- when you need to answer any of these:

- Which exact file did you use?
- Do the totals tie to the source?
- Can I run this again next month and get the same thing?
- Can someone else reproduce it without me in the room?
- Can I show a reviewer what happened?

Those are not AI questions. They are workpaper questions, and a chat transcript is a poor workpaper. A sticky note is fine for a grocery list. It is not ideal for lease accounting.

---

## Why AI Forgets: The Context Window

Every AI model reads and writes within a **context window** -- a fixed budget of text it can hold at once, covering your instructions, the files it has opened, and everything said so far in the session.

Two consequences matter for accounting work:

1. **When the session ends, the context is gone.** Start tomorrow and the model does not remember yesterday's decisions, your materiality threshold, or which accounts you agreed to exclude.
2. **When the window fills up, earlier material gets squeezed out.** A long, sprawling session quietly loses the instruction you gave at the beginning. Nothing announces this. The answers just get worse.

This is the actual reason for the three project files in [Project Hygiene](../08-project-hygiene/):

| File | What it survives |
|------|-----------------|
| `plan.md` | The scope, so it does not have to be re-explained every session |
| `status_update.md` | Where the work stopped, so tomorrow picks up rather than restarts |
| `backlog.md` | What is still outstanding, so it is not held in someone's memory |

Those files are not bureaucracy. They are external memory for a system that has none. Written down, your context survives a session reset, a model upgrade, and your own vacation.

---

## The Agent File

In a harness, the AI's standing instructions live in a file at the root of your project. That file is the closest thing you have to onboarding documentation for a new team member -- except this one actually reads it every time.

**On the filename:** you will see `CLAUDE.md` in some tools and `AGENTS.md` in others. Article 35 settles it:

> The primary agent file may be named `AGENTS.md`, `CLAUDE.md`, or another filename required by the AI harness you're using. The exact filename matters less than the content -- and whether the tool you picked actually reads it.

Check your tool's documentation for the name it expects. Everything below is about the content.

### The five sections

| Section | What it answers |
|---------|----------------|
| **Role** | What the AI is here to do -- and what it is not here to decide |
| **Rules** | The non-negotiables, stated as instructions rather than preferences |
| **Data Locations** | Which folder is source of truth, which is scratch, which is output |
| **Skills** | Which reusable procedures exist and when to use them |
| **Tone** | How output should read -- for most accounting work, suitable for workpaper documentation |

### A starting set of rules

These seven cover most of what goes wrong:

1. **Never process raw sensitive data.** Stop and ask for a masked version.
2. **Read `plan.md` first.**
3. **Propose before executing.**
4. **Save all outputs to `/outputs/`** with the date in the filename.
5. **Update `status_update.md`** after each milestone.
6. **Do not guess.** No assumed materiality thresholds, account mappings, or business rules.
7. **Keep it reproducible.**

Rule 6 is where AI workflows fail silently. A model asked to apply materiality with no threshold given will pick one that looks sensible and will not tell you it did. The output will be clean, formatted, and wrong in a way that survives review.

### Role is a governance statement

Write the Role section to say what the AI does *not* decide:

> You are a co-pilot for an accounting professional. Your job is to prepare, calculate, and document -- not to make decisions.

"Not to make decisions" is not a polite disclaimer. It is the line between a preparer and an approver, and it belongs in writing.

---

## Propose Before Executing

The single highest-value rule in the list is number 3.

**Propose before executing** means the AI states its plan -- inputs, steps, calculations, outputs -- and waits for you to approve it before touching anything. You already run this control. It is the preparer/reviewer workflow in your close process, moved one step earlier.

A good proposed plan tells you: which files it will read, what it will calculate, what assumptions it is making, which records it intends to exclude and why, what it will write and where, and what it will do if a check fails.

Reviewing that plan takes two minutes. Unwinding a bad run takes considerably longer.

---

## Instructions Are Not Controls

This is the most important paragraph in this module.

**Telling AI not to transmit sensitive data does not create a firewall. Telling AI not to overwrite raw data does not create a read-only permission.**

An agent file is written guidance. Written guidance is where control design starts, not where it ends. A policy stating that journal entries require approval is important. A system workflow that prevents an unapproved entry from posting is stronger. Both matter -- only one actually stops the error.

When a rule matters enough that you cannot afford it to be ignored, escalate it from instruction to enforcement:

| Instruction (guidance) | Enforcement (control) |
|---|---|
| "Do not modify `data/raw/`" | Operating-system read-only permission on the folder |
| "Mask sensitive fields before sending anything to a cloud service" | A [hook](../06-hooks-as-controls/) that blocks the call when a pattern matches |
| "Validate totals before saving output" | A script that raises an error and stops |
| "Get approval before executing" | An approval gate in the workflow configuration |
| "Only use approved files" | A [manifest](../16-configuration-literacy/) the script checks against |

A neat folder structure is not a security control. It is just a neat folder structure.

---

## Try This

1. **Name your harness.** Whatever tool you use, write one sentence describing what it can reach: which folders, which files, whether it can run code, whether anything leaves your machine.
2. **Write a five-line agent file.** Role, plus your top three non-negotiables. Five lines that exist beat fifty that do not.
3. **Add "propose before executing"** and run one real task. Read the plan before approving it. Notice what it assumed.
4. **Pick one rule you could not afford to have ignored** and work out what it would take to enforce rather than request.

---

## Key Takeaway

A harness is where AI can actually do accounting work: real files, real outputs, real evidence. The agent file is how you tell it the rules before it starts, rather than correcting it afterward.

But the file is guidance, not a control. Write it, commit it, keep it current -- and for the rules that genuinely matter, back them with something that can say no.

---

*Next: [Validation and Evidence](../15-validation-and-evidence/) -- proving the answer, not just producing it.*
