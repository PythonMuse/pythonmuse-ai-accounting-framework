# Local vs Cloud: Data Flow Checklist

*A practical decision-tree checklist for determining where your data goes when using AI tools.*

---

## Before You Start: What Data Are You Working With?

- [ ] **Identify the data sensitivity level**
  - [ ] Public or non-sensitive (industry averages, sample data, templates)
  - [ ] Internal (draft reports, non-confidential analysis)
  - [ ] Confidential (financial statements, employee data, client information)
  - [ ] Restricted (PII, SSNs, bank account numbers, HIPAA data)

---

## Step 1: What Tool Are You Using?

### Is the AI running locally on your machine?
- [ ] Yes -- data stays on your machine during processing
- [ ] No -- proceed to Step 2

### Does the tool require an internet connection to function?
- [ ] Yes -- data likely leaves your machine
- [ ] No -- data stays local

---

## Step 2: Does Data Leave Your Machine?

### Does the tool send file contents to a cloud API?
- [ ] Yes
  - [ ] What data is included in the request? (full file, excerpt, metadata only)
  - [ ] Where are the servers located? (US, EU, other)
  - [ ] Is the transmission encrypted?
- [ ] No

### Does the tool send your prompts/instructions to external servers?
- [ ] Yes (most chat-based AI tools do this)
- [ ] No

### Are outputs generated locally or returned from the cloud?
- [ ] Generated locally (code execution on your machine)
- [ ] Returned from cloud servers

---

## Step 3: Data Retention

### Does the provider store your data after processing?
- [ ] No -- data is processed and discarded
- [ ] Yes, temporarily -- How long? _____
- [ ] Yes, permanently
- [ ] Unknown -- **stop and investigate before proceeding**

### Can you opt out of data retention or training?
- [ ] Yes -- have you enabled the opt-out?
- [ ] No
- [ ] Not applicable

### Is there a data processing agreement (DPA) available?
- [ ] Yes -- has legal reviewed it?
- [ ] No

---

## Decision Matrix

| Data Sensitivity | Local Tool | Cloud Tool (No Retention) | Cloud Tool (With Retention) |
|-----------------|------------|--------------------------|---------------------------|
| Public / Sample | OK | OK | OK |
| Internal | OK | OK with review | Requires approval |
| Confidential | OK | Requires approval + masking | Not recommended |
| Restricted (PII) | OK with controls | Only with masking + approval | Do not use |

---

## Action Items After Assessment

- [ ] Document which tool was used and what data was processed
- [ ] Confirm data handling aligns with organizational policy
- [ ] If cloud processing was used with sensitive data, log the justification and controls applied
- [ ] If you are unsure about any answer above, consult IT before proceeding

---

*Back to [AI Permissions](../)*
