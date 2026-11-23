# Events and ticketing — practical founder testing playbook

[← All app types](README.md) · [Kenya hub](../kenya/README.md) · [Reusable skill](../skills/app-ticketing-events-deep-dive/SKILL.md)

## Outcome to protect

**Inventory, payments, offline gates and refunds.** Offline QR scanning and delayed payment confirmation can admit more guests than paid capacity.

## Critical user journeys

| Journey | Success condition | Common failure |
| --- | --- | --- |
| First use | A target user completes the primary task without coaching | Unclear CTA, missing permission or confusing form |
| Core transaction | Exactly one authorized logical operation is recorded | Duplicate, stale or cross-user state |
| Failure and recovery | User sees truthful status and a safe retry path | Silent data loss or false success |
| Support and dispute | User can find the status, evidence and next action | Untraceable case or inaccessible support |

## Executable-style acceptance scenarios

- **Authorization and event replay:** Given one seat and two simultaneous checkout attempts, when both submit, then only one reservation can be confirmed.
- **Concurrency or offline recovery:** Given a QR ticket already scanned on another offline gate, when syncing, then duplicate detection and dispute workflow are explicit.
- **Safety and truthfulness:** Given an M-Pesa payment pending, when gate staff search ticket, then status cannot be falsely represented as paid.

## Test environment and fixtures

Use two fictional organizations or households, a new user and returning user, a revoked role, synthetic records, a sandbox payment where applicable, slow mobile data, and an older Android phone. Seed predictable identifiers and reset state after each attempt. Do not use real customer records.

## Failure matrix

- **Seat race:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **duplicate QR:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **late payment:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **refunds:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **accessible check-in:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.

## Kenya deployment questions

Local event permits and merchant terms as applicable. Check whether your **actual activity** requires a license, contract, approval or qualified review; do not assume the category itself determines obligations. Test KES formatting, +254 and international numbers, Africa/Nairobi dates, Kiswahili and English content where relevant, shared-device privacy and intermittent connectivity.

## Primary references

- [Safaricom Daraja](https://developer.safaricom.co.ke/)
- [OWASP ASVS](https://asvs.owasp.org/)

## Release gate and evidence

**Block release** for unauthorized access, unreconciled money, unsafe advice, lost critical records or a blocked core task. Report build, scenario ID, preconditions, expected/actual result, severity, redacted evidence, owner, fix and retest. Record *not attempted* honestly.

[Copyable test case](../templates/test-case.md) · [Founder QA scorecard](../templates/founder-scorecard.md).
