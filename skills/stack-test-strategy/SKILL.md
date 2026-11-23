---
name: stack-test-strategy
description: Select and implement a test strategy for the project's actual tech stack with reproducible evidence and safe handling of participant data.
---

# Select and implement a test strategy for the project's actual tech stack

[← Skills](../README.md) · [Guide](../../stacks/README.md)

## Inputs

Named product/build, intended users, one core task, authorized environment, synthetic fixtures, privacy/consent plan and accountable reviewer.

## Procedure

1. Identify framework/runtime, deployment target and critical user journeys.
2. Select a unit runner, integration approach and one E2E runner compatible with installed versions.
3. Seed synthetic accounts, isolate databases and mock external providers.
4. Test permissions, invalid input, retries and critical user flow on representative device.
5. Record local commands, build SHA and actual outcomes.
6. Create owner-assigned issues and retest after release.

## Completion criteria

A versioned task matrix with expected/actual results, evidence quality, issue owner, fix reference and comparable retest. Record unexecuted tests as **not attempted**, not passed.

## Safety and scope

No unauthorized testing, real customer credentials, private recordings or sensitive participant data in public issues. Confirm current framework support and provider policies; integration plans are not proof of a working deployment.
