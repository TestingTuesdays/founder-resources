---
name: feedback-collection-integration
description: Integrate a privacy-safe feedback widget and triage pipeline with reproducible evidence and safe handling of participant data.
---

# Integrate a privacy-safe feedback widget and triage pipeline

[← Skills](../README.md) · [Guide](../../research/feedback-integration.md)

## Inputs

Named product/build, intended users, one core task, authorized environment, synthetic fixtures, privacy/consent plan and accountable reviewer.

## Procedure

1. Choose minimum feedback categories and optional contact fields.
2. Validate and rate limit server-side intake, keep secrets and PII out of logs.
3. Store private raw feedback with retention and deletion controls.
4. Send redacted reproducible summaries to a restricted issue tracker.
5. Deduplicate safely, assign severity/owner and link release.
6. Verify timeout, replay, unauthorized access and comparable retest.

## Completion criteria

A versioned task matrix with expected/actual results, evidence quality, issue owner, fix reference and comparable retest. Record unexecuted tests as **not attempted**, not passed.

## Safety and scope

No unauthorized testing, real customer credentials, private recordings or sensitive participant data in public issues. Confirm current framework support and provider policies; integration plans are not proof of a working deployment.
