# Support inboxes, help centers and operational quality

[← Founder resources](../README.md) · [Test cases](test-case-catalog.md) · [Templates](../templates/README.md)

## Who this is for

Founders receiving sign-in, subscription or account safety issues.

## Why it matters

The recovery experience is part of the product, not a separate afterthought.

## Frequent mistakes

- Sending password reset or personal data to unverified requesters.
- No defined urgent escalation for data/security incidents.
- Conflating customer support response time with actual resolution.
- Not turning repeating tickets into regression tests.

## Test scenarios

1. **User receives helpful receipt and safe resolution steps.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
2. **Support agent cannot access another tenant's records without authorization.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
3. **Escalation reaches proper on-call owner for critical issues.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
4. **Refund/delete requests are routed by documented policy.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
5. **Support content remains accessible and localized where needed.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
6. **Repeated issue creates linked engineering regression coverage.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.

## Founder workflow

1. Choose the top one to three real user journeys relevant to your product.
2. Prepare synthetic data and an authorized test environment. Do not share production credentials or personal records.
3. Write observable pass/fail criteria *before* executing the happy path and the failure/recovery scenarios.
4. Run the checks with appropriate devices, identities and permissions. Do not assume an automated tool proves the complete journey.
5. File reproducible defects, assign severity based on harm, fix in a versioned build and retest.
6. Decide go/no-go; block on critical privacy, money, safety, irreversible-data or core-task risks.

## Primary references and tools

| Resource | Value |
| --- | --- |
| [GOV.UK Service Manual](https://www.gov.uk/service-manual) | Primary documentation and implementation patterns |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Primary documentation and implementation patterns |
| [Atlassian incident guide](https://www.atlassian.com/incident-management) | Primary documentation and implementation patterns |

## Expected deliverable

Support workflow map, safe identity verification procedure and top recurring defects.

**Do:** keep assumptions and evidence separate, disclose uncertainty and verify current rules before release. **Don't:** imply testing coverage beyond what was executed, or expose real users and assets to experiments without permission.

_Last edited: 2026-11-23. External policies and tool capabilities can change._
