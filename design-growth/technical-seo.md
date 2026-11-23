# Technical SEO, indexing and crawl diagnostics

[← Design and growth hub](README.md) · [Skills](../skills/README.md) · [Audit template](../templates/design-growth-audit.md)

## Goal

Discover canonical, rendering, sitemap, indexing and redirect problems that prevent legitimate discovery.

## Practical audit procedure

1. Audit indexable URL inventory and choose a canonical for each logical page.
2. Validate robots.txt, noindex directives, sitemap.xml, hreflang and redirect chains.
3. Check SSR/rendered HTML contains primary title, content and links.
4. Verify 404/410 status, pagination and duplicate query parameter behavior.
5. Test mobile usability, Core Web Vitals and accessible navigation.
6. Use Search Console to diagnose coverage rather than promising indexing.

## Acceptance and evidence

For each issue record page URL, intended user task, current behavior, expected result, screenshot or redacted observation, mobile/desktop state, severity, owner and retest. Rank **user task success, accessibility, clarity and truthfulness** above visual novelty or search-engine guesswork.

## Common mistakes

- Confusing a tool score, design inspiration or model answer with a verified outcome.
- Copying competitor text, assets or layouts instead of designing for actual users.
- Treating SEO or AEO/GEO as guaranteed placement in Google, ChatGPT or other products.
- Failing to check real mobile devices, focus behavior and loading states.
- Publishing unsupported testimonials, star ratings, prices or claims in metadata.

## Primary references

- [Google Search Console](https://search.google.com/search-console/about)
- [Google crawling docs](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
- [web.dev Core Web Vitals](https://web.dev/articles/vitals)

## Ship-back

Publish an issue with before/after rationale, test conditions, the deployed version and observed retest. External platforms and algorithms change; recheck official documentation when shipping.

_Last curated: 2026-11-23._
