# QA & automated testing

[← Resource home](../README.md) · [Test catalog](test-case-catalog.md) · [Report a bug](../templates/bug-report.md)

## Why this matters

Prevent regressions across code, APIs and critical end-to-end journeys.

## Typical founder mistakes

- Only testing happy paths
- Making every test a brittle end-to-end test
- Hiding flaky checks and merging red builds
- Assuming a coverage percentage implies business correctness

## Run these tests

1. **Unit tests for validation, formatting and business rules.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
2. **API rejects missing and malformed input with safe errors.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
3. **Browser journey: signup → core action → expected result.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
4. **Session expiry during submit preserves data safely.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
5. **Duplicate API request creates one logical operation.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
6. **Previous production bug is covered by a regression test.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.

## Recommended workflow

Use unit checks for business logic, integration/contract checks for services, a few high-value end-to-end journeys and exploratory testing for unknown risks. Keep test data synthetic and deterministic. On every pull request run build, type checks, quick tests and secrets scanning.

## Tools and official references

| Resource | Use it for |
| --- | --- |
| [Playwright](https://playwright.dev/) | Cross-browser automation and traces |
| [Cypress](https://www.cypress.io/) | Browser-oriented testing |
| [Vitest](https://vitest.dev/) | JS/TS unit tests |
| [Testing Library](https://testing-library.com/) | Accessible UI interaction tests |
| [Postman](https://www.postman.com/) | API tests |
| [Bruno](https://www.usebruno.com/) | Git-friendly API collections |
| [Pact](https://pact.io/) | Service contract testing |
| [GitHub Actions](https://docs.github.com/en/actions) | Continuous integration |

## Do / don't

**Do:** test with representative people and devices, capture non-sensitive evidence, verify failure/recovery, assign ownership and retest the shipped fix.

**Don't:** rely solely on tool scores, copy unverified claims from a vendor, expose customer data, or call an unobserved outcome a passed test.

## Session deliverable

Bring one specific workflow, a safe build/test account, two or more reproducible observations, a severity-ranked fix list, and an agreed follow-up. [Use the session template](../templates/usability-session.md) and [retest sheet](../templates/retest.md).

_Last reviewed: 2026-11-23. Prices, support and platform rules may change._
