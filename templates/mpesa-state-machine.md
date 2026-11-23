# M-Pesa payment state-machine QA — sandbox template

**Order ID (synthetic):**  **Provider sandbox:**  **Build:**

| Starting state | Trigger | Expected next state | Side effects allowed? | Evidence |
| --- | --- | --- | --- | --- |
| Created | STK request accepted | Prompt pending | No entitlement yet | |
| Prompt pending | User cancels | Cancelled/failed | No charge claim | |
| Prompt pending | Provider timeout | Pending reconciliation | No premature success | |
| Pending | Verified successful event | Paid | Exactly one entitlement | |
| Paid | Duplicate callback | Paid | No duplicate ledger write | |
| Paid | Verified reversal/refund | Reversed/refunded | Reconciled ledger | |

**Reconciliation source and idempotency key strategy:**  
**Webhook authenticity and credential storage review:**  
**Production merchant approval:** Unverified / Confirmed with source  
**Retest owner/build:**  

Do not store phone numbers, tokens, transaction IDs or customer data in public GitHub.
