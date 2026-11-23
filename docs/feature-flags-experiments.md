# Feature flags, staged rollout and rollback

[← Founder resources](../README.md) · [Test cases](test-case-catalog.md) · [Templates](../templates/README.md)

## Who this is for

Teams rolling out risky features to early cohorts.

## Why it matters

A kill switch and eligibility gate are only useful if tested before launch.

## Frequent mistakes

- Assuming hidden frontend elements secure server-only features.
- Leaving old flags and migrations indefinitely.
- Rolling out to all users without rollback metrics.
- Assigning experiments with unstable identities.

## Test scenarios

1. **Feature is truly off for unassigned accounts on backend and UI.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
2. **Flag change takes effect within documented delay.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
3. **New version has safe fallback if provider is down.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
4. **Canary users and control group are assigned consistently.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
5. **Kill switch halts risky operation with no data loss.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
6. **Metric and guardrail dashboards identify meaningful regression.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.

## Founder workflow

1. Choose the top one to three real user journeys relevant to your product.
2. Prepare synthetic data and an authorized test environment. Do not share production credentials or personal records.
3. Write observable pass/fail criteria *before* executing the happy path and the failure/recovery scenarios.
4. Run the checks with appropriate devices, identities and permissions. Do not assume an automated tool proves the complete journey.
5. File reproducible defects, assign severity based on harm, fix in a versioned build and retest.
6. Decide go/no-go; block on critical privacy, money, safety, irreversible-data or core-task risks.

## Primary references and tools

| Resource | Value |
| --- | --- |
| [OpenFeature](https://openfeature.dev/) | Primary documentation and implementation patterns |
| [GrowthBook](https://www.growthbook.io/) | Primary documentation and implementation patterns |
| [Flagsmith](https://www.flagsmith.com/) | Primary documentation and implementation patterns |
| [LaunchDarkly](https://launchdarkly.com/) | Primary documentation and implementation patterns |

## Expected deliverable

Flag ownership registry, staged exposure plan, rollback triggers and verified off-state.

**Do:** keep assumptions and evidence separate, disclose uncertainty and verify current rules before release. **Don't:** imply testing coverage beyond what was executed, or expose real users and assets to experiments without permission.

_Last edited: 2026-11-23. External policies and tool capabilities can change._
