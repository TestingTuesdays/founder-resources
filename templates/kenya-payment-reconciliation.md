# Kenya payment integration test record — sandbox only

**Merchant legal entity / PSP (keep private):**  
**Sandbox provider and build:**  
**Currency:** KES  

| Scenario | Expected status | Provider event | Internal ledger | Actual / defect |
| --- | --- | --- | --- | --- |
| STK initiated | Pending | | | |
| Customer accepts | Paid only after verified result | | | |
| Customer cancels | Not paid | | | |
| Timeout / no callback | Pending / reconciliation path | | | |
| Duplicate callback | One logical event | | | |
| Refund or reversal | Reconciled and traceable | | | |
| Network retry | No duplicate payment | | | |

**Provider production onboarding confirmed?** Yes / No / Unknown  
**Applicable licensing question and owner:**  
**Retest build and result:**  

Do not publish transaction identifiers, customer phone numbers, access tokens or account data. Sandbox success is not production approval.
