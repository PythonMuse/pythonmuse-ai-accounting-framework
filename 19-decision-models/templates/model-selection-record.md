# Model Selection Record

*Use this record when a workflow step will use a decision model or an LLM at run time. It documents why this method was chosen, so a reviewer can challenge the choice before they review the vendor. Complete it before the step goes live, and update it when anything below changes.*

> **Practice on a synthetic step first.** Do not enter real customer, vendor, or employee data here. This record describes the design of the step, not the data it processes. See [AI Governance for Controllers](https://github.com/PythonMuse/ai-ledger/tree/main/articles/07-ai-governance-for-controllers).

---

## Overview

| Field | Value |
|-------|-------|
| **Workflow and step** | [e.g., AR inbox, late-payment reason code] |
| **Owner** | [Name or role] |
| **Date approved** | [YYYY-MM-DD] |
| **Next review date** | [YYYY-MM-DD] |

---

## 1. Why This Method?

| Question | Answer |
|----------|--------|
| What does the step need to produce? (the shape of the answer) | [A calculation / a choice among known answers / open-ended text / a judgment] |
| Could a written rule do it? If not, why not? | [Explain] |
| Method chosen | [Deterministic / decision model / LLM / person] |
| Alternatives considered and rejected | [List, with the reason for each] |
| Does the step need to generate an answer, or choose among answers we already understand? | [Explain] |

## 2. Permission

| Question | Answer |
|----------|--------|
| Is this tool approved for this data classification? | [Yes / No / Conditional] |
| Where does the model run, and what does the provider retain? | [Explain] |
| Does any customer contract restrict machine learning, automated decisions, or external processing? | [Yes / No / Checked on YYYY-MM-DD by role] |
| Minimum data the step needs | [e.g., the reason-code text only, not the full email thread] |

## 3. Consequence and Verification

| Question | Answer |
|----------|--------|
| What happens if the output is wrong? | [Describe the impact] |
| How hard is the output to check? | [Easy to tie out / needs reading / hard] |
| Validation evidence | [Test set, size, results, date] |

## 4. Probability Bands (decision models only)

Set these from your own labeled history, not from an article.

| Band | Range | What happens |
|------|-------|--------------|
| High | [e.g., set from own testing] | [Route automatically and log] |
| Middle | [range] | [Person confirms] |
| Low or split | [range] | [Person decides] |

| Item | Value |
|------|-------|
| Wording of the question and answer list frozen on | [YYYY-MM-DD] |
| Who may change the wording | [Role, through review] |

## 5. Change Control

| Question | Answer |
|----------|--------|
| Model name and version approved | [As recorded by the provider] |
| Who is notified when the provider changes or retires the model? | [Role] |
| Retest required when the model changes? | [Yes -- describe the test] |

## 6. Authority

- [ ] The model recommends or classifies only. It does not approve, post, or pay.
- [ ] A named person is accountable for every consequential decision.

---

## Sign-off

| Role | Name | Date |
|------|------|------|
| Process owner | | |
| Reviewer | | |

---

*Part of [Module 19: Decision Models](../README.md) in the [PythonMuse AI Accounting Framework](https://github.com/PythonMuse/pythonmuse-ai-accounting-framework).*
