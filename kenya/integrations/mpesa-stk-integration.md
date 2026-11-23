# M-Pesa STK Push implementation and failure-state design

[← Kenya hub](../README.md) · [Integration index](README.md) · [Test case template](../../templates/test-case.md)

## Why this matters

A successful prompt is not proof of a settled payment.

## Step-by-step founder workflow

1. Register an authorized Daraja sandbox app and review current provider API documentation.
2. Store consumer-facing order as pending before requesting STK push.
3. Use server-held credentials and correlate provider checkout/request IDs to one internal order.
4. Validate callback origin/shape as supported; independently query status or reconcile when missing.
5. Apply idempotent ledger transition, never rely on browser redirect or client status.
6. Handle canceled, timed-out, duplicated and late callbacks without double entitlement.
7. Reconcile refunds/reversals and keep phone numbers out of public logs.

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
