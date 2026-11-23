---
name: authz-matrix
description: Test identity, roles and cross-tenant access for founders and reviewers working with authorized product environments.
---

# Test identity, roles and cross-tenant access

[← All skills](../README.md) · [Topic guide](../../docs/authentication-authorization.md) · [Report template](../../templates/test-case.md)

## Goal

Produce evidence that a founder can use to decide whether a specific change is ready to ship.

## Inputs

Versioned product build, target user task, relevant official documentation, fictional test accounts, authorization to test, pass/fail criterion and accountable reviewer.

## Procedure

1. Define roles and resources, including owner, member, guest, removed member and system admin.
2. Build a matrix of read/write/export/delete permissions for each resource.
3. Create synthetic accounts in at least two isolated organizations.
4. Attempt each authorized and denied action through actual API, not only UI.
5. Revoke a user and replay old session, share link and export request.
6. File any leak or privilege escalation as a release blocker.

## Done when

Completed role-permission matrix with denied/allowed evidence and no sensitive data in logs.

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
