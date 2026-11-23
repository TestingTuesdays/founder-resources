---
name: feature-flag-rollout
description: Run a safe feature-flag and canary release for founders and reviewers working with authorized product environments.
---

# Run a safe feature-flag and canary release

[← All skills](../README.md) · [Topic guide](../../docs/feature-flags-experiments.md) · [Report template](../../templates/test-case.md)

## Goal

Produce evidence that a founder can use to decide whether a specific change is ready to ship.

## Inputs

Versioned product build, target user task, relevant official documentation, fictional test accounts, authorization to test, pass/fail criterion and accountable reviewer.

## Procedure

1. Define eligible cohort, owner, exposure goal, metric and rollback trigger.
2. Verify backend and UI both enforce off-state for ineligible users.
3. Use staging to rehearse flag provider outage and stale cache.
4. Start narrow exposure and monitor core task, error rate and cost.
5. Activate kill switch in rehearsal, verify state and cleanup.
6. Document rollout decision and owner for flag removal.

## Done when

Feature flag roll-out plan with tested kill switch, metric and cleanup date.

## Record

| Field | Required evidence |
| --- | --- |
| Task and risk | Why a failure would matter |
| Environment | Build, device, locale, test identity, feature flag |
| Steps | Exact reproducible actions |
| Expected / actual | Observable behavior, not guesswork |
| Severity and owner | Realistic impact and next action |
| Fix and retest | Deployed version, same task, changed outcome |

## Safety and limitations

Use synthetic identities/data in permissioned environments. Never scan or stress unowned systems, expose secrets or publish customer/participant recordings. A proposed test is not a passed test; always differentiate performed work from guidance. Escalate security, safety or regulated-product blockers for independent review.
