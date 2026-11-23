# No-code and low-code founder QA starter

[← Stack recipes](README.md) · [QA guide](../docs/qa-automation.md) · [Release gate](../docs/release-readiness.md)

## When to use

Use for products built with website builders, automation platforms and app creators.

## Founder checklist

- [ ] Define three actual user journeys and success criteria.
- [ ] Run clean signup, returning login, failure/recovery and logout.
- [ ] Test narrow mobile/older device, low bandwidth, keyboard and assistive technologies.
- [ ] Check authorization and data access at the backend, not merely in the UI.
- [ ] Test actual money and notification paths in provider sandboxes.
- [ ] Confirm logs, monitoring, backup/restore, rollback and support ownership.
- [ ] Repeat task after each fix; keep evidence tied to build and environment.

## Stack-specific considerations

You can still run neutral user testing, browser/device matrices, accessibility checks and billing/permission scenarios. Test workflow retries, data export, failed integrations, seat pricing, privacy settings and vendor lock-in.

## Tools and developer references

- [W3C Easy Checks](https://www.w3.org/WAI/test-evaluate/preliminary/)
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
- [GOV.UK user research](https://www.gov.uk/service-manual/user-research)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

## Do not skip

Use fictional test accounts, avoid public secrets and confirm up-to-date vendor and store policy. Do not claim complete security, accessibility or test coverage solely from this starter checklist.

**Output:** test matrix, priority issues, release decision and comparable retest evidence.
