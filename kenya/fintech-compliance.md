# Kenya fintech, lending and payment regulation discovery

[← Kenya hub](README.md) · [App-type playbooks](../app-types/README.md) · [Testing template](../templates/test-case.md)

Identify whether the business is providing regulated financial services rather than simply using a payment API.

## Founder considerations

- Check CBK rules for payment services, digital credit providers, banks and relevant licensing categories.
- Payment collection for own sales differs from holding customer funds or lending.
- KYC/AML obligations depend on activity and licensing; do not copy bank compliance checklists indiscriminately.
- If using digital credit, verify current DCP requirements, disclosures, debt collection rules and customer treatment.

## Minimum tests

1. **Product claims do not imply CBK authorization unless confirmed.** Record expected/actual result, build, affected user, severity, owner and retest.
2. **Credit pricing and repayment disclosures match contract.** Record expected/actual result, build, affected user, severity, owner and retest.
3. **Sensitive identity documents restricted by role.** Record expected/actual result, build, affected user, severity, owner and retest.
4. **Refund, reversal and disputed transaction traceable.** Record expected/actual result, build, affected user, severity, owner and retest.
5. **Customer complaints and fraud escalation documented.** Record expected/actual result, build, affected user, severity, owner and retest.

## Implementation and compliance workflow

1. Document the legal entity, target users, product activities, payment/data flows and provider contracts.
2. Consult current primary regulator and provider documentation; do not infer eligibility from a sandbox API key.
3. Identify the relevant permission, registration, licensing, contract or tax question; record it as **unverified** until confirmed.
4. Run tests on synthetic accounts, sandbox payments and representative Kenyan devices/networks.
5. Get appropriate qualified local legal/accounting/sector review for obligations and approvals.
6. Fix high-risk issues, version the release and retest the affected user journey.

## Primary starting points

- [Central Bank of Kenya](https://www.centralbank.go.ke/)
- [Financial Reporting Centre](https://www.frc.go.ke/)
- [Kenya Law](https://new.kenyalaw.org/)

## Evidence required

A product activity map, provider eligibility checklist, test results and a list of unresolved regulatory questions. This guide is not legal advice, proof of licensing, or a substitute for reading current Kenyan law.

_Last curated: 2026-11-23; rules and provider policies can change._
