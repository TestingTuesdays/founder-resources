# Notification deliverability & email reputation

[← Founder library](../README.md) · [Release readiness](release-readiness.md) · [Test-case template](../templates/test-case.md)

## When to use

Apps that rely on email verification, password reset, reminders or push.

## Most common mistake

Assuming the API accepted a message means it reached the user.

## Recommended practice

Set up SPF, DKIM and DMARC where applicable; review sender reputation and unsubscribe handling.

## Practical scenarios

1. **Send through sandbox/test recipients.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
2. **delay/bounce.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
3. **duplicate sends.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
4. **disabled notifications.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
5. **mobile rendering.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
6. **localized emails..** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.

## Founder workflow

1. Identify the primary user task, critical failure, and who will be impacted.
2. Prepare a safe sandbox, representative device/network and synthetic accounts.
3. Test normal behavior, rejection and partial failure independently.
4. Compare actual observation to documented provider or product promises.
5. Prioritize privacy, monetary, safety and blocked core-task defects.
6. Ship a reversible fix, observe the release, and retest the original task.

## Tools and primary references

| Resource | Scope |
| --- | --- |
| [Google Postmaster Tools](https://postmaster.google.com/) | Documentation or diagnostic tool |
| [Google email sender guidelines](https://support.google.com/a/answer/81126) | Documentation or diagnostic tool |
| [Twilio SendGrid docs](https://docs.sendgrid.com/) | Documentation or diagnostic tool |
| [Apple UserNotifications](https://developer.apple.com/documentation/usernotifications) | Documentation or diagnostic tool |

## Deliverable

A versioned test matrix, documented failures, assigned owners and evidence-backed retest. Tool availability, provider support and regulatory expectations can change; confirm them for your actual jurisdiction.

_Last curated: 2026-11-23._
