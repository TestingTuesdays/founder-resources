---
name: observability-privacy
description: Run a repeatable founder quality review for privacy-safe logging, tracing and analytics instrumentation.
---

# Privacy-safe logging, tracing and analytics instrumentation — reusable skill

[← Skills](../README.md) · [Guide](../../docs/observability-privacy.md)

## Goal

Produce evidence-backed release findings without inventing test results.

## Inputs

Product/build identifier, owner, target audience, safe test accounts, representative devices and applicable primary documentation.

## Procedure

1. Define event dictionary and redaction rules before collecting logs.
2. Test auth failures, payment failures and retries without logging credentials.
3. Ensure correlation IDs link requests without exposing user identity.
4. Check alert routing and ownership on controlled failures.
5. Verify retention, consent and deletion promises against actual telemetry.
6. Rank findings by impact and assign fix owners.
7. Repeat failed scenarios on the deployed fix and record changed outcome.

## Output

Versioned scenario matrix, expected/actual observations, redacted evidence, severity, fix owner and retest status.

## Safety

Use only authorized environments and synthetic data. Never publish private participant information, production credentials or billing records. Manual and specialist review remains necessary for high-impact claims.
