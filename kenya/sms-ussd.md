# Kenya SMS, USSD and communications product QA

[← Kenya hub](README.md) · [App-type playbooks](../app-types/README.md) · [Testing template](../templates/test-case.md)

Feature-phone access and messaging can improve reach, but shortcode and carrier approval are not automatic.

## Founder considerations

- Confirm SMS sender ID, short code, USSD access and aggregation terms with the chosen operator/aggregator.
- Consent and marketing preferences must be appropriate to message purpose and applicable law.
- Do not assume an international SMS provider has identical sender support or delivery guarantees in Kenya.
- Design concise, clear, language-aware messages and fallback when delivery fails.

## Minimum tests

1. **USSD session timeout and resume.** Record expected/actual result, build, affected user, severity, owner and retest.
2. **SMS delivered late, duplicated or failed.** Record expected/actual result, build, affected user, severity, owner and retest.
3. **Opt-out respected.** Record expected/actual result, build, affected user, severity, owner and retest.
4. **Wrong number or recycled number privacy.** Record expected/actual result, build, affected user, severity, owner and retest.
5. **Short code unprovisioned on a carrier.** Record expected/actual result, build, affected user, severity, owner and retest.
6. **Delivery receipt does not imply user read message.** Record expected/actual result, build, affected user, severity, owner and retest.

## Implementation and compliance workflow

1. Document the legal entity, target users, product activities, payment/data flows and provider contracts.
2. Consult current primary regulator and provider documentation; do not infer eligibility from a sandbox API key.
3. Identify the relevant permission, registration, licensing, contract or tax question; record it as **unverified** until confirmed.
4. Run tests on synthetic accounts, sandbox payments and representative Kenyan devices/networks.
5. Get appropriate qualified local legal/accounting/sector review for obligations and approvals.
6. Fix high-risk issues, version the release and retest the affected user journey.

## Primary starting points

- [Safaricom developer portal](https://developer.safaricom.co.ke/)
- [Communications Authority of Kenya](https://www.ca.go.ke/)
- [ODPC](https://www.odpc.go.ke/)

## Evidence required

A product activity map, provider eligibility checklist, test results and a list of unresolved regulatory questions. This guide is not legal advice, proof of licensing, or a substitute for reading current Kenyan law.

_Last curated: 2026-11-23; rules and provider policies can change._
