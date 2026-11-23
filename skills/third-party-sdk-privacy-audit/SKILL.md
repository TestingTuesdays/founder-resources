---
name: third-party-sdk-privacy-audit
description: Audit SDK telemetry and mobile privacy declarations for founder production quality and safe release decisions.
---

# Audit SDK telemetry and mobile privacy declarations

[← Skills index](../README.md) · [Topic guidance](../../docs/privacy-sdk-inventory.md)

## Goal

Convert an overlooked production risk into a repeatable test with observable results.

## Required inputs

An authorized staging/product environment, synthetic accounts, a named owner, expected outcomes and relevant platform/provider documentation. Use real end users only with informed consent.

## Step-by-step procedure

1. List packaged SDK versions and data transmitted.
2. Inspect traffic and settings on test devices.
3. Compare consent-off/consent-on behavior.
4. Compare disclosure statements and store Data safety/privacy inputs.
5. Check deletion and opt-out propagation.
6. File discrepancies with data classes and retest; obtain privacy review.

## Evidence and exit criteria

For every scenario capture version/build, environment, expected and actual result, redacted evidence, severity, owner, fix link and comparable retest. A successful command, an unexecuted checklist or a simulated answer is **not** a passing product test.

## Safety boundaries

Never run disruptive security, load or failure-injection actions on systems without explicit permission. Keep credentials, billing identities, participant recordings and sensitive records out of public reports. Seek qualified legal/domain review for high-impact or regulated flows.

[Bug report template](../../templates/bug-report.md) · [Test case template](../../templates/test-case.md) · [Retest](../../templates/retest.md).
