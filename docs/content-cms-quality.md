# CMS, knowledge bases and content publication QA

[← Founder resources](../README.md) · [Test cases](test-case-catalog.md) · [Templates](../templates/README.md)

## Who this is for

Founders publishing documentation, landing pages, blogs or community content.

## Why it matters

Outdated claims, broken links and inconsistent navigation erode trust and can create support or legal problems.

## Frequent mistakes

- Publishing policy-sensitive claims with no review date.
- Breaking documentation links when renaming folders.
- Not tracking original sources, licensing and ownership.
- Using AI-written content without fact-checking citations.

## Test scenarios

1. **Every internal navigation link resolves.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
2. **Content claims trace to authoritative sources and review date.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
3. **Images have rights, accessible alt text and correct credits.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
4. **Crawlers and people see truthful matching content.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
5. **Localization and search metadata reflect actual page language.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
6. **Publication owner can revert mistakes without data loss.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.

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
| [Google Search Central](https://developers.google.com/search/docs) | Primary documentation and implementation patterns |
| [W3C WAI](https://www.w3.org/WAI/) | Primary documentation and implementation patterns |
| [GitHub Markdown docs](https://docs.github.com/en/get-started/writing-on-github) | Primary documentation and implementation patterns |
| [Creative Commons licenses](https://creativecommons.org/licenses/) | Primary documentation and implementation patterns |

## Expected deliverable

Editorial review record, source provenance, link validation and rollback-ready change.

**Do:** keep assumptions and evidence separate, disclose uncertainty and verify current rules before release. **Don't:** imply testing coverage beyond what was executed, or expose real users and assets to experiments without permission.

_Last edited: 2026-11-23. External policies and tool capabilities can change._
