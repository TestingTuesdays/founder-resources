# Vue / Nuxt — testing framework recipe

[← Stack index](README.md) · [User research](../research/README.md) · [Evidence standard](../docs/quality-evidence-standard.md)

## Recommended framework layers

Vitest + Vue Test Utils; Playwright; MSW.

## What to test at each layer

Unit: composables and validation; component: Vue Test Utils with user events; E2E: navigation, SSR hydration, forms and auth; integration: mock 401, 429 and 500 responses.

## Suggested smoke-test matrix

| Scenario | Layer | Expected outcome | Evidence |
| --- | --- | --- | --- |
| Core user task | E2E on representative device | Unassisted completion | Not run |
| Validation and empty states | Unit/component | Clear, accessible recovery | Not run |
| Unauthorized cross-account access | Integration/API | Server denies | Not run |
| Provider timeout or duplicate event | Integration | Safe retry and one logical outcome | Not run |
| Slow mobile network | E2E/device | Preserved state and truthful status | Not run |
| Fix regression | Same layer as original defect | Previous failure no longer reproducible | Not run |

## Setup and release workflow

1. Choose one unit runner, one integration approach and one end-to-end runner rather than adding every tool.
2. Create deterministic synthetic fixtures and isolated test services.
3. Automate the critical paths locally; retain manual moderated user testing for comprehension and accessibility.
4. Capture build SHA, command, environment, expected/actual result and redacted evidence.
5. Fix, retest and release only after the risk owner approves. GitHub Actions remain intentionally disabled in this resource repository.

## Stack-specific caution

Test server-rendered metadata and client hydration, then keyboard focus and mobile layout.

## Official references

- [Vue Test Utils](https://test-utils.vuejs.org/)
- [Vitest](https://vitest.dev/)
- [Playwright](https://playwright.dev/)

These are selection starting points; tool compatibility and supported versions must be checked against the project's installed stack.
