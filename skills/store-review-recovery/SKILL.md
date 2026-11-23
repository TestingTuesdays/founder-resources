---
name: store-review-recovery
description: Prepare app review and rejection response for founders and reviewers working with authorized product environments.
---

# Prepare app review and rejection response

[← All skills](../README.md) · [Topic guide](../../docs/app-store-rejection-recovery.md) · [Report template](../../templates/test-case.md)

## Goal

Produce evidence that a founder can use to decide whether a specific change is ready to ship.

## Inputs

Versioned product build, target user task, relevant official documentation, fictional test accounts, authorization to test, pass/fail criterion and accountable reviewer.

## Procedure

1. Record reviewer message and official guideline cited; avoid guessing cause.
2. Reproduce issue on actual submitted binary/device/locale.
3. Fix behavior or metadata and validate reviewer demo access.
4. Check app listing truthfulness, privacy labels and payment/account flows.
5. Submit a clear, factual explanation of exact change and test steps.
6. Record new review outcome and schedule follow-up if rejected.

## Done when

Versioned submission record, reviewer path and tested fix, without promising acceptance.

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
