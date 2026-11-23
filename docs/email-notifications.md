# Email, push & messaging quality

[← Resource home](../README.md) · [Release checklist](release-readiness.md)

## Why founders should care

Transactional communication can fail silently, arrive late, or disclose sensitive data.

## Common mistakes

- Assuming a successful demo or dashboard proves the experience works for all users.
- Ignoring errors, permission boundaries, mobile constraints and exceptional states.
- Launching without a responsible owner, observable outcome or fallback.
- Using vendor tooling without checking costs, data protection or real capabilities.

## Core test scenarios

1. **Password reset email arrives, expires and cannot be replayed.** Record build/environment, expected vs actual, user impact and follow-up.
2. **Unsubscribe applies to marketing not essential service notices.** Record build/environment, expected vs actual, user impact and follow-up.
3. **Duplicate event does not send duplicate notification.** Record build/environment, expected vs actual, user impact and follow-up.
4. **Email renders on mobile and with blocked images.** Record build/environment, expected vs actual, user impact and follow-up.
5. **Push permission denied and notifications deep link correctly.** Record build/environment, expected vs actual, user impact and follow-up.
6. **Template localized with user time zone.** Record build/environment, expected vs actual, user impact and follow-up.

## Practical workflow

1. Identify the most important user task and a measurable success criterion.
2. Use safe synthetic data and a representative device/locale/account.
3. Test the expected route **and** failure/recovery case; observe results, not assumptions.
4. Check privacy/security, accessibility and reliability considerations where relevant.
5. File a reproducible issue, assign an owner and retest after the deployed fix.

## Trusted tools and reference material

| Reference | What it helps with |
| --- | --- |
| [Resend docs](https://resend.com/docs) | Transactional email |
| [Mailgun docs](https://documentation.mailgun.com/) | Email delivery |
| [Google Postmaster Tools](https://postmaster.google.com/) | Sender monitoring |
| [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging) | Push messaging |
| [Apple UserNotifications](https://developer.apple.com/documentation/usernotifications) | iOS notifications |

## Go/no-go consideration

Do not call this area ready if the core journey can cause loss of data, money, privacy or user access without a documented safe recovery path. Regulations and provider requirements change: review official documentation for your specific product and market.

_Last curated: 2026-11-23._
