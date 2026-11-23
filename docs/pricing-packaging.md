# Pricing pages, trials & conversion integrity

[← Founder library](../README.md) · [Release readiness](release-readiness.md) · [Test-case template](../templates/test-case.md)

## When to use

SaaS founders introducing paid tiers, seats, usage metering and trials.

## Most common mistake

Advertising unlimited plans when quotas, add-ons or renewals differ.

## Recommended practice

Audit all claims against actual checkout, entitlement, tax and invoice states.

## Practical scenarios

1. **Free trial eligibility.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
2. **tax/currency.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
3. **annual/monthly toggles.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
4. **changing seat count.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
5. **coupon expiry.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
6. **downgrade.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
7. **refund.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
8. **cancellation.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
9. **accessible checkout..** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.

## Founder workflow

1. Identify the primary user task, critical failure, and who will be impacted.
2. Prepare a safe sandbox, representative device/network and synthetic accounts.
3. Test normal behavior, rejection and partial failure independently.
4. Compare actual observation to documented provider or product promises.
5. Prioritize privacy, monetary, safety and blocked core-task defects.
6. Ship a reversible fix, observe the release, and retest the original task.

## Tools and primary references

| Resource | Scope |
| --- | --- |
| [Stripe Billing docs](https://docs.stripe.com/billing) | Documentation or diagnostic tool |
| [Paddle developer docs](https://developer.paddle.com/) | Documentation or diagnostic tool |
| [FTC business guidance](https://www.ftc.gov/business-guidance) | Documentation or diagnostic tool |

## Deliverable

A versioned test matrix, documented failures, assigned owners and evidence-backed retest. Tool availability, provider support and regulatory expectations can change; confirm them for your actual jurisdiction.

_Last curated: 2026-11-23._
