# Water and energy utilities — practical founder testing playbook

[← All app types](README.md) · [Kenya hub](../kenya/README.md) · [Reusable skill](../skills/app-energy-water-iot-deep-dive/SKILL.md)

## Outcome to protect

**Meter state, field safety, billing and data provenance.** Sensor readings are not inherently trustworthy and delayed uploads can double-charge customers.

## Critical user journeys

| Journey | Success condition | Common failure |
| --- | --- | --- |
| First use | A target user completes the primary task without coaching | Unclear CTA, missing permission or confusing form |
| Core transaction | Exactly one authorized logical operation is recorded | Duplicate, stale or cross-user state |
| Failure and recovery | User sees truthful status and a safe retry path | Silent data loss or false success |
| Support and dispute | User can find the status, evidence and next action | Untraceable case or inaccessible support |

## Executable-style acceptance scenarios

- **Authorization and event replay:** Given a meter transmits the same reading twice, when ingestion runs, then usage is counted once and raw events remain auditable.
- **Concurrency or offline recovery:** Given a meter is offline for 48 hours, when restored, then missing intervals and estimated usage are visibly distinguished.
- **Safety and truthfulness:** Given a technician account is revoked, when it sends a configuration change, then device/backend rejects it.

## Test environment and fixtures

Use two fictional organizations or households, a new user and returning user, a revoked role, synthetic records, a sandbox payment where applicable, slow mobile data, and an older Android phone. Seed predictable identifiers and reset state after each attempt. Do not use real customer records.

## Failure matrix

- **Meter replay:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **tamper event:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **offline estimate:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **bill dispute:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **technician authorization:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.

## Kenya deployment questions

WASREB/EPRA and county operational requirements as applicable. Check whether your **actual activity** requires a license, contract, approval or qualified review; do not assume the category itself determines obligations. Test KES formatting, +254 and international numbers, Africa/Nairobi dates, Kiswahili and English content where relevant, shared-device privacy and intermittent connectivity.

## Primary references

- [WASREB](https://wasreb.go.ke/)
- [EPRA](https://www.epra.go.ke/)

## Release gate and evidence

**Block release** for unauthorized access, unreconciled money, unsafe advice, lost critical records or a blocked core task. Report build, scenario ID, preconditions, expected/actual result, severity, redacted evidence, owner, fix and retest. Record *not attempted* honestly.

[Copyable test case](../templates/test-case.md) · [Founder QA scorecard](../templates/founder-scorecard.md).
