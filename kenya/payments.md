# Kenya payments: M-Pesa, PSPs and reconciliation

[← Kenya hub](README.md) · [App-type playbooks](../app-types/README.md) · [Testing template](../templates/test-case.md)

Start with a merchant eligibility decision, not just an SDK.

## Founder considerations

- Safaricom Daraja is an official M-Pesa integration entry point; production access and business verification are distinct from sandbox access.
- Check CBK's licensed payment service providers and applicable activity classification.
- Paystack and Flutterwave availability, settlement and methods must be confirmed for the exact Kenyan business/entity.
- Never treat a client redirect, STK prompt or callback alone as final ledger settlement.

## Minimum tests

1. **STK push initiated but user cancels or prompt expires.** Record expected/actual result, build, affected user, severity, owner and retest.
2. **Callback duplicated, delayed, missing or out of order.** Record expected/actual result, build, affected user, severity, owner and retest.
3. **Transaction reference mismatch, partial reversal or refund.** Record expected/actual result, build, affected user, severity, owner and retest.
4. **Duplicate click after network loss; idempotency key enforcement.** Record expected/actual result, build, affected user, severity, owner and retest.
5. **Wrong MSISDN formatting or shared device.** Record expected/actual result, build, affected user, severity, owner and retest.
6. **Payout/settlement amount differs from order ledger.** Record expected/actual result, build, affected user, severity, owner and retest.

## Implementation and compliance workflow

1. Document the legal entity, target users, product activities, payment/data flows and provider contracts.
2. Consult current primary regulator and provider documentation; do not infer eligibility from a sandbox API key.
3. Identify the relevant permission, registration, licensing, contract or tax question; record it as **unverified** until confirmed.
4. Run tests on synthetic accounts, sandbox payments and representative Kenyan devices/networks.
5. Get appropriate qualified local legal/accounting/sector review for obligations and approvals.
6. Fix high-risk issues, version the release and retest the affected user journey.

## Primary starting points

- [Safaricom Daraja](https://developer.safaricom.co.ke/)
- [CBK](https://www.centralbank.go.ke/)
- [Paystack docs](https://paystack.com/docs/)
- [Flutterwave docs](https://developer.flutterwave.com/)

## Evidence required

A product activity map, provider eligibility checklist, test results and a list of unresolved regulatory questions. This guide is not legal advice, proof of licensing, or a substitute for reading current Kenyan law.

_Last curated: 2026-11-23; rules and provider policies can change._
