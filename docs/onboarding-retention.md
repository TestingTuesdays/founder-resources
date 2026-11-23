# Onboarding, activation & retention

[← Resource home](../README.md) · [Release checklist](release-readiness.md)

## Why founders should care

A polished signup that never leads a user to value is a failed product journey.

## Common mistakes

- Assuming a successful demo or dashboard proves the experience works for all users.
- Ignoring errors, permission boundaries, mobile constraints and exceptional states.
- Launching without a responsible owner, observable outcome or fallback.
- Using vendor tooling without checking costs, data protection or real capabilities.

## Core test scenarios

1. **New user can reach first valuable action without a tour.** Record build/environment, expected vs actual, user impact and follow-up.
2. **Email verification delay and return flow.** Record build/environment, expected vs actual, user impact and follow-up.
3. **Skipped onboarding still has recovery path.** Record build/environment, expected vs actual, user impact and follow-up.
4. **Invite teammate and resume after interruption.** Record build/environment, expected vs actual, user impact and follow-up.
5. **Uninstall/inactivity and return path.** Record build/environment, expected vs actual, user impact and follow-up.
6. **Measure activation cohort, not just installs.** Record build/environment, expected vs actual, user impact and follow-up.

## Practical workflow

1. Identify the most important user task and a measurable success criterion.
2. Use safe synthetic data and a representative device/locale/account.
3. Test the expected route **and** failure/recovery case; observe results, not assumptions.
4. Check privacy/security, accessibility and reliability considerations where relevant.
5. File a reproducible issue, assign an owner and retest after the deployed fix.

## Trusted tools and reference material

| Reference | What it helps with |
| --- | --- |
| [PostHog](https://posthog.com/) | Activation funnel |
| [Amplitude](https://amplitude.com/) | Cohort analysis |
| [Mixpanel](https://mixpanel.com/) | Product funnels |
| [GOV.UK Service Manual](https://www.gov.uk/service-manual) | Accessible service design |

## Go/no-go consideration

Do not call this area ready if the core journey can cause loss of data, money, privacy or user access without a documented safe recovery path. Regulations and provider requirements change: review official documentation for your specific product and market.

_Last curated: 2026-11-23._
