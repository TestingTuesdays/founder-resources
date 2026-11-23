# API and background-job QA starter

[← Stack recipes](README.md) · [QA guide](../docs/qa-automation.md) · [Release gate](../docs/release-readiness.md)

## When to use

Use for backend-heavy apps with queues, REST/GraphQL, webhooks and integrations.

## Founder checklist

- [ ] Define three actual user journeys and success criteria.
- [ ] Run clean signup, returning login, failure/recovery and logout.
- [ ] Test narrow mobile/older device, low bandwidth, keyboard and assistive technologies.
- [ ] Check authorization and data access at the backend, not merely in the UI.
- [ ] Test actual money and notification paths in provider sandboxes.
- [ ] Confirm logs, monitoring, backup/restore, rollback and support ownership.
- [ ] Repeat task after each fix; keep evidence tied to build and environment.

## Stack-specific considerations

Check authentication and per-object authorization, input schemas, idempotency, quotas, timeouts, retries, job replay, audit trail and database consistency. Validate concurrency with synthetic accounts.

## Tools and developer references

- [OpenAPI spec](https://spec.openapis.org/oas/latest.html)
- [Bruno](https://www.usebruno.com/)
- [Postman](https://www.postman.com/)
- [OWASP API Security](https://owasp.org/projects/api-security-project)

## Do not skip

Use fictional test accounts, avoid public secrets and confirm up-to-date vendor and store policy. Do not claim complete security, accessibility or test coverage solely from this starter checklist.

**Output:** test matrix, priority issues, release decision and comparable retest evidence.
