# Kenyan payment provider evaluation and selection

[← Kenya hub](../README.md) · [Integration index](README.md) · [Test case template](../../templates/test-case.md)

## Why this matters

Choose a provider based on the actual legal entity, checkout methods and payout economics.

## Step-by-step founder workflow

1. Define legal incorporation, business category and target settlement currency.
2. Confirm provider merchant onboarding for Kenya and permitted business model.
3. Compare M-Pesa, card, bank and international rails available to your account.
4. Request written current fee, chargeback, payout schedule and reserve details.
5. Review hosted checkout versus direct integration, fraud, webhook signing and test environment.
6. Test refunds, reversals, partial settlements and support escalation.
7. Calculate true total cost including FX, tax, dispute fees and delayed payouts.

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
- [Paystack docs](https://paystack.com/docs/)
- [Flutterwave docs](https://developer.flutterwave.com/)
- [CBK](https://www.centralbank.go.ke/)

**Scope:** this is a test and implementation planning guide, not a live integration, guaranteed merchant onboarding, regulatory certification or legal/tax advice. Provider contracts, credentials, callbacks and current rules must be verified for the actual account.

_Last curated: 2026-11-23._
