# Mobile SDK privacy & third-party tracking inventory

[← Founder library](../README.md) · [Release readiness](release-readiness.md) · [Test-case template](../templates/test-case.md)

## When to use

Apps integrating analytics, ads, attribution, payments and customer support SDKs.

## Most common mistake

Declaring only data collected by app code and forgetting data collected by third-party SDKs.

## Recommended practice

Inventory SDKs, data types, transmission destinations, consent triggers, retention and store declarations.

## Practical scenarios

1. **Fresh install traffic.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
2. **consent denied.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
3. **device identifier.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
4. **user deletion.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
5. **analytics opt-out.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
6. **SDK update.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
7. **Apple privacy manifests.** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.
8. **Play Data safety labels..** Record preconditions, the expected outcome, actual behavior, risk, owner and retest result.

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
| [Apple privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files) | Documentation or diagnostic tool |
| [Google Play Data safety](https://support.google.com/googleplay/android-developer/answer/10787469) | Documentation or diagnostic tool |
| [OWASP MASVS](https://mas.owasp.org/) | Documentation or diagnostic tool |

## Deliverable

A versioned test matrix, documented failures, assigned owners and evidence-backed retest. Tool availability, provider support and regulatory expectations can change; confirm them for your actual jurisdiction.

_Last curated: 2026-11-23._
