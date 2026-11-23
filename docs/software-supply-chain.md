# Dependency, license & software supply-chain assurance

[← Founder library](../README.md) · [Release readiness](release-readiness.md) · [Test-case template](../templates/test-case.md)

## When to use

Open-source-consuming teams and AI-assisted codebases.

## Most common mistake

Copying dependencies or generated code without checking license, maintenance or provenance.

## Recommended practice

Use dependency review, lockfiles, license inventory, secret scanning and trusted release artifacts.

## Practical scenarios

1. **Known vulnerable dependency.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
2. **unpinned CI action.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
3. **malicious package test.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
4. **revoked token.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
5. **license conflict.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
6. **provenance check.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
7. **signed build artifact..** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.

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
| [OpenSSF Scorecard](https://scorecard.dev/) | Documentation or diagnostic tool |
| [OSV](https://osv.dev/) | Documentation or diagnostic tool |
| [GitHub dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review) | Documentation or diagnostic tool |
| [SLSA](https://slsa.dev/) | Documentation or diagnostic tool |
| [SPDX](https://spdx.dev/) | Documentation or diagnostic tool |

## Deliverable

A versioned test matrix, documented failures, assigned owners and evidence-backed retest. Tool availability, provider support and regulatory expectations can change; confirm them for your actual jurisdiction.

_Last curated: 2026-11-23._
