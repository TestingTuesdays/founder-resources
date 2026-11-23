# Agriculture and farmer services — practical founder testing playbook

[← All app types](README.md) · [Kenya hub](../kenya/README.md) · [Reusable skill](../skills/app-agritech-deep-dive/SKILL.md)

## Outcome to protect

**Advice freshness, units, field connectivity and payment trust.** Stale or location-mismatched advice can materially harm farmers.

## Critical user journeys

| Journey | Success condition | Common failure |
| --- | --- | --- |
| First use | A target user completes the primary task without coaching | Unclear CTA, missing permission or confusing form |
| Core transaction | Exactly one authorized logical operation is recorded | Duplicate, stale or cross-user state |
| Failure and recovery | User sees truthful status and a safe retry path | Silent data loss or false success |
| Support and dispute | User can find the status, evidence and next action | Untraceable case or inaccessible support |

## Executable-style acceptance scenarios

- **Authorization and event replay:** Given a weather advisory older than its supported validity, when displayed, then timestamp and uncertainty are prominent.
- **Concurrency or offline recovery:** Given a farmer enters kilograms, when converting units and prices, then displayed amount matches the recorded contract and currency.
- **Safety and truthfulness:** Given offline field collection, when two agents sync edits, then conflicts are resolved without silently overwriting observations.

## Test environment and fixtures

Use two fictional organizations or households, a new user and returning user, a revoked role, synthetic records, a sandbox payment where applicable, slow mobile data, and an older Android phone. Seed predictable identifiers and reset state after each attempt. Do not use real customer records.

## Failure matrix

- **Weather freshness:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **KES rounding:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **offline forms:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **farmer cooperative permissions:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.

## Kenya deployment questions

Kenya agriculture and meteorology sources; financial rail terms. Check whether your **actual activity** requires a license, contract, approval or qualified review; do not assume the category itself determines obligations. Test KES formatting, +254 and international numbers, Africa/Nairobi dates, Kiswahili and English content where relevant, shared-device privacy and intermittent connectivity.

## Primary references

- [Kenya Ministry of Agriculture](https://www.kilimo.go.ke/)
- [Kenya Meteorological Department](https://meteo.go.ke/)

## Release gate and evidence

**Block release** for unauthorized access, unreconciled money, unsafe advice, lost critical records or a blocked core task. Report build, scenario ID, preconditions, expected/actual result, severity, redacted evidence, owner, fix and retest. Record *not attempted* honestly.

[Copyable test case](../templates/test-case.md) · [Founder QA scorecard](../templates/founder-scorecard.md).
