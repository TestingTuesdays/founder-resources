# Payments, refunds, subscriptions and reconciliation

[← Founder resources](../README.md) · [Test cases](test-case-catalog.md) · [Templates](../templates/README.md)

## Who this is for

Subscription SaaS, ticketing, marketplaces and mobile apps selling services.

## Why it matters

A checkout success page is not proof that the provider ledger, entitlements and your database agree.

## Frequent mistakes

- Trusting the browser redirect instead of signed server-side events.
- Granting entitlements twice after webhook replay.
- Confusing authorization, capture, refund and payout states.
- Ignoring failed payment, dispute and duplicate checkout.

## Test scenarios

1. **Valid sandbox payment grants exactly one correct entitlement.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
2. **Payment declined does not grant access and offers clear recovery.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
3. **Duplicated and out-of-order provider events converge to correct state.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
4. **Trial-to-paid transition handles expired/failed payment safely.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
5. **Cancel and refund update access at documented effective dates.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
6. **Invoice, provider transaction, entitlement and internal record reconcile.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
7. **Mobile digital-goods flow is checked against current store payment rules.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.

## Founder workflow

1. Choose the top one to three real user journeys relevant to your product.
2. Prepare synthetic data and an authorized test environment. Do not share production credentials or personal records.
3. Write observable pass/fail criteria *before* executing the happy path and the failure/recovery scenarios.
4. Run the checks with appropriate devices, identities and permissions. Do not assume an automated tool proves the complete journey.
5. File reproducible defects, assign severity based on harm, fix in a versioned build and retest.
6. Decide go/no-go; block on critical privacy, money, safety, irreversible-data or core-task risks.

## Primary references and tools

| Resource | Value |
| --- | --- |
| [Stripe testing](https://docs.stripe.com/testing) | Primary documentation and implementation patterns |
| [Stripe Webhooks](https://docs.stripe.com/webhooks) | Primary documentation and implementation patterns |
| [Paddle developer docs](https://developer.paddle.com/) | Primary documentation and implementation patterns |
| [Apple Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) | Primary documentation and implementation patterns |
| [Google Play policy help](https://support.google.com/googleplay/android-developer/) | Primary documentation and implementation patterns |

## Expected deliverable

Sandbox event matrix, idempotency proof, ledger reconciliation sample and clear policy treatment.

**Do:** keep assumptions and evidence separate, disclose uncertainty and verify current rules before release. **Don't:** imply testing coverage beyond what was executed, or expose real users and assets to experiments without permission.

_Last edited: 2026-11-23. External policies and tool capabilities can change._
