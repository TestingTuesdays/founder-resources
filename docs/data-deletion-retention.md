# Account deletion, retention and data export

[← Founder resources](../README.md) · [Test cases](test-case-catalog.md) · [Templates](../templates/README.md)

## Who this is for

Apps storing user identity, conversations, payments, health or other personal data.

## Why it matters

Promises in the privacy policy must match what storage, logs, backups, exports and connected vendors actually do.

## Frequent mistakes

- Removing the UI account but leaving active sessions and publicly accessible files.
- Claiming immediate backup deletion when backups persist by schedule.
- Skipping processors and third-party integrations.
- Exporting data without authorizing the request.

## Test scenarios

1. **Authenticated user can request export/deletion via documented path.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
2. **Other user cannot export or delete someone else's account.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
3. **Session and tokens are revoked as intended after deletion.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
4. **Retention policy covers logs, backups and third parties with honest timing.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
5. **Deletion request status and failures are visible to an authorized owner.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
6. **Consent withdrawal does not leave prohibited analytics collection active.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.

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
| [ICO guidance](https://ico.org.uk/for-organisations/) | Primary documentation and implementation patterns |
| [EU GDPR overview](https://commission.europa.eu/law/law-topic/data-protection_en) | Primary documentation and implementation patterns |
| [OWASP Privacy Risks](https://owasp.org/www-project-top-10-privacy-risks/) | Primary documentation and implementation patterns |
| [Apple Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) | Primary documentation and implementation patterns |

## Expected deliverable

Data map, retention schedule, access-control tests and verified user request workflow.

**Do:** keep assumptions and evidence separate, disclose uncertainty and verify current rules before release. **Don't:** imply testing coverage beyond what was executed, or expose real users and assets to experiments without permission.

_Last edited: 2026-11-23. External policies and tool capabilities can change._
