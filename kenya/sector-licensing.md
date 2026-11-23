# Kenya sector regulator discovery checklist

[← Kenya hub](README.md) · [App-type playbooks](../app-types/README.md) · [Testing template](../templates/test-case.md)

Transport, utilities, education, health, finance and telecoms may require different permissions.

## Founder considerations

- Define precisely what the product does, who pays, who holds funds, who makes decisions and who owns physical operations.
- Identify relevant regulator and published licensing category before promising compliance.
- Check county permits or local operational requirements where relevant.
- Record qualified review and evidence; software testing alone cannot grant a license.

## Minimum tests

1. **Service description matches actual regulated function.** Record expected/actual result, build, affected user, severity, owner and retest.
2. **Required permits/approvals are not claimed without evidence.** Record expected/actual result, build, affected user, severity, owner and retest.
3. **Safety escalation owner assigned.** Record expected/actual result, build, affected user, severity, owner and retest.
4. **Provider terms match actual entity and market.** Record expected/actual result, build, affected user, severity, owner and retest.

## Implementation and compliance workflow

1. Document the legal entity, target users, product activities, payment/data flows and provider contracts.
2. Consult current primary regulator and provider documentation; do not infer eligibility from a sandbox API key.
3. Identify the relevant permission, registration, licensing, contract or tax question; record it as **unverified** until confirmed.
4. Run tests on synthetic accounts, sandbox payments and representative Kenyan devices/networks.
5. Get appropriate qualified local legal/accounting/sector review for obligations and approvals.
6. Fix high-risk issues, version the release and retest the affected user journey.

## Primary starting points

- [Kenya Law](https://new.kenyalaw.org/)
- [CBK](https://www.centralbank.go.ke/)
- [CA Kenya](https://www.ca.go.ke/)
- [EPRA](https://www.epra.go.ke/)
- [NTSA](https://www.ntsa.go.ke/)

## Evidence required

A product activity map, provider eligibility checklist, test results and a list of unresolved regulatory questions. This guide is not legal advice, proof of licensing, or a substitute for reading current Kenyan law.

_Last curated: 2026-11-23; rules and provider policies can change._
