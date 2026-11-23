---
name: error-state-inventory
description: Audit recovery and error-state experience through observable founder QA steps and comparable retesting.
---

# Audit recovery and error-state experience

[← Skills](../README.md) · [Guide](../../docs/error-states-library.md)

## Required inputs

Functional versioned build, intended user task, synthetic accounts, appropriate consent, permitted environment, named test owner and acceptance criteria.

## Procedure

1. Inventory primary workflows and error/empty/loading/offline states.
2. Trigger each state in an authorized environment.
3. Check plain-language explanation and accessible focus/status.
4. Ensure no secret, cross-user information or stack trace is leaked.
5. Verify data preservation, retries and idempotency.
6. File issues and retest on versioned build.

## Evidence required

Record build, device/context, expected and actual result, anonymized observation, severity, fix ownership and actual retest. Proposed actions are not passing tests.

## Risk and privacy limits

Do not access unowned systems, run disruptive tests without permission, reveal private research or let a founder's demonstrations count as independently validated usability.

[Issue template](../../templates/issue-triage-board.md) · [Device matrix](../../templates/qa-device-matrix.md) · [Research plan](../../templates/consent-and-research.md).
