---
name: retest-and-release
description: Verify a deployed change actually improved a user's task.
---

# Ship and retest

[← Skills](../README.md) · [Topic guide](../../docs/release-readiness.md)

## Objective

Verify a deployed change actually improved a user's task.

## Required inputs

Original observation, test scenario, fix/build link, same environment where possible.

## Procedure

1. Write pre-fix observed outcome and exact task.
2. Inspect deployed build ID and changelog.
3. Re-run comparable task without coaching.
4. Compare outcomes: improved, unchanged, worse or pending.
5. Check new regressions and accessibility impact.
6. Link evidence and decide close/reopen/follow-up.

## Done when

Retest record showing observed outcome—not merely merged PR.

## Safety and evidence

Use permissioned systems and synthetic data. Obtain research consent where applicable, redact personal information, preserve actual vs expected outcomes, and never state a check passed without running it. Human review remains necessary for high-risk conclusions.

## Copyable records

[Bug report](../../templates/bug-report.md) · [Testing session](../../templates/usability-session.md) · [Retest](../../templates/retest.md).
