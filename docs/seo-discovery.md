# SEO, AEO & discoverability QA

[← Resource home](../README.md) · [Release checklist](release-readiness.md)

## Why founders should care

Search engines and AI tools cannot recommend pages they cannot access or interpret correctly.

## Common mistakes

- Assuming a successful demo or dashboard proves the experience works for all users.
- Ignoring errors, permission boundaries, mobile constraints and exceptional states.
- Launching without a responsible owner, observable outcome or fallback.
- Using vendor tooling without checking costs, data protection or real capabilities.

## Core test scenarios

1. **Canonical URL and redirects return correct status.** Record build/environment, expected vs actual, user impact and follow-up.
2. **Robots and noindex do not block intended pages.** Record build/environment, expected vs actual, user impact and follow-up.
3. **Metadata, sitemap and hreflang match real pages.** Record build/environment, expected vs actual, user impact and follow-up.
4. **Structured data accurately matches visible content.** Record build/environment, expected vs actual, user impact and follow-up.
5. **Important content usable without client-only scripts.** Record build/environment, expected vs actual, user impact and follow-up.
6. **Share-preview image and social descriptions accurate.** Record build/environment, expected vs actual, user impact and follow-up.

## Practical workflow

1. Identify the most important user task and a measurable success criterion.
2. Use safe synthetic data and a representative device/locale/account.
3. Test the expected route **and** failure/recovery case; observe results, not assumptions.
4. Check privacy/security, accessibility and reliability considerations where relevant.
5. File a reproducible issue, assign an owner and retest after the deployed fix.

## Trusted tools and reference material

| Reference | What it helps with |
| --- | --- |
| [Google Search Central](https://developers.google.com/search/docs) | Official search guidance |
| [Google Rich Results Test](https://search.google.com/test/rich-results) | Structured-data checks |
| [Bing Webmaster Tools](https://www.bing.com/webmasters/) | Search visibility |
| [Schema.org](https://schema.org/) | Structured-data vocabulary |
| [web.dev](https://web.dev/) | Web quality |

## Go/no-go consideration

Do not call this area ready if the core journey can cause loss of data, money, privacy or user access without a documented safe recovery path. Regulations and provider requirements change: review official documentation for your specific product and market.

_Last curated: 2026-11-23._
