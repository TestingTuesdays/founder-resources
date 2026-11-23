---
name: test-data-management
description: Run a repeatable founder quality review for synthetic test data, fixtures and environment isolation.
---

# Synthetic test data, fixtures and environment isolation — reusable skill

[← Skills](../README.md) · [Guide](../../docs/test-data-management.md)

## Goal

Produce evidence-backed release findings without inventing test results.

## Inputs

Product/build identifier, owner, target audience, safe test accounts, representative devices and applicable primary documentation.

## Procedure

1. Use fictional users with different roles, locales, devices and organization memberships.
2. Seed and reset data deterministically before every critical test.
3. Ensure staging email/SMS and payment integrations cannot contact real customers.
4. Exercise malformed, duplicate, null, long and Unicode values.
5. Check test account cleanup and retention.
6. Rank findings by impact and assign fix owners.
7. Repeat failed scenarios on the deployed fix and record changed outcome.

## Output

Versioned scenario matrix, expected/actual observations, redacted evidence, severity, fix owner and retest status.

## Safety

Use only authorized environments and synthetic data. Never publish private participant information, production credentials or billing records. Manual and specialist review remains necessary for high-impact claims.
