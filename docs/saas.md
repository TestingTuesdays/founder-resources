# SaaS subscriptions & B2B operations

[← Resource home](../README.md) · [Test catalog](test-case-catalog.md) · [Report a bug](../templates/bug-report.md)

## Why this matters

Make signup, teams, entitlements, billing and account lifecycle reliable.

## Typical founder mistakes

- Granting team permissions based solely on client state
- Not testing downgrade/cancellation effective dates
- Processing repeated billing webhooks twice
- Having no clear data export/deletion or support workflow

## Run these tests

1. **Invite, remove and demote workspace users.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
2. **Team A cannot access Team B even through guessed IDs.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
3. **Trial expiration and reactivation.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
4. **Payment failure, refund, disputed payment and invoice retrieval.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
5. **Duplicate/out-of-order webhook delivery.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
6. **Upgrade, downgrade, proration and cancellation.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
7. **Account export and deletion with correct permissions.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.

## Recommended workflow

Diagram the complete subscription and organization lifecycle before implementing. Use server-side entitlements and idempotent billing handlers. Test payment flows with official sandboxes and reconcile your source-of-truth state after errors.

## Tools and official references

| Resource | Use it for |
| --- | --- |
| [Stripe testing](https://docs.stripe.com/testing) | Sandbox payment scenarios |
| [Paddle developer docs](https://developer.paddle.com/) | Billing integration |
| [PostHog](https://posthog.com/) | Product analytics |
| [Amplitude](https://amplitude.com/) | Funnels and cohorts |
| [Mixpanel](https://mixpanel.com/) | Behavior analytics |
| [GrowthBook](https://www.growthbook.io/) | Feature flags/experiments |
| [Flagsmith](https://www.flagsmith.com/) | Controlled rollout |
| [Supabase docs](https://supabase.com/docs) | Backend/auth guidance |

## Do / don't

**Do:** test with representative people and devices, capture non-sensitive evidence, verify failure/recovery, assign ownership and retest the shipped fix.

**Don't:** rely solely on tool scores, copy unverified claims from a vendor, expose customer data, or call an unobserved outcome a passed test.

## Session deliverable

Bring one specific workflow, a safe build/test account, two or more reproducible observations, a severity-ranked fix list, and an agreed follow-up. [Use the session template](../templates/usability-session.md) and [retest sheet](../templates/retest.md).

_Last reviewed: 2026-11-23. Prices, support and platform rules may change._
