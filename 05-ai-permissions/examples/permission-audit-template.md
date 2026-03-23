# AI Tool Permission Audit Template

*Use this template to document the permissions and data flow for each AI tool used in your projects.*

> **Why this matters:** Every AI tool your team uses should have a documented permission profile — what it can access, where data goes, and what controls are in place. This is not just good practice; it is a governance requirement. For the broader context on why controllers need to own this process, see [AI Governance for Controllers](https://github.com/PythonMuse/ai-ledger/tree/main/articles/07-ai-governance-for-controllers). For a structured assessment framework you can adopt alongside this template, see the [AI Governance Assessments](https://github.com/PythonMuse/accounting_and_finance-ai-governance/tree/main/assessments).

---

## Tool Profile

| Field | Value |
|-------|-------|
| **Tool Name** | [e.g., Claude Code, GitHub Copilot, ChatGPT] |
| **Version** | [version number or "web-based"] |
| **Provider** | [e.g., Anthropic, Microsoft, OpenAI] |
| **Date Assessed** | [YYYY-MM-DD] |
| **Assessed By** | [Name] |
| **IT Approved** | [Yes / No / Pending] |

---

## Access Permissions

| Permission | Capability | Scope | Notes |
|-----------|-----------|-------|-------|
| **Read Files** | [Yes / No] | [Which folders/files?] | [Any restrictions?] |
| **Write Files** | [Yes / No] | [Which folders?] | [Can it modify existing files?] |
| **Execute Code** | [Yes / No] | [What languages/commands?] | [Sandboxed or unrestricted?] |
| **Terminal Access** | [Yes / No] | [What commands?] | [Any blocked commands?] |
| **Clipboard Access** | [Yes / No] | [Read / Write / Both] | |
| **Network Access** | [Yes / No] | [Outbound only? Specific endpoints?] | |

---

## Data Flow

| Question | Answer | Details |
|----------|--------|---------|
| Where does processing occur? | [Local / Cloud / Hybrid] | |
| What data is sent externally? | [Prompts only / File contents / Metadata] | |
| Is transmission encrypted? | [Yes / No / Unknown] | |
| Server location | [US / EU / Other / Unknown] | |
| Data retention policy | [None / Temporary / Permanent] | |
| Opt-out available? | [Yes / No] | |
| DPA in place? | [Yes / No / N/A] | |

---

## Approved Use Cases

| # | Use Case | Data Sensitivity | Approved |
|---|----------|-----------------|----------|
| 1 | [e.g., Analyzing sample data] | [Low] | [Yes] |
| 2 | [e.g., Generating Python scripts] | [Low] | [Yes] |
| 3 | [e.g., Processing masked payroll data] | [Medium] | [Yes, with controls] |

---

## Restricted Use Cases

| # | Use Case | Reason for Restriction |
|---|----------|----------------------|
| 1 | [e.g., Processing unmasked PII] | [Data sent to cloud; no masking control] |
| 2 | [e.g., Querying production database] | [Tool has execute permission; risk of unintended changes] |

---

## Controls in Place

- [ ] Data masking applied before processing
- [ ] Sensitive folders excluded from tool access
- [ ] Output review required before use
- [ ] Activity logging enabled
- [ ] Hooks configured to block sensitive data patterns
- [ ] Regular permission review scheduled

---

## Review Schedule

| Review Date | Reviewer | Changes Made |
|-------------|----------|-------------|
| [YYYY-MM-DD] | [Name] | [Initial assessment] |
| [YYYY-MM-DD] | [Name] | [Quarterly review] |

---

*Template from the [PythonMuse AI Accounting Framework](https://github.com/PythonMuse/pythonmuse-ai-accounting-framework)*
