# Mobile & app-store launch

[← Resource home](../README.md) · [Test catalog](test-case-catalog.md) · [Report a bug](../templates/bug-report.md)

## Why this matters

Prepare accessible, reliable iOS/Android builds and compliant accurate store submissions.

## Typical founder mistakes

- Uploading placeholder screens or broken reviewer credentials
- Assuming permission access is always granted
- Skipping upgrades/migrations across app versions
- Treating upload success as approval or a safe release

## Run these tests

1. **Clean install on physical iOS and Android devices.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
2. **Update over previous version with local data migration.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
3. **Background, foreground, rotation and low storage.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
4. **Notifications, deep links and denied/revoked permissions.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
5. **Large font sizes, VoiceOver and TalkBack.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
6. **Store review/demo access, age rating and privacy disclosures.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
7. **Staged rollout, crash dashboard and halted rollout.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.

## Recommended workflow

Keep a store-specific checklist, test with internal/beta testers, use truthful screenshots and privacy declarations, prepare account deletion where applicable, and monitor a phased release. Store rules and eligibility requirements change; read the current official pages before submission.

## Tools and official references

| Resource | Use it for |
| --- | --- |
| [Apple Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) | Official iOS review rules |
| [App Store Connect](https://developer.apple.com/help/app-store-connect/) | Metadata and release |
| [TestFlight](https://developer.apple.com/testflight/) | iOS beta distribution |
| [Google Play Console Help](https://support.google.com/googleplay/android-developer/) | Android store policies and tracks |
| [Android quality](https://developer.android.com/quality) | Android quality guidelines |
| [Firebase App Distribution](https://firebase.google.com/docs/app-distribution) | Pre-release delivery |
| [Maestro](https://maestro.mobile.dev/) | Mobile flow automation |
| [Appium](https://appium.io/) | Cross-platform mobile automation |
| [Fastlane](https://fastlane.tools/) | Release automation |

## Do / don't

**Do:** test with representative people and devices, capture non-sensitive evidence, verify failure/recovery, assign ownership and retest the shipped fix.

**Don't:** rely solely on tool scores, copy unverified claims from a vendor, expose customer data, or call an unobserved outcome a passed test.

## Session deliverable

Bring one specific workflow, a safe build/test account, two or more reproducible observations, a severity-ranked fix list, and an agreed follow-up. [Use the session template](../templates/usability-session.md) and [retest sheet](../templates/retest.md).

_Last reviewed: 2026-11-23. Prices, support and platform rules may change._
