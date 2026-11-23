---
name: low-bandwidth-test
description: Test low-bandwidth mobile journeys for founders developing and testing real products.
---

# Test low-bandwidth mobile journeys

[← All skills](../README.md) · [Practical guide](../../docs/low-bandwidth-africa.md)

## Goal

Make a founder's testing action repeatable and independently verifiable.

## Required inputs

An authorized product/environment, versioned build, representative sample accounts, explicit pass/fail criterion, and appropriate privacy/research permissions.

## Procedure

1. Choose one critical end-to-end task and a representative older mobile device.
2. Test on poor simulated cellular and record data transfer, latency and user behavior.
3. Interrupt network mid-task; check preserved input, explicit retry and no duplicate action.
4. Repeat with location/time zone/locale settings relevant to the users.
5. Prioritize failures by task consequence and retest on the same network/device profile.

## Done when

A network/device test sheet with task outcome, recovery evidence and prioritized fixes.

## Restrictions

Do not state an outcome as passed until it was run. Use synthetic data for public examples and keep billing identifiers, participants' information, secrets and private accounts out of the open repository. Stop and escalate if the test could harm real customers or physical systems.

[Use a test case](../../templates/test-case.md) · [Report a bug](../../templates/bug-report.md) · [Verify a fix](../../templates/retest.md).
