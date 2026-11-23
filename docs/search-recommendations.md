# Search, recommendations & information retrieval

[← Founder library](../README.md) · [Release readiness](release-readiness.md) · [Test-case template](../templates/test-case.md)

## When to use

Consumer apps, marketplaces, directories, knowledge bases and AI search.

## Most common mistake

Only testing searches that match exact spelling and ignoring zero-result states.

## Recommended practice

Measure relevance on a representative query set, document synonyms and filtering, and protect private records.

## Practical scenarios

1. **Typo and synonym.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
2. **multiple locales.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
3. **filters zero results.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
4. **permissions on search index.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
5. **ranking instability.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
6. **pagination.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
7. **stale index after deletion..** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.

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
| [Elasticsearch docs](https://www.elastic.co/guide/) | Documentation or diagnostic tool |
| [Algolia docs](https://www.algolia.com/doc/) | Documentation or diagnostic tool |
| [Meilisearch docs](https://www.meilisearch.com/docs) | Documentation or diagnostic tool |
| [OpenSearch docs](https://opensearch.org/docs/) | Documentation or diagnostic tool |

## Deliverable

A versioned test matrix, documented failures, assigned owners and evidence-backed retest. Tool availability, provider support and regulatory expectations can change; confirm them for your actual jurisdiction.

_Last curated: 2026-11-23._
