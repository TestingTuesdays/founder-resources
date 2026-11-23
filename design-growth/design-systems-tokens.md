# Design systems, components and design tokens

[← Design and growth hub](README.md) · [Skills](../skills/README.md) · [Audit template](../templates/design-growth-audit.md)

## Goal

Improve consistency and reduce visual regressions as a product grows.

## Practical audit procedure

1. Inventory typography, colors, spacing, radii, shadows and icon styles.
2. Create semantic tokens rather than page-specific magic numbers.
3. Specify button, input, card, navigation and dialog states including errors and disabled.
4. Test keyboard, contrast, focus, zoom, long translations and loading states.
5. Create representative component stories and visual regression baselines.
6. Document responsive rules and ownership before broad migration.

## Acceptance and evidence

For each issue record page URL, intended user task, current behavior, expected result, screenshot or redacted observation, mobile/desktop state, severity, owner and retest. Rank **user task success, accessibility, clarity and truthfulness** above visual novelty or search-engine guesswork.

## Common mistakes

- Confusing a tool score, design inspiration or model answer with a verified outcome.
- Copying competitor text, assets or layouts instead of designing for actual users.
- Treating SEO or AEO/GEO as guaranteed placement in Google, ChatGPT or other products.
- Failing to check real mobile devices, focus behavior and loading states.
- Publishing unsupported testimonials, star ratings, prices or claims in metadata.

## Primary references

- [W3C Design Tokens Community Group](https://www.w3.org/community/design-tokens/)
- [Storybook](https://storybook.js.org/)
- [Material Design 3](https://m3.material.io/)

## Ship-back

Publish an issue with before/after rationale, test conditions, the deployed version and observed retest. External platforms and algorithms change; recheck official documentation when shipping.

_Last curated: 2026-11-23._
