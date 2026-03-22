# Sample Email: Requesting Read-Only SQL Access

*Copy, customize, and send to your IT team.*

---

**Subject:** Request for Read-Only Database Access for Financial Analysis

Hi [IT Contact / IT Team],

I am exploring ways to improve our monthly financial analysis process using Python-based data analysis tools. Currently, we export data manually from [ERP System Name] each month, which involves several manual steps and introduces opportunities for error.

I would like to request **read-only** SQL access to the following:

**Database:** [Database name, e.g., "Production GL Database"]

**Tables needed:**
- General ledger detail (transaction-level)
- Chart of accounts
- [Other specific tables]

**Purpose:** Automating the extraction of GL data for monthly analysis, including variance analysis, reconciliations, and management reporting.

**Scope:**
- **Read-only access only** (SELECT statements). No ability to modify, insert, or delete data.
- Access limited to the specific tables listed above.
- Queries will be run from my local workstation during business hours.
- No impact to system performance (queries will be simple and targeted).

**Security:**
- I will not store database credentials in any shared files or repositories
- Connection details will be stored in local environment variables only
- All analysis scripts will be version-controlled and reviewable

I am happy to discuss this further, walk through the specific queries I plan to use, or provide any additional information you need to evaluate this request.

Thank you for your help.

Best regards,
[Your Name]
[Your Title]
[Your Department]

---

## Tips for the Conversation

- **Be specific** about what tables you need. "Access to everything" is harder to approve than "read-only access to the GL detail table."
- **Emphasize read-only.** IT's biggest concern is usually that someone might accidentally change data.
- **Offer to demonstrate.** Showing IT exactly what queries you will run builds confidence.
- **Start with one table.** Once you demonstrate value and responsibility, expanding access is much easier.
- **Acknowledge their concerns.** IT is responsible for system security. Show that you respect that.

---

*Back to [SQL Access](../)*
