---
name: account-deletion
description: Audit privacy, export and account deletion for founders and reviewers working with authorized product environments.
---

# Audit privacy, export and account deletion

[← All skills](../README.md) · [Topic guide](../../docs/data-deletion-retention.md) · [Report template](../../templates/test-case.md)

## Goal

Produce evidence that a founder can use to decide whether a specific change is ready to ship.

## Inputs

Versioned product build, target user task, relevant official documentation, fictional test accounts, authorization to test, pass/fail criterion and accountable reviewer.

## Procedure

1. Inventory storage, analytics, logs, backups and third-party processors.
2. Run authorized export and deletion using synthetic accounts.
3. Attempt another user's request and confirm denial.
4. Verify sessions, public files and connected token access are treated correctly.
5. Compare published timeline and retained data with actual implementation.
6. Document unresolved retention obligations and review with qualified owner.

## Done when

Request lifecycle map with specific deletion/export evidence and honest policy notes.

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
