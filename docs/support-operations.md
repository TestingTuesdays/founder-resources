# Support, incidents & feedback loops

[← Resource home](../README.md) · [Release checklist](release-readiness.md)

## Why founders should care

User trust depends on what happens when products fail after launch.

## Common mistakes

- Assuming a successful demo or dashboard proves the experience works for all users.
- Ignoring errors, permission boundaries, mobile constraints and exceptional states.
- Launching without a responsible owner, observable outcome or fallback.
- Using vendor tooling without checking costs, data protection or real capabilities.

## Core test scenarios

1. **Support request gets acknowledgement and classification.** Record build/environment, expected vs actual, user impact and follow-up.
2. **Critical data/privacy report routes to responsible owner.** Record build/environment, expected vs actual, user impact and follow-up.
3. **Issue status and next update communicated truthfully.** Record build/environment, expected vs actual, user impact and follow-up.
4. **Status page accurately reflects degraded service.** Record build/environment, expected vs actual, user impact and follow-up.
5. **Withdrawal/deletion request follows documented process.** Record build/environment, expected vs actual, user impact and follow-up.
6. **Resolved ticket rechecked with user/QA evidence.** Record build/environment, expected vs actual, user impact and follow-up.

## Practical workflow

1. Identify the most important user task and a measurable success criterion.
2. Use safe synthetic data and a representative device/locale/account.
3. Test the expected route **and** failure/recovery case; observe results, not assumptions.
4. Check privacy/security, accessibility and reliability considerations where relevant.
5. File a reproducible issue, assign an owner and retest after the deployed fix.

## Trusted tools and reference material

| Reference | What it helps with |
| --- | --- |
| [Atlassian incident handbook](https://www.atlassian.com/incident-management) | Incident practice |
| [GitHub Issues](https://docs.github.com/en/issues) | Issue tracking |
| [Sentry](https://sentry.io/) | Error evidence |
| [Better Stack](https://betterstack.com/) | Status/incident tools |

## Go/no-go consideration

Do not call this area ready if the core journey can cause loss of data, money, privacy or user access without a documented safe recovery path. Regulations and provider requirements change: review official documentation for your specific product and market.

_Last curated: 2026-11-23._
