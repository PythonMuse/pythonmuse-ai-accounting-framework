# Hook Design Worksheet

*Use this worksheet to plan a new control hook for your AI workflow. Fill in each section before implementing.*

---

## Hook Overview

| Field | Value |
|-------|-------|
| **Hook Name** | [e.g., "Block Unmasked PII"] |
| **Type** | [PreToolUse / PostToolUse] |
| **Created By** | [Name] |
| **Date** | [YYYY-MM-DD] |
| **Project** | [Project name or folder] |

---

## Risk Identification

**What risk are you mitigating?**

[Describe the specific risk. Be concrete. Example: "AI could process a payroll file containing unmasked SSNs and send it to a cloud API, resulting in a data exposure incident."]

**What is the worst-case scenario if this risk materializes?**

[Example: "Employee PII is exposed. Regulatory notification required. Reputational damage."]

**What is the likelihood without a control?**

- [ ] High (happens frequently or is easy to trigger accidentally)
- [ ] Medium (could happen under certain conditions)
- [ ] Low (unlikely but possible)

---

## Hook Design

**What action triggers the hook?**

[Example: "Any file read or write operation on files in the data/payroll/ directory"]

- [ ] File read
- [ ] File write/edit
- [ ] Code execution
- [ ] Terminal command
- [ ] Other: _____

**What does the hook check?**

[Example: "Scans file contents for SSN patterns (XXX-XX-XXXX or 9 consecutive digits)"]

**What happens if the check passes?**

- [ ] Action proceeds normally
- [ ] Action proceeds with a logged note
- [ ] Other: _____

**What happens if the check fails?**

- [ ] Action is blocked completely
- [ ] Action is paused for human review
- [ ] Warning is displayed but action proceeds
- [ ] Other: _____

---

## Logging and Audit Trail

**What gets logged when the hook triggers?**

- [ ] Timestamp
- [ ] File name / path
- [ ] Action that was attempted
- [ ] Reason for block/pause
- [ ] User who was working
- [ ] Other: _____

**Where are logs stored?**

[Example: "In the project's logs/ directory, file: hook_audit.log"]

**Who reviews the logs?**

[Name or role]

**How often are logs reviewed?**

- [ ] Every session
- [ ] Weekly
- [ ] Monthly
- [ ] As needed

---

## Testing

**How will you test this hook?**

[Describe the test scenario. Example: "Create a test file with a known SSN pattern. Attempt to process it. Verify the hook blocks the action."]

**Test data:**

[What test file will you use?]

**Expected result:**

[What should happen when the hook is working correctly?]

---

## Implementation Notes

**Dependencies:**

[Any tools, scripts, or libraries required?]

**Configuration location:**

[Where will the hook configuration live? e.g., .claude/settings.json]

**Related hooks:**

[Are there other hooks that interact with this one?]

---

## Approval

| Role | Name | Date | Approved |
|------|------|------|----------|
| Designer | | | - [ ] |
| Reviewer | | | - [ ] |
| IT (if applicable) | | | - [ ] |

---

*Template from the [PythonMuse AI Accounting Framework](https://github.com/PythonMuse/pythonmuse-ai-accounting-framework)*
