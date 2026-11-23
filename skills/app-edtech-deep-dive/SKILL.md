---
name: app-edtech-deep-dive
description: Run scenario-driven quality assurance for education and learning with Kenya-specific considerations.
---

# Education and learning — deep-dive testing skill

[← Skills](../README.md) · [Detailed app playbook](../../app-types/edtech.md)

## Inputs

Versioned app, permitted sandbox, two fictional user identities, realistic target task, device/network matrix, current provider and sector guidance, test owner.

## Procedure

1. Define primary journey and observable success criterion.
2. Seed synthetic records and isolate user permissions.
3. Run the normal flow and capture expected versus actual result.
4. Execute the authorization/replay case: Given parent A and child B in different households, when parent A requests child B progress, then server denies it.
5. Execute the concurrency/offline case: Given a learner on low-bandwidth Android, when connection drops during assignment, then progress is preserved and submission status is clear.
6. Execute the safety/truth case: Given an assessment with screen reader and large text, when the learner completes the task, then every prompt and answer remains accessible.
7. Validate accessible recovery and relevant Kenyan locale/payment behavior.
8. Rank findings by harm and assign fixes; retest after deployment.

## Required output

A scenario matrix with actual evidence, owner, build and comparable retest. Explicitly distinguish unrun checks from passed checks. Escalate regulated, safety or legal questions for qualified review.

## Safety

Never expose real personal information, live payment credentials or unauthorized systems.
