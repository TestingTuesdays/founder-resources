# Education and learning — practical founder testing playbook

[← All app types](README.md) · [Kenya hub](../kenya/README.md) · [Reusable skill](../skills/app-edtech-deep-dive/SKILL.md)

## Outcome to protect

**Child privacy, accessibility and actual learning outcomes.** Engagement metrics and quiz completion are not proof of learning.

## Critical user journeys

| Journey | Success condition | Common failure |
| --- | --- | --- |
| First use | A target user completes the primary task without coaching | Unclear CTA, missing permission or confusing form |
| Core transaction | Exactly one authorized logical operation is recorded | Duplicate, stale or cross-user state |
| Failure and recovery | User sees truthful status and a safe retry path | Silent data loss or false success |
| Support and dispute | User can find the status, evidence and next action | Untraceable case or inaccessible support |

## Executable-style acceptance scenarios

- **Authorization and event replay:** Given parent A and child B in different households, when parent A requests child B progress, then server denies it.
- **Concurrency or offline recovery:** Given a learner on low-bandwidth Android, when connection drops during assignment, then progress is preserved and submission status is clear.
- **Safety and truthfulness:** Given an assessment with screen reader and large text, when the learner completes the task, then every prompt and answer remains accessible.

## Test environment and fixtures

Use two fictional organizations or households, a new user and returning user, a revoked role, synthetic records, a sandbox payment where applicable, slow mobile data, and an older Android phone. Seed predictable identifiers and reset state after each attempt. Do not use real customer records.

## Failure matrix

- **Cross-parent records:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **offline assignment:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **bias in scoring:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **parental consent:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.

## Kenya deployment questions

Ministry of Education; ODPC children data; school-specific rules. Check whether your **actual activity** requires a license, contract, approval or qualified review; do not assume the category itself determines obligations. Test KES formatting, +254 and international numbers, Africa/Nairobi dates, Kiswahili and English content where relevant, shared-device privacy and intermittent connectivity.

## Primary references

- [Kenya Ministry of Education](https://www.education.go.ke/)
- [W3C WAI](https://www.w3.org/WAI/)

## Release gate and evidence

**Block release** for unauthorized access, unreconciled money, unsafe advice, lost critical records or a blocked core task. Report build, scenario ID, preconditions, expected/actual result, severity, redacted evidence, owner, fix and retest. Record *not attempted* honestly.

[Copyable test case](../templates/test-case.md) · [Founder QA scorecard](../templates/founder-scorecard.md).
