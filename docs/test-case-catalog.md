# Common test scenarios for production products

[← Home](../README.md) · [Test-case template](../templates/test-case.md)

These are *examples*, not universal requirements. Mark non-applicable features N/A. For every attempt record build, environment, preconditions, expected versus actual outcome and whether a retest verified the fix.

| ID | Scenario | Expected behavior |
| --- | --- | --- |
| AUTH-01 | New user signs up and verifies email | One account; clear next step |
| AUTH-02 | Invalid/duplicate signup | Useful error, no duplicate record |
| AUTH-03 | Wrong password, lockout and recovery | No account enumeration or weak reset |
| AUTH-04 | Expired/reused reset link | Safely rejected; recovery path |
| AUTH-05 | Session expires during form submit | Safe recovery with no hidden data loss |
| UX-01 | New user finds main task | Completes without coaching |
| UX-02 | Search returns no results | Useful empty state and next action |
| UX-03 | Invalid, international and long form input | Accessible error; preserved input |
| UX-04 | Double-click submit or retry request | Exactly one logical action |
| UX-05 | Timeout / offline / reconnect | Graceful status; no corruption |
| A11Y-01 | Entire task keyboard-only | Reachable, visible focus, no trap |
| A11Y-02 | Screen reader form and modal | Named fields, errors, focus management |
| A11Y-03 | 200% zoom and large text | No missing essential content |
| SEC-01 | Access another user's object ID | Denied by server |
| SEC-02 | Cross-tenant search/export | No leakage of records |
| SEC-03 | Invalid file uploads | Safely rejected |
| SEC-04 | Secrets in bundle/logging | None disclosed |
| BILL-01 | Payment success, duplicate request | One charge/entitlement |
| BILL-02 | Payment declined, retry and refund | Correct invoice/state |
| BILL-03 | Duplicate/reordered billing webhook | Idempotent final state |
| BILL-04 | Cancel/trial expiry/downgrade | Correct effective date |
| PERF-01 | Slow mobile network | Primary task remains usable |
| PERF-02 | Service outage and job retries | Safe recovery and alarms |
| PERF-03 | Backup restoration and rollback | Verified recovery with owner |
| L10N-01 | Long translation, RTL and plurals | No semantic/layout failure |
| L10N-02 | Time zones and DST boundary | Correct representation |
| L10N-03 | Names/addresses/phone formats | No single-market assumptions |
| MOB-01 | Clean install and previous-version upgrade | No lost user state |
| MOB-02 | Denied permissions / background resume | Useful alternative |
| MOB-03 | Large text and screen readers | Core flow usable |
| MOB-04 | Store reviewer demo credentials | Real working review path |
| AI-01 | Known facts and unanswerable prompts | Grounded response, uncertainty |
| AI-02 | Injected instructions in retrieved content | No unauthorized action |
| AI-03 | Tool failure, wrong scope, malformed output | Safe bounded recovery |
| HW-01 | Loss of power/connectivity during use | Safe predictable state |
| HW-02 | Interrupted firmware update/ownership reset | Safe recovery and revoked access |
| MKT-01 | No supply/no search results | Useful fallback |
| MKT-02 | Report abusive content/block user | Action enforced and logged |

| AUTH-06 | Removed workspace user accesses old invitation or shared link | Access revoked server-side |
| AUTH-07 | Different tenant guesses export or object ID | No unauthorized data disclosed |
| AUTH-08 | MFA recovery flow after device loss | Identity verified without silent bypass |
| PAY-01 | Provider posts duplicated payment webhook | Single logical ledger transition |
| PAY-02 | Refund after downgrade or cancellation | Entitlements and invoices reconcile |
| PAY-03 | Checkout succeeds but redirect is lost | Server reconciles independently |
| PAY-04 | Billing event arrives out of order | Consistent final state |
| STORE-01 | App reviewer signs in with supplied demo mode | Working feature access |
| STORE-02 | App listing screenshots mismatch shipped build | Metadata corrected before submission |
| STORE-03 | Permission revoked after installation | Graceful recovery |
| FLAG-01 | Ineligible user forces feature API request | Backend denies or excludes |
| FLAG-02 | Kill switch disabled risky feature | No unsafe writes continue |
| FLAG-03 | Feature flag service unavailable | Safe documented fallback |
| VIS-01 | Small-device pricing page with large font | No clipped CTA |
| VIS-02 | Long RTL translation in modal | Readable layout and focus |
| VIS-03 | Dark mode and image fallback | Contrast and functional interactions preserved |
| PRIV-01 | User requests data export | Complete authorized scope |
| PRIV-02 | User deletes account and tries old session | Revoked per documented policy |
| PRIV-03 | Unauthorized actor requests another user's deletion | Denied and auditable |
| DR-01 | Restore snapshot into isolated environment | Integrity verified |
| DR-02 | Restore includes queued webhook state | No duplicate external side effects |
| AIAG-01 | Retrieved page injects tool instructions | Untrusted content cannot override authorization |
| AIAG-02 | Agent writes to another tenant's record | Tool service rejects operation |
| AIAG-03 | Model tool repeatedly times out | Bounded retry and safe state |
| FORM-01 | Screen reader identifies each field error | Error associated with field |
| FORM-02 | Offline during submission and reconnect | No loss or duplicate record |
| FORM-03 | Overlong/international name or address | Valid inputs retained and processed |
| HELP-01 | Support user requests account access | Safe identity verification |
| HELP-02 | Critical support ticket escalates | Correct owner, status and timeframe |
| WEB3-01 | Wallet rejects signature | UI recovers, nothing submitted |
| WEB3-02 | Wrong chain or transaction reverts | Correct status and next action |
| CONTENT-01 | Knowledge-base page renamed | Internal links updated |
| CONTENT-02 | Blog claims credit amount without primary evidence | Claim withheld or labeled unverified |

Use [the bug report](../templates/bug-report.md) to report failures and [the retest template](../templates/retest.md) to verify fixes. Never target systems without permission.
