# Resilience testing & dependency failures

[← Founder library](../README.md) · [Release readiness](release-readiness.md) · [Test-case template](../templates/test-case.md)

## When to use

SaaS products with queues, scheduled jobs, payment processors or multiple services.

## Most common mistake

Treating graceful degradation as an afterthought and testing outages only in production.

## Recommended practice

Define recovery objectives, error budgets and explicit circuit-breaker/fallback behavior.

## Practical scenarios

1. **Third-party timeout.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
2. **rate limit.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
3. **DNS failure.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
4. **queue backlog.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
5. **job replay.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
6. **service partial outage.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
7. **stale cache.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
8. **recovery after failover..** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.

## Founder workflow

1. Identify the primary user task, critical failure, and who will be impacted.
2. Prepare a safe sandbox, representative device/network and synthetic accounts.
3. Test normal behavior, rejection and partial failure independently.
4. Compare actual observation to documented provider or product promises.
5. Prioritize privacy, monetary, safety and blocked core-task defects.
6. Ship a reversible fix, observe the release, and retest the original task.

## Tools and primary references

| Resource | Scope |
| --- | --- |
| [Google SRE workbook](https://sre.google/workbook/table-of-contents/) | Documentation or diagnostic tool |
| [OpenTelemetry](https://opentelemetry.io/) | Documentation or diagnostic tool |
| [k6](https://grafana.com/oss/k6/) | Documentation or diagnostic tool |
| [Toxiproxy](https://github.com/Shopify/toxiproxy) | Documentation or diagnostic tool |

## Deliverable

A versioned test matrix, documented failures, assigned owners and evidence-backed retest. Tool availability, provider support and regulatory expectations can change; confirm them for your actual jurisdiction.

_Last curated: 2026-11-23._
