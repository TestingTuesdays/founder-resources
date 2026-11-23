# Kenya data protection, ODPC and consent

[← Kenya hub](README.md) · [App-type playbooks](../app-types/README.md) · [Testing template](../templates/test-case.md)

Kenyan personal-data obligations depend on processing, controllers/processors and sector.

## Founder considerations

- Map collection, storage, processing purpose, retention, vendors and international transfers.
- Review the Data Protection Act 2019 and current ODPC guidance; registration/notification obligations may apply depending on activities and thresholds.
- Avoid asserting consent is the only lawful basis; choose and document the appropriate basis with qualified review.
- Treat health, children, biometrics and financial records as higher-risk; check applicable safeguards.

## Minimum tests

1. **User can see privacy notice before data collection.** Record expected/actual result, build, affected user, severity, owner and retest.
2. **Withdraw marketing consent without disabling essential service.** Record expected/actual result, build, affected user, severity, owner and retest.
3. **Unauthorized user cannot access records.** Record expected/actual result, build, affected user, severity, owner and retest.
4. **Export/deletion requests follow documented process.** Record expected/actual result, build, affected user, severity, owner and retest.
5. **Processor and cross-border transfers have recorded safeguards.** Record expected/actual result, build, affected user, severity, owner and retest.
6. **Breach escalation owner and incident log exist.** Record expected/actual result, build, affected user, severity, owner and retest.

## Implementation and compliance workflow

1. Document the legal entity, target users, product activities, payment/data flows and provider contracts.
2. Consult current primary regulator and provider documentation; do not infer eligibility from a sandbox API key.
3. Identify the relevant permission, registration, licensing, contract or tax question; record it as **unverified** until confirmed.
4. Run tests on synthetic accounts, sandbox payments and representative Kenyan devices/networks.
5. Get appropriate qualified local legal/accounting/sector review for obligations and approvals.
6. Fix high-risk issues, version the release and retest the affected user journey.

## Primary starting points

- [ODPC](https://www.odpc.go.ke/)
- [Kenya Law](https://new.kenyalaw.org/)
- [Office of the Attorney General](https://www.statelaw.go.ke/)

## Evidence required

A product activity map, provider eligibility checklist, test results and a list of unresolved regulatory questions. This guide is not legal advice, proof of licensing, or a substitute for reading current Kenyan law.

_Last curated: 2026-11-23; rules and provider policies can change._
