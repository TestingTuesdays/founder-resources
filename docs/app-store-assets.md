# App store screenshots, metadata and listing QA

[← Resources](../README.md) · [Founder test cases](test-case-catalog.md) · [Release readiness](release-readiness.md)

## Why this matters

A good build can be rejected or poorly understood because store metadata misrepresents the product.

## Common founder mistakes

- Testing only a single ideal account or device.
- Confusing a successful demo with an independently observed user outcome.
- Failing to test errors, permissions, migration or recovery.
- Publishing claims or private records without a verifiable source and permission.

## Practical test scenarios

1. Check title, description, category, support/privacy URLs and age rating. Record the starting state, expected result, actual result, build and owner.
2. Verify screenshots represent real app features and approved dimensions. Record the starting state, expected result, actual result, build and owner.
3. Localize captions and screenshots for priority languages. Record the starting state, expected result, actual result, build and owner.
4. Check accessibility and legibility at store-preview size. Record the starting state, expected result, actual result, build and owner.
5. Test deep links from store to onboarding and accurate subscriptions. Record the starting state, expected result, actual result, build and owner.

## Repeatable workflow

1. Identify the intended user, critical task and failure risk.
2. Prepare fictional test data and an authorized environment.
3. Define success criteria and run both happy and failure paths.
4. Capture privacy-safe evidence and assign defects by user impact.
5. Fix the issue, publish a versioned build and retest under comparable conditions.

## Primary references

- [App Store Connect](https://developer.apple.com/help/app-store-connect/)
- [Google Play Console Help](https://support.google.com/googleplay/android-developer/)
- [Apple Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)

## Done when

There is a completed test matrix with actual observations, known limitations, owner, fix link and retest outcome. Do not claim compliance or production safety based only on a tool's score.

_Last curated: 2026-11-23._
