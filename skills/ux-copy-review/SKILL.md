---
name: ux-copy-review
description: Test microcopy, error states and comprehension for founder production quality and safe release decisions.
---

# Test microcopy, error states and comprehension

[← Skills index](../README.md) · [Topic guidance](../../docs/design-copy-content.md)

## Goal

Convert an overlooked production risk into a repeatable test with observable results.

## Required inputs

An authorized staging/product environment, synthetic accounts, a named owner, expected outcomes and relevant platform/provider documentation. Use real end users only with informed consent.

## Step-by-step procedure

1. Choose a primary journey and gather its labels, help text, pricing and errors.
2. Give intended users task-based prompts and observe their interpretation.
3. Check language for unsupported claims and manipulative design.
4. Verify error messages explain what happened and how to recover.
5. Review accessibility, translation and low literacy needs.
6. Change text, version it and retest comprehension.

## Evidence and exit criteria

For every scenario capture version/build, environment, expected and actual result, redacted evidence, severity, owner, fix link and comparable retest. A successful command, an unexecuted checklist or a simulated answer is **not** a passing product test.

## Safety boundaries

Never run disruptive security, load or failure-injection actions on systems without explicit permission. Keep credentials, billing identities, participant recordings and sensitive records out of public reports. Seek qualified legal/domain review for high-impact or regulated flows.

[Bug report template](../../templates/bug-report.md) · [Test case template](../../templates/test-case.md) · [Retest](../../templates/retest.md).
