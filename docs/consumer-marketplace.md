# Consumer, marketplace & community products

[← Resource home](../README.md) · [Test catalog](test-case-catalog.md) · [Report a bug](../templates/bug-report.md)

## Why this matters

Support safe discovery, messaging, payments, moderation and user-generated content.

## Typical founder mistakes

- Designing only for a supply-rich marketplace
- No reporting or abuse handling for user-generated content
- Ignoring fraud, refunds and disputes
- Failing on empty search or a first-week cold start

## Run these tests

1. **Search has empty, filtered and no-location fallback states.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
2. **User reports abusive content and receives a clear next step.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
3. **Seller/provider is unavailable during checkout.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
4. **Duplicate charge or cancelled booking is reconciled.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
5. **User blocks another user and access is enforced.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
6. **Fake listings, spam and rate-limit attempts.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.

## Recommended workflow

Test both sides of every transaction, beginning with first-time supply/demand imbalance. Include human moderation, identity verification where appropriate, fraud controls and privacy-safe reporting.

## Tools and official references

| Resource | Use it for |
| --- | --- |
| [Firebase Crashlytics](https://firebase.google.com/products/crashlytics) | Client crash monitoring |
| [Sentry](https://sentry.io/) | Error monitoring |
| [PostHog](https://posthog.com/) | Activation and retention |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Abuse and security patterns |

## Do / don't

**Do:** test with representative people and devices, capture non-sensitive evidence, verify failure/recovery, assign ownership and retest the shipped fix.

**Don't:** rely solely on tool scores, copy unverified claims from a vendor, expose customer data, or call an unobserved outcome a passed test.

## Session deliverable

Bring one specific workflow, a safe build/test account, two or more reproducible observations, a severity-ranked fix list, and an agreed follow-up. [Use the session template](../templates/usability-session.md) and [retest sheet](../templates/retest.md).

_Last reviewed: 2026-11-23. Prices, support and platform rules may change._
