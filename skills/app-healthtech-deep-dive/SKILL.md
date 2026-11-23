---
name: app-healthtech-deep-dive
description: Run scenario-driven quality assurance for health and care with Kenya-specific considerations.
---

# Health and care — deep-dive testing skill

[← Skills](../README.md) · [Detailed app playbook](../../app-types/healthtech.md)

## Inputs

Versioned app, permitted sandbox, two fictional user identities, realistic target task, device/network matrix, current provider and sector guidance, test owner.

## Procedure

1. Define primary journey and observable success criterion.
2. Seed synthetic records and isolate user permissions.
3. Run the normal flow and capture expected versus actual result.
4. Execute the authorization/replay case: Given two synthetic patients, when a caregiver opens a shared link for another patient, then server authorization denies the request.
5. Execute the concurrency/offline case: Given offline notes for two patients, when reconnecting and syncing, then notes retain patient identity and conflict resolution is visible.
6. Execute the safety/truth case: Given a safety-critical symptom entry, when the system cannot provide reliable guidance, then it clearly directs to appropriate clinical/emergency support rather than fabricating a diagnosis.
7. Validate accessible recovery and relevant Kenyan locale/payment behavior.
8. Rank findings by harm and assign fixes; retest after deployment.

## Required output

A scenario matrix with actual evidence, owner, build and comparable retest. Explicitly distinguish unrun checks from passed checks. Escalate regulated, safety or legal questions for qualified review.

## Safety

Never expose real personal information, live payment credentials or unauthorized systems.
