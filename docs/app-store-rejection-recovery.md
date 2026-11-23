# App-store rejection, appeals and resubmission

[← Founder resources](../README.md) · [Test cases](test-case-catalog.md) · [Templates](../templates/README.md)

## Who this is for

Founders distributing through App Store and Google Play.

## Why it matters

Review requires a working app, truthful metadata, review access, current policy understanding and a clear resubmission process.

## Frequent mistakes

- Resubmitting unchanged builds without addressing reviewer evidence.
- Using test credentials that require unavailable OTP/device.
- Submitting placeholder content or unsupported marketing claims.
- Assuming a rejection means the entire business model is banned.

## Test scenarios

1. **Reviewer can access every relevant paid/locked feature via safe demo mode.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
2. **Privacy/data declarations match actual SDKs and permissions.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
3. **Description/screenshots show the same real capabilities as reviewed binary.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
4. **Delete-account path and subscription disclosures work where required.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
5. **Rejected issue is reproducible and fixed in a new version with notes.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
6. **Support contact, public URLs and backend stay live during review.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.

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
| [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) | Primary documentation and implementation patterns |
| [App Store Connect help](https://developer.apple.com/help/app-store-connect/) | Primary documentation and implementation patterns |
| [Google Play Console Help](https://support.google.com/googleplay/android-developer/) | Primary documentation and implementation patterns |
| [Android app quality](https://developer.android.com/quality) | Primary documentation and implementation patterns |

## Expected deliverable

Reviewer checklist, issue-to-fix mapping, new-build notes and documented next review outcome.

**Do:** keep assumptions and evidence separate, disclose uncertainty and verify current rules before release. **Don't:** imply testing coverage beyond what was executed, or expose real users and assets to experiments without permission.

_Last edited: 2026-11-23. External policies and tool capabilities can change._
