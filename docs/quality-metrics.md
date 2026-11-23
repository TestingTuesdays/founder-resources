# Quality metrics, defect severity and founder scorecards

[← Resource home](../README.md) · [Release gate](release-readiness.md) · [Testing templates](../templates/README.md)

## For whom

Founders tracking real product improvements without vanity quality scores.

## The failure you are trying to prevent

Product quality is about actual user outcomes, not only whether a build compiles. Verify a realistic journey and the ways it can fail, then retest after changes.

## Common mistakes

- Using lines-of-code coverage as a proxy for user quality
- Counting a merged pull request as a verified fix
- Combining attempted and not-attempted sessions
- Calling peer feedback statistically representative
- Ignoring high severity issues because their frequency is low

## Run this test plan

1. **Define task success unassisted/assisted/failed/not attempted.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
2. **Track crash-free sessions and error rate by version.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
3. **Set thresholds for P0/P1 blockers and explicit exceptions.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
4. **Measure fixed defects retested with same task and device cohort.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
5. **Monitor recurrence and new-regression rate.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
6. **Track accessibility barriers alongside performance and reliability.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.

## Working method

**Prepare:** select three high-risk tasks and a realistic device, account and permission profile. Use fictional data; do not disclose user recordings, credentials or restricted company information.

**Observe:** run both successful and failure/recovery paths. Distinguish a user's observed behavior from the researcher's proposed solution.

**Prioritize:** flag data loss, harm, exposed private information and blocked primary user actions before cosmetic problems. Record any accepted risk with an accountable owner.

**Verify:** deploy a versioned fix, repeat the same task under comparable conditions and record improved/unchanged/worse/pending outcome.

## Official documentation and useful tools

| Reference | When it helps |
| --- | --- |
| [Google HEART framework](https://research.google/pubs/heart-framework-for-measuring-user-experience/) | Primary documentation, methods or diagnostics |
| [DORA research](https://dora.dev/) | Primary documentation, methods or diagnostics |
| [Sentry](https://sentry.io/) | Primary documentation, methods or diagnostics |
| [PostHog](https://posthog.com/) | Primary documentation, methods or diagnostics |
| [Web Vitals](https://web.dev/articles/vitals) | Primary documentation, methods or diagnostics |

## Completion evidence

Weekly scorecard of attempted tasks, observed outcomes, owner-backed fixes and comparable retest results.

## Don't overclaim

A single pass does not prove all users, devices, jurisdictions or failure conditions are covered. Tool limits and external rules evolve. Recheck official sources before a regulated or commercially consequential release.

_Last curated: 2026-11-23._
