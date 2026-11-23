---
name: content-review
description: Review docs and claims before public publication for founders and reviewers working with authorized product environments.
---

# Review docs and claims before public publication

[← All skills](../README.md) · [Topic guide](../../docs/content-cms-quality.md) · [Report template](../../templates/test-case.md)

## Goal

Produce evidence that a founder can use to decide whether a specific change is ready to ship.

## Inputs

Versioned product build, target user task, relevant official documentation, fictional test accounts, authorization to test, pass/fail criterion and accountable reviewer.

## Procedure

1. Inventory changed docs and critical claims.
2. Check each significant fact against dated primary sources.
3. Verify local links, titles, alt text, metadata and reading order.
4. Check personal information, rights/licensing and accidental secret exposure.
5. Preview on phone and with keyboard navigation.
6. Publish versioned change, record reviewer and retest corrected links.

## Done when

Editorial checklist with provenance, source dates and link verification.

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
