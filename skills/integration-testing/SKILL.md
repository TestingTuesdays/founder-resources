---
name: integration-testing
description: Verify API contracts, OAuth scopes and webhook delivery across third-party integrations.
---

# Integration and webhook testing

[← Skills](../README.md) · [API guide](../../docs/api-integrations.md)

## Required inputs

Integration contract, authorized staging environment, synthetic accounts, callbacks, expected side effects and error budgets.

## Runbook

1. Record permissions, webhook signing method, retries and delivery assumptions.
2. Test normal auth and expired/revoked credentials.
3. Exercise invalid signatures, duplicates and out-of-order events in sandbox.
4. Simulate rate limiting, provider outage and partial failure.
5. Verify idempotency, tenant isolation and no sensitive logs.
6. Reconcile final state, assign defects and retest.

## Output

Matrix of scenario, expected result, actual result, build, severity, owner and pass/fail. Never call external third-party APIs without authorization.
