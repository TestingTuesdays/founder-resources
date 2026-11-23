---
name: saas-release
description: Check identity, organizations, billing and operations before launch.
---

# SaaS release verification

[← Skills](../README.md) · [Topic guide](../../docs/saas.md)

## Objective

Check identity, organizations, billing and operations before launch.

## Required inputs

Staging app, synthetic users across two tenants, billing sandbox, rollback plan.

## Procedure

1. Test signup, reset, invite, role changes and team switching.
2. Verify cross-tenant server authorization, exports and links.
3. Simulate billing success, decline, duplicate webhooks, cancellation and trial expiry.
4. Check deletion, support, logs, backup restore and monitoring.
5. Review P0/P1 and rollback readiness.
6. Smoke test post-deploy and record go/no-go.

## Done when

Release gate with evidence, owner, decision and monitoring window.

## Safety and evidence

Use permissioned systems and synthetic data. Obtain research consent where applicable, redact personal information, preserve actual vs expected outcomes, and never state a check passed without running it. Human review remains necessary for high-risk conclusions.

## Copyable records

[Bug report](../../templates/bug-report.md) · [Testing session](../../templates/usability-session.md) · [Retest](../../templates/retest.md).
