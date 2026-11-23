---
name: deliverability-audit
description: Audit transactional email and push deliverability for founder production quality and safe release decisions.
---

# Audit transactional email and push deliverability

[← Skills index](../README.md) · [Topic guidance](../../docs/notification-deliverability.md)

## Goal

Convert an overlooked production risk into a repeatable test with observable results.

## Required inputs

An authorized staging/product environment, synthetic accounts, a named owner, expected outcomes and relevant platform/provider documentation. Use real end users only with informed consent.

## Step-by-step procedure

1. Inventory event triggers and sender domains, authentication and user preferences.
2. Use test recipients to verify verification, reset and transactional email without personal data.
3. Trigger delays, bounces, duplicate events and missing permissions.
4. Inspect template layout on narrow devices and screen readers.
5. Confirm opt-out rules separate marketing from essential notices.
6. Report actual delivery and application state; retest after correction.

## Evidence and exit criteria

For every scenario capture version/build, environment, expected and actual result, redacted evidence, severity, owner, fix link and comparable retest. A successful command, an unexecuted checklist or a simulated answer is **not** a passing product test.

## Safety boundaries

Never run disruptive security, load or failure-injection actions on systems without explicit permission. Keep credentials, billing identities, participant recordings and sensitive records out of public reports. Seek qualified legal/domain review for high-impact or regulated flows.

[Bug report template](../../templates/bug-report.md) · [Test case template](../../templates/test-case.md) · [Retest](../../templates/retest.md).
