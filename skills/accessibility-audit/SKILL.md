---
name: accessibility-audit
description: Identify barriers to critical flows with manual and automated coverage.
---

# Accessibility audit

[← Skills](../README.md) · [Topic guide](../../docs/accessibility.md)

## Objective

Identify barriers to critical flows with manual and automated coverage.

## Required inputs

Representative flow, current product build and chosen WCAG 2.2 criteria.

## Procedure

1. Run axe or WAVE for leads, not certification.
2. Navigate all controls by keyboard and verify focus.
3. Check labels, headings, dialogs and errors with screen reader.
4. Zoom 200%, inspect reflow, contrast and reduced motion.
5. Validate critical flows with disabled users where feasible.
6. File barrier and criteria mapping; retest manually.

## Done when

Prioritized barriers with assistive-tech environment and retest evidence.

## Safety and evidence

Use permissioned systems and synthetic data. Obtain research consent where applicable, redact personal information, preserve actual vs expected outcomes, and never state a check passed without running it. Human review remains necessary for high-risk conclusions.

## Copyable records

[Bug report](../../templates/bug-report.md) · [Testing session](../../templates/usability-session.md) · [Retest](../../templates/retest.md).
