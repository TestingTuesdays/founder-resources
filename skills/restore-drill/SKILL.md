---
name: restore-drill
description: Conduct backup, restoration and data-integrity drill for founders and reviewers working with authorized product environments.
---

# Conduct backup, restoration and data-integrity drill

[← All skills](../README.md) · [Topic guide](../../docs/disaster-recovery.md) · [Report template](../../templates/test-case.md)

## Goal

Produce evidence that a founder can use to decide whether a specific change is ready to ship.

## Inputs

Versioned product build, target user task, relevant official documentation, fictional test accounts, authorization to test, pass/fail criterion and accountable reviewer.

## Procedure

1. Define recovery point/time targets and critical user records.
2. Take or select protected snapshot and restore in isolated test environment.
3. Compare counts, ownership, referential integrity and application tasks.
4. Measure data age and end-to-end restore time.
5. Verify recovered jobs and events do not duplicate external effects.
6. Write risks, escalation, owner and next drill.

## Done when

Measured recovery test with integrity checks and realistic RTO/RPO caveats.

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
