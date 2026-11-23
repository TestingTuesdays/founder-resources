---
name: billing-webhook-replay
description: Test payment webhooks, entitlements and refunds for founders and reviewers working with authorized product environments.
---

# Test payment webhooks, entitlements and refunds

[← All skills](../README.md) · [Topic guide](../../docs/payment-reconciliation.md) · [Report template](../../templates/test-case.md)

## Goal

Produce evidence that a founder can use to decide whether a specific change is ready to ship.

## Inputs

Versioned product build, target user task, relevant official documentation, fictional test accounts, authorization to test, pass/fail criterion and accountable reviewer.

## Procedure

1. Prepare sandbox subscription, expected invoice and entitlement states.
2. Simulate paid, failed, refunded and cancelled events.
3. Replay identical signed webhook and send realistic out-of-order events.
4. Check only one logical charge and entitlement transition occurs.
5. Reconcile provider and internal transaction identifiers, price and effective date.
6. Repeat after a fix and record unresolved drift.

## Done when

Sandbox ledger reconciliation showing idempotency and final entitlement state.

## Record

| Field | Required evidence |
| --- | --- |
| Task and risk | Why a failure would matter |
| Environment | Build, device, locale, test identity, feature flag |
| Steps | Exact reproducible actions |
| Expected / actual | Observable behavior, not guesswork |
| Severity and owner | Realistic impact and next action |
| Fix and retest | Deployed version, same task, changed outcome |

## Safety and limitations

Use synthetic identities/data in permissioned environments. Never scan or stress unowned systems, expose secrets or publish customer/participant recordings. A proposed test is not a passed test; always differentiate performed work from guidance. Escalate security, safety or regulated-product blockers for independent review.
