# Multilingual accessibility and inclusive language QA

[← Resources](../README.md) · [Founder test cases](test-case-catalog.md) · [Release readiness](release-readiness.md)

## Why this matters

Translated interfaces may lose accessibility even when English pages pass.

## Common founder mistakes

- Testing only a single ideal account or device.
- Confusing a successful demo with an independently observed user outcome.
- Failing to test errors, permissions, migration or recovery.
- Publishing claims or private records without a verifiable source and permission.

## Practical test scenarios

1. Test screen-reader language switching and correct document lang. Record the starting state, expected result, actual result, build and owner.
2. Verify RTL reading order and focus sequence. Record the starting state, expected result, actual result, build and owner.
3. Check pluralization, input errors and translated accessible names. Record the starting state, expected result, actual result, build and owner.
4. Test captions, transcripts and regional number/date announcements. Record the starting state, expected result, actual result, build and owner.
5. Review high-risk content with fluent users and assistive technology. Record the starting state, expected result, actual result, build and owner.

## Repeatable workflow

1. Identify the intended user, critical task and failure risk.
2. Prepare fictional test data and an authorized environment.
3. Define success criteria and run both happy and failure paths.
4. Capture privacy-safe evidence and assign defects by user impact.
5. Fix the issue, publish a versioned build and retest under comparable conditions.

## Primary references

- [W3C Internationalization](https://www.w3.org/International/)
- [WAI language guidance](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html)
- [Unicode CLDR](https://cldr.unicode.org/)

## Done when

There is a completed test matrix with actual observations, known limitations, owner, fix link and retest outcome. Do not claim compliance or production safety based only on a tool's score.

_Last curated: 2026-11-23._
