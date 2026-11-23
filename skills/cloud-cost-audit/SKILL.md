---
name: cloud-cost-audit
description: Audit cloud billing and startup credit burn for founders developing and testing real products.
---

# Audit cloud billing and startup credit burn

[← All skills](../README.md) · [Practical guide](../../docs/finops-cloud-costs.md)

## Goal

Make a founder's testing action repeatable and independently verifiable.

## Required inputs

An authorized product/environment, versioned build, representative sample accounts, explicit pass/fail criterion, and appropriate privacy/research permissions.

## Procedure

1. Enumerate vendors, production/staging environments, paid seats and billing owners.
2. For each provider read usage, applied credits, expiring amounts and estimated next invoice.
3. Inspect automatic seat provisioning, per-seat charges and environment spend.
4. Set budgets, approvals and alerts; use current spend rather than maximum credit amount.
5. Forecast monthly post-credit spend and record three practical cuts.

## Done when

A confidential monthly cost ledger, alerts, approval owners and forecast. Never publish invoices or account identifiers.

## Restrictions

Do not state an outcome as passed until it was run. Use synthetic data for public examples and keep billing identifiers, participants' information, secrets and private accounts out of the open repository. Stop and escalate if the test could harm real customers or physical systems.

[Use a test case](../../templates/test-case.md) · [Report a bug](../../templates/bug-report.md) · [Verify a fix](../../templates/retest.md).
