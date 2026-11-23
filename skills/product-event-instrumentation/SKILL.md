---
name: product-event-instrumentation
description: Instrument privacy-safe product funnels and quality events with reproducible evidence and safe handling of participant data.
---

# Instrument privacy-safe product funnels and quality events

[← Skills](../README.md) · [Guide](../../research/analytics-instrumentation.md)

## Inputs

Named product/build, intended users, one core task, authorized environment, synthetic fixtures, privacy/consent plan and accountable reviewer.

## Procedure

1. Define exact event trigger and safe properties for core task.
2. Implement event deduplication and consent handling.
3. Test signup identity transitions, offline retries and deletion.
4. Reconcile synthetic event counts against backend source-of-truth.
5. Review funnels with denominators and exclusions.
6. Document changes, owner and validation evidence.

## Completion criteria

A versioned task matrix with expected/actual results, evidence quality, issue owner, fix reference and comparable retest. Record unexecuted tests as **not attempted**, not passed.

## Safety and scope

No unauthorized testing, real customer credentials, private recordings or sensitive participant data in public issues. Confirm current framework support and provider policies; integration plans are not proof of a working deployment.
