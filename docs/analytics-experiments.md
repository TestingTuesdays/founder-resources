# Analytics, growth & experiments

[← Resource home](../README.md) · [Test catalog](test-case-catalog.md) · [Report a bug](../templates/bug-report.md)

## Why this matters

Measure meaningful outcomes without misleading founders or overcollecting user data.

## Typical founder mistakes

- Tracking events with no definitions or ownership
- Confusing acquisition with activation and retention
- Reporting tiny-sample conversion changes as proven uplift
- Collecting unneeded identifiers or session recordings

## Run these tests

1. **Event triggers exactly once at the expected point.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
2. **Anonymous to authenticated identity transition does not inflate counts.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
3. **Funnel captures error/abandonment events accurately.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
4. **Consent withdrawal affects analytics collection appropriately.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
5. **Experiment assignment stays stable and metrics have guardrails.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.

## Recommended workflow

Define one north-star outcome plus guardrails, create an event dictionary, document hypothesis and sample-size assumptions before experiments and watch retention by cohorts rather than raw traffic alone.

## Tools and official references

| Resource | Use it for |
| --- | --- |
| [PostHog](https://posthog.com/) | Events, funnels and experiments |
| [Amplitude](https://amplitude.com/) | Behavior analysis |
| [Mixpanel](https://mixpanel.com/) | Product metrics |
| [Plausible](https://plausible.io/) | Lightweight web analytics |
| [Matomo](https://matomo.org/) | Self-hostable analytics |
| [GrowthBook](https://www.growthbook.io/) | Experiments and feature flags |

## Do / don't

**Do:** test with representative people and devices, capture non-sensitive evidence, verify failure/recovery, assign ownership and retest the shipped fix.

**Don't:** rely solely on tool scores, copy unverified claims from a vendor, expose customer data, or call an unobserved outcome a passed test.

## Session deliverable

Bring one specific workflow, a safe build/test account, two or more reproducible observations, a severity-ranked fix list, and an agreed follow-up. [Use the session template](../templates/usability-session.md) and [retest sheet](../templates/retest.md).

_Last reviewed: 2026-11-23. Prices, support and platform rules may change._
