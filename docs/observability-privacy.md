# Privacy-safe logging, tracing and analytics instrumentation

[← Resources](../README.md) · [Founder test cases](test-case-catalog.md) · [Release readiness](release-readiness.md)

## Why this matters

Observability is only useful if it reveals failures without exposing secrets or personal records.

## Common founder mistakes

- Testing only a single ideal account or device.
- Confusing a successful demo with an independently observed user outcome.
- Failing to test errors, permissions, migration or recovery.
- Publishing claims or private records without a verifiable source and permission.

## Practical test scenarios

1. Define event dictionary and redaction rules before collecting logs. Record the starting state, expected result, actual result, build and owner.
2. Test auth failures, payment failures and retries without logging credentials. Record the starting state, expected result, actual result, build and owner.
3. Ensure correlation IDs link requests without exposing user identity. Record the starting state, expected result, actual result, build and owner.
4. Check alert routing and ownership on controlled failures. Record the starting state, expected result, actual result, build and owner.
5. Verify retention, consent and deletion promises against actual telemetry. Record the starting state, expected result, actual result, build and owner.

## Repeatable workflow

1. Identify the intended user, critical task and failure risk.
2. Prepare fictional test data and an authorized environment.
3. Define success criteria and run both happy and failure paths.
4. Capture privacy-safe evidence and assign defects by user impact.
5. Fix the issue, publish a versioned build and retest under comparable conditions.

## Primary references

- [OpenTelemetry](https://opentelemetry.io/)
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- [Sentry data management](https://docs.sentry.io/security-legal-pii/scrubbing/)

## Done when

There is a completed test matrix with actual observations, known limitations, owner, fix link and retest outcome. Do not claim compliance or production safety based only on a tool's score.

_Last curated: 2026-11-23._
