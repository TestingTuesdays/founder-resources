# Metadata, social previews and structured data

[← Design and growth hub](README.md) · [Skills](../skills/README.md) · [Audit template](../templates/design-growth-audit.md)

## Goal

Make each page shareable and accurately represented in search, messaging and social platforms.

## Practical audit procedure

1. Define unique page title and description aligned to actual visible content.
2. Validate canonical, robots, language, viewport and site name.
3. Add appropriate Open Graph title, description, URL and accessible image; use absolute HTTPS URLs.
4. Add Twitter/X card tags where applicable and test platform previews.
5. Implement JSON-LD only for relevant supported entities; never mark nonexistent reviews, FAQs or prices.
6. Check 200/404, locale, staging noindex and missing image fallback.

## Acceptance and evidence

For each issue record page URL, intended user task, current behavior, expected result, screenshot or redacted observation, mobile/desktop state, severity, owner and retest. Rank **user task success, accessibility, clarity and truthfulness** above visual novelty or search-engine guesswork.

## Common mistakes

- Confusing a tool score, design inspiration or model answer with a verified outcome.
- Copying competitor text, assets or layouts instead of designing for actual users.
- Treating SEO or AEO/GEO as guaranteed placement in Google, ChatGPT or other products.
- Failing to check real mobile devices, focus behavior and loading states.
- Publishing unsupported testimonials, star ratings, prices or claims in metadata.

## Primary references

- [Open Graph protocol](https://ogp.me/)
- [Google structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [X Cards](https://developer.x.com/en/docs/x-for-websites/cards/overview/abouts-cards)

## Ship-back

Publish an issue with before/after rationale, test conditions, the deployed version and observed retest. External platforms and algorithms change; recheck official documentation when shipping.

_Last curated: 2026-11-23._
