# KRA eTIMS invoice and refund workflow QA

[← Kenya hub](../README.md) · [Integration index](README.md) · [Test case template](../../templates/test-case.md)

## Why this matters

Tax compliance requires correct applicability, invoicing and reconciled records.

## Step-by-step founder workflow

1. Confirm eTIMS and tax obligations for the legal entity with current KRA guidance.
2. Map order/payment/refund to invoice and credit note states.
3. Verify invoice identifiers and tax calculations in approved test environment.
4. Test partial refund, cancellation and delayed payment settlement.
5. Reconcile ledger, tax record and invoice without duplicate issuance.
6. Handle service outage or retry without duplicated tax documents.
7. Ask a Kenyan tax professional to validate the actual setup.

## Required test evidence

| Scenario | Expected state | Actual result | Severity | Owner / retest |
| --- | --- | --- | --- | --- |
| Successful authorized path | Documented expected outcome | Not run | | |
| Provider/network timeout | Safe retry or pending | Not run | | |
| Duplicate event/request | One logical outcome | Not run | | |
| Unauthorized or malformed input | Safely denied | Not run | | |
| Reversal/cleanup where relevant | Consistent records | Not run | | |

## Official starting points

- [KRA](https://www.kra.go.ke/)
- [Kenya Law](https://new.kenyalaw.org/)

**Scope:** this is a test and implementation planning guide, not a live integration, guaranteed merchant onboarding, regulatory certification or legal/tax advice. Provider contracts, credentials, callbacks and current rules must be verified for the actual account.

_Last curated: 2026-11-23._
