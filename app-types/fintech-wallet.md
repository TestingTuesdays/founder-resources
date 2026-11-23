# Fintech wallet and lending — practical founder testing playbook

[← All app types](README.md) · [Kenya hub](../kenya/README.md) · [Reusable skill](../skills/app-fintech-wallet-deep-dive/SKILL.md)

## Outcome to protect

**Ledger integrity, customer funds and disclosures.** A payment request may be accepted but never settle; balances and entitlements must follow independently verified state.

## Critical user journeys

| Journey | Success condition | Common failure |
| --- | --- | --- |
| First use | A target user completes the primary task without coaching | Unclear CTA, missing permission or confusing form |
| Core transaction | Exactly one authorized logical operation is recorded | Duplicate, stale or cross-user state |
| Failure and recovery | User sees truthful status and a safe retry path | Silent data loss or false success |
| Support and dispute | User can find the status, evidence and next action | Untraceable case or inaccessible support |

## Executable-style acceptance scenarios

- **Authorization and event replay:** Given a synthetic order with one pending STK request, when a success callback arrives twice, then exactly one ledger credit is posted and the provider reference remains unique.
- **Concurrency or offline recovery:** Given a customer wallet with insufficient funds, when two transfers race, then available balance never becomes negative and neither recipient is credited without corresponding debit.
- **Safety and truthfulness:** Given a delayed reversal after a paid state, when reconciliation runs, then the customer balance, invoice and audit trail reflect the reversal with an explicit reason.

## Test environment and fixtures

Use two fictional organizations or households, a new user and returning user, a revoked role, synthetic records, a sandbox payment where applicable, slow mobile data, and an older Android phone. Seed predictable identifiers and reset state after each attempt. Do not use real customer records.

## Failure matrix

- **M-Pesa settlement mismatch:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **duplicate callback:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **unauthorized wallet read:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.
- **repayment and loan disclosure:** define trigger, expected state, observable actual state, harm, fix owner and comparable retest.

## Kenya deployment questions

Kenya/CBK applicability; ODPC sensitive data; PSP onboarding. Check whether your **actual activity** requires a license, contract, approval or qualified review; do not assume the category itself determines obligations. Test KES formatting, +254 and international numbers, Africa/Nairobi dates, Kiswahili and English content where relevant, shared-device privacy and intermittent connectivity.

## Primary references

- [CBK](https://www.centralbank.go.ke/)
- [Safaricom Daraja](https://developer.safaricom.co.ke/)

## Release gate and evidence

**Block release** for unauthorized access, unreconciled money, unsafe advice, lost critical records or a blocked core task. Report build, scenario ID, preconditions, expected/actual result, severity, redacted evidence, owner, fix and retest. Record *not attempted* honestly.

[Copyable test case](../templates/test-case.md) · [Founder QA scorecard](../templates/founder-scorecard.md).
