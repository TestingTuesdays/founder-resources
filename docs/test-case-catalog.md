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

Use [the bug report](../templates/bug-report.md) to report failures and [the retest template](../templates/retest.md) to verify fixes. Never target systems without permission.
