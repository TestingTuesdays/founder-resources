---
name: dependency-failure-drill
description: Simulate dependency failures in staging for founder production quality and safe release decisions.
---

# Simulate dependency failures in staging

[← Skills index](../README.md) · [Topic guidance](../../docs/resilience-chaos.md)

## Goal

Convert an overlooked production risk into a repeatable test with observable results.

## Required inputs

An authorized staging/product environment, synthetic accounts, a named owner, expected outcomes and relevant platform/provider documentation. Use real end users only with informed consent.

## Step-by-step procedure

1. List critical providers and the permitted fault injection environment.
2. Choose timeout, rate limit, outage or network flap scenario.
3. Record baseline task, expected degradation and alert.
4. Inject fault in isolated/staging setup, never unapproved production.
5. Test retry budget, idempotency, escalation and recovery.
6. Measure result, document owner, retest after fix.

## Evidence and exit criteria

For every scenario capture version/build, environment, expected and actual result, redacted evidence, severity, owner, fix link and comparable retest. A successful command, an unexecuted checklist or a simulated answer is **not** a passing product test.

## Safety boundaries

Never run disruptive security, load or failure-injection actions on systems without explicit permission. Keep credentials, billing identities, participant recordings and sensitive records out of public reports. Seek qualified legal/domain review for high-impact or regulated flows.

[Bug report template](../../templates/bug-report.md) · [Test case template](../../templates/test-case.md) · [Retest](../../templates/retest.md).
