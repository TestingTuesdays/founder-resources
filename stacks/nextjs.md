# Next.js and React production test starter

[← Stack recipes](README.md) · [QA guide](../docs/qa-automation.md) · [Release gate](../docs/release-readiness.md)

## When to use

Use on a typical Next.js + React app.

## Founder checklist

- [ ] Define three actual user journeys and success criteria.
- [ ] Run clean signup, returning login, failure/recovery and logout.
- [ ] Test narrow mobile/older device, low bandwidth, keyboard and assistive technologies.
- [ ] Check authorization and data access at the backend, not merely in the UI.
- [ ] Test actual money and notification paths in provider sandboxes.
- [ ] Confirm logs, monitoring, backup/restore, rollback and support ownership.
- [ ] Repeat task after each fix; keep evidence tied to build and environment.

## Stack-specific considerations

Run local unit tests for functions and component behavior; use Playwright for browser journeys; run axe for obvious accessibility rules; inspect build and deployed page. Test server actions, session cookies, cache invalidation, forms, redirects and rate limits.

## Tools and developer references

- [Playwright](https://playwright.dev/docs/intro)
- [Testing Library](https://testing-library.com/docs/)
- [Next.js testing guide](https://nextjs.org/docs/app/guides/testing)
- [Vitest](https://vitest.dev/)

## Do not skip

Use fictional test accounts, avoid public secrets and confirm up-to-date vendor and store policy. Do not claim complete security, accessibility or test coverage solely from this starter checklist.

**Output:** test matrix, priority issues, release decision and comparable retest evidence.
