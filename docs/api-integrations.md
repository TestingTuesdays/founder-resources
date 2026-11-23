# APIs, integrations & webhooks

[← Resource home](../README.md) · [Release checklist](release-readiness.md)

## Why founders should care

Third-party reliability depends on contracts, retries, scopes, and clear ownership.

## Common mistakes

- Assuming a successful demo or dashboard proves the experience works for all users.
- Ignoring errors, permission boundaries, mobile constraints and exceptional states.
- Launching without a responsible owner, observable outcome or fallback.
- Using vendor tooling without checking costs, data protection or real capabilities.

## Core test scenarios

1. **Expired/invalid OAuth token handled safely.** Record build/environment, expected vs actual, user impact and follow-up.
2. **Provider 429 and 500 errors retried with backoff where appropriate.** Record build/environment, expected vs actual, user impact and follow-up.
3. **Webhook signature invalid, duplicate or out of order.** Record build/environment, expected vs actual, user impact and follow-up.
4. **Integration disconnected and revoked permissions respected.** Record build/environment, expected vs actual, user impact and follow-up.
5. **API schema breaking change detected with contract test.** Record build/environment, expected vs actual, user impact and follow-up.
6. **Import/export handles partial failure and resumability.** Record build/environment, expected vs actual, user impact and follow-up.

## Practical workflow

1. Identify the most important user task and a measurable success criterion.
2. Use safe synthetic data and a representative device/locale/account.
3. Test the expected route **and** failure/recovery case; observe results, not assumptions.
4. Check privacy/security, accessibility and reliability considerations where relevant.
5. File a reproducible issue, assign an owner and retest after the deployed fix.

## Trusted tools and reference material

| Reference | What it helps with |
| --- | --- |
| [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) | API contracts |
| [Postman](https://www.postman.com/) | API collections |
| [Bruno](https://www.usebruno.com/) | Git-based API tests |
| [Pact](https://pact.io/) | Contract tests |
| [OWASP API Top 10](https://owasp.org/API-Security/) | API threats |

## Go/no-go consideration

Do not call this area ready if the core journey can cause loss of data, money, privacy or user access without a documented safe recovery path. Regulations and provider requirements change: review official documentation for your specific product and market.

_Last curated: 2026-11-23._
