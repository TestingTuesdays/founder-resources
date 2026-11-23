---
name: bug-triage
description: Turn vague reports into evidence-backed prioritized fixes.
---

# Reproduce and triage product bugs

[← Skills](../README.md) · [Topic guide](../../docs/qa-automation.md)

## Objective

Turn vague reports into evidence-backed prioritized fixes.

## Required inputs

Bug report, non-sensitive test data, build/version, reproducible environment.

## Procedure

1. Identify expected outcome and user impact.
2. Try precise reproduction steps on recorded device/browser.
3. Compare actual outcome and logs without secrets.
4. Classify P0/P1/P2/P3 by impact, not convenience.
5. Link owner, relevant regression test and due date.
6. Retest after the change; keep original issue evidence.

## Done when

Actionable issue with steps, severity, owner, build and verified status.

## Safety and evidence

Use permissioned systems and synthetic data. Obtain research consent where applicable, redact personal information, preserve actual vs expected outcomes, and never state a check passed without running it. Human review remains necessary for high-risk conclusions.

## Copyable records

[Bug report](../../templates/bug-report.md) · [Testing session](../../templates/usability-session.md) · [Retest](../../templates/retest.md).
