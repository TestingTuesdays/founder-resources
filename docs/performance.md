# Performance, reliability & observability

[← Resource home](../README.md) · [Test catalog](test-case-catalog.md) · [Report a bug](../templates/bug-report.md)

## Why this matters

Keep the product responsive and recoverable under realistic devices, networks and load.

## Typical founder mistakes

- Testing only on fast laptops and office Wi-Fi
- Optimizing a single synthetic score instead of real experience
- Launching with no production alerts or rollback owner
- Having backups without ever testing restore

## Run these tests

1. **Mobile slow-network first load and checkout.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
2. **p95 endpoint latency with representative concurrency.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
3. **Database connection loss and reconnect.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
4. **Retry a failed background job without duplication.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
5. **Restore backed-up data to a controlled environment.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
6. **Roll back a bad release and check user state.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.

## Recommended workflow

Baseline Core Web Vitals (LCP, INP, CLS) for web and crash/ANR metrics on mobile; track p50/p95 latency and task success. Introduce realistic failures in controlled environments. Define thresholds with owners and release stop conditions.

## Tools and official references

| Resource | Use it for |
| --- | --- |
| [PageSpeed Insights](https://pagespeed.web.dev/) | Web performance field/lab insights |
| [WebPageTest](https://www.webpagetest.org/) | Network and waterfall diagnostics |
| [Chrome DevTools](https://developer.chrome.com/docs/devtools/) | CPU, network and memory |
| [k6](https://grafana.com/oss/k6/) | Load tests |
| [Locust](https://locust.io/) | Python load scenarios |
| [OpenTelemetry](https://opentelemetry.io/) | Portable tracing/metrics |
| [Grafana](https://grafana.com/) | Observability |
| [Sentry](https://sentry.io/) | Error monitoring |
| [Better Stack](https://betterstack.com/) | Incident monitoring |

## Do / don't

**Do:** test with representative people and devices, capture non-sensitive evidence, verify failure/recovery, assign ownership and retest the shipped fix.

**Don't:** rely solely on tool scores, copy unverified claims from a vendor, expose customer data, or call an unobserved outcome a passed test.

## Session deliverable

Bring one specific workflow, a safe build/test account, two or more reproducible observations, a severity-ranked fix list, and an agreed follow-up. [Use the session template](../templates/usability-session.md) and [retest sheet](../templates/retest.md).

_Last reviewed: 2026-11-23. Prices, support and platform rules may change._
