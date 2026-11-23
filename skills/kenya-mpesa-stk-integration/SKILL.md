---
name: kenya-mpesa-stk-integration
description: Perform an evidence-based Kenya-focused review of m-pesa stk push implementation and failure-state design.
---

# M-Pesa STK Push implementation and failure-state design — reusable skill

[← Skills](../README.md) · [Detailed guide](../../kenya/integrations/mpesa-stk-integration.md)

## Inputs

Real business activity description, current official provider/regulator documents, synthetic accounts, approved sandbox and named reviewer.

## Procedure

1. Register an authorized Daraja sandbox app and review current provider API documentation.
2. Store consumer-facing order as pending before requesting STK push.
3. Use server-held credentials and correlate provider checkout/request IDs to one internal order.
4. Validate callback origin/shape as supported; independently query status or reconcile when missing.
5. Apply idempotent ledger transition, never rely on browser redirect or client status.
6. Handle canceled, timed-out, duplicated and late callbacks without double entitlement.
7. Reconcile refunds/reversals and keep phone numbers out of public logs.

## Done when

A completed scenario matrix documents actual behavior, risk, owner, fix and comparable retest. Record any licensing, merchant onboarding or tax decision as **unverified** until confirmed with the competent source.

## Safety

Never use real customer records, production secrets or real money in open testing. Do not confuse a documented plan with an executed integration.
