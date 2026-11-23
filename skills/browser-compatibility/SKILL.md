---
name: browser-compatibility
description: Run a repeatable founder quality review for browser, device and os compatibility.
---

# Browser, device and OS compatibility — reusable skill

[← Skills](../README.md) · [Guide](../../docs/browser-compatibility.md)

## Goal

Produce evidence-backed release findings without inventing test results.

## Inputs

Product/build identifier, owner, target audience, safe test accounts, representative devices and applicable primary documentation.

## Procedure

1. Cover latest and representative older browsers based on actual audience.
2. Check responsive viewport, zoom, orientation and virtual keyboard.
3. Test permissions, downloads, file pickers, clipboard and deep links.
4. Verify progressive enhancement when advanced APIs are unavailable.
5. Record unsupported browsers and graceful fallback.
6. Rank findings by impact and assign fix owners.
7. Repeat failed scenarios on the deployed fix and record changed outcome.

## Output

Versioned scenario matrix, expected/actual observations, redacted evidence, severity, fix owner and retest status.

## Safety

Use only authorized environments and synthetic data. Never publish private participant information, production credentials or billing records. Manual and specialist review remains necessary for high-impact claims.
