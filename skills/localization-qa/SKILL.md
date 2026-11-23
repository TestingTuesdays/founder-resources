---
name: localization-qa
description: Find formatting, language, layout and cultural mismatches.
---

# Localization quality assurance

[← Skills](../README.md) · [Topic guide](../../docs/localization.md)

## Objective

Find formatting, language, layout and cultural mismatches.

## Required inputs

Priority locale list, translated strings, test user journeys.

## Procedure

1. Check missing strings and placeholder/pseudolocalized text.
2. Test long words, plurals, RTL/mixed numerals.
3. Verify locale date/time/currency, address/name input.
4. Inspect app-store text, notifications, emails and error messages.
5. Review critical text with fluent speaker.
6. File issues per locale and retest in context.

## Done when

Locale/device-specific issues and reviewed strings.

## Safety and evidence

Use permissioned systems and synthetic data. Obtain research consent where applicable, redact personal information, preserve actual vs expected outcomes, and never state a check passed without running it. Human review remains necessary for high-risk conclusions.

## Copyable records

[Bug report](../../templates/bug-report.md) · [Testing session](../../templates/usability-session.md) · [Retest](../../templates/retest.md).
