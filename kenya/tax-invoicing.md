# Kenya tax, KRA and eTIMS readiness

[← Kenya hub](README.md) · [App-type playbooks](../app-types/README.md) · [Testing template](../templates/test-case.md)

Tax registration, invoicing and digital service obligations vary by business and current law.

## Founder considerations

- Check KRA's current eTIMS, VAT, income tax and relevant electronic invoicing guidance for your legal entity.
- Do not assume every founder or invoice has the same obligation or tax rate.
- Reconcile invoice totals, refunds and payment receipts; keep tax identifiers private.
- Use a qualified Kenyan accountant for tax classification, deadlines and eTIMS integration requirements.

## Minimum tests

1. **Invoice generated for completed sale.** Record expected/actual result, build, affected user, severity, owner and retest.
2. **Cancelled/refunded sale reconciles without duplicate revenue.** Record expected/actual result, build, affected user, severity, owner and retest.
3. **KES rounding and tax calculation consistent.** Record expected/actual result, build, affected user, severity, owner and retest.
4. **Invoice fields and records retained as required.** Record expected/actual result, build, affected user, severity, owner and retest.
5. **Offline issuance or provider outage has safe recovery.** Record expected/actual result, build, affected user, severity, owner and retest.

## Implementation and compliance workflow

1. Document the legal entity, target users, product activities, payment/data flows and provider contracts.
2. Consult current primary regulator and provider documentation; do not infer eligibility from a sandbox API key.
3. Identify the relevant permission, registration, licensing, contract or tax question; record it as **unverified** until confirmed.
4. Run tests on synthetic accounts, sandbox payments and representative Kenyan devices/networks.
5. Get appropriate qualified local legal/accounting/sector review for obligations and approvals.
6. Fix high-risk issues, version the release and retest the affected user journey.

## Primary starting points

- [Kenya Revenue Authority](https://www.kra.go.ke/)
- [Kenya Law](https://new.kenyalaw.org/)

## Evidence required

A product activity map, provider eligibility checklist, test results and a list of unresolved regulatory questions. This guide is not legal advice, proof of licensing, or a substitute for reading current Kenyan law.

_Last curated: 2026-11-23; rules and provider policies can change._
