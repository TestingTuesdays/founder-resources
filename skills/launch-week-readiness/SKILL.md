---
name: launch-week-readiness
description: Run the founder launch-week quality review through observable founder QA steps and comparable retesting.
---

# Run the founder launch-week quality review

[← Skills](../README.md) · [Guide](../../docs/founder-launch-week.md)

## Required inputs

Functional versioned build, intended user task, synthetic accounts, appropriate consent, permitted environment, named test owner and acceptance criteria.

## Procedure

1. List critical tasks, owners, version and users.
2. Verify authz, billing, mobile, accessibility and performance evidence.
3. Confirm backup, monitoring, incident escalation and rollback.
4. Run preproduction smoke tests using safe accounts.
5. Ship in an approved controlled rollout if ready.
6. Check production outcomes and retest user flows.

## Evidence required

Record build, device/context, expected and actual result, anonymized observation, severity, fix ownership and actual retest. Proposed actions are not passing tests.

## Risk and privacy limits

Do not access unowned systems, run disruptive tests without permission, reveal private research or let a founder's demonstrations count as independently validated usability.

[Issue template](../../templates/issue-triage-board.md) · [Device matrix](../../templates/qa-device-matrix.md) · [Research plan](../../templates/consent-and-research.md).
