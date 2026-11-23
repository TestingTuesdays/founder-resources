---
name: app-ticketing-events-deep-dive
description: Run scenario-driven quality assurance for events and ticketing with Kenya-specific considerations.
---

# Events and ticketing — deep-dive testing skill

[← Skills](../README.md) · [Detailed app playbook](../../app-types/ticketing-events.md)

## Inputs

Versioned app, permitted sandbox, two fictional user identities, realistic target task, device/network matrix, current provider and sector guidance, test owner.

## Procedure

1. Define primary journey and observable success criterion.
2. Seed synthetic records and isolate user permissions.
3. Run the normal flow and capture expected versus actual result.
4. Execute the authorization/replay case: Given one seat and two simultaneous checkout attempts, when both submit, then only one reservation can be confirmed.
5. Execute the concurrency/offline case: Given a QR ticket already scanned on another offline gate, when syncing, then duplicate detection and dispute workflow are explicit.
6. Execute the safety/truth case: Given an M-Pesa payment pending, when gate staff search ticket, then status cannot be falsely represented as paid.
7. Validate accessible recovery and relevant Kenyan locale/payment behavior.
8. Rank findings by harm and assign fixes; retest after deployment.

## Required output

A scenario matrix with actual evidence, owner, build and comparable retest. Explicitly distinguish unrun checks from passed checks. Escalate regulated, safety or legal questions for qualified review.

## Safety

Never expose real personal information, live payment credentials or unauthorized systems.
