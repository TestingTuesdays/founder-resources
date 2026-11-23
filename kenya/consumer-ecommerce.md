# Kenya consumer protection and e-commerce launch

[← Kenya hub](README.md) · [App-type playbooks](../app-types/README.md) · [Testing template](../templates/test-case.md)

Advertising, pricing, returns and customer treatment must reflect actual checkout and delivery.

## Founder considerations

- Review Kenya Competition Authority consumer protection guidance and applicable law.
- Show clear total price, fees, KES currency, availability and delivery terms.
- Do not claim guaranteed refunds or chargeback rights unsupported by the provider and law.
- Avoid misleading scarcity, fake reviews and inaccessible cancellation.

## Minimum tests

1. **Cart shows true final amount.** Record expected/actual result, build, affected user, severity, owner and retest.
2. **Refund and failed delivery have clear status.** Record expected/actual result, build, affected user, severity, owner and retest.
3. **Cancellation request can be submitted.** Record expected/actual result, build, affected user, severity, owner and retest.
4. **Misleading stock/discount claims corrected.** Record expected/actual result, build, affected user, severity, owner and retest.
5. **Customer support accessible on mobile.** Record expected/actual result, build, affected user, severity, owner and retest.

## Implementation and compliance workflow

1. Document the legal entity, target users, product activities, payment/data flows and provider contracts.
2. Consult current primary regulator and provider documentation; do not infer eligibility from a sandbox API key.
3. Identify the relevant permission, registration, licensing, contract or tax question; record it as **unverified** until confirmed.
4. Run tests on synthetic accounts, sandbox payments and representative Kenyan devices/networks.
5. Get appropriate qualified local legal/accounting/sector review for obligations and approvals.
6. Fix high-risk issues, version the release and retest the affected user journey.

## Primary starting points

- [Competition Authority of Kenya](https://www.cak.go.ke/)
- [Kenya Law](https://new.kenyalaw.org/)
- [Safaricom Daraja](https://developer.safaricom.co.ke/)

## Evidence required

A product activity map, provider eligibility checklist, test results and a list of unresolved regulatory questions. This guide is not legal advice, proof of licensing, or a substitute for reading current Kenyan law.

_Last curated: 2026-11-23; rules and provider policies can change._
