---
name: app-agritech-deep-dive
description: Run scenario-driven quality assurance for agriculture and farmer services with Kenya-specific considerations.
---

# Agriculture and farmer services — deep-dive testing skill

[← Skills](../README.md) · [Detailed app playbook](../../app-types/agritech.md)

## Inputs

Versioned app, permitted sandbox, two fictional user identities, realistic target task, device/network matrix, current provider and sector guidance, test owner.

## Procedure

1. Define primary journey and observable success criterion.
2. Seed synthetic records and isolate user permissions.
3. Run the normal flow and capture expected versus actual result.
4. Execute the authorization/replay case: Given a weather advisory older than its supported validity, when displayed, then timestamp and uncertainty are prominent.
5. Execute the concurrency/offline case: Given a farmer enters kilograms, when converting units and prices, then displayed amount matches the recorded contract and currency.
6. Execute the safety/truth case: Given offline field collection, when two agents sync edits, then conflicts are resolved without silently overwriting observations.
7. Validate accessible recovery and relevant Kenyan locale/payment behavior.
8. Rank findings by harm and assign fixes; retest after deployment.

## Required output

A scenario matrix with actual evidence, owner, build and comparable retest. Explicitly distinguish unrun checks from passed checks. Escalate regulated, safety or legal questions for qualified review.

## Safety

Never expose real personal information, live payment credentials or unauthorized systems.
