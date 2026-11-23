---
name: app-energy-water-iot-deep-dive
description: Run scenario-driven quality assurance for water and energy utilities with Kenya-specific considerations.
---

# Water and energy utilities — deep-dive testing skill

[← Skills](../README.md) · [Detailed app playbook](../../app-types/energy-water-iot.md)

## Inputs

Versioned app, permitted sandbox, two fictional user identities, realistic target task, device/network matrix, current provider and sector guidance, test owner.

## Procedure

1. Define primary journey and observable success criterion.
2. Seed synthetic records and isolate user permissions.
3. Run the normal flow and capture expected versus actual result.
4. Execute the authorization/replay case: Given a meter transmits the same reading twice, when ingestion runs, then usage is counted once and raw events remain auditable.
5. Execute the concurrency/offline case: Given a meter is offline for 48 hours, when restored, then missing intervals and estimated usage are visibly distinguished.
6. Execute the safety/truth case: Given a technician account is revoked, when it sends a configuration change, then device/backend rejects it.
7. Validate accessible recovery and relevant Kenyan locale/payment behavior.
8. Rank findings by harm and assign fixes; retest after deployment.

## Required output

A scenario matrix with actual evidence, owner, build and comparable retest. Explicitly distinguish unrun checks from passed checks. Escalate regulated, safety or legal questions for qualified review.

## Safety

Never expose real personal information, live payment credentials or unauthorized systems.
