# International payments, currency & regional checkout

[← Founder library](../README.md) · [Release readiness](release-readiness.md) · [Test-case template](../templates/test-case.md)

## When to use

Founders charging customers in Kenya, elsewhere in Africa, or across borders.

## Most common mistake

Assuming provider supports every legal entity, payout currency, card, wallet or mobile-money rail.

## Recommended practice

Verify business eligibility, settlement, chargebacks, refunds, exchange rates and local payment UX against current provider terms.

## Practical scenarios

1. **Local vs foreign card.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
2. **mobile-money failure.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
3. **currency rounding.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
4. **FX display.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
5. **delayed payout.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
6. **incomplete KYC.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
7. **abandoned redirect.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
8. **cross-border tax..** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.

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
| [Stripe global availability](https://stripe.com/global) | Documentation or diagnostic tool |
| [Paystack docs](https://paystack.com/docs/) | Documentation or diagnostic tool |
| [Flutterwave developer docs](https://developer.flutterwave.com/) | Documentation or diagnostic tool |
| [Safaricom Daraja](https://developer.safaricom.co.ke/) | Documentation or diagnostic tool |

## Deliverable

A versioned test matrix, documented failures, assigned owners and evidence-backed retest. Tool availability, provider support and regulatory expectations can change; confirm them for your actual jurisdiction.

_Last curated: 2026-11-23._
