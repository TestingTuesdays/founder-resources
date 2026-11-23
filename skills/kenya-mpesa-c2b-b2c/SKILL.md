---
name: kenya-mpesa-c2b-b2c
description: Perform an evidence-based Kenya-focused review of m-pesa c2b, b2c and payout workflow qa.
---

# M-Pesa C2B, B2C and payout workflow QA — reusable skill

[← Skills](../README.md) · [Detailed guide](../../kenya/integrations/mpesa-c2b-b2c.md)

## Inputs

Real business activity description, current official provider/regulator documents, synthetic accounts, approved sandbox and named reviewer.

## Procedure

1. Determine whether your business model needs collections, disbursements or both.
2. Verify production merchant, shortcode, limits and API availability directly with Safaricom or PSP.
3. Model callback, validation, confirmation and transaction reconciliation separately.
4. Reject duplicate C2B events and reconcile unmatched payments.
5. Restrict B2C payout permissions, approvals, destination edits and limits.
6. Simulate payout failures and reversals with fictional accounts.
7. Reconcile provider statement, internal ledger and customer status.

## Done when

A completed scenario matrix documents actual behavior, risk, owner, fix and comparable retest. Record any licensing, merchant onboarding or tax decision as **unverified** until confirmed with the competent source.

## Safety

Never use real customer records, production secrets or real money in open testing. Do not confuse a documented plan with an executed integration.
