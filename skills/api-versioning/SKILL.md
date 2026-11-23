---
name: api-versioning
description: Run a repeatable founder quality review for api compatibility, deprecation and client upgrades.
---

# API compatibility, deprecation and client upgrades — reusable skill

[← Skills](../README.md) · [Guide](../../docs/api-versioning.md)

## Goal

Produce evidence-backed release findings without inventing test results.

## Inputs

Product/build identifier, owner, target audience, safe test accounts, representative devices and applicable primary documentation.

## Procedure

1. Inventory active client versions and API contracts.
2. Test old and new clients against a staged server.
3. Use explicit deprecation windows and truthful migration instructions.
4. Verify pagination, error schemas, nullable fields and backward-compatible additions.
5. Test rollback after schema and API deployment.
6. Rank findings by impact and assign fix owners.
7. Repeat failed scenarios on the deployed fix and record changed outcome.

## Output

Versioned scenario matrix, expected/actual observations, redacted evidence, severity, fix owner and retest status.

## Safety

Use only authorized environments and synthetic data. Never publish private participant information, production credentials or billing records. Manual and specialist review remains necessary for high-impact claims.
