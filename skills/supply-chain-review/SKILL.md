---
name: supply-chain-review
description: Review open-source dependency and build provenance for founder production quality and safe release decisions.
---

# Review open-source dependency and build provenance

[← Skills index](../README.md) · [Topic guidance](../../docs/software-supply-chain.md)

## Goal

Convert an overlooked production risk into a repeatable test with observable results.

## Required inputs

An authorized staging/product environment, synthetic accounts, a named owner, expected outcomes and relevant platform/provider documentation. Use real end users only with informed consent.

## Step-by-step procedure

1. Inventory direct and transitive dependencies and licenses.
2. Check advisories and maintenance signals with official ecosystem sources.
3. Review lockfile changes and suspicious lifecycle scripts.
4. Confirm no secrets in dependencies, build logs or release artifacts.
5. Review third-party CI actions and provenance where available.
6. File actionable remediation and recheck build after updates.

## Evidence and exit criteria

For every scenario capture version/build, environment, expected and actual result, redacted evidence, severity, owner, fix link and comparable retest. A successful command, an unexecuted checklist or a simulated answer is **not** a passing product test.

## Safety boundaries

Never run disruptive security, load or failure-injection actions on systems without explicit permission. Keep credentials, billing identities, participant recordings and sensitive records out of public reports. Seek qualified legal/domain review for high-impact or regulated flows.

[Bug report template](../../templates/bug-report.md) · [Test case template](../../templates/test-case.md) · [Retest](../../templates/retest.md).
