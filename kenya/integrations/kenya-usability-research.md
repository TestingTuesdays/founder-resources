# Kenya field research, older Android and language testing

[← Kenya hub](../README.md) · [Integration index](README.md) · [Test case template](../../templates/test-case.md)

## Why this matters

Urban Nairobi, rural counties and diaspora users may have very different devices, languages and connectivity.

## Step-by-step founder workflow

1. Recruit participants based on actual task and context rather than assumed demographics.
2. Test English/Kiswahili wording and any other required language with fluent reviewers.
3. Use a representative low-memory Android device and slow/unstable mobile network.
4. Test shared devices, low storage, power interruption and mobile-money prompt switching.
5. Verify phone formats, KES display, location uncertainty and accessible errors.
6. Record unassisted completion, failed tasks and compensation/consent.
7. Retest improvements with matched task and network conditions.

## Required test evidence

| Scenario | Expected state | Actual result | Severity | Owner / retest |
| --- | --- | --- | --- | --- |
| Successful authorized path | Documented expected outcome | Not run | | |
| Provider/network timeout | Safe retry or pending | Not run | | |
| Duplicate event/request | One logical outcome | Not run | | |
| Unauthorized or malformed input | Safely denied | Not run | | |
| Reversal/cleanup where relevant | Consistent records | Not run | | |

## Official starting points

- [W3C WAI](https://www.w3.org/WAI/)
- [W3C Internationalization](https://www.w3.org/International/)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/network/)

**Scope:** this is a test and implementation planning guide, not a live integration, guaranteed merchant onboarding, regulatory certification or legal/tax advice. Provider contracts, credentials, callbacks and current rules must be verified for the actual account.

_Last curated: 2026-11-23._
