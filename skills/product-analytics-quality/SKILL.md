---
name: product-analytics-quality
description: Run a repeatable founder quality review for product analytics taxonomy and data-quality testing.
---

# Product analytics taxonomy and data-quality testing — reusable skill

[← Skills](../README.md) · [Guide](../../docs/product-analytics-quality.md)

## Goal

Produce evidence-backed release findings without inventing test results.

## Inputs

Product/build identifier, owner, target audience, safe test accounts, representative devices and applicable primary documentation.

## Procedure

1. Create an event dictionary with owner and trigger.
2. Verify one logical event per user action.
3. Check anonymous-to-authenticated identity transitions.
4. Reconcile funnel denominators with backend facts.
5. Test consent withdrawal, deleted users and data retention.
6. Rank findings by impact and assign fix owners.
7. Repeat failed scenarios on the deployed fix and record changed outcome.

## Output

Versioned scenario matrix, expected/actual observations, redacted evidence, severity, fix owner and retest status.

## Safety

Use only authorized environments and synthetic data. Never publish private participant information, production credentials or billing records. Manual and specialist review remains necessary for high-impact claims.
