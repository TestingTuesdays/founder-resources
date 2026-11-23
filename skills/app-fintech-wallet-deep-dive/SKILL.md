---
name: app-fintech-wallet-deep-dive
description: Run scenario-driven quality assurance for fintech wallet and lending with Kenya-specific considerations.
---

# Fintech wallet and lending — deep-dive testing skill

[← Skills](../README.md) · [Detailed app playbook](../../app-types/fintech-wallet.md)

## Inputs

Versioned app, permitted sandbox, two fictional user identities, realistic target task, device/network matrix, current provider and sector guidance, test owner.

## Procedure

1. Define primary journey and observable success criterion.
2. Seed synthetic records and isolate user permissions.
3. Run the normal flow and capture expected versus actual result.
4. Execute the authorization/replay case: Given a synthetic order with one pending STK request, when a success callback arrives twice, then exactly one ledger credit is posted and the provider reference remains unique.
5. Execute the concurrency/offline case: Given a customer wallet with insufficient funds, when two transfers race, then available balance never becomes negative and neither recipient is credited without corresponding debit.
6. Execute the safety/truth case: Given a delayed reversal after a paid state, when reconciliation runs, then the customer balance, invoice and audit trail reflect the reversal with an explicit reason.
7. Validate accessible recovery and relevant Kenyan locale/payment behavior.
8. Rank findings by harm and assign fixes; retest after deployment.

## Required output

A scenario matrix with actual evidence, owner, build and comparable retest. Explicitly distinguish unrun checks from passed checks. Escalate regulated, safety or legal questions for qualified review.

## Safety

Never expose real personal information, live payment credentials or unauthorized systems.
