# Forms, validation, uploads and accessible errors

[← Founder resources](../README.md) · [Test cases](test-case-catalog.md) · [Templates](../templates/README.md)

## Who this is for

Every founder using onboarding, checkout, intake or administrative forms.

## Why it matters

Forms can silently lose data, mislabel errors, reject international names or fail for assistive technology.

## Frequent mistakes

- Using placeholder text as the only label.
- Discarding entries after an error or expired session.
- Assuming all names and addresses fit one-country formats.
- Accepting unsafe uploads or files without limits.

## Test scenarios

1. **Required and optional fields are clear to screen reader and sighted user.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
2. **Long names, diacritics, phone formats and copy-paste work.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
3. **Invalid input preserves other answers and announces corrective error.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
4. **Slow double submit creates one record.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
5. **Upload rejects unsupported type/size safely without exposing file content.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
6. **Form submitted after network drop has retry/idempotency status.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.

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
| [W3C Forms tutorial](https://www.w3.org/WAI/tutorials/forms/) | Primary documentation and implementation patterns |
| [MDN forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms) | Primary documentation and implementation patterns |
| [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) | Primary documentation and implementation patterns |

## Expected deliverable

Form field specification, accessible failure-state report and high-risk regression tests.

**Do:** keep assumptions and evidence separate, disclose uncertainty and verify current rules before release. **Don't:** imply testing coverage beyond what was executed, or expose real users and assets to experiments without permission.

_Last edited: 2026-11-23. External policies and tool capabilities can change._
