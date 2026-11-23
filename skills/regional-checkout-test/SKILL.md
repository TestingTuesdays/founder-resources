---
name: regional-checkout-test
description: Test local and cross-border payment UX for founder production quality and safe release decisions.
---

# Test local and cross-border payment UX

[← Skills index](../README.md) · [Topic guidance](../../docs/international-payments.md)

## Goal

Convert an overlooked production risk into a repeatable test with observable results.

## Required inputs

An authorized staging/product environment, synthetic accounts, a named owner, expected outcomes and relevant platform/provider documentation. Use real end users only with informed consent.

## Step-by-step procedure

1. Verify provider offers merchant onboarding in legal entity country.
2. Document available checkout rails and settlement currencies.
3. Simulate local and foreign payment paths only in provider sandbox.
4. Check abandoned redirect, duplicate callbacks, refund and disputes.
5. Review exchange rate, rounding, tax display and payout communication.
6. Record merchant eligibility unknowns and retest before public rollout.

## Evidence and exit criteria

For every scenario capture version/build, environment, expected and actual result, redacted evidence, severity, owner, fix link and comparable retest. A successful command, an unexecuted checklist or a simulated answer is **not** a passing product test.

## Safety boundaries

Never run disruptive security, load or failure-injection actions on systems without explicit permission. Keep credentials, billing identities, participant recordings and sensitive records out of public reports. Seek qualified legal/domain review for high-impact or regulated flows.

[Bug report template](../../templates/bug-report.md) · [Test case template](../../templates/test-case.md) · [Retest](../../templates/retest.md).
