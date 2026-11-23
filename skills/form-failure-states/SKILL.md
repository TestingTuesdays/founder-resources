---
name: form-failure-states
description: Audit accessible forms and file uploads for founders and reviewers working with authorized product environments.
---

# Audit accessible forms and file uploads

[← All skills](../README.md) · [Topic guide](../../docs/forms-validation.md) · [Report template](../../templates/test-case.md)

## Goal

Produce evidence that a founder can use to decide whether a specific change is ready to ship.

## Inputs

Versioned product build, target user task, relevant official documentation, fictional test accounts, authorization to test, pass/fail criterion and accountable reviewer.

## Procedure

1. List fields, helper text, validation rules and protected server operations.
2. Try missing/invalid/very long and international input.
3. Use keyboard and screen reader to trigger and resolve errors.
4. Simulate network loss, expiration and duplicate submit.
5. Validate uploads for size/type/access controls in sandbox.
6. Retest after fixes and verify user input preservation.

## Done when

Form QA matrix covering errors, access, network and inclusive input.

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
