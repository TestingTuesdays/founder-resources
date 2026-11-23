# Kenya digital health and sensitive patient data

[← Kenya hub](README.md) · [App-type playbooks](../app-types/README.md) · [Testing template](../templates/test-case.md)

Health products may trigger additional sector, patient confidentiality and device requirements.

## Founder considerations

- Check Ministry of Health and relevant current digital health frameworks for interoperability, facility and provider requirements.
- Health data privacy, patient consent and caregiver permissions need explicit review.
- Clinical advice, diagnosis and device claims may require professional or regulatory oversight.
- Do not infer medical approval from app-store publication.

## Minimum tests

1. **Patient/caregiver role separation.** Record expected/actual result, build, affected user, severity, owner and retest.
2. **Wrong patient record access denied.** Record expected/actual result, build, affected user, severity, owner and retest.
3. **Swahili instructions clinically reviewed.** Record expected/actual result, build, affected user, severity, owner and retest.
4. **Offline sync does not mix patient records.** Record expected/actual result, build, affected user, severity, owner and retest.
5. **Emergency escalation instructions accurate and safe.** Record expected/actual result, build, affected user, severity, owner and retest.

## Implementation and compliance workflow

1. Document the legal entity, target users, product activities, payment/data flows and provider contracts.
2. Consult current primary regulator and provider documentation; do not infer eligibility from a sandbox API key.
3. Identify the relevant permission, registration, licensing, contract or tax question; record it as **unverified** until confirmed.
4. Run tests on synthetic accounts, sandbox payments and representative Kenyan devices/networks.
5. Get appropriate qualified local legal/accounting/sector review for obligations and approvals.
6. Fix high-risk issues, version the release and retest the affected user journey.

## Primary starting points

- [Kenya Ministry of Health](https://www.health.go.ke/)
- [ODPC](https://www.odpc.go.ke/)
- [Kenya Law](https://new.kenyalaw.org/)

## Evidence required

A product activity map, provider eligibility checklist, test results and a list of unresolved regulatory questions. This guide is not legal advice, proof of licensing, or a substitute for reading current Kenyan law.

_Last curated: 2026-11-23; rules and provider policies can change._
