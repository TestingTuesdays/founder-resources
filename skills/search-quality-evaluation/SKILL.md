---
name: search-quality-evaluation
description: Evaluate product search and relevance for founder production quality and safe release decisions.
---

# Evaluate product search and relevance

[← Skills index](../README.md) · [Topic guidance](../../docs/search-recommendations.md)

## Goal

Convert an overlooked production risk into a repeatable test with observable results.

## Required inputs

An authorized staging/product environment, synthetic accounts, a named owner, expected outcomes and relevant platform/provider documentation. Use real end users only with informed consent.

## Step-by-step procedure

1. Create a dataset of realistic queries, synonyms, typos and intended results.
2. Test empty and filtered result UX.
3. Check access controls on private or cross-tenant search hits.
4. Measure relevant results rather than only search response time.
5. Verify stale index after rename/delete and localization.
6. File relevance and permission failures with examples and retest.

## Evidence and exit criteria

For every scenario capture version/build, environment, expected and actual result, redacted evidence, severity, owner, fix link and comparable retest. A successful command, an unexecuted checklist or a simulated answer is **not** a passing product test.

## Safety boundaries

Never run disruptive security, load or failure-injection actions on systems without explicit permission. Keep credentials, billing identities, participant recordings and sensitive records out of public reports. Seek qualified legal/domain review for high-impact or regulated flows.

[Bug report template](../../templates/bug-report.md) · [Test case template](../../templates/test-case.md) · [Retest](../../templates/retest.md).
