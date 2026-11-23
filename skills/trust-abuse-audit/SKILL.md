---
name: trust-abuse-audit
description: Audit abuse and moderation workflows for founders developing and testing real products.
---

# Audit abuse and moderation workflows

[← All skills](../README.md) · [Practical guide](../../docs/fraud-abuse-trust.md)

## Goal

Make a founder's testing action repeatable and independently verifiable.

## Required inputs

An authorized product/environment, versioned build, representative sample accounts, explicit pass/fail criterion, and appropriate privacy/research permissions.

## Procedure

1. Map ways a malicious or mistaken user could affect others.
2. Test report, block, moderation, appeal and role permissions in authorized sandbox.
3. Verify API enforcement—not just hidden UI controls.
4. Check audit trails, abuse rate limiting and false-positive reversal.
5. Record incident owner and retest all high-severity findings.

## Done when

An abuse-case matrix, moderation safeguards, owner and verified outcomes.

## Restrictions

Do not state an outcome as passed until it was run. Use synthetic data for public examples and keep billing identifiers, participants' information, secrets and private accounts out of the open repository. Stop and escalate if the test could harm real customers or physical systems.

[Use a test case](../../templates/test-case.md) · [Report a bug](../../templates/bug-report.md) · [Verify a fix](../../templates/retest.md).
