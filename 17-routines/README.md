# Routines -- Work That Runs Without You in the Room

*A prompt is something you ask once. A routine is something that runs on a schedule, indefinitely.*

---

## The Line You Are Crossing

Everything up to this point has had you present. You asked, the AI answered, you reviewed.

A routine changes that. It runs on a schedule or a trigger, whether or not you are watching, and it keeps running until someone stops it. That is a genuinely different risk posture, and it deserves a different level of design.

The good news: this is familiar ground. You already run unattended processes -- recurring journal entries, automated bank feeds, scheduled reports. You already know the questions. Who owns it? What happens if it fails? Who finds out? What stops it from doing the wrong thing twice a month, quietly, for a year?

---

## Where Routines Sit

```
Prompts are where many of us start.
Skills make the instructions reusable.
Routines make the work repeatable.
Controls make it safe.
Evidence makes it audit-friendly.
```

A routine without the last two rungs is not automation. It is an unsupervised intern with recurring calendar access.

---

## The Routine Pattern

Most useful accounting routines follow one shape:

```
Source -> Local Knowledge Base -> Routine -> Proposed Update -> Human Review -> Commit
```

In plain terms, six questions:

1. **Where does the truth live externally?** The regulator's site, the vendor's release notes, the bank's portal.
2. **Where did we write down our current interpretation?** Your own guidance file -- separate from the source.
3. **How often should we check?** Daily, monthly, quarterly.
4. **What should AI do if it finds a change?** Draft something. Never apply it.
5. **Who reviews it?** A named person, not a role in the abstract.
6. **How do we preserve the evidence?** A dated file in `evidence/`.

Step 2 matters more than it looks. **Keep official guidance separate from your company's interpretation of it.** The source is a fact you do not control. Your application of it is a decision you own. Merging them means you can never tell which changed.

---

## The Five Things You Review Before You Click Run

Modern tools will generate a complete routine from a sentence. That is the same moment as clicking "PivotTable" -- one action creates real machinery, and the machinery is what matters.

The command is not the automation. The command *generates* the automation. Before it runs, review five things.

### 1. The Trigger
*When does this fire, and can it fire twice?*
```yaml
trigger: monthly_on_day_3
```
A schedule that overlaps with a retry, or a trigger tied to a file appearing, can fire more than once. Ask what happens on the second run.

### 2. The Sequence
*What order do the steps run in, and what happens if step 2 fails?*
Does it stop, skip, or carry on with incomplete data? Carrying on is the dangerous default.

### 3. The Permissions
*What can this reach?*
```yaml
permissions:
  allowed_folders:
    - data/raw
    - outputs
```
The narrowest list that still works. Watch for `- /`.

### 4. The Retry Rules
*What does it do when something fails?*
```yaml
retry:
  attempts: 3
  delay_seconds: 60
```
Three retries on a read is sensible. Three retries on anything that writes, sends, or posts is three of them.

### 5. The Human Gate
*Where does a person have to say yes?*
```yaml
approval:
  required: true
  approver_role: controller
```
If the answer is nowhere, that is a design decision. Make it deliberately.

---

## The Proposed Change Package

The single most useful pattern for accounting routines: **the routine never changes anything. It prepares a change for someone to approve.**

Output a dated file containing:

- Date checked
- Source reviewed, with the link
- Summary of the detected change
- Potential impact
- Files potentially affected
- Recommended update
- Human review required: yes
- Reviewer notes: _______
- Decision: `[ ] Approved  [ ] Rejected  [ ] Needs more research`

This turns an unattended process into a preparer. The reviewer stays exactly where they were. The routine did the watching, the reading, and the drafting -- the three things that do not require judgment and are easy to let slide.

Please do not let your tax guidance wander the internet unsupervised.

---

## The Autonomy Ladder

Not every routine deserves the same latitude. There is a natural progression, and the safest approach is to earn each rung:

| Rung | What the AI does | Risk |
|------|-----------------|------|
| **Retrieve** | Fetches and shows information | Low -- read only |
| **Analyze** | Calculates, compares, summarizes | Low -- still no change |
| **Recommend** | Proposes an action | Low -- human decides |
| **Prepare** | Drafts the entry, file, or message | Moderate -- output exists but is not live |
| **Approve** | Routes to a person for sign-off | The gate itself |
| **Execute** | Makes the change in a real system | High -- reversible only with effort |

Most accounting value sits in the first four rungs. Start at Retrieve. Move up only when the rung below has run cleanly for long enough that you would defend it to a reviewer.

---

## Four Ways Routines Go Wrong

Each of these is real, and each is caught by one of the five review items:

1. **The permission that grants too much.** `allowed_folders: - /`. Nothing fails. Everything is reachable.
2. **The delete against the wrong folder.** A path that was correct in testing and is not correct in production.
3. **The trigger that fires twice.** Two runs, two outputs, two sets of numbers, no error.
4. **The notification that goes to the wrong list.** Internal exception detail delivered outside the team.

None announces itself. All four produce a workflow that appears to be working.

---

## Where the Human Still Belongs

A routine can watch, read, compare, and draft. It should not be the one deciding:

- Whether a change actually applies to your company
- What materiality means in this context
- Whether an exception is an error or a legitimate variation
- Whether a conclusion is defensible to an auditor
- When to stop and ask someone

Your role moves from *doing* to **designing, reviewing, and approving**. That is a promotion, but only if the design work actually happens.

---

## A Note on Tools

Routines require a harness. A chat window can listen and respond -- it cannot create a file on a schedule or run a step at 6 a.m. See [Module 14](../14-ai-work-harness/).

Beyond that, the specific tool matters less than the structure. Scheduling mechanisms differ across products and change frequently. The five review items, the proposed-change package, and the autonomy ladder do not.

**The tooling is a harness. The governance is yours.**

---

## Try This

1. Name one thing you check on a recurring basis that never changes and always has to be checked anyway. That is your first routine candidate.
2. Write the six Routine Pattern answers for it before writing any configuration.
3. Design it to stop at **Recommend**. Run it for a full cycle that way.
4. Write the proposed-change package template once and reuse it.

---

## Key Takeaway

A routine is a process that operates without you in the room, which makes it a control environment question rather than a convenience question.

Review the trigger, the sequence, the permissions, the retries, and the human gate before it runs. Have it prepare changes rather than make them. Start at the bottom of the autonomy ladder. Keep the evidence.

In the AI era, "I didn't write the code" will not be enough of a control explanation.

---

*You have reached the end of the framework. Return to the [Table of Contents](../README.md), or explore the full article series at [PythonMuse AI Ledger](https://github.com/PythonMuse/ai-ledger).*
