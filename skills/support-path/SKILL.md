---
name: support-path
description: Rehearse support and incident escalation for founders and reviewers working with authorized product environments.
---

# Rehearse support and incident escalation

[← All skills](../README.md) · [Topic guide](../../docs/customer-support-qa.md) · [Report template](../../templates/test-case.md)

## Goal

Produce evidence that a founder can use to decide whether a specific change is ready to ship.

## Inputs

Versioned product build, target user task, relevant official documentation, fictional test accounts, authorization to test, pass/fail criterion and accountable reviewer.

## Procedure

1. Select password recovery, refund, privacy and outage scenarios.
2. Submit fictional support request through actual channel.
3. Verify receipt, ticket routing, priority and owner.
4. Test safe identity verification and prevent unauthorized account disclosure.
5. Check escalation and status update for serious incident.
6. Record outcome, owner and recurring product defect follow-up.

## Done when

Support journey report with secure escalation, accessible communication and tracked engineering follow-up.

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
