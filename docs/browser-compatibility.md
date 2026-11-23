# Browser, device and OS compatibility

[← Resources](../README.md) · [Founder test cases](test-case-catalog.md) · [Release readiness](release-readiness.md)

## Why this matters

An app can work on Chrome desktop and fail on mobile Safari, older Android or assistive technology.

## Common founder mistakes

- Testing only a single ideal account or device.
- Confusing a successful demo with an independently observed user outcome.
- Failing to test errors, permissions, migration or recovery.
- Publishing claims or private records without a verifiable source and permission.

## Practical test scenarios

1. Cover latest and representative older browsers based on actual audience. Record the starting state, expected result, actual result, build and owner.
2. Check responsive viewport, zoom, orientation and virtual keyboard. Record the starting state, expected result, actual result, build and owner.
3. Test permissions, downloads, file pickers, clipboard and deep links. Record the starting state, expected result, actual result, build and owner.
4. Verify progressive enhancement when advanced APIs are unavailable. Record the starting state, expected result, actual result, build and owner.
5. Record unsupported browsers and graceful fallback. Record the starting state, expected result, actual result, build and owner.

## Repeatable workflow

1. Identify the intended user, critical task and failure risk.
2. Prepare fictional test data and an authorized environment.
3. Define success criteria and run both happy and failure paths.
4. Capture privacy-safe evidence and assign defects by user impact.
5. Fix the issue, publish a versioned build and retest under comparable conditions.

## Primary references

- [MDN Browser Compatibility Data](https://github.com/mdn/browser-compat-data)
- [Can I use](https://caniuse.com/)
- [Playwright browsers](https://playwright.dev/docs/browsers)

## Done when

There is a completed test matrix with actual observations, known limitations, owner, fix link and retest outcome. Do not claim compliance or production safety based only on a tool's score.

_Last curated: 2026-11-23._
