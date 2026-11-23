---
name: pricing-integrity-audit
description: Verify pricing claims and billing entitlements for founder production quality and safe release decisions.
---

# Verify pricing claims and billing entitlements

[← Skills index](../README.md) · [Topic guidance](../../docs/pricing-packaging.md)

## Goal

Convert an overlooked production risk into a repeatable test with observable results.

## Required inputs

An authorized staging/product environment, synthetic accounts, a named owner, expected outcomes and relevant platform/provider documentation. Use real end users only with informed consent.

## Step-by-step procedure

1. List all displayed plan features, limits, fees, renewals and currencies.
2. Compare pricing page and checkout against billing provider configuration.
3. Test trial, expired coupon, change plan and cancellation in sandbox.
4. Check taxes, seat count and metered overages for examples.
5. Confirm entitlements are enforced server side.
6. Document discrepancies and retest actual invoice/access behavior.

## Evidence and exit criteria

For every scenario capture version/build, environment, expected and actual result, redacted evidence, severity, owner, fix link and comparable retest. A successful command, an unexecuted checklist or a simulated answer is **not** a passing product test.

## Safety boundaries

Never run disruptive security, load or failure-injection actions on systems without explicit permission. Keep credentials, billing identities, participant recordings and sensitive records out of public reports. Seek qualified legal/domain review for high-impact or regulated flows.

[Bug report template](../../templates/bug-report.md) · [Test case template](../../templates/test-case.md) · [Retest](../../templates/retest.md).
