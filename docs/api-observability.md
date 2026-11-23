# API observability and error-budget audit

[← Documentation index](README.md) · [Skill](../skills/api-observability/SKILL.md)

Average latency can hide failures on core user journeys.

## Step-by-step founder checklist

1. Choose user-visible success and error metrics per critical endpoint.
2. Instrument requests, background jobs and provider callbacks with safe correlation IDs.
3. Verify alert routing, owner and severity.
4. Test timeout, 429, malformed response and provider outage.
5. Measure latency percentiles and error rate by route and client version.
6. Retest remediation and check logging redaction.

## Test evidence and acceptance

Record build, task, test accounts, environment, expected/actual result, impact, owner and comparable retest. Do not claim a test passed when it has not run. Use synthetic records and authorized environments.

## Primary sources

- [OpenTelemetry](https://opentelemetry.io/)
- [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)

**Scope:** educational procedure; verify current provider policies and local obligations before deployment.
