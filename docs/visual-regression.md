# Visual regression and responsive UI audits

[← Founder resources](../README.md) · [Test cases](test-case-catalog.md) · [Templates](../templates/README.md)

## Who this is for

Web apps and design-system teams shipping frequent visual updates.

## Why it matters

Passing functional tests does not guarantee that a modal, pricing page or CTA still fits on a real device.

## Frequent mistakes

- Approving snapshots without viewing meaningful diffs.
- Masking actual accessibility failures as visual flakiness.
- Skipping font loading, translated text and dark mode.
- Using only desktop viewport snapshots.

## Test scenarios

1. **Capture representative pages at small mobile, tablet and desktop widths.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
2. **Check navigation, overlays, keyboard focus and sticky elements.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
3. **Compare long translated strings and 200% zoom.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
4. **Review image loading/fallback, missing fonts and theme changes.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
5. **Approve intentional diffs and file defects for regressions.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.

## Founder workflow

1. Choose the top one to three real user journeys relevant to your product.
2. Prepare synthetic data and an authorized test environment. Do not share production credentials or personal records.
3. Write observable pass/fail criteria *before* executing the happy path and the failure/recovery scenarios.
4. Run the checks with appropriate devices, identities and permissions. Do not assume an automated tool proves the complete journey.
5. File reproducible defects, assign severity based on harm, fix in a versioned build and retest.
6. Decide go/no-go; block on critical privacy, money, safety, irreversible-data or core-task risks.

## Primary references and tools

| Resource | Value |
| --- | --- |
| [Playwright screenshots](https://playwright.dev/docs/screenshots) | Primary documentation and implementation patterns |
| [Storybook visual tests](https://storybook.js.org/docs/writing-tests/visual-testing) | Primary documentation and implementation patterns |
| [Chromatic](https://www.chromatic.com/) | Primary documentation and implementation patterns |
| [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Primary documentation and implementation patterns |

## Expected deliverable

Versioned visual comparison matrix with intentional changes separated from regressions.

**Do:** keep assumptions and evidence separate, disclose uncertainty and verify current rules before release. **Don't:** imply testing coverage beyond what was executed, or expose real users and assets to experiments without permission.

_Last edited: 2026-11-23. External policies and tool capabilities can change._
