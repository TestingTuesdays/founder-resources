# Synthetic test data, fixtures and environment isolation

[← Resources](../README.md) · [Founder test cases](test-case-catalog.md) · [Release readiness](release-readiness.md)

## Why this matters

Realistic test data must cover difficult inputs without copying customer records.

## Common founder mistakes

- Testing only a single ideal account or device.
- Confusing a successful demo with an independently observed user outcome.
- Failing to test errors, permissions, migration or recovery.
- Publishing claims or private records without a verifiable source and permission.

## Practical test scenarios

1. Use fictional users with different roles, locales, devices and organization memberships. Record the starting state, expected result, actual result, build and owner.
2. Seed and reset data deterministically before every critical test. Record the starting state, expected result, actual result, build and owner.
3. Ensure staging email/SMS and payment integrations cannot contact real customers. Record the starting state, expected result, actual result, build and owner.
4. Exercise malformed, duplicate, null, long and Unicode values. Record the starting state, expected result, actual result, build and owner.
5. Check test account cleanup and retention. Record the starting state, expected result, actual result, build and owner.

## Repeatable workflow

1. Identify the intended user, critical task and failure risk.
2. Prepare fictional test data and an authorized environment.
3. Define success criteria and run both happy and failure paths.
4. Capture privacy-safe evidence and assign defects by user impact.
5. Fix the issue, publish a versioned build and retest under comparable conditions.

## Primary references

- [Faker](https://fakerjs.dev/)
- [Playwright fixtures](https://playwright.dev/docs/test-fixtures)
- [OWASP Test Guide](https://owasp.org/www-project-web-security-testing-guide/)

## Done when

There is a completed test matrix with actual observations, known limitations, owner, fix link and retest outcome. Do not claim compliance or production safety based only on a tool's score.

_Last curated: 2026-11-23._
