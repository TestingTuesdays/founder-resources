# Health and care — practical founder testing playbook

[← All app types](README.md) · [Kenya hub](../kenya/README.md) · [Reusable skill](../skills/app-healthtech-deep-dive/SKILL.md)

## Outcome to protect

**Patient identity, clinical risk and caregiver permissions.** An apparently successful form submission can associate notes with the wrong patient or expose sensitive records.

## Critical user journeys

| Journey | Success condition | Common failure |
| --- | --- | --- |
| First use | A target user completes the primary task without coaching | Unclear CTA, missing permission or confusing form |
| Core transaction | Exactly one authorized logical operation is recorded | Duplicate, stale or cross-user state |
| Failure and recovery | User sees truthful status and a safe retry path | Silent data loss or false success |
| Support and dispute | User can find the status, evidence and next action | Untraceable case or inaccessible support |

## Executable-style acceptance scenarios

- **Authorization and event replay:** Given two synthetic patients, when a caregiver opens a shared link for another patient, then server authorization denies the request.
- **Concurrency or offline recovery:** Given offline notes for two patients, when reconnecting and syncing, then notes retain patient identity and conflict resolution is visible.
- **Safety and truthfulness:** Given a safety-critical symptom entry, when the system cannot provide reliable guidance, then it clearly directs to appropriate clinical/emergency support rather than fabricating a diagnosis.

## Test environment and fixtures

Use two fictional organizations or households, a new user and returning user, a revoked role, synthetic records, a sandbox payment where applicable, slow mobile data, and an older Android phone. Seed predictable identifiers and reset state after each attempt. Do not use real customer records.

## Failure matrix

- **Wrong-patient access:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **clinical claim accuracy:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **offline conflict:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **large text and speech access:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.

## Kenya deployment questions

Ministry of Health guidance; ODPC; clinical review of medical claims. Check whether your **actual activity** requires a license, contract, approval or qualified review; do not assume the category itself determines obligations. Test KES formatting, +254 and international numbers, Africa/Nairobi dates, Kiswahili and English content where relevant, shared-device privacy and intermittent connectivity.

## Primary references

- [Kenya Ministry of Health](https://www.health.go.ke/)
- [ODPC](https://www.odpc.go.ke/)

## Release gate and evidence

**Block release** for unauthorized access, unreconciled money, unsafe advice, lost critical records or a blocked core task. Report build, scenario ID, preconditions, expected/actual result, severity, redacted evidence, owner, fix and retest. Record *not attempted* honestly.

[Copyable test case](../templates/test-case.md) · [Founder QA scorecard](../templates/founder-scorecard.md).
