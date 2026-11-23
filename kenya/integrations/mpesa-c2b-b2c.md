# M-Pesa C2B, B2C and payout workflow QA

[← Kenya hub](../README.md) · [Integration index](README.md) · [Test case template](../../templates/test-case.md)

## Why this matters

Collection and disbursement are distinct flows with distinct access, approval and reconciliation.

## Step-by-step founder workflow

1. Determine whether your business model needs collections, disbursements or both.
2. Verify production merchant, shortcode, limits and API availability directly with Safaricom or PSP.
3. Model callback, validation, confirmation and transaction reconciliation separately.
4. Reject duplicate C2B events and reconcile unmatched payments.
5. Restrict B2C payout permissions, approvals, destination edits and limits.
6. Simulate payout failures and reversals with fictional accounts.
7. Reconcile provider statement, internal ledger and customer status.

## Required test evidence

| Scenario | Expected state | Actual result | Severity | Owner / retest |
| --- | --- | --- | --- | --- |
| Successful authorized path | Documented expected outcome | Not run | | |
| Provider/network timeout | Safe retry or pending | Not run | | |
| Duplicate event/request | One logical outcome | Not run | | |
| Unauthorized or malformed input | Safely denied | Not run | | |
| Reversal/cleanup where relevant | Consistent records | Not run | | |

## Official starting points

- [Safaricom Daraja](https://developer.safaricom.co.ke/)
- [CBK](https://www.centralbank.go.ke/)

**Scope:** this is a test and implementation planning guide, not a live integration, guaranteed merchant onboarding, regulatory certification or legal/tax advice. Provider contracts, credentials, callbacks and current rules must be verified for the actual account.

_Last curated: 2026-11-23._
