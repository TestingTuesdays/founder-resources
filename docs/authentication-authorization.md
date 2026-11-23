# Authentication, session security and authorization

[← Founder resources](../README.md) · [Test cases](test-case-catalog.md) · [Templates](../templates/README.md)

## Who this is for

Multi-user SaaS, communities, admin panels and apps with private records.

## Why it matters

A login screen does not prove that an authenticated user is authorized to view or modify every object.

## Frequent mistakes

- Checking roles in React but not the API.
- Allowing an invitation link to grant excessive privileges.
- Failing to revoke sessions after account compromise.
- Relying on guess-resistant object IDs instead of permission checks.

## Test scenarios

1. **Guest calls protected API endpoint and is denied without leaking records.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
2. **User A requests or modifies User B resource by ID and is denied.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
3. **Tenant A searches, exports, downloads or previews Tenant B data and is denied.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
4. **Former team member loses access after revocation, including old links and tokens.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
5. **Password reset token expiry and reuse produce safe rejection.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
6. **Session expiration mid-form has accessible recovery and no unintended data loss.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
7. **MFA recovery and device/session sign-out respect identity verification.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.

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
| [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) | Primary documentation and implementation patterns |
| [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | Primary documentation and implementation patterns |
| [OWASP API Security](https://owasp.org/projects/api-security-project) | Primary documentation and implementation patterns |
| [NIST Digital Identity Guidelines](https://pages.nist.gov/800-63-4/) | Primary documentation and implementation patterns |

## Expected deliverable

Role × action × object matrix plus test evidence, denied access logs and owner-assigned fixes.

**Do:** keep assumptions and evidence separate, disclose uncertainty and verify current rules before release. **Don't:** imply testing coverage beyond what was executed, or expose real users and assets to experiments without permission.

_Last edited: 2026-11-23. External policies and tool capabilities can change._
