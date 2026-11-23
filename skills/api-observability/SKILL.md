---
name: api-observability
description: Execute a repeatable founder QA review for api observability and error-budget audit.
---

# API observability and error-budget audit

[← Skills](../README.md) · [Guide](../../docs/api-observability.md)

## Inputs

Versioned product, real target user task, synthetic test accounts, authorized environment and named reviewer.

## Procedure

1. Choose user-visible success and error metrics per critical endpoint.
2. Instrument requests, background jobs and provider callbacks with safe correlation IDs.
3. Verify alert routing, owner and severity.
4. Test timeout, 429, malformed response and provider outage.
5. Measure latency percentiles and error rate by route and client version.
6. Retest remediation and check logging redaction.

## Completion criteria

Evidence-backed issue register with observed outcomes, severity, owner, fix, build and retest. Separate hypotheses and proposed tests from executed tests.

## Privacy and safety

Never publish participant identities, payment details, credentials or unapproved security findings. Escalate regulated or safety-critical questions for expert review.
