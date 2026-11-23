---
name: visual-diff
description: Run a visual regression and reflow audit for founders and reviewers working with authorized product environments.
---

# Run a visual regression and reflow audit

[← All skills](../README.md) · [Topic guide](../../docs/visual-regression.md) · [Report template](../../templates/test-case.md)

## Goal

Produce evidence that a founder can use to decide whether a specific change is ready to ship.

## Inputs

Versioned product build, target user task, relevant official documentation, fictional test accounts, authorization to test, pass/fail criterion and accountable reviewer.

## Procedure

1. Choose critical screens and consistent screenshots at mobile/tablet/desktop sizes.
2. Capture loading/error/empty/long-content and dark/light states.
3. Check zoom, keyboard focus, translations and modal overflow.
4. Compare against approved baseline; classify intentional vs unintended changes.
5. Log reproducible visual defects with dimensions, browser and severity.
6. Retest corrected build and update baseline only with approval.

## Done when

Reviewed visual diff register plus accessible reflow results.

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
